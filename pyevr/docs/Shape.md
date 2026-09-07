# Shape


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Kuju nimi. | [optional] 
**drawing** | [**Attachment**](Attachment.md) |  | [optional] 
**notes** | **str** | Lisamärkused. | [optional] 
**source_id** | **str** | Kauba lähetaja infosüsteemi identifikaator. | [optional] 
**target_id** | **str** | Kauba saaja infosüsteemi identifikaator. | [optional] 
**custom_data** | **object** | Api kasutaja poolt kohandatavad andmed. | [optional] 

## Example

```python
from openapi_client.models.shape import Shape

# TODO update the JSON string below
json = "{}"
# create an instance of Shape from a JSON string
shape_instance = Shape.from_json(json)
# print the JSON string representation of the object
print(Shape.to_json())

# convert the object into a dict
shape_dict = shape_instance.to_dict()
# create an instance of Shape from a dict
shape_from_dict = Shape.from_dict(shape_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


