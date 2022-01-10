docker-compose-up:
	docker-compose up -d

docker-compose-down:
	docker-compose down --remove-orphans

docker-compose-restart:
	make docker-compose-down
	make docker-compose-up

docker-compose-prune:
	docker volume prune -f
