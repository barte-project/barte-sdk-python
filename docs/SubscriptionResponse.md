# SubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**status** | **str** |  | 
**customer** | [**CustomerResponse**](CustomerResponse.md) |  | 
**start_date** | **str** |  | 
**value** | [**SubscriptionBasicValueResponse**](SubscriptionBasicValueResponse.md) |  | 
**additional_value** | [**SubscriptionAdditionalValueResponse**](SubscriptionAdditionalValueResponse.md) |  | [optional] 
**payment_method** | **str** |  | 
**charges** | [**List[ChargeResponse]**](ChargeResponse.md) |  | [optional] 
**idempotency_key** | **str** |  | [optional] 

## Example

```python
from bartesdk.models.subscription_response import SubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionResponse from a JSON string
subscription_response_instance = SubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionResponse.to_json())

# convert the object into a dict
subscription_response_dict = subscription_response_instance.to_dict()
# create an instance of SubscriptionResponse from a dict
subscription_response_from_dict = SubscriptionResponse.from_dict(subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


