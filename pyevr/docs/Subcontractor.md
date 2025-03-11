# Subcontractor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nimi | 
**code** | **str** | Isiku- või registrikood | 
**contact_person** | [**ContactPerson**](ContactPerson.md) |  | [optional] 

## Example

```python
from openapi_client.models.subcontractor import Subcontractor

# TODO update the JSON string below
json = "{}"
# create an instance of Subcontractor from a JSON string
subcontractor_instance = Subcontractor.from_json(json)
# print the JSON string representation of the object
print(Subcontractor.to_json())

# convert the object into a dict
subcontractor_dict = subcontractor_instance.to_dict()
# create an instance of Subcontractor from a dict
subcontractor_from_dict = Subcontractor.from_dict(subcontractor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


