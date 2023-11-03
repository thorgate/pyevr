# Transporter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nimi | 
**code** | **str** | Isiku- või registrikood | 
**contact_person** | [**ContactPerson**](ContactPerson.md) |  | [optional] 

## Example

```python
from openapi_client.models.transporter import Transporter

# TODO update the JSON string below
json = "{}"
# create an instance of Transporter from a JSON string
transporter_instance = Transporter.from_json(json)
# print the JSON string representation of the object
print Transporter.to_json()

# convert the object into a dict
transporter_dict = transporter_instance.to_dict()
# create an instance of Transporter from a dict
transporter_form_dict = transporter.from_dict(transporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


