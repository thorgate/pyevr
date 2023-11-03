# Transport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transporter** | [**Transporter**](Transporter.md) |  | 
**driver_name** | **str** | Autojuhi nimi | 
**driver_id_code** | **str** | Autojuhi isikukood | 
**driver_phone** | **str** | Autojuhi telefoninumber | [optional] 
**van_registration_number** | **str** | Veoki riiklik registreerimisnumber | 
**trailer_registration_number** | **str** | Haagise kasutamise korral haagise riiklik registreerimisnumber | [optional] 

## Example

```python
from openapi_client.models.transport import Transport

# TODO update the JSON string below
json = "{}"
# create an instance of Transport from a JSON string
transport_instance = Transport.from_json(json)
# print the JSON string representation of the object
print Transport.to_json()

# convert the object into a dict
transport_dict = transport_instance.to_dict()
# create an instance of Transport from a dict
transport_form_dict = transport.from_dict(transport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


