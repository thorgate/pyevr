# ForestWaybill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipments** | [**List[Shipment]**](Shipment.md) | Lähetatud metsamaterjali veose andmed | 

## Example

```python
from openapi_client.models.forest_waybill import ForestWaybill

# TODO update the JSON string below
json = "{}"
# create an instance of ForestWaybill from a JSON string
forest_waybill_instance = ForestWaybill.from_json(json)
# print the JSON string representation of the object
print(ForestWaybill.to_json())

# convert the object into a dict
forest_waybill_dict = forest_waybill_instance.to_dict()
# create an instance of ForestWaybill from a dict
forest_waybill_from_dict = ForestWaybill.from_dict(forest_waybill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


