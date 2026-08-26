# ShipmentItemBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Kogus | 
**pack** | [**Pack**](Pack.md) |  | [optional] 
**unit_code** | **str** | [Mõõtühiku kood](#operation/MeasurementUnits_List) | 
**assortment** | [**ShipmentAssortment**](ShipmentAssortment.md) |  | 

## Example

```python
from openapi_client.models.shipment_item_base import ShipmentItemBase

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentItemBase from a JSON string
shipment_item_base_instance = ShipmentItemBase.from_json(json)
# print the JSON string representation of the object
print(ShipmentItemBase.to_json())

# convert the object into a dict
shipment_item_base_dict = shipment_item_base_instance.to_dict()
# create an instance of ShipmentItemBase from a dict
shipment_item_base_from_dict = ShipmentItemBase.from_dict(shipment_item_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


