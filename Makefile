.DEFAULT_GOAL := help

.PHONY: help build up start down destroy stop

help:
		@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-30s\033[0m %s\n", $$1, $$2}'

build: ## Build Docker container
		docker-compose -f docker-compose.yml build
up: ## Up Docker container
		docker-compose -f docker-compose.yml up
start: ## Start Docker container
		docker-compose -f docker-compose.yml start
down: ## Down Docker container
		docker-compose -f docker-compose.yml down
destroy: ## Destroy Docker container
		docker-compose -f docker-compose.yml down -v
stop: ## Stop Docker container
		docker-compose -f docker-compose.yml stop