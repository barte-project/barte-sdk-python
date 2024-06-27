# PageChargeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[ChargeResponse]**](ChargeResponse.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**Sort**](Sort.md) |  | [optional] 
**pageable** | [**PageableObject**](PageableObject.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from bartesdk.models.page_charge_response import PageChargeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageChargeResponse from a JSON string
page_charge_response_instance = PageChargeResponse.from_json(json)
# print the JSON string representation of the object
print(PageChargeResponse.to_json())

# convert the object into a dict
page_charge_response_dict = page_charge_response_instance.to_dict()
# create an instance of PageChargeResponse from a dict
page_charge_response_from_dict = PageChargeResponse.from_dict(page_charge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


