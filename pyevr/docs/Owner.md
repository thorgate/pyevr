# Owner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nimi | 
**code** | **str** | Isiku- või registrikood | 
**email** | **str** | Email | [optional] 
**address** | [**Address**](Address.md) |  | 
**contact_person** | [**ContactPerson**](ContactPerson.md) |  | [optional] 
**representer** | [**Representer**](Representer.md) |  | [optional] 

## Example

```python
from openapi_client.models.owner import Owner

# TODO update the JSON string below
json = "{}"
# create an instance of Owner from a JSON string
owner_instance = Owner.from_json(json)
# print the JSON string representation of the object
print Owner.to_json()

# convert the object into a dict
owner_dict = owner_instance.to_dict()
# create an instance of Owner from a dict
owner_form_dict = owner.from_dict(owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


