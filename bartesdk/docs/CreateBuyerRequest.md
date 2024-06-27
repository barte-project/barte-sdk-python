# CreateBuyerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**country_code** | **str** |  | [optional] 
**phone** | **str** |  | 
**alternative_email** | **str** |  | [optional] 
**address** | [**AddressSellerClientRequest**](AddressSellerClientRequest.md) |  | [optional] 

## Example

```python
from bartesdk.models.create_buyer_request import CreateBuyerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBuyerRequest from a JSON string
create_buyer_request_instance = CreateBuyerRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBuyerRequest.to_json())

# convert the object into a dict
create_buyer_request_dict = create_buyer_request_instance.to_dict()
# create an instance of CreateBuyerRequest from a dict
create_buyer_request_from_dict = CreateBuyerRequest.from_dict(create_buyer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


