# SubSellerPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**document** | **str** |  | [optional] 
**phone_country_code** | **str** |  | 
**phone** | **str** |  | 
**email** | **str** |  | 
**seller_id** | **int** |  | 
**is_active** | **bool** |  | 
**address** | [**Address**](Address.md) |  | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 

## Example

```python
from bartesdk.models.sub_seller_patch_request import SubSellerPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubSellerPatchRequest from a JSON string
sub_seller_patch_request_instance = SubSellerPatchRequest.from_json(json)
# print the JSON string representation of the object
print(SubSellerPatchRequest.to_json())

# convert the object into a dict
sub_seller_patch_request_dict = sub_seller_patch_request_instance.to_dict()
# create an instance of SubSellerPatchRequest from a dict
sub_seller_patch_request_from_dict = SubSellerPatchRequest.from_dict(sub_seller_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


