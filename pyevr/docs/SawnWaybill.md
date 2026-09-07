# SawnWaybill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipments** | [**List[SawnShipment]**](SawnShipment.md) | Lähetatud saematerjali veose andmed | 

## Example

```python
from openapi_client.models.sawn_waybill import SawnWaybill

# TODO update the JSON string below
json = "{}"
# create an instance of SawnWaybill from a JSON string
sawn_waybill_instance = SawnWaybill.from_json(json)
# print the JSON string representation of the object
print(SawnWaybill.to_json())

# convert the object into a dict
sawn_waybill_dict = sawn_waybill_instance.to_dict()
# create an instance of SawnWaybill from a dict
sawn_waybill_from_dict = SawnWaybill.from_dict(sawn_waybill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


