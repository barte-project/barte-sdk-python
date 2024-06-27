# AddressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**country** | **str** |  | 
**state** | **str** |  | 
**city** | **str** |  | 
**district** | **str** |  | 
**street** | **str** |  | 
**zip_code** | **str** |  | 
**number** | **str** |  | [optional] 
**complement** | **str** |  | [optional] 

## Example

```python
from bartesdk.models.address_response import AddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressResponse from a JSON string
address_response_instance = AddressResponse.from_json(json)
# print the JSON string representation of the object
print(AddressResponse.to_json())

# convert the object into a dict
address_response_dict = address_response_instance.to_dict()
# create an instance of AddressResponse from a dict
address_response_from_dict = AddressResponse.from_dict(address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


