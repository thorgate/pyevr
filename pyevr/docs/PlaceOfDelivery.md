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
**open_times** | **list[str]** | Millal avatud | [optional] 
**is_public** | **bool** | Kas on avalik | [optional] 
**is_active** | **bool** | Kas on aktiivne | [optional] 
**preferred_certificates** | **list[str]** | Eelistatud sertifikaadid | [optional] 
**contact_person** | [**ContactPerson**](ContactPerson.md) |  | [optional] 
**waybill_authorizations** | [**list[WaybillAuthorization]**](WaybillAuthorization.md) | Volitused | [optional] 
**description** | **str** | Märkused | [optional] 
**user_custom_data** | **object** | Api kasutaja poolt kohandatavad andmed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


