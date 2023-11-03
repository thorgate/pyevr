# PagedResultOfPlaceOfDelivery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** | Lehekülje number | [optional] 
**page_size** | **int** | Lehekülje suurus | [optional] 
**page_result** | [**List[PlaceOfDelivery]**](PlaceOfDelivery.md) | Lehekülje tulemused | [optional] 
**total_count** | **int** | Päringu vastete arv kokku | [optional] 

## Example

```python
from openapi_client.models.paged_result_of_place_of_delivery import PagedResultOfPlaceOfDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResultOfPlaceOfDelivery from a JSON string
paged_result_of_place_of_delivery_instance = PagedResultOfPlaceOfDelivery.from_json(json)
# print the JSON string representation of the object
print PagedResultOfPlaceOfDelivery.to_json()

# convert the object into a dict
paged_result_of_place_of_delivery_dict = paged_result_of_place_of_delivery_instance.to_dict()
# create an instance of PagedResultOfPlaceOfDelivery from a dict
paged_result_of_place_of_delivery_form_dict = paged_result_of_place_of_delivery.from_dict(paged_result_of_place_of_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


