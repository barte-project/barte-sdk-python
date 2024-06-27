# BillingAddressRequest


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
from bartesdk.models.billing_address_request import BillingAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillingAddressRequest from a JSON string
billing_address_request_instance = BillingAddressRequest.from_json(json)
# print the JSON string representation of the object
print(BillingAddressRequest.to_json())

# convert the object into a dict
billing_address_request_dict = billing_address_request_instance.to_dict()
# create an instance of BillingAddressRequest from a dict
billing_address_request_from_dict = BillingAddressRequest.from_dict(billing_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


