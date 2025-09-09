# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ListIPsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    ATTACHED_AT_DESC = "attached_at_desc"
    ATTACHED_AT_ASC = "attached_at_asc"
    IP_ADDRESS_DESC = "ip_address_desc"
    IP_ADDRESS_ASC = "ip_address_asc"
    MAC_ADDRESS_DESC = "mac_address_desc"
    MAC_ADDRESS_ASC = "mac_address_asc"

    def __str__(self) -> str:
        return str(self.value)


class ResourceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    CUSTOM = "custom"
    INSTANCE_SERVER = "instance_server"
    INSTANCE_IP = "instance_ip"
    INSTANCE_PRIVATE_NIC = "instance_private_nic"
    LB_SERVER = "lb_server"
    FIP_IP = "fip_ip"
    VPC_GATEWAY = "vpc_gateway"
    VPC_GATEWAY_NETWORK = "vpc_gateway_network"
    K8S_NODE = "k8s_node"
    K8S_CLUSTER = "k8s_cluster"
    RDB_INSTANCE = "rdb_instance"
    REDIS_CLUSTER = "redis_cluster"
    BAREMETAL_SERVER = "baremetal_server"
    BAREMETAL_PRIVATE_NIC = "baremetal_private_nic"
    LLM_DEPLOYMENT = "llm_deployment"
    MGDB_INSTANCE = "mgdb_instance"
    APPLE_SILICON_SERVER = "apple_silicon_server"
    APPLE_SILICON_PRIVATE_NIC = "apple_silicon_private_nic"
    SERVERLESS_CONTAINER = "serverless_container"
    SERVERLESS_FUNCTION = "serverless_function"
    VPN_GATEWAY = "vpn_gateway"
    DDL_DATALAB = "ddl_datalab"
    KAFKA_CLUSTER = "kafka_cluster"
    BGP_ENDPOINT = "bgp_endpoint"
    SCBL_SEDB_CLUSTER = "scbl_sedb_cluster"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Resource:
    type_: ResourceType
    """
    Type of resource the IP is attached to.
    """

    id: str
    """
    ID of the resource the IP is attached to.
    """

    mac_address: Optional[str] = None
    """
    MAC of the resource the IP is attached to.
    """

    name: Optional[str] = None
    """
    When the IP is in a Private Network, then a DNS record is available to resolve the resource name to this IP.
    """


@dataclass
class Reverse:
    hostname: str
    """
    Reverse domain name.
    """

    address: Optional[str] = None
    """
    IP corresponding to the hostname.
    """


@dataclass
class Source:
    zonal: Optional[str] = None

    private_network_id: Optional[str] = None

    subnet_id: Optional[str] = None

    vpc_id: Optional[str] = None


@dataclass
class CustomResource:
    mac_address: str
    """
    MAC address of the custom resource.
    """

    name: Optional[str] = None
    """
    When the resource is in a Private Network, a DNS record is available to resolve the resource name.
    """


@dataclass
class IP:
    id: str
    """
    IP ID.
    """

    address: str
    """
    IPv4 or IPv6 address in CIDR notation.
    """

    project_id: str
    """
    Scaleway Project the IP belongs to.
    """

    is_ipv6: bool
    """
    Defines whether the IP is an IPv6 (false = IPv4).
    """

    tags: List[str]
    """
    Tags for the IP.
    """

    reverses: List[Reverse]
    """
    Array of reverses associated with the IP.
    """

    region: ScwRegion
    """
    Region of the IP.
    """

    created_at: Optional[datetime] = None
    """
    Date the IP was reserved.
    """

    updated_at: Optional[datetime] = None
    """
    Date the IP was last modified.
    """

    source: Optional[Source] = None
    """
    Source pool where the IP was reserved in.
    """

    resource: Optional[Resource] = None
    """
    Resource which the IP is attached to.
    """

    zone: Optional[ScwZone] = None
    """
    Zone of the IP, if zonal.
    """


