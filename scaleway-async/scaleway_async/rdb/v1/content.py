# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    DatabaseBackupStatus,
    InstanceLogStatus,
    InstanceStatus,
    MaintenanceStatus,
    ReadReplicaStatus,
    SnapshotStatus,
)

DATABASE_BACKUP_TRANSIENT_STATUSES: list[DatabaseBackupStatus] = [
    DatabaseBackupStatus.CREATING,
    DatabaseBackupStatus.RESTORING,
    DatabaseBackupStatus.DELETING,
    DatabaseBackupStatus.EXPORTING,
]
"""
Lists transient statutes of the enum :class:`DatabaseBackupStatus <DatabaseBackupStatus>`.
"""
INSTANCE_LOG_TRANSIENT_STATUSES: list[InstanceLogStatus] = [
    InstanceLogStatus.CREATING,
]
"""
Lists transient statutes of the enum :class:`InstanceLogStatus <InstanceLogStatus>`.
"""
INSTANCE_TRANSIENT_STATUSES: list[InstanceStatus] = [
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
MAINTENANCE_TRANSIENT_STATUSES: list[MaintenanceStatus] = [
    MaintenanceStatus.ONGOING,
]
"""
Lists transient statutes of the enum :class:`MaintenanceStatus <MaintenanceStatus>`.
"""
READ_REPLICA_TRANSIENT_STATUSES: list[ReadReplicaStatus] = [
    ReadReplicaStatus.PROVISIONING,
    ReadReplicaStatus.INITIALIZING,
    ReadReplicaStatus.DELETING,
    ReadReplicaStatus.CONFIGURING,
    ReadReplicaStatus.PROMOTING,
]
"""
Lists transient statutes of the enum :class:`ReadReplicaStatus <ReadReplicaStatus>`.
"""
SNAPSHOT_TRANSIENT_STATUSES: list[SnapshotStatus] = [
    SnapshotStatus.CREATING,
    SnapshotStatus.RESTORING,
    SnapshotStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`SnapshotStatus <SnapshotStatus>`.
"""
