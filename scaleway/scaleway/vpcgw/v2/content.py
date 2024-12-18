# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    GatewayNetworkStatus,
    GatewayStatus,
)

GATEWAY_NETWORK_TRANSIENT_STATUSES: List[GatewayNetworkStatus] = [
    GatewayNetworkStatus.ATTACHING,
    GatewayNetworkStatus.CONFIGURING,
    GatewayNetworkStatus.DETACHING,
]
"""
Lists transient statutes of the enum :class:`GatewayNetworkStatus <GatewayNetworkStatus>`.
"""
GATEWAY_TRANSIENT_STATUSES: List[GatewayStatus] = [
    GatewayStatus.ALLOCATING,
    GatewayStatus.CONFIGURING,
    GatewayStatus.STOPPING,
    GatewayStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`GatewayStatus <GatewayStatus>`.
"""
