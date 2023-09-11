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


class WaybillPlaceOfDelivery(object):
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
        'code': 'str',
        'name': 'str',
        'coordinates': 'Coordinates',
        'address': 'Address',
        'contact_person': 'ContactPerson',
        'near_address': 'str',
        'user_custom_data': 'object'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'coordinates': 'coordinates',
        'address': 'address',
        'contact_person': 'contactPerson',
        'near_address': 'nearAddress',
        'user_custom_data': 'userCustomData'
    }

    def __init__(self, code=None, name=None, coordinates=None, address=None, contact_person=None, near_address=None, user_custom_data=None, local_vars_configuration=None):  # noqa: E501
        """WaybillPlaceOfDelivery - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._name = None
        self._coordinates = None
        self._address = None
        self._contact_person = None
        self._near_address = None
        self._user_custom_data = None
        self.discriminator = None

        self.code = code
        self.name = name
        if coordinates is not None:
            self.coordinates = coordinates
        self.address = address
        if contact_person is not None:
            self.contact_person = contact_person
        self.near_address = near_address
        if user_custom_data is not None:
            self.user_custom_data = user_custom_data

    @property
    def code(self):
        """Gets the code of this WaybillPlaceOfDelivery.  # noqa: E501

        EVR tarnekoha kood (kui on EVR-i lisatud tarnekoht)  # noqa: E501

        :return: The code of this WaybillPlaceOfDelivery.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this WaybillPlaceOfDelivery.

        EVR tarnekoha kood (kui on EVR-i lisatud tarnekoht)  # noqa: E501

        :param code: The code of this WaybillPlaceOfDelivery.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 25):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `25`")  # noqa: E501

        self._code = code

    @property
    def name(self):
        """Gets the name of this WaybillPlaceOfDelivery.  # noqa: E501

        Tarnekoha nimi  # noqa: E501

        :return: The name of this WaybillPlaceOfDelivery.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WaybillPlaceOfDelivery.

        Tarnekoha nimi  # noqa: E501

        :param name: The name of this WaybillPlaceOfDelivery.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 200):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def coordinates(self):
        """Gets the coordinates of this WaybillPlaceOfDelivery.  # noqa: E501


        :return: The coordinates of this WaybillPlaceOfDelivery.  # noqa: E501
        :rtype: Coordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this WaybillPlaceOfDelivery.


        :param coordinates: The coordinates of this WaybillPlaceOfDelivery.  # noqa: E501
        :type: Coordinates
        """

        self._coordinates = coordinates

    @property
    def address(self):
        """Gets the address of this WaybillPlaceOfDelivery.  # noqa: E501


        :return: The address of this WaybillPlaceOfDelivery.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this WaybillPlaceOfDelivery.


        :param address: The address of this WaybillPlaceOfDelivery.  # noqa: E501
        :type: Address
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def contact_person(self):
        """Gets the contact_person of this WaybillPlaceOfDelivery.  # noqa: E501


        :return: The contact_person of this WaybillPlaceOfDelivery.  # noqa: E501
        :rtype: ContactPerson
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person):
        """Sets the contact_person of this WaybillPlaceOfDelivery.


        :param contact_person: The contact_person of this WaybillPlaceOfDelivery.  # noqa: E501
        :type: ContactPerson
        """

        self._contact_person = contact_person

    @property
    def near_address(self):
        """Gets the near_address of this WaybillPlaceOfDelivery.  # noqa: E501

        Lähiaadress  # noqa: E501

        :return: The near_address of this WaybillPlaceOfDelivery.  # noqa: E501
        :rtype: str
        """
        return self._near_address

    @near_address.setter
    def near_address(self, near_address):
        """Sets the near_address of this WaybillPlaceOfDelivery.

        Lähiaadress  # noqa: E501

        :param near_address: The near_address of this WaybillPlaceOfDelivery.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                near_address is not None and len(near_address) > 150):
            raise ValueError("Invalid value for `near_address`, length must be less than or equal to `150`")  # noqa: E501

        self._near_address = near_address

    @property
    def user_custom_data(self):
        """Gets the user_custom_data of this WaybillPlaceOfDelivery.  # noqa: E501

        Api kasutaja poolt kohandatavad andmed  # noqa: E501

        :return: The user_custom_data of this WaybillPlaceOfDelivery.  # noqa: E501
        :rtype: object
        """
        return self._user_custom_data

    @user_custom_data.setter
    def user_custom_data(self, user_custom_data):
        """Sets the user_custom_data of this WaybillPlaceOfDelivery.

        Api kasutaja poolt kohandatavad andmed  # noqa: E501

        :param user_custom_data: The user_custom_data of this WaybillPlaceOfDelivery.  # noqa: E501
        :type: object
        """

        self._user_custom_data = user_custom_data

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
        if not isinstance(other, WaybillPlaceOfDelivery):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WaybillPlaceOfDelivery):
            return True

        return self.to_dict() != other.to_dict()
