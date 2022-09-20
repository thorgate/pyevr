# coding: utf-8

"""
    EVR API

    OpenAPI Generator'i jaoks kohandatud EVR API kirjeldus. Kasuta seda juhul, kui spetsifikatsioonile vastava EVR API kirjeldusega ei õnnestu klienti genereerida.  # noqa: E501

    The version of the OpenAPI document: 1.9.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pyevr.openapi_client.configuration import Configuration


class PutPlaceOfDeliveryRequest(object):
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
        'address': 'Address',
        'near_address': 'str',
        'coordinates': 'Coordinates',
        'description': 'str',
        'is_active': 'bool',
        'is_public': 'bool',
        'preferred_certificates': 'list[str]',
        'open_times': 'list[str]',
        'contact_person': 'ContactPerson',
        'waybill_authorizations': 'list[WaybillAuthorization]',
        'user_custom_data': 'object'
    }

    attribute_map = {
        'name': 'name',
        'address': 'address',
        'near_address': 'nearAddress',
        'coordinates': 'coordinates',
        'description': 'description',
        'is_active': 'isActive',
        'is_public': 'isPublic',
        'preferred_certificates': 'preferredCertificates',
        'open_times': 'openTimes',
        'contact_person': 'contactPerson',
        'waybill_authorizations': 'waybillAuthorizations',
        'user_custom_data': 'userCustomData'
    }

    def __init__(self, name=None, address=None, near_address=None, coordinates=None, description=None, is_active=None, is_public=None, preferred_certificates=None, open_times=None, contact_person=None, waybill_authorizations=None, user_custom_data=None, local_vars_configuration=None):  # noqa: E501
        """PutPlaceOfDeliveryRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._address = None
        self._near_address = None
        self._coordinates = None
        self._description = None
        self._is_active = None
        self._is_public = None
        self._preferred_certificates = None
        self._open_times = None
        self._contact_person = None
        self._waybill_authorizations = None
        self._user_custom_data = None
        self.discriminator = None

        self.name = name
        self.address = address
        if near_address is not None:
            self.near_address = near_address
        self.coordinates = coordinates
        if description is not None:
            self.description = description
        self.is_active = is_active
        self.is_public = is_public
        if preferred_certificates is not None:
            self.preferred_certificates = preferred_certificates
        if open_times is not None:
            self.open_times = open_times
        if contact_person is not None:
            self.contact_person = contact_person
        if waybill_authorizations is not None:
            self.waybill_authorizations = waybill_authorizations
        if user_custom_data is not None:
            self.user_custom_data = user_custom_data

    @property
    def name(self):
        """Gets the name of this PutPlaceOfDeliveryRequest.  # noqa: E501

        Nimi  # noqa: E501

        :return: The name of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutPlaceOfDeliveryRequest.

        Nimi  # noqa: E501

        :param name: The name of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def address(self):
        """Gets the address of this PutPlaceOfDeliveryRequest.  # noqa: E501


        :return: The address of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PutPlaceOfDeliveryRequest.


        :param address: The address of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :type: Address
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def near_address(self):
        """Gets the near_address of this PutPlaceOfDeliveryRequest.  # noqa: E501

        Lähiaadress  # noqa: E501

        :return: The near_address of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :rtype: str
        """
        return self._near_address

    @near_address.setter
    def near_address(self, near_address):
        """Sets the near_address of this PutPlaceOfDeliveryRequest.

        Lähiaadress  # noqa: E501

        :param near_address: The near_address of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                near_address is not None and len(near_address) > 150):
            raise ValueError("Invalid value for `near_address`, length must be less than or equal to `150`")  # noqa: E501

        self._near_address = near_address

    @property
    def coordinates(self):
        """Gets the coordinates of this PutPlaceOfDeliveryRequest.  # noqa: E501


        :return: The coordinates of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :rtype: Coordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this PutPlaceOfDeliveryRequest.


        :param coordinates: The coordinates of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :type: Coordinates
        """
        if self.local_vars_configuration.client_side_validation and coordinates is None:  # noqa: E501
            raise ValueError("Invalid value for `coordinates`, must not be `None`")  # noqa: E501

        self._coordinates = coordinates

    @property
    def description(self):
        """Gets the description of this PutPlaceOfDeliveryRequest.  # noqa: E501

        Märkused  # noqa: E501

        :return: The description of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutPlaceOfDeliveryRequest.

        Märkused  # noqa: E501

        :param description: The description of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 400):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `400`")  # noqa: E501

        self._description = description

    @property
    def is_active(self):
        """Gets the is_active of this PutPlaceOfDeliveryRequest.  # noqa: E501

        Kas on aktiivne  # noqa: E501

        :return: The is_active of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this PutPlaceOfDeliveryRequest.

        Kas on aktiivne  # noqa: E501

        :param is_active: The is_active of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_active is None:  # noqa: E501
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

    @property
    def is_public(self):
        """Gets the is_public of this PutPlaceOfDeliveryRequest.  # noqa: E501

        Kas on avalik (avalikke ladusid näevad ka teised asutused)  # noqa: E501

        :return: The is_public of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this PutPlaceOfDeliveryRequest.

        Kas on avalik (avalikke ladusid näevad ka teised asutused)  # noqa: E501

        :param is_public: The is_public of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_public is None:  # noqa: E501
            raise ValueError("Invalid value for `is_public`, must not be `None`")  # noqa: E501

        self._is_public = is_public

    @property
    def preferred_certificates(self):
        """Gets the preferred_certificates of this PutPlaceOfDeliveryRequest.  # noqa: E501

        Eelistatud sertifikaadid  # noqa: E501

        :return: The preferred_certificates of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._preferred_certificates

    @preferred_certificates.setter
    def preferred_certificates(self, preferred_certificates):
        """Sets the preferred_certificates of this PutPlaceOfDeliveryRequest.

        Eelistatud sertifikaadid  # noqa: E501

        :param preferred_certificates: The preferred_certificates of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :type: list[str]
        """

        self._preferred_certificates = preferred_certificates

    @property
    def open_times(self):
        """Gets the open_times of this PutPlaceOfDeliveryRequest.  # noqa: E501

        Millal avatud  # noqa: E501

        :return: The open_times of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._open_times

    @open_times.setter
    def open_times(self, open_times):
        """Sets the open_times of this PutPlaceOfDeliveryRequest.

        Millal avatud  # noqa: E501

        :param open_times: The open_times of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :type: list[str]
        """

        self._open_times = open_times

    @property
    def contact_person(self):
        """Gets the contact_person of this PutPlaceOfDeliveryRequest.  # noqa: E501


        :return: The contact_person of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :rtype: ContactPerson
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person):
        """Sets the contact_person of this PutPlaceOfDeliveryRequest.


        :param contact_person: The contact_person of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :type: ContactPerson
        """

        self._contact_person = contact_person

    @property
    def waybill_authorizations(self):
        """Gets the waybill_authorizations of this PutPlaceOfDeliveryRequest.  # noqa: E501

        Volitatud mõõtjad ja vaatlejad  # noqa: E501

        :return: The waybill_authorizations of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :rtype: list[WaybillAuthorization]
        """
        return self._waybill_authorizations

    @waybill_authorizations.setter
    def waybill_authorizations(self, waybill_authorizations):
        """Sets the waybill_authorizations of this PutPlaceOfDeliveryRequest.

        Volitatud mõõtjad ja vaatlejad  # noqa: E501

        :param waybill_authorizations: The waybill_authorizations of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :type: list[WaybillAuthorization]
        """

        self._waybill_authorizations = waybill_authorizations

    @property
    def user_custom_data(self):
        """Gets the user_custom_data of this PutPlaceOfDeliveryRequest.  # noqa: E501

        Api kasutaja poolt kohandatavad andmed  # noqa: E501

        :return: The user_custom_data of this PutPlaceOfDeliveryRequest.  # noqa: E501
        :rtype: object
        """
        return self._user_custom_data

    @user_custom_data.setter
    def user_custom_data(self, user_custom_data):
        """Sets the user_custom_data of this PutPlaceOfDeliveryRequest.

        Api kasutaja poolt kohandatavad andmed  # noqa: E501

        :param user_custom_data: The user_custom_data of this PutPlaceOfDeliveryRequest.  # noqa: E501
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
        if not isinstance(other, PutPlaceOfDeliveryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutPlaceOfDeliveryRequest):
            return True

        return self.to_dict() != other.to_dict()
