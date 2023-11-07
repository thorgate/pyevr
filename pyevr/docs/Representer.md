# Representer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nimi | 
**code** | **str** | Isiku- või registrikood | 
**address** | [**Address**](Address.md) |  | 
**right_of_representation** | **str** | Esindusõiguse alus | [optional] 
**email** | **str** | Email | [optional] 
**phone** | **str** | Telefoninumber | [optional] 

## Example

```python
from openapi_client.models.representer import Representer

# TODO update the JSON string below
json = "{}"
# create an instance of Representer from a JSON string
representer_instance = Representer.from_json(json)
# print the JSON string representation of the object
print Representer.to_json()

# convert the object into a dict
representer_dict = representer_instance.to_dict()
# create an instance of Representer from a dict
representer_form_dict = representer.from_dict(representer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


