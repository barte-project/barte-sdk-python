# bartesdk.APIDePlanosApi

All URIs are relative to *https://sandbox-api.barte.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create1**](APIDePlanosApi.md#create1) | **POST** /v1/plans | Cria um plano
[**find_all_plans**](APIDePlanosApi.md#find_all_plans) | **GET** /v1/plans | Busca todos os planos do usuário logado.
[**find_by_id**](APIDePlanosApi.md#find_by_id) | **GET** /v1/plans/{uuid} | Busca um plano pelo seu ID
[**update**](APIDePlanosApi.md#update) | **PUT** /v1/plans/{uuid} | Atualiza um plano pelo seu ID.


# **create1**
> PlanResponse create1(plan_request)

Cria um plano

Deve criar uma plano e retornar o mesmo caso todos os parâmetros sejam informados corretamente.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.plan_request import PlanRequest
from bartesdk.models.plan_response import PlanResponse
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
    api_instance = bartesdk.APIDePlanosApi(api_client)
    plan_request = bartesdk.PlanRequest() # PlanRequest | 

    try:
        # Cria um plano
        api_response = api_instance.create1(plan_request)
        print("The response of APIDePlanosApi->create1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDePlanosApi->create1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_request** | [**PlanRequest**](PlanRequest.md)|  | 

### Return type

[**PlanResponse**](PlanResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Plano cadastrado com sucesso. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_plans**
> List[PlanResponse] find_all_plans()

Busca todos os planos do usuário logado.

Deve retornar uma lista de planos cadastrados para o usuário logado.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.plan_response import PlanResponse
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
    api_instance = bartesdk.APIDePlanosApi(api_client)

    try:
        # Busca todos os planos do usuário logado.
        api_response = api_instance.find_all_plans()
        print("The response of APIDePlanosApi->find_all_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDePlanosApi->find_all_plans: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PlanResponse]**](PlanResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Planos encontrados. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_id**
> PlanResponse find_by_id(uuid)

Busca um plano pelo seu ID

Deve retornar uma plano específico caso o ID informado esteja presente na base de dados.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.plan_response import PlanResponse
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
    api_instance = bartesdk.APIDePlanosApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Busca um plano pelo seu ID
        api_response = api_instance.find_by_id(uuid)
        print("The response of APIDePlanosApi->find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDePlanosApi->find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**PlanResponse**](PlanResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plano encontrado. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**404** | Não foi encontado nenhum plano com este ID. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(uuid, plan_request)

Atualiza um plano pelo seu ID.

Deve atualizar uma plano específico caso o ID informado esteja presente na base de dados e os parâmentos sejam informados corretamente.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.plan_request import PlanRequest
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
    api_instance = bartesdk.APIDePlanosApi(api_client)
    uuid = 'uuid_example' # str | 
    plan_request = bartesdk.PlanRequest() # PlanRequest | 

    try:
        # Atualiza um plano pelo seu ID.
        api_instance.update(uuid, plan_request)
    except Exception as e:
        print("Exception when calling APIDePlanosApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **plan_request** | [**PlanRequest**](PlanRequest.md)|  | 

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
**204** | Plano atualizado com sucesso. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**404** | Não foi encontado nenhum plano com este ID. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

