# StartForestWaybillRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipments** | [**List[Shipment]**](Shipment.md) | Lähetatud metsamaterjali veose andmed | 

## Example

```python
from openapi_client.models.start_forest_waybill_request import StartForestWaybillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartForestWaybillRequest from a JSON string
start_forest_waybill_request_instance = StartForestWaybillRequest.from_json(json)
# print the JSON string representation of the object
print(StartForestWaybillRequest.to_json())

# convert the object into a dict
start_forest_waybill_request_dict = start_forest_waybill_request_instance.to_dict()
# create an instance of StartForestWaybillRequest from a dict
start_forest_waybill_request_from_dict = StartForestWaybillRequest.from_dict(start_forest_waybill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


