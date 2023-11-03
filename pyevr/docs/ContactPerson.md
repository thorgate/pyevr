# ContactPerson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nimi | [optional] 
**phone** | **str** | Telefoninumber | [optional] 
**email** | **str** | Email | [optional] 

## Example

```python
from openapi_client.models.contact_person import ContactPerson

# TODO update the JSON string below
json = "{}"
# create an instance of ContactPerson from a JSON string
contact_person_instance = ContactPerson.from_json(json)
# print the JSON string representation of the object
print ContactPerson.to_json()

# convert the object into a dict
contact_person_dict = contact_person_instance.to_dict()
# create an instance of ContactPerson from a dict
contact_person_form_dict = contact_person.from_dict(contact_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


