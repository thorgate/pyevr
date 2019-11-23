# coding: utf-8

"""
    EVR API

    OpenAPI Generator'i jaoks kohandatud EVR API kirjeldus. Kasuta seda juhul, kui spetsifikatsioonile vastava EVR API kirjeldusega ei õnnestu klienti genereerida.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pyevr.openapi_client.api_client import ApiClient
from pyevr.openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class MeasurementsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def measurements_get(self, number, **kwargs):  # noqa: E501
        """Veoselehe mõõtmisandmete pärimine  # noqa: E501

        Tagastab veoselehega seotud mõõtmisandmed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.measurements_get(number, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str number: Veoselehe number (required)
        :param int page: Tagastatav lehekülg
        :param str evr_language: Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks).
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedResultOfMeasurementAct
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.measurements_get_with_http_info(number, **kwargs)  # noqa: E501

    def measurements_get_with_http_info(self, number, **kwargs):  # noqa: E501
        """Veoselehe mõõtmisandmete pärimine  # noqa: E501

        Tagastab veoselehega seotud mõõtmisandmed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.measurements_get_with_http_info(number, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str number: Veoselehe number (required)
        :param int page: Tagastatav lehekülg
        :param str evr_language: Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks).
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PagedResultOfMeasurementAct, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['number', 'page', 'evr_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method measurements_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'number' is set
        if self.api_client.client_side_validation and ('number' not in local_var_params or  # noqa: E501
                                                        local_var_params['number'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `number` when calling `measurements_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] > -9223372036854771616:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `measurements_get`, must be a value less than or equal to `-9223372036854771616`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `measurements_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'number' in local_var_params:
            path_params['number'] = local_var_params['number']  # noqa: E501

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = {}
        if 'evr_language' in local_var_params:
            header_params['EVR-LANGUAGE'] = local_var_params['evr_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['SecretApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/waybills/{number}/measurements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResultOfMeasurementAct',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def measurements_post(self, number, add_measurement_act_request, **kwargs):  # noqa: E501
        """Veoselehele mõõtmisandmete lisamine  # noqa: E501

        Lisab veoselehele mõõtmisandmed. Mõõtmisandmeid saab lisada \"koorem maas\" staatuses veoselehele sellele märgitud veose saaja või tema volitatud mõõtja. Mõõtmistulemusi on võimalik lisada koormapakkidena või lihtsalt sortimentide kogustena.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.measurements_post(number, add_measurement_act_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str number: Veoselehe number (required)
        :param AddMeasurementActRequest add_measurement_act_request: Mõõtmisandmed (required)
        :param str evr_language: Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks).
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.measurements_post_with_http_info(number, add_measurement_act_request, **kwargs)  # noqa: E501

    def measurements_post_with_http_info(self, number, add_measurement_act_request, **kwargs):  # noqa: E501
        """Veoselehele mõõtmisandmete lisamine  # noqa: E501

        Lisab veoselehele mõõtmisandmed. Mõõtmisandmeid saab lisada \"koorem maas\" staatuses veoselehele sellele märgitud veose saaja või tema volitatud mõõtja. Mõõtmistulemusi on võimalik lisada koormapakkidena või lihtsalt sortimentide kogustena.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.measurements_post_with_http_info(number, add_measurement_act_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str number: Veoselehe number (required)
        :param AddMeasurementActRequest add_measurement_act_request: Mõõtmisandmed (required)
        :param str evr_language: Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks).
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['number', 'add_measurement_act_request', 'evr_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method measurements_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'number' is set
        if self.api_client.client_side_validation and ('number' not in local_var_params or  # noqa: E501
                                                        local_var_params['number'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `number` when calling `measurements_post`")  # noqa: E501
        # verify the required parameter 'add_measurement_act_request' is set
        if self.api_client.client_side_validation and ('add_measurement_act_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['add_measurement_act_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `add_measurement_act_request` when calling `measurements_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'number' in local_var_params:
            path_params['number'] = local_var_params['number']  # noqa: E501

        query_params = []

        header_params = {}
        if 'evr_language' in local_var_params:
            header_params['EVR-LANGUAGE'] = local_var_params['evr_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'add_measurement_act_request' in local_var_params:
            body_params = local_var_params['add_measurement_act_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['SecretApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/waybills/{number}/measurements', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
