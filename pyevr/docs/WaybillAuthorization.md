# WaybillAuthorization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Registrikood | 
**type** | [**AuthorizationType**](AuthorizationType.md) |  | 

## Example

```python
from openapi_client.models.waybill_authorization import WaybillAuthorization

# TODO update the JSON string below
json = "{}"
# create an instance of WaybillAuthorization from a JSON string
waybill_authorization_instance = WaybillAuthorization.from_json(json)
# print the JSON string representation of the object
print(WaybillAuthorization.to_json())

# convert the object into a dict
waybill_authorization_dict = waybill_authorization_instance.to_dict()
# create an instance of WaybillAuthorization from a dict
waybill_authorization_from_dict = WaybillAuthorization.from_dict(waybill_authorization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


