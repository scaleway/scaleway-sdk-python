# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    ReferenceStatus,
    SnapshotStatus,
    VolumeStatus,
)

REFERENCE_TRANSIENT_STATUSES: list[ReferenceStatus] = [
    ReferenceStatus.ATTACHING,
    ReferenceStatus.DETACHING,
    ReferenceStatus.CREATING,
]
"""
Lists transient statutes of the enum :class:`ReferenceStatus <ReferenceStatus>`.
"""
SNAPSHOT_TRANSIENT_STATUSES: list[SnapshotStatus] = [
    SnapshotStatus.CREATING,
    SnapshotStatus.DELETING,
    SnapshotStatus.EXPORTING,
]
"""
Lists transient statutes of the enum :class:`SnapshotStatus <SnapshotStatus>`.
"""
VOLUME_TRANSIENT_STATUSES: list[VolumeStatus] = [
    VolumeStatus.CREATING,
    VolumeStatus.DELETING,
    VolumeStatus.RESIZING,
    VolumeStatus.SNAPSHOTTING,
    VolumeStatus.UPDATING,
]
"""
Lists transient statutes of the enum :class:`VolumeStatus <VolumeStatus>`.
"""
