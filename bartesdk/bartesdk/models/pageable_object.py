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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from bartesdk.models.sort import Sort
from typing import Optional, Set
from typing_extensions import Self

class PageableObject(BaseModel):
    """
    PageableObject
    """ # noqa: E501
    offset: Optional[StrictInt] = None
    sort: Optional[Sort] = None
    paged: Optional[StrictBool] = None
    unpaged: Optional[StrictBool] = None
    page_number: Optional[StrictInt] = Field(default=None, alias="pageNumber")
    page_size: Optional[StrictInt] = Field(default=None, alias="pageSize")
    __properties: ClassVar[List[str]] = ["offset", "sort", "paged", "unpaged", "pageNumber", "pageSize"]

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
        """Create an instance of PageableObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sort
        if self.sort:
            _dict['sort'] = self.sort.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PageableObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "offset": obj.get("offset"),
            "sort": Sort.from_dict(obj["sort"]) if obj.get("sort") is not None else None,
            "paged": obj.get("paged"),
            "unpaged": obj.get("unpaged"),
            "pageNumber": obj.get("pageNumber"),
            "pageSize": obj.get("pageSize")
        })
        return _obj


