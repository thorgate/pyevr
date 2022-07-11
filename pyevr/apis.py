from typing import Callable

from pyevr.openapi_client import api


class AllMixin:
    """Mixin for API endpoint classes to have an all() method for returning objects from all pages.

    :attr list_endpoint_attr: API endpoint's method for returning paged results
    :attr evr_page_param: Argument name that determines the page number
    """

    list_endpoint_attr = None
    evr_page_param = 'page'

    def get_list_endpoint(self) -> Callable:
        """Method for getting the callable API's endpoint that is responsible for returning paged results

        :return: Callable API's list endpoint method.
        """
        if self.list_endpoint_attr is None:
            raise ValueError("AllMixin requires `list_endpoint_attr` to be set")
        if not hasattr(self, self.list_endpoint_attr):
            raise ValueError("%s does not have the required list attribute `%s`" % (
                self.__class__, self.list_endpoint_attr,
            ))
        return getattr(self, self.list_endpoint_attr)

    def all(self, **kwargs):
        """Method for going through all the pages of a list view that is responsible for returning paged results"""
        if self.evr_page_param in kwargs:
            del kwargs[self.evr_page_param]
        endpoint = self.get_list_endpoint()

        current_page = 1
        current_count = 0
        total_count = None

        while total_count is None or current_count < total_count:
            kwargs[self.evr_page_param] = current_page
            page_response = endpoint(**kwargs)
            if total_count is None:
                total_count = page_response.total_count

            if page_response.page_result:
                for item in page_response.page_result:
                    current_count += 1
                    yield item
            else:
                # Possibly number of items changed while iterating, in this case assume no more items are coming
                return

            current_page += 1


class AssortmentsAPI(AllMixin, api.AssortmentsApi):
    list_endpoint_attr = 'assortments_list'


class CertificatesAPI(AllMixin, api.CertificatesApi):
    list_endpoint_attr = 'certificates_list'


class MeasurementsAPI(AllMixin, api.MeasurementsApi):
    list_endpoint_attr = 'measurements_get'


class MeasurementUnitsAPI(AllMixin, api.MeasurementUnitsApi):
    list_endpoint_attr = 'measurement_units_list'


class OrganizationsAPI(AllMixin, api.OrganizationsApi):
    list_endpoint_attr = 'organizations_list'


class PlaceOfDeliveriesAPI(AllMixin, api.PlaceOfDeliveriesApi):
    list_endpoint_attr = 'place_of_deliveries_list'


class WaybillsAPI(AllMixin, api.WaybillsApi):
    list_endpoint_attr = 'waybills_list'
