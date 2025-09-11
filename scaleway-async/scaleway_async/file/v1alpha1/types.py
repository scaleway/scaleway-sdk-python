# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class AttachmentResourceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_RESOURCE_TYPE = "unknown_resource_type"
    INSTANCE_SERVER = "instance_server"

    def __str__(self) -> str:
        return str(self.value)


class FileSystemStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    AVAILABLE = "available"
    ERROR = "error"
    CREATING = "creating"
    UPDATING = "updating"

    def __str__(self) -> str:
        return str(self.value)


class ListFileSystemsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Attachment:
    """
    Represents an attachment between a filesystem and a resource.
    """

    id: str
    """
    UUID of the attachment.
    """

    filesystem_id: str
    """
    UUID of the filesystem.
    """

    resource_id: str
    """
    UUID of the attached resource.
    """

    resource_type: AttachmentResourceType
    """
    The type of the attached resource.
    """

    zone: Optional[ScwZone] = None
    """
    The zone where the resource is located.
    """


@dataclass
class FileSystem:
    """
    Represents a filesystem resource and its properties.
    """

    id: str
    """
    UUID of the filesystem.
    """

    name: str
    """
    Name of the filesystem.
    """

    size: int
    """
    Filesystem size in bytes.
    """

    status: FileSystemStatus
    """
    Current status of the filesystem (e.g. creating, available, ...).
    """

    project_id: str
    """
    UUID of the project to which the filesystem belongs.
    """

    organization_id: str
    """
    UUID of the organization to which the filesystem belongs.
    """

    tags: list[str]
    """
    List of tags assigned to the filesystem.
    """

    number_of_attachments: int
    """
    The current number of attachments (mounts) that the filesystem has.
    """

    region: ScwRegion
    """
    Region where the filesystem is located.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the filesystem.
    """

    updated_at: Optional[datetime] = None
    """
    Last update date of the properties of the filesystem.
    """


@dataclass
class CreateFileSystemRequest:
    """
    Request to create a new filesystem.
    """

    name: str
    """
    Name of the filesystem.
    """

    size: int
    """
    Must be compliant with the minimum (100 GB) and maximum (10 TB) allowed size.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    UUID of the project the filesystem belongs to.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List of tags assigned to the filesystem.
    """


@dataclass
class DeleteFileSystemRequest:
    """
    Request to delete a specific filesystem.
    """

    filesystem_id: str
    """
    UUID of the filesystem.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetFileSystemRequest:
    """
    Request to retrieve a specific filesystem.
    """

    filesystem_id: str
    """
    UUID of the filesystem.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListAttachmentsRequest:
    """
    Request to list filesystem attachments with filtering and pagination options.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    filesystem_id: Optional[str] = None
    """
    UUID of the File Storage volume.
    """

    resource_id: Optional[str] = None
    """
    Filter by resource ID.
    """

    resource_type: Optional[AttachmentResourceType] = (
        AttachmentResourceType.UNKNOWN_RESOURCE_TYPE
    )
    """
    Filter by resource type.
    """

    zone: Optional[ScwZone] = None
    """
    Filter by resource zone.
    """

    page: Optional[int] = 0
    """
    Page number (starting at 1).
    """

    page_size: Optional[int] = 0
    """
    Number of entries per page (default: 20, max: 100).
    """


@dataclass
class ListAttachmentsResponse:
    """
    Response containing a list of filesystem attachments and total count.
    """

    attachments: list[Attachment]
    """
    List of filesystem attachments matching the request criteria.
    """

    total_count: int
    """
    Total number of filesystem attachments matching the criteria.
    """


@dataclass
class ListFileSystemsRequest:
    """
    Request to list filesystems with filtering and pagination options.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListFileSystemsRequestOrderBy] = (
        ListFileSystemsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Criteria to use when ordering the list.
    """

    project_id: Optional[str] = None
    """
    Filter by project ID.
    """

    organization_id: Optional[str] = None
    """
    Filter by organization ID.
    """

    page: Optional[int] = 0
    """
    Page number (starting at 1).
    """

    page_size: Optional[int] = 0
    """
    Number of entries per page (default: 20, max: 100).
    """

    name: Optional[str] = None
    """
    Filter the returned filesystems by their names.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Filter by tags. Only filesystems with one or more matching tags will be returned.
    """


@dataclass
class ListFileSystemsResponse:
    """
    Response containing a list of filesystems and total count.
    """

    filesystems: list[FileSystem]
    """
    List of filesystems matching the request criteria.
    """

    total_count: int
    """
    Total number of filesystems matching the criteria.
    """


@dataclass
class UpdateFileSystemRequest:
    """
    Request to update a specific filesystem.
    """

    filesystem_id: str
    """
    UUID of the filesystem.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    When defined, is the new name of the filesystem.
    """

    size: Optional[int] = 0
    """
    Size in bytes, with a granularity of 100 GB (10^11 bytes).
Must be compliant with the minimum (100 GB) and maximum (10 TB) allowed size.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List of tags assigned to the filesystem.
    """
