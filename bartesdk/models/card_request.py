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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CardRequest(BaseModel):
    """
    CardRequest
    """ # noqa: E501
    holder_name: Annotated[str, Field(strict=True)] = Field(alias="holderName")
    number: Annotated[str, Field(strict=True)]
    expiration: Annotated[str, Field(strict=True)]
    cvv: Annotated[str, Field(strict=True)]
    __properties: ClassVar[List[str]] = ["holderName", "number", "expiration", "cvv"]

    @field_validator('holder_name')
    def holder_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z ]{1,64}$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z ]{1,64}$/")
        return value

    @field_validator('number')
    def number_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\d]{15,16}$", value):
            raise ValueError(r"must validate the regular expression /^[\d]{15,16}$/")
        return value

    @field_validator('expiration')
    def expiration_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\d]{2}\/[\d]{4}$", value):
            raise ValueError(r"must validate the regular expression /^[\d]{2}\/[\d]{4}$/")
        return value

    @field_validator('cvv')
    def cvv_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\d]{3,4}$", value):
            raise ValueError(r"must validate the regular expression /^[\d]{3,4}$/")
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
        """Create an instance of CardRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CardRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "holderName": obj.get("holderName"),
            "number": obj.get("number"),
            "expiration": obj.get("expiration"),
            "cvv": obj.get("cvv")
        })
        return _obj

