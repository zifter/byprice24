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

cluster-images:
	$(info List of loaded images into cluster)
	docker exec -it byprice24-control-plane crictl images

infra-install:
	$(info Install infra releases to k8s)
	helmfile -l tier!=backend sync

backend-install: IMAGE_TAG := zifter/byprice24-cms:test
backend-install:
	$(info Install actual application to k9s)
	make build-image
	make load-image
	helmfile -l tier=backend sync
	make cms-init
	make print-urls

backend-uninstall:
	$(info Uninstall backend)
	helmfile -l tier=backend delete

backend-image-load: IMAGE_TAG := zifter/byprice24-cms:test
backend-image-load:
	$(info Load docker to kind cluster)
	kind load docker-image --name byprice24 ${IMAGE_TAG}

helmfile-sync:
	$(info Sync all releases)
	helmfile sync

restart-deployments:
	$(info Restart deployment in order to use latest version of docker image)
	kubectl rollout restart deployment cms
	kubectl rollout restart deployment worker-crawler
	kubectl rollout restart deployment worker-etc

print-urls:
	$(info ===========================================================)
	$(info CMS: 			http://localhost:1080/)
	$(info Admin: 			http://localhost:1080/admin/)
	$(info Grafana: 		http://localhost:1080/grafana (admin - admin))
	$(info Prometheus: 		http://localhost:1080/prometheus)
	$(info AlertManager: 	http://localhost:1080/alertmanager)
	$(info ===========================================================)

validate:
	$(info Validate helmfile)
	helmfile build
	helmfile lint
	helmfile -e prod build
	helmfile -e prod lint
	helmfile template
