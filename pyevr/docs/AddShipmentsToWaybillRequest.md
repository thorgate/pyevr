# AddShipmentsToWaybillRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipments** | [**List[Shipment]**](Shipment.md) | Lisatavad veose andmed | 

## Example

```python
from openapi_client.models.add_shipments_to_waybill_request import AddShipmentsToWaybillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddShipmentsToWaybillRequest from a JSON string
add_shipments_to_waybill_request_instance = AddShipmentsToWaybillRequest.from_json(json)
# print the JSON string representation of the object
print(AddShipmentsToWaybillRequest.to_json())

# convert the object into a dict
add_shipments_to_waybill_request_dict = add_shipments_to_waybill_request_instance.to_dict()
# create an instance of AddShipmentsToWaybillRequest from a dict
add_shipments_to_waybill_request_from_dict = AddShipmentsToWaybillRequest.from_dict(add_shipments_to_waybill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


