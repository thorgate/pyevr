# ShipmentAssortment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Sortimendi kood. Kui organisatsioon on seadistatud kasutama EVR sortimente, peab kood olema [üks EVR sortimentide koodist.](#operation/Assortments_List) | 
**name** | **str** | Sortimendi nimetus | 
**product_group** | **str** | Tootegrupi kood | 

## Example

```python
from openapi_client.models.shipment_assortment import ShipmentAssortment

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentAssortment from a JSON string
shipment_assortment_instance = ShipmentAssortment.from_json(json)
# print the JSON string representation of the object
print ShipmentAssortment.to_json()

# convert the object into a dict
shipment_assortment_dict = shipment_assortment_instance.to_dict()
# create an instance of ShipmentAssortment from a dict
shipment_assortment_form_dict = shipment_assortment.from_dict(shipment_assortment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


