# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    ClusterStatus,
    NodeStatus,
    PoolStatus,
)

CLUSTER_TRANSIENT_STATUSES: list[ClusterStatus] = [
    ClusterStatus.CREATING,
    ClusterStatus.DELETING,
    ClusterStatus.UPDATING,
]
"""
Lists transient statutes of the enum :class:`ClusterStatus <ClusterStatus>`.
"""
NODE_TRANSIENT_STATUSES: list[NodeStatus] = [
    NodeStatus.CREATING,
    NodeStatus.DELETING,
    NodeStatus.REBOOTING,
    NodeStatus.UPGRADING,
    NodeStatus.STARTING,
    NodeStatus.REGISTERING,
]
"""
Lists transient statutes of the enum :class:`NodeStatus <NodeStatus>`.
"""
POOL_TRANSIENT_STATUSES: list[PoolStatus] = [
    PoolStatus.DELETING,
    PoolStatus.SCALING,
    PoolStatus.UPGRADING,
]
"""
Lists transient statutes of the enum :class:`PoolStatus <PoolStatus>`.
"""
