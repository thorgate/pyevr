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


class AddMeasurementActRequest(object):
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
        'act_number': 'str',
        'measurements': 'list[ShipmentItem]',
        'custom_measurement_data': 'object'
    }

    attribute_map = {
        'act_number': 'actNumber',
        'measurements': 'measurements',
        'custom_measurement_data': 'customMeasurementData'
    }

    def __init__(self, act_number=None, measurements=None, custom_measurement_data=None, local_vars_configuration=None):  # noqa: E501
        """AddMeasurementActRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._act_number = None
        self._measurements = None
        self._custom_measurement_data = None
        self.discriminator = None

        self.act_number = act_number
        self.measurements = measurements
        self.custom_measurement_data = custom_measurement_data

    @property
    def act_number(self):
        """Gets the act_number of this AddMeasurementActRequest.  # noqa: E501

        Mõõtmisakti number  # noqa: E501

        :return: The act_number of this AddMeasurementActRequest.  # noqa: E501
        :rtype: str
        """
        return self._act_number

    @act_number.setter
    def act_number(self, act_number):
        """Sets the act_number of this AddMeasurementActRequest.

        Mõõtmisakti number  # noqa: E501

        :param act_number: The act_number of this AddMeasurementActRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                act_number is not None and len(act_number) > 25):
            raise ValueError("Invalid value for `act_number`, length must be less than or equal to `25`")  # noqa: E501

        self._act_number = act_number

    @property
    def measurements(self):
        """Gets the measurements of this AddMeasurementActRequest.  # noqa: E501

        Mõõtmistulemused  # noqa: E501

        :return: The measurements of this AddMeasurementActRequest.  # noqa: E501
        :rtype: list[ShipmentItem]
        """
        return self._measurements

    @measurements.setter
    def measurements(self, measurements):
        """Sets the measurements of this AddMeasurementActRequest.

        Mõõtmistulemused  # noqa: E501

        :param measurements: The measurements of this AddMeasurementActRequest.  # noqa: E501
        :type: list[ShipmentItem]
        """

        self._measurements = measurements

    @property
    def custom_measurement_data(self):
        """Gets the custom_measurement_data of this AddMeasurementActRequest.  # noqa: E501

        Mõõtmistulemused vabas formaadis.  # noqa: E501

        :return: The custom_measurement_data of this AddMeasurementActRequest.  # noqa: E501
        :rtype: object
        """
        return self._custom_measurement_data

    @custom_measurement_data.setter
    def custom_measurement_data(self, custom_measurement_data):
        """Sets the custom_measurement_data of this AddMeasurementActRequest.

        Mõõtmistulemused vabas formaadis.  # noqa: E501

        :param custom_measurement_data: The custom_measurement_data of this AddMeasurementActRequest.  # noqa: E501
        :type: object
        """

        self._custom_measurement_data = custom_measurement_data

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
        if not isinstance(other, AddMeasurementActRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddMeasurementActRequest):
            return True

        return self.to_dict() != other.to_dict()