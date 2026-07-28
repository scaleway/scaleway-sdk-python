# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    PrivateNetworkInterfaceStatus,
    ServerFilesystemStatus,
    ServerIPStatus,
    ServerPrivateNetworkInterfaceStatus,
    ServerPublicNetworkInterfaceStatus,
    ServerStatus,
    SnapshotStatus,
    VolumeStatus,
)

PRIVATE_NETWORK_INTERFACE_TRANSIENT_STATUSES: list[PrivateNetworkInterfaceStatus] = [
    PrivateNetworkInterfaceStatus.ATTACHING,
    PrivateNetworkInterfaceStatus.DETACHING,
    PrivateNetworkInterfaceStatus.SYNCING,
]
"""
Lists transient statutes of the enum :class:`PrivateNetworkInterfaceStatus <PrivateNetworkInterfaceStatus>`.
"""
SERVER_FILESYSTEM_TRANSIENT_STATUSES: list[ServerFilesystemStatus] = [
    ServerFilesystemStatus.ATTACHING,
    ServerFilesystemStatus.DETACHING,
]
"""
Lists transient statutes of the enum :class:`ServerFilesystemStatus <ServerFilesystemStatus>`.
"""
SERVER_IP_TRANSIENT_STATUSES: list[ServerIPStatus] = [
    ServerIPStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`ServerIPStatus <ServerIPStatus>`.
"""
SERVER_PRIVATE_NETWORK_INTERFACE_TRANSIENT_STATUSES: list[
    ServerPrivateNetworkInterfaceStatus
] = [
    ServerPrivateNetworkInterfaceStatus.ATTACHING,
    ServerPrivateNetworkInterfaceStatus.DETACHING,
    ServerPrivateNetworkInterfaceStatus.SYNCING,
]
"""
Lists transient statutes of the enum :class:`ServerPrivateNetworkInterfaceStatus <ServerPrivateNetworkInterfaceStatus>`.
"""
SERVER_PUBLIC_NETWORK_INTERFACE_TRANSIENT_STATUSES: list[
    ServerPublicNetworkInterfaceStatus
] = [
    ServerPublicNetworkInterfaceStatus.SYNCING,
]
"""
Lists transient statutes of the enum :class:`ServerPublicNetworkInterfaceStatus <ServerPublicNetworkInterfaceStatus>`.
"""
SERVER_TRANSIENT_STATUSES: list[ServerStatus] = [
    ServerStatus.STARTING,
    ServerStatus.STOPPING,
    ServerStatus.PAUSING,
    ServerStatus.REBOOTING,
]
"""
Lists transient statutes of the enum :class:`ServerStatus <ServerStatus>`.
"""
SNAPSHOT_TRANSIENT_STATUSES: list[SnapshotStatus] = [
    SnapshotStatus.CREATING,
    SnapshotStatus.EXPORTING,
]
"""
Lists transient statutes of the enum :class:`SnapshotStatus <SnapshotStatus>`.
"""
VOLUME_TRANSIENT_STATUSES: list[VolumeStatus] = [
    VolumeStatus.SNAPSHOTTING,
    VolumeStatus.ATTACHING,
    VolumeStatus.DETACHING,
    VolumeStatus.CREATING,
    VolumeStatus.MIGRATING,
]
"""
Lists transient statutes of the enum :class:`VolumeStatus <VolumeStatus>`.
"""
