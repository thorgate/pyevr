#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `EVRClient`."""

import unittest

from pyevr import EVRClient


class TestEVRClient(unittest.TestCase):
    api_key = 'asd123'
    host = 'https://api.evr.test'

    def setUp(self) -> None:
        super().setUp()
        self.client = EVRClient(self.api_key, self.host)

    def test_initial_api_key(self):
        self.assertRaises(TypeError, EVRClient)
        self.assertDictEqual(self.client.openapi_client.configuration.api_key, {'EVR-APIKEY': self.api_key})

    def test_initial_host(self):
        self.assertEqual(self.client.openapi_client.configuration.host, self.host)
        client = EVRClient(self.api_key)
        self.assertEqual(client.openapi_client.configuration.host, 'https://evr-test.azurewebsites.net')

    def test_api_groups(self):
        from pyevr.openapi_client import api
        self.assertEqual(type(self.client.assortments), api.AssortmentsApi)
        self.assertEqual(type(self.client.certificates), api.CertificatesApi)
        self.assertEqual(type(self.client.measurements), api.MeasurementsApi)
        self.assertEqual(type(self.client.measurement_units), api.MeasurementUnitsApi)
        self.assertEqual(type(self.client.organizations), api.OrganizationsApi)
        self.assertEqual(type(self.client.place_of_deliveries), api.PlaceOfDeliveriesApi)
        self.assertEqual(type(self.client.waybills), api.WaybillsApi)


if __name__ == '__main__':
    unittest.main()
