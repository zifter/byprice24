# byprice24
## Contribute
### Setup
You need any kind of Linux system - the latest ubuntu will be great.

#### [Docker](https://www.docker.com/)
All deployment based on containers. Docker is simple to use at that moment.

#### [python3.10.0](https://www.python.org/downloads/release/python-3100/)
It's guarantee that application is workig with that version.

#### [pycharm](https://www.jetbrains.com/ru-ru/pycharm/)
The best IDE for python developing.

#### [Lens](https://k8slens.dev/)
The best IDE for k8s developing.

### Toolset
All toolset will be installed via make command:
```bash
make setup-toolset
```

#### pipenv
Pipenv is tool to working with virtual environment.

#### helm
Package manager for kubernetes.

#### helm diff plugin
Plugin for showing diff between releases.

#### helmfile
helmfile is tool for describing helm releases via files.

#### kind
kind is a tool for running local Kubernetes clusters using Docker container “nodes”.

#### Install git pre-commit hook
Используем библиотеку [pre-commit](https://pre-commit.com).

### Run
All commands for controlling cluster is describing in Makefile.

```bash
# run cluster with prepared applications
$ make run-dev-cluster
# run cluster with full setup
$ make run-full-cluster
# install byprice24 application to cluster
$ make helmfile-sync-backend
```

## Deploy
### ScraperAPI
Proxy for scrabing
```bash
https://dashboard.scraperapi.com/dashboard
```
