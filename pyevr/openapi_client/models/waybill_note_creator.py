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


from pydantic import BaseModel, Field, constr


class WaybillNoteCreator(BaseModel):
    """
    WaybillNoteCreator
    """

    name: constr(strict=True, max_length=200, min_length=0) = Field(
        ..., description="Nimi"
    )
    code: constr(strict=True, max_length=20, min_length=0) = Field(
        ..., description="Isiku- või registrikood"
    )
    __properties = ["name", "code"]

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
    def from_json(cls, json_str: str) -> WaybillNoteCreator:
        """Create an instance of WaybillNoteCreator from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WaybillNoteCreator:
        """Create an instance of WaybillNoteCreator from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WaybillNoteCreator.parse_obj(obj)

        _obj = WaybillNoteCreator.parse_obj(
            {"name": obj.get("name"), "code": obj.get("code")}
        )
        return _obj
