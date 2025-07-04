# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    InstanceStatus,
    SnapshotStatus,
)

INSTANCE_TRANSIENT_STATUSES: List[InstanceStatus] = [
    InstanceStatus.PROVISIONING,
    InstanceStatus.CONFIGURING,
    InstanceStatus.DELETING,
    InstanceStatus.INITIALIZING,
    InstanceStatus.SNAPSHOTTING,
]
"""
Lists transient statutes of the enum :class:`InstanceStatus <InstanceStatus>`.
"""
SNAPSHOT_TRANSIENT_STATUSES: List[SnapshotStatus] = [
    SnapshotStatus.CREATING,
    SnapshotStatus.RESTORING,
    SnapshotStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`SnapshotStatus <SnapshotStatus>`.
"""
