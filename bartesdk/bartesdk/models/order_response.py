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
from bartesdk.models.charge_response import ChargeResponse
from bartesdk.models.customer_response import CustomerResponse
from typing import Optional, Set
from typing_extensions import Self

class OrderResponse(BaseModel):
    """
    OrderResponse
    """ # noqa: E501
    uuid: StrictStr
    status: StrictStr
    title: StrictStr
    description: Optional[StrictStr] = None
    value: Union[StrictFloat, StrictInt]
    installments: StrictInt
    start_date: date = Field(alias="startDate")
    payment: StrictStr
    customer: CustomerResponse
    idempotency_key: Optional[StrictStr] = Field(default=None, alias="idempotencyKey")
    charges: Optional[List[ChargeResponse]] = None
    __properties: ClassVar[List[str]] = ["uuid", "status", "title", "description", "value", "installments", "startDate", "payment", "customer", "idempotencyKey", "charges"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['SENT', 'LATE', 'PARTIALLY_PAID', 'PAID', 'CANCELED', 'ABANDONED', 'REFUND', 'CHARGEBACK']):
            raise ValueError("must be one of enum values ('SENT', 'LATE', 'PARTIALLY_PAID', 'PAID', 'CANCELED', 'ABANDONED', 'REFUND', 'CHARGEBACK')")
        return value

    @field_validator('payment')
    def payment_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PIX', 'BANK_SLIP', 'CREDIT_CARD', 'CREDIT_CARD_EARLY_BUYER', 'CREDIT_CARD_EARLY_SELLER', 'DEBIT_CARD']):
            raise ValueError("must be one of enum values ('PIX', 'BANK_SLIP', 'CREDIT_CARD', 'CREDIT_CARD_EARLY_BUYER', 'CREDIT_CARD_EARLY_SELLER', 'DEBIT_CARD')")
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
        """Create an instance of OrderResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in charges (list)
        _items = []
        if self.charges:
            for _item in self.charges:
                if _item:
                    _items.append(_item.to_dict())
            _dict['charges'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "value": obj.get("value"),
            "installments": obj.get("installments"),
            "startDate": obj.get("startDate"),
            "payment": obj.get("payment"),
            "customer": CustomerResponse.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "idempotencyKey": obj.get("idempotencyKey"),
            "charges": [ChargeResponse.from_dict(_item) for _item in obj["charges"]] if obj.get("charges") is not None else None
        })
        return _obj


