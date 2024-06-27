# SubSellerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**document_type** | **str** |  | 
**document** | **str** |  | 
**phone_country_code** | **str** |  | 
**phone** | **str** |  | 
**email** | **str** |  | 
**seller_id** | **int** |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 

## Example

```python
from bartesdk.models.sub_seller_request import SubSellerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubSellerRequest from a JSON string
sub_seller_request_instance = SubSellerRequest.from_json(json)
# print the JSON string representation of the object
print(SubSellerRequest.to_json())

# convert the object into a dict
sub_seller_request_dict = sub_seller_request_instance.to_dict()
# create an instance of SubSellerRequest from a dict
sub_seller_request_from_dict = SubSellerRequest.from_dict(sub_seller_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


