# PatchBasicValueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid_plan** | **str** |  | 
**basic_value_request** | [**BasicValueRequest**](BasicValueRequest.md) |  | 
**bank_slip_description** | **str** |  | [optional] 

## Example

```python
from bartesdk.models.patch_basic_value_request import PatchBasicValueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchBasicValueRequest from a JSON string
patch_basic_value_request_instance = PatchBasicValueRequest.from_json(json)
# print the JSON string representation of the object
print(PatchBasicValueRequest.to_json())

# convert the object into a dict
patch_basic_value_request_dict = patch_basic_value_request_instance.to_dict()
# create an instance of PatchBasicValueRequest from a dict
patch_basic_value_request_from_dict = PatchBasicValueRequest.from_dict(patch_basic_value_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


