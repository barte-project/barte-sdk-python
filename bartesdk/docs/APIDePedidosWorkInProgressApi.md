# bartesdk.APIDePedidosWorkInProgressApi

All URIs are relative to *https://sandbox-api.barte.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel1**](APIDePedidosWorkInProgressApi.md#cancel1) | **DELETE** /v1/orders/{uuid} | Cancela um pedido pelo seu ID.
[**create2**](APIDePedidosWorkInProgressApi.md#create2) | **POST** /v1/orders | Cria um pedido
[**find_all1**](APIDePedidosWorkInProgressApi.md#find_all1) | **GET** /v1/orders | Busca todas os pedidos do usuário logado.
[**find_by_uuid1**](APIDePedidosWorkInProgressApi.md#find_by_uuid1) | **GET** /v1/orders/{uuid} | Busca um pedido pelo seu ID


# **cancel1**
> cancel1(uuid)

Cancela um pedido pelo seu ID.

Deve cancelar um pedido específico caso o ID informado esteja presente na base de dados.

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
    api_instance = bartesdk.APIDePedidosWorkInProgressApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Cancela um pedido pelo seu ID.
        api_instance.cancel1(uuid)
    except Exception as e:
        print("Exception when calling APIDePedidosWorkInProgressApi->cancel1: %s\n" % e)
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
**204** | Pedido cancelado com sucesso. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**404** | Não foi encontado nenhum pedido com este ID. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create2**
> OrderResponse create2(order_request, x_idempotency_key=x_idempotency_key, x_ip_origin_request=x_ip_origin_request)

Cria um pedido

Deve criar um pedido e retornar o mesma caso todos os parâmetros sejam informados corretamente.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.order_request import OrderRequest
from bartesdk.models.order_response import OrderResponse
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
    api_instance = bartesdk.APIDePedidosWorkInProgressApi(api_client)
    order_request = bartesdk.OrderRequest() # OrderRequest | 
    x_idempotency_key = 'x_idempotency_key_example' # str |  (optional)
    x_ip_origin_request = 'x_ip_origin_request_example' # str |  (optional)

    try:
        # Cria um pedido
        api_response = api_instance.create2(order_request, x_idempotency_key=x_idempotency_key, x_ip_origin_request=x_ip_origin_request)
        print("The response of APIDePedidosWorkInProgressApi->create2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDePedidosWorkInProgressApi->create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_request** | [**OrderRequest**](OrderRequest.md)|  | 
 **x_idempotency_key** | **str**|  | [optional] 
 **x_ip_origin_request** | **str**|  | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

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

# **find_all1**
> PageOrderResponse find_all1(pageable, status=status, customer_name=customer_name, customer_document=customer_document)

Busca todas os pedidos do usuário logado.

Deve retornar uma lista de pedidos cadastradas para o usuário logado.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.page_order_response import PageOrderResponse
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
    api_instance = bartesdk.APIDePedidosWorkInProgressApi(api_client)
    pageable = bartesdk.Pageable() # Pageable | 
    status = 'status_example' # str |  (optional)
    customer_name = 'customer_name_example' # str |  (optional)
    customer_document = 'customer_document_example' # str |  (optional)

    try:
        # Busca todas os pedidos do usuário logado.
        api_response = api_instance.find_all1(pageable, status=status, customer_name=customer_name, customer_document=customer_document)
        print("The response of APIDePedidosWorkInProgressApi->find_all1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDePedidosWorkInProgressApi->find_all1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageable** | [**Pageable**](.md)|  | 
 **status** | **str**|  | [optional] 
 **customer_name** | **str**|  | [optional] 
 **customer_document** | **str**|  | [optional] 

### Return type

[**PageOrderResponse**](PageOrderResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pedidos encontrados. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_uuid1**
> OrderResponse find_by_uuid1(uuid)

Busca um pedido pelo seu ID

Deve retornar um pedido específico caso o ID informado esteja presente na base de dados.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.order_response import OrderResponse
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
    api_instance = bartesdk.APIDePedidosWorkInProgressApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Busca um pedido pelo seu ID
        api_response = api_instance.find_by_uuid1(uuid)
        print("The response of APIDePedidosWorkInProgressApi->find_by_uuid1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDePedidosWorkInProgressApi->find_by_uuid1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pedido encontrada. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**404** | Não foi encontrado nenhum pedido com este ID. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

