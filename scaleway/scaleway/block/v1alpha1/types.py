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
    SNAPSHOTTING = "snapshotting"
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

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class CreateVolumeRequestFromEmpty:
    """
    Create volume request. from empty.
    """

    size: int
    """
    Volume size in bytes, with a granularity of 1 GB (10^9 bytes).
    Must be compliant with the minimum (1 GB) and maximum (10 TB) allowed size.
    """


@dataclass
class CreateVolumeRequestFromSnapshot:
    """
    Create volume request. from snapshot.
    """

    size: Optional[int]
    """
    Volume size in bytes, with a granularity of 1 GB (10^9 bytes).
    Must be compliant with the minimum (1 GB) and maximum (10 TB) allowed size.
    Size is optional and is used only if a resize of the volume is requested, otherwise original snapshot size will be used.
    """

    snapshot_id: str
    """
    Source snapshot from which volume will be created.
    """


@dataclass
class ListSnapshotsResponse:
    """
    List snapshots response.
    """

    snapshots: List[SnapshotSummary]
    """
    Paginated returned list of snapshots.
    """

    total_count: int
    """
    Total number of snpashots in the project.
    """


@dataclass
class ListVolumeTypesResponse:
    """
    List volume types response.
    """

    volume_types: List[VolumeType]
    """
    Returns paginated list of volume-types.
    """

    total_count: int
    """
    Total number of volume-types currently available in stock.
    """


@dataclass
class ListVolumesResponse:
    """
    List volumes response.
    """

    volumes: List[Volume]
    """
    Paginated returned list of volumes.
    """

    total_count: int
    """
    Total number of volumes in the project.
    """


@dataclass
class Reference:
    """
    Reference.
    """

    id: str
    """
    UUID of the reference.
    """

    product_resource_type: str
    """
    Type of resoruce to which the reference is associated (snapshot or volume).
    """

    product_resource_id: str
    """
    UUID of the volume or the snapshot it refers to (according to the product_resource_type).
    """

    created_at: Optional[datetime]
    """
    Creation date of the reference.
    """

    type_: ReferenceType
    """
    Type of reference (link, exclusive, read_only).
    """

    status: ReferenceStatus
    """
    Status of reference (attaching, attached, detaching).
    """


@dataclass
class Snapshot:
    """
    Snapshot.
    """

    id: str
    """
    UUID of the snapshot.
    """

    name: str
    """
    Name of the snapshot.
    """

    parent_volume: Optional[SnapshotParentVolume]
    """
    Information about the parent volume.
    If the parent volume was deleted, value is null.
    """

    size: int
    """
    Size in bytes of the snapshot.
    """

    project_id: str
    """
    UUID of the project the snapshot belongs to.
    """

    created_at: Optional[datetime]
    """
    Creation date of the snapshot.
    """

    updated_at: Optional[datetime]
    """
    Last modification date of the properties of a snapshot.
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


@dataclass
class SnapshotParentVolume:
    """
    Snapshot. parent volume.
    """

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
class SnapshotSummary:
    """
    Snapshot summary.
    """

    id: str
    """
    UUID of the snapshot.
    """

    name: str
    """
    Name of the snapshot.
    """

    parent_volume: Optional[SnapshotParentVolume]
    """
    Information about the parent volume.
    If the parent volume has been deleted, value is null.
    """

    size: int
    """
    Size of the snapshot in bytes.
    """

    project_id: str
    """
    UUID of the project the snapshot belongs to.
    """

    created_at: Optional[datetime]
    """
    Creation date of the snapshot.
    """

    updated_at: Optional[datetime]
    """
    Last modification date of the properties of a snapshot.
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
    Snapshot Availability Zone.
    """

    class_: StorageClass
    """
    Storage class of the snapshot.
    """


@dataclass
class Volume:
    """
    Volume.
    """

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

    created_at: Optional[datetime]
    """
    Creation date of the volume.
    """

    updated_at: Optional[datetime]
    """
    Last update of the properties of a volume.
    """

    references: List[Reference]
    """
    List of the references to the volume.
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
class VolumeSpecifications:
    """
    Volume specifications.
    """

    perf_iops: Optional[int]
    """
    The maximum IO/s expected, according to the different options available in stock (`5000 | 15000`).
    """

    class_: StorageClass
    """
    The storage class of the volume.
    """


@dataclass
class VolumeType:
    """
    Volume type.
    """

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
class CreateVolumeRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: str
    """
    Name of the volume.
    """

    perf_iops: Optional[int]
    """
    The maximum IO/s expected, according to the different options available in stock (`5000 | 15000`).
    
    One-of ('requirements'): at most one of 'perf_iops' could be set.
    """

    project_id: Optional[str]
    """
    UUID of the project the volume belongs to.
    """

    from_empty: Optional[CreateVolumeRequestFromEmpty]
    """
    Specify the size of the new volume if creating a new one from scratch.
    
    One-of ('from_'): at most one of 'from_empty', 'from_snapshot' could be set.
    """

    from_snapshot: Optional[CreateVolumeRequestFromSnapshot]
    """
    Specify the snapshot ID of the original snapshot.
    
    One-of ('from_'): at most one of 'from_empty', 'from_snapshot' could be set.
    """

    tags: Optional[List[str]]
    """
    List of tags assigned to the volume.
    """


@dataclass
class GetVolumeRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_id: str
    """
    UUID of the volume.
    """


@dataclass
class DeleteVolumeRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_id: str
    """
    UUID of the volume.
    """


@dataclass
class UpdateVolumeRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_id: str
    """
    UUID of the volume.
    """

    name: Optional[str]
    """
    When defined, is the new name of the volume.
    """

    size: Optional[int]
    """
    Optional field for increasing the size of a volume (size must be equal or larger than the current one).
    Size in bytes of the volume, with a granularity of 1 GB (10^9 bytes).
    Must be compliant with the minimum (1GB) and maximum (10TB) allowed size.
    """

    tags: Optional[List[str]]
    """
    List of tags assigned to the volume.
    """

    perf_iops: Optional[int]
    """
    The maximum IO/s expected, according to the different options available in stock (`5000 | 15000`).
    The selected value must be available for the volume's current storage class.
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
class GetSnapshotRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    snapshot_id: str
    """
    UUID of the snapshot.
    """


@dataclass
class CreateSnapshotRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_id: str
    """
    UUID of the volume to snapshot.
    """

    name: str
    """
    Name of the snapshot.
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
class ImportSnapshotFromS3Request:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    bucket: str

    key: str

    name: str

    project_id: Optional[str]

    tags: Optional[List[str]]


@dataclass
class DeleteSnapshotRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    snapshot_id: str
    """
    UUID of the snapshot.
    """


@dataclass
class UpdateSnapshotRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    snapshot_id: str
    """
    UUID of the snapshot.
    """

    name: Optional[str]
    """
    When defined, is the name of the snapshot.
    """

    tags: Optional[List[str]]
    """
    List of tags assigned to the snapshot.
    """
