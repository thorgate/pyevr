# coding: utf-8

"""
    EVR API

    OpenAPI Generator'i jaoks kohandatud EVR API kirjeldus. Kasuta seda juhul, kui spetsifikatsioonile vastava EVR API kirjeldusega ei õnnestu klienti genereerida.  # noqa: E501

    The version of the OpenAPI document: 0.14-dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class PlaceOfDelivery(object):
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
        'register_code': 'str',
        'address': 'Address',
        'near_address': 'str',
        'coordinates': 'Coordinates',
        'open_times': 'list[str]',
        'is_public': 'bool',
        'is_active': 'bool',
        'preferred_certificates': 'list[str]',
        'contact_person': 'ContactPerson',
        'waybill_authorizations': 'list[WaybillAuthorization]',
        'description': 'str',
        'user_custom_data': 'object'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code',
        'register_code': 'registerCode',
        'address': 'address',
        'near_address': 'nearAddress',
        'coordinates': 'coordinates',
        'open_times': 'openTimes',
        'is_public': 'isPublic',
        'is_active': 'isActive',
        'preferred_certificates': 'preferredCertificates',
        'contact_person': 'contactPerson',
        'waybill_authorizations': 'waybillAuthorizations',
        'description': 'description',
        'user_custom_data': 'userCustomData'
    }

    def __init__(self, name=None, code=None, register_code=None, address=None, near_address=None, coordinates=None, open_times=None, is_public=None, is_active=None, preferred_certificates=None, contact_person=None, waybill_authorizations=None, description=None, user_custom_data=None, local_vars_configuration=None):  # noqa: E501
        """PlaceOfDelivery - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._code = None
        self._register_code = None
        self._address = None
        self._near_address = None
        self._coordinates = None
        self._open_times = None
        self._is_public = None
        self._is_active = None
        self._preferred_certificates = None
        self._contact_person = None
        self._waybill_authorizations = None
        self._description = None
        self._user_custom_data = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if register_code is not None:
            self.register_code = register_code
        if address is not None:
            self.address = address
        if near_address is not None:
            self.near_address = near_address
        if coordinates is not None:
            self.coordinates = coordinates
        if open_times is not None:
            self.open_times = open_times
        if is_public is not None:
            self.is_public = is_public
        if is_active is not None:
            self.is_active = is_active
        if preferred_certificates is not None:
            self.preferred_certificates = preferred_certificates
        if contact_person is not None:
            self.contact_person = contact_person
        if waybill_authorizations is not None:
            self.waybill_authorizations = waybill_authorizations
        if description is not None:
            self.description = description
        if user_custom_data is not None:
            self.user_custom_data = user_custom_data

    @property
    def name(self):
        """Gets the name of this PlaceOfDelivery.  # noqa: E501

        Tarnekoha nimi  # noqa: E501

        :return: The name of this PlaceOfDelivery.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlaceOfDelivery.

        Tarnekoha nimi  # noqa: E501

        :param name: The name of this PlaceOfDelivery.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this PlaceOfDelivery.  # noqa: E501

        Tarnekoha kood  # noqa: E501

        :return: The code of this PlaceOfDelivery.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PlaceOfDelivery.

        Tarnekoha kood  # noqa: E501

        :param code: The code of this PlaceOfDelivery.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def register_code(self):
        """Gets the register_code of this PlaceOfDelivery.  # noqa: E501

        Registrikood  # noqa: E501

        :return: The register_code of this PlaceOfDelivery.  # noqa: E501
        :rtype: str
        """
        return self._register_code

    @register_code.setter
    def register_code(self, register_code):
        """Sets the register_code of this PlaceOfDelivery.

        Registrikood  # noqa: E501

        :param register_code: The register_code of this PlaceOfDelivery.  # noqa: E501
        :type: str
        """

        self._register_code = register_code

    @property
    def address(self):
        """Gets the address of this PlaceOfDelivery.  # noqa: E501


        :return: The address of this PlaceOfDelivery.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PlaceOfDelivery.


        :param address: The address of this PlaceOfDelivery.  # noqa: E501
        :type: Address
        """

        self._address = address

    @property
    def near_address(self):
        """Gets the near_address of this PlaceOfDelivery.  # noqa: E501

        Lähiaadress  # noqa: E501

        :return: The near_address of this PlaceOfDelivery.  # noqa: E501
        :rtype: str
        """
        return self._near_address

    @near_address.setter
    def near_address(self, near_address):
        """Sets the near_address of this PlaceOfDelivery.

        Lähiaadress  # noqa: E501

        :param near_address: The near_address of this PlaceOfDelivery.  # noqa: E501
        :type: str
        """

        self._near_address = near_address

    @property
    def coordinates(self):
        """Gets the coordinates of this PlaceOfDelivery.  # noqa: E501


        :return: The coordinates of this PlaceOfDelivery.  # noqa: E501
        :rtype: Coordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this PlaceOfDelivery.


        :param coordinates: The coordinates of this PlaceOfDelivery.  # noqa: E501
        :type: Coordinates
        """

        self._coordinates = coordinates

    @property
    def open_times(self):
        """Gets the open_times of this PlaceOfDelivery.  # noqa: E501

        Millal avatud  # noqa: E501

        :return: The open_times of this PlaceOfDelivery.  # noqa: E501
        :rtype: list[str]
        """
        return self._open_times

    @open_times.setter
    def open_times(self, open_times):
        """Sets the open_times of this PlaceOfDelivery.

        Millal avatud  # noqa: E501

        :param open_times: The open_times of this PlaceOfDelivery.  # noqa: E501
        :type: list[str]
        """

        self._open_times = open_times

    @property
    def is_public(self):
        """Gets the is_public of this PlaceOfDelivery.  # noqa: E501

        Kas on avalik  # noqa: E501

        :return: The is_public of this PlaceOfDelivery.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this PlaceOfDelivery.

        Kas on avalik  # noqa: E501

        :param is_public: The is_public of this PlaceOfDelivery.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def is_active(self):
        """Gets the is_active of this PlaceOfDelivery.  # noqa: E501

        Kas on aktiivne  # noqa: E501

        :return: The is_active of this PlaceOfDelivery.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this PlaceOfDelivery.

        Kas on aktiivne  # noqa: E501

        :param is_active: The is_active of this PlaceOfDelivery.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def preferred_certificates(self):
        """Gets the preferred_certificates of this PlaceOfDelivery.  # noqa: E501

        Eelistatud sertifikaadid  # noqa: E501

        :return: The preferred_certificates of this PlaceOfDelivery.  # noqa: E501
        :rtype: list[str]
        """
        return self._preferred_certificates

    @preferred_certificates.setter
    def preferred_certificates(self, preferred_certificates):
        """Sets the preferred_certificates of this PlaceOfDelivery.

        Eelistatud sertifikaadid  # noqa: E501

        :param preferred_certificates: The preferred_certificates of this PlaceOfDelivery.  # noqa: E501
        :type: list[str]
        """

        self._preferred_certificates = preferred_certificates

    @property
    def contact_person(self):
        """Gets the contact_person of this PlaceOfDelivery.  # noqa: E501


        :return: The contact_person of this PlaceOfDelivery.  # noqa: E501
        :rtype: ContactPerson
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person):
        """Sets the contact_person of this PlaceOfDelivery.


        :param contact_person: The contact_person of this PlaceOfDelivery.  # noqa: E501
        :type: ContactPerson
        """

        self._contact_person = contact_person

    @property
    def waybill_authorizations(self):
        """Gets the waybill_authorizations of this PlaceOfDelivery.  # noqa: E501

        Volitused  # noqa: E501

        :return: The waybill_authorizations of this PlaceOfDelivery.  # noqa: E501
        :rtype: list[WaybillAuthorization]
        """
        return self._waybill_authorizations

    @waybill_authorizations.setter
    def waybill_authorizations(self, waybill_authorizations):
        """Sets the waybill_authorizations of this PlaceOfDelivery.

        Volitused  # noqa: E501

        :param waybill_authorizations: The waybill_authorizations of this PlaceOfDelivery.  # noqa: E501
        :type: list[WaybillAuthorization]
        """

        self._waybill_authorizations = waybill_authorizations

    @property
    def description(self):
        """Gets the description of this PlaceOfDelivery.  # noqa: E501

        Märkused  # noqa: E501

        :return: The description of this PlaceOfDelivery.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PlaceOfDelivery.

        Märkused  # noqa: E501

        :param description: The description of this PlaceOfDelivery.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 400):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `400`")  # noqa: E501

        self._description = description

    @property
    def user_custom_data(self):
        """Gets the user_custom_data of this PlaceOfDelivery.  # noqa: E501

        Api kasutaja poolt kohandatavad andmed  # noqa: E501

        :return: The user_custom_data of this PlaceOfDelivery.  # noqa: E501
        :rtype: object
        """
        return self._user_custom_data

    @user_custom_data.setter
    def user_custom_data(self, user_custom_data):
        """Sets the user_custom_data of this PlaceOfDelivery.

        Api kasutaja poolt kohandatavad andmed  # noqa: E501

        :param user_custom_data: The user_custom_data of this PlaceOfDelivery.  # noqa: E501
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
        if not isinstance(other, PlaceOfDelivery):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlaceOfDelivery):
            return True

        return self.to_dict() != other.to_dict()
