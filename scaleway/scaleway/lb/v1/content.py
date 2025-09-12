# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    CertificateStatus,
    InstanceStatus,
    LbStatus,
    PrivateNetworkStatus,
)

CERTIFICATE_TRANSIENT_STATUSES: list[CertificateStatus] = [
    CertificateStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`CertificateStatus <CertificateStatus>`.
"""
INSTANCE_TRANSIENT_STATUSES: list[InstanceStatus] = [
    InstanceStatus.PENDING,
    InstanceStatus.MIGRATING,
]
"""
Lists transient statutes of the enum :class:`InstanceStatus <InstanceStatus>`.
"""
LB_TRANSIENT_STATUSES: list[LbStatus] = [
    LbStatus.PENDING,
    LbStatus.MIGRATING,
    LbStatus.TO_CREATE,
    LbStatus.CREATING,
    LbStatus.TO_DELETE,
    LbStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`LbStatus <LbStatus>`.
"""
PRIVATE_NETWORK_TRANSIENT_STATUSES: list[PrivateNetworkStatus] = [
    PrivateNetworkStatus.PENDING,
]
"""
Lists transient statutes of the enum :class:`PrivateNetworkStatus <PrivateNetworkStatus>`.
"""
