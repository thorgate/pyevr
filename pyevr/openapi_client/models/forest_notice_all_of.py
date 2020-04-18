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


class ForestNoticeAllOf(object):
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
        'cadaster': 'str',
        'compartment': 'str',
        'forest_allocation_number': 'str',
        'number': 'str'
    }

    attribute_map = {
        'cadaster': 'cadaster',
        'compartment': 'compartment',
        'forest_allocation_number': 'forestAllocationNumber',
        'number': 'number'
    }

    def __init__(self, cadaster=None, compartment=None, forest_allocation_number=None, number=None, local_vars_configuration=None):  # noqa: E501
        """ForestNoticeAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cadaster = None
        self._compartment = None
        self._forest_allocation_number = None
        self._number = None
        self.discriminator = None

        self.cadaster = cadaster
        self.compartment = compartment
        if forest_allocation_number is not None:
            self.forest_allocation_number = forest_allocation_number
        if number is not None:
            self.number = number

    @property
    def cadaster(self):
        """Gets the cadaster of this ForestNoticeAllOf.  # noqa: E501

        Katastritunnus  # noqa: E501

        :return: The cadaster of this ForestNoticeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._cadaster

    @cadaster.setter
    def cadaster(self, cadaster):
        """Sets the cadaster of this ForestNoticeAllOf.

        Katastritunnus  # noqa: E501

        :param cadaster: The cadaster of this ForestNoticeAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cadaster is None:  # noqa: E501
            raise ValueError("Invalid value for `cadaster`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cadaster is not None and len(cadaster) > 500):
            raise ValueError("Invalid value for `cadaster`, length must be less than or equal to `500`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cadaster is not None and len(cadaster) < 1):
            raise ValueError("Invalid value for `cadaster`, length must be greater than or equal to `1`")  # noqa: E501

        self._cadaster = cadaster

    @property
    def compartment(self):
        """Gets the compartment of this ForestNoticeAllOf.  # noqa: E501

        Kvartal  # noqa: E501

        :return: The compartment of this ForestNoticeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._compartment

    @compartment.setter
    def compartment(self, compartment):
        """Sets the compartment of this ForestNoticeAllOf.

        Kvartal  # noqa: E501

        :param compartment: The compartment of this ForestNoticeAllOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                compartment is not None and len(compartment) > 200):
            raise ValueError("Invalid value for `compartment`, length must be less than or equal to `200`")  # noqa: E501

        self._compartment = compartment

    @property
    def forest_allocation_number(self):
        """Gets the forest_allocation_number of this ForestNoticeAllOf.  # noqa: E501

        Metsaeraldis  # noqa: E501

        :return: The forest_allocation_number of this ForestNoticeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._forest_allocation_number

    @forest_allocation_number.setter
    def forest_allocation_number(self, forest_allocation_number):
        """Sets the forest_allocation_number of this ForestNoticeAllOf.

        Metsaeraldis  # noqa: E501

        :param forest_allocation_number: The forest_allocation_number of this ForestNoticeAllOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                forest_allocation_number is not None and len(forest_allocation_number) > 200):
            raise ValueError("Invalid value for `forest_allocation_number`, length must be less than or equal to `200`")  # noqa: E501

        self._forest_allocation_number = forest_allocation_number

    @property
    def number(self):
        """Gets the number of this ForestNoticeAllOf.  # noqa: E501

        Metsateatise number  # noqa: E501

        :return: The number of this ForestNoticeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ForestNoticeAllOf.

        Metsateatise number  # noqa: E501

        :param number: The number of this ForestNoticeAllOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                number is not None and len(number) > 50):
            raise ValueError("Invalid value for `number`, length must be less than or equal to `50`")  # noqa: E501

        self._number = number

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
        if not isinstance(other, ForestNoticeAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ForestNoticeAllOf):
            return True

        return self.to_dict() != other.to_dict()
