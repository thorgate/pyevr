=========
Changelog
=========

2.0.0.dev1
----------

**Breaking**

* Update EVR schema to 2.0.0 (fetched 2026-09-07). EVR now has two waybill
  types: forest (``mets``) and sawn timber (``saematerjal``), see the new
  ``WaybillType`` enum (``FOREST``/``SAWN``).
* ``Waybill`` and ``StartWaybillRequest`` are now abstract base models with a
  ``type`` discriminator. ``shipments`` no longer exists on them; it lives on
  the concrete subclasses ``ForestWaybill``/``SawnWaybill`` and
  ``StartForestWaybillRequest``/``StartSawnWayBillRequest`` (upstream spelling).
* Replace ``StartWaybillRequest(..., shipments=[...])`` with
  ``StartForestWaybillRequest(..., type="forest", shipments=[...])``. ``type``
  is required and is not defaulted by the generated subclasses.
* ``Waybill.from_dict``/``from_json`` (and thus ``EVRClient.deserialize_data``
  and all API responses) return ``ForestWaybill`` or ``SawnWaybill``. Check
  ``isinstance(waybill, ForestWaybill)`` (or ``waybill.type == "forest"``)
  before reading ``waybill.shipments``.
* ``waybills_get(number)`` returns a ``SawnWaybill`` if the number belongs to a
  sawn timber waybill.

**Bugs**

* ``EVRClient.deserialize_data`` can again rehydrate the output of
  ``EVRClient.sanitize_for_serialization`` (snake_case attribute names,
  nested models included). Since 1.0.0 the generated ``from_dict`` only read
  camelCase aliases, so nested models such as ``Address`` failed validation.
  API-shaped (camelCase) data is still accepted.
* Waybill data serialized before EVR 2.0.0, which lacks the ``type``
  discriminator, deserializes as ``ForestWaybill`` (and
  ``StartForestWaybillRequest``), see ``pyevr.client.LEGACY_DISCRIMINATOR_DEFAULTS``.

**Generic**

* ``waybills_list`` / ``client.waybills.all`` gained ``waybill_types``. The
  upstream default is forest only, so existing list consumers keep receiving
  only forest waybills. Pass ``waybill_types=[WaybillType.FOREST]`` to be
  explicit.
* Forest schemas (``Shipment``, ``ShipmentItem``, ``HoldingBase`` and
  subtypes) are unchanged; ``ForestWaybill`` is the old ``Waybill`` plus
  ``type``.
* Add sawn timber models (26 new schemas): ``SawnShipment`` with ``SawnWood``
  (species, dimensions, grade, treatment, profile, packing, tolerances,
  certificate statement, article ids) and ``SawnPack``/``SawnPackLength``.
* ``waybills_add_shipments`` still accepts only forest ``Shipment`` objects.
* ``Address`` gained an optional ``zip`` field.
* Track the fetched upstream schema
  ``pyevr/openapi/openapi-generator-compatible.json`` in git so schema updates
  are diffable; ``make openapi-apply-patch`` now writes the patched file
  separately instead of modifying the upstream file in place.
* Regenerate the schema-fixes patch for 2.0.0 (same minLength relaxations,
  plus required strings in the new ``Attachment``, ``CertificateStatement``
  and ``Packing`` schemas).
* Rename the ``_without_preload_content`` variants of
  ``waybills_get``/``waybills_get2`` consistently with the rest.

1.0.1.dev4

**Breaking**

* TLS peer verification now uses the ``certifi`` CA bundle by default instead
  of the system CA store. This makes verification independent of the age of
  the system store (e.g. old Docker base images missing newer roots such as
  Sectigo R46, used by evr.veoseleht.ee since 2026-08) and matches the
  behavior of requests/httpx. Set ``PYEVR_CERTIFI_ENABLED`` to a falsy value
  (``0``/``false``/``no``/``off``) to opt back into the system CA store —
  needed if your system store carries extra CAs (corporate TLS proxy,
  private instance CA).

**Generic**

* Add ``certifi`` as a dependency.
* Update EVR schema to 1.40.1 (fetched 2026-08-26)

1.0.1.dev3

**Generic**

* Update EVR schema to 1.4.0.1

1.0.1.dev2
----------

**Generic**

* Update EVR schema to 1.35 (from EVR test server, revision 2025-09-09)

1.0.0
----------

**BREAKING**

* Drop support for python 3.8

**Generic**

* Update to use newer openapi generator (pydantic 2)
* Improve `sanitize_for_serialization` for caching the data

**Updates**

Use EVR schema 1.30

* Support for EUDR fields
* Other misc changes


0.7.0
----------

**Generic**

* Update openapi generator to latest version
* Move to poetry

0.6.0.dev4
----------

**Generic**

* Change `all` method to be a generator instead of returning a list, to
  allow data consumer to start consumption faster and avoid loading the
  unnecessary pages if error happens early on
* Add `deserialize_data` method that allows to rehydrate the model from
  result of `sanitize_for_serialization` (allowing to store models as
  json and similar use-cases)

**Updates**

Use EVR schema 1.14

* Support `WithoutForestNotice` holding base

* Support `page_size` parameter for list endpoints

* Support `last_modified_after` and `last_modified_before` for waybill list

* Support `waybill_latest_measurements` in waybill model

* Other misc changes


0.5.2 (2022-04-06)
------------------

**Generic**

* Improve documentation

**Compatibility**

* Update to newest EVR schema
* Workaround: Patch minLength in schema to be consistent with data returned by API
* Remove workaround for assortmnet schema

0.5.0 (2020-04-18)
------------------

**Generic**

* Remove Python 3.5 support (#56)
* Update client code to match EVR API v1.1.1 (#56)
* Update openapi-generator-cli to v4.3.0 (#56)
* Update Python dependencies (#43 #52 #54 #55 #56)

0.4.0 (2020-02-02)
------------------

**Generic**

* Update Python requirements (#33 #36 #40 #41)
* Update openapi-generator-cli to v4.2.3 (#42)

**Bugs**

* Add type to holding base children when sending a waybill to EVR (#42)
* Fix `Assortment.product_group` usage (#42)

0.3.0 (2020-01-16)
------------------

**Enhancements**

* Add a method for returning all of the results for EVR API's list endpoints
* Update WaybillsApi to use waybills_list instead of waybills_get and waybills_get instead of waybills_get2

0.2.2 (2019-12-04)
------------------

**Generic**

* Remove workarounds that where created because of invalid API schema and wrong data in test server
* Update openapi-generator-cli to v4.2.2

**Bugs**

* Fix issues with all configuration instances having same values as the one that was created first

0.2.1 (2019-11-26)
------------------

**Generic**

* Update openapi-generator-cli to v4.2.1
* Update Python requirements and fix them for the CI

**Bugs**

* Fix issues with maximum values in API schema (until it gets fixed in schema)
* Workaround for issues with invalid data in test server (until if gets fixed in test server)


0.2.0 (2019-11-23)
------------------

**Generic**

* Implement the initial client using auto-generated code by openapi-generator-cli


0.1.0 (2019-11-09)
------------------

* First release on PyPI.
