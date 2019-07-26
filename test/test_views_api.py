# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import influxdb2
from influxdb2.api.views_api import ViewsApi  # noqa: E501
from influxdb2.rest import ApiException


class TestViewsApi(unittest.TestCase):
    """ViewsApi unit test stubs"""

    def setUp(self):
        self.api = influxdb2.api.views_api.ViewsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_dashboards_id_cells_id_view(self):
        """Test case for get_dashboards_id_cells_id_view

        Retrieve the view for a cell in a dashboard  # noqa: E501
        """
        pass

    def test_patch_dashboards_id_cells_id_view(self):
        """Test case for patch_dashboards_id_cells_id_view

        Update the view for a cell  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()