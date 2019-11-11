# Waybill

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
**number** | **str** | Veoselehe number | [optional] 
**status** | [**WaybillStatus**](WaybillStatus.md) |  | [optional] 
**creation_time** | **datetime** | Loomise aeg | [optional] 
**cancellation_time** | **datetime** | Tühistamise aeg (kui veoseleht on tühistatud) | [optional] 
**cancellation_reason** | **str** | Tühistamise põhjus (kui veoseleht on tühistatud) | [optional] 
**total_journey_mileage** | **int** | Kilometraaž koormaga (kui veoselehel on vedu lõpetatud) | [optional] 
**unloading_comment** | **str** | Mahalaadimise kommentaar (kui veoselehel on vedu lõpetatud) | [optional] 
**unloading_time** | **datetime** | Mahalaadimise aeg (kui veoselehel on vedu lõpetatud) | [optional] 
**finishing_time** | **datetime** | Veoselehe lõpetamise aeg (kui veoseleht on lõpetatud) | [optional] 
**last_modification_time** | **datetime** | Veoselehe viimase muutmise aeg | [optional] 
**waybill_authorizations** | [**list[WaybillAuthorization]**](WaybillAuthorization.md) | Veoselehe volitused | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


