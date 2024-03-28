# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    DatabaseStatus,
)

DATABASE_TRANSIENT_STATUSES: List[DatabaseStatus] = [
    DatabaseStatus.CREATING,
    DatabaseStatus.DELETING,
    DatabaseStatus.RESTORING,
]
"""
Lists transient statutes of the enum :class:`DatabaseStatus <DatabaseStatus>`.
"""
