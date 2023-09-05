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


class Address(object):
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
        'country_code': 'str',
        'county': 'str',
        'city': 'str',
        'street': 'str'
    }

    attribute_map = {
        'country_code': 'countryCode',
        'county': 'county',
        'city': 'city',
        'street': 'street'
    }

    def __init__(self, country_code=None, county=None, city=None, street=None, local_vars_configuration=None):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._country_code = None
        self._county = None
        self._city = None
        self._street = None
        self.discriminator = None

        self.country_code = country_code
        self.county = county
        self.city = city
        self.street = street

    @property
    def country_code(self):
        """Gets the country_code of this Address.  # noqa: E501

        Riigi kood  # noqa: E501

        :return: The country_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Address.

        Riigi kood  # noqa: E501

        :param country_code: The country_code of this Address.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and country_code is None:  # noqa: E501
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                country_code is not None and len(country_code) > 3):
            raise ValueError("Invalid value for `country_code`, length must be less than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                country_code is not None and len(country_code) < 3):
            raise ValueError("Invalid value for `country_code`, length must be greater than or equal to `3`")  # noqa: E501

        self._country_code = country_code

    @property
    def county(self):
        """Gets the county of this Address.  # noqa: E501

        Maakond  # noqa: E501

        :return: The county of this Address.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this Address.

        Maakond  # noqa: E501

        :param county: The county of this Address.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and county is None:  # noqa: E501
            raise ValueError("Invalid value for `county`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                county is not None and len(county) > 100):
            raise ValueError("Invalid value for `county`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                county is not None and len(county) < 0):
            raise ValueError("Invalid value for `county`, length must be greater than or equal to `0`")  # noqa: E501

        self._county = county

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501

        Linn/vald  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.

        Linn/vald  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and city is None:  # noqa: E501
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                city is not None and len(city) > 100):
            raise ValueError("Invalid value for `city`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                city is not None and len(city) < 0):
            raise ValueError("Invalid value for `city`, length must be greater than or equal to `0`")  # noqa: E501

        self._city = city

    @property
    def street(self):
        """Gets the street of this Address.  # noqa: E501

        Tänav/küla  # noqa: E501

        :return: The street of this Address.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this Address.

        Tänav/küla  # noqa: E501

        :param street: The street of this Address.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and street is None:  # noqa: E501
            raise ValueError("Invalid value for `street`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                street is not None and len(street) > 100):
            raise ValueError("Invalid value for `street`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                street is not None and len(street) < 0):
            raise ValueError("Invalid value for `street`, length must be greater than or equal to `0`")  # noqa: E501

        self._street = street

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
        if not isinstance(other, Address):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Address):
            return True

        return self.to_dict() != other.to_dict()
