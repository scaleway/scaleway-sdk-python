# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Region,
)


class ImageStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class ImageVisibility(str, Enum):
    VISIBILITY_UNKNOWN = "visibility_unknown"
    INHERIT = "inherit"
    PUBLIC = "public"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)


class ListImagesRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListNamespacesRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    DESCRIPTION_ASC = "description_asc"
    DESCRIPTION_DESC = "description_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListTagsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class NamespaceStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class TagStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Image:
    """
    Image
    """

    id: str
    """
    The unique ID of the Image
    """

    name: str
    """
    The Image name, unique in a namespace
    """

    namespace_id: str
    """
    The unique ID of the Namespace the image belongs to
    """

    status: ImageStatus
    """
    The status of the image
    """

    status_message: Optional[str]
    """
    Details of the image status
    """

    visibility: ImageVisibility
    """
    A `public` image is pullable from internet without authentication, opposed to a `private` image. `inherit` will use the namespace `is_public` parameter
    """

    size: int
    """
    Image size in bytes, calculated from the size of image layers. One layer used in two tags of the same image is counted once but one layer used in two images is counted twice.
    """

    created_at: Optional[datetime]
    """
    Creation date
    """

    updated_at: Optional[datetime]
    """
    Last modification date, from the user or the service
    """

    tags: List[str]
    """
    List of docker tags of the image
    """


@dataclass
class ListImagesResponse:
    """
    List images response
    """

    images: List[Image]
    """
    Paginated list of images matching filters
    """

    total_count: int
    """
    Total number of images matching filters
    """


@dataclass
class ListNamespacesResponse:
    """
    List namespaces response
    """

    namespaces: List[Namespace]
    """
    Paginated list of namespaces matching filters
    """

    total_count: int
    """
    Total number of namespaces matching filters
    """


@dataclass
class ListTagsResponse:
    """
    List tags response
    """

    tags: List[Tag]
    """
    Paginated list of tags matching filters
    """

    total_count: int
    """
    Total number of tags matching filters
    """


@dataclass
class Namespace:
    """
    Namespace
    """

    id: str
    """
    The unique ID of the namespace
    """

    name: str
    """
    The name of the namespace, unique in a region accross all organizations
    """

    description: str
    """
    Description of the namespace
    """

    organization_id: str
    """
    Owner of the namespace
    """

    project_id: str
    """
    Project of the namespace
    """

    status: NamespaceStatus
    """
    Namespace status
    """

    status_message: str
    """
    Namespace status details
    """

    endpoint: str
    """
    Endpoint reachable by docker
    """

    is_public: bool
    """
    Namespace visibility policy
    """

    size: int
    """
    Total size of the namespace, calculated as the sum of the size of all images in the namespace
    """

    created_at: Optional[datetime]
    """
    Creation date
    """

    updated_at: Optional[datetime]
    """
    Last modification date, from the user or the service
    """

    image_count: int
    """
    Number of images in the namespace
    """

    region: Region
    """
    Region the namespace belongs to
    """


@dataclass
class Tag:
    """
    Tag
    """

    id: str
    """
    The unique ID of the tag
    """

    name: str
    """
    Tag name, unique for an image
    """

    image_id: str
    """
    Image ID this tag belongs to
    """

    status: TagStatus
    """
    Tag status
    """

    digest: str
    """
    Hash of the tag actual content. Several tags of a same image may have the same digest
    """

    created_at: Optional[datetime]
    """
    Creation date
    """

    updated_at: Optional[datetime]
    """
    Last modification date, from the user or the service
    """


@dataclass
class ListNamespacesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    page: Optional[int]
    """
    A positive integer to choose the page to display
    """

    page_size: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to display
    """

    order_by: Optional[ListNamespacesRequestOrderBy]
    """
    Field by which to order the display of Images
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID
    """

    project_id: Optional[str]
    """
    Filter by Project ID
    """

    name: Optional[str]
    """
    Filter by the namespace name (exact match)
    """


@dataclass
class GetNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    namespace_id: str
    """
    The unique ID of the Namespace
    """


@dataclass
class CreateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    name: Optional[str]
    """
    Define a namespace name
    """

    description: str
    """
    Define a description
    """

    organization_id: Optional[str]
    """
    Assign the namespace owner (deprecated).
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Assign the namespace to a project ID.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """

    is_public: bool
    """
    Define the default visibility policy
    """


@dataclass
class UpdateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    namespace_id: str
    """
    Namespace ID to update
    """

    description: Optional[str]
    """
    Define a description
    """

    is_public: Optional[bool]
    """
    Define the default visibility policy
    """


@dataclass
class DeleteNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    namespace_id: str
    """
    The unique ID of the Namespace
    """


@dataclass
class ListImagesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    page: Optional[int]
    """
    A positive integer to choose the page to display
    """

    page_size: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to display
    """

    order_by: Optional[ListImagesRequestOrderBy]
    """
    Field by which to order the display of Images
    """

    namespace_id: Optional[str]
    """
    Filter by the Namespace ID
    """

    name: Optional[str]
    """
    Filter by the Image name (exact match)
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID
    """

    project_id: Optional[str]
    """
    Filter by Project ID
    """


@dataclass
class GetImageRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    image_id: str
    """
    The unique ID of the Image
    """


@dataclass
class UpdateImageRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    image_id: str
    """
    Image ID to update
    """

    visibility: ImageVisibility
    """
    A `public` image is pullable from internet without authentication, opposed to a `private` image. `inherit` will use the namespace `is_public` parameter
    """


@dataclass
class DeleteImageRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    image_id: str
    """
    The unique ID of the Image
    """


@dataclass
class ListTagsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    image_id: str
    """
    The unique ID of the image
    """

    page: Optional[int]
    """
    A positive integer to choose the page to display
    """

    page_size: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to display
    """

    order_by: Optional[ListTagsRequestOrderBy]
    """
    Field by which to order the display of Images
    """

    name: Optional[str]
    """
    Filter by the tag name (exact match)
    """


@dataclass
class GetTagRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    tag_id: str
    """
    The unique ID of the Tag
    """


@dataclass
class DeleteTagRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    tag_id: str
    """
    The unique ID of the tag
    """

    force: bool
    """
    If two tags share the same digest the deletion will fail unless this parameter is set to true
    """
