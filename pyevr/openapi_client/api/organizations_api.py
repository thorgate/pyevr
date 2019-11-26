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


class OrganizationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def organizations_list(self, **kwargs):  # noqa: E501
        """Registreeritud asutuste pärimine  # noqa: E501

        Tagastab EVR-i aktiivsed asutused.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.organizations_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str code_starts_with: Filtreerib asutused, mille registrikood algab otsinguterminiga
        :param str name_contains: Filtreerib asutused, mille nimi sisaldab otsinguterminit
        :param int page: Tagastatav lehekülg
        :param str evr_language: Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks).
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedResultOfOrganization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.organizations_list_with_http_info(**kwargs)  # noqa: E501

    def organizations_list_with_http_info(self, **kwargs):  # noqa: E501
        """Registreeritud asutuste pärimine  # noqa: E501

        Tagastab EVR-i aktiivsed asutused.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.organizations_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str code_starts_with: Filtreerib asutused, mille registrikood algab otsinguterminiga
        :param str name_contains: Filtreerib asutused, mille nimi sisaldab otsinguterminit
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
        :return: tuple(PagedResultOfOrganization, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['code_starts_with', 'name_contains', 'page', 'evr_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method organizations_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] > 2147483647:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `organizations_list`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `organizations_list`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'code_starts_with' in local_var_params and local_var_params['code_starts_with'] is not None:  # noqa: E501
            query_params.append(('code_starts_with', local_var_params['code_starts_with']))  # noqa: E501
        if 'name_contains' in local_var_params and local_var_params['name_contains'] is not None:  # noqa: E501
            query_params.append(('name_contains', local_var_params['name_contains']))  # noqa: E501
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
            '/api/organizations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResultOfOrganization',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
