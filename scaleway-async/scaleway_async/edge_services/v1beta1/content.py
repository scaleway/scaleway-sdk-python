# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    PipelineStatus,
    PurgeRequestStatus,
)

PIPELINE_TRANSIENT_STATUSES: list[PipelineStatus] = [
    PipelineStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`PipelineStatus <PipelineStatus>`.
"""
PURGE_REQUEST_TRANSIENT_STATUSES: list[PurgeRequestStatus] = [
    PurgeRequestStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`PurgeRequestStatus <PurgeRequestStatus>`.
"""
