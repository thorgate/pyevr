# SalesContract


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_number** | **str** | Dokumendi number | 
**contract_date** | **datetime** | Dokumendi kuupäev | 
**cadaster** | **str** | Katastritunnus | 
**compartment** | **str** | Kvartal | [optional] 
**forest_allocation_number** | **str** | Metsaeraldis | [optional] 
**previous_owner** | [**PreviousOwner**](PreviousOwner.md) |  | 

## Example

```python
from openapi_client.models.sales_contract import SalesContract

# TODO update the JSON string below
json = "{}"
# create an instance of SalesContract from a JSON string
sales_contract_instance = SalesContract.from_json(json)
# print the JSON string representation of the object
print SalesContract.to_json()

# convert the object into a dict
sales_contract_dict = sales_contract_instance.to_dict()
# create an instance of SalesContract from a dict
sales_contract_form_dict = sales_contract.from_dict(sales_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


