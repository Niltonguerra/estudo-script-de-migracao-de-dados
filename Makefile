SERVICE_NAME := script-provisorio
PORT_SERVICE := 3500
VERSION := 1.0.1
IMAGE_NAME := script/$(SERVICE_NAME)


.PHONY: help build dev load deploy scaffold logs list

help:
	@echo "Comandos disponíveis:"
	@echo "  make build      - Builda a imagem de produção"
	@echo "  make run-dev    - Sobe o serviço em modo desenvolvimento"


build:
	docker build --target production -t $(IMAGE_NAME):$(VERSION) .

run-dev:
	.venv/bin/pip install -r requirements.txt
	docker compose up --build
