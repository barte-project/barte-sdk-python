# CardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holder_name** | **str** |  | 
**number** | **str** |  | 
**expiration** | **str** |  | 
**cvv** | **str** |  | 

## Example

```python
from bartesdk.models.card_request import CardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CardRequest from a JSON string
card_request_instance = CardRequest.from_json(json)
# print the JSON string representation of the object
print(CardRequest.to_json())

# convert the object into a dict
card_request_dict = card_request_instance.to_dict()
# create an instance of CardRequest from a dict
card_request_from_dict = CardRequest.from_dict(card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


