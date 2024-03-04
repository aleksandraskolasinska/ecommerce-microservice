# Docker Operations

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

# DB Debug

psql:
	psql -h localhost -p 5432 -U admin -d db

remove-db:
	docker volume rm microservices_pgdata


# Curling GET Endpoints
