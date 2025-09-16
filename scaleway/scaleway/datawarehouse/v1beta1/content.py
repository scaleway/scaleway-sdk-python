# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    DeploymentStatus,
)

DEPLOYMENT_TRANSIENT_STATUSES: list[DeploymentStatus] = [
    DeploymentStatus.CREATING,
    DeploymentStatus.CONFIGURING,
    DeploymentStatus.DELETING,
    DeploymentStatus.LOCKING,
    DeploymentStatus.UNLOCKING,
]
"""
Lists transient statutes of the enum :class:`DeploymentStatus <DeploymentStatus>`.
"""
