#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `EVRClient`."""

import os
import unittest
from unittest import mock

import certifi

from pydantic import ValidationError

from pyevr import EVRClient
from pyevr.openapi_client.models import (
    ForestNotice, ForestWaybill, HoldingBase, Receiver, SawnShipment, SawnWaybill, Shipment,
    StartForestWaybillRequest, StartSawnWayBillRequest, StartWaybillRequest, Waybill,
)


def waybill_data(waybill_type):
    """Minimal valid waybill payload (camelCase, as returned by the API) for the given ``type``."""
    addr = {'countryCode': 'EST', 'county': 'c', 'city': 'c', 'street': 's'}
    base = dict(
        owner={'name': 'O', 'code': '1', 'address': addr},
        transport={
            'driverName': 'D',
            'driverIdCode': '1',
            'vanRegistrationNumber': 'X',
            'transporter': {'name': 'T', 'code': '3', 'address': addr},
        },
        receiver={'name': 'R', 'code': '2', 'address': addr},
        placeOfDelivery={'name': 'P', 'address': addr},
        departureTime='2026-01-01T00:00:00Z',
        submissionTime='2026-01-01T00:00:00Z',
    )
    shipments = {
        'forest': [{
            'holdingBase': {'type': 'ForestNotice', 'cadaster': 'c', 'noticeNumber': 'n'},
            'source': {'name': 's', 'address': addr},
            'items': [{'unitCode': 'm3', 'amount': 1, 'assortment': {'code': 'a', 'name': 'n', 'productGroup': 'g'}}],
        }],
        'sawn': [{
            'sawnWood': {'species': ['pine'], 'thickness': 50, 'width': 100},
            'packs': [{'volume': 1.5}],
        }],
    }
    return dict(base, type=waybill_type, shipments=shipments[waybill_type])


class TestEVRClient(unittest.TestCase):
    api_key = 'asd123'
    host = 'https://api.evr.test'

    def setUp(self) -> None:
        super().setUp()
        self.client = EVRClient(self.api_key, self.host)

    def test_initial_api_key(self):
        self.assertRaises(TypeError, EVRClient)
        self.assertDictEqual(self.client.openapi_client.configuration.api_key, {'SecretApiKey': self.api_key})

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
        notice = ForestNotice(
            cadaster='1',
            compartment='c',
            forest_allocation_number='f',
            number='n',
            type="ForestNotice",
        )
        obj_dict = self.client.openapi_client.sanitize_for_serialization(notice)
        self.assertDictEqual(obj_dict, {
            'type': 'ForestNotice',
            'cadaster': '1',
            'compartment': 'c',
            'forestAllocationNumber': 'f',
            'number': 'n',
        })

    def test_deserialize_data(self):
        # Given serialized forest notice data
        forest_notice_data = {
            'type': 'ForestNotice',
            'cadaster': '1',
            'compartment': 'c',
            'forestAllocationNumber': 'f',
            'number': 'n',
        }

        # When it is deserialized
        forest_notice = self.client.deserialize_data(forest_notice_data, ForestNotice)

        # Then result is instance of correct model
        assert isinstance(forest_notice, ForestNotice)

        # And has correct data
        assert forest_notice.cadaster == "1"

    def test_deserialize_data_error_reporting(self):
        # Given invalid serialized receiver data
        receiver_data = {
            'name': 'Metsavaht OÜ',
            'code': '42',
            'address': {
                'countryCode': 'EEEE',
                'county': 'Metsamaa',
                'city': 'Metsaküla',
                'street': 'Metsa',
            },
            'contactPerson': {
                'name': 'Jaan Jänese',
                'phone': '',
                'email': 'jaan@metsavaht.example.com',
            },
        }
        with self.assertRaises(ValueError) as raises_context_manager:
            # When it is deserialized
            self.client.deserialize_data(receiver_data, Receiver)

        # Then is ValueError pointing out at the exact field
        assert "Address" in str(raises_context_manager.exception)
        assert "countryCode" in str(raises_context_manager.exception)


