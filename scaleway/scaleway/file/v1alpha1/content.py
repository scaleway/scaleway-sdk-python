# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    FileSystemStatus,
    SnapshotStatus,
)

FILE_SYSTEM_TRANSIENT_STATUSES: list[FileSystemStatus] = [
    FileSystemStatus.CREATING,
    FileSystemStatus.UPDATING,
    FileSystemStatus.SNAPSHOTTING,
]
"""
Lists transient statutes of the enum :class:`FileSystemStatus <FileSystemStatus>`.
"""
SNAPSHOT_TRANSIENT_STATUSES: list[SnapshotStatus] = [
    SnapshotStatus.CREATING,
    SnapshotStatus.DELETING,
    SnapshotStatus.CLONING,
]
"""
Lists transient statutes of the enum :class:`SnapshotStatus <SnapshotStatus>`.
"""
