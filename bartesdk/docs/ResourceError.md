# ResourceError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**additional_info** | **Dict[str, str]** |  | [optional] 

## Example

```python
from bartesdk.models.resource_error import ResourceError

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceError from a JSON string
resource_error_instance = ResourceError.from_json(json)
# print the JSON string representation of the object
print(ResourceError.to_json())

# convert the object into a dict
resource_error_dict = resource_error_instance.to_dict()
# create an instance of ResourceError from a dict
resource_error_from_dict = ResourceError.from_dict(resource_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


