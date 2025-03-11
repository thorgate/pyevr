# PagedResultOfWaybill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** | Lehekülje number | [optional] 
**page_size** | **int** | Lehekülje suurus | [optional] 
**page_result** | [**List[Waybill]**](Waybill.md) | Lehekülje tulemused | [optional] 
**total_count** | **int** | Päringu vastete arv kokku | [optional] 

## Example

```python
from openapi_client.models.paged_result_of_waybill import PagedResultOfWaybill

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResultOfWaybill from a JSON string
paged_result_of_waybill_instance = PagedResultOfWaybill.from_json(json)
# print the JSON string representation of the object
print(PagedResultOfWaybill.to_json())

# convert the object into a dict
paged_result_of_waybill_dict = paged_result_of_waybill_instance.to_dict()
# create an instance of PagedResultOfWaybill from a dict
paged_result_of_waybill_from_dict = PagedResultOfWaybill.from_dict(paged_result_of_waybill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


