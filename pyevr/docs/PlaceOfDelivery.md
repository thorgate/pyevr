# PlaceOfDelivery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Tarnekoha nimi | [optional] 
**code** | **str** | Tarnekoha kood | [optional] 
**register_code** | **str** | Registrikood | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**near_address** | **str** | Lähiaadress | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 
**open_times** | **List[str]** | Millal avatud | [optional] 
**is_active** | **bool** | Kas on aktiivne | [optional] 
**preferred_certificates** | **List[str]** | Eelistatud sertifikaadid | [optional] 
**contact_person** | [**ContactPerson**](ContactPerson.md) |  | [optional] 
**waybill_authorizations** | [**List[WaybillAuthorization]**](WaybillAuthorization.md) | Volitused | [optional] 
**description** | **str** | Märkused | [optional] 
**user_custom_data** | **object** | Api kasutaja poolt kohandatavad andmed | [optional] 

## Example

```python
from openapi_client.models.place_of_delivery import PlaceOfDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of PlaceOfDelivery from a JSON string
place_of_delivery_instance = PlaceOfDelivery.from_json(json)
# print the JSON string representation of the object
print(PlaceOfDelivery.to_json())

# convert the object into a dict
place_of_delivery_dict = place_of_delivery_instance.to_dict()
# create an instance of PlaceOfDelivery from a dict
place_of_delivery_from_dict = PlaceOfDelivery.from_dict(place_of_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


