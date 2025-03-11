# WaybillNoteCreator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nimi | 
**code** | **str** | Isiku- või registrikood | 

## Example

```python
from openapi_client.models.waybill_note_creator import WaybillNoteCreator

# TODO update the JSON string below
json = "{}"
# create an instance of WaybillNoteCreator from a JSON string
waybill_note_creator_instance = WaybillNoteCreator.from_json(json)
# print the JSON string representation of the object
print(WaybillNoteCreator.to_json())

# convert the object into a dict
waybill_note_creator_dict = waybill_note_creator_instance.to_dict()
# create an instance of WaybillNoteCreator from a dict
waybill_note_creator_from_dict = WaybillNoteCreator.from_dict(waybill_note_creator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


