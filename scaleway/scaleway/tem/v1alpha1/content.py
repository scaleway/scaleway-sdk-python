# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    DomainStatus,
    EmailStatus,
)

DOMAIN_TRANSIENT_STATUSES: List[DomainStatus] = [
    DomainStatus.PENDING,
    DomainStatus.AUTOCONFIGURING,
]
"""
Lists transient statutes of the enum :class:`DomainStatus <DomainStatus>`.
"""
EMAIL_TRANSIENT_STATUSES: List[EmailStatus] = [
    EmailStatus.NEW,
    EmailStatus.SENDING,
]
"""
Lists transient statutes of the enum :class:`EmailStatus <EmailStatus>`.
"""
