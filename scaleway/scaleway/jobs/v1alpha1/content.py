# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    JobRunState,
)

JOB_RUN_TRANSIENT_STATUSES: List[JobRunState] = [
    JobRunState.QUEUED,
    JobRunState.SCHEDULED,
    JobRunState.RUNNING,
]
"""
Lists transient statutes of the enum :class:`JobRunState <JobRunState>`.
"""
