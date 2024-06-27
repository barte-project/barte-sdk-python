# AdditionalValueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | 
**installments** | **int** |  | 

## Example

```python
from bartesdk.models.additional_value_request import AdditionalValueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalValueRequest from a JSON string
additional_value_request_instance = AdditionalValueRequest.from_json(json)
# print the JSON string representation of the object
print(AdditionalValueRequest.to_json())

# convert the object into a dict
additional_value_request_dict = additional_value_request_instance.to_dict()
# create an instance of AdditionalValueRequest from a dict
additional_value_request_from_dict = AdditionalValueRequest.from_dict(additional_value_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


