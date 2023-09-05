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


class Coordinates(object):
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
        'x': 'float',
        'y': 'float',
        'epsg': 'int'
    }

    attribute_map = {
        'x': 'x',
        'y': 'y',
        'epsg': 'epsg'
    }

    def __init__(self, x=None, y=None, epsg=None, local_vars_configuration=None):  # noqa: E501
        """Coordinates - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._x = None
        self._y = None
        self._epsg = None
        self.discriminator = None

        self.x = x
        self.y = y
        self.epsg = epsg

    @property
    def x(self):
        """Gets the x of this Coordinates.  # noqa: E501

        X koordinaat  # noqa: E501

        :return: The x of this Coordinates.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this Coordinates.

        X koordinaat  # noqa: E501

        :param x: The x of this Coordinates.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and x is None:  # noqa: E501
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

    @property
    def y(self):
        """Gets the y of this Coordinates.  # noqa: E501

        Y koordinaat  # noqa: E501

        :return: The y of this Coordinates.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this Coordinates.

        Y koordinaat  # noqa: E501

        :param y: The y of this Coordinates.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and y is None:  # noqa: E501
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501

        self._y = y

    @property
    def epsg(self):
        """Gets the epsg of this Coordinates.  # noqa: E501

        EPSG formaadis koordinaatsüsteemiväärtus (näide: 3301)  # noqa: E501

        :return: The epsg of this Coordinates.  # noqa: E501
        :rtype: int
        """
        return self._epsg

    @epsg.setter
    def epsg(self, epsg):
        """Sets the epsg of this Coordinates.

        EPSG formaadis koordinaatsüsteemiväärtus (näide: 3301)  # noqa: E501

        :param epsg: The epsg of this Coordinates.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                epsg is not None and epsg > 99999):  # noqa: E501
            raise ValueError("Invalid value for `epsg`, must be a value less than or equal to `99999`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                epsg is not None and epsg < 1000):  # noqa: E501
            raise ValueError("Invalid value for `epsg`, must be a value greater than or equal to `1000`")  # noqa: E501

        self._epsg = epsg

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
        if not isinstance(other, Coordinates):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Coordinates):
            return True

        return self.to_dict() != other.to_dict()
