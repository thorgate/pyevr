# CertificateClaim


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | [Tarneahela sertifikaadi väite kood](#operation/Certificates_List) | 
**number** | **str** | Sertifikaadi number | [optional] 

## Example

```python
from openapi_client.models.certificate_claim import CertificateClaim

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateClaim from a JSON string
certificate_claim_instance = CertificateClaim.from_json(json)
# print the JSON string representation of the object
print CertificateClaim.to_json()

# convert the object into a dict
certificate_claim_dict = certificate_claim_instance.to_dict()
# create an instance of CertificateClaim from a dict
certificate_claim_form_dict = certificate_claim.from_dict(certificate_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


