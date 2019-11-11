.PHONY: clean clean-test clean-pyc clean-build docs help openapi
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 pyevr tests

test: ## run tests quickly with the default Python
	pytest

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source pyevr -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/pyevr.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ pyevr
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install

openapi: ## generate new API client based on the OpenAPI specification
	rm -rf .openapi
	rm -rf pyevr/openapi_client
	# Original API schema is located at https://evr-test.azurewebsites.net/api/openapi.json
	docker run --rm -v ${PWD}/.openapi:/openapi openapitools/openapi-generator-cli:v4.2.0 generate -i https://evr-test.azurewebsites.net/api/openapi-generator-compatible.json -g python -o /openapi
	# Import generated code from the correct place
	docker run --rm -v ${PWD}/.openapi:/openapi openapitools/openapi-generator-cli:v4.2.0 find /openapi/openapi_client -type f -exec sed -i 's/openapi_client.models/pyevr.openapi_client.models/g' {} +
	docker run --rm -v ${PWD}/.openapi:/openapi openapitools/openapi-generator-cli:v4.2.0 find /openapi/openapi_client -type f -exec sed -i 's/from openapi_client/from pyevr.openapi_client/g' {} +
	# Remove trailing whitespaces
	docker run --rm -v ${PWD}/.openapi:/openapi openapitools/openapi-generator-cli:v4.2.0 find /openapi/openapi_client -type f -exec sed -i -re 's/[ \t]+$$//' {} +
	cp -r .openapi/openapi_client pyevr/openapi_client
	rm -rf .openapi
