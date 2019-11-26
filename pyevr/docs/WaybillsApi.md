# openapi_client.WaybillsApi

All URIs are relative to *https://evr-test.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**waybills_add_shipments**](WaybillsApi.md#waybills_add_shipments) | **POST** /api/waybills/{number}/shipments | Veoselehele veose lisamine
[**waybills_cancel**](WaybillsApi.md#waybills_cancel) | **POST** /api/waybills/{number}/cancel | Veoselehe tühistamine
[**waybills_finish**](WaybillsApi.md#waybills_finish) | **POST** /api/waybills/{number}/finish | Veoselehe lõpetamine
[**waybills_get**](WaybillsApi.md#waybills_get) | **GET** /api/waybills | Veoselehtede pärimine
[**waybills_get2**](WaybillsApi.md#waybills_get2) | **GET** /api/waybills/{number} | Veoselehe pärimine
[**waybills_post**](WaybillsApi.md#waybills_post) | **POST** /api/waybills | Veoselehe loomine
[**waybills_unload**](WaybillsApi.md#waybills_unload) | **POST** /api/waybills/{number}/unload | Veoselehel veo lõpetamine


# **waybills_add_shipments**
> waybills_add_shipments(number, add_shipments_to_waybill_request, evr_language=evr_language)

Veoselehele veose lisamine

Lisab veoselehele uue veose. Uusi veoseid saab lisada ainult veoselehele vedajaks märgitud asutus. Veoseid saab lisada ainult veos olevatele veoselehtedele.

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
api_instance = openapi_client.WaybillsApi(openapi_client.ApiClient(configuration))
number = 'number_example' # str | Veoselehe number
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
 **number** | **str**| Veoselehe number | 
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

Tühistab veoselehe. Veoselehe staatuseks märgitakse tühistatud (status: \"cancelled\"). Veoselehe saab tühistada ainult veoselehe looja, kuni veoseleht pole veel vastu võetud.

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
api_instance = openapi_client.WaybillsApi(openapi_client.ApiClient(configuration))
number = 'number_example' # str | Veoselehe number
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
 **number** | **str**| Veoselehe number | 
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

Lõpetab veoselehe ja veoselehe staatuseks märgitakse \"veoseleht lõpetatud\" (status: \"finished\"). Veoselehte saab lõpetada veoselehele märgitud saaja ja seda ainult \"koorem maas\" staatuses.

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
api_instance = openapi_client.WaybillsApi(openapi_client.ApiClient(configuration))
number = 'number_example' # str | Veoselehe number
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
 **number** | **str**| Veoselehe number | 
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

# **waybills_get**
> PagedResultOfWaybill waybills_get(created_after=created_after, created_before=created_before, last_modified_after=last_modified_after, status=status, owner_code=owner_code, transporter_code=transporter_code, receiver_code=receiver_code, van_registration_number=van_registration_number, trailer_registration_number=trailer_registration_number, text=text, sort=sort, page=page, evr_language=evr_language)

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

# Defining host is optional and default to https://evr-test.azurewebsites.net
configuration.host = "https://evr-test.azurewebsites.net"
# Create an instance of the API class
api_instance = openapi_client.WaybillsApi(openapi_client.ApiClient(configuration))
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filtreerib veoselehed, mis on loodud hiljem või samal ajal. Ajavahemik 'created_after' ning 'created_before' vahel peab jääma 1 kuu piiresse. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filtreerib veoselehed, mis on loodud varem või samal ajal. Ajavahemik 'created_after' ning 'created_before' vahel peab jääma 1 kuu piiresse. (optional)
last_modified_after = '2013-10-20T19:20:30+01:00' # datetime | Filtreerib veoselehed, mis on muutunud pärast määratud aega (optional)
status = openapi_client.WaybillStatus() # WaybillStatus | Filtreerib veoselehed, mis vastavad määratud staatusele (optional)
owner_code = 'owner_code_example' # str | Filtreerib veoselehed, millel on sama omaniku kood (optional)
transporter_code = 'transporter_code_example' # str | Filtreerib veoselehed, millel on sama transportija kood (optional)
receiver_code = 'receiver_code_example' # str | Filtreerib veoselehed, millel on sama saaja kood (optional)
van_registration_number = 'van_registration_number_example' # str | Filtreerib veoselehed, millel on sama veoki registreerimisnumber (tõstutundlik) (optional)
trailer_registration_number = 'trailer_registration_number_example' # str | Filtreerib veoselehed, millel on sama haagise registreerimisnumber (tõstutundlik) (optional)
text = 'text_example' # str | Vabateksti otsing.  Toetatud on järgmine süntaks:  * ilma jutumärkideta tekst: sõnade vahel rakendatakse loogiline JA.  * jutumärkides tekst: otsitakse jutumärkides olevat lauset.  * OR: loogiline VÕI operaator sõnade vahel.  * -: loogiline EITUS. (optional)
sort = openapi_client.WaybillSortField() # WaybillSortField | Sorteerib tulemused valitud välja järgi (optional)
page = 56 # int | Määrab tagastatava lehekülje (optional)
evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

try:
    # Veoselehtede pärimine
    api_response = api_instance.waybills_get(created_after=created_after, created_before=created_before, last_modified_after=last_modified_after, status=status, owner_code=owner_code, transporter_code=transporter_code, receiver_code=receiver_code, van_registration_number=van_registration_number, trailer_registration_number=trailer_registration_number, text=text, sort=sort, page=page, evr_language=evr_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WaybillsApi->waybills_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **datetime**| Filtreerib veoselehed, mis on loodud hiljem või samal ajal. Ajavahemik &#39;created_after&#39; ning &#39;created_before&#39; vahel peab jääma 1 kuu piiresse. | [optional] 
 **created_before** | **datetime**| Filtreerib veoselehed, mis on loodud varem või samal ajal. Ajavahemik &#39;created_after&#39; ning &#39;created_before&#39; vahel peab jääma 1 kuu piiresse. | [optional] 
 **last_modified_after** | **datetime**| Filtreerib veoselehed, mis on muutunud pärast määratud aega | [optional] 
 **status** | [**WaybillStatus**](.md)| Filtreerib veoselehed, mis vastavad määratud staatusele | [optional] 
 **owner_code** | **str**| Filtreerib veoselehed, millel on sama omaniku kood | [optional] 
 **transporter_code** | **str**| Filtreerib veoselehed, millel on sama transportija kood | [optional] 
 **receiver_code** | **str**| Filtreerib veoselehed, millel on sama saaja kood | [optional] 
 **van_registration_number** | **str**| Filtreerib veoselehed, millel on sama veoki registreerimisnumber (tõstutundlik) | [optional] 
 **trailer_registration_number** | **str**| Filtreerib veoselehed, millel on sama haagise registreerimisnumber (tõstutundlik) | [optional] 
 **text** | **str**| Vabateksti otsing.  Toetatud on järgmine süntaks:  * ilma jutumärkideta tekst: sõnade vahel rakendatakse loogiline JA.  * jutumärkides tekst: otsitakse jutumärkides olevat lauset.  * OR: loogiline VÕI operaator sõnade vahel.  * -: loogiline EITUS. | [optional] 
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

# **waybills_get2**
> Waybill waybills_get2(number, evr_language=evr_language)

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

# Defining host is optional and default to https://evr-test.azurewebsites.net
configuration.host = "https://evr-test.azurewebsites.net"
# Create an instance of the API class
api_instance = openapi_client.WaybillsApi(openapi_client.ApiClient(configuration))
number = 'number_example' # str | Päritava veoselehe number
evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

try:
    # Veoselehe pärimine
    api_response = api_instance.waybills_get2(number, evr_language=evr_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WaybillsApi->waybills_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Päritava veoselehe number | 
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

Loob veoselehe staatusega \"vedu alustatud\" (status: \"shipping\"). Veo alustaja peab olema ise märgitud veoselehele kas omanikuks või vedajaks. Toimingu õnnestumisel tagastatakse loodud veoselehe number.

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
api_instance = openapi_client.WaybillsApi(openapi_client.ApiClient(configuration))
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

Lõpetab veo veoselehel ja veoselehe staatuseks märgitakse \"koorem maas\" (status: \"unloaded\"). Vedu saab lõpetada veoselehele märgitud vedaja ja seda ainult \"vedu alustatud\" (status: shipping) staatuses.

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
api_instance = openapi_client.WaybillsApi(openapi_client.ApiClient(configuration))
number = 'number_example' # str | Veoselehe number
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
 **number** | **str**| Veoselehe number | 
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

