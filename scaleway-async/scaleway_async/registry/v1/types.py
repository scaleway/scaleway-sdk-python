# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ImageStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class ImageVisibility(str, Enum, metaclass=StrEnumMeta):
    VISIBILITY_UNKNOWN = "visibility_unknown"
    INHERIT = "inherit"
    PUBLIC = "public"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)


class ListImagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListNamespacesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    DESCRIPTION_ASC = "description_asc"
    DESCRIPTION_DESC = "description_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListTagsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class NamespaceStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class TagStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Image:
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

    visibility: ImageVisibility
    """
    Set to `public` to allow the image to be pulled without authentication. Else, set to  `private`. Set to `inherit` to keep the same visibility configuration as the namespace.
    """

    size: int
    """
    Image size in bytes, calculated from the size of image layers. One layer used in two tags of the same image is counted once but one layer used in two images is counted twice.
    """

    tags: list[str]
    """
    List of docker tags of the image.
    """

    status_message: Optional[str] = None
    """
    Details of the image status.
    """

    created_at: Optional[datetime] = None
    """
    Date and time of image creation.
    """

    updated_at: Optional[datetime] = None
    """
    Date and time of last update.
    """


@dataclass
class Namespace:
    id: str
    """
    UUID of the namespace.
    """

    name: str
    """
    Name of the namespace, unique in a region across all organizations.
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

    image_count: int
    """
    Number of images in the namespace.
    """

    region: ScwRegion
    """
    Region the namespace belongs to.
    """

    created_at: Optional[datetime] = None
    """
    Date and time of creation.
    """

    updated_at: Optional[datetime] = None
    """
    Date and time of last update.
    """


@dataclass
class Tag:
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

    created_at: Optional[datetime] = None
    """
    Date and time of creation.
    """

    updated_at: Optional[datetime] = None
    """
    Date and time of last update.
    """


@dataclass
class CreateNamespaceRequest:
    description: str
    """
    Description of the namespace.
    """

    is_public: bool
    """
    Defines whether or not namespace is public.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the namespace.
    """

    project_id: Optional[str] = None

    organization_id: Optional[str] = None


@dataclass
class DeleteImageRequest:
    image_id: str
    """
    UUID of the image.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteNamespaceRequest:
    namespace_id: str
    """
    UUID of the namespace.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteTagRequest:
    tag_id: str
    """
    UUID of the tag.
    """

    force: bool
    """
    If two tags share the same digest the deletion will fail unless this parameter is set to true (deprecated).
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetImageRequest:
    image_id: str
    """
    UUID of the image.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetNamespaceRequest:
    namespace_id: str
    """
    UUID of the namespace.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetTagRequest:
    tag_id: str
    """
    UUID of the tag.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListImagesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    A positive integer to choose the page to display.
    """

    page_size: Optional[int] = 0
    """
    A positive integer lower or equal to 100 to select the number of items to display.
    """

    order_by: Optional[ListImagesRequestOrderBy] = (
        ListImagesRequestOrderBy.CREATED_AT_ASC
    )
    """
    Criteria to use when ordering image listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
    """

    namespace_id: Optional[str] = None
    """
    Filter by the namespace ID.
    """

    name: Optional[str] = None
    """
    Filter by the image name (exact match).
    """

    organization_id: Optional[str] = None
    """
    Filter by Organization ID.
    """

    project_id: Optional[str] = None
    """
    Filter by Project ID.
    """


@dataclass
class ListImagesResponse:
    images: list[Image]
    """
    Paginated list of images that match the selected filters.
    """

    total_count: int
    """
    Total number of images that match the selected filters.
    """


@dataclass
class ListNamespacesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    A positive integer to choose the page to display.
    """

    page_size: Optional[int] = 0
    """
    A positive integer lower or equal to 100 to select the number of items to display.
    """

    order_by: Optional[ListNamespacesRequestOrderBy] = (
        ListNamespacesRequestOrderBy.CREATED_AT_ASC
    )
    """
    Criteria to use when ordering namespace listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
    """

    organization_id: Optional[str] = None
    """
    Filter by Organization ID.
    """

    project_id: Optional[str] = None
    """
    Filter by Project ID.
    """

    name: Optional[str] = None
    """
    Filter by the namespace name (exact match).
    """


@dataclass
class ListNamespacesResponse:
    namespaces: list[Namespace]
    """
    Paginated list of namespaces that match the selected filters.
    """

    total_count: int
    """
    Total number of namespaces that match the selected filters.
    """


@dataclass
class ListTagsRequest:
    image_id: str
    """
    UUID of the image.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    A positive integer to choose the page to display.
    """

    page_size: Optional[int] = 0
    """
    A positive integer lower or equal to 100 to select the number of items to display.
    """

    order_by: Optional[ListTagsRequestOrderBy] = ListTagsRequestOrderBy.CREATED_AT_ASC
    """
    Criteria to use when ordering tag listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
    """

    name: Optional[str] = None
    """
    Filter by the tag name (exact match).
    """


@dataclass
class ListTagsResponse:
    tags: list[Tag]
    """
    Paginated list of tags that match the selected filters.
    """

    total_count: int
    """
    Total number of tags that match the selected filters.
    """


@dataclass
class UpdateImageRequest:
    image_id: str
    """
    ID of the image to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    visibility: Optional[ImageVisibility] = ImageVisibility.VISIBILITY_UNKNOWN
    """
    Set to `public` to allow the image to be pulled without authentication. Else, set to  `private`. Set to `inherit` to keep the same visibility configuration as the namespace.
    """


@dataclass
class UpdateNamespaceRequest:
    namespace_id: str
    """
    ID of the namespace to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    description: Optional[str] = None
    """
    Namespace description.
    """

    is_public: Optional[bool] = False
    """
    Defines whether or not the namespace is public.
    """
