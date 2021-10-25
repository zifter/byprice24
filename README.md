# byprice24
## Contribute
### Setup
You need any kind of Linux system - the latest ubuntu will be great.

#### [Docker](https://www.docker.com/)
All deployment based on containers. Docker is simple to use at that moment.

#### [python3.9](https://www.python.org/downloads/release/python-390/)
It's guarantee that application is workig with that version.

#### [pycharm](https://www.jetbrains.com/ru-ru/pycharm/)
The best IDE for python developing.

#### pipenv
Pipenv is tool to working with virtual environment.
```bash
python3 -m pip install pipenv
```

#### helm
Package manager for kubernetes.
```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 && \
chmod 700 get_helm.sh && \
./get_helm.sh --version v3.6.3 \
&& rm -f ./get_helm.sh
```

#### helm diff plugin
Plugin for showing diff between releases.
```bash
helm plugin install https://github.com/databus23/helm-diff --version 3.1.3
```

#### helmfile
helmfile is tool for describing helm releases via files.
```bash
sudo wget "https://github.com/roboll/helmfile/releases/download/v0.140.0/helmfile_linux_amd64" -O /usr/bin/helmfile && sudo chmod +x /usr/bin/helmfile
```

#### kind
kind is a tool for running local Kubernetes clusters using Docker container “nodes”.

```bash
sudo wget "https://github.com/kubernetes-sigs/kind/releases/download/v0.11.1/kind-linux-amd64" -O /usr/bin/kind && sudo chmod +x /usr/bin/kind
```

#### Install git pre-commit hook
Используем библиотеку [pre-commit](https://pre-commit.com).

```bash
# install pre-commit
$ python3 -m pip install pre-commit
$ pre-commit --version

# install the git hook scripts
$ pre-commit install
```

### Run
All commands for controlling cluster is describing in Makefile.

```bash
# run cluster with prepared applications
$ make run-cluster
# install byprice24 application to cluster
$ make helmfile-sync-backend
```
## Deploy
### ScraperAPI
Proxy for scrabing
```bash
https://dashboard.scraperapi.com/dashboard
```
