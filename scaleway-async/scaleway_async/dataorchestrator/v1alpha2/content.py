# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    RunServerlessContainersTaskStatus,
    RunStatus,
)

RUN_SERVERLESS_CONTAINERS_TASK_TRANSIENT_STATUSES: list[
    RunServerlessContainersTaskStatus
] = [
    RunServerlessContainersTaskStatus.DELETING,
    RunServerlessContainersTaskStatus.UPDATING,
    RunServerlessContainersTaskStatus.CREATING,
    RunServerlessContainersTaskStatus.UPGRADING,
    RunServerlessContainersTaskStatus.REBALANCING,
    RunServerlessContainersTaskStatus.TRIGGERING,
]
"""
Lists transient statutes of the enum :class:`RunServerlessContainersTaskStatus <RunServerlessContainersTaskStatus>`.
"""
RUN_TRANSIENT_STATUSES: list[RunStatus] = [
    RunStatus.INITIALIZED,
    RunStatus.VALIDATED,
    RunStatus.QUEUED,
    RunStatus.RUNNING,
    RunStatus.INTERRUPTING,
    RunStatus.PAUSING,
]
"""
Lists transient statutes of the enum :class:`RunStatus <RunStatus>`.
"""
