# bartesdk.APIDeCobranasApi

All URIs are relative to *https://sandbox-api.barte.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_charges**](APIDeCobranasApi.md#find_charges) | **GET** /v1/charges | Busca todas as cobranças do usuário logado.
[**find_charges_by_uuid**](APIDeCobranasApi.md#find_charges_by_uuid) | **GET** /v1/charges/{uuid} | Busca uma cobrança pelo seu ID
[**process_chargeback**](APIDeCobranasApi.md#process_chargeback) | **PATCH** /v1/charges/{uuid}/chargeback | 
[**process_refund**](APIDeCobranasApi.md#process_refund) | **PATCH** /v1/charges/{uuid}/refund | Estorna uma cobrança pelo seu ID.
[**update_charge_to_cancel**](APIDeCobranasApi.md#update_charge_to_cancel) | **DELETE** /v1/charges/{uuid} | Cancela uma cobrança pelo seu ID.


# **find_charges**
> PageChargeResponse find_charges(pageable, expiration_date_initial=expiration_date_initial, expiration_date_final=expiration_date_final, payment_method=payment_method, status=status, customer_document=customer_document)

Busca todas as cobranças do usuário logado.

Deve retornar uma lista de cobranças cadastradas para o usuário logado.  Regra da pesquisa pelas datas de expiração:      expirationDateInitial: Pesquisa todas as cobranças começando pela data indicada   expirationDateFinal: Pesquisa todas as cobranças anteriores até a data indicada   expirationDateInitial + expirationDateFinal: Pesquisa todas as cobranças dentro do intervalo indicado

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.page_charge_response import PageChargeResponse
from bartesdk.models.pageable import Pageable
from bartesdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox-api.barte.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bartesdk.Configuration(
    host = "https://sandbox-api.barte.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with bartesdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bartesdk.APIDeCobranasApi(api_client)
    pageable = bartesdk.Pageable() # Pageable | 
    expiration_date_initial = '2013-10-20' # date |  (optional)
    expiration_date_final = '2013-10-20' # date |  (optional)
    payment_method = 'payment_method_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    customer_document = 'customer_document_example' # str |  (optional)

    try:
        # Busca todas as cobranças do usuário logado.
        api_response = api_instance.find_charges(pageable, expiration_date_initial=expiration_date_initial, expiration_date_final=expiration_date_final, payment_method=payment_method, status=status, customer_document=customer_document)
        print("The response of APIDeCobranasApi->find_charges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDeCobranasApi->find_charges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageable** | [**Pageable**](.md)|  | 
 **expiration_date_initial** | **date**|  | [optional] 
 **expiration_date_final** | **date**|  | [optional] 
 **payment_method** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **customer_document** | **str**|  | [optional] 

### Return type

[**PageChargeResponse**](PageChargeResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cobranças encontradas. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_charges_by_uuid**
> ChargeResponse find_charges_by_uuid(uuid)

Busca uma cobrança pelo seu ID

Deve retornar uma cobrança específica caso o ID informado esteja presente na base de dados.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.charge_response import ChargeResponse
from bartesdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox-api.barte.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bartesdk.Configuration(
    host = "https://sandbox-api.barte.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with bartesdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bartesdk.APIDeCobranasApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Busca uma cobrança pelo seu ID
        api_response = api_instance.find_charges_by_uuid(uuid)
        print("The response of APIDeCobranasApi->find_charges_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDeCobranasApi->find_charges_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ChargeResponse**](ChargeResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cobrança encontrada. |  -  |
**400** | Não foi encontrado nenhuma cobrança com este ID. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_chargeback**
> ChargeResponse process_chargeback(uuid)



### Example


```python
import bartesdk
from bartesdk.models.charge_response import ChargeResponse
from bartesdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox-api.barte.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bartesdk.Configuration(
    host = "https://sandbox-api.barte.com"
)


# Enter a context with an instance of the API client
with bartesdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bartesdk.APIDeCobranasApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_response = api_instance.process_chargeback(uuid)
        print("The response of APIDeCobranasApi->process_chargeback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDeCobranasApi->process_chargeback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ChargeResponse**](ChargeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_refund**
> ChargeResponse process_refund(uuid, refund_request)

Estorna uma cobrança pelo seu ID.

Deve estornar uma cobrança específica caso o ID informado esteja presente na base de dados.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.charge_response import ChargeResponse
from bartesdk.models.refund_request import RefundRequest
from bartesdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox-api.barte.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bartesdk.Configuration(
    host = "https://sandbox-api.barte.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with bartesdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bartesdk.APIDeCobranasApi(api_client)
    uuid = 'uuid_example' # str | 
    refund_request = bartesdk.RefundRequest() # RefundRequest | 

    try:
        # Estorna uma cobrança pelo seu ID.
        api_response = api_instance.process_refund(uuid, refund_request)
        print("The response of APIDeCobranasApi->process_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDeCobranasApi->process_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **refund_request** | [**RefundRequest**](RefundRequest.md)|  | 

### Return type

[**ChargeResponse**](ChargeResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cobrança estornada com sucesso. |  -  |
**400** | Não foi encontrada nenhuma cobrança com este ID. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_charge_to_cancel**
> update_charge_to_cancel(uuid)

Cancela uma cobrança pelo seu ID.

Deve cancelar uma cobrança específica caso o ID informado esteja presente na base de dados.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox-api.barte.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bartesdk.Configuration(
    host = "https://sandbox-api.barte.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with bartesdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bartesdk.APIDeCobranasApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Cancela uma cobrança pelo seu ID.
        api_instance.update_charge_to_cancel(uuid)
    except Exception as e:
        print("Exception when calling APIDeCobranasApi->update_charge_to_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Cobrança cancelada com sucesso. |  -  |
**400** | Não foi encontrada nenhuma cobrança com este ID. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

