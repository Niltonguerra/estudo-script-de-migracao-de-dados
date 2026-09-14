SERVICE_NAME := script-provisorio
PORT_SERVICE := 3500
VERSION := 1.0.1
IMAGE_NAME := script/$(SERVICE_NAME)

.PHONY: help build run-dev logs logs-db

help:
	@echo "Comandos disponíveis:"
	@echo "  make build      - Builda a imagem de produção"
	@echo "  make run-dev    - Sobe o serviço em modo desenvolvimento"
	@echo "  make stop       - Derruba o serviço"
	@echo "  make logs       - Mostra logs do servidor"
	@echo "  make logs-db    - Mostra logs do banco de dados"

build:
	docker build --target production -t $(IMAGE_NAME):$(VERSION) .

run-dev:
	.venv/bin/pip install -r requirements.txt
	docker compose up --build -d

stop:
	docker compose down
	
logs:
	docker compose logs -f script-provisorio

logs-db:
	docker compose logs -f mongodb