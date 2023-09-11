# coding: utf-8

"""
    EVR API

    OpenAPI Generator'i jaoks kohandatud EVR API kirjeldus. Kasuta seda juhul, kui spetsifikatsioonile vastava EVR API kirjeldusega ei õnnestu klienti genereerida.  # noqa: E501

    The version of the OpenAPI document: 1.14.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pyevr.openapi_client.configuration import Configuration


class Pack(object):
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
        'pack_number': 'int',
        'length': 'float',
        'height': 'float',
        'width': 'float',
        'coefficient': 'float',
        'location': 'PackLocation'
    }

    attribute_map = {
        'pack_number': 'packNumber',
        'length': 'length',
        'height': 'height',
        'width': 'width',
        'coefficient': 'coefficient',
        'location': 'location'
    }

    def __init__(self, pack_number=None, length=None, height=None, width=None, coefficient=None, location=None, local_vars_configuration=None):  # noqa: E501
        """Pack - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pack_number = None
        self._length = None
        self._height = None
        self._width = None
        self._coefficient = None
        self._location = None
        self.discriminator = None

        self.pack_number = pack_number
        self.length = length
        self.height = height
        self.width = width
        self.coefficient = coefficient
        self.location = location

    @property
    def pack_number(self):
        """Gets the pack_number of this Pack.  # noqa: E501

        Paki number  # noqa: E501

        :return: The pack_number of this Pack.  # noqa: E501
        :rtype: int
        """
        return self._pack_number

    @pack_number.setter
    def pack_number(self, pack_number):
        """Sets the pack_number of this Pack.

        Paki number  # noqa: E501

        :param pack_number: The pack_number of this Pack.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and pack_number is None:  # noqa: E501
            raise ValueError("Invalid value for `pack_number`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pack_number is not None and pack_number > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `pack_number`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pack_number is not None and pack_number < 1):  # noqa: E501
            raise ValueError("Invalid value for `pack_number`, must be a value greater than or equal to `1`")  # noqa: E501

        self._pack_number = pack_number

    @property
    def length(self):
        """Gets the length of this Pack.  # noqa: E501

        Koormapaki pikkus  # noqa: E501

        :return: The length of this Pack.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Pack.

        Koormapaki pikkus  # noqa: E501

        :param length: The length of this Pack.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and length is None:  # noqa: E501
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                length is not None and length > 1.0E+9):  # noqa: E501
            raise ValueError("Invalid value for `length`, must be a value less than or equal to `1.0E+9`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                length is not None and length < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `length`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._length = length

    @property
    def height(self):
        """Gets the height of this Pack.  # noqa: E501

        Koosmapaki kõrgus  # noqa: E501

        :return: The height of this Pack.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Pack.

        Koosmapaki kõrgus  # noqa: E501

        :param height: The height of this Pack.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and height is None:  # noqa: E501
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                height is not None and height > 1.0E+9):  # noqa: E501
            raise ValueError("Invalid value for `height`, must be a value less than or equal to `1.0E+9`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                height is not None and height < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `height`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._height = height

    @property
    def width(self):
        """Gets the width of this Pack.  # noqa: E501

        Koormapaki laius  # noqa: E501

        :return: The width of this Pack.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Pack.

        Koormapaki laius  # noqa: E501

        :param width: The width of this Pack.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and width is None:  # noqa: E501
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                width is not None and width > 1.0E+9):  # noqa: E501
            raise ValueError("Invalid value for `width`, must be a value less than or equal to `1.0E+9`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                width is not None and width < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `width`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._width = width

    @property
    def coefficient(self):
        """Gets the coefficient of this Pack.  # noqa: E501

        Koeffitsient  # noqa: E501

        :return: The coefficient of this Pack.  # noqa: E501
        :rtype: float
        """
        return self._coefficient

    @coefficient.setter
    def coefficient(self, coefficient):
        """Sets the coefficient of this Pack.

        Koeffitsient  # noqa: E501

        :param coefficient: The coefficient of this Pack.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and coefficient is None:  # noqa: E501
            raise ValueError("Invalid value for `coefficient`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                coefficient is not None and coefficient > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `coefficient`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                coefficient is not None and coefficient < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `coefficient`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._coefficient = coefficient

    @property
    def location(self):
        """Gets the location of this Pack.  # noqa: E501


        :return: The location of this Pack.  # noqa: E501
        :rtype: PackLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Pack.


        :param location: The location of this Pack.  # noqa: E501
        :type: PackLocation
        """
        if self.local_vars_configuration.client_side_validation and location is None:  # noqa: E501
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

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
        if not isinstance(other, Pack):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Pack):
            return True

        return self.to_dict() != other.to_dict()
