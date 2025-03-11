# ForestAct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_number** | **str** | Dokumendi number | [optional] 
**contract_date** | **datetime** | Dokumendi kuupäev | [optional] 
**cadaster** | **str** | Katastritunnus | 
**compartment** | **str** | Kvartal | [optional] 
**forest_allocation_number** | **str** | Metsaeraldis | [optional] 

## Example

```python
from openapi_client.models.forest_act import ForestAct

# TODO update the JSON string below
json = "{}"
# create an instance of ForestAct from a JSON string
forest_act_instance = ForestAct.from_json(json)
# print the JSON string representation of the object
print(ForestAct.to_json())

# convert the object into a dict
forest_act_dict = forest_act_instance.to_dict()
# create an instance of ForestAct from a dict
forest_act_from_dict = ForestAct.from_dict(forest_act_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


