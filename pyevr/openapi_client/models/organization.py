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


class Organization(object):
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
        'waybill_number_prefix': 'str',
        'register_code': 'str',
        'address': 'Address',
        'email': 'str',
        'phone': 'str',
        'contact_persons': 'list[ContactPerson]'
    }

    attribute_map = {
        'name': 'name',
        'waybill_number_prefix': 'waybillNumberPrefix',
        'register_code': 'registerCode',
        'address': 'address',
        'email': 'email',
        'phone': 'phone',
        'contact_persons': 'contactPersons'
    }

    def __init__(self, name=None, waybill_number_prefix=None, register_code=None, address=None, email=None, phone=None, contact_persons=None, local_vars_configuration=None):  # noqa: E501
        """Organization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._waybill_number_prefix = None
        self._register_code = None
        self._address = None
        self._email = None
        self._phone = None
        self._contact_persons = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if waybill_number_prefix is not None:
            self.waybill_number_prefix = waybill_number_prefix
        if register_code is not None:
            self.register_code = register_code
        if address is not None:
            self.address = address
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if contact_persons is not None:
            self.contact_persons = contact_persons

    @property
    def name(self):
        """Gets the name of this Organization.  # noqa: E501

        Asutuse nimi  # noqa: E501

        :return: The name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organization.

        Asutuse nimi  # noqa: E501

        :param name: The name of this Organization.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def waybill_number_prefix(self):
        """Gets the waybill_number_prefix of this Organization.  # noqa: E501


        :return: The waybill_number_prefix of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._waybill_number_prefix

    @waybill_number_prefix.setter
    def waybill_number_prefix(self, waybill_number_prefix):
        """Sets the waybill_number_prefix of this Organization.


        :param waybill_number_prefix: The waybill_number_prefix of this Organization.  # noqa: E501
        :type: str
        """

        self._waybill_number_prefix = waybill_number_prefix

    @property
    def register_code(self):
        """Gets the register_code of this Organization.  # noqa: E501

        Registrikood  # noqa: E501

        :return: The register_code of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._register_code

    @register_code.setter
    def register_code(self, register_code):
        """Sets the register_code of this Organization.

        Registrikood  # noqa: E501

        :param register_code: The register_code of this Organization.  # noqa: E501
        :type: str
        """

        self._register_code = register_code

    @property
    def address(self):
        """Gets the address of this Organization.  # noqa: E501


        :return: The address of this Organization.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Organization.


        :param address: The address of this Organization.  # noqa: E501
        :type: Address
        """

        self._address = address

    @property
    def email(self):
        """Gets the email of this Organization.  # noqa: E501

        Asutuse üldemail  # noqa: E501

        :return: The email of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Organization.

        Asutuse üldemail  # noqa: E501

        :param email: The email of this Organization.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this Organization.  # noqa: E501

        Asutuse üldtelefon  # noqa: E501

        :return: The phone of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Organization.

        Asutuse üldtelefon  # noqa: E501

        :param phone: The phone of this Organization.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def contact_persons(self):
        """Gets the contact_persons of this Organization.  # noqa: E501

        Kontaktisikud  # noqa: E501

        :return: The contact_persons of this Organization.  # noqa: E501
        :rtype: list[ContactPerson]
        """
        return self._contact_persons

    @contact_persons.setter
    def contact_persons(self, contact_persons):
        """Sets the contact_persons of this Organization.

        Kontaktisikud  # noqa: E501

        :param contact_persons: The contact_persons of this Organization.  # noqa: E501
        :type: list[ContactPerson]
        """

        self._contact_persons = contact_persons

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
        if not isinstance(other, Organization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Organization):
            return True

        return self.to_dict() != other.to_dict()
