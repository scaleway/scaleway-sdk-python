# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    BackupStatus,
    DomainAvailabilityStatus,
    DomainStatus,
    HostingStatus,
)

BACKUP_TRANSIENT_STATUSES: list[BackupStatus] = [
    BackupStatus.RESTORING,
]
"""
Lists transient statutes of the enum :class:`BackupStatus <BackupStatus>`.
"""
DOMAIN_AVAILABILITY_TRANSIENT_STATUSES: list[DomainAvailabilityStatus] = [
    DomainAvailabilityStatus.VALIDATING,
]
"""
Lists transient statutes of the enum :class:`DomainAvailabilityStatus <DomainAvailabilityStatus>`.
"""
DOMAIN_TRANSIENT_STATUSES: list[DomainStatus] = [
    DomainStatus.VALIDATING,
]
"""
Lists transient statutes of the enum :class:`DomainStatus <DomainStatus>`.
"""
HOSTING_TRANSIENT_STATUSES: list[HostingStatus] = [
    HostingStatus.DELIVERING,
    HostingStatus.DELETING,
    HostingStatus.MIGRATING,
    HostingStatus.UPDATING,
]
"""
Lists transient statutes of the enum :class:`HostingStatus <HostingStatus>`.
"""
