# openapi_client.WaybillsApi

All URIs are relative to *https://evr.veoseleht.ee*

Method | HTTP request | Description
------------- | ------------- | -------------
[**waybills_add_note**](WaybillsApi.md#waybills_add_note) | **POST** /api/waybills/{number}/note | Veoselehe märkuse lisamine
[**waybills_add_shipments**](WaybillsApi.md#waybills_add_shipments) | **POST** /api/waybills/{number}/shipments | Veoselehele veose lisamine
[**waybills_cancel**](WaybillsApi.md#waybills_cancel) | **POST** /api/waybills/{number}/cancel | Veoselehe tühistamine
[**waybills_finish**](WaybillsApi.md#waybills_finish) | **POST** /api/waybills/{number}/finish | Veoselehe lõpetamine
[**waybills_list**](WaybillsApi.md#waybills_list) | **GET** /api/waybills | Veoselehtede pärimine
[**waybills_get**](WaybillsApi.md#waybills_get) | **GET** /api/waybills/{number} | Veoselehe pärimine
[**waybills_post**](WaybillsApi.md#waybills_post) | **POST** /api/waybills | Veoselehe loomine
[**waybills_unload**](WaybillsApi.md#waybills_unload) | **POST** /api/waybills/{number}/unload | Veoselehel veo lõpetamine


# **waybills_add_note**
> waybills_add_note(number, add_waybill_note_request, evr_language=evr_language)

Veoselehe märkuse lisamine

Lisab veoselehele uue märkuse. Olemasolevaid märkuseid ei muudeta. Märkust saavad lisada kõik veoselehega seotud osapooled (v.a volitatud vaatleja).

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
    api_instance = openapi_client.WaybillsApi(api_client)
    number = 'number_example' # str | Veoselehe number (tõstutundetu)
add_waybill_note_request = openapi_client.AddWaybillNoteRequest() # AddWaybillNoteRequest | 
evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Veoselehe märkuse lisamine
        api_instance.waybills_add_note(number, add_waybill_note_request, evr_language=evr_language)
    except ApiException as e:
        print("Exception when calling WaybillsApi->waybills_add_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Veoselehe number (tõstutundetu) | 
 **add_waybill_note_request** | [**AddWaybillNoteRequest**](AddWaybillNoteRequest.md)|  | 
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
**404** |  |  -  |
**400** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **waybills_add_shipments**
> waybills_add_shipments(number, add_shipments_to_waybill_request, evr_language=evr_language)

Veoselehele veose lisamine

Lisab veoselehele uue veose. Veoseid saab lisada veoselehele vedaja ja veoselehe looja. Veoseid saab lisada ainult veos olevatele veoselehtedele.

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
    api_instance = openapi_client.WaybillsApi(api_client)
    number = 'number_example' # str | Veoselehe number (tõstutundetu)
add_shipments_to_waybill_request = openapi_client.AddShipmentsToWaybillRequest() # AddShipmentsToWaybillRequest | 
evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Veoselehele veose lisamine
        api_instance.waybills_add_shipments(number, add_shipments_to_waybill_request, evr_language=evr_language)
    except ApiException as e:
        print("Exception when calling WaybillsApi->waybills_add_shipments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Veoselehe number (tõstutundetu) | 
 **add_shipments_to_waybill_request** | [**AddShipmentsToWaybillRequest**](AddShipmentsToWaybillRequest.md)|  | 
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
**404** |  |  -  |
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **waybills_cancel**
> waybills_cancel(number, cancel_waybill_request, evr_language=evr_language)

Veoselehe tühistamine

Tühistab veoselehe. Veoselehe staatuseks märgitakse tühistatud (status: \"cancelled\"). Veoselehe saab tühistada veoselehe looja, kuni veoseleht pole veel vastu võetud.

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
    api_instance = openapi_client.WaybillsApi(api_client)
    number = 'number_example' # str | Veoselehe number (tõstutundetu)
cancel_waybill_request = openapi_client.CancelWaybillRequest() # CancelWaybillRequest | 
evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Veoselehe tühistamine
        api_instance.waybills_cancel(number, cancel_waybill_request, evr_language=evr_language)
    except ApiException as e:
        print("Exception when calling WaybillsApi->waybills_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Veoselehe number (tõstutundetu) | 
 **cancel_waybill_request** | [**CancelWaybillRequest**](CancelWaybillRequest.md)|  | 
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
**404** |  |  -  |
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **waybills_finish**
> waybills_finish(number, evr_language=evr_language)

Veoselehe lõpetamine

Lõpetab veoselehe ja veoselehe staatuseks märgitakse \"veoseleht lõpetatud\" (status: \"finished\"). Veoselehte saavad lõpetada veoselehele märgitud saaja ning volitatud mõõtja ja seda ainult \"koorem maas\" staatuses.

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
    api_instance = openapi_client.WaybillsApi(api_client)
    number = 'number_example' # str | Veoselehe number (tõstutundetu)
evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Veoselehe lõpetamine
        api_instance.waybills_finish(number, evr_language=evr_language)
    except ApiException as e:
        print("Exception when calling WaybillsApi->waybills_finish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Veoselehe number (tõstutundetu) | 
 **evr_language** | **str**| Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \&quot;et\&quot; eesti keele ning \&quot;en\&quot; inglise keele jaoks). | [optional] 

### Return type

void (empty response body)

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
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **waybills_list**
> PagedResultOfWaybill waybills_list(created_after=created_after, created_before=created_before, last_modified_after=last_modified_after, status=status, owner_code=owner_code, transporter_code=transporter_code, receiver_code=receiver_code, van_registration_number=van_registration_number, trailer_registration_number=trailer_registration_number, driver_id_code=driver_id_code, text=text, sort=sort, page=page, evr_language=evr_language)

Veoselehtede pärimine

Tagastab filtritele vastavad veoselehed. Veoselehti saavad pärida ainult nendega seotud asutused.

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
    api_instance = openapi_client.WaybillsApi(api_client)
    created_after = '2013-10-20T19:20:30+01:00' # datetime | Filtreerib veoselehed, mis on loodud hiljem või samal ajal. Ajavahemik 'created_after' ning 'created_before' vahe peab jääma 1 kuu piiresse. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filtreerib veoselehed, mis on loodud varem või samal ajal. Ajavahemik 'created_after' ning 'created_before' vahe peab jääma 1 kuu piiresse. (optional)
last_modified_after = '2013-10-20T19:20:30+01:00' # datetime | Filtreerib veoselehed, mis on muutunud pärast määratud aega (optional)
status = openapi_client.WaybillStatus() # WaybillStatus | Filtreerib veoselehed, mis vastavad määratud staatusele (optional)
owner_code = 'owner_code_example' # str | Filtreerib veoselehed, millel on sama omaniku kood (optional)
transporter_code = 'transporter_code_example' # str | Filtreerib veoselehed, millel on sama transportija kood (optional)
receiver_code = 'receiver_code_example' # str | Filtreerib veoselehed, millel on sama saaja kood (optional)
van_registration_number = 'van_registration_number_example' # str | Filtreerib veoselehed, millel on sama veoki registreerimisnumber (tõstutundlik) (optional)
trailer_registration_number = 'trailer_registration_number_example' # str | Filtreerib veoselehed, millel on sama haagise registreerimisnumber (tõstutundlik) (optional)
driver_id_code = 'driver_id_code_example' # str | Filtreerib veoselehed, millel on sama transportija autojuhi isikukood (tõstutundlik) (optional)
text = 'text_example' # str | Vabateksti otsing. Toetatud on järgmine süntaks: * ilma jutumärkideta tekst: sõnade vahel rakendatakse loogiline JA. * jutumärkides tekst: otsitakse jutumärkides olevat lauset. * OR: loogiline VÕI operaator sõnade vahel. * -: loogiline EITUS. (optional)
sort = openapi_client.WaybillSortField() # WaybillSortField | Sorteerib tulemused valitud välja järgi (optional)
page = 56 # int | Määrab tagastatava lehekülje (optional)
evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Veoselehtede pärimine
        api_response = api_instance.waybills_list(created_after=created_after, created_before=created_before, last_modified_after=last_modified_after, status=status, owner_code=owner_code, transporter_code=transporter_code, receiver_code=receiver_code, van_registration_number=van_registration_number, trailer_registration_number=trailer_registration_number, driver_id_code=driver_id_code, text=text, sort=sort, page=page, evr_language=evr_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WaybillsApi->waybills_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **datetime**| Filtreerib veoselehed, mis on loodud hiljem või samal ajal. Ajavahemik &#39;created_after&#39; ning &#39;created_before&#39; vahe peab jääma 1 kuu piiresse. | [optional] 
 **created_before** | **datetime**| Filtreerib veoselehed, mis on loodud varem või samal ajal. Ajavahemik &#39;created_after&#39; ning &#39;created_before&#39; vahe peab jääma 1 kuu piiresse. | [optional] 
 **last_modified_after** | **datetime**| Filtreerib veoselehed, mis on muutunud pärast määratud aega | [optional] 
 **status** | [**WaybillStatus**](.md)| Filtreerib veoselehed, mis vastavad määratud staatusele | [optional] 
 **owner_code** | **str**| Filtreerib veoselehed, millel on sama omaniku kood | [optional] 
 **transporter_code** | **str**| Filtreerib veoselehed, millel on sama transportija kood | [optional] 
 **receiver_code** | **str**| Filtreerib veoselehed, millel on sama saaja kood | [optional] 
 **van_registration_number** | **str**| Filtreerib veoselehed, millel on sama veoki registreerimisnumber (tõstutundlik) | [optional] 
 **trailer_registration_number** | **str**| Filtreerib veoselehed, millel on sama haagise registreerimisnumber (tõstutundlik) | [optional] 
 **driver_id_code** | **str**| Filtreerib veoselehed, millel on sama transportija autojuhi isikukood (tõstutundlik) | [optional] 
 **text** | **str**| Vabateksti otsing. Toetatud on järgmine süntaks: * ilma jutumärkideta tekst: sõnade vahel rakendatakse loogiline JA. * jutumärkides tekst: otsitakse jutumärkides olevat lauset. * OR: loogiline VÕI operaator sõnade vahel. * -: loogiline EITUS. | [optional] 
 **sort** | [**WaybillSortField**](.md)| Sorteerib tulemused valitud välja järgi | [optional] 
 **page** | **int**| Määrab tagastatava lehekülje | [optional] 
 **evr_language** | **str**| Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \&quot;et\&quot; eesti keele ning \&quot;en\&quot; inglise keele jaoks). | [optional] 

### Return type

[**PagedResultOfWaybill**](PagedResultOfWaybill.md)

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
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **waybills_get**
> Waybill waybills_get(number, evr_language=evr_language)

Veoselehe pärimine

Tagastab numbrile vastava veoselehe. Veoselehte saavad pärida ainult sellega seotud asutused.

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
    api_instance = openapi_client.WaybillsApi(api_client)
    number = 'number_example' # str | Päritava veoselehe number (tõstutundetu)
evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Veoselehe pärimine
        api_response = api_instance.waybills_get(number, evr_language=evr_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WaybillsApi->waybills_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Päritava veoselehe number (tõstutundetu) | 
 **evr_language** | **str**| Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \&quot;et\&quot; eesti keele ning \&quot;en\&quot; inglise keele jaoks). | [optional] 

### Return type

[**Waybill**](Waybill.md)

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

# **waybills_post**
> str waybills_post(start_waybill_request, evr_language=evr_language)

Veoselehe loomine

Loob veoselehe staatusega \"vedu alustatud\" (status: \"shipping\"). Veo alustaja peab olema ise märgitud veoselehele kas omanikuks või vedajaks. Kui metsamaterjali saaja on EVR'iga liitunud asutus, peab veoselehel märgitud tarnekoht kuuluma ka saaja asutusele. Toimingu õnnestumisel tagastatakse loodud veoselehe number.

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
    api_instance = openapi_client.WaybillsApi(api_client)
    start_waybill_request = openapi_client.StartWaybillRequest() # StartWaybillRequest | Veoselehe andmed
evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Veoselehe loomine
        api_response = api_instance.waybills_post(start_waybill_request, evr_language=evr_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WaybillsApi->waybills_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_waybill_request** | [**StartWaybillRequest**](StartWaybillRequest.md)| Veoselehe andmed | 
 **evr_language** | **str**| Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \&quot;et\&quot; eesti keele ning \&quot;en\&quot; inglise keele jaoks). | [optional] 

### Return type

**str**

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
**200** | Tagastab loodud veoselehe numbri |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **waybills_unload**
> waybills_unload(number, unload_waybill_request, evr_language=evr_language)

Veoselehel veo lõpetamine

Lõpetab veo veoselehel ja veoselehe staatuseks märgitakse \"koorem maas\" (status: \"unloaded\"). Vedu saab lõpetada veoselehe looja või vedaja ja seda ainult \"vedu alustatud\" (status: shipping) staatuses.

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
    api_instance = openapi_client.WaybillsApi(api_client)
    number = 'number_example' # str | Veoselehe number (tõstutundetu)
unload_waybill_request = openapi_client.UnloadWaybillRequest() # UnloadWaybillRequest | 
evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Veoselehel veo lõpetamine
        api_instance.waybills_unload(number, unload_waybill_request, evr_language=evr_language)
    except ApiException as e:
        print("Exception when calling WaybillsApi->waybills_unload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Veoselehe number (tõstutundetu) | 
 **unload_waybill_request** | [**UnloadWaybillRequest**](UnloadWaybillRequest.md)|  | 
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
**404** |  |  -  |
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

