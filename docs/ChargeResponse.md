# ChargeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**title** | **str** |  | 
**expiration_date** | **str** |  | 
**paid_date** | **str** |  | [optional] 
**value** | **float** |  | 
**payment_method** | **str** |  | 
**status** | **str** |  | 
**customer** | [**CustomerResponse**](CustomerResponse.md) |  | 
**interest_amount** | **float** |  | [optional] 
**bank_slip_barcode** | **str** |  | [optional] 
**bank_slip** | **str** |  | [optional] 
**pix_code** | **str** |  | [optional] 
**pix_qr_code_image** | **str** |  | [optional] 
**chargeback_deadline** | **date** |  | [optional] 

## Example

```python
from bartesdk.models.charge_response import ChargeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeResponse from a JSON string
charge_response_instance = ChargeResponse.from_json(json)
# print the JSON string representation of the object
print(ChargeResponse.to_json())

# convert the object into a dict
charge_response_dict = charge_response_instance.to_dict()
# create an instance of ChargeResponse from a dict
charge_response_from_dict = ChargeResponse.from_dict(charge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