class TestWaybillTypes(unittest.TestCase):
    api_key = 'asd123'
    host = 'https://api.evr.test'

    def setUp(self) -> None:
        super().setUp()
        self.client = EVRClient(self.api_key, self.host)

    def test_deserialize_forest_waybill(self):
        waybill = self.client.deserialize_data(waybill_data('forest'), Waybill)
        self.assertIsInstance(waybill, ForestWaybill)
        self.assertEqual(waybill.type, 'forest')
        self.assertEqual(len(waybill.shipments), 1)
        self.assertIsInstance(waybill.shipments[0], Shipment)

    def test_deserialize_sawn_waybill(self):
        waybill = self.client.deserialize_data(waybill_data('sawn'), Waybill)
        self.assertIsInstance(waybill, SawnWaybill)
        self.assertEqual(waybill.type, 'sawn')
        self.assertEqual(len(waybill.shipments), 1)
        self.assertIsInstance(waybill.shipments[0], SawnShipment)

    def test_sanitize_forest_waybill(self):
        waybill = self.client.deserialize_data(waybill_data('forest'), Waybill)
        data = self.client.sanitize_for_serialization(waybill)
        self.assertEqual(data['type'], 'forest')
        self.assertEqual(len(data['shipments']), 1)
        # EVRClient.sanitize_for_serialization serializes model.__dict__, i.e. snake_case field names
        self.assertEqual(data['shipments'][0]['holding_base']['type'], 'ForestNotice')

    def test_sanitize_sawn_waybill(self):
        waybill = self.client.deserialize_data(waybill_data('sawn'), Waybill)
        data = self.client.sanitize_for_serialization(waybill)
        self.assertEqual(data['type'], 'sawn')
        self.assertEqual(len(data['shipments']), 1)
        self.assertEqual(data['shipments'][0]['sawn_wood']['species'], ['pine'])
        self.assertEqual(data['shipments'][0]['packs'][0]['volume'], 1.5)

    def test_start_waybill_requests_require_type(self):
        for request_class, waybill_type in (
            (StartForestWaybillRequest, 'forest'),
            (StartSawnWayBillRequest, 'sawn'),
        ):
            data = waybill_data(waybill_type)
            del data['type']
            with self.assertRaises(ValidationError):
                request_class.model_validate(data)

    def test_start_forest_waybill_request_to_dict(self):
        request = StartForestWaybillRequest.model_validate(waybill_data('forest'))
        self.assertIsInstance(request.shipments[0], Shipment)
        data = request.to_dict()
        self.assertEqual(data['type'], 'forest')
        self.assertEqual(data['shipments'][0]['holdingBase']['type'], 'ForestNotice')

    def test_start_sawn_waybill_request_to_dict(self):
        request = StartSawnWayBillRequest.model_validate(waybill_data('sawn'))
        self.assertIsInstance(request.shipments[0], SawnShipment)
        data = request.to_dict()
        self.assertEqual(data['type'], 'sawn')
        self.assertEqual(data['shipments'][0]['sawnWood']['species'], ['pine'])


