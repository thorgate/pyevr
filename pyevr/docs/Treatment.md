# Treatment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nime/koodi tähendus on poolte vahel eelnevalt kokku lepitud. Mõned klassikalised näited on KK10% Tanalith, Must värvitud teritatud, Intensiivne-termo soontega. | [optional] 
**seasoning** | [**Seasoning**](Seasoning.md) |  | [optional] 
**impregnation** | [**Impregnation**](Impregnation.md) |  | [optional] 
**surface** | [**Surface**](Surface.md) |  | [optional] 
**shape** | [**Shape**](Shape.md) |  | [optional] 
**other** | **str** | Kõik muud omadused Töötlusüksuse definitsioonis kirjeldatud, mis ei kuulu allpool ühegi komponendi alla, nt. kaubamärgiga märgistatud. | [optional] 
**notes** | **str** | Lisamärkused. | [optional] 
**source_id** | **str** | Kauba lähetaja infosüsteemi identifikaator. | [optional] 
**target_id** | **str** | Kauba saaja infosüsteemi identifikaator. | [optional] 
**custom_data** | **object** | Api kasutaja poolt kohandatavad andmed. | [optional] 

## Example

```python
from openapi_client.models.treatment import Treatment

# TODO update the JSON string below
json = "{}"
# create an instance of Treatment from a JSON string
treatment_instance = Treatment.from_json(json)
# print the JSON string representation of the object
print(Treatment.to_json())

# convert the object into a dict
treatment_dict = treatment_instance.to_dict()
# create an instance of Treatment from a dict
treatment_from_dict = Treatment.from_dict(treatment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


