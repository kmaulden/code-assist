.PHONY: help ## Print this help
help:
	@grep -E '^\.PHONY: [a-zA-Z_-]+ .*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: init ## Initialize for development
init:
	update-alternatives --set python /usr/bin/python3.10
	poetry config virtualenvs.in-project true
	poetry env use python3.10
	@poetry install

.PHONY: lint ## Lint
lint:
	poetry run pre-commit run --all-files

.PHONY: test ## Run tests
test:
	poetry run pytest

check: lint test