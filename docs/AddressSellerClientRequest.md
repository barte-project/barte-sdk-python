# AddressSellerClientRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**state** | **str** |  | 
**city** | **str** |  | 
**district** | **str** |  | 
**street** | **str** |  | 
**zip_code** | **str** |  | 
**number** | **str** |  | [optional] 
**complement** | **str** |  | [optional] 

## Example

```python
from bartesdk.models.address_seller_client_request import AddressSellerClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddressSellerClientRequest from a JSON string
address_seller_client_request_instance = AddressSellerClientRequest.from_json(json)
# print the JSON string representation of the object
print(AddressSellerClientRequest.to_json())

# convert the object into a dict
address_seller_client_request_dict = address_seller_client_request_instance.to_dict()
# create an instance of AddressSellerClientRequest from a dict
address_seller_client_request_from_dict = AddressSellerClientRequest.from_dict(address_seller_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


