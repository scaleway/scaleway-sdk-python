# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    ClusterStatus,
)

CLUSTER_TRANSIENT_STATUSES: list[ClusterStatus] = [
    ClusterStatus.PROVISIONING,
    ClusterStatus.CONFIGURING,
    ClusterStatus.DELETING,
    ClusterStatus.AUTOHEALING,
    ClusterStatus.INITIALIZING,
]
"""
Lists transient statutes of the enum :class:`ClusterStatus <ClusterStatus>`.
"""
