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
**preferred_certificates** | **list[str]** | Eelistatud sertifikaadid | [optional] 
**open_times** | **list[str]** | Millal avatud | [optional] 
**contact_person** | [**ContactPerson**](ContactPerson.md) |  | [optional] 
**waybill_authorizations** | [**list[WaybillAuthorization]**](WaybillAuthorization.md) | Volitatud mõõtjad ja vaatlejad | [optional] 
**user_custom_data** | **object** | Api kasutaja poolt kohandatavad andmed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


