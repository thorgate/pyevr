# Source


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Maaüksuse või laoplatsi nimi | 
**code** | **str** | Laokood | [optional] 
**compartment** | **str** | Kvartal | [optional] 
**appropriation** | **str** | Eraldis | [optional] 
**planning_area** | **str** | Planeerimispiirkond | [optional] 
**address** | [**Address**](Address.md) |  | 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 
**contact_person** | [**ContactPerson**](ContactPerson.md) |  | [optional] 
**near_address** | **str** | Lähiaadress | [optional] 
**source_document_url** | **str** | Päritoludokumendi URL | [optional] 

## Example

```python
from openapi_client.models.source import Source

# TODO update the JSON string below
json = "{}"
# create an instance of Source from a JSON string
source_instance = Source.from_json(json)
# print the JSON string representation of the object
print(Source.to_json())

# convert the object into a dict
source_dict = source_instance.to_dict()
# create an instance of Source from a dict
source_from_dict = Source.from_dict(source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


