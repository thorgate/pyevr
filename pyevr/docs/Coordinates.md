# Coordinates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** | X koordinaat | 
**y** | **float** | Y koordinaat | 
**epsg** | **int** | EPSG formaadis koordinaatsüsteemiväärtus (näide: 3301) | [optional] 

## Example

```python
from openapi_client.models.coordinates import Coordinates

# TODO update the JSON string below
json = "{}"
# create an instance of Coordinates from a JSON string
coordinates_instance = Coordinates.from_json(json)
# print the JSON string representation of the object
print(Coordinates.to_json())

# convert the object into a dict
coordinates_dict = coordinates_instance.to_dict()
# create an instance of Coordinates from a dict
coordinates_from_dict = Coordinates.from_dict(coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


