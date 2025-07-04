# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_Money,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    Reference,
    SnapshotParentVolume,
    Snapshot,
    VolumeSpecifications,
    Volume,
    ListSnapshotsResponse,
    VolumeType,
    ListVolumeTypesResponse,
    ListVolumesResponse,
    CreateSnapshotRequest,
    CreateVolumeRequestFromEmpty,
    CreateVolumeRequestFromSnapshot,
    CreateVolumeRequest,
    ExportSnapshotToObjectStorageRequest,
    ImportSnapshotFromObjectStorageRequest,
    ImportSnapshotFromS3Request,
    UpdateSnapshotRequest,
    UpdateVolumeRequest,
)


def unmarshal_Reference(data: Any) -> Reference:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Reference' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("product_resource_type", None)
    if field is not None:
        args["product_resource_type"] = field

    field = data.get("product_resource_id", None)
    if field is not None:
        args["product_resource_id"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return Reference(**args)


def unmarshal_SnapshotParentVolume(data: Any) -> SnapshotParentVolume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SnapshotParentVolume' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    return SnapshotParentVolume(**args)


def unmarshal_Snapshot(data: Any) -> Snapshot:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Snapshot' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("size", None)
    if field is not None:
        args["size"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("references", None)
    if field is not None:
        args["references"] = (
            [unmarshal_Reference(v) for v in field] if field is not None else None
        )

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

    field = data.get("class", None)
    if field is not None:
        args["class_"] = field

    field = data.get("parent_volume", None)
    if field is not None:
        args["parent_volume"] = unmarshal_SnapshotParentVolume(field)
    else:
        args["parent_volume"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return Snapshot(**args)


def unmarshal_VolumeSpecifications(data: Any) -> VolumeSpecifications:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeSpecifications' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("class", None)
    if field is not None:
        args["class_"] = field

    field = data.get("perf_iops", None)
    if field is not None:
        args["perf_iops"] = field
    else:
        args["perf_iops"] = None

    return VolumeSpecifications(**args)


def unmarshal_Volume(data: Any) -> Volume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Volume' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("size", None)
    if field is not None:
        args["size"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("references", None)
    if field is not None:
        args["references"] = (
            [unmarshal_Reference(v) for v in field] if field is not None else None
        )

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("parent_snapshot_id", None)
    if field is not None:
        args["parent_snapshot_id"] = field
    else:
        args["parent_snapshot_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

    field = data.get("specs", None)
    if field is not None:
        args["specs"] = unmarshal_VolumeSpecifications(field)
    else:
        args["specs"] = None

    field = data.get("last_detached_at", None)
    if field is not None:
        args["last_detached_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["last_detached_at"] = None

    return Volume(**args)


def unmarshal_ListSnapshotsResponse(data: Any) -> ListSnapshotsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSnapshotsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshots", None)
    if field is not None:
        args["snapshots"] = (
            [unmarshal_Snapshot(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListSnapshotsResponse(**args)


def unmarshal_VolumeType(data: Any) -> VolumeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("pricing", None)
    if field is not None:
        args["pricing"] = unmarshal_Money(field)
    else:
        args["pricing"] = None

    field = data.get("snapshot_pricing", None)
    if field is not None:
        args["snapshot_pricing"] = unmarshal_Money(field)
    else:
        args["snapshot_pricing"] = None

    field = data.get("specs", None)
    if field is not None:
        args["specs"] = unmarshal_VolumeSpecifications(field)
    else:
        args["specs"] = None

    return VolumeType(**args)


def unmarshal_ListVolumeTypesResponse(data: Any) -> ListVolumeTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVolumeTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("volume_types", None)
    if field is not None:
        args["volume_types"] = (
            [unmarshal_VolumeType(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListVolumeTypesResponse(**args)


def unmarshal_ListVolumesResponse(data: Any) -> ListVolumesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVolumesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("volumes", None)
    if field is not None:
        args["volumes"] = (
            [unmarshal_Volume(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListVolumesResponse(**args)


def marshal_CreateSnapshotRequest(
    request: CreateSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateVolumeRequestFromEmpty(
    request: CreateVolumeRequestFromEmpty,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.size is not None:
        output["size"] = request.size

    return output


def marshal_CreateVolumeRequestFromSnapshot(
    request: CreateVolumeRequestFromSnapshot,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.snapshot_id is not None:
        output["snapshot_id"] = request.snapshot_id

    if request.size is not None:
        output["size"] = request.size

    return output


def marshal_CreateVolumeRequest(
    request: CreateVolumeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("from_empty", request.from_empty),
                OneOfPossibility("from_snapshot", request.from_snapshot),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("perf_iops", request.perf_iops),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_ExportSnapshotToObjectStorageRequest(
    request: ExportSnapshotToObjectStorageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.bucket is not None:
        output["bucket"] = request.bucket

    if request.key is not None:
        output["key"] = request.key

    return output


def marshal_ImportSnapshotFromObjectStorageRequest(
    request: ImportSnapshotFromObjectStorageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.bucket is not None:
        output["bucket"] = request.bucket

    if request.key is not None:
        output["key"] = request.key

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.size is not None:
        output["size"] = request.size

    return output


def marshal_ImportSnapshotFromS3Request(
    request: ImportSnapshotFromS3Request,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.bucket is not None:
        output["bucket"] = request.bucket

    if request.key is not None:
        output["key"] = request.key

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.size is not None:
        output["size"] = request.size

    return output


def marshal_UpdateSnapshotRequest(
    request: UpdateSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateVolumeRequest(
    request: UpdateVolumeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.size is not None:
        output["size"] = request.size

    if request.tags is not None:
        output["tags"] = request.tags

    if request.perf_iops is not None:
        output["perf_iops"] = request.perf_iops

    return output
