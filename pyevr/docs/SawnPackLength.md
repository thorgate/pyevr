# SawnPackLength


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **float** | Väärtus millimeetrites (mm). | 
**pieces** | **int** | Tükkide (laudade) arv pakis selle pikkusega. | 
**notes** | **str** | Lisamärkused. | [optional] 
**source_id** | **str** | Kauba lähetaja infosüsteemi identifikaator. | [optional] 
**target_id** | **str** | Kauba saaja infosüsteemi identifikaator. | [optional] 
**custom_data** | **object** | Api kasutaja poolt kohandatavad andmed. | [optional] 

## Example

```python
from openapi_client.models.sawn_pack_length import SawnPackLength

# TODO update the JSON string below
json = "{}"
# create an instance of SawnPackLength from a JSON string
sawn_pack_length_instance = SawnPackLength.from_json(json)
# print the JSON string representation of the object
print(SawnPackLength.to_json())

# convert the object into a dict
sawn_pack_length_dict = sawn_pack_length_instance.to_dict()
# create an instance of SawnPackLength from a dict
sawn_pack_length_from_dict = SawnPackLength.from_dict(sawn_pack_length_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


