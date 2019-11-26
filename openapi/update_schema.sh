docker-entrypoint.sh generate -i $1 -g python -o /openapi

# Import generated code from the correct place
find /openapi/openapi_client -type f -exec sed -i 's/openapi_client.models/pyevr.openapi_client.models/g' {} +
find /openapi/openapi_client -type f -exec sed -i 's/from openapi_client/from pyevr.openapi_client/g' {} +

# Remove trailing whitespaces
find /openapi/openapi_client -type f -exec sed -i -re 's/[ \t]+$$//' {} +
# TODO: Remove when maximum values in API schema are fixed
find /openapi/openapi_client -type f -exec sed -i -re 's/-9223372036854771616/2147483647/' {} +
# TODO: Remove when Organization.address.country_code in test server has valid data
find /openapi/openapi_client -type f -exec sed -i -re 's/len\(country_code\) > 3/len\(country_code\) > 300/' {} +
# TODO: Remove when Organization.contact_person.phone and Waybill.owner.representer.phone in test server has valid data
find /openapi/openapi_client -type f -exec sed -i -re 's/len\(phone\) > 25/len\(phone\) > 250/' {} +
