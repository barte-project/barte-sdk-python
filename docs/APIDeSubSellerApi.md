# bartesdk.APIDeSubSellerApi

All URIs are relative to *https://sandbox-api.barte.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create4**](APIDeSubSellerApi.md#create4) | **POST** /seller/subseller | Cria um SubSeller
[**find_by_id2**](APIDeSubSellerApi.md#find_by_id2) | **GET** /seller/subseller/{id} | Busca o SubSeller do usuário.
[**update_sub_seller**](APIDeSubSellerApi.md#update_sub_seller) | **PATCH** /seller/subseller/{id} | Atualiza um SubSeller pelo seu ID.


# **create4**
> create4(sub_seller_request)

Cria um SubSeller

Deve criar um SubSeller e retornar o mesmo caso todos os parâmetros sejam informados corretamente.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.sub_seller_request import SubSellerRequest
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
    api_instance = bartesdk.APIDeSubSellerApi(api_client)
    sub_seller_request = bartesdk.SubSellerRequest() # SubSellerRequest | 

    try:
        # Cria um SubSeller
        api_instance.create4(sub_seller_request)
    except Exception as e:
        print("Exception when calling APIDeSubSellerApi->create4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_seller_request** | [**SubSellerRequest**](SubSellerRequest.md)|  | 

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
**201** | SubSeller cadastrado com sucesso. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_id2**
> SubSellerResponse find_by_id2(id)

Busca o SubSeller do usuário.

Deve retornar o SubSeller cadastrado para o usuário logado.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.sub_seller_response import SubSellerResponse
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
    api_instance = bartesdk.APIDeSubSellerApi(api_client)
    id = 'id_example' # str | 

    try:
        # Busca o SubSeller do usuário.
        api_response = api_instance.find_by_id2(id)
        print("The response of APIDeSubSellerApi->find_by_id2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDeSubSellerApi->find_by_id2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SubSellerResponse**](SubSellerResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SubSeller encontrado. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**404** | Não foi encontrado nenhum SubSeller com este ID. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sub_seller**
> SubSellerResponse update_sub_seller(id, sub_seller_patch_request)

Atualiza um SubSeller pelo seu ID.

Deve atualizar os valores de um SubSeller o ID informado na base de dados e os paramentos sejam informados corretamente.

### Example

* Api Key Authentication (api_token):

```python
import bartesdk
from bartesdk.models.sub_seller_patch_request import SubSellerPatchRequest
from bartesdk.models.sub_seller_response import SubSellerResponse
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
    api_instance = bartesdk.APIDeSubSellerApi(api_client)
    id = 'id_example' # str | 
    sub_seller_patch_request = bartesdk.SubSellerPatchRequest() # SubSellerPatchRequest | 

    try:
        # Atualiza um SubSeller pelo seu ID.
        api_response = api_instance.update_sub_seller(id, sub_seller_patch_request)
        print("The response of APIDeSubSellerApi->update_sub_seller:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDeSubSellerApi->update_sub_seller: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sub_seller_patch_request** | [**SubSellerPatchRequest**](SubSellerPatchRequest.md)|  | 

### Return type

[**SubSellerResponse**](SubSellerResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | SubSeller atualizado com sucesso. |  -  |
**400** | Usuário sem permissão para acessar esta função. |  -  |
**404** | Não foi encontrado nenhum SubSeller com este ID. |  -  |
**500** | Houve um erro interno, tente novamente mais tarde. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