class TestDeserializeNormalization(unittest.TestCase):
    """``deserialize_data`` accepts snake_case (``sanitize_for_serialization`` output) and legacy data without ``type``."""

    api_key = 'asd123'
    host = 'https://api.evr.test'

    def setUp(self) -> None:
        super().setUp()
        self.client = EVRClient(self.api_key, self.host)

    def _snake_case_waybill_data(self, waybill_type):
        waybill = self.client.deserialize_data(waybill_data(waybill_type), Waybill)
        return self.client.sanitize_for_serialization(waybill)

    def test_round_trip_equality(self):
        for waybill_type in ('forest', 'sawn'):
            with self.subTest(waybill_type=waybill_type):
                waybill = self.client.deserialize_data(waybill_data(waybill_type), Waybill)
                data = self.client.sanitize_for_serialization(waybill)
                self.assertEqual(self.client.deserialize_data(data, Waybill), waybill)

    def test_camel_case_data_deserializes_unchanged(self):
        data = waybill_data('sawn')
        original = dict(data)
        waybill = self.client.deserialize_data(data, Waybill)
        self.assertIsInstance(waybill, SawnWaybill)
        self.assertEqual(waybill.shipments[0].sawn_wood.species, ['pine'])
        self.assertEqual(data, original)

    def test_legacy_camel_case_without_type_is_forest(self):
        data = waybill_data('forest')
        del data['type']
        waybill = self.client.deserialize_data(data, Waybill)
        self.assertIsInstance(waybill, ForestWaybill)
        self.assertEqual(waybill.type, 'forest')
        self.assertIsInstance(waybill.shipments[0].holding_base, ForestNotice)

    def test_legacy_camel_case_without_type_to_forest_waybill_directly(self):
        data = waybill_data('forest')
        del data['type']
        waybill = self.client.deserialize_data(data, ForestWaybill)
        self.assertIsInstance(waybill, ForestWaybill)
        self.assertEqual(waybill.type, 'forest')

    def test_legacy_snake_case_without_type_is_forest(self):
        data = self._snake_case_waybill_data('forest')
        del data['type']
        waybill = self.client.deserialize_data(data, Waybill)
        self.assertIsInstance(waybill, ForestWaybill)
        self.assertEqual(waybill.type, 'forest')
        self.assertIsInstance(waybill.shipments[0], Shipment)
        self.assertIsInstance(waybill.shipments[0].holding_base, ForestNotice)
        self.assertEqual(waybill.shipments[0].holding_base.cadaster, 'c')

    def test_legacy_start_waybill_request_without_type_is_forest(self):
        for data in (waybill_data('forest'), self._snake_case_waybill_data('forest')):
            del data['type']
            with self.subTest(keys=sorted(data)[:3]):
                request = self.client.deserialize_data(data, StartWaybillRequest)
                self.assertIsInstance(request, StartForestWaybillRequest)
                self.assertEqual(request.type, 'forest')
                self.assertIsInstance(request.shipments[0], Shipment)

    def test_sawn_data_without_type_raises(self):
        for data in (waybill_data('sawn'), self._snake_case_waybill_data('sawn')):
            del data['type']
            with self.subTest(keys=sorted(data)[:3]), self.assertRaises(ValidationError):
                self.client.deserialize_data(data, Waybill)

    def test_nested_discriminator_snake_case(self):
        notice = self.client.deserialize_data(
            {'type': 'ForestNotice', 'cadaster': 'c', 'forest_allocation_number': 'f'}, HoldingBase
        )
        self.assertIsInstance(notice, ForestNotice)
        self.assertEqual(notice.forest_allocation_number, 'f')


class TestCertifiEnv(unittest.TestCase):
    api_key = 'asd123'

    def _make_client(self, env_value):
        env = {'PYEVR_CERTIFI_ENABLED': env_value} if env_value is not None else {}
        with mock.patch.dict(os.environ, env, clear=False):
            if env_value is None:
                os.environ.pop('PYEVR_CERTIFI_ENABLED', None)
            return EVRClient(self.api_key)

    def test_default_uses_certifi(self):
        client = self._make_client(None)
        self.assertEqual(
            client.openapi_client.configuration.ssl_ca_cert, certifi.where()
        )

    def test_falsy_values_opt_out_to_system_store(self):
        for value in ('', '0', 'false', 'no', 'off', 'nonsense'):
            client = self._make_client(value)
            self.assertIsNone(
                client.openapi_client.configuration.ssl_ca_cert,
                'expected system store for PYEVR_CERTIFI_ENABLED=%r' % value,
            )

    def test_truthy_values_use_certifi(self):
        for value in ('1', 'true', 'True', 'YES', 'on', ' 1 '):
            client = self._make_client(value)
            self.assertEqual(
                client.openapi_client.configuration.ssl_ca_cert,
                certifi.where(),
                'expected certifi bundle for PYEVR_CERTIFI_ENABLED=%r' % value,
            )


if __name__ == '__main__':
    unittest.main()
