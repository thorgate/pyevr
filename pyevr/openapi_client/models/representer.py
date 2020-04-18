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


class Representer(object):
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
        'code': 'str',
        'address': 'Address',
        'right_of_representation': 'str',
        'email': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code',
        'address': 'address',
        'right_of_representation': 'rightOfRepresentation',
        'email': 'email',
        'phone': 'phone'
    }

    def __init__(self, name=None, code=None, address=None, right_of_representation=None, email=None, phone=None, local_vars_configuration=None):  # noqa: E501
        """Representer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._code = None
        self._address = None
        self._right_of_representation = None
        self._email = None
        self._phone = None
        self.discriminator = None

        self.name = name
        self.code = code
        self.address = address
        self.right_of_representation = right_of_representation
        self.email = email
        if phone is not None:
            self.phone = phone

    @property
    def name(self):
        """Gets the name of this Representer.  # noqa: E501

        Nimi  # noqa: E501

        :return: The name of this Representer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Representer.

        Nimi  # noqa: E501

        :param name: The name of this Representer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 200):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def code(self):
        """Gets the code of this Representer.  # noqa: E501

        Isiku- või registrikood  # noqa: E501

        :return: The code of this Representer.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Representer.

        Isiku- või registrikood  # noqa: E501

        :param code: The code of this Representer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 11):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `11`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 1):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501

        self._code = code

    @property
    def address(self):
        """Gets the address of this Representer.  # noqa: E501


        :return: The address of this Representer.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Representer.


        :param address: The address of this Representer.  # noqa: E501
        :type: Address
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def right_of_representation(self):
        """Gets the right_of_representation of this Representer.  # noqa: E501

        Esindusõiguse alus  # noqa: E501

        :return: The right_of_representation of this Representer.  # noqa: E501
        :rtype: str
        """
        return self._right_of_representation

    @right_of_representation.setter
    def right_of_representation(self, right_of_representation):
        """Sets the right_of_representation of this Representer.

        Esindusõiguse alus  # noqa: E501

        :param right_of_representation: The right_of_representation of this Representer.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                right_of_representation is not None and len(right_of_representation) > 200):
            raise ValueError("Invalid value for `right_of_representation`, length must be less than or equal to `200`")  # noqa: E501

        self._right_of_representation = right_of_representation

    @property
    def email(self):
        """Gets the email of this Representer.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this Representer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Representer.

        Email  # noqa: E501

        :param email: The email of this Representer.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 254):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this Representer.  # noqa: E501

        Telefoninumber  # noqa: E501

        :return: The phone of this Representer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Representer.

        Telefoninumber  # noqa: E501

        :param phone: The phone of this Representer.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                phone is not None and len(phone) > 25):
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `25`")  # noqa: E501

        self._phone = phone

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
        if not isinstance(other, Representer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Representer):
            return True

        return self.to_dict() != other.to_dict()
