# openapi_client.AssortmentsApi

All URIs are relative to *https://evr.veoseleht.ee*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assortments_list**](AssortmentsApi.md#assortments_list) | **GET** /api/assortments | Sortimentide pärimine


# **assortments_list**
> PagedResultOfAssortment assortments_list(page=page, page_size=page_size, evr_language=evr_language)

Sortimentide pärimine

Tagastab EVR-i aktiivsed sortimendid.

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

# Defining host is optional and default to https://evr.veoseleht.ee
configuration.host = "https://evr.veoseleht.ee"

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssortmentsApi(api_client)
    page = 56 # int | Tagastatav lehekülg (optional)
page_size = 56 # int | Tagastatava lehekülje suurus (optional)
evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Sortimentide pärimine
        api_response = api_instance.assortments_list(page=page, page_size=page_size, evr_language=evr_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssortmentsApi->assortments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Tagastatav lehekülg | [optional] 
 **page_size** | **int**| Tagastatava lehekülje suurus | [optional] 
 **evr_language** | **str**| Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \&quot;et\&quot; eesti keele ning \&quot;en\&quot; inglise keele jaoks). | [optional] 

### Return type

[**PagedResultOfAssortment**](PagedResultOfAssortment.md)

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

