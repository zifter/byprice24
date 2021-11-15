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
	docker run $(IMAGE_TAG) check --configuration=${DJANGO_CONFIGURATION}
	docker run $(IMAGE_TAG) test -p "*_test.py" --configuration=${DJANGO_CONFIGURATION}

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
	$(info Publis docker imgage $(PUBLISH_IMAGE_TAG))
	docker tag $(IMAGE_TAG) $(PUBLISH_IMAGE_TAG)
	docker push $(PUBLISH_IMAGE_TAG)

#############
# Dev cluster

# Create kind cluster with kubernetes
delete-cluster:
	$(info Delete kind cluster)
	kind delete cluster || true

# Delete kind cluster with kubernetes
create-cluster:
	$(info Create kind cluster)
	kind create cluster -v 1 --config kind-config.yaml

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
	$(info Grafana: 		http://localhost:1080/grafana (admin - admin))
	$(info Prometheus: 		http://localhost:1080/prometheus)
	$(info AlertManager: 	http://localhost:1080/alertmanager)
	$(info ===========================================================)

load-image: IMAGE_TAG := zifter/byprice24-cms:test
load-image:
	$(info Load docker to kind cluster)
	kind load docker-image ${IMAGE_TAG}

restart-deployment:
	$(info Restart deployment in order to use latest version of docker image)
	kubectl rollout restart deployment cms
	kubectl rollout restart deployment worker-crawler
	kubectl rollout restart deployment worker-etc

# Run cluster from scratch for dev, without application
run-dev-cluster: delete-cluster create-cluster install-infra print-urls

# Run cluster with full setup
run-full-cluster: delete-cluster create-cluster install-infra install-backend print-urls

# Update Docker Image in kind cluster
update-image: IMAGE_TAG := zifter/byprice24-cms:test
update-image: build-image load-image restart-deployment

###########
# Local Dev
test:
	$(info Run tests locally)
	pipenv run ./src/manage.py test -p "*_test.py" --configuration=Test
	pipenv run ./src/manage.py check --configuration=Test

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
