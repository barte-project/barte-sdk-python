# coding: utf-8

"""
    Barte Api

    Documentação para integração com a API da Barte <h3>Segurança</h3> Utilizamos um token de autorização cadastrado dentro da plataforma da Barte no menu  <b>Configurações -> Integração -> Chaves API</b> para autenticar as operações executadas.</br> Adicione o token a requisição utilizando o header <b>X-Token-Api</b>, na documentação utilize  o botão <b>Authorize</b> para os testes. <h3>Ambientes</h3> Disponibilizamos dois ambientes <b>(sandbox e produção)</b>. Utilize o primeiro para seus  testes de desenvolvimento.</br> Você pode selecionar o ambiente que quer utilizar na nossa documentação através com combo  <b>servers</b></br> <b>Observação: </b> Entre contato com nossa equipe de operações para lhe auxiliar na criação  de uma conta em nosso ambiente de sandbox.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from bartesdk.models.customer_response import CustomerResponse
from typing import Optional, Set
from typing_extensions import Self

class ChargeResponse(BaseModel):
    """
    ChargeResponse
    """ # noqa: E501
    uuid: StrictStr
    title: StrictStr
    expiration_date: StrictStr = Field(alias="expirationDate")
    paid_date: Optional[StrictStr] = Field(default=None, alias="paidDate")
    value: Union[StrictFloat, StrictInt]
    payment_method: StrictStr = Field(alias="paymentMethod")
    status: StrictStr
    customer: CustomerResponse
    interest_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="interestAmount")
    bank_slip_barcode: Optional[StrictStr] = Field(default=None, alias="bankSlipBarcode")
    bank_slip: Optional[StrictStr] = Field(default=None, alias="bankSlip")
    pix_code: Optional[StrictStr] = Field(default=None, alias="pixCode")
    pix_qr_code_image: Optional[StrictStr] = Field(default=None, alias="pixQRCodeImage")
    chargeback_deadline: Optional[date] = Field(default=None, alias="chargebackDeadline")
    __properties: ClassVar[List[str]] = ["uuid", "title", "expirationDate", "paidDate", "value", "paymentMethod", "status", "customer", "interestAmount", "bankSlipBarcode", "bankSlip", "pixCode", "pixQRCodeImage", "chargebackDeadline"]

    @field_validator('payment_method')
    def payment_method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PIX', 'BANK_SLIP', 'CREDIT_CARD', 'CREDIT_CARD_EARLY_BUYER', 'CREDIT_CARD_EARLY_SELLER', 'DEBIT_CARD']):
            raise ValueError("must be one of enum values ('PIX', 'BANK_SLIP', 'CREDIT_CARD', 'CREDIT_CARD_EARLY_BUYER', 'CREDIT_CARD_EARLY_SELLER', 'DEBIT_CARD')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['SCHEDULED', 'LATE', 'PAID', 'CANCELED', 'PAID_MANUALLY', 'ABANDONED', 'REFUND', 'FAILED', 'CHARGEBACK']):
            raise ValueError("must be one of enum values ('SCHEDULED', 'LATE', 'PAID', 'CANCELED', 'PAID_MANUALLY', 'ABANDONED', 'REFUND', 'FAILED', 'CHARGEBACK')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ChargeResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChargeResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "title": obj.get("title"),
            "expirationDate": obj.get("expirationDate"),
            "paidDate": obj.get("paidDate"),
            "value": obj.get("value"),
            "paymentMethod": obj.get("paymentMethod"),
            "status": obj.get("status"),
            "customer": CustomerResponse.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "interestAmount": obj.get("interestAmount"),
            "bankSlipBarcode": obj.get("bankSlipBarcode"),
            "bankSlip": obj.get("bankSlip"),
            "pixCode": obj.get("pixCode"),
            "pixQRCodeImage": obj.get("pixQRCodeImage"),
            "chargebackDeadline": obj.get("chargebackDeadline")
        })
        return _obj


