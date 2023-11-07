# ForestNotice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cadaster** | **str** | Katastritunnus | 
**compartment** | **str** | Kvartal | [optional] 
**forest_allocation_number** | **str** | Metsaeraldis | [optional] 
**number** | **str** | Metsateatise number | [optional] 

## Example

```python
from openapi_client.models.forest_notice import ForestNotice

# TODO update the JSON string below
json = "{}"
# create an instance of ForestNotice from a JSON string
forest_notice_instance = ForestNotice.from_json(json)
# print the JSON string representation of the object
print ForestNotice.to_json()

# convert the object into a dict
forest_notice_dict = forest_notice_instance.to_dict()
# create an instance of ForestNotice from a dict
forest_notice_form_dict = forest_notice.from_dict(forest_notice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


