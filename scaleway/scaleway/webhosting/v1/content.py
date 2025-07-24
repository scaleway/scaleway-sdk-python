# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    DomainAvailabilityStatus,
    DomainStatus,
    HostingStatus,
)

DOMAIN_AVAILABILITY_TRANSIENT_STATUSES: List[DomainAvailabilityStatus] = [
    DomainAvailabilityStatus.VALIDATING,
]
"""
Lists transient statutes of the enum :class:`DomainAvailabilityStatus <DomainAvailabilityStatus>`.
"""
DOMAIN_TRANSIENT_STATUSES: List[DomainStatus] = [
    DomainStatus.VALIDATING,
]
"""
Lists transient statutes of the enum :class:`DomainStatus <DomainStatus>`.
"""
HOSTING_TRANSIENT_STATUSES: List[HostingStatus] = [
    HostingStatus.DELIVERING,
    HostingStatus.DELETING,
    HostingStatus.MIGRATING,
    HostingStatus.UPDATING,
]
"""
Lists transient statutes of the enum :class:`HostingStatus <HostingStatus>`.
"""
