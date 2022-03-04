####################
# Docker Image
docker-compose-up:
	docker-compose up -d

docker-compose-down:
	docker-compose down --remove-orphans

docker-compose-restart:
	make docker-compose-down
	make docker-compose-up

docker-compose-prune:
	docker volume prune -f


####################
# Backend Image
image-build: IMAGE_TAG := test
image-build:
	$(info Build docker image for backend - CMS and workes)
	docker build . -t zifter/byprice24-cms:$(IMAGE_TAG)

# Test Docker image
image-test: IMAGE_TAG := test
image-test: DJANGO_CONFIGURATION := Test
image-test:
	$(info Run tests for docker image)
	docker run --rm zifter/byprice24-cms:$(IMAGE_TAG) python3 manage.py check --configuration=${DJANGO_CONFIGURATION}
	docker run --rm --network=backend --env-file=image-test.env zifter/byprice24-cms:$(IMAGE_TAG) /bin/bash -c "\
		pytest . --cov=. && \
		coverage report --include="*tests.py" --rcfile=pytest.ini --fail-under=100 && \
		coverage report --include="*" --rcfile=pytest.ini --fail-under=96 \
		"

image-migrations-check: IMAGE_TAG := test
image-migrations-check:
	$(info Check if migrations is needed)
	docker run --rm zifter/byprice24-cms:$(IMAGE_TAG) python3 manage.py makemigrations --check --dry-run

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
	pipenv run coverage report --include="src/*" --rcfile=src/pytest.ini --fail-under=96

open-coverage:
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
	pipenv run ./src/manage.py create-admin-user --username root --password 1234

load-fixtures:
	$(info Load fixtures to database)
	pipenv run ./src/manage.py loaddata fixtures/prod/*.yaml

load-fixtures-dump:
	$(info Load test fixtures to database)
	pipenv run ./src/manage.py loaddata fixtures/dump/*.yaml

save-fixtures-dump:
	$(info Load test fixtures to database)
	pipenv run ./src/manage.py dumpdata marketplace --format yaml > ./fixtures/dump/marketplace.yaml

workers:
	$(info Load workes for all queues)
	pipenv run ./src/manage.py rqworker crawler-feed crawler-result search-query

runserver:
	$(info Run server)
	pipenv run ./src/manage.py runserver 0.0.0.0:8080

rebuild_index:
	$(info Run server)
	pipenv run ./src/manage.py search_index --rebuild -f

cms-init: createuser rebuild_index load-fixtures
