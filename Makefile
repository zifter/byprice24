####################
# Linux Setup toolset for contributing
setup-toolset: setup-pipenv setup-helm setup-helm-diff-plugin setup-helmfile setup-kind setup-pre-commit-hook pipenv-install

# MacOS Setup toolset for contributing
setup-toolset-mac: setup-pipenv setup-helm-mac setup-helmfile-mac setup-kind-mac setup-pre-commit-hook \
 pipenv-install setup-helm-diff-plugin

setup-pipenv:
	$(info Install pipenv)
	python3 -m pip install pipenv

setup-helm:
	$(info Install helm)
	curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 && \
	chmod 700 get_helm.sh && \
	./get_helm.sh --version v3.6.3 \
	&& rm -f ./get_helm.sh

setup-helm-mac:
	$(info Install helm-mac)
	brew install helm

setup-helm-diff-plugin:
	$(info Install helm diff plugin)
	helm plugin uninstall diff || true
	helm plugin install https://github.com/databus23/helm-diff --version 3.1.3

setup-helmfile:
	$(info Install helmfile)
	sudo wget "https://github.com/roboll/helmfile/releases/download/v0.140.0/helmfile_linux_amd64" -O /usr/bin/helmfile \
	&& sudo chmod +x /usr/bin/helmfile

setup-helmfile-mac:
	$(info Install helmfile mac)
	brew install helmfile

setup-kind:
	$(info Install kind)
	sudo wget "https://github.com/kubernetes-sigs/kind/releases/download/v0.11.1/kind-linux-amd64" -O /usr/bin/kind \
	&& sudo chmod +x /usr/bin/kind

setup-kind-mac:
	$(info Install kind mac)
	brew install kind

setup-pre-commit-hook:
	$(info Install pre commit hook)
	python3 -m pip install pre-commit==2.15.0
	pre-commit install

pipenv-install:
	$(info Setup pipenv dependencies)
	pipenv install --dev


####################
# Image

# Build image of CMS
build-image: IMAGE_TAG := zifter/byprice24-cms:test
build-image:
	$(info Build docker image)
	docker build . -t $(IMAGE_TAG)

# Test Docker image
# We must be sure, that docker image is 100% correct
test-image: IMAGE_TAG := zifter/byprice24-cms:test
test-image: DJANGO_CONFIGURATION := Test
test-image:
	$(info Run tests for docker image)
	docker run $(IMAGE_TAG) python3 manage.py check --configuration=${DJANGO_CONFIGURATION}
	docker run $(IMAGE_TAG) /bin/bash -c "\
		pytest . --cov=. && \
		coverage report --include="*_tests.py" --rcfile=pytest.ini --fail-under=100 && \
		coverage report --include="*" --rcfile=pytest.ini --fail-under=90 \
		"

# Before publishing you must perform login to DockerHub
docker-login: DOCKER_USER ?= ""
docker-login: DOCKER_PASS ?= ""
docker-login:
	$(info Perform login to DockerHub)
	docker login -u $(DOCKER_USER) -p $(DOCKER_PASS)

# Publish DockerImage to latest tag
publish-image: IMAGE_TAG := zifter/byprice24-cms:test
publish-image: PUBLISH_IMAGE_TAG := zifter/byprice24-cms:latest
publish-image:
	$(info Publish docker imgage $(PUBLISH_IMAGE_TAG))
	docker tag $(IMAGE_TAG) $(PUBLISH_IMAGE_TAG)
	docker push $(PUBLISH_IMAGE_TAG)

#############
# Dev cluster

# Create kind cluster with kubernetes
delete-cluster:
	$(info Delete kind cluster)
	kind delete cluster --name byprice24 || true

# Delete kind cluster with kubernetes
create-cluster:
	$(info Create kind cluster)
	kind create cluster -v 1 --config kind-config.yaml

load-infra-images:
	$(info Load docker images for infrastucture)
	docker pull docker.io/bitnami/postgresql:11.10.0-debian-10-r83
	kind load docker-image --name byprice24 docker.io/bitnami/postgresql:11.10.0-debian-10-r83 || true

	docker pull docker.io/bitnami/redis:6.2.6-debian-10-r0
	kind load docker-image --name byprice24 docker.io/bitnami/redis:6.2.6-debian-10-r0 || true

pause-cluster:
	$(info Pause kind cluster)
	docker pause byprice24-control-plane

unpause-cluster:
	$(info Pause kind cluster)
	docker unpause byprice24-control-plane

cluster-images:
	docker exec -it byprice24-control-plane crictl images

# Install all helm releases
install-infra:
	$(info Install infra releases to k8s)
	helmfile -l tier!=backend sync

install-backend: IMAGE_TAG := zifter/byprice24-cms:test
install-backend:
	$(info Install actual application to k9s)
	make build-image
	make load-image
	helmfile -l tier=backend sync
	make cms-init
	make print-urls

helmfile-sync:
	$(info Sync releases)
	helmfile sync

print-urls:
	$(info ===========================================================)
	$(info CMS: 			http://localhost:1080/)
	$(info Admin: 			http://localhost:1080/admin/)
	$(info Grafana: 		http://localhost:1080/grafana (admin - admin))
	$(info Prometheus: 		http://localhost:1080/prometheus)
	$(info AlertManager: 	http://localhost:1080/alertmanager)
	$(info ===========================================================)

load-image: IMAGE_TAG := zifter/byprice24-cms:test
load-image:
	$(info Load docker to kind cluster)
	kind load docker-image --name byprice24 ${IMAGE_TAG}

restart-deployment:
	$(info Restart deployment in order to use latest version of docker image)
	kubectl rollout restart deployment cms
	kubectl rollout restart deployment worker-crawler
	kubectl rollout restart deployment worker-etc

# Run cluster from scratch for dev, without application
run-dev-cluster: delete-cluster create-cluster load-infra-images install-infra print-urls

# Run cluster with full deployment
run-full-cluster: delete-cluster create-cluster load-infra-images install-infra install-backend print-urls

# Update Docker Image in kind cluster
update-image: IMAGE_TAG := zifter/byprice24-cms:test
update-image: build-image load-image restart-deployment

###########
# Local Dev
pytest:
	$(info Run pytest)
	pipenv run pytest src --cov=src

test:
	$(info Run all necessary tests locally)
	pipenv run ./src/manage.py check --configuration=Test
	make pytest
	make coverage-report

coverage-report:
	pipenv run coverage report --include="src/**_tests.py" --rcfile=src/pytest.ini --fail-under=100
	pipenv run coverage report --include="src/*" --rcfile=src/pytest.ini --fail-under=90

open-coverage:
	make pytest
	pipenv run coverage html --rcfile=src/pytest.ini
	xdg-open htmlcov/index.html || open htmlcov/index.html

makemigrations:
	$(info Make migrations for all applications)
	pipenv run ./src/manage.py makemigrations crawler
	pipenv run ./src/manage.py makemigrations marketplace

collectstatic:
	$(info Collect static files)
	pipenv run ./src/manage.py collectstatic --noinput

migrate:
	make makemigrations
	$(info Run migration for database)
	pipenv run ./src/manage.py migrate

createuser:
	$(info Create test user in cms)
	pipenv run ./src/manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('root', '', '1234')"

load-fixtures:
	$(info Load fixtures to database)
	pipenv run ./src/manage.py loaddata fixtures/*.yaml

workers:
	$(info Load workes for all queues)
	pipenv run ./src/manage.py rqworker crawler-feed crawler-result

runserver:
	$(info Run server)
	pipenv run ./src/manage.py runserver 0.0.0.0:8080

cms-init: createuser load-fixtures
