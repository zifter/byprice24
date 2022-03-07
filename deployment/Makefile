cluster-delete:
	$(info Delete kind cluster)
	kind delete cluster --name byprice24 || true

cluster-create:
	$(info Create kind cluster)
	kind create cluster -v 1 --config kind-config.yaml --wait 3m

cluster-pause:
	$(info Pause kind cluster for a while)
	docker pause byprice24-control-plane

cluster-unpause:
	$(info Pause kind cluster)
	docker unpause byprice24-control-plane

infra-load-images:
	$(info Load docker images for infrastucture)
	docker pull docker.io/bitnami/postgresql:11.10.0-debian-10-r83
	kind load docker-image --name byprice24 docker.io/bitnami/postgresql:11.10.0-debian-10-r83 || true

	docker pull docker.io/bitnami/redis:6.2.6-debian-10-r0
	kind load docker-image --name byprice24 docker.io/bitnami/redis:6.2.6-debian-10-r0 || true

	docker pull docker.io/bitnami/elasticsearch:7.16.2-debian-10-r0
	kind load docker-image --name byprice24 docker.io/bitnami/elasticsearch:7.16.2-debian-10-r0 || true

cluster-images:
	$(info List of loaded images into cluster)
	docker exec -it byprice24-control-plane crictl images

infra-install:
	$(info Install infra releases to k8s)
	helmfile -e local -l tier!=app sync --concurrency 1

###########
# BACKEND
backend-helm-install: IMAGE_TAG := test
backend-helm-install:
	$(info Install actual application to k8s)
	helmfile -e local -l side=backend sync --concurrency 1

backend-helm-uninstall:
	$(info Uninstall backend)
	helmfile -e local -l side=backend delete

backend-image-load: IMAGE_TAG := test
backend-image-load:
	$(info Load docker to kind cluster)
	kind load docker-image --name byprice24 zifter/byprice24-cms:${IMAGE_TAG}

###########
# FRONTEND
frontend-helm-install: IMAGE_TAG := test
frontend-helm-install:
	$(info Install frontend)
	helmfile -e local -l side=frontend sync --concurrency 1

frontend-helm-uninstall:
	$(info Uninstall frontend)
	helmfile -e local -l side=frontend delete

frontend-image-load: IMAGE_TAG := test
frontend-image-load:
	$(info Load docker to kind cluster)
	kind load docker-image --name byprice24 zifter/byprice24-site:${IMAGE_TAG}

helmfile-sync:
	$(info Sync all releases)
	helmfile -e local sync --concurrency 1

restart-deployments:
	$(info Restart deployment in order to use latest version of docker image)
	kubectl rollout restart deployment cms
	kubectl rollout restart deployment worker-crawler
	kubectl rollout restart deployment worker-etc

print-urls:
	$(info ===========================================================)
	$(info Site: 			http://localhost:1080/)
	$(info Admin: 			http://localhost:1080/admin/)
	$(info Grafana: 		http://localhost:1080/grafana (admin - admin))
	$(info Prometheus: 		http://localhost:1080/prometheus)
	$(info AlertManager: 	http://localhost:1080/alertmanager)
	$(info ===========================================================)

validate-local:
	$(info Validate helmfile for local environment)
	helmfile -e local build
	helmfile -e local lint
	helmfile -e local template

helmfile-prod: RELEASE_TAG := latest
validate-prod:
	$(info Validate helmfile for prod)
	make helmfile-prod ARGS=build
	make helmfile-prod ARGS=lint
	make helmfile-prod ARGS=template

helmfile-prod: ARGS := diff
helmfile-prod: RELEASE_TAG := latest
helmfile-prod:
	docker pull zifter/byprice24-cms:${RELEASE_TAG}
	docker pull zifter/byprice24-site:${RELEASE_TAG}
	export `cat .env | xargs` && \
	export RELEASE_TAG=${RELEASE_TAG} \
	export BACKEND_IMAGE_SHA256=`docker inspect --format='{{index .RepoDigests 0}}' zifter/byprice24-cms:${RELEASE_TAG} | cut -f 2 -d @` && \
	export FRONTEND_IMAGE_SHA256=`docker inspect --format='{{index .RepoDigests 0}}' zifter/byprice24-site:${RELEASE_TAG} | cut -f 2 -d @` && \
	helmfile -e prod ${ARGS}
