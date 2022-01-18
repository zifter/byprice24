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
	cd backend && make pipenv-install

# MacOS Setup toolset for contributing
setup-toolset-mac:
	cd contributing && make setup-pipenv
	cd contributing && make setup-helm-mac
	cd contributing && make setup-helm-diff-plugin
	cd contributing && make setup-helmfile-mac
	cd contributing && make setup-kind-mac
	cd contributing && make setup-pre-commit-hook
	cd backend && make pipenv-install

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
backend-image-update: IMAGE_TAG := zifter/byprice24-cms:test
backend-image-update:
	cd backend && make image-build
	cd deployment && make backend-image-load
	cd deployment && make restart-deployments

backend-image-publish: IMAGE_TAG := zifter/byprice24-cms:test
backend-image-publish: PUBLISH_IMAGE_TAG := zifter/byprice24-cms:latest
backend-image-publish:
	$(info Publish docker imgage $(PUBLISH_IMAGE_TAG))
	docker tag $(IMAGE_TAG) $(PUBLISH_IMAGE_TAG)
	docker push $(PUBLISH_IMAGE_TAG)

backend-install: IMAGE_TAG := zifter/byprice24-cms:test
backend-install:
	$(info Install actual application to k8s)
	cd backend && make image-build
	cd deployment && make backend-image-load
	cd deployment && make backend-helm-install
	cd backend && make cms-init
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
	cd deployment && make infra-install
	cd deployment && make print-urls

# Run cluster with full deployment
run-full-cluster:
	cd deployment && make cluster-delete
	cd deployment && make cluster-create
	make install-full-cluster

install-full-cluster:
	cd deployment && make infra-install
	make backend-install
	make frontend-install
	cd deployment && make print-urls
