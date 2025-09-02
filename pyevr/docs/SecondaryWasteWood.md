# SecondaryWasteWood


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_number** | **str** | Dokumendi number | [optional] 
**contract_date** | **datetime** | Dokumendi kuupäev | [optional] 
**previous_owner** | [**PreviousOwner**](PreviousOwner.md) |  | [optional] 

## Example

```python
from openapi_client.models.secondary_waste_wood import SecondaryWasteWood

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryWasteWood from a JSON string
secondary_waste_wood_instance = SecondaryWasteWood.from_json(json)
# print the JSON string representation of the object
print(SecondaryWasteWood.to_json())

# convert the object into a dict
secondary_waste_wood_dict = secondary_waste_wood_instance.to_dict()
# create an instance of SecondaryWasteWood from a dict
secondary_waste_wood_from_dict = SecondaryWasteWood.from_dict(secondary_waste_wood_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


