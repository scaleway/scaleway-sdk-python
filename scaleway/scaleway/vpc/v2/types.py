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


class ListPrivateNetworksRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListVPCsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class AddSubnetsResponse:
    subnets: List[str]


@dataclass
class DeleteSubnetsResponse:
    subnets: List[str]


@dataclass
class ListPrivateNetworksResponse:
    private_networks: List[PrivateNetwork]

    total_count: int


@dataclass
class ListVPCsResponse:
    vpcs: List[VPC]

    total_count: int


@dataclass
class PrivateNetwork:
    """
    Private network.
    """

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

    region: Region
    """
    Region in which the Private Network is available.
    """

    tags: List[str]
    """
    Tags of the Private Network.
    """

    created_at: Optional[datetime]
    """
    Date the Private Network was created.
    """

    updated_at: Optional[datetime]
    """
    Date the Private Network was last modified.
    """

    subnets: List[Subnet]
    """
    Private Network subnets.
    """

    vpc_id: str
    """
    VPC the Private Network belongs to.
    """


@dataclass
class SetSubnetsResponse:
    subnets: List[str]


@dataclass
class Subnet:
    """
    Subnet.
    """

    id: str
    """
    ID of the subnet.
    """

    created_at: Optional[datetime]
    """
    Subnet creation date.
    """

    updated_at: Optional[datetime]
    """
    Subnet last modification date.
    """

    subnet: str
    """
    Subnet CIDR.
    """


@dataclass
class VPC:
    """
    Vpc.
    """

    id: str
    """
    VPC ID.
    """

    name: str
    """
    VPC name.
    """

    organization_id: str
    """
    Scaleway Organization the VPC belongs to.
    """

    project_id: str
    """
    Scaleway Project the VPC belongs to.
    """

    region: Region
    """
    Region of the VPC.
    """

    tags: List[str]
    """
    Tags for the VPC.
    """

    is_default: bool
    """
    Defines whether the VPC is the default one for its Project.
    """

    created_at: Optional[datetime]
    """
    Date the VPC was created.
    """

    updated_at: Optional[datetime]
    """
    Date the VPC was last modified.
    """

    private_network_count: int
    """
    Number of Private Networks within this VPC.
    """


@dataclass
class ListVPCsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListVPCsRequestOrderBy]
    """
    Sort order of the returned VPCs.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Maximum number of VPCs to return per page.
    """

    name: Optional[str]
    """
    Name to filter for. Only VPCs with names containing this string will be returned.
    """

    tags: Optional[List[str]]
    """
    Tags to filter for. Only VPCs with one more more matching tags will be returned.
    """

    organization_id: Optional[str]
    """
    Organization ID to filter for. Only VPCs belonging to this Organization will be returned.
    """

    project_id: Optional[str]
    """
    Project ID to filter for. Only VPCs belonging to this Project will be returned.
    """

    is_default: Optional[bool]
    """
    Defines whether to filter only for VPCs which are the default one for their Project.
    """


@dataclass
class CreateVPCRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name for the VPC.
    """

    default_private_network_name: str
    """
    Name for the VPC's associated default Private Network.
    """

    project_id: Optional[str]
    """
    Scaleway Project in which to create the VPC.
    """

    tags: Optional[List[str]]
    """
    Tags for the VPC.
    """


@dataclass
class GetVPCRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    vpc_id: str
    """
    VPC ID.
    """


@dataclass
class UpdateVPCRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    vpc_id: str
    """
    VPC ID.
    """

    name: Optional[str]
    """
    Name for the VPC.
    """

    tags: Optional[List[str]]
    """
    Tags for the VPC.
    """


@dataclass
class DeleteVPCRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    vpc_id: str
    """
    VPC ID.
    """


@dataclass
class ListPrivateNetworksRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
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

    vpc_id: Optional[str]
    """
    VPC ID to filter for. Only Private Networks belonging to this VPC will be returned.
    """


@dataclass
class CreatePrivateNetworkRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
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

    vpc_id: Optional[str]
    """
    VPC in which to create the Private Network.
    """


@dataclass
class GetPrivateNetworkRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    private_network_id: str
    """
    Private Network ID.
    """


@dataclass
class UpdatePrivateNetworkRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    private_network_id: str
    """
    Private Network ID.
    """

    name: Optional[str]
    """
    Name for the Private Network.
    """

    tags: Optional[List[str]]
    """
    Tags for the Private Network.
    """


@dataclass
class DeletePrivateNetworkRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    private_network_id: str
    """
    Private Network ID.
    """


@dataclass
class MigrateZonalPrivateNetworksRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str]
    """
    Organization ID to target. The specified zoned Private Networks within this Organization will be migrated to regional.
    
    One-of ('scope'): at most one of 'organization_id', 'project_id' could be set.
    """

    project_id: Optional[str]
    """
    Project to target. The specified zoned Private Networks within this Project will be migrated to regional.
    
    One-of ('scope'): at most one of 'organization_id', 'project_id' could be set.
    """

    private_network_ids: Optional[List[str]]
    """
    IDs of the Private Networks to migrate.
    """


@dataclass
class SetSubnetsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    private_network_id: str
    """
    Private Network ID.
    """

    subnets: Optional[List[str]]
    """
    Private Network subnets CIDR.
    """


@dataclass
class AddSubnetsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    private_network_id: str
    """
    Private Network ID.
    """

    subnets: Optional[List[str]]
    """
    Private Network subnets CIDR.
    """


@dataclass
class DeleteSubnetsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    private_network_id: str
    """
    Private Network ID.
    """

    subnets: Optional[List[str]]
    """
    Private Network subnets CIDR.
    """
