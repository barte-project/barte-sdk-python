# bartesdk.APIDeCompradoresApi

All URIs are relative to *https://sandbox-api.barte.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create3**](APIDeCompradoresApi.md#create3) | **POST** /v1/buyers | Cria um comprador
[**find_all2**](APIDeCompradoresApi.md#find_all2) | **GET** /v1/buyers | Busca todos os compradores do usuário logado.
[**find_by_id1**](APIDeCompradoresApi.md#find_by_id1) | **GET** /v1/buyers/{uuid} | Busca um comprador pelo seu ID
[**update1**](APIDeCompradoresApi.md#update1) | **PUT** /v1/buyers/{uuid} | Atualiza um comprador pelo seu ID.


# **create3**
> BuyerResponse create3(create_buyer_request)

Cria um comprador

Deve criar um comprador e retornar o mesmo caso todos os parâmetros sejam informados corretamente.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.buyer_response import BuyerResponse
from bartesdk.models.create_buyer_request import CreateBuyerRequest
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
    api_instance = bartesdk.APIDeCompradoresApi(api_client)
    create_buyer_request = bartesdk.CreateBuyerRequest() # CreateBuyerRequest | 

    try:
        # Cria um comprador
        api_response = api_instance.create3(create_buyer_request)
        print("The response of APIDeCompradoresApi->create3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDeCompradoresApi->create3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_buyer_request** | [**CreateBuyerRequest**](CreateBuyerRequest.md)|  | 

### Return type

[**BuyerResponse**](BuyerResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comprador cadastrado com sucesso. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all2**
> PageBuyerResponse find_all2(pageable, name=name, document=document)

Busca todos os compradores do usuário logado.

Deve retornar uma lista de compradores cadastrados para o usuário logado.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.page_buyer_response import PageBuyerResponse
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
    api_instance = bartesdk.APIDeCompradoresApi(api_client)
    pageable = bartesdk.Pageable() # Pageable | 
    name = 'name_example' # str |  (optional)
    document = 'document_example' # str |  (optional)

    try:
        # Busca todos os compradores do usuário logado.
        api_response = api_instance.find_all2(pageable, name=name, document=document)
        print("The response of APIDeCompradoresApi->find_all2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDeCompradoresApi->find_all2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageable** | [**Pageable**](.md)|  | 
 **name** | **str**|  | [optional] 
 **document** | **str**|  | [optional] 

### Return type

[**PageBuyerResponse**](PageBuyerResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compradores encontrados. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_id1**
> BuyerResponse find_by_id1(uuid)

Busca um comprador pelo seu ID

Deve retornar um comprador específico caso o ID informado esteja presente na base de dados.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.buyer_response import BuyerResponse
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
    api_instance = bartesdk.APIDeCompradoresApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Busca um comprador pelo seu ID
        api_response = api_instance.find_by_id1(uuid)
        print("The response of APIDeCompradoresApi->find_by_id1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDeCompradoresApi->find_by_id1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**BuyerResponse**](BuyerResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comprador encontrado. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**404** | Não foi encontado nenhum comprador com este ID. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**
> update1(uuid, update_buyer_request)

Atualiza um comprador pelo seu ID.

Deve atualizar um comprador específico caso o ID informado esteja presente na base de dados e os parâmentos sejam informados corretamente.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.update_buyer_request import UpdateBuyerRequest
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
    api_instance = bartesdk.APIDeCompradoresApi(api_client)
    uuid = 'uuid_example' # str | 
    update_buyer_request = bartesdk.UpdateBuyerRequest() # UpdateBuyerRequest | 

    try:
        # Atualiza um comprador pelo seu ID.
        api_instance.update1(uuid, update_buyer_request)
    except Exception as e:
        print("Exception when calling APIDeCompradoresApi->update1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **update_buyer_request** | [**UpdateBuyerRequest**](UpdateBuyerRequest.md)|  | 

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
**204** | Comprador atualizado com sucesso. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**404** | Não foi encontado nenhum comprador com este ID. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

