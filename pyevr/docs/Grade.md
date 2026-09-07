# Grade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nime/koodi tähendus on poolte vahel eelnevalt kokku lepitud. Soovitatav kasutada vastava turu standardset märkimist või võimalikult lähedast. | [optional] 
**code_name** | **str** | Võib kasutada lisaks nime atribuudile, et muuta vastendamine lihtsamaks - see on asjakohane, kui saatev pool (API-le) ei saa anda numbrilist ID-d või GUID atribuuti. | [optional] 
**clear_faces_count** | **int** | Laiemate külgede arv ilma oksadeta. Väärtus võib olla 1 või 2. | [optional] 
**clear_edges_count** | **int** | Kitsamate külgede arv ilma oksadeta. Väärtus võib olla 1 või 2. | [optional] 
**clear_sides_type** | **str** | Näitab \&quot;kui puhas\&quot; peab pind olema, nt. mõnikord on lubatud täisoksad alla 3mm läbimõõduga. Väärtused peavad olema poolte vahel eelnevalt kokku lepitud. | [optional] 
**fj_vertical** | **bool** | Kasutatakse vertikaalseid sõrmliiteid. | [optional] 
**fj_horizontal** | **bool** | Kasutatakse horisontaalseid sõrmliiteid. | [optional] 
**fj_length** | **float** | \&quot;Sõrme\&quot; pikkus sõrmliitprotsessis millimeetrites (mm). | [optional] 
**laminated** | **str** | Tähistab servliitelist materjali. Iga väärtust võib lugeda kui \&quot;jah\&quot;, kuid andmetüüp on (mitte JahEi) jäetud avatuks, et pooled saaksid täpsemalt määratleda lamineerimise tüübi. | [optional] 
**glue** | **str** | Kasutatakse koos lamineeritud/SL-ga juhul, kui pooled soovivad täpsemalt määratleda, et liim peab olema nt. veekindel. | [optional] 
**sawing_pattern** | [**SawingPattern**](SawingPattern.md) |  | [optional] 
**heartwood_rate** | **float** | Maksimaalne % südamikust, mis võib sisalduda pakis/partiis. | [optional] 
**max_ring_width** | **float** | Määrab maksimaalse puu aasta/kasvurõnga suuruse millimeetrites (mm). | [optional] 
**roundwood_in_water** | **int** | Maksimaalne päevade arv, kui kaua ümarmaterjal (millest materjal on lõigatud) on vees olnud. | [optional] 
**reject** | **bool** | Konkreetsed tagasilükkamise põhjused saab täpsustada RejectSpecification väljal. | [optional] 
**reject_specification** | **str** | Tagasilükkamise põhjuse täpsustus. | [optional] 
**notes** | **str** | Lisamärkused. | [optional] 
**source_id** | **str** | Kauba lähetaja infosüsteemi identifikaator. | [optional] 
**target_id** | **str** | Kauba saaja infosüsteemi identifikaator. | [optional] 
**custom_data** | **object** | Api kasutaja poolt kohandatavad andmed. | [optional] 

## Example

```python
from openapi_client.models.grade import Grade

# TODO update the JSON string below
json = "{}"
# create an instance of Grade from a JSON string
grade_instance = Grade.from_json(json)
# print the JSON string representation of the object
print(Grade.to_json())

# convert the object into a dict
grade_dict = grade_instance.to_dict()
# create an instance of Grade from a dict
grade_from_dict = Grade.from_dict(grade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


