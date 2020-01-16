#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyevr.apis`."""

import unittest
from collections import namedtuple
from unittest.mock import Mock

from pyevr import EVRClient
from pyevr.apis import (
    AllMixin, AssortmentsAPI, CertificatesAPI, MeasurementsAPI, MeasurementUnitsAPI, OrganizationsAPI,
    PlaceOfDeliveriesAPI, WaybillsAPI,
)


class TestEVRClient(unittest.TestCase):
    api_key = 'asd123'
    host = 'https://api.evr.test'
    list_of_apis = [
        AssortmentsAPI,
        CertificatesAPI,
        MeasurementsAPI,
        MeasurementUnitsAPI,
        OrganizationsAPI,
        PlaceOfDeliveriesAPI,
        WaybillsAPI,
    ]

    def setUp(self) -> None:
        super().setUp()
        self.client = EVRClient(self.api_key, self.host)

    def run_api_test(self, api):
        self.assertTrue(isinstance(api, AllMixin))
        self.assertTrue(hasattr(api, api.list_endpoint_attr))
        self.assertIsNotNone(api.get_list_endpoint())

    def test_apis(self):
        for api_class in self.list_of_apis:
            self.run_api_test(api_class(self.client))

    def run_all_mixin_test(self, data):
        PagedResult = namedtuple('PagedResult', ['page', 'page_size', 'page_result', 'total_count'])

        def assortments_list(page):
            index_increment = (page - 1) * 3
            return PagedResult(
                page, 3, data[0 + index_increment:3 + index_increment], len(data),
            )

        api = AssortmentsAPI(self.client)
        api.assortments_list = Mock(side_effect=assortments_list)
        self.assertListEqual(api.all(), data)
        # Pass in a random page to make sure that it does not have any effect
        self.assertListEqual(api.all(page=99), data)

    def test_all_mixin(self):
        with self.assertRaises(ValueError):
            api = AssortmentsAPI(self.client)
            api.list_endpoint_attr = None
            api.get_list_endpoint()

        with self.assertRaises(ValueError):
            api = AssortmentsAPI(self.client)
            api.list_endpoint_attr = 'random_method'
            api.get_list_endpoint()

        self.run_all_mixin_test([])
        self.run_all_mixin_test([1])
        self.run_all_mixin_test([1, 2, 3])
        self.run_all_mixin_test([1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()
