# InventoryAct


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
from openapi_client.models.inventory_act import InventoryAct

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAct from a JSON string
inventory_act_instance = InventoryAct.from_json(json)
# print the JSON string representation of the object
print InventoryAct.to_json()

# convert the object into a dict
inventory_act_dict = inventory_act_instance.to_dict()
# create an instance of InventoryAct from a dict
inventory_act_form_dict = inventory_act.from_dict(inventory_act_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


