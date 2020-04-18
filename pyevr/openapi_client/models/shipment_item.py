# coding: utf-8

"""
    EVR API

    OpenAPI Generator'i jaoks kohandatud EVR API kirjeldus. Kasuta seda juhul, kui spetsifikatsioonile vastava EVR API kirjeldusega ei õnnestu klienti genereerida.  # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pyevr.openapi_client.configuration import Configuration


class ShipmentItem(object):
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
        'pack': 'Pack',
        'unit_code': 'str',
        'assortment': 'ShipmentAssortment'
    }

    attribute_map = {
        'amount': 'amount',
        'pack': 'pack',
        'unit_code': 'unitCode',
        'assortment': 'assortment'
    }

    def __init__(self, amount=None, pack=None, unit_code=None, assortment=None, local_vars_configuration=None):  # noqa: E501
        """ShipmentItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._pack = None
        self._unit_code = None
        self._assortment = None
        self.discriminator = None

        self.amount = amount
        if pack is not None:
            self.pack = pack
        self.unit_code = unit_code
        self.assortment = assortment

    @property
    def amount(self):
        """Gets the amount of this ShipmentItem.  # noqa: E501

        Kogus  # noqa: E501

        :return: The amount of this ShipmentItem.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ShipmentItem.

        Kogus  # noqa: E501

        :param amount: The amount of this ShipmentItem.  # noqa: E501
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
    def pack(self):
        """Gets the pack of this ShipmentItem.  # noqa: E501


        :return: The pack of this ShipmentItem.  # noqa: E501
        :rtype: Pack
        """
        return self._pack

    @pack.setter
    def pack(self, pack):
        """Sets the pack of this ShipmentItem.


        :param pack: The pack of this ShipmentItem.  # noqa: E501
        :type: Pack
        """

        self._pack = pack

    @property
    def unit_code(self):
        """Gets the unit_code of this ShipmentItem.  # noqa: E501

        [Mõõtühiku kood](#operation/MeasurementUnits_List)  # noqa: E501

        :return: The unit_code of this ShipmentItem.  # noqa: E501
        :rtype: str
        """
        return self._unit_code

    @unit_code.setter
    def unit_code(self, unit_code):
        """Sets the unit_code of this ShipmentItem.

        [Mõõtühiku kood](#operation/MeasurementUnits_List)  # noqa: E501

        :param unit_code: The unit_code of this ShipmentItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and unit_code is None:  # noqa: E501
            raise ValueError("Invalid value for `unit_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                unit_code is not None and len(unit_code) > 10):
            raise ValueError("Invalid value for `unit_code`, length must be less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                unit_code is not None and len(unit_code) < 1):
            raise ValueError("Invalid value for `unit_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._unit_code = unit_code

    @property
    def assortment(self):
        """Gets the assortment of this ShipmentItem.  # noqa: E501


        :return: The assortment of this ShipmentItem.  # noqa: E501
        :rtype: ShipmentAssortment
        """
        return self._assortment

    @assortment.setter
    def assortment(self, assortment):
        """Sets the assortment of this ShipmentItem.


        :param assortment: The assortment of this ShipmentItem.  # noqa: E501
        :type: ShipmentAssortment
        """
        if self.local_vars_configuration.client_side_validation and assortment is None:  # noqa: E501
            raise ValueError("Invalid value for `assortment`, must not be `None`")  # noqa: E501

        self._assortment = assortment

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
        if not isinstance(other, ShipmentItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShipmentItem):
            return True

        return self.to_dict() != other.to_dict()
