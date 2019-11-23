# openapi_client.OrganizationsApi

All URIs are relative to *https://evr-test.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_list**](OrganizationsApi.md#organizations_list) | **GET** /api/organizations | Registreeritud asutuste pärimine


# **organizations_list**
> PagedResultOfOrganization organizations_list(code_starts_with=code_starts_with, name_contains=name_contains, page=page, evr_language=evr_language)

Registreeritud asutuste pärimine

Tagastab EVR-i aktiivsed asutused.

### Example

* Api Key Authentication (SecretApiKey):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: SecretApiKey
configuration.api_key['EVR-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['EVR-APIKEY'] = 'Bearer'

# Defining host is optional and default to https://evr-test.azurewebsites.net
configuration.host = "https://evr-test.azurewebsites.net"
# Create an instance of the API class
api_instance = openapi_client.OrganizationsApi(openapi_client.ApiClient(configuration))
code_starts_with = 'code_starts_with_example' # str | Filtreerib asutused, mille registrikood algab otsinguterminiga (optional)
name_contains = 'name_contains_example' # str | Filtreerib asutused, mille nimi sisaldab otsinguterminit (optional)
page = 56 # int | Tagastatav lehekülg (optional)
evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

try:
    # Registreeritud asutuste pärimine
    api_response = api_instance.organizations_list(code_starts_with=code_starts_with, name_contains=name_contains, page=page, evr_language=evr_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_starts_with** | **str**| Filtreerib asutused, mille registrikood algab otsinguterminiga | [optional] 
 **name_contains** | **str**| Filtreerib asutused, mille nimi sisaldab otsinguterminit | [optional] 
 **page** | **int**| Tagastatav lehekülg | [optional] 
 **evr_language** | **str**| Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \&quot;et\&quot; eesti keele ning \&quot;en\&quot; inglise keele jaoks). | [optional] 

### Return type

[**PagedResultOfOrganization**](PagedResultOfOrganization.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** |  |  -  |
**401** |  |  -  |
**400** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

