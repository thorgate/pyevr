# TimberReportItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wood_type** | [**WoodType**](WoodType.md) |  | 
**log_amount** | **float** | Palkide arv (tk) | 
**wood_quality** | [**WoodQuality**](WoodQuality.md) |  | 
**defect_code** | [**DefectCode**](DefectCode.md) |  | [optional] 
**buyer_product_code** | **str** | Ostja kaubakood | [optional] 
**price_group_key** | **str** | Hinnagrupi võti | 
**tree_top_diameter_with_bark** | **float** | Ladva diameeter koorega - mm | [optional] 
**tree_top_diameter_without_bark** | **float** | Ladva diameeter kooreta - mm | 
**snag_diameter** | **float** | Tüüka diameeter - cm | [optional] 
**estimated_diameter** | **float** | Arvestuslik diameeter – cm | 
**actual_diameter** | **int** | Tegelik mõõdetud pikkus – täissentimeetrites | 
**payable_length** | **int** | Arvestuspikkus – täisdetsimeeter | 
**price** | **float** | Hind | [optional] 
**actual_volume** | **float** | Tegelik maht | [optional] 
**payable_volume** | **float** | Arvestusmaht | 
**measurer_name** | **str** | Mõõtja nimi | [optional] 

## Example

```python
from openapi_client.models.timber_report_item import TimberReportItem

# TODO update the JSON string below
json = "{}"
# create an instance of TimberReportItem from a JSON string
timber_report_item_instance = TimberReportItem.from_json(json)
# print the JSON string representation of the object
print(TimberReportItem.to_json())

# convert the object into a dict
timber_report_item_dict = timber_report_item_instance.to_dict()
# create an instance of TimberReportItem from a dict
timber_report_item_from_dict = TimberReportItem.from_dict(timber_report_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


