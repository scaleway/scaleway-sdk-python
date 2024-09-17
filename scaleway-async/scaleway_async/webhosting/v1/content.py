# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    HostingStatus,
    HostingSummaryStatus,
)

HOSTING_TRANSIENT_STATUSES: List[HostingStatus] = [
    HostingStatus.DELIVERING,
    HostingStatus.DELETING,
    HostingStatus.MIGRATING,
]
"""
Lists transient statutes of the enum :class:`HostingStatus <HostingStatus>`.
"""
HOSTING_SUMMARY_TRANSIENT_STATUSES: List[HostingSummaryStatus] = [
    HostingSummaryStatus.DELIVERING,
    HostingSummaryStatus.DELETING,
    HostingSummaryStatus.MIGRATING,
]
"""
Lists transient statutes of the enum :class:`HostingSummaryStatus <HostingSummaryStatus>`.
"""
