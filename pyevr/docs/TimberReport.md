# TimberReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_number** | **str** | Mõõtmisraporti number | [optional] 
**items** | [**List[TimberReportItem]**](TimberReportItem.md) | Palgi mõõtmisraporti andmed | 
**report_date** | **datetime** | Palgi mõõtmisraporti aeg | [optional] 

## Example

```python
from openapi_client.models.timber_report import TimberReport

# TODO update the JSON string below
json = "{}"
# create an instance of TimberReport from a JSON string
timber_report_instance = TimberReport.from_json(json)
# print the JSON string representation of the object
print(TimberReport.to_json())

# convert the object into a dict
timber_report_dict = timber_report_instance.to_dict()
# create an instance of TimberReport from a dict
timber_report_from_dict = TimberReport.from_dict(timber_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


