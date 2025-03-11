# CancelWaybillRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Selgitus | 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 

## Example

```python
from openapi_client.models.cancel_waybill_request import CancelWaybillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelWaybillRequest from a JSON string
cancel_waybill_request_instance = CancelWaybillRequest.from_json(json)
# print the JSON string representation of the object
print(CancelWaybillRequest.to_json())

# convert the object into a dict
cancel_waybill_request_dict = cancel_waybill_request_instance.to_dict()
# create an instance of CancelWaybillRequest from a dict
cancel_waybill_request_from_dict = CancelWaybillRequest.from_dict(cancel_waybill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


