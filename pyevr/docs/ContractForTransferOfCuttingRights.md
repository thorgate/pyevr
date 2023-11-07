# ContractForTransferOfCuttingRights


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
from openapi_client.models.contract_for_transfer_of_cutting_rights import ContractForTransferOfCuttingRights

# TODO update the JSON string below
json = "{}"
# create an instance of ContractForTransferOfCuttingRights from a JSON string
contract_for_transfer_of_cutting_rights_instance = ContractForTransferOfCuttingRights.from_json(json)
# print the JSON string representation of the object
print ContractForTransferOfCuttingRights.to_json()

# convert the object into a dict
contract_for_transfer_of_cutting_rights_dict = contract_for_transfer_of_cutting_rights_instance.to_dict()
# create an instance of ContractForTransferOfCuttingRights from a dict
contract_for_transfer_of_cutting_rights_form_dict = contract_for_transfer_of_cutting_rights.from_dict(contract_for_transfer_of_cutting_rights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


