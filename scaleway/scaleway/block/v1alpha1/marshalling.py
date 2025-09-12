# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
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
    ReferenceStatus,
    ReferenceType,
    SnapshotStatus,
    StorageClass,
    VolumeStatus,
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

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("product_resource_type", None)
    if field is not None:
        args["product_resource_type"] = field
    else:
        args["product_resource_type"] = None

    field = data.get("product_resource_id", None)
    if field is not None:
        args["product_resource_id"] = field
    else:
        args["product_resource_id"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = ReferenceType.UNKNOWN_TYPE

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ReferenceStatus.UNKNOWN_STATUS

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

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = VolumeStatus.UNKNOWN_STATUS

    return SnapshotParentVolume(**args)


def unmarshal_Snapshot(data: Any) -> Snapshot:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Snapshot' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = 0

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("references", None)
    if field is not None:
        args["references"] = (
            [unmarshal_Reference(v) for v in field] if field is not None else None
        )
    else:
        args["references"] = []

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = SnapshotStatus.UNKNOWN_STATUS

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("class", None)
    if field is not None:
        args["class_"] = field
    else:
        args["class_"] = StorageClass.UNKNOWN_STORAGE_CLASS

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

    args: dict[str, Any] = {}

    field = data.get("class", None)
    if field is not None:
        args["class_"] = field
    else:
        args["class_"] = StorageClass.UNKNOWN_STORAGE_CLASS

    field = data.get("perf_iops", None)
    if field is not None:
        args["perf_iops"] = field
    else:
        args["perf_iops"] = 0

    return VolumeSpecifications(**args)


def unmarshal_Volume(data: Any) -> Volume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Volume' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = 0

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("references", None)
    if field is not None:
        args["references"] = (
            [unmarshal_Reference(v) for v in field] if field is not None else None
        )
    else:
        args["references"] = []

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
    else:
        args["status"] = VolumeStatus.UNKNOWN_STATUS

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

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

    args: dict[str, Any] = {}

    field = data.get("snapshots", None)
    if field is not None:
        args["snapshots"] = (
            [unmarshal_Snapshot(v) for v in field] if field is not None else None
        )
    else:
        args["snapshots"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListSnapshotsResponse(**args)


def unmarshal_VolumeType(data: Any) -> VolumeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeType' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

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

    args: dict[str, Any] = {}

    field = data.get("volume_types", None)
    if field is not None:
        args["volume_types"] = (
            [unmarshal_VolumeType(v) for v in field] if field is not None else None
        )
    else:
        args["volume_types"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListVolumeTypesResponse(**args)


def unmarshal_ListVolumesResponse(data: Any) -> ListVolumesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVolumesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("volumes", None)
    if field is not None:
        args["volumes"] = (
            [unmarshal_Volume(v) for v in field] if field is not None else None
        )
    else:
        args["volumes"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListVolumesResponse(**args)


def marshal_CreateSnapshotRequest(
    request: CreateSnapshotRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateVolumeRequestFromEmpty(
    request: CreateVolumeRequestFromEmpty,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.size is not None:
        output["size"] = request.size

    return output


def marshal_CreateVolumeRequestFromSnapshot(
    request: CreateVolumeRequestFromSnapshot,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.snapshot_id is not None:
        output["snapshot_id"] = request.snapshot_id

    if request.size is not None:
        output["size"] = request.size

    return output


def marshal_CreateVolumeRequest(
    request: CreateVolumeRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="from_empty",
                    value=request.from_empty,
                    marshal_func=marshal_CreateVolumeRequestFromEmpty,
                ),
                OneOfPossibility(
                    param="from_snapshot",
                    value=request.from_snapshot,
                    marshal_func=marshal_CreateVolumeRequestFromSnapshot,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="perf_iops", value=request.perf_iops, marshal_func=None
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_ExportSnapshotToObjectStorageRequest(
    request: ExportSnapshotToObjectStorageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.bucket is not None:
        output["bucket"] = request.bucket

    if request.key is not None:
        output["key"] = request.key

    return output


def marshal_ImportSnapshotFromObjectStorageRequest(
    request: ImportSnapshotFromObjectStorageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.bucket is not None:
        output["bucket"] = request.bucket

    if request.key is not None:
        output["key"] = request.key

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.size is not None:
        output["size"] = request.size

    return output


def marshal_ImportSnapshotFromS3Request(
    request: ImportSnapshotFromS3Request,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.bucket is not None:
        output["bucket"] = request.bucket

    if request.key is not None:
        output["key"] = request.key

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.size is not None:
        output["size"] = request.size

    return output


def marshal_UpdateSnapshotRequest(
    request: UpdateSnapshotRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateVolumeRequest(
    request: UpdateVolumeRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.size is not None:
        output["size"] = request.size

    if request.tags is not None:
        output["tags"] = request.tags

    if request.perf_iops is not None:
        output["perf_iops"] = request.perf_iops

    return output