@dataclass
class AttachIPRequest:
    ip_id: str
    """
    IP ID.
    """

    resource: CustomResource
    """
    Custom resource to be attached to the IP.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class BookIPRequest:
    source: Source
    """
    Source in which to reserve the IP. Not all sources are available for reservation.
    """

    is_ipv6: bool
    """
    Request an IPv6 instead of an IPv4.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    When creating an IP in a Private Network, the Project must match the Private Network's Project.
    """

    address: Optional[str] = None
    """
    The requested address should not include the subnet mask (/suffix). Note that only the Private Network source allows you to pick a specific IP. If the requested IP is already reserved, then the call will fail.
    """

    tags: Optional[List[str]] = field(default_factory=list)
    """
    Tags for the IP.
    """

    resource: Optional[CustomResource] = None
    """
    Custom resource to attach to the IP being reserved. An example of a custom resource is a virtual machine hosted on an Elastic Metal server. Do not use this for attaching IP addresses to standard Scaleway resources, as it will fail - instead, see the relevant product API for an equivalent method.
    """


@dataclass
class DetachIPRequest:
    ip_id: str
    """
    IP ID.
    """

    resource: CustomResource
    """
    Custom resource currently attached to the IP.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetIPRequest:
    ip_id: str
    """
    IP ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListIPsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListIPsRequestOrderBy] = ListIPsRequestOrderBy.CREATED_AT_DESC
    """
    Sort order of the returned IPs.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of IPs to return per page.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for. Only IPs belonging to this Project will be returned.
    """

    vpc_id: Optional[str] = None
    """
    Only IPs owned by resources in this VPC will be returned.
    """

    attached: Optional[bool] = False
    """
    Defines whether to filter only for IPs which are attached to a resource.
    """

    resource_name: Optional[str] = None
    """
    Attached resource name to filter for, only IPs attached to a resource with this string within their name will be returned.
    """

    resource_id: Optional[str] = None
    """
    Resource ID to filter for. Only IPs attached to this resource will be returned.
    """

    resource_ids: Optional[List[str]] = field(default_factory=list)
    """
    Resource IDs to filter for. Only IPs attached to at least one of these resources will be returned.
    """

    resource_type: Optional[ResourceType] = ResourceType.UNKNOWN_TYPE
    """
    Resource type to filter for. Only IPs attached to this type of resource will be returned.
    """

    resource_types: Optional[List[ResourceType]] = field(default_factory=list)
    """
    Resource types to filter for. Only IPs attached to these types of resources will be returned.
    """

    mac_address: Optional[str] = None
    """
    MAC address to filter for. Only IPs attached to a resource with this MAC address will be returned.
    """

    tags: Optional[List[str]] = field(default_factory=list)
    """
    Tags to filter for, only IPs with one or more matching tags will be returned.
    """

    organization_id: Optional[str] = None
    """
    Organization ID to filter for. Only IPs belonging to this Organization will be returned.
    """

    is_ipv6: Optional[bool] = False
    """
    Defines whether to filter only for IPv4s or IPv6s.
    """

    ip_ids: Optional[List[str]] = field(default_factory=list)
    """
    IP IDs to filter for. Only IPs with these UUIDs will be returned.
    """

    zonal: Optional[str] = None

    private_network_id: Optional[str] = None

    subnet_id: Optional[str] = None

    source_vpc_id: Optional[str] = None


@dataclass
class ListIPsResponse:
    total_count: int
    ips: List[IP]


@dataclass
class MoveIPRequest:
    ip_id: str
    """
    IP ID.
    """

    from_resource: CustomResource
    """
    Custom resource currently attached to the IP.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    to_resource: Optional[CustomResource] = None
    """
    Custom resource to be attached to the IP.
    """


@dataclass
class ReleaseIPRequest:
    ip_id: str
    """
    IP ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ReleaseIPSetRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    ip_ids: Optional[List[str]] = field(default_factory=list)


@dataclass
class UpdateIPRequest:
    ip_id: str
    """
    IP ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    tags: Optional[List[str]] = field(default_factory=list)
    """
    Tags for the IP.
    """

    reverses: Optional[List[Reverse]] = field(default_factory=list)
    """
    Array of reverse domain names associated with an IP in the subnet of the current IP.
    """
