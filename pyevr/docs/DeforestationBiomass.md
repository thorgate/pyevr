# DeforestationBiomass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cadaster** | **str** | Katastritunnus | 
**contract_number** | **str** | Dokumendi number | [optional] 
**contract_date** | **datetime** | Dokumendi kuupäev | [optional] 

## Example

```python
from openapi_client.models.deforestation_biomass import DeforestationBiomass

# TODO update the JSON string below
json = "{}"
# create an instance of DeforestationBiomass from a JSON string
deforestation_biomass_instance = DeforestationBiomass.from_json(json)
# print the JSON string representation of the object
print(DeforestationBiomass.to_json())

# convert the object into a dict
deforestation_biomass_dict = deforestation_biomass_instance.to_dict()
# create an instance of DeforestationBiomass from a dict
deforestation_biomass_from_dict = DeforestationBiomass.from_dict(deforestation_biomass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


