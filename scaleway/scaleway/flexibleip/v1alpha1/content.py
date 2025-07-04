# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    FlexibleIPStatus,
    MACAddressStatus,
)

FLEXIBLE_IP_TRANSIENT_STATUSES: List[FlexibleIPStatus] = [
    FlexibleIPStatus.UPDATING,
    FlexibleIPStatus.DETACHING,
]
"""
Lists transient statutes of the enum :class:`FlexibleIPStatus <FlexibleIPStatus>`.
"""
MAC_ADDRESS_TRANSIENT_STATUSES: List[MACAddressStatus] = [
    MACAddressStatus.UPDATING,
    MACAddressStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`MACAddressStatus <MACAddressStatus>`.
"""
