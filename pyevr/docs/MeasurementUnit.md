# MeasurementUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Mõõtühiku kood | [optional] 
**name** | **str** | Mõõtühiku nimetus | [optional] 

## Example

```python
from openapi_client.models.measurement_unit import MeasurementUnit

# TODO update the JSON string below
json = "{}"
# create an instance of MeasurementUnit from a JSON string
measurement_unit_instance = MeasurementUnit.from_json(json)
# print the JSON string representation of the object
print(MeasurementUnit.to_json())

# convert the object into a dict
measurement_unit_dict = measurement_unit_instance.to_dict()
# create an instance of MeasurementUnit from a dict
measurement_unit_from_dict = MeasurementUnit.from_dict(measurement_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


