####################
# SETUP
####################
# Linux Setup toolset for contributing
setup-toolset:
	cd contributing && make setup-pipenv
	cd contributing && make setup-helm
	cd contributing && make setup-helm-diff-plugin
	cd contributing && make setup-helmfile
	cd contributing && make setup-kind
	cd contributing && make setup-pre-commit-hook
	make pipenv-install

# MacOS Setup toolset for contributing
setup-toolset-mac:
	cd contributing && make setup-pipenv
	cd contributing && make setup-helm-mac
	cd contributing && make setup-helm-diff-plugin
	cd contributing && make setup-helmfile-mac
	cd contributing && make setup-kind-mac
	cd contributing && make setup-pre-commit-hook
	make pipenv-install

setup-verify:
	cd contributing && make verify

######
# OTHER
# Before publishing you must perform login to DockerHub
docker-login: DOCKER_USER ?= ""
docker-login: DOCKER_PASS ?= ""
docker-login:
	$(info Perform login to DockerHub)
	docker login -u $(DOCKER_USER) -p $(DOCKER_PASS)

####################
# Backend Image
backend-image-build: IMAGE_TAG := zifter/byprice24-cms:test
backend-image-build:
	$(info Build docker image for backend - CMS and workes)
	docker build . -t $(IMAGE_TAG)

# Test Docker image
backend-image-test: IMAGE_TAG := zifter/byprice24-cms:test
backend-image-test: DJANGO_CONFIGURATION := Test
backend-image-test:
	$(info Run tests for docker image)
	docker run $(IMAGE_TAG) python3 manage.py check --configuration=${DJANGO_CONFIGURATION}
	docker run $(IMAGE_TAG) /bin/bash -c "\
		pytest . --cov=. && \
		coverage report --include="*tests.py" --rcfile=pytest.ini --fail-under=100 && \
		coverage report --include="*" --rcfile=pytest.ini --fail-under=93 \
		"

backend-image-publish: IMAGE_TAG := zifter/byprice24-cms:test
backend-image-publish: PUBLISH_IMAGE_TAG := zifter/byprice24-cms:latest
backend-image-publish:
	$(info Publish docker imgage $(PUBLISH_IMAGE_TAG))
	docker tag $(IMAGE_TAG) $(PUBLISH_IMAGE_TAG)
	docker push $(PUBLISH_IMAGE_TAG)

backend-image-update: IMAGE_TAG := zifter/byprice24-cms:test
backend-image-update:
	make backend-image-build
	cd deployment && make backend-image-load
	cd deployment && make restart-deployments

backend-image-migrations-check: IMAGE_TAG := zifter/byprice24-cms:test
backend-image-migrations-check:
	$(info Check if migrations is needed)
	docker run $(IMAGE_TAG) python3 manage.py makemigrations --check --dry-run

backend-install: IMAGE_TAG := zifter/byprice24-cms:test
backend-install:
	$(info Install actual application to k8s)
	make backend-image-build
	cd deployment && make backend-image-load
	cd deployment && make backend-helm-install
	make cms-init
	cd deployment && make print-urls

#############
# Frontend cluster
frontend-image-build: IMAGE_TAG := zifter/byprice24-site:test
frontend-image-build:
	$(info Build docker image for frontend - site)
	cd frontend && make image-build

frontend-image-publish: IMAGE_TAG := zifter/byprice24-site:test
frontend-image-publish: PUBLISH_IMAGE_TAG := zifter/byprice24-site:latest
frontend-image-publish:
	$(info Publish docker imgage $(PUBLISH_IMAGE_TAG))
	docker tag $(IMAGE_TAG) $(PUBLISH_IMAGE_TAG)
	docker push $(PUBLISH_IMAGE_TAG)

frontend-image-update: IMAGE_TAG := zifter/byprice24-site:test
frontend-image-update:
	make frontend-image-build
	cd deployment && make frontend-image-load
	cd deployment && make restart-deployments

frontend-install: IMAGE_TAG := zifter/byprice24-site:test
frontend-install:
	$(info Install actual application to k8s)
	make frontend-image-build
	cd deployment && make frontend-image-load
	cd deployment && make frontend-helm-install
	cd deployment && make print-urls

#############
# Dev cluster
# Run cluster from scratch for dev, without application
run-dev-cluster:
	cd deployment && make cluster-delete
	cd deployment && make cluster-create
	cd deployment && make infra-load-images
	cd deployment && make infra-install
	cd deployment && make print-urls

# Run cluster with full deployment
run-full-cluster:
	cd deployment && make cluster-delete
	cd deployment && make cluster-create
	cd deployment && make infra-load-images
	cd deployment && make infra-install
	make backend-install
	make frontend-install
	cd deployment && make print-urls

###########
# Backend Local Dev
pipenv-install:
	$(info Setup pipenv dependencies)
	pipenv install --dev

pytest:
	$(info Run pytest)
	pipenv run pytest src --cov=src

test:
	$(info Run all necessary tests locally)
	pipenv run ./src/manage.py check --configuration=Test
	make pytest
	make coverage-report

coverage-report:
	pipenv run coverage report --include="src/**tests.py" --rcfile=src/pytest.ini --fail-under=100
	pipenv run coverage report --include="src/*" --rcfile=src/pytest.ini --fail-under=93

open-coverage:
	make pytest
	pipenv run coverage html --rcfile=src/pytest.ini
	xdg-open htmlcov/index.html || open htmlcov/index.html

makemigrations:
	$(info Make migrations for all applications)
	pipenv run ./src/manage.py makemigrations

migrations-check:
	$(info Check if migrations is needed)
	pipenv run ./src/manage.py makemigrations --check --dry-run

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
	pipenv run ./src/manage.py loaddata fixtures/prod/*.yaml

load-fixtures-test:
	$(info Load test fixtures to database)
	pipenv run ./src/manage.py loaddata fixtures/test/*.yaml

dump-fixtures-test:
	$(info Load test fixtures to database)
	pipenv run ./src/manage.py dumpdata marketplace --format yaml > ./fixtures/dump/marketplace.yaml

workers:
	$(info Load workes for all queues)
	pipenv run ./src/manage.py rqworker crawler-feed crawler-result

runserver:
	$(info Run server)
	pipenv run ./src/manage.py runserver 0.0.0.0:8080

cms-init: createuser load-fixtures
