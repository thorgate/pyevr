# AddTimberReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_number** | **str** | Mõõtmisraporti number | [optional] 
**items** | [**List[TimberReportItem]**](TimberReportItem.md) | Palgi mõõtmisraporti andmed | 
**report_date** | **datetime** | Palgi mõõtmisraporti aeg | [optional] 

## Example

```python
from openapi_client.models.add_timber_report_request import AddTimberReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTimberReportRequest from a JSON string
add_timber_report_request_instance = AddTimberReportRequest.from_json(json)
# print the JSON string representation of the object
print(AddTimberReportRequest.to_json())

# convert the object into a dict
add_timber_report_request_dict = add_timber_report_request_instance.to_dict()
# create an instance of AddTimberReportRequest from a dict
add_timber_report_request_from_dict = AddTimberReportRequest.from_dict(add_timber_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


