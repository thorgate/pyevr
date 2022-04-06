# coding: utf-8

"""
    EVR API

    OpenAPI Generator'i jaoks kohandatud EVR API kirjeldus. Kasuta seda juhul, kui spetsifikatsioonile vastava EVR API kirjeldusega ei õnnestu klienti genereerida.  # noqa: E501

    The version of the OpenAPI document: 1.5.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pyevr.openapi_client.configuration import Configuration


class Source(object):
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
        'compartment': 'str',
        'appropriation': 'str',
        'planning_area': 'str',
        'address': 'Address',
        'coordinates': 'Coordinates',
        'contact_person': 'ContactPerson',
        'near_address': 'str',
        'source_document_url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code',
        'compartment': 'compartment',
        'appropriation': 'appropriation',
        'planning_area': 'planningArea',
        'address': 'address',
        'coordinates': 'coordinates',
        'contact_person': 'contactPerson',
        'near_address': 'nearAddress',
        'source_document_url': 'sourceDocumentUrl'
    }

    def __init__(self, name=None, code=None, compartment=None, appropriation=None, planning_area=None, address=None, coordinates=None, contact_person=None, near_address=None, source_document_url=None, local_vars_configuration=None):  # noqa: E501
        """Source - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._code = None
        self._compartment = None
        self._appropriation = None
        self._planning_area = None
        self._address = None
        self._coordinates = None
        self._contact_person = None
        self._near_address = None
        self._source_document_url = None
        self.discriminator = None

        self.name = name
        self.code = code
        self.compartment = compartment
        self.appropriation = appropriation
        self.planning_area = planning_area
        self.address = address
        if coordinates is not None:
            self.coordinates = coordinates
        if contact_person is not None:
            self.contact_person = contact_person
        self.near_address = near_address
        self.source_document_url = source_document_url

    @property
    def name(self):
        """Gets the name of this Source.  # noqa: E501

        Maaüksuse või laoplatsi nimi  # noqa: E501

        :return: The name of this Source.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Source.

        Maaüksuse või laoplatsi nimi  # noqa: E501

        :param name: The name of this Source.  # noqa: E501
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
    def code(self):
        """Gets the code of this Source.  # noqa: E501

        Laokood  # noqa: E501

        :return: The code of this Source.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Source.

        Laokood  # noqa: E501

        :param code: The code of this Source.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 50):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `50`")  # noqa: E501

        self._code = code

    @property
    def compartment(self):
        """Gets the compartment of this Source.  # noqa: E501

        Kvartal  # noqa: E501

        :return: The compartment of this Source.  # noqa: E501
        :rtype: str
        """
        return self._compartment

    @compartment.setter
    def compartment(self, compartment):
        """Sets the compartment of this Source.

        Kvartal  # noqa: E501

        :param compartment: The compartment of this Source.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                compartment is not None and len(compartment) > 100):
            raise ValueError("Invalid value for `compartment`, length must be less than or equal to `100`")  # noqa: E501

        self._compartment = compartment

    @property
    def appropriation(self):
        """Gets the appropriation of this Source.  # noqa: E501

        Eraldis  # noqa: E501

        :return: The appropriation of this Source.  # noqa: E501
        :rtype: str
        """
        return self._appropriation

    @appropriation.setter
    def appropriation(self, appropriation):
        """Sets the appropriation of this Source.

        Eraldis  # noqa: E501

        :param appropriation: The appropriation of this Source.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                appropriation is not None and len(appropriation) > 200):
            raise ValueError("Invalid value for `appropriation`, length must be less than or equal to `200`")  # noqa: E501

        self._appropriation = appropriation

    @property
    def planning_area(self):
        """Gets the planning_area of this Source.  # noqa: E501

        Planeerimispiirkond  # noqa: E501

        :return: The planning_area of this Source.  # noqa: E501
        :rtype: str
        """
        return self._planning_area

    @planning_area.setter
    def planning_area(self, planning_area):
        """Sets the planning_area of this Source.

        Planeerimispiirkond  # noqa: E501

        :param planning_area: The planning_area of this Source.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                planning_area is not None and len(planning_area) > 100):
            raise ValueError("Invalid value for `planning_area`, length must be less than or equal to `100`")  # noqa: E501

        self._planning_area = planning_area

    @property
    def address(self):
        """Gets the address of this Source.  # noqa: E501


        :return: The address of this Source.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Source.


        :param address: The address of this Source.  # noqa: E501
        :type: Address
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def coordinates(self):
        """Gets the coordinates of this Source.  # noqa: E501


        :return: The coordinates of this Source.  # noqa: E501
        :rtype: Coordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Source.


        :param coordinates: The coordinates of this Source.  # noqa: E501
        :type: Coordinates
        """

        self._coordinates = coordinates

    @property
    def contact_person(self):
        """Gets the contact_person of this Source.  # noqa: E501


        :return: The contact_person of this Source.  # noqa: E501
        :rtype: ContactPerson
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person):
        """Sets the contact_person of this Source.


        :param contact_person: The contact_person of this Source.  # noqa: E501
        :type: ContactPerson
        """

        self._contact_person = contact_person

    @property
    def near_address(self):
        """Gets the near_address of this Source.  # noqa: E501

        Lähiaadress  # noqa: E501

        :return: The near_address of this Source.  # noqa: E501
        :rtype: str
        """
        return self._near_address

    @near_address.setter
    def near_address(self, near_address):
        """Sets the near_address of this Source.

        Lähiaadress  # noqa: E501

        :param near_address: The near_address of this Source.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                near_address is not None and len(near_address) > 150):
            raise ValueError("Invalid value for `near_address`, length must be less than or equal to `150`")  # noqa: E501

        self._near_address = near_address

    @property
    def source_document_url(self):
        """Gets the source_document_url of this Source.  # noqa: E501

        Päritoludokumendi URL  # noqa: E501

        :return: The source_document_url of this Source.  # noqa: E501
        :rtype: str
        """
        return self._source_document_url

    @source_document_url.setter
    def source_document_url(self, source_document_url):
        """Sets the source_document_url of this Source.

        Päritoludokumendi URL  # noqa: E501

        :param source_document_url: The source_document_url of this Source.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                source_document_url is not None and len(source_document_url) > 2000):
            raise ValueError("Invalid value for `source_document_url`, length must be less than or equal to `2000`")  # noqa: E501

        self._source_document_url = source_document_url

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
        if not isinstance(other, Source):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Source):
            return True

        return self.to_dict() != other.to_dict()
