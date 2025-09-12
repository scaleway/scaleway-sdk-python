# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    ServerInstallStatus,
    ServerPrivateNetworkStatus,
    ServerStatus,
)

SERVER_INSTALL_TRANSIENT_STATUSES: list[ServerInstallStatus] = [
    ServerInstallStatus.TO_INSTALL,
    ServerInstallStatus.INSTALLING,
]
"""
Lists transient statutes of the enum :class:`ServerInstallStatus <ServerInstallStatus>`.
"""
SERVER_PRIVATE_NETWORK_TRANSIENT_STATUSES: list[ServerPrivateNetworkStatus] = [
    ServerPrivateNetworkStatus.ATTACHING,
    ServerPrivateNetworkStatus.DETACHING,
]
"""
Lists transient statutes of the enum :class:`ServerPrivateNetworkStatus <ServerPrivateNetworkStatus>`.
"""
SERVER_TRANSIENT_STATUSES: list[ServerStatus] = [
    ServerStatus.DELIVERING,
    ServerStatus.STOPPING,
    ServerStatus.STARTING,
    ServerStatus.DELETING,
    ServerStatus.ORDERED,
    ServerStatus.RESETTING,
    ServerStatus.MIGRATING,
]
"""
Lists transient statutes of the enum :class:`ServerStatus <ServerStatus>`.
"""
