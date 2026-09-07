# SawnPack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_number** | **int** | Järjekorranumber, mida sageli nimetatakse \&quot;positsiooniks\&quot; selles veokirjas või partiis. Väärtused peaksid olema numbrid nagu 1 .. 30 (nt.) ilma lünkadeta. | [optional] 
**pack_number** | **str** | Unikaalne identifikaator, mis on pakile trükitud / kirjutatud. Tavaliselt on see lisaks ka triipkoodiga ja/või QR-koodiga. | [optional] 
**marking** | **str** | Identifikaator, mis on tavaliselt pakile trükitud või kirjutatud, et täpsustada (eristada) partiid/kihti, mida tuleb koos käidelda. Erinevalt pakinumbri atribuudist see EI ole unikaalne. | [optional] 
**pieces** | [**List[SawnPackLength]**](SawnPackLength.md) | Tavalise fikseeritud pikkusega paki korral sisaldab nimekiri ainult 1 elementi. | [optional] 
**contract** | **str** | Viide müügi-/ostulepingule. | [optional] 
**volume** | **float** | Kogu paki kogus kuupmeetrites (m³). | 
**running_meters** | **float** | Kogu paki kogus meetrites (m) ehk kõigi laudade pikkuste summa. | [optional] 
**price** | [**Price**](Price.md) |  | [optional] 
**creation** | **datetime** | See on peamiselt paki vanuse hõlpsaks määramiseks. | [optional] 
**notes** | **str** | Lisamärkused. | [optional] 
**source_id** | **str** | Kauba lähetaja infosüsteemi identifikaator. | [optional] 
**target_id** | **str** | Kauba saaja infosüsteemi identifikaator. | [optional] 
**custom_data** | **object** | Api kasutaja poolt kohandatavad andmed. | [optional] 

## Example

```python
from openapi_client.models.sawn_pack import SawnPack

# TODO update the JSON string below
json = "{}"
# create an instance of SawnPack from a JSON string
sawn_pack_instance = SawnPack.from_json(json)
# print the JSON string representation of the object
print(SawnPack.to_json())

# convert the object into a dict
sawn_pack_dict = sawn_pack_instance.to_dict()
# create an instance of SawnPack from a dict
sawn_pack_from_dict = SawnPack.from_dict(sawn_pack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


