.DEFAULT_GOAL := help

OPENAPI_GENERATOR_VERSION ?= v7.12.0

.PHONY:
lint:
	poetry run ruff check --select I pyevr --exclude pyevr/openapi_client
	poetry run ruff check pyevr --exclude pyevr/openapi_client

.PHONY:
fmt:
	poetry run ruff check --select I pyevr --fix --exclude pyevr/openapi_client
	poetry run ruff check pyevr --fix --exclude pyevr/openapi_client
	poetry run ruff format pyevr --exclude pyevr/openapi_client

.PHONY:
test: # run tests quickly with the default Python
	poetry run pytest

.PHONY:
test-all: # run tests on every Python version with tox
	tox

.PHONY:
coverage: # check code coverage quickly with the default Python
	poetry run coverage run --source pyevr -m pytest
	poetry run coverage report -m
	poetry run coverage html

.PHONY:
openapi-fetch:
	curl https://evr.veoseleht.ee/api/openapi-generator-compatible.json -o pyevr/openapi/openapi-generator-compatible.json

.PHONY:
openapi-patch: openapi-fetch
	diff -Naur ./pyevr/openapi/openapi-generator-compatible.json ./pyevr/openapi/openapi-generator-compatible-patched.json > ./pyevr/openapi/patches/schema-fixes.patch || echo "Patch created"

.PHONY:
openapi-apply-patch: openapi-fetch
	# Keep the fetched (upstream) schema untouched; write the patched result to a separate file
	patch -p0 -o pyevr/openapi/openapi-generator-compatible-patched.json < pyevr/openapi/patches/schema-fixes.patch

.PHONY:
openapi-build:
	rm -rf .openapi
	rm -rf pyevr/openapi_client
	rm -rf pyevr/docs
	docker run --rm --ulimit nofile=122880:122880  -v ${PWD}/pyevr/openapi/update_schema.sh:/helpers/update_schema.sh -v ${PWD}/pyevr/openapi/openapi-generator-compatible-patched.json:/openapi-generator-compatible.json -v ${PWD}/.openapi/:/openapi openapitools/openapi-generator-cli:$(OPENAPI_GENERATOR_VERSION) /bin/bash /helpers/update_schema.sh /openapi-generator-compatible.json
	sudo chown -R ${USER} .openapi
	cp -r .openapi/openapi_client pyevr/openapi_client
	cp -r .openapi/docs pyevr/docs
	rm -rf .openapi
	poetry run ruff check --select I pyevr/openapi_client --fix
	poetry run ruff format pyevr/openapi_client

.PHONY:
openapi: openapi-apply-patch openapi-build
