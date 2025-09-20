# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    ImageState,
    IpState,
    PrivateNICState,
    SecurityGroupState,
    ServerFilesystemState,
    ServerIpState,
    ServerState,
    SnapshotState,
    TaskStatus,
    VolumeServerState,
    VolumeState,
)

IMAGE_TRANSIENT_STATUSES: list[ImageState] = [
    ImageState.CREATING,
]
"""
Lists transient statutes of the enum :class:`ImageState <ImageState>`.
"""
IP_TRANSIENT_STATUSES: list[IpState] = [
    IpState.PENDING,
]
"""
Lists transient statutes of the enum :class:`IpState <IpState>`.
"""
PRIVATE_NIC_TRANSIENT_STATUSES: list[PrivateNICState] = [
    PrivateNICState.SYNCING,
]
"""
Lists transient statutes of the enum :class:`PrivateNICState <PrivateNICState>`.
"""
SECURITY_GROUP_TRANSIENT_STATUSES: list[SecurityGroupState] = [
    SecurityGroupState.SYNCING,
]
"""
Lists transient statutes of the enum :class:`SecurityGroupState <SecurityGroupState>`.
"""
SERVER_FILESYSTEM_TRANSIENT_STATUSES: list[ServerFilesystemState] = [
    ServerFilesystemState.ATTACHING,
    ServerFilesystemState.DETACHING,
]
"""
Lists transient statutes of the enum :class:`ServerFilesystemState <ServerFilesystemState>`.
"""
SERVER_IP_TRANSIENT_STATUSES: list[ServerIpState] = [
    ServerIpState.PENDING,
]
"""
Lists transient statutes of the enum :class:`ServerIpState <ServerIpState>`.
"""
SERVER_TRANSIENT_STATUSES: list[ServerState] = [
    ServerState.STARTING,
    ServerState.STOPPING,
]
"""
Lists transient statutes of the enum :class:`ServerState <ServerState>`.
"""
SNAPSHOT_TRANSIENT_STATUSES: list[SnapshotState] = [
    SnapshotState.SNAPSHOTTING,
    SnapshotState.IMPORTING,
    SnapshotState.EXPORTING,
]
"""
Lists transient statutes of the enum :class:`SnapshotState <SnapshotState>`.
"""
TASK_TRANSIENT_STATUSES: list[TaskStatus] = [
    TaskStatus.PENDING,
    TaskStatus.STARTED,
    TaskStatus.RETRY,
]
"""
Lists transient statutes of the enum :class:`TaskStatus <TaskStatus>`.
"""
VOLUME_SERVER_TRANSIENT_STATUSES: list[VolumeServerState] = [
    VolumeServerState.SNAPSHOTTING,
    VolumeServerState.RESIZING,
    VolumeServerState.FETCHING,
    VolumeServerState.SAVING,
    VolumeServerState.HOTSYNCING,
    VolumeServerState.ATTACHING,
]
"""
Lists transient statutes of the enum :class:`VolumeServerState <VolumeServerState>`.
"""
VOLUME_TRANSIENT_STATUSES: list[VolumeState] = [
    VolumeState.SNAPSHOTTING,
    VolumeState.FETCHING,
    VolumeState.SAVING,
    VolumeState.ATTACHING,
    VolumeState.RESIZING,
    VolumeState.HOTSYNCING,
]
"""
Lists transient statutes of the enum :class:`VolumeState <VolumeState>`.
"""
