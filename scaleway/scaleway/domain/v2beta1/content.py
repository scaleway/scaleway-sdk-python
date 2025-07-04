# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    DNSZoneStatus,
    DomainFeatureStatus,
    DomainRegistrationStatusTransferStatus,
    DomainStatus,
    HostStatus,
    SSLCertificateStatus,
    TaskStatus,
)

DNS_ZONE_TRANSIENT_STATUSES: List[DNSZoneStatus] = [
    DNSZoneStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`DNSZoneStatus <DNSZoneStatus>`.
"""
DOMAIN_FEATURE_TRANSIENT_STATUSES: List[DomainFeatureStatus] = [
    DomainFeatureStatus.ENABLING,
    DomainFeatureStatus.DISABLING,
]
"""
Lists transient statutes of the enum :class:`DomainFeatureStatus <DomainFeatureStatus>`.
"""
DOMAIN_REGISTRATION_STATUS_TRANSFER_TRANSIENT_STATUSES: List[
    DomainRegistrationStatusTransferStatus
] = [
    DomainRegistrationStatusTransferStatus.PENDING,
    DomainRegistrationStatusTransferStatus.PROCESSING,
]
"""
Lists transient statutes of the enum :class:`DomainRegistrationStatusTransferStatus <DomainRegistrationStatusTransferStatus>`.
"""
DOMAIN_TRANSIENT_STATUSES: List[DomainStatus] = [
    DomainStatus.CREATING,
    DomainStatus.RENEWING,
    DomainStatus.XFERING,
    DomainStatus.EXPIRING,
    DomainStatus.UPDATING,
    DomainStatus.CHECKING,
    DomainStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`DomainStatus <DomainStatus>`.
"""
HOST_TRANSIENT_STATUSES: List[HostStatus] = [
    HostStatus.UPDATING,
    HostStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`HostStatus <HostStatus>`.
"""
SSL_CERTIFICATE_TRANSIENT_STATUSES: List[SSLCertificateStatus] = [
    SSLCertificateStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`SSLCertificateStatus <SSLCertificateStatus>`.
"""
TASK_TRANSIENT_STATUSES: List[TaskStatus] = [
    TaskStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`TaskStatus <TaskStatus>`.
"""
