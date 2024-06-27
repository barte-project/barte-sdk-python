# bartesdk.APIDeAssinaturasApi

All URIs are relative to *https://sandbox-api.barte.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel**](APIDeAssinaturasApi.md#cancel) | **DELETE** /v1/subscriptions/{uuid} | Desativa uma assinatura pelo seu ID.
[**create**](APIDeAssinaturasApi.md#create) | **POST** /v1/subscriptions | Cria uma assinatura
[**find_all**](APIDeAssinaturasApi.md#find_all) | **GET** /v1/subscriptions | Busca todas as assinaturas do usuário logado.
[**find_by_uuid**](APIDeAssinaturasApi.md#find_by_uuid) | **GET** /v1/subscriptions/{uuid} | Busca uma assinatura pelo seu ID
[**update_basic_value**](APIDeAssinaturasApi.md#update_basic_value) | **PATCH** /v1/subscriptions/{uuid}/basic-value | Atualiza o valor base de uma assinatura pelo seu ID.


# **cancel**
> cancel(uuid)

Desativa uma assinatura pelo seu ID.

Deve desativar uma assinatura específica caso o ID informado esteja presente na base de dados.

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
    api_instance = bartesdk.APIDeAssinaturasApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Desativa uma assinatura pelo seu ID.
        api_instance.cancel(uuid)
    except Exception as e:
        print("Exception when calling APIDeAssinaturasApi->cancel: %s\n" % e)
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
**204** | Assinatura desativada com sucesso. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**404** | Não foi encontado nenhuma assinatura com este ID. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> SubscriptionResponse create(subscription_request, x_idempotency_key=x_idempotency_key, x_ip_origin_request=x_ip_origin_request)

Cria uma assinatura

Deve criar uma assinatura e retornar a mesma caso todos os parâmetros sejam informados corretamente.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.subscription_request import SubscriptionRequest
from bartesdk.models.subscription_response import SubscriptionResponse
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
    api_instance = bartesdk.APIDeAssinaturasApi(api_client)
    subscription_request = bartesdk.SubscriptionRequest() # SubscriptionRequest | 
    x_idempotency_key = 'x_idempotency_key_example' # str |  (optional)
    x_ip_origin_request = 'x_ip_origin_request_example' # str |  (optional)

    try:
        # Cria uma assinatura
        api_response = api_instance.create(subscription_request, x_idempotency_key=x_idempotency_key, x_ip_origin_request=x_ip_origin_request)
        print("The response of APIDeAssinaturasApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDeAssinaturasApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_request** | [**SubscriptionRequest**](SubscriptionRequest.md)|  | 
 **x_idempotency_key** | **str**|  | [optional] 
 **x_ip_origin_request** | **str**|  | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Assinatura cadastrada com sucesso. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all**
> PageSubscriptionResponse find_all(pageable, status=status, customer_name=customer_name, customer_document=customer_document)

Busca todas as assinaturas do usuário logado.

Deve retornar uma lista de assinaturas cadastradas para o usuário logado.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.page_subscription_response import PageSubscriptionResponse
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
    api_instance = bartesdk.APIDeAssinaturasApi(api_client)
    pageable = bartesdk.Pageable() # Pageable | 
    status = 'status_example' # str |  (optional)
    customer_name = 'customer_name_example' # str |  (optional)
    customer_document = 'customer_document_example' # str |  (optional)

    try:
        # Busca todas as assinaturas do usuário logado.
        api_response = api_instance.find_all(pageable, status=status, customer_name=customer_name, customer_document=customer_document)
        print("The response of APIDeAssinaturasApi->find_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDeAssinaturasApi->find_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageable** | [**Pageable**](.md)|  | 
 **status** | **str**|  | [optional] 
 **customer_name** | **str**|  | [optional] 
 **customer_document** | **str**|  | [optional] 

### Return type

[**PageSubscriptionResponse**](PageSubscriptionResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assinaturas encontradas. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_uuid**
> SubscriptionResponse find_by_uuid(uuid)

Busca uma assinatura pelo seu ID

Deve retornar uma assinatura específica caso o ID informado esteja presente na base de dados.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.subscription_response import SubscriptionResponse
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
    api_instance = bartesdk.APIDeAssinaturasApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Busca uma assinatura pelo seu ID
        api_response = api_instance.find_by_uuid(uuid)
        print("The response of APIDeAssinaturasApi->find_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDeAssinaturasApi->find_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assinatura encontrada. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**404** | Não foi encontrado nenhuma assinatura com este ID. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_basic_value**
> update_basic_value(uuid, patch_basic_value_request)

Atualiza o valor base de uma assinatura pelo seu ID.

Deve atualizar o valor base de uma assinatura específica caso o ID informado esteja presente na base de dados e os paramentos sejam informados corretamente.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.patch_basic_value_request import PatchBasicValueRequest
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
    api_instance = bartesdk.APIDeAssinaturasApi(api_client)
    uuid = 'uuid_example' # str | 
    patch_basic_value_request = bartesdk.PatchBasicValueRequest() # PatchBasicValueRequest | 

    try:
        # Atualiza o valor base de uma assinatura pelo seu ID.
        api_instance.update_basic_value(uuid, patch_basic_value_request)
    except Exception as e:
        print("Exception when calling APIDeAssinaturasApi->update_basic_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **patch_basic_value_request** | [**PatchBasicValueRequest**](PatchBasicValueRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Assinatura atualizada com sucesso. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**404** | Não foi encontrado nenhuma assinatura com este ID. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

