# BasicValueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value_per_month** | **float** |  | 

## Example

```python
from bartesdk.models.basic_value_request import BasicValueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BasicValueRequest from a JSON string
basic_value_request_instance = BasicValueRequest.from_json(json)
# print the JSON string representation of the object
print(BasicValueRequest.to_json())

# convert the object into a dict
basic_value_request_dict = basic_value_request_instance.to_dict()
# create an instance of BasicValueRequest from a dict
basic_value_request_from_dict = BasicValueRequest.from_dict(basic_value_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


