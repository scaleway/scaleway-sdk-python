# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    ContainerStatus,
    DomainStatus,
    NamespaceStatus,
    TriggerStatus,
)

CONTAINER_TRANSIENT_STATUSES: list[ContainerStatus] = [
    ContainerStatus.UPDATING,
    ContainerStatus.DELETING,
    ContainerStatus.LOCKING,
    ContainerStatus.CREATING,
    ContainerStatus.UPGRADING,
]
"""
Lists transient statutes of the enum :class:`ContainerStatus <ContainerStatus>`.
"""
DOMAIN_TRANSIENT_STATUSES: list[DomainStatus] = [
    DomainStatus.CREATING,
    DomainStatus.UPDATING,
    DomainStatus.DELETING,
    DomainStatus.LOCKING,
    DomainStatus.UPGRADING,
]
"""
Lists transient statutes of the enum :class:`DomainStatus <DomainStatus>`.
"""
NAMESPACE_TRANSIENT_STATUSES: list[NamespaceStatus] = [
    NamespaceStatus.UPDATING,
    NamespaceStatus.DELETING,
    NamespaceStatus.LOCKING,
    NamespaceStatus.CREATING,
    NamespaceStatus.UPGRADING,
]
"""
Lists transient statutes of the enum :class:`NamespaceStatus <NamespaceStatus>`.
"""
TRIGGER_TRANSIENT_STATUSES: list[TriggerStatus] = [
    TriggerStatus.DELETING,
    TriggerStatus.UPDATING,
    TriggerStatus.CREATING,
    TriggerStatus.LOCKING,
    TriggerStatus.UPGRADING,
]
"""
Lists transient statutes of the enum :class:`TriggerStatus <TriggerStatus>`.
"""
