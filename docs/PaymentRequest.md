# PaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**card** | [**CardRequest**](CardRequest.md) |  | [optional] 
**fraud_data** | [**FraudDataRequest**](FraudDataRequest.md) |  | [optional] 
**brand** | **str** |  | [optional] 

## Example

```python
from bartesdk.models.payment_request import PaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequest from a JSON string
payment_request_instance = PaymentRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentRequest.to_json())

# convert the object into a dict
payment_request_dict = payment_request_instance.to_dict()
# create an instance of PaymentRequest from a dict
payment_request_from_dict = PaymentRequest.from_dict(payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


