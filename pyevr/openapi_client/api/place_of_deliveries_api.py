# coding: utf-8

"""
    EVR API

    OpenAPI Generator'i jaoks kohandatud EVR API kirjeldus. Kasuta seda juhul, kui spetsifikatsioonile vastava EVR API kirjeldusega ei õnnestu klienti genereerida.  # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pyevr.openapi_client.api_client import ApiClient
from pyevr.openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PlaceOfDeliveriesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def place_of_deliveries_add_or_update(self, code, put_place_of_delivery_request, **kwargs):  # noqa: E501
        """Tarnekoha lisamine ja muutmine  # noqa: E501

        Lisab uue tarnekoha. Kui antud koodiga tarnekoht juba eksisteerib, siis muudab olemasolevat tarnekohta. Loomisel märgitakse päringu tegija tarnekoha omanikuks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_of_deliveries_add_or_update(code, put_place_of_delivery_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str code: Kood (required)
        :param PutPlaceOfDeliveryRequest put_place_of_delivery_request: (required)
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
        return self.place_of_deliveries_add_or_update_with_http_info(code, put_place_of_delivery_request, **kwargs)  # noqa: E501

    def place_of_deliveries_add_or_update_with_http_info(self, code, put_place_of_delivery_request, **kwargs):  # noqa: E501
        """Tarnekoha lisamine ja muutmine  # noqa: E501

        Lisab uue tarnekoha. Kui antud koodiga tarnekoht juba eksisteerib, siis muudab olemasolevat tarnekohta. Loomisel märgitakse päringu tegija tarnekoha omanikuks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_of_deliveries_add_or_update_with_http_info(code, put_place_of_delivery_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str code: Kood (required)
        :param PutPlaceOfDeliveryRequest put_place_of_delivery_request: (required)
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

        all_params = [
            'code',
            'put_place_of_delivery_request',
            'evr_language'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method place_of_deliveries_add_or_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if self.api_client.client_side_validation and ('code' not in local_var_params or  # noqa: E501
                                                        local_var_params['code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `code` when calling `place_of_deliveries_add_or_update`")  # noqa: E501
        # verify the required parameter 'put_place_of_delivery_request' is set
        if self.api_client.client_side_validation and ('put_place_of_delivery_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['put_place_of_delivery_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `put_place_of_delivery_request` when calling `place_of_deliveries_add_or_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []

        header_params = {}
        if 'evr_language' in local_var_params:
            header_params['EVR-LANGUAGE'] = local_var_params['evr_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'put_place_of_delivery_request' in local_var_params:
            body_params = local_var_params['put_place_of_delivery_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['SecretApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/placeofdeliveries/{code}', 'PUT',
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

    def place_of_deliveries_get(self, code, **kwargs):  # noqa: E501
        """Tarnekoha pärimine  # noqa: E501

        Tagastab koodile vastava tarnekoha. Pärida saab ainult enda asutusele kuuluvat tarnekohta.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_of_deliveries_get(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str code: Päritava tarnekoha kood (required)
        :param str evr_language: Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks).
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PlaceOfDelivery
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.place_of_deliveries_get_with_http_info(code, **kwargs)  # noqa: E501

    def place_of_deliveries_get_with_http_info(self, code, **kwargs):  # noqa: E501
        """Tarnekoha pärimine  # noqa: E501

        Tagastab koodile vastava tarnekoha. Pärida saab ainult enda asutusele kuuluvat tarnekohta.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_of_deliveries_get_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str code: Päritava tarnekoha kood (required)
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
        :return: tuple(PlaceOfDelivery, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'code',
            'evr_language'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method place_of_deliveries_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if self.api_client.client_side_validation and ('code' not in local_var_params or  # noqa: E501
                                                        local_var_params['code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `code` when calling `place_of_deliveries_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []

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
            '/api/placeofdeliveries/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlaceOfDelivery',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def place_of_deliveries_list(self, **kwargs):  # noqa: E501
        """Tarnekohtade pärimine  # noqa: E501

        Tagastab filtritele vastavad aktiivsed avalikud tarnekohad ja kõik ettevõttega seotud tarnekohad.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_of_deliveries_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str name_contains: Filtreerib tarnekohad, mille nimi sisaldab otsinguterminit
        :param str code_starts_with: Filtreerib tarnekohad, mille kood algab otsinguterminiga
        :param str register_code: Filtreerib ettevõtte tarnekohad, mille registrikood vastab otsinguterminile
        :param str address: Vabatekstiline aadressi otsing.  Toetatud on järgmine süntaks:  * ilma jutumärkideta tekst: sõnade vahel rakendatakse loogiline JA  * jutumärkides tekst: otsitakse jutumärkides olevat lauset  * OR: loogiline VÕI operaator sõnade vahel  * -: loogiline EITUS
        :param int page: Tagastatav lehekülg
        :param str evr_language: Defineerib keele tagastatavatele veateadetele (toetatud on väärtused \"et\" eesti keele ning \"en\" inglise keele jaoks).
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedResultOfPlaceOfDelivery
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.place_of_deliveries_list_with_http_info(**kwargs)  # noqa: E501

    def place_of_deliveries_list_with_http_info(self, **kwargs):  # noqa: E501
        """Tarnekohtade pärimine  # noqa: E501

        Tagastab filtritele vastavad aktiivsed avalikud tarnekohad ja kõik ettevõttega seotud tarnekohad.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_of_deliveries_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str name_contains: Filtreerib tarnekohad, mille nimi sisaldab otsinguterminit
        :param str code_starts_with: Filtreerib tarnekohad, mille kood algab otsinguterminiga
        :param str register_code: Filtreerib ettevõtte tarnekohad, mille registrikood vastab otsinguterminile
        :param str address: Vabatekstiline aadressi otsing.  Toetatud on järgmine süntaks:  * ilma jutumärkideta tekst: sõnade vahel rakendatakse loogiline JA  * jutumärkides tekst: otsitakse jutumärkides olevat lauset  * OR: loogiline VÕI operaator sõnade vahel  * -: loogiline EITUS
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
        :return: tuple(PagedResultOfPlaceOfDelivery, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'name_contains',
            'code_starts_with',
            'register_code',
            'address',
            'page',
            'evr_language'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method place_of_deliveries_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] > 2147483647:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `place_of_deliveries_list`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `place_of_deliveries_list`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name_contains' in local_var_params and local_var_params['name_contains'] is not None:  # noqa: E501
            query_params.append(('name_contains', local_var_params['name_contains']))  # noqa: E501
        if 'code_starts_with' in local_var_params and local_var_params['code_starts_with'] is not None:  # noqa: E501
            query_params.append(('code_starts_with', local_var_params['code_starts_with']))  # noqa: E501
        if 'register_code' in local_var_params and local_var_params['register_code'] is not None:  # noqa: E501
            query_params.append(('register_code', local_var_params['register_code']))  # noqa: E501
        if 'address' in local_var_params and local_var_params['address'] is not None:  # noqa: E501
            query_params.append(('address', local_var_params['address']))  # noqa: E501
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
            '/api/placeofdeliveries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResultOfPlaceOfDelivery',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
