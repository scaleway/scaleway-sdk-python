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
    Image.
    """

    id: str
    """
    UUID of the image.
    """

    name: str
    """
    Name of the image, it must be unique within the namespace.
    """

    namespace_id: str
    """
    UUID of the namespace the image belongs to.
    """

    status: ImageStatus
    """
    Status of the image.
    """

    status_message: Optional[str]
    """
    Details of the image status.
    """

    visibility: ImageVisibility
    """
    Set to `public` to allow the image to be pulled without authentication. Else, set to  `private`. Set to `inherit` to keep the same visibility configuration as the namespace.
    """

    size: int
    """
    Image size in bytes, calculated from the size of image layers.
    Image size in bytes, calculated from the size of image layers. One layer used in two tags of the same image is counted once but one layer used in two images is counted twice.
    """

    created_at: Optional[datetime]
    """
    Date and time of image creation.
    """

    updated_at: Optional[datetime]
    """
    Date and time of last update.
    """

    tags: List[str]
    """
    List of docker tags of the image.
    """


@dataclass
class ListImagesResponse:
    """
    List images response.
    """

    images: List[Image]
    """
    Paginated list of images that match the selected filters.
    """

    total_count: int
    """
    Total number of images that match the selected filters.
    """


@dataclass
class ListNamespacesResponse:
    """
    List namespaces response.
    """

    namespaces: List[Namespace]
    """
    Paginated list of namespaces that match the selected filters.
    """

    total_count: int
    """
    Total number of namespaces that match the selected filters.
    """


@dataclass
class ListTagsResponse:
    """
    List tags response.
    """

    tags: List[Tag]
    """
    Paginated list of tags that match the selected filters.
    """

    total_count: int
    """
    Total number of tags that match the selected filters.
    """


@dataclass
class Namespace:
    """
    Namespace.
    """

    id: str
    """
    UUID of the namespace.
    """

    name: str
    """
    Name of the namespace, unique in a region accross all organizations.
    """

    description: str
    """
    Description of the namespace.
    """

    organization_id: str
    """
    Owner of the namespace.
    """

    project_id: str
    """
    Project of the namespace.
    """

    status: NamespaceStatus
    """
    Namespace status.
    """

    status_message: str
    """
    Namespace status details.
    """

    endpoint: str
    """
    Endpoint reachable by docker.
    """

    is_public: bool
    """
    Defines whether or not namespace is public.
    """

    size: int
    """
    Total size of the namespace, calculated as the sum of the size of all images in the namespace.
    """

    created_at: Optional[datetime]
    """
    Date and time of creation.
    """

    updated_at: Optional[datetime]
    """
    Date and time of last update.
    """

    image_count: int
    """
    Number of images in the namespace.
    """

    region: Region
    """
    Region the namespace belongs to.
    """


@dataclass
class Tag:
    """
    Tag.
    """

    id: str
    """
    UUID of the tag.
    """

    name: str
    """
    Tag name, unique to an image.
    """

    image_id: str
    """
    Image ID the of the image the tag belongs to.
    """

    status: TagStatus
    """
    Tag status.
    """

    digest: str
    """
    Hash of the tag content. Several tags of a same image may have the same digest.
    """

    created_at: Optional[datetime]
    """
    Date and time of creation.
    """

    updated_at: Optional[datetime]
    """
    Date and time of last update.
    """


@dataclass
class ListNamespacesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    A positive integer to choose the page to display.
    """

    page_size: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to display.
    """

    order_by: Optional[ListNamespacesRequestOrderBy]
    """
    Criteria to use when ordering namespace listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID.
    """

    project_id: Optional[str]
    """
    Filter by Project ID.
    """

    name: Optional[str]
    """
    Filter by the namespace name (exact match).
    """


@dataclass
class GetNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: str
    """
    UUID of the namespace.
    """


@dataclass
class CreateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the namespace.
    """

    description: str
    """
    Description of the namespace.
    """

    organization_id: Optional[str]
    """
    Namespace owner (deprecated).
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Project ID on which the namespace will be created.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """

    is_public: bool
    """
    Defines whether or not namespace is public.
    """


@dataclass
class UpdateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: str
    """
    ID of the namespace to update.
    """

    description: Optional[str]
    """
    Namespace description.
    """

    is_public: Optional[bool]
    """
    Defines whether or not the namespace is public.
    """


@dataclass
class DeleteNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: str
    """
    UUID of the namespace.
    """


@dataclass
class ListImagesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    A positive integer to choose the page to display.
    """

    page_size: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to display.
    """

    order_by: Optional[ListImagesRequestOrderBy]
    """
    Criteria to use when ordering image listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
    """

    namespace_id: Optional[str]
    """
    Filter by the namespace ID.
    """

    name: Optional[str]
    """
    Filter by the image name (exact match).
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID.
    """

    project_id: Optional[str]
    """
    Filter by Project ID.
    """


@dataclass
class GetImageRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    image_id: str
    """
    UUID of the image.
    """


@dataclass
class UpdateImageRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    image_id: str
    """
    ID of the image to update.
    """

    visibility: ImageVisibility
    """
    Set to `public` to allow the image to be pulled without authentication. Else, set to  `private`. Set to `inherit` to keep the same visibility configuration as the namespace.
    """


@dataclass
class DeleteImageRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    image_id: str
    """
    UUID of the image.
    """


@dataclass
class ListTagsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    image_id: str
    """
    UUID of the image.
    """

    page: Optional[int]
    """
    A positive integer to choose the page to display.
    """

    page_size: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to display.
    """

    order_by: Optional[ListTagsRequestOrderBy]
    """
    Criteria to use when ordering tag listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
    """

    name: Optional[str]
    """
    Filter by the tag name (exact match).
    """


@dataclass
class GetTagRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    tag_id: str
    """
    UUID of the tag.
    """


@dataclass
class DeleteTagRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    tag_id: str
    """
    UUID of the tag.
    """

    force: Optional[bool]
    """
    If two tags share the same digest the deletion will fail unless this parameter is set to true (deprecated).
    :deprecated
    """
