# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    InstanceLogStatus,
    InstanceStatus,
    MaintenanceStatus,
    ReadReplicaStatus,
    SnapshotStatus,
)

INSTANCE_LOG_TRANSIENT_STATUSES: List[InstanceLogStatus] = [
    InstanceLogStatus.CREATING,
]
"""
Lists transient statutes of the enum :class:`InstanceLogStatus <InstanceLogStatus>`.
"""
INSTANCE_TRANSIENT_STATUSES: List[InstanceStatus] = [
    InstanceStatus.PROVISIONING,
    InstanceStatus.CONFIGURING,
    InstanceStatus.DELETING,
    InstanceStatus.AUTOHEALING,
    InstanceStatus.INITIALIZING,
    InstanceStatus.BACKUPING,
    InstanceStatus.SNAPSHOTTING,
    InstanceStatus.RESTARTING,
]
"""
Lists transient statutes of the enum :class:`InstanceStatus <InstanceStatus>`.
"""
MAINTENANCE_TRANSIENT_STATUSES: List[MaintenanceStatus] = [
    MaintenanceStatus.ONGOING,
]
"""
Lists transient statutes of the enum :class:`MaintenanceStatus <MaintenanceStatus>`.
"""
READ_REPLICA_TRANSIENT_STATUSES: List[ReadReplicaStatus] = [
    ReadReplicaStatus.PROVISIONING,
    ReadReplicaStatus.INITIALIZING,
    ReadReplicaStatus.DELETING,
    ReadReplicaStatus.CONFIGURING,
    ReadReplicaStatus.PROMOTING,
]
"""
Lists transient statutes of the enum :class:`ReadReplicaStatus <ReadReplicaStatus>`.
"""
SNAPSHOT_TRANSIENT_STATUSES: List[SnapshotStatus] = [
    SnapshotStatus.CREATING,
    SnapshotStatus.RESTORING,
    SnapshotStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`SnapshotStatus <SnapshotStatus>`.
"""
