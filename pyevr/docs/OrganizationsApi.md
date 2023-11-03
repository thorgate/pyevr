# openapi_client.OrganizationsApi

All URIs are relative to *https://evr.veoseleht.ee*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_list**](OrganizationsApi.md#organizations_list) | **GET** /api/organizations | Registreeritud asutuste pärimine
[**organizations_me**](OrganizationsApi.md#organizations_me) | **GET** /api/me | Päringu teostaja enda organisatsiooni andmete pärimine


# **organizations_list**
> PagedResultOfOrganization organizations_list(code_starts_with=code_starts_with, name_contains=name_contains, page=page, page_size=page_size, evr_language=evr_language)

Registreeritud asutuste pärimine

Tagastab EVR-i aktiivsed asutused.

### Example

* Api Key Authentication (SecretApiKey):
```python
import time
import os
import openapi_client
from openapi_client.models.paged_result_of_organization import PagedResultOfOrganization
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://evr.veoseleht.ee
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://evr.veoseleht.ee"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SecretApiKey
configuration.api_key['SecretApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecretApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OrganizationsApi(api_client)
    code_starts_with = 'code_starts_with_example' # str | Filtreerib asutused, mille registrikood algab otsinguterminiga (optional)
    name_contains = 'name_contains_example' # str | Filtreerib asutused, mille nimi sisaldab otsinguterminit (optional)
    page = 56 # int | Tagastatav lehekülg (optional)
    page_size = 56 # int | Tagastatava lehekülje suurus (optional)
    evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Registreeritud asutuste pärimine
        api_response = api_instance.organizations_list(code_starts_with=code_starts_with, name_contains=name_contains, page=page, page_size=page_size, evr_language=evr_language)
        print("The response of OrganizationsApi->organizations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_starts_with** | **str**| Filtreerib asutused, mille registrikood algab otsinguterminiga | [optional] 
 **name_contains** | **str**| Filtreerib asutused, mille nimi sisaldab otsinguterminit | [optional] 
 **page** | **int**| Tagastatav lehekülg | [optional] 
 **page_size** | **int**| Tagastatava lehekülje suurus | [optional] 
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

# **organizations_me**
> Organization organizations_me(evr_language=evr_language)

Päringu teostaja enda organisatsiooni andmete pärimine

Tagastab asutuse andmed

### Example

* Api Key Authentication (SecretApiKey):
```python
import time
import os
import openapi_client
from openapi_client.models.organization import Organization
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://evr.veoseleht.ee
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://evr.veoseleht.ee"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SecretApiKey
configuration.api_key['SecretApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecretApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OrganizationsApi(api_client)
    evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Päringu teostaja enda organisatsiooni andmete pärimine
        api_response = api_instance.organizations_me(evr_language=evr_language)
        print("The response of OrganizationsApi->organizations_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_me: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evr_language** | **str**| Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \&quot;et\&quot; eesti keele ning \&quot;en\&quot; inglise keele jaoks). | [optional] 

### Return type

[**Organization**](Organization.md)

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

