# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Money,
    Zone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ListSnapshotsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListVolumesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ReferenceStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ATTACHING = "attaching"
    ATTACHED = "attached"
    DETACHING = "detaching"
    DETACHED = "detached"
    CREATING = "creating"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class ReferenceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    LINK = "link"
    EXCLUSIVE = "exclusive"
    READ_ONLY = "read_only"

    def __str__(self) -> str:
        return str(self.value)


class SnapshotStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    CREATING = "creating"
    AVAILABLE = "available"
    ERROR = "error"
    DELETING = "deleting"
    DELETED = "deleted"
    IN_USE = "in_use"
    LOCKED = "locked"
    EXPORTING = "exporting"

    def __str__(self) -> str:
        return str(self.value)


class StorageClass(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STORAGE_CLASS = "unknown_storage_class"
    UNSPECIFIED = "unspecified"
    BSSD = "bssd"
    SBS = "sbs"

    def __str__(self) -> str:
        return str(self.value)


class VolumeStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    CREATING = "creating"
    AVAILABLE = "available"
    IN_USE = "in_use"
    DELETING = "deleting"
    DELETED = "deleted"
    RESIZING = "resizing"
    ERROR = "error"
    SNAPSHOTTING = "snapshotting"
    LOCKED = "locked"
    UPDATING = "updating"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Reference:
    id: str
    """
    UUID of the reference.
    """

    product_resource_type: str
    """
    Type of resource to which the reference is associated.
    """

    product_resource_id: str
    """
    UUID of the product resource it refers to (according to the product_resource_type).
    """

    type_: ReferenceType
    """
    Type of reference (link, exclusive, read_only).
    """

    status: ReferenceStatus
    """
    Status of the reference. Statuses include `attaching`, `attached`, and `detaching`.
    """

    created_at: Optional[datetime]
    """
    Creation date of the reference.
    """


@dataclass
class SnapshotParentVolume:
    id: str
    """
    Parent volume UUID (volume from which the snapshot originates).
    """

    name: str
    """
    Name of the parent volume.
    """

    type_: str
    """
    Volume type of the parent volume.
    """

    status: VolumeStatus
    """
    Current status the parent volume.
    """


@dataclass
class VolumeSpecifications:
    class_: StorageClass
    """
    The storage class of the volume.
    """

    perf_iops: Optional[int]
    """
    The maximum IO/s expected, according to the different options available in stock (`5000 | 15000`).
    """


@dataclass
class CreateVolumeRequestFromEmpty:
    size: int
    """
    Must be compliant with the minimum (1 GB) and maximum (10 TB) allowed size.
    """


@dataclass
class CreateVolumeRequestFromSnapshot:
    snapshot_id: str
    """
    Source snapshot from which volume will be created.
    """

    size: Optional[int]
    """
    Must be compliant with the minimum (1 GB) and maximum (10 TB) allowed size.
Size is optional and is used only if a resize of the volume is requested, otherwise original snapshot size will be used.
    """


@dataclass
class Snapshot:
    id: str
    """
    UUID of the snapshot.
    """

    name: str
    """
    Name of the snapshot.
    """

    size: int
    """
    Size in bytes of the snapshot.
    """

    project_id: str
    """
    UUID of the project the snapshot belongs to.
    """

    references: List[Reference]
    """
    List of the references to the snapshot.
    """

    status: SnapshotStatus
    """
    Current status of the snapshot (available, in_use, ...).
    """

    tags: List[str]
    """
    List of tags assigned to the volume.
    """

    zone: Zone
    """
    Snapshot zone.
    """

    class_: StorageClass
    """
    Storage class of the snapshot.
    """

    parent_volume: Optional[SnapshotParentVolume]
    """
    If the parent volume was deleted, value is null.
    """

    created_at: Optional[datetime]
    """
    Creation date of the snapshot.
    """

    updated_at: Optional[datetime]
    """
    Last modification date of the properties of a snapshot.
    """


@dataclass
class VolumeType:
    type_: str
    """
    Volume type.
    """

    pricing: Optional[Money]
    """
    Price of the volume billed in GB/hour.
    """

    snapshot_pricing: Optional[Money]
    """
    Price of the snapshot billed in GB/hour.
    """

    specs: Optional[VolumeSpecifications]
    """
    Volume specifications of the volume type.
    """


@dataclass
class Volume:
    id: str
    """
    UUID of the volume.
    """

    name: str
    """
    Name of the volume.
    """

    type_: str
    """
    Volume type.
    """

    size: int
    """
    Volume size in bytes.
    """

    project_id: str
    """
    UUID of the project to which the volume belongs.
    """

    references: List[Reference]
    """
    List of the references to the volume.
    """

    created_at: Optional[datetime]
    """
    Creation date of the volume.
    """

    updated_at: Optional[datetime]
    """
    Last update of the properties of a volume.
    """

    parent_snapshot_id: Optional[str]
    """
    When a volume is created from a snapshot, is the UUID of the snapshot from which the volume has been created.
    """

    status: VolumeStatus
    """
    Current status of the volume (available, in_use, ...).
    """

    tags: List[str]
    """
    List of tags assigned to the volume.
    """

    zone: Zone
    """
    Volume zone.
    """

    specs: Optional[VolumeSpecifications]
    """
    Specifications of the volume.
    """

    last_detached_at: Optional[datetime]
    """
    Last time the volume was detached.
    """


@dataclass
class CreateSnapshotRequest:
    volume_id: str
    """
    UUID of the volume to snapshot.
    """

    name: str
    """
    Name of the snapshot.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    UUID of the project to which the volume and the snapshot belong.
    """

    tags: Optional[List[str]]
    """
    List of tags assigned to the snapshot.
    """


@dataclass
class CreateVolumeRequest:
    name: str
    """
    Name of the volume.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    UUID of the project the volume belongs to.
    """

    tags: Optional[List[str]]
    """
    List of tags assigned to the volume.
    """

    from_empty: Optional[CreateVolumeRequestFromEmpty]

    from_snapshot: Optional[CreateVolumeRequestFromSnapshot]

    perf_iops: Optional[int]


@dataclass
class DeleteSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteVolumeRequest:
    volume_id: str
    """
    UUID of the volume.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ExportSnapshotToObjectStorageRequest:
    snapshot_id: str
    """
    UUID of the snapshot.
    """

    bucket: str
    """
    Scaleway Object Storage bucket where the object is stored.
    """

    key: str
    """
    The object key inside the given bucket.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetVolumeRequest:
    volume_id: str
    """
    UUID of the volume.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ImportSnapshotFromObjectStorageRequest:
    bucket: str
    """
    Scaleway Object Storage bucket where the object is stored.
    """

    key: str
    """
    The object key inside the given bucket.
    """

    name: str
    """
    Name of the snapshot.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    UUID of the Project to which the volume and the snapshot belong.
    """

    tags: Optional[List[str]]
    """
    List of tags assigned to the snapshot.
    """

    size: Optional[int]
    """
    Size of the snapshot.
    """


@dataclass
class ImportSnapshotFromS3Request:
    bucket: str
    """
    Scaleway Object Storage bucket where the object is stored.
    """

    key: str
    """
    The object key inside the given bucket.
    """

    name: str
    """
    Name of the snapshot.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    UUID of the Project to which the volume and the snapshot belong.
    """

    tags: Optional[List[str]]
    """
    List of tags assigned to the snapshot.
    """

    size: Optional[int]
    """
    Size of the snapshot.
    """


@dataclass
class ListSnapshotsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListSnapshotsRequestOrderBy]
    """
    Criteria to use when ordering the list.
    """

    project_id: Optional[str]
    """
    Filter by Project ID.
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Page size, defines how many entries are returned in one page, must be lower or equal to 100.
    """

    volume_id: Optional[str]
    """
    Filter snapshots by the ID of the original volume.
    """

    name: Optional[str]
    """
    Filter snapshots by their names.
    """


@dataclass
class ListSnapshotsResponse:
    snapshots: List[Snapshot]
    """
    Paginated returned list of snapshots.
    """

    total_count: int
    """
    Total number of snpashots in the project.
    """


@dataclass
class ListVolumeTypesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Page size, defines how many entries are returned in one page, must be lower or equal to 100.
    """


@dataclass
class ListVolumeTypesResponse:
    volume_types: List[VolumeType]
    """
    Returns paginated list of volume-types.
    """

    total_count: int
    """
    Total number of volume-types currently available in stock.
    """


@dataclass
class ListVolumesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListVolumesRequestOrderBy]
    """
    Criteria to use when ordering the list.
    """

    project_id: Optional[str]
    """
    Filter by Project ID.
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Page size, defines how many entries are returned in one page, must be lower or equal to 100.
    """

    name: Optional[str]
    """
    Filter the return volumes by their names.
    """

    product_resource_id: Optional[str]
    """
    Filter by a product resource ID linked to this volume (such as an Instance ID).
    """


@dataclass
class ListVolumesResponse:
    volumes: List[Volume]
    """
    Paginated returned list of volumes.
    """

    total_count: int
    """
    Total number of volumes in the project.
    """


@dataclass
class UpdateSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    When defined, is the name of the snapshot.
    """

    tags: Optional[List[str]]
    """
    List of tags assigned to the snapshot.
    """


@dataclass
class UpdateVolumeRequest:
    volume_id: str
    """
    UUID of the volume.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    When defined, is the new name of the volume.
    """

    size: Optional[int]
    """
    Size in bytes of the volume, with a granularity of 1 GB (10^9 bytes).
Must be compliant with the minimum (1GB) and maximum (10TB) allowed size.
    """

    tags: Optional[List[str]]
    """
    List of tags assigned to the volume.
    """

    perf_iops: Optional[int]
    """
    The selected value must be available for the volume's current storage class.
    """
