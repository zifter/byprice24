# Specific toolset installation
setup-pipenv:
	$(info Install pipenv)
	python3 -m pip install --upgrade pip setuptools wheel
	python3 -m pip install pipenv

setup-helm:
	$(info Install helm)
	curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 && \
	sudo chmod 700 get_helm.sh && \
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
	sudo wget "https://github.com/roboll/helmfile/releases/download/v0.140.0/helmfile_linux_amd64" -O /usr/local/bin/helmfile \
	&& sudo chmod +x /usr/local/bin/helmfile

setup-helmfile-mac:
	$(info Install helmfile mac)
	brew install helmfile

setup-kind:
	$(info Install kind)
	sudo wget "https://github.com/kubernetes-sigs/kind/releases/download/v0.12.0/kind-linux-amd64" -O /usr/local/bin/kind \
	&& sudo chmod +x /usr/local/bin/kind

setup-kind-mac:
	$(info Install kind mac)
	brew install kind

setup-pre-commit-hook:
	$(info Install pre commit hook)
	python3 -m pip install pre-commit==2.15.0
	pre-commit install

verify:
	$(info Verify that everything is ok)
	pre-commit --version
	helm version
	helmfile --version
	pyenv --version
	terraform -version
