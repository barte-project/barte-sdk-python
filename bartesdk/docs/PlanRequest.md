# PlanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**active** | **bool** |  | 
**bullets** | [**List[BulletRequest]**](BulletRequest.md) |  | [optional] 
**values** | [**List[BasicValueRequest]**](BasicValueRequest.md) |  | [optional] 
**accept_payment_methods** | **List[str]** |  | [optional] 

## Example

```python
from bartesdk.models.plan_request import PlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlanRequest from a JSON string
plan_request_instance = PlanRequest.from_json(json)
# print the JSON string representation of the object
print(PlanRequest.to_json())

# convert the object into a dict
plan_request_dict = plan_request_instance.to_dict()
# create an instance of PlanRequest from a dict
plan_request_from_dict = PlanRequest.from_dict(plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


