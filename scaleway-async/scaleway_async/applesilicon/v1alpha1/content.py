# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    ServerStatus,
)

SERVER_TRANSIENT_STATUSES: List[ServerStatus] = [
    ServerStatus.STARTING,
    ServerStatus.REBOOTING,
    ServerStatus.UPDATING,
    ServerStatus.LOCKING,
    ServerStatus.UNLOCKING,
    ServerStatus.REINSTALLING,
]
"""
Lists transient statutes of the enum :class:`ServerStatus <ServerStatus>`.
"""
