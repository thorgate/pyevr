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


class Waybill(object):
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
        'owner': 'Owner',
        'transport': 'Transport',
        'receiver': 'Receiver',
        'place_of_delivery': 'WaybillPlaceOfDelivery',
        'comment': 'str',
        'departure_time': 'datetime',
        'submission_time': 'datetime',
        'shipments': 'list[Shipment]',
        'pre_journey_mileage': 'int',
        'user_custom_data': 'object',
        'mass': 'float',
        'number': 'str',
        'status': 'WaybillStatus',
        'creation_time': 'datetime',
        'cancellation_time': 'datetime',
        'cancellation_reason': 'str',
        'total_journey_mileage': 'int',
        'unloading_comment': 'str',
        'unloading_time': 'datetime',
        'finishing_time': 'datetime',
        'last_modification_time': 'datetime',
        'waybill_authorizations': 'list[WaybillAuthorization]'
    }

    attribute_map = {
        'owner': 'owner',
        'transport': 'transport',
        'receiver': 'receiver',
        'place_of_delivery': 'placeOfDelivery',
        'comment': 'comment',
        'departure_time': 'departureTime',
        'submission_time': 'submissionTime',
        'shipments': 'shipments',
        'pre_journey_mileage': 'preJourneyMileage',
        'user_custom_data': 'userCustomData',
        'mass': 'mass',
        'number': 'number',
        'status': 'status',
        'creation_time': 'creationTime',
        'cancellation_time': 'cancellationTime',
        'cancellation_reason': 'cancellationReason',
        'total_journey_mileage': 'totalJourneyMileage',
        'unloading_comment': 'unloadingComment',
        'unloading_time': 'unloadingTime',
        'finishing_time': 'finishingTime',
        'last_modification_time': 'lastModificationTime',
        'waybill_authorizations': 'waybillAuthorizations'
    }

    def __init__(self, owner=None, transport=None, receiver=None, place_of_delivery=None, comment=None, departure_time=None, submission_time=None, shipments=None, pre_journey_mileage=None, user_custom_data=None, mass=None, number=None, status=None, creation_time=None, cancellation_time=None, cancellation_reason=None, total_journey_mileage=None, unloading_comment=None, unloading_time=None, finishing_time=None, last_modification_time=None, waybill_authorizations=None, local_vars_configuration=None):  # noqa: E501
        """Waybill - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._owner = None
        self._transport = None
        self._receiver = None
        self._place_of_delivery = None
        self._comment = None
        self._departure_time = None
        self._submission_time = None
        self._shipments = None
        self._pre_journey_mileage = None
        self._user_custom_data = None
        self._mass = None
        self._number = None
        self._status = None
        self._creation_time = None
        self._cancellation_time = None
        self._cancellation_reason = None
        self._total_journey_mileage = None
        self._unloading_comment = None
        self._unloading_time = None
        self._finishing_time = None
        self._last_modification_time = None
        self._waybill_authorizations = None
        self.discriminator = None

        self.owner = owner
        self.transport = transport
        self.receiver = receiver
        self.place_of_delivery = place_of_delivery
        if comment is not None:
            self.comment = comment
        self.departure_time = departure_time
        self.submission_time = submission_time
        self.shipments = shipments
        self.pre_journey_mileage = pre_journey_mileage
        if user_custom_data is not None:
            self.user_custom_data = user_custom_data
        self.mass = mass
        if number is not None:
            self.number = number
        if status is not None:
            self.status = status
        if creation_time is not None:
            self.creation_time = creation_time
        self.cancellation_time = cancellation_time
        self.cancellation_reason = cancellation_reason
        self.total_journey_mileage = total_journey_mileage
        self.unloading_comment = unloading_comment
        self.unloading_time = unloading_time
        self.finishing_time = finishing_time
        self.last_modification_time = last_modification_time
        self.waybill_authorizations = waybill_authorizations

    @property
    def owner(self):
        """Gets the owner of this Waybill.  # noqa: E501


        :return: The owner of this Waybill.  # noqa: E501
        :rtype: Owner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Waybill.


        :param owner: The owner of this Waybill.  # noqa: E501
        :type: Owner
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def transport(self):
        """Gets the transport of this Waybill.  # noqa: E501


        :return: The transport of this Waybill.  # noqa: E501
        :rtype: Transport
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """Sets the transport of this Waybill.


        :param transport: The transport of this Waybill.  # noqa: E501
        :type: Transport
        """
        if self.local_vars_configuration.client_side_validation and transport is None:  # noqa: E501
            raise ValueError("Invalid value for `transport`, must not be `None`")  # noqa: E501

        self._transport = transport

    @property
    def receiver(self):
        """Gets the receiver of this Waybill.  # noqa: E501


        :return: The receiver of this Waybill.  # noqa: E501
        :rtype: Receiver
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this Waybill.


        :param receiver: The receiver of this Waybill.  # noqa: E501
        :type: Receiver
        """
        if self.local_vars_configuration.client_side_validation and receiver is None:  # noqa: E501
            raise ValueError("Invalid value for `receiver`, must not be `None`")  # noqa: E501

        self._receiver = receiver

    @property
    def place_of_delivery(self):
        """Gets the place_of_delivery of this Waybill.  # noqa: E501


        :return: The place_of_delivery of this Waybill.  # noqa: E501
        :rtype: WaybillPlaceOfDelivery
        """
        return self._place_of_delivery

    @place_of_delivery.setter
    def place_of_delivery(self, place_of_delivery):
        """Sets the place_of_delivery of this Waybill.


        :param place_of_delivery: The place_of_delivery of this Waybill.  # noqa: E501
        :type: WaybillPlaceOfDelivery
        """
        if self.local_vars_configuration.client_side_validation and place_of_delivery is None:  # noqa: E501
            raise ValueError("Invalid value for `place_of_delivery`, must not be `None`")  # noqa: E501

        self._place_of_delivery = place_of_delivery

    @property
    def comment(self):
        """Gets the comment of this Waybill.  # noqa: E501

        Märkused/lisainfo  # noqa: E501

        :return: The comment of this Waybill.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Waybill.

        Märkused/lisainfo  # noqa: E501

        :param comment: The comment of this Waybill.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                comment is not None and len(comment) > 400):
            raise ValueError("Invalid value for `comment`, length must be less than or equal to `400`")  # noqa: E501

        self._comment = comment

    @property
    def departure_time(self):
        """Gets the departure_time of this Waybill.  # noqa: E501

        Väljasõidu aeg  # noqa: E501

        :return: The departure_time of this Waybill.  # noqa: E501
        :rtype: datetime
        """
        return self._departure_time

    @departure_time.setter
    def departure_time(self, departure_time):
        """Sets the departure_time of this Waybill.

        Väljasõidu aeg  # noqa: E501

        :param departure_time: The departure_time of this Waybill.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and departure_time is None:  # noqa: E501
            raise ValueError("Invalid value for `departure_time`, must not be `None`")  # noqa: E501

        self._departure_time = departure_time

    @property
    def submission_time(self):
        """Gets the submission_time of this Waybill.  # noqa: E501

        Veoselehe EVR-i saatmise aeg  # noqa: E501

        :return: The submission_time of this Waybill.  # noqa: E501
        :rtype: datetime
        """
        return self._submission_time

    @submission_time.setter
    def submission_time(self, submission_time):
        """Sets the submission_time of this Waybill.

        Veoselehe EVR-i saatmise aeg  # noqa: E501

        :param submission_time: The submission_time of this Waybill.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and submission_time is None:  # noqa: E501
            raise ValueError("Invalid value for `submission_time`, must not be `None`")  # noqa: E501

        self._submission_time = submission_time

    @property
    def shipments(self):
        """Gets the shipments of this Waybill.  # noqa: E501

        Lähetatud veose andmed  # noqa: E501

        :return: The shipments of this Waybill.  # noqa: E501
        :rtype: list[Shipment]
        """
        return self._shipments

    @shipments.setter
    def shipments(self, shipments):
        """Sets the shipments of this Waybill.

        Lähetatud veose andmed  # noqa: E501

        :param shipments: The shipments of this Waybill.  # noqa: E501
        :type: list[Shipment]
        """
        if self.local_vars_configuration.client_side_validation and shipments is None:  # noqa: E501
            raise ValueError("Invalid value for `shipments`, must not be `None`")  # noqa: E501

        self._shipments = shipments

    @property
    def pre_journey_mileage(self):
        """Gets the pre_journey_mileage of this Waybill.  # noqa: E501

        Ettesõidu kilometraaž  # noqa: E501

        :return: The pre_journey_mileage of this Waybill.  # noqa: E501
        :rtype: int
        """
        return self._pre_journey_mileage

    @pre_journey_mileage.setter
    def pre_journey_mileage(self, pre_journey_mileage):
        """Sets the pre_journey_mileage of this Waybill.

        Ettesõidu kilometraaž  # noqa: E501

        :param pre_journey_mileage: The pre_journey_mileage of this Waybill.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                pre_journey_mileage is not None and pre_journey_mileage > 100000):  # noqa: E501
            raise ValueError("Invalid value for `pre_journey_mileage`, must be a value less than or equal to `100000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pre_journey_mileage is not None and pre_journey_mileage < 1):  # noqa: E501
            raise ValueError("Invalid value for `pre_journey_mileage`, must be a value greater than or equal to `1`")  # noqa: E501

        self._pre_journey_mileage = pre_journey_mileage

    @property
    def user_custom_data(self):
        """Gets the user_custom_data of this Waybill.  # noqa: E501

        Api kasutaja poolt kohandatavad andmed  # noqa: E501

        :return: The user_custom_data of this Waybill.  # noqa: E501
        :rtype: object
        """
        return self._user_custom_data

    @user_custom_data.setter
    def user_custom_data(self, user_custom_data):
        """Sets the user_custom_data of this Waybill.

        Api kasutaja poolt kohandatavad andmed  # noqa: E501

        :param user_custom_data: The user_custom_data of this Waybill.  # noqa: E501
        :type: object
        """

        self._user_custom_data = user_custom_data

    @property
    def mass(self):
        """Gets the mass of this Waybill.  # noqa: E501

        Autorongi mass tonnides  # noqa: E501

        :return: The mass of this Waybill.  # noqa: E501
        :rtype: float
        """
        return self._mass

    @mass.setter
    def mass(self, mass):
        """Sets the mass of this Waybill.

        Autorongi mass tonnides  # noqa: E501

        :param mass: The mass of this Waybill.  # noqa: E501
        :type: float
        """

        self._mass = mass

    @property
    def number(self):
        """Gets the number of this Waybill.  # noqa: E501

        Veoselehe number  # noqa: E501

        :return: The number of this Waybill.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Waybill.

        Veoselehe number  # noqa: E501

        :param number: The number of this Waybill.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def status(self):
        """Gets the status of this Waybill.  # noqa: E501


        :return: The status of this Waybill.  # noqa: E501
        :rtype: WaybillStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Waybill.


        :param status: The status of this Waybill.  # noqa: E501
        :type: WaybillStatus
        """

        self._status = status

    @property
    def creation_time(self):
        """Gets the creation_time of this Waybill.  # noqa: E501

        Loomise aeg  # noqa: E501

        :return: The creation_time of this Waybill.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Waybill.

        Loomise aeg  # noqa: E501

        :param creation_time: The creation_time of this Waybill.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def cancellation_time(self):
        """Gets the cancellation_time of this Waybill.  # noqa: E501

        Tühistamise aeg (kui veoseleht on tühistatud)  # noqa: E501

        :return: The cancellation_time of this Waybill.  # noqa: E501
        :rtype: datetime
        """
        return self._cancellation_time

    @cancellation_time.setter
    def cancellation_time(self, cancellation_time):
        """Sets the cancellation_time of this Waybill.

        Tühistamise aeg (kui veoseleht on tühistatud)  # noqa: E501

        :param cancellation_time: The cancellation_time of this Waybill.  # noqa: E501
        :type: datetime
        """

        self._cancellation_time = cancellation_time

    @property
    def cancellation_reason(self):
        """Gets the cancellation_reason of this Waybill.  # noqa: E501

        Tühistamise põhjus (kui veoseleht on tühistatud)  # noqa: E501

        :return: The cancellation_reason of this Waybill.  # noqa: E501
        :rtype: str
        """
        return self._cancellation_reason

    @cancellation_reason.setter
    def cancellation_reason(self, cancellation_reason):
        """Sets the cancellation_reason of this Waybill.

        Tühistamise põhjus (kui veoseleht on tühistatud)  # noqa: E501

        :param cancellation_reason: The cancellation_reason of this Waybill.  # noqa: E501
        :type: str
        """

        self._cancellation_reason = cancellation_reason

    @property
    def total_journey_mileage(self):
        """Gets the total_journey_mileage of this Waybill.  # noqa: E501

        Kilometraaž koormaga (kui veoselehel on vedu lõpetatud)  # noqa: E501

        :return: The total_journey_mileage of this Waybill.  # noqa: E501
        :rtype: int
        """
        return self._total_journey_mileage

    @total_journey_mileage.setter
    def total_journey_mileage(self, total_journey_mileage):
        """Sets the total_journey_mileage of this Waybill.

        Kilometraaž koormaga (kui veoselehel on vedu lõpetatud)  # noqa: E501

        :param total_journey_mileage: The total_journey_mileage of this Waybill.  # noqa: E501
        :type: int
        """

        self._total_journey_mileage = total_journey_mileage

    @property
    def unloading_comment(self):
        """Gets the unloading_comment of this Waybill.  # noqa: E501

        Mahalaadimise kommentaar (kui veoselehel on vedu lõpetatud)  # noqa: E501

        :return: The unloading_comment of this Waybill.  # noqa: E501
        :rtype: str
        """
        return self._unloading_comment

    @unloading_comment.setter
    def unloading_comment(self, unloading_comment):
        """Sets the unloading_comment of this Waybill.

        Mahalaadimise kommentaar (kui veoselehel on vedu lõpetatud)  # noqa: E501

        :param unloading_comment: The unloading_comment of this Waybill.  # noqa: E501
        :type: str
        """

        self._unloading_comment = unloading_comment

    @property
    def unloading_time(self):
        """Gets the unloading_time of this Waybill.  # noqa: E501

        Mahalaadimise aeg (kui veoselehel on vedu lõpetatud)  # noqa: E501

        :return: The unloading_time of this Waybill.  # noqa: E501
        :rtype: datetime
        """
        return self._unloading_time

    @unloading_time.setter
    def unloading_time(self, unloading_time):
        """Sets the unloading_time of this Waybill.

        Mahalaadimise aeg (kui veoselehel on vedu lõpetatud)  # noqa: E501

        :param unloading_time: The unloading_time of this Waybill.  # noqa: E501
        :type: datetime
        """

        self._unloading_time = unloading_time

    @property
    def finishing_time(self):
        """Gets the finishing_time of this Waybill.  # noqa: E501

        Veoselehe lõpetamise aeg (kui veoseleht on lõpetatud)  # noqa: E501

        :return: The finishing_time of this Waybill.  # noqa: E501
        :rtype: datetime
        """
        return self._finishing_time

    @finishing_time.setter
    def finishing_time(self, finishing_time):
        """Sets the finishing_time of this Waybill.

        Veoselehe lõpetamise aeg (kui veoseleht on lõpetatud)  # noqa: E501

        :param finishing_time: The finishing_time of this Waybill.  # noqa: E501
        :type: datetime
        """

        self._finishing_time = finishing_time

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this Waybill.  # noqa: E501

        Veoselehe viimase muutmise aeg  # noqa: E501

        :return: The last_modification_time of this Waybill.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this Waybill.

        Veoselehe viimase muutmise aeg  # noqa: E501

        :param last_modification_time: The last_modification_time of this Waybill.  # noqa: E501
        :type: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def waybill_authorizations(self):
        """Gets the waybill_authorizations of this Waybill.  # noqa: E501

        Veoselehe volitused  # noqa: E501

        :return: The waybill_authorizations of this Waybill.  # noqa: E501
        :rtype: list[WaybillAuthorization]
        """
        return self._waybill_authorizations

    @waybill_authorizations.setter
    def waybill_authorizations(self, waybill_authorizations):
        """Sets the waybill_authorizations of this Waybill.

        Veoselehe volitused  # noqa: E501

        :param waybill_authorizations: The waybill_authorizations of this Waybill.  # noqa: E501
        :type: list[WaybillAuthorization]
        """

        self._waybill_authorizations = waybill_authorizations

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
        if not isinstance(other, Waybill):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Waybill):
            return True

        return self.to_dict() != other.to_dict()
