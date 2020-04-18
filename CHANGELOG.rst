=========
Changelog
=========

Not released yet
----------------

**Generic**

* Improve documentation

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
