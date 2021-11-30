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

---

#### How to launch project in [pycharm](https://www.jetbrains.com/ru-ru/pycharm/):
I. Configure Python interpreter for the project:
   1. In the bottom of the pycharm press _interpreter settings_
   2. Press _Add interpreter_ in pop-up tab
   3. In a new tab press _Pipenv Environment_
   4. Configure as default and press _Ok_

II. Connect Python interpreter to the pycharm
   1. In the top of the pycharm press _Add configuration_
   2. In the bottom of a new opened tab you will see _fix django_, you should press this tab
   3. In a new tab select the path to settings file (in cms folder) and the path to manage.py file and press Ok
   4. Press OK

III. Press Run - _green arrow_

#### How to launch tests in [pycharm](https://www.jetbrains.com/ru-ru/pycharm/):
II. Connect Python interpreter to the pycharm pytests engine
   1. In the top open tab which we press before (_Add configuration_), now this tab is called differently
   2. In the top left press **+** , choose pytest and press ok
   3. Choose script path to the test file you want to launc
   4. Press OK

III. Press Run - _green arrow_

---

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
