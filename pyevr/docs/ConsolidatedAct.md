# ConsolidatedAct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_number** | **str** | Dokumendi number | 
**contract_date** | **datetime** | Dokumendi kuupäev | 
**cadaster** | **str** | Katastritunnus | 
**compartment** | **str** | Kvartal | [optional] 
**forest_allocation_number** | **str** | Metsaeraldis | [optional] 

## Example

```python
from openapi_client.models.consolidated_act import ConsolidatedAct

# TODO update the JSON string below
json = "{}"
# create an instance of ConsolidatedAct from a JSON string
consolidated_act_instance = ConsolidatedAct.from_json(json)
# print the JSON string representation of the object
print ConsolidatedAct.to_json()

# convert the object into a dict
consolidated_act_dict = consolidated_act_instance.to_dict()
# create an instance of ConsolidatedAct from a dict
consolidated_act_form_dict = consolidated_act.from_dict(consolidated_act_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


