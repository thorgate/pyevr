# CertificateStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_type** | [**CertificateType**](CertificateType.md) |  | 
**certificate_number** | **str** | Asutusele väljastatud sertifikaadi number | 
**percent** | **float** | Kohustuslik ja lubatud ainult tüüpide &#39;FscMixPercent&#39; ja &#39;PefcCertified&#39; puhul. | [optional] 

## Example

```python
from openapi_client.models.certificate_statement import CertificateStatement

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateStatement from a JSON string
certificate_statement_instance = CertificateStatement.from_json(json)
# print the JSON string representation of the object
print(CertificateStatement.to_json())

# convert the object into a dict
certificate_statement_dict = certificate_statement_instance.to_dict()
# create an instance of CertificateStatement from a dict
certificate_statement_from_dict = CertificateStatement.from_dict(certificate_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


