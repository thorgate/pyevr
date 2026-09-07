# SawnWood


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**species** | [**List[Species]**](Species.md) | Puiduliigid. | 
**grade** | [**Grade**](Grade.md) |  | [optional] 
**thickness** | **float** | Väärtus millimeetrites (mm). Vaata loogikat Puiduklassi dokumentatsioonis dimensioonide jaotises. | 
**width** | **float** | Väärtus millimeetrites (mm). Vaata loogikat Puiduklassi dokumentatsioonis dimensioonide jaotises. | 
**thickness2** | **float** | Väärtus millimeetrites (mm). Vaata loogikat Puiduklassi dokumentatsioonis dimensioonide jaotises. Tuleb täita, kui width2 on määratud. | [optional] 
**width2** | **float** | Väärtus millimeetrites (mm). Vaata loogikat Puiduklassi dokumentatsioonis dimensioonide jaotises. Tuleb täita, kui thickness2 on määratud. | [optional] 
**thickness3** | **float** | Väärtus millimeetrites (mm). Vaata loogikat Puiduklassi dokumentatsioonis dimensioonide jaotises. Tuleb täita, kui width3 on määratud. | [optional] 
**width3** | **float** | Väärtus millimeetrites (mm). Vaata loogikat Puiduklassi dokumentatsioonis dimensioonide jaotises. Tuleb täita, kui thickness3 on määratud. | [optional] 
**ppp** | **int** | Tükki paki kohta (TPK) ei tohi täita, kui on olemas täpne pakendi kirjeldus koos pakipikkuse atribuudiga. | [optional] 
**treatment** | [**Treatment**](Treatment.md) |  | [optional] 
**profile** | [**Profile**](Profile.md) |  | [optional] 
**minibundle** | [**Minibundle**](Minibundle.md) |  | [optional] 
**epd_gwp** | **float** | Toote keskkonnadeklaratsioonid (TKD) mõõdavad globaalse soojenemise potentsiaali (GSP) kuupmeetri (m³) kohta. | [optional] 
**tolerances** | [**Tolerances**](Tolerances.md) |  | [optional] 
**packing** | [**Packing**](Packing.md) |  | [optional] 
**notes** | **str** | Lisamärkused. | [optional] 
**source_id** | **str** | Kauba lähetaja infosüsteemi identifikaator. | [optional] 
**target_id** | **str** | Kauba saaja infosüsteemi identifikaator. | [optional] 
**custom_data** | **object** | Api kasutaja poolt kohandatavad andmed. | [optional] 
**article_id** | **str** | Toote identifikaator, nagu partnerite vahel kokku lepitud. See võib dubleerida osa teist atribuutidest olevat teavet või kirjeldada kaupu täielikult - sellisel juhul võivad kõik teised atribuudid olla tühjad. | [optional] 
**article_name** | **str** | Seda tuleks täita ainult siis, kui pooled on kokku leppinud artiklite sisestamises jooksvalt sihtkoha süsteemi API kaudu. | [optional] 
**ean** | **str** | Rahvusvaheline artiklite number (tuntud ka kui Euroopa artiklite number või EAN) GS1 organisatsioonilt. API-d võivad väärtust piirata 13-kohalise piiranguga. | [optional] 
**ean2** | **str** | Kasutatakse, kui toodet nt. saadetakse otse kliendi kliendile, kes müüb neid edasi oma tootena erineva EAN-i all. | [optional] 
**certificate_statement** | [**CertificateStatement**](CertificateStatement.md) |  | [optional] 

## Example

```python
from openapi_client.models.sawn_wood import SawnWood

# TODO update the JSON string below
json = "{}"
# create an instance of SawnWood from a JSON string
sawn_wood_instance = SawnWood.from_json(json)
# print the JSON string representation of the object
print(SawnWood.to_json())

# convert the object into a dict
sawn_wood_dict = sawn_wood_instance.to_dict()
# create an instance of SawnWood from a dict
sawn_wood_from_dict = SawnWood.from_dict(sawn_wood_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


