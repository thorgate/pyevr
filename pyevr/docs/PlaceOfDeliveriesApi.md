# openapi_client.PlaceOfDeliveriesApi

All URIs are relative to *https://evr-test.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**place_of_deliveries_add_or_update**](PlaceOfDeliveriesApi.md#place_of_deliveries_add_or_update) | **PUT** /api/placeofdeliveries/{code} | Tarnekoha lisamine ja muutmine
[**place_of_deliveries_get**](PlaceOfDeliveriesApi.md#place_of_deliveries_get) | **GET** /api/placeofdeliveries/{code} | Tarnekoha pärimine
[**place_of_deliveries_list**](PlaceOfDeliveriesApi.md#place_of_deliveries_list) | **GET** /api/placeofdeliveries | Tarnekohtade pärimine


# **place_of_deliveries_add_or_update**
> place_of_deliveries_add_or_update(code, put_place_of_delivery_request)

Tarnekoha lisamine ja muutmine

Lisab uue tarnekoha. Kui antud koodiga tarnekoht juba eksisteerib, siis muudab olemasolevat tarnekohta. Loomisel märgitakse päringu tegija tarnekoha omanikuks.

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
api_instance = openapi_client.PlaceOfDeliveriesApi(openapi_client.ApiClient(configuration))
code = 'code_example' # str | Kood
put_place_of_delivery_request = openapi_client.PutPlaceOfDeliveryRequest() # PutPlaceOfDeliveryRequest | 

try:
    # Tarnekoha lisamine ja muutmine
    api_instance.place_of_deliveries_add_or_update(code, put_place_of_delivery_request)
except ApiException as e:
    print("Exception when calling PlaceOfDeliveriesApi->place_of_deliveries_add_or_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Kood | 
 **put_place_of_delivery_request** | [**PutPlaceOfDeliveryRequest**](PutPlaceOfDeliveryRequest.md)|  | 

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
> PlaceOfDelivery place_of_deliveries_get(code)

Tarnekoha pärimine

Tagastab koodile vastava tarnekoha. Pärida saab ainult enda asutusele kuuluvat tarnekohta.

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
api_instance = openapi_client.PlaceOfDeliveriesApi(openapi_client.ApiClient(configuration))
code = 'code_example' # str | Päritava tarnekoha kood

try:
    # Tarnekoha pärimine
    api_response = api_instance.place_of_deliveries_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaceOfDeliveriesApi->place_of_deliveries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Päritava tarnekoha kood | 

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
> PagedResultOfPlaceOfDelivery place_of_deliveries_list(name_contains=name_contains, code_starts_with=code_starts_with, register_code=register_code, address=address, page=page)

Tarnekohtade pärimine

Tagastab filtritele vastavad aktiivsed avalikud tarnekohad ja kõik ettevõttega seotud tarnekohad.

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
api_instance = openapi_client.PlaceOfDeliveriesApi(openapi_client.ApiClient(configuration))
name_contains = 'name_contains_example' # str | Filtreerib tarnekohad, mille nimi sisaldab otsinguterminit (optional)
code_starts_with = 'code_starts_with_example' # str | Filtreerib tarnekohad, mille kood algab otsinguterminiga (optional)
register_code = 'register_code_example' # str | Filtreerib ettevõtte tarnekohad, mille registrikood vastab otsinguterminile   (optional)
address = 'address_example' # str | Vabatekstiline aadressi otsing. Toetatud on järgmine süntaks: * ilma jutumärkideta tekst: sõnade vahel rakendatakse loogiline JA. * jutumärkides tekst: otsitakse jutumärkides olevat lauset. * OR: loogiline VÕI operaator sõnade vahel. * -: loogiline EITUS. (optional)
page = 56 # int | Tagastatav lehekülg (optional)

try:
    # Tarnekohtade pärimine
    api_response = api_instance.place_of_deliveries_list(name_contains=name_contains, code_starts_with=code_starts_with, register_code=register_code, address=address, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaceOfDeliveriesApi->place_of_deliveries_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_contains** | **str**| Filtreerib tarnekohad, mille nimi sisaldab otsinguterminit | [optional] 
 **code_starts_with** | **str**| Filtreerib tarnekohad, mille kood algab otsinguterminiga | [optional] 
 **register_code** | **str**| Filtreerib ettevõtte tarnekohad, mille registrikood vastab otsinguterminile   | [optional] 
 **address** | **str**| Vabatekstiline aadressi otsing. Toetatud on järgmine süntaks: * ilma jutumärkideta tekst: sõnade vahel rakendatakse loogiline JA. * jutumärkides tekst: otsitakse jutumärkides olevat lauset. * OR: loogiline VÕI operaator sõnade vahel. * -: loogiline EITUS. | [optional] 
 **page** | **int**| Tagastatav lehekülg | [optional] 

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
