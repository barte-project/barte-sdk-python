# SubscriptionAdditionalValueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | 
**installments** | **int** |  | 

## Example

```python
from bartesdk.models.subscription_additional_value_response import SubscriptionAdditionalValueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionAdditionalValueResponse from a JSON string
subscription_additional_value_response_instance = SubscriptionAdditionalValueResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionAdditionalValueResponse.to_json())

# convert the object into a dict
subscription_additional_value_response_dict = subscription_additional_value_response_instance.to_dict()
# create an instance of SubscriptionAdditionalValueResponse from a dict
subscription_additional_value_response_from_dict = SubscriptionAdditionalValueResponse.from_dict(subscription_additional_value_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


