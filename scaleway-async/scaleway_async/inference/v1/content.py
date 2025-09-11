# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    DeploymentStatus,
    ModelStatus,
)

DEPLOYMENT_TRANSIENT_STATUSES: list[DeploymentStatus] = [
    DeploymentStatus.CREATING,
    DeploymentStatus.DEPLOYING,
    DeploymentStatus.DELETING,
    DeploymentStatus.SCALING,
]
"""
Lists transient statutes of the enum :class:`DeploymentStatus <DeploymentStatus>`.
"""
MODEL_TRANSIENT_STATUSES: list[ModelStatus] = [
    ModelStatus.PREPARING,
    ModelStatus.DOWNLOADING,
]
"""
Lists transient statutes of the enum :class:`ModelStatus <ModelStatus>`.
"""
