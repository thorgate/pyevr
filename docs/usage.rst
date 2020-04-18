=====
Usage
=====

To use pyevr in a project::

    from pyevr import EVRClient

    evr = EVRClient("YOUR-API-KEY", "https://evr-test.azurewebsites.net/")

    # Fetch all assortments
    assortments = evr.assortments.all()

    # Fetch all certificates
    certificates = evr.certificates.all()

    # Fetch all measurements for a waybill
    measurements = evr.measurements.all(number="WB123")

    # Fetch all measurement units
    measurement_units = evr.measurement_units.all()

    # Fetch all organizations
    organizations = evr.organizations.all()

    # Fetch all place of deliveries
    place_of_deliveries = evr.place_of_deliveries.all()

    # Fetch waybills in date range
    waybills = evr.waybills.all(
        created_after=datetime(2020, 4, 1),
        created_before=datetime(2020, 5, 1),
    )


Details about using the endpoints can be found from `EVR API docs`_.

.. _`EVR API docs`: https://evr-test.azurewebsites.net/doc-en.html
