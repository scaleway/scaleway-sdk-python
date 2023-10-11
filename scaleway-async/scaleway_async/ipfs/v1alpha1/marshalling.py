# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    PinCIDMeta,
    PinCID,
    PinInfo,
    Pin,
    Volume,
    ListPinsResponse,
    ListVolumesResponse,
    ReplacePinResponse,
    PinOptions,
    CreatePinByCIDRequest,
    CreatePinByURLRequest,
    CreateVolumeRequest,
    ReplacePinRequest,
    UpdateVolumeRequest,
)


def unmarshal_PinCIDMeta(data: Any) -> PinCIDMeta:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PinCIDMeta' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    return PinCIDMeta(**args)


def unmarshal_PinCID(data: Any) -> PinCID:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PinCID' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("meta", None)
    args["meta"] = unmarshal_PinCIDMeta(field)

    field = data.get("origins", None)
    args["origins"] = field

    field = data.get("cid", None)
    args["cid"] = field

    field = data.get("name", None)
    args["name"] = field

    return PinCID(**args)


def unmarshal_PinInfo(data: Any) -> PinInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PinInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status_details", None)
    args["status_details"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("url", None)
    args["url"] = field

    field = data.get("size", None)
    args["size"] = field

    field = data.get("progress", None)
    args["progress"] = field

    return PinInfo(**args)


def unmarshal_Pin(data: Any) -> Pin:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Pin' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("info", None)
    args["info"] = unmarshal_PinInfo(field)

    field = data.get("delegates", None)
    args["delegates"] = field

    field = data.get("cid", None)
    args["cid"] = unmarshal_PinCID(field)

    field = data.get("status", None)
    args["status"] = field

    field = data.get("pin_id", None)
    args["pin_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Pin(**args)


def unmarshal_Volume(data: Any) -> Volume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Volume' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    args["name"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("count_pin", None)
    args["count_pin"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("size", None)
    args["size"] = field

    return Volume(**args)


def unmarshal_ListPinsResponse(data: Any) -> ListPinsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPinsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pins", None)
    args["pins"] = [unmarshal_Pin(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListPinsResponse(**args)


def unmarshal_ListVolumesResponse(data: Any) -> ListVolumesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVolumesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("volumes", None)
    args["volumes"] = (
        [unmarshal_Volume(v) for v in field] if field is not None else None
    )

    return ListVolumesResponse(**args)


def unmarshal_ReplacePinResponse(data: Any) -> ReplacePinResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ReplacePinResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pin", None)
    args["pin"] = unmarshal_Pin(field)

    return ReplacePinResponse(**args)


def marshal_PinOptions(
    request: PinOptions,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.replication_count is not None:
        output["replication_count"] = request.replication_count

    if request.required_zones is not None:
        output["required_zones"] = request.required_zones

    return output


def marshal_CreatePinByCIDRequest(
    request: CreatePinByCIDRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.pin_options is not None:
        output["pin_options"] = (marshal_PinOptions(request.pin_options, defaults),)

    if request.cid is not None:
        output["cid"] = request.cid

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id

    if request.origins is not None:
        output["origins"] = request.origins

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_CreatePinByURLRequest(
    request: CreatePinByURLRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.pin_options is not None:
        output["pin_options"] = (marshal_PinOptions(request.pin_options, defaults),)

    if request.url is not None:
        output["url"] = request.url

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_CreateVolumeRequest(
    request: CreateVolumeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_ReplacePinRequest(
    request: ReplacePinRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.pin_options is not None:
        output["pin_options"] = (marshal_PinOptions(request.pin_options, defaults),)

    if request.cid is not None:
        output["cid"] = request.cid

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id

    if request.name is not None:
        output["name"] = request.name

    if request.origins is not None:
        output["origins"] = request.origins

    return output


def marshal_UpdateVolumeRequest(
    request: UpdateVolumeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    return output
