# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    ListSnapshotsRequestOrderBy,
    ListVolumesRequestOrderBy,
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
    UpdateSnapshotRequest,
    UpdateVolumeRequest,
)

def unmarshal_Reference(data: Any) -> Reference:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Reference' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("product_resource_type", str())
    args["product_resource_type"] = field

    field = data.get("product_resource_id", str())
    args["product_resource_id"] = field

    field = data.get("type", getattr(ReferenceType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("status", getattr(ReferenceStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Reference(**args)

def unmarshal_SnapshotParentVolume(data: Any) -> SnapshotParentVolume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SnapshotParentVolume' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("status", getattr(VolumeStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    return SnapshotParentVolume(**args)

def unmarshal_Snapshot(data: Any) -> Snapshot:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Snapshot' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("size", 0)
    args["size"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("references", [])
    args["references"] = [unmarshal_Reference(v) for v in field] if field is not None else None

    field = data.get("status", getattr(SnapshotStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("class", getattr(StorageClass, "UNKNOWN_STORAGE_CLASS"))
    args["class_"] = field

    field = data.get("parent_volume", None)
    args["parent_volume"] = unmarshal_SnapshotParentVolume(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Snapshot(**args)

def unmarshal_VolumeSpecifications(data: Any) -> VolumeSpecifications:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeSpecifications' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("class", getattr(StorageClass, "UNKNOWN_STORAGE_CLASS"))
    args["class_"] = field

    field = data.get("perf_iops", None)
    args["perf_iops"] = field

    return VolumeSpecifications(**args)

def unmarshal_Volume(data: Any) -> Volume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Volume' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("size", 0)
    args["size"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("references", [])
    args["references"] = [unmarshal_Reference(v) for v in field] if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("parent_snapshot_id", None)
    args["parent_snapshot_id"] = field

    field = data.get("status", getattr(VolumeStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("specs", None)
    args["specs"] = unmarshal_VolumeSpecifications(field) if field is not None else None

    field = data.get("last_detached_at", None)
    args["last_detached_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Volume(**args)

def unmarshal_ListSnapshotsResponse(data: Any) -> ListSnapshotsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSnapshotsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshots", [])
    args["snapshots"] = [unmarshal_Snapshot(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListSnapshotsResponse(**args)

def unmarshal_VolumeType(data: Any) -> VolumeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("pricing", None)
    args["pricing"] = unmarshal_Money(field) if field is not None else None

    field = data.get("snapshot_pricing", None)
    args["snapshot_pricing"] = unmarshal_Money(field) if field is not None else None

    field = data.get("specs", None)
    args["specs"] = unmarshal_VolumeSpecifications(field) if field is not None else None

    return VolumeType(**args)

def unmarshal_ListVolumeTypesResponse(data: Any) -> ListVolumeTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVolumeTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("volume_types", [])
    args["volume_types"] = [unmarshal_VolumeType(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListVolumeTypesResponse(**args)

def unmarshal_ListVolumesResponse(data: Any) -> ListVolumesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVolumesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("volumes", [])
    args["volumes"] = [unmarshal_Volume(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListVolumesResponse(**args)

def marshal_CreateSnapshotRequest(
    request: CreateSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id
    else:
        output["volume_id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_CreateVolumeRequestFromEmpty(
    request: CreateVolumeRequestFromEmpty,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = str()


    return output

def marshal_CreateVolumeRequestFromSnapshot(
    request: CreateVolumeRequestFromSnapshot,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.snapshot_id is not None:
        output["snapshot_id"] = request.snapshot_id
    else:
        output["snapshot_id"] = str()

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = None


    return output

def marshal_CreateVolumeRequest(
    request: CreateVolumeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="from_empty", value=request.from_empty,marshal_func=marshal_CreateVolumeRequestFromEmpty
            ),
            OneOfPossibility(param="from_snapshot", value=request.from_snapshot,marshal_func=marshal_CreateVolumeRequestFromSnapshot
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="perf_iops", value=request.perf_iops,marshal_func=None
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_ExportSnapshotToObjectStorageRequest(
    request: ExportSnapshotToObjectStorageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.bucket is not None:
        output["bucket"] = request.bucket
    else:
        output["bucket"] = str()

    if request.key is not None:
        output["key"] = request.key
    else:
        output["key"] = str()


    return output

def marshal_ImportSnapshotFromObjectStorageRequest(
    request: ImportSnapshotFromObjectStorageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.bucket is not None:
        output["bucket"] = request.bucket
    else:
        output["bucket"] = str()

    if request.key is not None:
        output["key"] = request.key
    else:
        output["key"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = None


    return output

def marshal_UpdateSnapshotRequest(
    request: UpdateSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_UpdateVolumeRequest(
    request: UpdateVolumeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.perf_iops is not None:
        output["perf_iops"] = request.perf_iops
    else:
        output["perf_iops"] = None


    return output
