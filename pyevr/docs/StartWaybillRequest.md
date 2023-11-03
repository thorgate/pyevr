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
**shipments** | [**List[Shipment]**](Shipment.md) | Lähetatud veose andmed | 
**pre_journey_mileage** | **int** | Ettesõidu kilometraaž | [optional] 
**user_custom_data** | **object** | Api kasutaja poolt kohandatavad andmed | [optional] 
**mass** | **float** | Autorongi mass tonnides | [optional] 
**transport_order** | **str** | Veotellimuse number | [optional] 
**viewers** | [**List[Viewer]**](Viewer.md) | Veoselehe vaatlejad | [optional] 

## Example

```python
from openapi_client.models.start_waybill_request import StartWaybillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartWaybillRequest from a JSON string
start_waybill_request_instance = StartWaybillRequest.from_json(json)
# print the JSON string representation of the object
print StartWaybillRequest.to_json()

# convert the object into a dict
start_waybill_request_dict = start_waybill_request_instance.to_dict()
# create an instance of StartWaybillRequest from a dict
start_waybill_request_form_dict = start_waybill_request.from_dict(start_waybill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


