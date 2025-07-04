# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ListPrivateNetworksRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class PrivateNetwork:
    id: str
    """
    Private Network ID.
    """

    name: str
    """
    Private Network name.
    """

    organization_id: str
    """
    Scaleway Organization the Private Network belongs to.
    """

    project_id: str
    """
    Scaleway Project the Private Network belongs to.
    """

    zone: Zone
    """
    Availability Zone in which the Private Network is available.
    """

    tags: List[str]
    """
    Tags of the Private Network.
    """

    subnets: List[str]
    """
    Private Network subnets CIDR.
    """

    created_at: Optional[datetime]
    """
    Date the Private Network was created.
    """

    updated_at: Optional[datetime]
    """
    Date the Private Network was last modified.
    """


@dataclass
class CreatePrivateNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name for the Private Network.
    """

    project_id: Optional[str]
    """
    Scaleway Project in which to create the Private Network.
    """

    tags: Optional[List[str]]
    """
    Tags for the Private Network.
    """

    subnets: Optional[List[str]]
    """
    Private Network subnets CIDR.
    """


@dataclass
class DeletePrivateNetworkRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetPrivateNetworkRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListPrivateNetworksRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListPrivateNetworksRequestOrderBy]
    """
    Sort order of the returned Private Networks.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Maximum number of Private Networks to return per page.
    """

    name: Optional[str]
    """
    Name to filter for. Only Private Networks with names containing this string will be returned.
    """

    tags: Optional[List[str]]
    """
    Tags to filter for. Only Private Networks with one or more matching tags will be returned.
    """

    organization_id: Optional[str]
    """
    Organization ID to filter for. Only Private Networks belonging to this Organization will be returned.
    """

    project_id: Optional[str]
    """
    Project ID to filter for. Only Private Networks belonging to this Project will be returned.
    """

    private_network_ids: Optional[List[str]]
    """
    Private Network IDs to filter for. Only Private Networks with one of these IDs will be returned.
    """

    include_regional: Optional[bool]
    """
    Defines whether to include regional Private Networks in the response.
    """


@dataclass
class ListPrivateNetworksResponse:
    private_networks: List[PrivateNetwork]

    total_count: int


@dataclass
class UpdatePrivateNetworkRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the private network.
    """

    tags: Optional[List[str]]
    """
    Tags for the Private Network.
    """

    subnets: Optional[List[str]]
    """
    Private Network subnets CIDR (deprecated).
    """
