# ConsolidatedActSourceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** |  | [optional] 
**cadaster** | **str** | Katastritunnus | 
**compartment** | **str** | Kvartal | [optional] 
**assortment** | [**ShipmentAssortment**](ShipmentAssortment.md) |  | 
**amount** | **int** | Kogus | 
**unit_code** | **str** | [Mõõtühiku kood](#operation/MeasurementUnits_List) | 
**holding_base** | [**HoldingBase**](HoldingBase.md) |  | 
**forest_notice_number** | **str** | Metsateatise number | [optional] 
**contract_number** | **str** | Dokumendi number | [optional] 
**contract_date** | **datetime** | Dokumendi kuupäev | [optional] 
**certificate** | [**CertificateClaim**](CertificateClaim.md) |  | [optional] 
**previous_owner** | [**PreviousOwner**](PreviousOwner.md) |  | [optional] 

## Example

```python
from openapi_client.models.consolidated_act_source_item import ConsolidatedActSourceItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConsolidatedActSourceItem from a JSON string
consolidated_act_source_item_instance = ConsolidatedActSourceItem.from_json(json)
# print the JSON string representation of the object
print(ConsolidatedActSourceItem.to_json())

# convert the object into a dict
consolidated_act_source_item_dict = consolidated_act_source_item_instance.to_dict()
# create an instance of ConsolidatedActSourceItem from a dict
consolidated_act_source_item_from_dict = ConsolidatedActSourceItem.from_dict(consolidated_act_source_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


