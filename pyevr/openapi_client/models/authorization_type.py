# coding: utf-8

"""
    EVR API

    OpenAPI Generator'i jaoks kohandatud EVR API kirjeldus. Kasuta seda juhul, kui spetsifikatsioonile vastava EVR API kirjeldusega ei õnnestu klienti genereerida.

    The version of the OpenAPI document: 1.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg


class AuthorizationType(str, Enum):
    """ """

    """
    allowed enum values
    """
    FORVIEWING = "forViewing"
    FORMEASURING = "forMeasuring"

    @classmethod
    def from_json(cls, json_str: str) -> "AuthorizationType":
        """Create an instance of AuthorizationType from a JSON string"""
        return AuthorizationType(json.loads(json_str))
