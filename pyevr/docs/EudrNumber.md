# EudrNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_number** | **str** | Viitenumber | [optional] 
**verification_number** | **str** | Kontroll number | [optional] 

## Example

```python
from openapi_client.models.eudr_number import EudrNumber

# TODO update the JSON string below
json = "{}"
# create an instance of EudrNumber from a JSON string
eudr_number_instance = EudrNumber.from_json(json)
# print the JSON string representation of the object
print(EudrNumber.to_json())

# convert the object into a dict
eudr_number_dict = eudr_number_instance.to_dict()
# create an instance of EudrNumber from a dict
eudr_number_from_dict = EudrNumber.from_dict(eudr_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


