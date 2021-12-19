cluster-delete:
	$(info Delete kind cluster)
	kind delete cluster --name byprice24 || true

cluster-create:
	$(info Create kind cluster)
	kind create cluster -v 1 --config kind-config.yaml

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

	docker pull docker.io/bitnami/elasticsearch:7.15.2-debian-10-r10
	kind load docker-image --name byprice24 docker.io/bitnami/elasticsearch:7.15.2-debian-10-r10 || true

cluster-images:
	$(info List of loaded images into cluster)
	docker exec -it byprice24-control-plane crictl images

infra-install:
	$(info Install infra releases to k8s)
	helmfile -e local -l tier!=app sync

###########
# BACKEND
backend-helm-install: IMAGE_TAG := zifter/byprice24-cms:test
backend-helm-install:
	$(info Install actual application to k8s)
	helmfile -e local -l side=backend sync

backend-helm-uninstall:
	$(info Uninstall backend)
	helmfile -e local -l side=backend delete

backend-image-load: IMAGE_TAG := zifter/byprice24-cms:test
backend-image-load:
	$(info Load docker to kind cluster)
	kind load docker-image --name byprice24 ${IMAGE_TAG}

###########
# FRONTEND
frontend-helm-install: IMAGE_TAG := zifter/byprice24-site:test
frontend-helm-install:
	$(info Install frontend)
	helmfile -e local -l side=frontend sync

frontend-helm-uninstall:
	$(info Uninstall frontend)
	helmfile -e local -l side=frontend delete

frontend-image-load: IMAGE_TAG := zifter/byprice24-site:test
frontend-image-load:
	$(info Load docker to kind cluster)
	kind load docker-image --name byprice24 ${IMAGE_TAG}

helmfile-sync:
	$(info Sync all releases)
	helmfile -e local sync

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

validate:
	$(info Validate helmfile for all environments)
	helmfile -e local build
	helmfile -e local lint
	helmfile -e local template
	helmfile -e prod build
	helmfile -e prod lint

helmfile-prod: ARGS := diff
helmfile-prod: BACKEND_IMAGE_TAG := zifter/byprice24-cms:latest
helmfile-prod: FRONTEND_IMAGE_TAG := zifter/byprice24-site:latest
helmfile-prod:
	docker pull ${BACKEND_IMAGE_TAG}
	docker pull ${FRONTEND_IMAGE_TAG}
	export `cat .env | xargs` && \
	export BACKEND_IMAGE_SHA256=`docker inspect --format='{{index .RepoDigests 0}}' ${BACKEND_IMAGE_TAG} | cut -f 2 -d @` && \
	export FRONTEND_IMAGE_SHA256=`docker inspect --format='{{index .RepoDigests 0}}' ${FRONTEND_IMAGE_TAG} | cut -f 2 -d @` && \
	kubectl config current-context && \
	helmfile -e prod ${ARGS}
