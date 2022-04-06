# StartWaybillRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | [**Owner**](Owner.md) |  | 
**transport** | [**Transport**](Transport.md) |  | 
**receiver** | [**Receiver**](Receiver.md) |  | 
**place_of_delivery** | [**WaybillPlaceOfDelivery**](WaybillPlaceOfDelivery.md) |  | 
**comment** | **str** | Märkused/lisainfo | [optional] 
**departure_time** | **datetime** | Väljasõidu aeg | 
**submission_time** | **datetime** | Veoselehe EVR-i saatmise aeg | 
**shipments** | [**list[Shipment]**](Shipment.md) | Lähetatud veose andmed | 
**pre_journey_mileage** | **int** | Ettesõidu kilometraaž | [optional] 
**user_custom_data** | **object** | Api kasutaja poolt kohandatavad andmed | [optional] 
**mass** | **float** | Autorongi mass tonnides | [optional] 
**transport_order** | **str** | Veotellimuse number | [optional] 
**viewers** | [**list[Viewer]**](Viewer.md) | Veoselehe vaatlejad | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


