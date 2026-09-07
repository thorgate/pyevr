# StartSawnWayBillRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipments** | [**List[SawnShipment]**](SawnShipment.md) | Lähetatud saematerjali veose andmed | 

## Example

```python
from openapi_client.models.start_sawn_way_bill_request import StartSawnWayBillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartSawnWayBillRequest from a JSON string
start_sawn_way_bill_request_instance = StartSawnWayBillRequest.from_json(json)
# print the JSON string representation of the object
print(StartSawnWayBillRequest.to_json())

# convert the object into a dict
start_sawn_way_bill_request_dict = start_sawn_way_bill_request_instance.to_dict()
# create an instance of StartSawnWayBillRequest from a dict
start_sawn_way_bill_request_from_dict = StartSawnWayBillRequest.from_dict(start_sawn_way_bill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


