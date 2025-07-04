# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    DeploymentStatus,
)

DEPLOYMENT_TRANSIENT_STATUSES: List[DeploymentStatus] = [
    DeploymentStatus.CREATING,
    DeploymentStatus.DEPLOYING,
    DeploymentStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`DeploymentStatus <DeploymentStatus>`.
"""
