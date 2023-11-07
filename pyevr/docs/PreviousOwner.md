# PreviousOwner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nimi | 
**code** | **str** | Eelmiste omanike isiku- või registrikoodid | 
**address** | **str** | Aadress | 

## Example

```python
from openapi_client.models.previous_owner import PreviousOwner

# TODO update the JSON string below
json = "{}"
# create an instance of PreviousOwner from a JSON string
previous_owner_instance = PreviousOwner.from_json(json)
# print the JSON string representation of the object
print PreviousOwner.to_json()

# convert the object into a dict
previous_owner_dict = previous_owner_instance.to_dict()
# create an instance of PreviousOwner from a dict
previous_owner_form_dict = previous_owner.from_dict(previous_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


