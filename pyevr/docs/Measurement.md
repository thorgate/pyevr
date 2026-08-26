# Measurement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Kogus | 
**pack** | [**Pack**](Pack.md) |  | [optional] 
**unit_code** | **str** | [Mõõtühiku kood](#operation/MeasurementUnits_List) | 
**assortment** | [**ShipmentAssortment**](ShipmentAssortment.md) |  | 
**moisture_percentage** | **float** | Niiskuse protsent | [optional] 
**energy_mwh** | **float** | Mõõdetud energia megavatt-tunnis | [optional] 
**measurement_report_url** | **str** | Mõõtmisandmete raporti link | [optional] 

## Example

```python
from openapi_client.models.measurement import Measurement

# TODO update the JSON string below
json = "{}"
# create an instance of Measurement from a JSON string
measurement_instance = Measurement.from_json(json)
# print the JSON string representation of the object
print(Measurement.to_json())

# convert the object into a dict
measurement_dict = measurement_instance.to_dict()
# create an instance of Measurement from a dict
measurement_from_dict = Measurement.from_dict(measurement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


