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
**shipments** | [**List[Shipment]**](Shipment.md) | Lähetatud veose andmed | 
**pre_journey_mileage** | **int** | Ettesõidu kilometraaž | [optional] 
**user_custom_data** | **object** | Api kasutaja poolt kohandatavad andmed | [optional] 
**mass** | **float** | Autorongi mass tonnides | [optional] 
**transport_order** | **str** | Veotellimuse number | [optional] 
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
**notes** | [**List[WaybillNote]**](WaybillNote.md) | Veoselehe märkused | [optional] 
**waybill_authorizations** | [**List[WaybillAuthorization]**](WaybillAuthorization.md) | Veoselehe volitused | [optional] 
**waybill_latest_measurements** | [**MeasurementAct**](MeasurementAct.md) |  | [optional] 

## Example

```python
from openapi_client.models.waybill import Waybill

# TODO update the JSON string below
json = "{}"
# create an instance of Waybill from a JSON string
waybill_instance = Waybill.from_json(json)
# print the JSON string representation of the object
print Waybill.to_json()

# convert the object into a dict
waybill_dict = waybill_instance.to_dict()
# create an instance of Waybill from a dict
waybill_form_dict = waybill.from_dict(waybill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


