# ShipmentItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Kogus | 
**pack** | [**Pack**](Pack.md) |  | [optional] 
**unit_code** | **str** | [Mõõtühiku kood](#operation/MeasurementUnits_List) | 
**assortment** | [**ShipmentAssortment**](ShipmentAssortment.md) |  | 

## Example

```python
from openapi_client.models.shipment_item import ShipmentItem

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentItem from a JSON string
shipment_item_instance = ShipmentItem.from_json(json)
# print the JSON string representation of the object
print ShipmentItem.to_json()

# convert the object into a dict
shipment_item_dict = shipment_item_instance.to_dict()
# create an instance of ShipmentItem from a dict
shipment_item_form_dict = shipment_item.from_dict(shipment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


