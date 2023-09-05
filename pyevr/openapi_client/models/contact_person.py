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


class ContactPerson(object):
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
        'name': 'str',
        'phone': 'str',
        'email': 'str'
    }

    attribute_map = {
        'name': 'name',
        'phone': 'phone',
        'email': 'email'
    }

    def __init__(self, name=None, phone=None, email=None, local_vars_configuration=None):  # noqa: E501
        """ContactPerson - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._phone = None
        self._email = None
        self.discriminator = None

        self.name = name
        self.phone = phone
        self.email = email

    @property
    def name(self):
        """Gets the name of this ContactPerson.  # noqa: E501

        Nimi  # noqa: E501

        :return: The name of this ContactPerson.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContactPerson.

        Nimi  # noqa: E501

        :param name: The name of this ContactPerson.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 200):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this ContactPerson.  # noqa: E501

        Telefoninumber  # noqa: E501

        :return: The phone of this ContactPerson.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ContactPerson.

        Telefoninumber  # noqa: E501

        :param phone: The phone of this ContactPerson.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                phone is not None and len(phone) > 25):
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `25`")  # noqa: E501

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this ContactPerson.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this ContactPerson.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContactPerson.

        Email  # noqa: E501

        :param email: The email of this ContactPerson.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 254):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501

        self._email = email

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
        if not isinstance(other, ContactPerson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContactPerson):
            return True

        return self.to_dict() != other.to_dict()
