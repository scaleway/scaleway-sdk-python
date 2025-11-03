# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    ClusterStatus,
)

CLUSTER_TRANSIENT_STATUSES: list[ClusterStatus] = [
    ClusterStatus.CREATING,
    ClusterStatus.CONFIGURING,
    ClusterStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`ClusterStatus <ClusterStatus>`.
"""
