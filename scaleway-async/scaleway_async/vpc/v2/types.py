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


class ListPrivateNetworksRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListVPCsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Subnet:
    id: str
    """
    ID of the subnet.
    """

    subnet: str
    """
    Subnet CIDR.
    """

    created_at: Optional[datetime]
    """
    Subnet creation date.
    """

    updated_at: Optional[datetime]
    """
    Subnet last modification date.
    """


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

    region: Region
    """
    Region in which the Private Network is available.
    """

    tags: List[str]
    """
    Tags of the Private Network.
    """

    subnets: List[Subnet]
    """
    Private Network subnets.
    """

    vpc_id: str
    """
    VPC the Private Network belongs to.
    """

    dhcp_enabled: bool
    """
    Defines whether managed DHCP is enabled for this Private Network.
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
class VPC:
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

    private_network_count: int
    """
    Number of Private Networks within this VPC.
    """

    routing_enabled: bool
    """
    Defines whether the VPC routes traffic between its Private Networks.
    """

    created_at: Optional[datetime]
    """
    Date the VPC was created.
    """

    updated_at: Optional[datetime]
    """
    Date the VPC was last modified.
    """


@dataclass
class AddSubnetsRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    subnets: Optional[List[str]]
    """
    Private Network subnets CIDR.
    """


@dataclass
class AddSubnetsResponse:
    subnets: List[str]


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
class CreateVPCRequest:
    enable_routing: bool
    """
    Enable routing between Private Networks in the VPC.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name for the VPC.
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
class DeletePrivateNetworkRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteSubnetsRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    subnets: Optional[List[str]]
    """
    Private Network subnets CIDR.
    """


@dataclass
class DeleteSubnetsResponse:
    subnets: List[str]


@dataclass
class DeleteVPCRequest:
    vpc_id: str
    """
    VPC ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class EnableDHCPRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetPrivateNetworkRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetVPCRequest:
    vpc_id: str
    """
    VPC ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
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

    dhcp_enabled: Optional[bool]
    """
    DHCP status to filter for. When true, only Private Networks with managed DHCP enabled will be returned.
    """


@dataclass
class ListPrivateNetworksResponse:
    private_networks: List[PrivateNetwork]

    total_count: int


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

    routing_enabled: Optional[bool]
    """
    Defines whether to filter only for VPCs which route traffic between their Private Networks.
    """


@dataclass
class ListVPCsResponse:
    vpcs: List[VPC]

    total_count: int


@dataclass
class MigrateZonalPrivateNetworksRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    private_network_ids: Optional[List[str]]
    """
    IDs of the Private Networks to migrate.
    """

    organization_id: Optional[str]

    project_id: Optional[str]


@dataclass
class SetSubnetsRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    subnets: Optional[List[str]]
    """
    Private Network subnets CIDR.
    """


@dataclass
class SetSubnetsResponse:
    subnets: List[str]


@dataclass
class UpdatePrivateNetworkRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
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
class UpdateVPCRequest:
    vpc_id: str
    """
    VPC ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name for the VPC.
    """

    tags: Optional[List[str]]
    """
    Tags for the VPC.
    """
