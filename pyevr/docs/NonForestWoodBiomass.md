# NonForestWoodBiomass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cadaster** | **str** | Katastritunnus | 
**contract_number** | **str** | Dokumendi number | [optional] 
**contract_date** | **datetime** | Dokumendi kuupäev | [optional] 
**previous_owner** | [**PreviousOwner**](PreviousOwner.md) |  | [optional] 

## Example

```python
from openapi_client.models.non_forest_wood_biomass import NonForestWoodBiomass

# TODO update the JSON string below
json = "{}"
# create an instance of NonForestWoodBiomass from a JSON string
non_forest_wood_biomass_instance = NonForestWoodBiomass.from_json(json)
# print the JSON string representation of the object
print(NonForestWoodBiomass.to_json())

# convert the object into a dict
non_forest_wood_biomass_dict = non_forest_wood_biomass_instance.to_dict()
# create an instance of NonForestWoodBiomass from a dict
non_forest_wood_biomass_from_dict = NonForestWoodBiomass.from_dict(non_forest_wood_biomass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


