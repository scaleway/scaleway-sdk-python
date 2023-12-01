# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    NameStatus,
    PinStatus,
)

NAME_TRANSIENT_STATUSES: List[NameStatus] = [
    NameStatus.QUEUED,
    NameStatus.PUBLISHING,
]
"""
Lists transient statutes of the enum :class:`NameStatus <NameStatus>`.
"""
PIN_TRANSIENT_STATUSES: List[PinStatus] = [
    PinStatus.QUEUED,
    PinStatus.PINNING,
]
"""
Lists transient statutes of the enum :class:`PinStatus <PinStatus>`.
"""
