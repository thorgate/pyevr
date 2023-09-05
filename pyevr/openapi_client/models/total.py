# coding: utf-8

"""
    EVR API

    OpenAPI Generator'i jaoks kohandatud EVR API kirjeldus. Kasuta seda juhul, kui spetsifikatsioonile vastava EVR API kirjeldusega ei õnnestu klienti genereerida.  # noqa: E501

    The version of the OpenAPI document: 1.13.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pyevr.openapi_client.configuration import Configuration


class Total(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'amount': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'unit': 'unit'
    }

    def __init__(self, amount=None, unit=None, local_vars_configuration=None):  # noqa: E501
        """Total - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._unit = None
        self.discriminator = None

        self.amount = amount
        self.unit = unit

    @property
    def amount(self):
        """Gets the amount of this Total.  # noqa: E501

        Mõõdetud kogus  # noqa: E501

        :return: The amount of this Total.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Total.

        Mõõdetud kogus  # noqa: E501

        :param amount: The amount of this Total.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                amount is not None and amount > 1.0E+9):  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value less than or equal to `1.0E+9`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                amount is not None and amount < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._amount = amount

    @property
    def unit(self):
        """Gets the unit of this Total.  # noqa: E501

        Mõõtühik  # noqa: E501

        :return: The unit of this Total.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Total.

        Mõõtühik  # noqa: E501

        :param unit: The unit of this Total.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and unit is None:  # noqa: E501
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                unit is not None and len(unit) > 10):
            raise ValueError("Invalid value for `unit`, length must be less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                unit is not None and len(unit) < 0):
            raise ValueError("Invalid value for `unit`, length must be greater than or equal to `0`")  # noqa: E501

        self._unit = unit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Total):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Total):
            return True

        return self.to_dict() != other.to_dict()