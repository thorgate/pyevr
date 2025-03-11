# AddMeasurementActRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**act_number** | **str** | Mõõtmisakti number | [optional] 
**act_date** | **datetime** | Mõõtmisakti kuupäev | [optional] 
**measurements** | [**List[Measurement]**](Measurement.md) | Mõõtmistulemused | [optional] 
**custom_measurement_data** | **object** | Mõõtmistulemused vabas formaadis. | [optional] 
**total** | [**Total**](Total.md) |  | [optional] 

## Example

```python
from openapi_client.models.add_measurement_act_request import AddMeasurementActRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddMeasurementActRequest from a JSON string
add_measurement_act_request_instance = AddMeasurementActRequest.from_json(json)
# print the JSON string representation of the object
print(AddMeasurementActRequest.to_json())

# convert the object into a dict
add_measurement_act_request_dict = add_measurement_act_request_instance.to_dict()
# create an instance of AddMeasurementActRequest from a dict
add_measurement_act_request_from_dict = AddMeasurementActRequest.from_dict(add_measurement_act_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


