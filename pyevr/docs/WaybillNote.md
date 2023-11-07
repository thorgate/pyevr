# WaybillNote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | [**WaybillNoteCreator**](WaybillNoteCreator.md) |  | [optional] 
**creation_time** | **datetime** | Loomise aeg | [optional] 
**message** | **str** | Sõnum | [optional] 

## Example

```python
from openapi_client.models.waybill_note import WaybillNote

# TODO update the JSON string below
json = "{}"
# create an instance of WaybillNote from a JSON string
waybill_note_instance = WaybillNote.from_json(json)
# print the JSON string representation of the object
print WaybillNote.to_json()

# convert the object into a dict
waybill_note_dict = waybill_note_instance.to_dict()
# create an instance of WaybillNote from a dict
waybill_note_form_dict = waybill_note.from_dict(waybill_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


