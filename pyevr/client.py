# -*- coding: utf-8 -*-

"""Main module."""
from pyevr import apis
from pyevr.openapi_client.api_client import ApiClient
from pyevr.openapi_client.configuration import Configuration


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

        self.assortments = apis.AssortmentsAPI(self.openapi_client)
        self.certificates = apis.CertificatesAPI(self.openapi_client)
        self.measurements = apis.MeasurementsAPI(self.openapi_client)
        self.measurement_units = apis.MeasurementUnitsAPI(self.openapi_client)
        self.organizations = apis.OrganizationsAPI(self.openapi_client)
        self.place_of_deliveries = apis.PlaceOfDeliveriesAPI(self.openapi_client)
        self.waybills = apis.WaybillsAPI(self.openapi_client)
