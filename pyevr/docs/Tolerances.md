# Tolerances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thickness_plus** | **float** | Maksimaalne erinevus ÜLE määratud paksuse millimeetrites (mm). | [optional] 
**thickness_minus** | **float** | Maksimaalne erinevus ALLA määratud paksuse millimeetrites (mm). | [optional] 
**width_plus** | **float** | Maksimaalne erinevus ÜLE määratud laiuse millimeetrites (mm). | [optional] 
**width_minus** | **float** | Maksimaalne erinevus ALLA määratud laiuse millimeetrites (mm). | [optional] 
**length_plus** | **float** | Maksimaalne erinevus ÜLE määratud pikkuse millimeetrites (mm). | [optional] 
**length_minus** | **float** | Maksimaalne erinevus ALLA määratud pikkuse millimeetrites (mm). | [optional] 
**source_id** | **str** | Kauba lähetaja infosüsteemi identifikaator. | [optional] 
**target_id** | **str** | Kauba saaja infosüsteemi identifikaator. | [optional] 
**custom_data** | **object** | Api kasutaja poolt kohandatavad andmed. | [optional] 

## Example

```python
from openapi_client.models.tolerances import Tolerances

# TODO update the JSON string below
json = "{}"
# create an instance of Tolerances from a JSON string
tolerances_instance = Tolerances.from_json(json)
# print the JSON string representation of the object
print(Tolerances.to_json())

# convert the object into a dict
tolerances_dict = tolerances_instance.to_dict()
# create an instance of Tolerances from a dict
tolerances_from_dict = Tolerances.from_dict(tolerances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


