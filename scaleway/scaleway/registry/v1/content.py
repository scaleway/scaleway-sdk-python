# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    ImageStatus,
    NamespaceStatus,
    TagStatus,
)

IMAGE_TRANSIENT_STATUSES: List[ImageStatus] = [
    ImageStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`ImageStatus <ImageStatus>`.
"""
NAMESPACE_TRANSIENT_STATUSES: List[NamespaceStatus] = [
    NamespaceStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`NamespaceStatus <NamespaceStatus>`.
"""
TAG_TRANSIENT_STATUSES: List[TagStatus] = [
    TagStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`TagStatus <TagStatus>`.
"""
