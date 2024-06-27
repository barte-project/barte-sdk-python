# BuyerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**document** | **str** |  | 
**name** | **str** |  | 
**country_code** | **str** |  | 
**phone** | **str** |  | 
**email** | **str** |  | 
**alternative_email** | **str** |  | [optional] 

## Example

```python
from bartesdk.models.buyer_response import BuyerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerResponse from a JSON string
buyer_response_instance = BuyerResponse.from_json(json)
# print the JSON string representation of the object
print(BuyerResponse.to_json())

# convert the object into a dict
buyer_response_dict = buyer_response_instance.to_dict()
# create an instance of BuyerResponse from a dict
buyer_response_from_dict = BuyerResponse.from_dict(buyer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


