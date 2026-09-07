# Surface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Pinnatöötluse või viimistluse nimetus. | [optional] 
**ral_code** | **str** | Väärtused piiratud RAL värvistandardiga. | [optional] 
**ncs_code** | **str** | Väärtused piiratud NCS värvistandardiga. | [optional] 
**rgb_code** | **str** | Väärtused piiratud RGB värvimudeli HEX formaadiga. | [optional] 
**transparency** | **float** | Katteaine läbipaistvuse protsent. | [optional] 
**refinement** | **str** | Pindtöötluse lisadetailid, nt. granulaarsus või harjatamise tugevus. | [optional] 
**notes** | **str** | Lisamärkused. | [optional] 
**source_id** | **str** | Kauba lähetaja infosüsteemi identifikaator. | [optional] 
**target_id** | **str** | Kauba saaja infosüsteemi identifikaator. | [optional] 
**custom_data** | **object** | Api kasutaja poolt kohandatavad andmed. | [optional] 

## Example

```python
from openapi_client.models.surface import Surface

# TODO update the JSON string below
json = "{}"
# create an instance of Surface from a JSON string
surface_instance = Surface.from_json(json)
# print the JSON string representation of the object
print(Surface.to_json())

# convert the object into a dict
surface_dict = surface_instance.to_dict()
# create an instance of Surface from a dict
surface_from_dict = Surface.from_dict(surface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


