# Assortment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Sortimendi kood | [optional] 
**product_group_code** | **str** | Sortimendi tootegrupp | [optional] 
**name** | **str** | Sortimendi nimi | [optional] 
**measurement_unit_code** | **str** | Sortimendi mõõtühik | [optional] 

## Example

```python
from openapi_client.models.assortment import Assortment

# TODO update the JSON string below
json = "{}"
# create an instance of Assortment from a JSON string
assortment_instance = Assortment.from_json(json)
# print the JSON string representation of the object
print(Assortment.to_json())

# convert the object into a dict
assortment_dict = assortment_instance.to_dict()
# create an instance of Assortment from a dict
assortment_from_dict = Assortment.from_dict(assortment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


