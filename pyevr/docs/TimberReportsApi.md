# openapi_client.TimberReportsApi

All URIs are relative to *https://evr-test.veoseleht.ee*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timber_reports_get_timber_report**](TimberReportsApi.md#timber_reports_get_timber_report) | **GET** /api/waybills/{waybillNumber}/timberreports | Veoselehe palkide mõõtmisraporti pärimine
[**timber_reports_upsert_timber_report**](TimberReportsApi.md#timber_reports_upsert_timber_report) | **PUT** /api/waybills/{waybillNumber}/timberreports | Veoselehele palgi mõõtmisraporti lisamine


# **timber_reports_get_timber_report**
> TimberReport timber_reports_get_timber_report(waybill_number, evr_language=evr_language)

Veoselehe palkide mõõtmisraporti pärimine

### Example

* Api Key Authentication (SecretApiKey):

```python
import openapi_client
from openapi_client.models.timber_report import TimberReport
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://evr-test.veoseleht.ee
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://evr-test.veoseleht.ee"
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
    api_instance = openapi_client.TimberReportsApi(api_client)
    waybill_number = 'waybill_number_example' # str | Veoselehe number (tõstutundetu)
    evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Veoselehe palkide mõõtmisraporti pärimine
        api_response = api_instance.timber_reports_get_timber_report(waybill_number, evr_language=evr_language)
        print("The response of TimberReportsApi->timber_reports_get_timber_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimberReportsApi->timber_reports_get_timber_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waybill_number** | **str**| Veoselehe number (tõstutundetu) | 
 **evr_language** | **str**| Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \&quot;et\&quot; eesti keele ning \&quot;en\&quot; inglise keele jaoks). | [optional] 

### Return type

[**TimberReport**](TimberReport.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** |  |  -  |
**404** |  |  -  |
**200** | Tagastab numbrile vastava veoselehe palkide mõõtmisraporti. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timber_reports_upsert_timber_report**
> TimberReport timber_reports_upsert_timber_report(waybill_number, add_timber_report_request, evr_language=evr_language)

Veoselehele palgi mõõtmisraporti lisamine

Lisab veoselehele palgi mõõtmisraporti. Mõõtmisraporti saab lisada "koorem maas" staatuses veoselehele sellele märgitud veose saaja või tema volitatud mõõtja.

### Example

* Api Key Authentication (SecretApiKey):

```python
import openapi_client
from openapi_client.models.add_timber_report_request import AddTimberReportRequest
from openapi_client.models.timber_report import TimberReport
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://evr-test.veoseleht.ee
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://evr-test.veoseleht.ee"
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
    api_instance = openapi_client.TimberReportsApi(api_client)
    waybill_number = 'waybill_number_example' # str | Veoselehe number (tõstutundetu)
    add_timber_report_request = openapi_client.AddTimberReportRequest() # AddTimberReportRequest | Palkide mõõtmisraporti andmed
    evr_language = 'evr_language_example' # str | Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks). (optional)

    try:
        # Veoselehele palgi mõõtmisraporti lisamine
        api_response = api_instance.timber_reports_upsert_timber_report(waybill_number, add_timber_report_request, evr_language=evr_language)
        print("The response of TimberReportsApi->timber_reports_upsert_timber_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimberReportsApi->timber_reports_upsert_timber_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waybill_number** | **str**| Veoselehe number (tõstutundetu) | 
 **add_timber_report_request** | [**AddTimberReportRequest**](AddTimberReportRequest.md)| Palkide mõõtmisraporti andmed | 
 **evr_language** | **str**| Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \&quot;et\&quot; eesti keele ning \&quot;en\&quot; inglise keele jaoks). | [optional] 

### Return type

[**TimberReport**](TimberReport.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

