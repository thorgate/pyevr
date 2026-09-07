# Seasoning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Kuivatusmeetodi nimetus. | [optional] 
**kd** | **bool** | Näitab kiiret kuivatusprotsessi kambris. Väärtus \&quot;Ei\&quot; näitab pikka kuivatamist ümbritseva temperatuuri juures. | [optional] 
**ht5630** | **bool** | Puit on sertifitseeritud ISPM 15 standardi järgi soojustöödelduna 56/30. | [optional] 
**percent** | **float** | Niiskus % +/- 2% tolerantsiga. Võib tõlgendada märja materjalina, kui jäetakse tühjaks. | [optional] 
**thermo_intense** | **int** | Võimalikud väärtused: 0&#x3D;ei, 1&#x3D;keskmine, 2&#x3D;intensiivne. | [optional] 
**notes** | **str** | Lisamärkused. | [optional] 
**source_id** | **str** | Kauba lähetaja infosüsteemi identifikaator. | [optional] 
**target_id** | **str** | Kauba saaja infosüsteemi identifikaator. | [optional] 
**custom_data** | **object** | Api kasutaja poolt kohandatavad andmed. | [optional] 

## Example

```python
from openapi_client.models.seasoning import Seasoning

# TODO update the JSON string below
json = "{}"
# create an instance of Seasoning from a JSON string
seasoning_instance = Seasoning.from_json(json)
# print the JSON string representation of the object
print(Seasoning.to_json())

# convert the object into a dict
seasoning_dict = seasoning_instance.to_dict()
# create an instance of Seasoning from a dict
seasoning_from_dict = Seasoning.from_dict(seasoning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


