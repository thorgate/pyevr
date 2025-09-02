# SecondaryWoodBiomass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_number** | **str** | Dokumendi number | [optional] 
**contract_date** | **datetime** | Dokumendi kuupäev | [optional] 
**previous_owner** | [**PreviousOwner**](PreviousOwner.md) |  | [optional] 

## Example

```python
from openapi_client.models.secondary_wood_biomass import SecondaryWoodBiomass

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryWoodBiomass from a JSON string
secondary_wood_biomass_instance = SecondaryWoodBiomass.from_json(json)
# print the JSON string representation of the object
print(SecondaryWoodBiomass.to_json())

# convert the object into a dict
secondary_wood_biomass_dict = secondary_wood_biomass_instance.to_dict()
# create an instance of SecondaryWoodBiomass from a dict
secondary_wood_biomass_from_dict = SecondaryWoodBiomass.from_dict(secondary_wood_biomass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


