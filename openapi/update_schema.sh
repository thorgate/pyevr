docker-entrypoint.sh generate -i $1 -g python -o /openapi

# Import generated code from the correct place
find /openapi/openapi_client -type f -exec sed -i 's/openapi_client.models/pyevr.openapi_client.models/g' {} +
find /openapi/openapi_client -type f -exec sed -i 's/from openapi_client/from pyevr.openapi_client/g' {} +

# Update WaybillsApi to use waybills_list instead of waybills_get and waybills_get instead of waybills_get2
find /openapi -type f -exec sed -i -re 's/waybills_get\(/waybills_list\(/' {} +
find /openapi -type f -exec sed -i -re 's/waybills_get\)/waybills_list\)/' {} +
find /openapi -type f -exec sed -i -re 's/waybills_get\*/waybills_list\*/' {} +
find /openapi -type f -exec sed -i -re 's/waybills_get:/waybills_list:/' {} +
find /openapi -type f -exec sed -i -re 's/waybills_get"/waybills_list"/' {} +
find /openapi -type f -exec sed -i -re 's/waybills_get_with_http_info\(/waybills_list_with_http_info\(/' {} +
find /openapi -type f -exec sed -i -re 's/waybills_get2\(/waybills_get\(/' {} +
find /openapi -type f -exec sed -i -re 's/waybills_get2\)/waybills_get\)/' {} +
find /openapi -type f -exec sed -i -re 's/waybills_get2\*/waybills_get\*/' {} +
find /openapi -type f -exec sed -i -re 's/waybills_get2:/waybills_get:/' {} +
find /openapi -type f -exec sed -i -re 's/waybills_get2"/waybills_get"/' {} +
find /openapi -type f -exec sed -i -re 's/waybills_get2`/waybills_get`/' {} +
find /openapi -type f -exec sed -i -re 's/waybills_get2_with_http_info\(/waybills_get_with_http_info\(/' {} +

# Remove trailing whitespaces
find /openapi/openapi_client -type f -exec sed -i -re 's/[ \t]+$$//' {} +
