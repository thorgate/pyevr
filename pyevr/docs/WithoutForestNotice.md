# WithoutForestNotice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cadaster** | **str** | Katastritunnus | 
**compartment** | **str** | Kvartal | [optional] 
**forest_allocation_number** | **str** | Metsaeraldis | [optional] 

## Example

```python
from openapi_client.models.without_forest_notice import WithoutForestNotice

# TODO update the JSON string below
json = "{}"
# create an instance of WithoutForestNotice from a JSON string
without_forest_notice_instance = WithoutForestNotice.from_json(json)
# print the JSON string representation of the object
print WithoutForestNotice.to_json()

# convert the object into a dict
without_forest_notice_dict = without_forest_notice_instance.to_dict()
# create an instance of WithoutForestNotice from a dict
without_forest_notice_form_dict = without_forest_notice.from_dict(without_forest_notice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


