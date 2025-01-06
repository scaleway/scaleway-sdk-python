# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    ServerPrivateNetworkServerStatus,
    ServerPrivateNetworkStatus,
    ServerStatus,
)

SERVER_PRIVATE_NETWORK_SERVER_TRANSIENT_STATUSES: List[
    ServerPrivateNetworkServerStatus
] = [
    ServerPrivateNetworkServerStatus.ATTACHING,
    ServerPrivateNetworkServerStatus.DETACHING,
]
"""
Lists transient statutes of the enum :class:`ServerPrivateNetworkServerStatus <ServerPrivateNetworkServerStatus>`.
"""
SERVER_PRIVATE_NETWORK_TRANSIENT_STATUSES: List[ServerPrivateNetworkStatus] = [
    ServerPrivateNetworkStatus.VPC_UPDATING,
]
"""
Lists transient statutes of the enum :class:`ServerPrivateNetworkStatus <ServerPrivateNetworkStatus>`.
"""
SERVER_TRANSIENT_STATUSES: List[ServerStatus] = [
    ServerStatus.STARTING,
    ServerStatus.REBOOTING,
    ServerStatus.UPDATING,
    ServerStatus.LOCKING,
    ServerStatus.UNLOCKING,
    ServerStatus.REINSTALLING,
    ServerStatus.BUSY,
]
"""
Lists transient statutes of the enum :class:`ServerStatus <ServerStatus>`.
"""
