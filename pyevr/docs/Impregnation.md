# Impregnation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Immutusprotsessi nimi. | [optional] 
**chemical** | **str** | Kaitsmiseks kasutatud aine. | [optional] 
**level** | **int** | Väärtused peaksid olema vahemikus 1..6. | [optional] 
**notes** | **str** | Lisamärkused. | [optional] 
**source_id** | **str** | Kauba lähetaja infosüsteemi identifikaator. | [optional] 
**target_id** | **str** | Kauba saaja infosüsteemi identifikaator. | [optional] 
**custom_data** | **object** | Api kasutaja poolt kohandatavad andmed. | [optional] 

## Example

```python
from openapi_client.models.impregnation import Impregnation

# TODO update the JSON string below
json = "{}"
# create an instance of Impregnation from a JSON string
impregnation_instance = Impregnation.from_json(json)
# print the JSON string representation of the object
print(Impregnation.to_json())

# convert the object into a dict
impregnation_dict = impregnation_instance.to_dict()
# create an instance of Impregnation from a dict
impregnation_from_dict = Impregnation.from_dict(impregnation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


