#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `EVRClient`."""

import unittest

from pyevr import EVRClient
from pyevr.openapi_client.models import ForestNotice, ForestNoticeAllOf


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
        self.assertEqual(client.openapi_client.configuration.host, 'https://evr.veoseleht.ee')

    def test_api_groups(self):
        from pyevr import apis
        self.assertEqual(type(self.client.assortments), apis.AssortmentsAPI)
        self.assertEqual(type(self.client.certificates), apis.CertificatesAPI)
        self.assertEqual(type(self.client.measurements), apis.MeasurementsAPI)
        self.assertEqual(type(self.client.measurement_units), apis.MeasurementUnitsAPI)
        self.assertEqual(type(self.client.organizations), apis.OrganizationsAPI)
        self.assertEqual(type(self.client.place_of_deliveries), apis.PlaceOfDeliveriesAPI)
        self.assertEqual(type(self.client.waybills), apis.WaybillsAPI)

        from pyevr.openapi_client import api
        self.assertTrue(isinstance(self.client.assortments, api.AssortmentsApi))
        self.assertTrue(isinstance(self.client.certificates, api.CertificatesApi))
        self.assertTrue(isinstance(self.client.measurements, api.MeasurementsApi))
        self.assertTrue(isinstance(self.client.measurement_units, api.MeasurementUnitsApi))
        self.assertTrue(isinstance(self.client.organizations, api.OrganizationsApi))
        self.assertTrue(isinstance(self.client.place_of_deliveries, api.PlaceOfDeliveriesApi))
        self.assertTrue(isinstance(self.client.waybills, api.WaybillsApi))


class TestExtendedApiClient(unittest.TestCase):
    api_key = 'asd123'
    host = 'https://api.evr.test'

    def setUp(self) -> None:
        super().setUp()
        self.client = EVRClient(self.api_key, self.host)

    def test_sanitize_for_serialization(self):
        notice = ForestNotice(cadaster='1', compartment='c', forest_allocation_number='f', number='n')
        obj_dict = self.client.openapi_client.sanitize_for_serialization(notice)
        self.assertDictEqual(obj_dict, {
            'type': 'ForestNotice',
            'cadaster': '1',
            'compartment': 'c',
            'forestAllocationNumber': 'f',
            'number': 'n',
        })

        notice_all_of = ForestNoticeAllOf(cadaster='12', compartment='c2', forest_allocation_number='f2', number='n2')
        obj_dict = self.client.openapi_client.sanitize_for_serialization(notice_all_of)
        self.assertDictEqual(obj_dict, {
            'type': 'ForestNotice',
            'cadaster': '12',
            'compartment': 'c2',
            'forestAllocationNumber': 'f2',
            'number': 'n2',
        })


if __name__ == '__main__':
    unittest.main()
