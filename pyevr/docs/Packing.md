# Packing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plastic_sides** | **int** | Kui mitu paki külge plastikku mähkida, tavalised väärtused on 1 ja 5. | [optional] 
**plastic_specification** | **str** | Kasutatakse juhul, kui pooled vajavad erinevatele pakkidele erinevat tüüpi plastikuid ja peavad neid eristama. | [optional] 
**pallet** | **bool** | EUR/EPAL - alusplokk paki all. | [optional] 
**columns** | **int** | Kui palju tükke (laudu) on pakis horisontaalselt ühes kihis. | [optional] 
**rows** | **int** | Kui palju tükke (laudu) on pakis vertikaalselt &#x3D; kui palju kihte. | [optional] 
**sticks_count** | **int** | Kui palju vahelaudu ühes kihis (samal tasemel (horisontaalselt)). | [optional] 
**sticks_layers** | **int** | Mitme kihi järel vahelaudu kasutada. Väärtus 1 tähendab vahelaudu iga kihi vahel. | [optional] 
**straps_count** | **int** | Kui palju rihmlinte paki ümber panna. | [optional] 
**straps_type** | [**Straps**](Straps.md) |  | [optional] 
**labels_count** | **int** | Kui palju pakimärgiseid peale panna. | [optional] 
**labels_placement** | **str** | Kasutatakse juhul, kui pooled vajavad erinevat loogikat märgiste paigutamiseks (sama arvu märgiste korral) erinevatele pakkidele. | [optional] 
**source_id** | **str** | Kauba lähetaja infosüsteemi identifikaator. | [optional] 
**target_id** | **str** | Kauba saaja infosüsteemi identifikaator. | [optional] 
**custom_data** | **object** | Api kasutaja poolt kohandatavad andmed. | [optional] 
**name** | **str** | Paki nimetus | 

## Example

```python
from openapi_client.models.packing import Packing

# TODO update the JSON string below
json = "{}"
# create an instance of Packing from a JSON string
packing_instance = Packing.from_json(json)
# print the JSON string representation of the object
print(Packing.to_json())

# convert the object into a dict
packing_dict = packing_instance.to_dict()
# create an instance of Packing from a dict
packing_from_dict = Packing.from_dict(packing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


