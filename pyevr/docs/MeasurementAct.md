# MeasurementAct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**act_number** | **str** | Mõõtmisakti number | [optional] 
**act_date** | **datetime** | Mõõtmisakti kuupäev | [optional] 
**measurements** | [**List[Measurement]**](Measurement.md) | Mõõtmistulemused EVR poolt sätestatud formaadis  | [optional] 
**custom_measurement_data** | **object** | Mõõtmistulemused vabas formaadis | [optional] 
**measurer_code** | **str** | Mõõtja registri kood | [optional] 
**creation_time** | **datetime** | Lisamise aeg | [optional] 
**total** | [**Total**](Total.md) |  | [optional] 

## Example

```python
from openapi_client.models.measurement_act import MeasurementAct

# TODO update the JSON string below
json = "{}"
# create an instance of MeasurementAct from a JSON string
measurement_act_instance = MeasurementAct.from_json(json)
# print the JSON string representation of the object
print(MeasurementAct.to_json())

# convert the object into a dict
measurement_act_dict = measurement_act_instance.to_dict()
# create an instance of MeasurementAct from a dict
measurement_act_from_dict = MeasurementAct.from_dict(measurement_act_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


