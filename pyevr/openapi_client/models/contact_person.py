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


class ContactPerson(BaseModel):
    """
    ContactPerson
    """

    name: Optional[constr(strict=True, max_length=200)] = Field(
        None, description="Nimi"
    )
    phone: Optional[constr(strict=True, max_length=25)] = Field(
        None, description="Telefoninumber"
    )
    email: Optional[constr(strict=True, max_length=254)] = Field(
        None, description="Email"
    )
    __properties = ["name", "phone", "email"]

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
    def from_json(cls, json_str: str) -> ContactPerson:
        """Create an instance of ContactPerson from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict["name"] = None

        # set to None if phone (nullable) is None
        # and __fields_set__ contains the field
        if self.phone is None and "phone" in self.__fields_set__:
            _dict["phone"] = None

        # set to None if email (nullable) is None
        # and __fields_set__ contains the field
        if self.email is None and "email" in self.__fields_set__:
            _dict["email"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContactPerson:
        """Create an instance of ContactPerson from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContactPerson.parse_obj(obj)

        _obj = ContactPerson.parse_obj(
            {
                "name": obj.get("name"),
                "phone": obj.get("phone"),
                "email": obj.get("email"),
            }
        )
        return _obj
