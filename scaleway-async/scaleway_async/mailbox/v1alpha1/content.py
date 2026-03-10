# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    DomainRecordStatus,
    DomainStatus,
    MailboxStatus,
)

DOMAIN_RECORD_TRANSIENT_STATUSES: list[DomainRecordStatus] = [
    DomainRecordStatus.VALIDATING,
]
"""
Lists transient statutes of the enum :class:`DomainRecordStatus <DomainRecordStatus>`.
"""
DOMAIN_TRANSIENT_STATUSES: list[DomainStatus] = [
    DomainStatus.CREATING,
    DomainStatus.VALIDATING,
    DomainStatus.PROVISIONING,
    DomainStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`DomainStatus <DomainStatus>`.
"""
MAILBOX_TRANSIENT_STATUSES: list[MailboxStatus] = [
    MailboxStatus.CREATING,
    MailboxStatus.WAITING_PAYMENT,
    MailboxStatus.WAITING_DOMAIN,
    MailboxStatus.RENEWING,
    MailboxStatus.DELETING,
    MailboxStatus.RESTORING,
]
"""
Lists transient statutes of the enum :class:`MailboxStatus <MailboxStatus>`.
"""
