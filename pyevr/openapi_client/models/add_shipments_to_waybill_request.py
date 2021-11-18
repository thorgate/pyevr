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


class AddShipmentsToWaybillRequest(object):
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
        'shipments': 'list[Shipment]'
    }

    attribute_map = {
        'shipments': 'shipments'
    }

    def __init__(self, shipments=None, local_vars_configuration=None):  # noqa: E501
        """AddShipmentsToWaybillRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._shipments = None
        self.discriminator = None

        self.shipments = shipments

    @property
    def shipments(self):
        """Gets the shipments of this AddShipmentsToWaybillRequest.  # noqa: E501

        Lisatavad veose andmed  # noqa: E501

        :return: The shipments of this AddShipmentsToWaybillRequest.  # noqa: E501
        :rtype: list[Shipment]
        """
        return self._shipments

    @shipments.setter
    def shipments(self, shipments):
        """Sets the shipments of this AddShipmentsToWaybillRequest.

        Lisatavad veose andmed  # noqa: E501

        :param shipments: The shipments of this AddShipmentsToWaybillRequest.  # noqa: E501
        :type: list[Shipment]
        """
        if self.local_vars_configuration.client_side_validation and shipments is None:  # noqa: E501
            raise ValueError("Invalid value for `shipments`, must not be `None`")  # noqa: E501

        self._shipments = shipments

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
        if not isinstance(other, AddShipmentsToWaybillRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddShipmentsToWaybillRequest):
            return True

        return self.to_dict() != other.to_dict()
