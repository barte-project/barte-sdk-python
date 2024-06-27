# FraudDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**billing_address** | [**BillingAddressRequest**](BillingAddressRequest.md) |  | 

## Example

```python
from bartesdk.models.fraud_data_request import FraudDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FraudDataRequest from a JSON string
fraud_data_request_instance = FraudDataRequest.from_json(json)
# print the JSON string representation of the object
print(FraudDataRequest.to_json())

# convert the object into a dict
fraud_data_request_dict = fraud_data_request_instance.to_dict()
# create an instance of FraudDataRequest from a dict
fraud_data_request_from_dict = FraudDataRequest.from_dict(fraud_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


