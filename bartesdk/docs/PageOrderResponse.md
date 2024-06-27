# PageOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[OrderResponse]**](OrderResponse.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**Sort**](Sort.md) |  | [optional] 
**pageable** | [**PageableObject**](PageableObject.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from bartesdk.models.page_order_response import PageOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageOrderResponse from a JSON string
page_order_response_instance = PageOrderResponse.from_json(json)
# print the JSON string representation of the object
print(PageOrderResponse.to_json())

# convert the object into a dict
page_order_response_dict = page_order_response_instance.to_dict()
# create an instance of PageOrderResponse from a dict
page_order_response_from_dict = PageOrderResponse.from_dict(page_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


