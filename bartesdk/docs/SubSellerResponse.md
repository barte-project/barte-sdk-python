# SubSellerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**document** | **str** |  | [optional] 
**phone_country_code** | **str** |  | 
**phone** | **str** |  | 
**email** | **str** |  | 
**seller_id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**address** | [**AddressResponse**](AddressResponse.md) |  | [optional] 
**account** | [**AccountResponse**](AccountResponse.md) |  | [optional] 

## Example

```python
from bartesdk.models.sub_seller_response import SubSellerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubSellerResponse from a JSON string
sub_seller_response_instance = SubSellerResponse.from_json(json)
# print the JSON string representation of the object
print(SubSellerResponse.to_json())

# convert the object into a dict
sub_seller_response_dict = sub_seller_response_instance.to_dict()
# create an instance of SubSellerResponse from a dict
sub_seller_response_from_dict = SubSellerResponse.from_dict(sub_seller_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


