# Minibundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **int** | Kui palju tükke (laudu) on kimbukeses horisontaalselt ühes kihis. Mittenelinurkse kimbu korral (nt. ümardatud profileeritud detailid) on see lihtsalt tükkide koguarv. | [optional] 
**rows** | **int** | Kui palju tükke (laudu) on kimbukeses vertikaalselt &#x3D; kui palju kihte. | [optional] 
**specification** | **str** | Kasutatakse siis, kui pooled kasutavad erinevaid minikimbustamise stiile, nt. otsad/täielikult plastikku mähitud, nööriga seotud. | [optional] 
**source_id** | **str** | Kauba lähetaja infosüsteemi identifikaator. | [optional] 
**target_id** | **str** | Kauba saaja infosüsteemi identifikaator. | [optional] 
**custom_data** | **object** | Api kasutaja poolt kohandatavad andmed. | [optional] 

## Example

```python
from openapi_client.models.minibundle import Minibundle

# TODO update the JSON string below
json = "{}"
# create an instance of Minibundle from a JSON string
minibundle_instance = Minibundle.from_json(json)
# print the JSON string representation of the object
print(Minibundle.to_json())

# convert the object into a dict
minibundle_dict = minibundle_instance.to_dict()
# create an instance of Minibundle from a dict
minibundle_from_dict = Minibundle.from_dict(minibundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


