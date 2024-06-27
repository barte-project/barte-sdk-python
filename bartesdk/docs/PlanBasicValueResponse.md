# PlanBasicValueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** |  | 
**value_per_month** | **float** |  | 

## Example

```python
from bartesdk.models.plan_basic_value_response import PlanBasicValueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanBasicValueResponse from a JSON string
plan_basic_value_response_instance = PlanBasicValueResponse.from_json(json)
# print the JSON string representation of the object
print(PlanBasicValueResponse.to_json())

# convert the object into a dict
plan_basic_value_response_dict = plan_basic_value_response_instance.to_dict()
# create an instance of PlanBasicValueResponse from a dict
plan_basic_value_response_from_dict = PlanBasicValueResponse.from_dict(plan_basic_value_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


