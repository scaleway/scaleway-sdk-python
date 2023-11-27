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
from scaleway_core.utils import (
    StrEnumMeta,
)


class ListNamesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPinsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListVolumesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class NameStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    QUEUED = "queued"
    PUBLISHING = "publishing"
    FAILED = "failed"
    PUBLISHED = "published"

    def __str__(self) -> str:
        return str(self.value)


class PinDetails(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_DETAILS = "unknown_details"
    PINNING_LOOKING_FOR_PROVIDER = "pinning_looking_for_provider"
    PINNING_IN_PROGRESS = "pinning_in_progress"
    PINNING_BLOCKS_FETCHED = "pinning_blocks_fetched"
    PINNING_FETCHING_URL_DATA = "pinning_fetching_url_data"
    PINNED_OK = "pinned_ok"
    UNPINNED_OK = "unpinned_ok"
    UNPINNING_IN_PROGRESS = "unpinning_in_progress"
    FAILED_CONTAINS_BANNED_CID = "failed_contains_banned_cid"
    FAILED_PINNING = "failed_pinning"
    FAILED_PINNING_NO_PROVIDER = "failed_pinning_no_provider"
    FAILED_PINNING_BAD_CID_FORMAT = "failed_pinning_bad_cid_format"
    FAILED_PINNING_TIMEOUT = "failed_pinning_timeout"
    FAILED_PINNING_TOO_BIG_CONTENT = "failed_pinning_too_big_content"
    FAILED_PINNING_UNREACHABLE_URL = "failed_pinning_unreachable_url"
    FAILED_PINNING_BAD_URL_FORMAT = "failed_pinning_bad_url_format"
    FAILED_PINNING_NO_URL_CONTENT_LENGTH = "failed_pinning_no_url_content_length"
    FAILED_PINNING_BAD_URL_STATUS_CODE = "failed_pinning_bad_url_status_code"
    FAILED_UNPINNING = "failed_unpinning"
    CHECKING_COHERENCE = "checking_coherence"
    RESCHEDULED = "rescheduled"

    def __str__(self) -> str:
        return str(self.value)


class PinStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    QUEUED = "queued"
    PINNING = "pinning"
    FAILED = "failed"
    PINNED = "pinned"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class PinCIDMeta:
    id: Optional[str]


@dataclass
class PinCID:
    origins: List[str]

    cid: Optional[str]

    name: Optional[str]

    meta: Optional[PinCIDMeta]


@dataclass
class PinInfo:
    status_details: PinDetails

    id: Optional[str]

    url: Optional[str]

    size: Optional[int]

    progress: Optional[int]


@dataclass
class Name:
    name_id: str

    project_id: str

    tags: List[str]

    name: str

    key: str

    status: NameStatus

    value: str

    region: Region
    """
    Region to target. If none is passed will use default region from the config.
    """

    created_at: Optional[datetime]

    updated_at: Optional[datetime]


@dataclass
class Pin:
    pin_id: str

    status: PinStatus

    delegates: List[str]

    created_at: Optional[datetime]

    cid: Optional[PinCID]

    info: Optional[PinInfo]


@dataclass
class Volume:
    id: str

    project_id: str

    region: Region
    """
    Region to target. If none is passed will use default region from the config.
    """

    count_pin: int

    tags: List[str]

    name: str

    created_at: Optional[datetime]

    updated_at: Optional[datetime]

    size: Optional[int]


@dataclass
class CreatePinByCIDRequest:
    volume_id: str
    """
    Volume ID on which you want to pin your content.
    """

    cid: str
    """
    CID containing the content you want to pin.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    origins: Optional[List[str]]
    """
    Node containing the content you want to pin.
    """

    name: Optional[str]
    """
    Pin name.
    """


@dataclass
class CreatePinByURLRequest:
    volume_id: str
    """
    Volume ID on which you want to pin your content.
    """

    url: str
    """
    URL containing the content you want to pin.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Pin name.
    """


@dataclass
class CreateVolumeRequest:
    name: str
    """
    Volume name.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project ID.
    """


@dataclass
class DeletePinRequest:
    volume_id: str
    """
    Volume ID.
    """

    pin_id: str
    """
    Pin ID you want to remove from the volume.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteVolumeRequest:
    volume_id: str
    """
    Volume ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ExportKeyNameResponse:
    name_id: str

    project_id: str

    public_key: str

    private_key: str

    created_at: Optional[datetime]

    updated_at: Optional[datetime]


@dataclass
class GetPinRequest:
    volume_id: str
    """
    Volume ID.
    """

    pin_id: str
    """
    Pin ID of which you want to obtain information.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetVolumeRequest:
    volume_id: str
    """
    Volume ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class IpnsApiCreateNameRequest:
    name: str
    """
    Name for your records.
    """

    value: str
    """
    Value you want to associate with your records, CID or IPNS key.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project ID.
    """


@dataclass
class IpnsApiDeleteNameRequest:
    name_id: str
    """
    Name ID you wish to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class IpnsApiExportKeyNameRequest:
    name_id: str
    """
    Name ID whose keys you want to export.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class IpnsApiGetNameRequest:
    name_id: str
    """
    Name ID whose information you want to retrieve.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class IpnsApiImportKeyNameRequest:
    name: str
    """
    Name for your records.
    """

    private_key: str
    """
    Base64 private key.
    """

    value: str
    """
    Value you want to associate with your records, CID or IPNS key.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project ID.
    """


@dataclass
class IpnsApiListNamesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project ID.
    """

    organization_id: Optional[str]
    """
    Organization ID.
    """

    order_by: Optional[ListNamesRequestOrderBy]
    """
    Sort the order of the returned names.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Maximum number of names to return per page.
    """


@dataclass
class IpnsApiUpdateNameRequest:
    name_id: str
    """
    Name ID you wish to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    New name you want to associate with your record.
    """

    tags: Optional[List[str]]
    """
    New tags you want to associate with your record.
    """

    value: Optional[str]
    """
    Value you want to associate with your records, CID or IPNS key.
    """


@dataclass
class ListNamesResponse:
    names: List[Name]

    total_count: int


@dataclass
class ListPinsRequest:
    volume_id: str
    """
    Volume ID of which you want to list the pins.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project ID.
    """

    organization_id: Optional[str]
    """
    Organization ID.
    """

    order_by: Optional[ListPinsRequestOrderBy]
    """
    Sort order of the returned Volume.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Maximum number of volumes to return per page.
    """

    status: Optional[PinStatus]
    """
    List pins by status.
    """


@dataclass
class ListPinsResponse:
    total_count: int

    pins: List[Pin]


@dataclass
class ListVolumesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project ID, only volumes belonging to this project will be listed.
    """

    order_by: Optional[ListVolumesRequestOrderBy]
    """
    Sort the order of the returned volumes.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Maximum number of volumes to return per page.
    """


@dataclass
class ListVolumesResponse:
    volumes: List[Volume]

    total_count: int


@dataclass
class ReplacePinRequest:
    volume_id: str
    """
    Volume ID.
    """

    pin_id: str
    """
    Pin ID whose information you wish to replace.
    """

    cid: str
    """
    New CID you want to pin in place of the old one.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    New name to replace.
    """

    origins: Optional[List[str]]
    """
    Node containing the content you want to pin.
    """


@dataclass
class ReplacePinResponse:
    pin: Optional[Pin]


@dataclass
class UpdateVolumeRequest:
    volume_id: str
    """
    Volume ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Volume name.
    """

    tags: Optional[List[str]]
    """
    Tags of the volume.
    """
