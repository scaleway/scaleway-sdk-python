# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    ImageState,
    IpState,
    PrivateNICState,
    SecurityGroupState,
    ServerIpState,
    ServerState,
    SnapshotState,
    TaskStatus,
    VolumeServerState,
    VolumeState,
)

IMAGE_TRANSIENT_STATUSES: List[ImageState] = [
    ImageState.CREATING,
]
"""
Lists transient statutes of the enum :class:`ImageState <ImageState>`.
"""
IP_TRANSIENT_STATUSES: List[IpState] = [
    IpState.PENDING,
]
"""
Lists transient statutes of the enum :class:`IpState <IpState>`.
"""
PRIVATE_NIC_TRANSIENT_STATUSES: List[PrivateNICState] = [
    PrivateNICState.SYNCING,
]
"""
Lists transient statutes of the enum :class:`PrivateNICState <PrivateNICState>`.
"""
SECURITY_GROUP_TRANSIENT_STATUSES: List[SecurityGroupState] = [
    SecurityGroupState.SYNCING,
]
"""
Lists transient statutes of the enum :class:`SecurityGroupState <SecurityGroupState>`.
"""
SERVER_IP_TRANSIENT_STATUSES: List[ServerIpState] = [
    ServerIpState.PENDING,
]
"""
Lists transient statutes of the enum :class:`ServerIpState <ServerIpState>`.
"""
SERVER_TRANSIENT_STATUSES: List[ServerState] = [
    ServerState.STARTING,
    ServerState.STOPPING,
]
"""
Lists transient statutes of the enum :class:`ServerState <ServerState>`.
"""
SNAPSHOT_TRANSIENT_STATUSES: List[SnapshotState] = [
    SnapshotState.SNAPSHOTTING,
    SnapshotState.IMPORTING,
    SnapshotState.EXPORTING,
]
"""
Lists transient statutes of the enum :class:`SnapshotState <SnapshotState>`.
"""
TASK_TRANSIENT_STATUSES: List[TaskStatus] = [
    TaskStatus.PENDING,
    TaskStatus.STARTED,
    TaskStatus.RETRY,
]
"""
Lists transient statutes of the enum :class:`TaskStatus <TaskStatus>`.
"""
VOLUME_SERVER_TRANSIENT_STATUSES: List[VolumeServerState] = [
    VolumeServerState.SNAPSHOTTING,
    VolumeServerState.FETCHING,
    VolumeServerState.RESIZING,
    VolumeServerState.SAVING,
    VolumeServerState.HOTSYNCING,
]
"""
Lists transient statutes of the enum :class:`VolumeServerState <VolumeServerState>`.
"""
VOLUME_TRANSIENT_STATUSES: List[VolumeState] = [
    VolumeState.SNAPSHOTTING,
    VolumeState.FETCHING,
    VolumeState.RESIZING,
    VolumeState.SAVING,
    VolumeState.HOTSYNCING,
]
"""
Lists transient statutes of the enum :class:`VolumeState <VolumeState>`.
"""
