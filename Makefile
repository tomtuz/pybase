.PHONY: setup install update clean test lint format typecheck

setup: ## Initial project setup
	cp .env.example .env
	poetry install
	poetry run pre-commit install

install: ## Install dependencies
	poetry install

update: ## Update dependencies
	poetry update

test: ## Run tests
	poetry run pytest

lint: ## Run linting
	poetry run ruff check .

format: ## Format code
	poetry run ruff format .

typecheck: ## Run type checking
	poetry run mypy .

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
