# OrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** |  | 
**value** | **float** |  | 
**installments** | **int** |  | 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**payment** | [**PaymentRequest**](PaymentRequest.md) |  | 
**uuid_buyer** | **str** |  | 

## Example

```python
from bartesdk.models.order_request import OrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRequest from a JSON string
order_request_instance = OrderRequest.from_json(json)
# print the JSON string representation of the object
print(OrderRequest.to_json())

# convert the object into a dict
order_request_dict = order_request_instance.to_dict()
# create an instance of OrderRequest from a dict
order_request_from_dict = OrderRequest.from_dict(order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


