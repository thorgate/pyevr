=====
pyevr
=====


Python client for EVR (estonian e-waybill registry for forestry, https://evr.veoseleht.ee).


.. image:: https://img.shields.io/pypi/v/pyevr.svg
        :target: https://pypi.python.org/pypi/pyevr


Free software: MIT license

Usage
-----

.. code-block:: python

    from pyevr import EVRClient
    from pyevr.openapi_client.models import (
        ForestWaybill,
        SawnWaybill,
        StartForestWaybillRequest,
        WaybillType,
    )

    client = EVRClient(api_key)

    # List waybills. The API default is forest waybills only; pass
    # ``waybill_types`` to be explicit (or to include sawn timber waybills).
    for waybill in client.waybills.all(waybill_types=[WaybillType.FOREST]):
        print(waybill.number)

    # Start a forest waybill. ``type`` is required and must be passed explicitly.
    client.waybills.waybills_post(
        StartForestWaybillRequest(type="forest", ..., shipments=[...])
    )

    # Get by number can return either type; branch on the concrete class.
    waybill = client.waybills.waybills_get(number)
    if isinstance(waybill, ForestWaybill):
        shipments = waybill.shipments  # list of ``Shipment``
    elif isinstance(waybill, SawnWaybill):
        shipments = waybill.shipments  # list of ``SawnShipment``

Migrating from 1.x (forest-only integrations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The list endpoint defaults to forest waybills, so ``client.waybills.all(...)``
  keeps returning the same data without code changes. Pass
  ``waybill_types=[WaybillType.FOREST]`` to make this explicit.
* ``waybills_get(number)`` may return a ``SawnWaybill``; check
  ``isinstance(waybill, ForestWaybill)`` (or ``waybill.type == "forest"``)
  before reading ``waybill.shipments``.
* Replace ``StartWaybillRequest(...)`` with
  ``StartForestWaybillRequest(type="forest", ...)``; ``shipments`` is no
  longer on the base class.
* ``waybills_add_shipments`` accepts only forest ``Shipment`` objects; there is
  no sawn timber equivalent.

Credits
-------

This package is created with openapi generator - https://hub.docker.com/r/openapitools/openapi-generator-cli
