# coding: utf-8

"""
    EVR API

    OpenAPI Generator'i jaoks kohandatud EVR API kirjeldus. Kasuta seda juhul, kui spetsifikatsioonile vastava EVR API kirjeldusega ei õnnestu klienti genereerida.

    The version of the OpenAPI document: 1.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, constr
from pyevr.openapi_client.models.address import Address
from pyevr.openapi_client.models.contact_person import ContactPerson
from pyevr.openapi_client.models.representer import Representer


class Owner(BaseModel):
    """
    Owner
    """

    name: constr(strict=True, max_length=200, min_length=0) = Field(
        ..., description="Nimi"
    )
    code: constr(strict=True, max_length=20, min_length=0) = Field(
        ..., description="Isiku- või registrikood"
    )
    email: Optional[constr(strict=True, max_length=254)] = Field(
        None, description="Email"
    )
    address: Address = Field(...)
    contact_person: Optional[ContactPerson] = Field(None, alias="contactPerson")
    representer: Optional[Representer] = None
    __properties = ["name", "code", "email", "address", "contactPerson", "representer"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Owner:
        """Create an instance of Owner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict["address"] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contact_person
        if self.contact_person:
            _dict["contactPerson"] = self.contact_person.to_dict()
        # override the default output from pydantic by calling `to_dict()` of representer
        if self.representer:
            _dict["representer"] = self.representer.to_dict()
        # set to None if email (nullable) is None
        # and __fields_set__ contains the field
        if self.email is None and "email" in self.__fields_set__:
            _dict["email"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Owner:
        """Create an instance of Owner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Owner.parse_obj(obj)

        _obj = Owner.parse_obj(
            {
                "name": obj.get("name"),
                "code": obj.get("code"),
                "email": obj.get("email"),
                "address": Address.from_dict(obj.get("address"))
                if obj.get("address") is not None
                else None,
                "contact_person": ContactPerson.from_dict(obj.get("contactPerson"))
                if obj.get("contactPerson") is not None
                else None,
                "representer": Representer.from_dict(obj.get("representer"))
                if obj.get("representer") is not None
                else None,
            }
        )
        return _obj
