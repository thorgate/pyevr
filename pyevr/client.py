# -*- coding: utf-8 -*-

"""Main module."""
from pyevr.openapi_client.api_client import ApiClient
from pyevr.openapi_client.configuration import Configuration
from pyevr.openapi_client.api import (
    AssortmentsApi, CertificatesApi, MeasurementsApi, MeasurementUnitsApi,
    OrganizationsApi, PlaceOfDeliveriesApi, WaybillsApi,
)


class EVRClient(object):
    """API client class for EVR.

    :param api_key: Company API key in EVR
    :param host: EVR host. Defaults to test host (optional)
    """

    def __init__(self, api_key: str, host: str = None):
        configuration = Configuration(api_key={'EVR-APIKEY': api_key})
        if host is not None:
            configuration.host = host
        self.openapi_client = ApiClient(configuration)

        self.assortments = AssortmentsApi(self.openapi_client)
        self.certificates = CertificatesApi(self.openapi_client)
        self.measurements = MeasurementsApi(self.openapi_client)
        self.measurement_units = MeasurementUnitsApi(self.openapi_client)
        self.organizations = OrganizationsApi(self.openapi_client)
        self.place_of_deliveries = PlaceOfDeliveriesApi(self.openapi_client)
        self.waybills = WaybillsApi(self.openapi_client)
