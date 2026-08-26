# Pack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack_number** | **int** | Paki number | 
**length** | **float** | Koormapaki pikkus | 
**height** | **float** | Koosmapaki kõrgus | 
**width** | **float** | Koormapaki laius | 
**coefficient** | **float** | Koeffitsient | 
**location** | [**PackLocation**](PackLocation.md) |  | 

## Example

```python
from openapi_client.models.pack import Pack

# TODO update the JSON string below
json = "{}"
# create an instance of Pack from a JSON string
pack_instance = Pack.from_json(json)
# print the JSON string representation of the object
print(Pack.to_json())

# convert the object into a dict
pack_dict = pack_instance.to_dict()
# create an instance of Pack from a dict
pack_from_dict = Pack.from_dict(pack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


