# UpdateBuyerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**country_code** | **str** |  | [optional] 
**phone** | **str** |  | 
**alternative_email** | **str** |  | [optional] 

## Example

```python
from bartesdk.models.update_buyer_request import UpdateBuyerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBuyerRequest from a JSON string
update_buyer_request_instance = UpdateBuyerRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateBuyerRequest.to_json())

# convert the object into a dict
update_buyer_request_dict = update_buyer_request_instance.to_dict()
# create an instance of UpdateBuyerRequest from a dict
update_buyer_request_from_dict = UpdateBuyerRequest.from_dict(update_buyer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


