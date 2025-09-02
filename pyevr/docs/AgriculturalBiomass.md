# AgriculturalBiomass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_number** | **str** | Dokumendi number | [optional] 
**contract_date** | **datetime** | Dokumendi kuupäev | [optional] 
**cadaster** | **str** | Katastritunnus | 
**agricultural_area_name** | **str** | Kõlviku nimetus | [optional] 
**previous_owner** | [**PreviousOwner**](PreviousOwner.md) |  | [optional] 

## Example

```python
from openapi_client.models.agricultural_biomass import AgriculturalBiomass

# TODO update the JSON string below
json = "{}"
# create an instance of AgriculturalBiomass from a JSON string
agricultural_biomass_instance = AgriculturalBiomass.from_json(json)
# print the JSON string representation of the object
print(AgriculturalBiomass.to_json())

# convert the object into a dict
agricultural_biomass_dict = agricultural_biomass_instance.to_dict()
# create an instance of AgriculturalBiomass from a dict
agricultural_biomass_from_dict = AgriculturalBiomass.from_dict(agricultural_biomass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


