# SubscriptionBasicValueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** |  | 
**value_per_month** | **float** |  | 

## Example

```python
from bartesdk.models.subscription_basic_value_response import SubscriptionBasicValueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionBasicValueResponse from a JSON string
subscription_basic_value_response_instance = SubscriptionBasicValueResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionBasicValueResponse.to_json())

# convert the object into a dict
subscription_basic_value_response_dict = subscription_basic_value_response_instance.to_dict()
# create an instance of SubscriptionBasicValueResponse from a dict
subscription_basic_value_response_from_dict = SubscriptionBasicValueResponse.from_dict(subscription_basic_value_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


