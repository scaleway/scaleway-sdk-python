# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    ContainerStatus,
    CronStatus,
    DomainStatus,
    NamespaceStatus,
    TokenStatus,
    TriggerStatus,
)

CONTAINER_TRANSIENT_STATUSES: List[ContainerStatus] = [
    ContainerStatus.DELETING,
    ContainerStatus.CREATING,
    ContainerStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`ContainerStatus <ContainerStatus>`.
"""
CRON_TRANSIENT_STATUSES: List[CronStatus] = [
    CronStatus.DELETING,
    CronStatus.CREATING,
    CronStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`CronStatus <CronStatus>`.
"""
DOMAIN_TRANSIENT_STATUSES: List[DomainStatus] = [
    DomainStatus.DELETING,
    DomainStatus.CREATING,
    DomainStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`DomainStatus <DomainStatus>`.
"""
NAMESPACE_TRANSIENT_STATUSES: List[NamespaceStatus] = [
    NamespaceStatus.DELETING,
    NamespaceStatus.CREATING,
    NamespaceStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`NamespaceStatus <NamespaceStatus>`.
"""
TOKEN_TRANSIENT_STATUSES: List[TokenStatus] = [
    TokenStatus.DELETING,
    TokenStatus.CREATING,
]
"""
Lists transient statutes of the enum :class:`TokenStatus <TokenStatus>`.
"""
TRIGGER_TRANSIENT_STATUSES: List[TriggerStatus] = [
    TriggerStatus.DELETING,
    TriggerStatus.CREATING,
    TriggerStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`TriggerStatus <TriggerStatus>`.
"""
