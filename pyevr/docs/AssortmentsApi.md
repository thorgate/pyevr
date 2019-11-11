# openapi_client.AssortmentsApi

All URIs are relative to *https://evr-test.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assortments_list**](AssortmentsApi.md#assortments_list) | **GET** /api/assortments | Sortimentide pärimine


# **assortments_list**
> PagedResultOfAssortment assortments_list(page=page)

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

# Defining host is optional and default to https://evr-test.azurewebsites.net
configuration.host = "https://evr-test.azurewebsites.net"
# Create an instance of the API class
api_instance = openapi_client.AssortmentsApi(openapi_client.ApiClient(configuration))
page = 56 # int | Tagastatav lehekülg (optional)

try:
    # Sortimentide pärimine
    api_response = api_instance.assortments_list(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssortmentsApi->assortments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Tagastatav lehekülg | [optional] 

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

