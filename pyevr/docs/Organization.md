# Organization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Asutuse nimi | [optional] 
**waybill_number_prefix** | **str** |  | [optional] 
**register_code** | **str** | Registrikood | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**email** | **str** | Asutuse üldemail | [optional] 
**phone** | **str** | Asutuse üldtelefon | [optional] 
**contact_persons** | [**List[ContactPerson]**](ContactPerson.md) | Kontaktisikud | [optional] 

## Example

```python
from openapi_client.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


