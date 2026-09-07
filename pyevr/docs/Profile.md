# Profile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nime/koodi tähendus on poolte vahel eelnevalt kokku lepitud. Klassikalised näited on protsessi- või masinavälistega seotud, nt. hööveldatud (S4S), kalibreeritud, freesitud, ümardatud, S4Sr3. | [optional] 
**edges_count** | **int** | Kitsemate külgede arv töödeldud, väärtus võib olla 1 või 2. | [optional] 
**faces_count** | **int** | Laiemate külgede arv töödeldud, väärtus võib olla 1 või 2. | [optional] 
**arris_style** | **str** | Klassikalised näited on terav (mitte nõrgendatud), ümardatud, nurgalõigatud. | [optional] 
**arris_radius** | **float** | Kasutatakse koos servastiiliga, väärtus millimeetrites (mm). | [optional] 
**drawing** | [**Attachment**](Attachment.md) |  | [optional] 
**notes** | **str** | Lisamärkused. | [optional] 
**source_id** | **str** | Kauba lähetaja infosüsteemi identifikaator. | [optional] 
**target_id** | **str** | Kauba saaja infosüsteemi identifikaator. | [optional] 
**custom_data** | **object** | Api kasutaja poolt kohandatavad andmed. | [optional] 

## Example

```python
from openapi_client.models.profile import Profile

# TODO update the JSON string below
json = "{}"
# create an instance of Profile from a JSON string
profile_instance = Profile.from_json(json)
# print the JSON string representation of the object
print(Profile.to_json())

# convert the object into a dict
profile_dict = profile_instance.to_dict()
# create an instance of Profile from a dict
profile_from_dict = Profile.from_dict(profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


