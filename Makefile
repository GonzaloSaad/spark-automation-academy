.PHONY: init \

############################################################################
## General Parameters Configuration
############################################################################

VENV ?= venv
REQUIREMENTS ?= requirements.txt

############################################################################
## Target definitions
## This section will define the projects make targets
############################################################################


help:
	@echo "    init"
	@echo "        Initializes development environment."

init: clean init-venv init-precommit

init-venv: clean-venv create-venv update-venv
	@echo ""
	@echo "Do not forget to activate your new virtual environment"

create-venv:
	@echo "Creating virtual environment: $(VENV)..."
	@python3 -m venv $(VENV)

update-venv:
	@echo "Updating virtual environment: $(VENV)..."
	@( \
		. $(VENV)/bin/activate; \
		pip install --upgrade pip; \
		pip install -r $(REQUIREMENTS); \
	)

init-precommit:
	@echo "Installing pre commit..."
	@( \
		. $(VENV)/bin/activate; \
		pre-commit install; \
	)

clean: clean-pyc clean-venv

clean-venv:
	@echo "Removing virtual environment: $(VENV)..."
	@rm -rf $(VENV)

clean-pyc:
	@echo "Removing compiled bytecode files..."
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
