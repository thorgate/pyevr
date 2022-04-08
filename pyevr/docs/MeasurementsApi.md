# openapi_client.MeasurementsApi

All URIs are relative to *https://evr.veoseleht.ee*

Method | HTTP request | Description
------------- | ------------- | -------------
[**measurements_get**](MeasurementsApi.md#measurements_get) | **GET** /api/waybills/{number}/measurements | Veoselehe mõõtmisandmete pärimine
[**measurements_post**](MeasurementsApi.md#measurements_post) | **POST** /api/waybills/{number}/measurements | Veoselehele mõõtmisandmete lisamine


# **measurements_get**
> PagedResultOfMeasurementAct measurements_get(number, page=page, evr_language=evr_language)

Veoselehe mõõtmisandmete pärimine

Tagastab veoselehega seotud mõõtmisandmed.

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
    api_instance = openapi_client.MeasurementsApi(api_client)
    number = 'number_example' # str | Veoselehe number (tõstutundetu)
page = 1 # int | Tagastatav lehekülg (optional) (default to 1)
evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Veoselehe mõõtmisandmete pärimine
        api_response = api_instance.measurements_get(number, page=page, evr_language=evr_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MeasurementsApi->measurements_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Veoselehe number (tõstutundetu) | 
 **page** | **int**| Tagastatav lehekülg | [optional] [default to 1]
 **evr_language** | **str**| Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \&quot;et\&quot; eesti keele ning \&quot;en\&quot; inglise keele jaoks). | [optional] 

### Return type

[**PagedResultOfMeasurementAct**](PagedResultOfMeasurementAct.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** |  |  -  |
**403** |  |  -  |
**401** |  |  -  |
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measurements_post**
> measurements_post(number, add_measurement_act_request, evr_language=evr_language)

Veoselehele mõõtmisandmete lisamine

Lisab veoselehele mõõtmisandmed. Mõõtmisandmeid saab lisada \"koorem maas\" staatuses veoselehele sellele märgitud veose saaja või tema volitatud mõõtja. Mõõtmistulemusi on võimalik lisada koormapakkidena või lihtsalt sortimentide kogustena.

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
    api_instance = openapi_client.MeasurementsApi(api_client)
    number = 'number_example' # str | Veoselehe number (tõstutundetu)
add_measurement_act_request = openapi_client.AddMeasurementActRequest() # AddMeasurementActRequest | Mõõtmisandmed
evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Veoselehele mõõtmisandmete lisamine
        api_instance.measurements_post(number, add_measurement_act_request, evr_language=evr_language)
    except ApiException as e:
        print("Exception when calling MeasurementsApi->measurements_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Veoselehe number (tõstutundetu) | 
 **add_measurement_act_request** | [**AddMeasurementActRequest**](AddMeasurementActRequest.md)| Mõõtmisandmed | 
 **evr_language** | **str**| Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \&quot;et\&quot; eesti keele ning \&quot;en\&quot; inglise keele jaoks). | [optional] 

### Return type

void (empty response body)

### Authorization

[SecretApiKey](../README.md#SecretApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** |  |  -  |
**403** |  |  -  |
**401** |  |  -  |
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

