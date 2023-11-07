# PutPlaceOfDeliveryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nimi | 
**address** | [**Address**](Address.md) |  | 
**near_address** | **str** | Lähiaadress | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) |  | 
**description** | **str** | Märkused | [optional] 
**is_active** | **bool** | Kas on aktiivne | 
**is_public** | **bool** | Kas on avalik (avalikke ladusid näevad ka teised asutused) | 
**preferred_certificates** | **List[str]** | Eelistatud sertifikaadid | [optional] 
**open_times** | **List[str]** | Millal avatud | [optional] 
**contact_person** | [**ContactPerson**](ContactPerson.md) |  | [optional] 
**waybill_authorizations** | [**List[WaybillAuthorization]**](WaybillAuthorization.md) | Volitatud mõõtjad ja vaatlejad | [optional] 
**user_custom_data** | **object** | Api kasutaja poolt kohandatavad andmed | [optional] 

## Example

```python
from openapi_client.models.put_place_of_delivery_request import PutPlaceOfDeliveryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutPlaceOfDeliveryRequest from a JSON string
put_place_of_delivery_request_instance = PutPlaceOfDeliveryRequest.from_json(json)
# print the JSON string representation of the object
print PutPlaceOfDeliveryRequest.to_json()

# convert the object into a dict
put_place_of_delivery_request_dict = put_place_of_delivery_request_instance.to_dict()
# create an instance of PutPlaceOfDeliveryRequest from a dict
put_place_of_delivery_request_form_dict = put_place_of_delivery_request.from_dict(put_place_of_delivery_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


