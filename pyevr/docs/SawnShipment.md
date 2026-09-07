# SawnShipment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sawn_wood** | [**SawnWood**](SawnWood.md) |  | 
**packs** | [**List[SawnPack]**](SawnPack.md) | Definitsiooni järgi on pakis ainult üks ristlõikemõõt, tamme jne puhul varieerimisega kasutame keskmist laiust või virtuaalseid alamkimpe. | 
**row_number** | **int** | Saadetise rea või järjekorra number. | [optional] 
**eudr_numbers** | [**List[EudrNumber]**](EudrNumber.md) | Euroopa Liidu puidu asukoha registreerimise numbrid | [optional] 
**name** | **str** | Saadetise nimi, lühikirjeldus või partiinumber. | [optional] 
**source_id** | **str** | Kauba lähetaja infosüsteemi identifikaator. | [optional] 
**target_id** | **str** | Kauba saaja infosüsteemi identifikaator. | [optional] 
**custom_data** | **object** | Api kasutaja poolt kohandatavad andmed. | [optional] 

## Example

```python
from openapi_client.models.sawn_shipment import SawnShipment

# TODO update the JSON string below
json = "{}"
# create an instance of SawnShipment from a JSON string
sawn_shipment_instance = SawnShipment.from_json(json)
# print the JSON string representation of the object
print(SawnShipment.to_json())

# convert the object into a dict
sawn_shipment_dict = sawn_shipment_instance.to_dict()
# create an instance of SawnShipment from a dict
sawn_shipment_from_dict = SawnShipment.from_dict(sawn_shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


