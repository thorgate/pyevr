# WaybillPlaceOfDelivery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | EVR tarnekoha kood (kui on EVR-i lisatud tarnekoht) | [optional] 
**name** | **str** | Tarnekoha nimi | 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 
**address** | [**Address**](Address.md) |  | 
**contact_person** | [**ContactPerson**](ContactPerson.md) |  | [optional] 
**near_address** | **str** | Lähiaadress | [optional] 
**user_custom_data** | **object** | Api kasutaja poolt kohandatavad andmed | [optional] 

## Example

```python
from openapi_client.models.waybill_place_of_delivery import WaybillPlaceOfDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of WaybillPlaceOfDelivery from a JSON string
waybill_place_of_delivery_instance = WaybillPlaceOfDelivery.from_json(json)
# print the JSON string representation of the object
print(WaybillPlaceOfDelivery.to_json())

# convert the object into a dict
waybill_place_of_delivery_dict = waybill_place_of_delivery_instance.to_dict()
# create an instance of WaybillPlaceOfDelivery from a dict
waybill_place_of_delivery_from_dict = WaybillPlaceOfDelivery.from_dict(waybill_place_of_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


