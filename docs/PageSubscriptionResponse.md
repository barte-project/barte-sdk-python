# PageSubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[SubscriptionResponse]**](SubscriptionResponse.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**Sort**](Sort.md) |  | [optional] 
**pageable** | [**PageableObject**](PageableObject.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from bartesdk.models.page_subscription_response import PageSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageSubscriptionResponse from a JSON string
page_subscription_response_instance = PageSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(PageSubscriptionResponse.to_json())

# convert the object into a dict
page_subscription_response_dict = page_subscription_response_instance.to_dict()
# create an instance of PageSubscriptionResponse from a dict
page_subscription_response_from_dict = PageSubscriptionResponse.from_dict(page_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


