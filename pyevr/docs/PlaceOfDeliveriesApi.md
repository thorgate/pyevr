# openapi_client.PlaceOfDeliveriesApi

All URIs are relative to *https://evr.veoseleht.ee*

Method | HTTP request | Description
------------- | ------------- | -------------
[**place_of_deliveries_add_or_update**](PlaceOfDeliveriesApi.md#place_of_deliveries_add_or_update) | **PUT** /api/placeofdeliveries/{code} | Tarnekoha lisamine ja muutmine
[**place_of_deliveries_get**](PlaceOfDeliveriesApi.md#place_of_deliveries_get) | **GET** /api/placeofdeliveries/{code} | Tarnekoha pärimine
[**place_of_deliveries_list**](PlaceOfDeliveriesApi.md#place_of_deliveries_list) | **GET** /api/placeofdeliveries | Tarnekohtade pärimine


# **place_of_deliveries_add_or_update**
> place_of_deliveries_add_or_update(code, put_place_of_delivery_request, evr_language=evr_language)

Tarnekoha lisamine ja muutmine

Lisab uue tarnekoha. Kui antud koodiga tarnekoht juba eksisteerib, siis muudab olemasolevat tarnekohta. Loomisel märgitakse päringu tegija tarnekoha omanikuks.

### Example

* Api Key Authentication (SecretApiKey):
```python
import time
import os
import openapi_client
from openapi_client.models.put_place_of_delivery_request import PutPlaceOfDeliveryRequest
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
    api_instance = openapi_client.PlaceOfDeliveriesApi(api_client)
    code = 'code_example' # str | Kood
    put_place_of_delivery_request = openapi_client.PutPlaceOfDeliveryRequest() # PutPlaceOfDeliveryRequest | 
    evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Tarnekoha lisamine ja muutmine
        api_instance.place_of_deliveries_add_or_update(code, put_place_of_delivery_request, evr_language=evr_language)
    except Exception as e:
        print("Exception when calling PlaceOfDeliveriesApi->place_of_deliveries_add_or_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Kood | 
 **put_place_of_delivery_request** | [**PutPlaceOfDeliveryRequest**](PutPlaceOfDeliveryRequest.md)|  | 
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
**401** |  |  -  |
**403** |  |  -  |
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_of_deliveries_get**
> PlaceOfDelivery place_of_deliveries_get(code, evr_language=evr_language)

Tarnekoha pärimine

Tagastab koodile vastava tarnekoha. Pärida saab ainult enda asutusele kuuluvat tarnekohta.

### Example

* Api Key Authentication (SecretApiKey):
```python
import time
import os
import openapi_client
from openapi_client.models.place_of_delivery import PlaceOfDelivery
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
    api_instance = openapi_client.PlaceOfDeliveriesApi(api_client)
    code = 'code_example' # str | Päritava tarnekoha kood (tõstutundlik)
    evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Tarnekoha pärimine
        api_response = api_instance.place_of_deliveries_get(code, evr_language=evr_language)
        print("The response of PlaceOfDeliveriesApi->place_of_deliveries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaceOfDeliveriesApi->place_of_deliveries_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Päritava tarnekoha kood (tõstutundlik) | 
 **evr_language** | **str**| Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \&quot;et\&quot; eesti keele ning \&quot;en\&quot; inglise keele jaoks). | [optional] 

### Return type

[**PlaceOfDelivery**](PlaceOfDelivery.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_of_deliveries_list**
> PagedResultOfPlaceOfDelivery place_of_deliveries_list(name_contains=name_contains, code_starts_with=code_starts_with, register_code=register_code, address=address, page=page, page_size=page_size, evr_language=evr_language)

Tarnekohtade pärimine

Tagastab filtritele vastavad aktiivsed avalikud tarnekohad ja kõik ettevõttega seotud tarnekohad.

### Example

* Api Key Authentication (SecretApiKey):
```python
import time
import os
import openapi_client
from openapi_client.models.paged_result_of_place_of_delivery import PagedResultOfPlaceOfDelivery
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
    api_instance = openapi_client.PlaceOfDeliveriesApi(api_client)
    name_contains = 'name_contains_example' # str | Filtreerib tarnekohad, mille nimi sisaldab otsinguterminit (optional)
    code_starts_with = 'code_starts_with_example' # str | Filtreerib tarnekohad, mille kood algab otsinguterminiga (tõstutundlik) (optional)
    register_code = 'register_code_example' # str | Filtreerib ettevõtte tarnekohad, mille registrikood vastab otsinguterminile (optional)
    address = 'address_example' # str | Vabatekstiline aadressi otsing. Toetatud on järgmine süntaks: * ilma jutumärkideta tekst: sõnade vahel rakendatakse loogiline JA * jutumärkides tekst: otsitakse jutumärkides olevat lauset * OR: loogiline VÕI operaator sõnade vahel * -: loogiline EITUS (optional)
    page = 56 # int | Tagastatav lehekülg (optional)
    page_size = 56 # int | Tagastatava lehekülje suurus (optional)
    evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Tarnekohtade pärimine
        api_response = api_instance.place_of_deliveries_list(name_contains=name_contains, code_starts_with=code_starts_with, register_code=register_code, address=address, page=page, page_size=page_size, evr_language=evr_language)
        print("The response of PlaceOfDeliveriesApi->place_of_deliveries_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaceOfDeliveriesApi->place_of_deliveries_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_contains** | **str**| Filtreerib tarnekohad, mille nimi sisaldab otsinguterminit | [optional] 
 **code_starts_with** | **str**| Filtreerib tarnekohad, mille kood algab otsinguterminiga (tõstutundlik) | [optional] 
 **register_code** | **str**| Filtreerib ettevõtte tarnekohad, mille registrikood vastab otsinguterminile | [optional] 
 **address** | **str**| Vabatekstiline aadressi otsing. Toetatud on järgmine süntaks: * ilma jutumärkideta tekst: sõnade vahel rakendatakse loogiline JA * jutumärkides tekst: otsitakse jutumärkides olevat lauset * OR: loogiline VÕI operaator sõnade vahel * -: loogiline EITUS | [optional] 
 **page** | **int**| Tagastatav lehekülg | [optional] 
 **page_size** | **int**| Tagastatava lehekülje suurus | [optional] 
 **evr_language** | **str**| Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \&quot;et\&quot; eesti keele ning \&quot;en\&quot; inglise keele jaoks). | [optional] 

### Return type

[**PagedResultOfPlaceOfDelivery**](PagedResultOfPlaceOfDelivery.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** |  |  -  |
**403** |  |  -  |
**400** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

