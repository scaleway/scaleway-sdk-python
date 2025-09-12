# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    CronStatus,
    DomainStatus,
    FunctionStatus,
    NamespaceStatus,
    TokenStatus,
    TriggerStatus,
)

CRON_TRANSIENT_STATUSES: list[CronStatus] = [
    CronStatus.DELETING,
    CronStatus.CREATING,
    CronStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`CronStatus <CronStatus>`.
"""
DOMAIN_TRANSIENT_STATUSES: list[DomainStatus] = [
    DomainStatus.DELETING,
    DomainStatus.CREATING,
    DomainStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`DomainStatus <DomainStatus>`.
"""
FUNCTION_TRANSIENT_STATUSES: list[FunctionStatus] = [
    FunctionStatus.DELETING,
    FunctionStatus.CREATING,
    FunctionStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`FunctionStatus <FunctionStatus>`.
"""
NAMESPACE_TRANSIENT_STATUSES: list[NamespaceStatus] = [
    NamespaceStatus.DELETING,
    NamespaceStatus.CREATING,
    NamespaceStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`NamespaceStatus <NamespaceStatus>`.
"""
TOKEN_TRANSIENT_STATUSES: list[TokenStatus] = [
    TokenStatus.DELETING,
    TokenStatus.CREATING,
]
"""
Lists transient statutes of the enum :class:`TokenStatus <TokenStatus>`.
"""
TRIGGER_TRANSIENT_STATUSES: list[TriggerStatus] = [
    TriggerStatus.DELETING,
    TriggerStatus.CREATING,
    TriggerStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`TriggerStatus <TriggerStatus>`.
"""
