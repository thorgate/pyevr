# UnloadWaybillRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_journey_mileage** | **int** | Kilometraaž koormaga | 
**comment** | **str** | Kommentaar | [optional] 

## Example

```python
from openapi_client.models.unload_waybill_request import UnloadWaybillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnloadWaybillRequest from a JSON string
unload_waybill_request_instance = UnloadWaybillRequest.from_json(json)
# print the JSON string representation of the object
print UnloadWaybillRequest.to_json()

# convert the object into a dict
unload_waybill_request_dict = unload_waybill_request_instance.to_dict()
# create an instance of UnloadWaybillRequest from a dict
unload_waybill_request_form_dict = unload_waybill_request.from_dict(unload_waybill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


