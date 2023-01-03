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


class ListPrivateNetworksRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class ListPrivateNetworksResponse:
    private_networks: List[PrivateNetwork]

    total_count: int


@dataclass
class PrivateNetwork:
    """
    Private network
    """

    id: str
    """
    The private network ID
    """

    name: str
    """
    The private network name
    """

    organization_id: str
    """
    The private network organization
    """

    project_id: str
    """
    The private network project ID
    """

    zone: Zone
    """
    The zone in which the private network is available
    """

    tags: List[str]
    """
    The private network tags
    """

    created_at: Optional[datetime]
    """
    The private network creation date
    """

    updated_at: Optional[datetime]
    """
    The last private network modification date
    """

    subnets: List[str]
    """
    Private network subnets CIDR
    """


@dataclass
class ListPrivateNetworksRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    order_by: Optional[ListPrivateNetworksRequestOrderBy]
    """
    The sort order of the returned private networks
    """

    page: Optional[int]
    """
    The page number for the returned private networks
    """

    page_size: Optional[int]
    """
    The maximum number of private networks per page
    """

    name: Optional[str]
    """
    Filter private networks with names containing this string
    """

    tags: Optional[List[str]]
    """
    Filter private networks with one or more matching tags
    """

    organization_id: Optional[str]
    """
    The organization ID on which to filter the returned private networks
    """

    project_id: Optional[str]
    """
    The project ID on which to filter the returned private networks
    """

    private_network_ids: Optional[List[str]]
    """
    The PrivateNetwork IDs on which to filter the returned private networks
    """


@dataclass
class CreatePrivateNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    name: Optional[str]
    """
    The name of the private network
    """

    project_id: Optional[str]
    """
    The project ID of the private network
    """

    tags: Optional[List[str]]
    """
    The private networks tags
    """

    subnets: Optional[List[str]]
    """
    Private network subnets CIDR
    """


@dataclass
class GetPrivateNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    private_network_id: str
    """
    The private network id
    """


@dataclass
class UpdatePrivateNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    private_network_id: str
    """
    The private network ID
    """

    name: Optional[str]
    """
    The name of the private network
    """

    tags: Optional[List[str]]
    """
    The private networks tags
    """

    subnets: Optional[List[str]]
    """
    Private network subnets CIDR
    """


@dataclass
class DeletePrivateNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    private_network_id: str
    """
    The private network ID
    """
