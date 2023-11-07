.PHONY: clean clean-test clean-pyc clean-build docs help openapi
.DEFAULT_GOAL := help

OPENAPI_GENERATOR_VERSION ?= v7.0.1

lint:
	poetry run flake8 --select=E9,F63,F7,F82 pyevr

fmt:
	poetry run black pyevr
	poetry run black test

test: ## run tests quickly with the default Python
	poetry run pytest

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source pyevr -m pytest
	coverage report -m
	coverage html

release: dist ## package and upload a release
	# todo
	twine upload dist/*

dist: clean ## builds source and wheel package
	# todo
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	$ todo
	python setup.py install

openapi-patch: ## create patch for openapi schema
	curl https://evr.veoseleht.ee/api/openapi-generator-compatible.json -o pyevr/openapi/openapi-generator-compatible.json
	diff -Naur ./pyevr/openapi/openapi-generator-compatible.json ./pyevr/openapi/openapi-generator-compatible-patched.json > ./pyevr/openapi/patches/schema-fixes.patch || echo "Patch created"

openapi: ## generate new API client based on the OpenAPI specification
	rm -rf .openapi
	rm -rf pyevr/openapi_client
	rm -rf pyevr/docs
	curl https://evr.veoseleht.ee/api/openapi-generator-compatible.json -o pyevr/openapi/openapi-generator-compatible.json
	patch -p0 < pyevr/openapi/patches/schema-fixes.patch
	docker run --rm --ulimit nofile=122880:122880  -v ${PWD}/pyevr/openapi/update_schema.sh:/helpers/update_schema.sh -v ${PWD}/pyevr/openapi/openapi-generator-compatible.json:/openapi-generator-compatible.json -v ${PWD}/.openapi/:/openapi openapitools/openapi-generator-cli:$(OPENAPI_GENERATOR_VERSION) /bin/bash /helpers/update_schema.sh /openapi-generator-compatible.json
	sudo chown -R ${USER} .openapi
	cp -r .openapi/openapi_client pyevr/openapi_client
	cp -r .openapi/docs pyevr/docs
	rm -rf .openapi
	poetry run black pyevr
