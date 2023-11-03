# Shipment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_base** | [**HoldingBase**](HoldingBase.md) |  | 
**source** | [**Source**](Source.md) |  | 
**items** | [**List[ShipmentItem]**](ShipmentItem.md) | Saadetis | 
**certificate_claims** | [**List[CertificateClaim]**](CertificateClaim.md) | Tarneahela sertifikaadi väited | [optional] 
**user_custom_data** | **object** | Api kasutaja poolt kohandatavad andmed | [optional] 
**supply_contract_number** | **str** | Tarnelepingu number | [optional] 

## Example

```python
from openapi_client.models.shipment import Shipment

# TODO update the JSON string below
json = "{}"
# create an instance of Shipment from a JSON string
shipment_instance = Shipment.from_json(json)
# print the JSON string representation of the object
print Shipment.to_json()

# convert the object into a dict
shipment_dict = shipment_instance.to_dict()
# create an instance of Shipment from a dict
shipment_form_dict = shipment.from_dict(shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


