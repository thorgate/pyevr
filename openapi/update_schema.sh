docker-entrypoint.sh generate -i $1 -g python -o /openapi

# Import generated code from the correct place
find /openapi/openapi_client -type f -exec sed -i 's/openapi_client.models/pyevr.openapi_client.models/g' {} +
find /openapi/openapi_client -type f -exec sed -i 's/from openapi_client/from pyevr.openapi_client/g' {} +

# Remove trailing whitespaces
find /openapi/openapi_client -type f -exec sed -i -re 's/[ \t]+$$//' {} +
# TODO: Remove when maximum values in API schema are fixed
find /openapi/openapi_client -type f -exec sed -i -re 's/-9223372036854771616/2147483647/' {} +
