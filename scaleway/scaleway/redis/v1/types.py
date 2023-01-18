# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    TimeSeries,
    Zone,
)


class AvailableClusterSettingPropertyType(str, Enum):
    UNKNOWN = "UNKNOWN"
    BOOLEAN = "BOOLEAN"
    INT = "INT"
    STRING = "STRING"

    def __str__(self) -> str:
        return str(self.value)


class ClusterStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    PROVISIONING = "provisioning"
    CONFIGURING = "configuring"
    DELETING = "deleting"
    ERROR = "error"
    AUTOHEALING = "autohealing"
    LOCKED = "locked"
    SUSPENDED = "suspended"
    INITIALIZING = "initializing"

    def __str__(self) -> str:
        return str(self.value)


class ListClustersRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class NodeTypeStock(str, Enum):
    UNKNOWN = "unknown"
    LOW_STOCK = "low_stock"
    OUT_OF_STOCK = "out_of_stock"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class ACLRule:
    """
    Acl rule
    """

    id: str
    """
    ID of the rule
    """

    ip_cidr: Optional[str]
    """
    IPv4 network address of the rule
    """

    description: Optional[str]
    """
    Description of the rule
    """


@dataclass
class ACLRuleSpec:
    """
    Acl rule spec
    """

    ip_cidr: str
    """
    IPv4 network address of the rule
    """

    description: str
    """
    Description of the rule
    """


@dataclass
class AddAclRulesResponse:
    """
    Add acl rules response
    """

    acl_rules: List[ACLRule]
    """
    ACL Rules enabled on the cluster
    """

    total_count: int
    """
    Total count of acl rules of the cluster
    """


@dataclass
class AddEndpointsResponse:
    """
    Add endpoints response
    """

    endpoints: List[Endpoint]
    """
    Endpoints defined on the cluster
    """

    total_count: int
    """
    Total count of endpoints of the cluster
    """


@dataclass
class AvailableClusterSetting:
    """
    Available cluster setting
    """

    name: str
    """
    Name of the setting
    """

    default_value: Optional[str]
    """
    Default value of the setting
    """

    type_: AvailableClusterSettingPropertyType
    """
    Type of the setting
    """

    description: str
    """
    Description of the setting
    """

    max_value: Optional[int]
    """
    Optional maximum value of the setting
    """

    min_value: Optional[int]
    """
    Optional minimum value of the setting
    """

    regex: Optional[str]
    """
    Optional validation rule of the setting
    """

    deprecated: bool
    """
    Whether the setting is deprecated
    """


@dataclass
class Cluster:
    """
    Cluster
    """

    id: str
    """
    UUID of the cluster
    """

    name: str
    """
    Name of the cluster
    """

    project_id: str
    """
    Project ID the cluster belongs to
    """

    status: ClusterStatus
    """
    Status of the cluster
    """

    version: str
    """
    Redis™ engine version of the cluster
    """

    endpoints: List[Endpoint]
    """
    List of cluster endpoints
    """

    tags: List[str]
    """
    List of tags applied to the cluster
    """

    node_type: str
    """
    Node type of the cluster
    """

    created_at: Optional[datetime]
    """
    Creation date (Format ISO 8601)
    """

    updated_at: Optional[datetime]
    """
    Update date (Format ISO 8601)
    """

    tls_enabled: bool
    """
    Whether or not TLS is enabled
    """

    cluster_settings: List[ClusterSetting]
    """
    List of cluster settings
    """

    acl_rules: List[ACLRule]
    """
    List of acl rules
    """

    cluster_size: int
    """
    Number of nodes of the cluster
    """

    zone: Zone
    """
    Zone of the cluster
    """

    user_name: str
    """
    Name of the user associated to the cluster
    """

    upgradable_versions: List[str]
    """
    List of versions the cluster can be migrated to
    """


@dataclass
class ClusterMetricsResponse:
    """
    Cluster metrics response
    """

    timeseries: List[TimeSeries]
    """
    Time series of metrics of a given cluster
    """


@dataclass
class ClusterSetting:
    """
    Cluster setting
    """

    value: str
    """
    Value of the setting
    """

    name: str
    """
    Name of the setting
    """


@dataclass
class ClusterSettingsResponse:
    """
    Cluster settings response
    """

    settings: List[ClusterSetting]
    """
    Settings configured for a given cluster
    """


@dataclass
class ClusterVersion:
    """
    Cluster version
    """

    version: str
    """
    Redis™ engine version
    """

    end_of_life_at: Optional[datetime]
    """
    End of life date
    """

    available_settings: List[AvailableClusterSetting]
    """
    Cluster settings available to be set
    """

    logo_url: str
    """
    Redis™ logo url
    """

    zone: Zone
    """
    Zone of the Managed Database for Redis™
    """


@dataclass
class Endpoint:
    """
    Endpoint
    """

    port: int
    """
    TCP port of the endpoint
    """

    private_network: Optional[PrivateNetwork]
    """
    Private network details.
    
    One-of ('details'): at most one of 'private_network', 'public_network' could be set.
    """

    public_network: Optional[PublicNetwork]
    """
    Public network details.
    
    One-of ('details'): at most one of 'private_network', 'public_network' could be set.
    """

    ips: List[str]
    """
    Lis of IPv4 address of the endpoint
    """

    id: str
    """
    UUID of the endpoint
    """


@dataclass
class EndpointSpec:
    """
    Endpoint spec
    """

    private_network: Optional[EndpointSpecPrivateNetworkSpec]
    """
    Private network spec details.
    
    One-of ('endpoint_type'): at most one of 'private_network', 'public_network' could be set.
    """

    public_network: Optional[EndpointSpecPublicNetworkSpec]
    """
    Public network spec details.
    
    One-of ('endpoint_type'): at most one of 'private_network', 'public_network' could be set.
    """


@dataclass
class EndpointSpecPrivateNetworkSpec:
    """
    Endpoint spec. private network spec
    """

    id: str
    """
    UUID of the private network to be connected to the cluster
    """

    service_ips: List[str]
    """
    Endpoint IPv4 adress with a CIDR notation. You must provide at least one IPv4 per node. Check documentation about IP and subnet limitation.
    """


@dataclass
class EndpointSpecPublicNetworkSpec:
    """
    Endpoint spec. public network spec
    """


@dataclass
class ListClusterVersionsResponse:
    """
    List cluster versions response
    """

    versions: List[ClusterVersion]
    """
    List of the available Redis™ engine versions
    """

    total_count: int
    """
    Total count of available Redis™ engine versions
    """


@dataclass
class ListClustersResponse:
    """
    List clusters response
    """

    clusters: List[Cluster]
    """
    List all clusters
    """

    total_count: int
    """
    Total count of clusters
    """


@dataclass
class ListNodeTypesResponse:
    """
    List node types response
    """

    node_types: List[NodeType]
    """
    Types of the node
    """

    total_count: int
    """
    Total count of node-types available
    """


@dataclass
class NodeType:
    """
    Node type
    """

    name: str
    """
    Node Type name identifier
    """

    stock_status: NodeTypeStock
    """
    Current stock status for the Node Type
    """

    description: str
    """
    Current specs of the offer
    """

    vcpus: int
    """
    Number of virtual CPUs
    """

    memory: int
    """
    Quantity of RAM
    """

    disabled: bool
    """
    The Node Type is currently disabled
    """

    beta: bool
    """
    The Node Type is currently in beta
    """

    zone: Zone
    """
    Zone the Node Type is in
    """


@dataclass
class PrivateNetwork:
    """
    Private network
    """

    id: str
    """
    UUID of the private network
    """

    service_ips: List[str]
    """
    List of IPv4 CIDR notation addresses of the endpoint
    """

    zone: Zone
    """
    Private network zone
    """


@dataclass
class PublicNetwork:
    pass


@dataclass
class SetAclRulesResponse:
    """
    Set acl rules response
    """

    acl_rules: List[ACLRule]
    """
    ACL Rules enabled on the cluster
    """


@dataclass
class SetEndpointsResponse:
    """
    Set endpoints response
    """

    endpoints: List[Endpoint]
    """
    Endpoints defined on the cluster
    """


@dataclass
class CreateClusterRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    project_id: Optional[str]
    """
    The project ID on which to create the cluster
    """

    name: Optional[str]
    """
    Name of the cluster
    """

    version: str
    """
    Redis™ engine version of the cluster
    """

    tags: Optional[List[str]]
    """
    Tags to apply to the cluster
    """

    node_type: str
    """
    Type of node to use for the cluster
    """

    user_name: str
    """
    Name of the user created when the cluster is created
    """

    password: str
    """
    Password of the user
    """

    cluster_size: Optional[int]
    """
    Number of nodes for the cluster
    """

    acl_rules: Optional[List[ACLRuleSpec]]
    """
    List of ACLRuleSpec used to secure your publicly exposed cluster
    """

    endpoints: Optional[List[EndpointSpec]]
    """
    Zero or multiple EndpointSpec used to expose your cluster publicly and inside private networks. If no EndpoindSpec is given the cluster will be publicly exposed by default.
    """

    tls_enabled: bool
    """
    Whether or not TLS is enabled
    """

    cluster_settings: Optional[List[ClusterSetting]]
    """
    List of cluster settings to be set at cluster initialisation
    """


@dataclass
class UpdateClusterRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    cluster_id: str
    """
    UUID of the cluster to update
    """

    name: Optional[str]
    """
    Name of the cluster
    """

    tags: Optional[List[str]]
    """
    Tags of a given cluster
    """

    user_name: Optional[str]
    """
    Name of the cluster user
    """

    password: Optional[str]
    """
    Password of the cluster user
    """


@dataclass
class GetClusterRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    cluster_id: str
    """
    UUID of the cluster
    """


@dataclass
class ListClustersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    tags: Optional[List[str]]
    """
    Tags of the clusters to filter upon
    """

    name: Optional[str]
    """
    Name of the clusters to filter upon
    """

    order_by: Optional[ListClustersRequestOrderBy]
    """
    Criteria to use when ordering cluster listing
    """

    project_id: Optional[str]
    """
    Project ID to list the cluster of
    """

    organization_id: Optional[str]
    """
    Organization ID to list the cluster of
    """

    version: Optional[str]
    """
    Version of the clusters to filter upon
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class MigrateClusterRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    cluster_id: str
    """
    UUID of the cluster to update
    """

    version: Optional[str]
    """
    Redis™ engine version of the cluster.
    
    One-of ('action'): at most one of 'version', 'node_type', 'cluster_size' could be set.
    """

    node_type: Optional[str]
    """
    Type of node to use for the cluster.
    
    One-of ('action'): at most one of 'version', 'node_type', 'cluster_size' could be set.
    """

    cluster_size: Optional[int]
    """
    Number of nodes for the cluster.
    
    One-of ('action'): at most one of 'version', 'node_type', 'cluster_size' could be set.
    """


@dataclass
class DeleteClusterRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    cluster_id: str
    """
    UUID of the cluster to delete
    """


@dataclass
class GetClusterMetricsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    cluster_id: str
    """
    UUID of the cluster
    """

    start_at: Optional[datetime]
    """
    Start date to gather metrics from
    """

    end_at: Optional[datetime]
    """
    End date to gather metrics from
    """

    metric_name: Optional[str]
    """
    Name of the metric to gather
    """


@dataclass
class ListNodeTypesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    include_disabled_types: bool
    """
    Whether or not to include disabled types
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListClusterVersionsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    include_disabled: bool
    """
    Whether or not to include disabled Redis™ engine versions
    """

    include_beta: bool
    """
    Whether or not to include beta Redis™ engine versions
    """

    include_deprecated: bool
    """
    Whether or not to include deprecated Redis™ engine versions
    """

    version: Optional[str]
    """
    List Redis™ engine versions that match a given name pattern
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class GetClusterCertificateRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    cluster_id: str
    """
    UUID of the cluster
    """


@dataclass
class RenewClusterCertificateRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    cluster_id: str
    """
    UUID of the cluster
    """


@dataclass
class AddClusterSettingsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    cluster_id: str
    """
    UUID of the cluster you want to add settings to
    """

    settings: List[ClusterSetting]
    """
    Settings to add on the cluster
    """


@dataclass
class DeleteClusterSettingRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    cluster_id: str
    """
    UUID of the cluster where the settings has to be set
    """

    setting_name: str
    """
    Setting name to delete
    """


@dataclass
class SetClusterSettingsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    cluster_id: str
    """
    UUID of the cluster where the settings has to be set
    """

    settings: List[ClusterSetting]
    """
    Settings to define for the cluster
    """


@dataclass
class SetAclRulesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    cluster_id: str
    """
    UUID of the cluster where the ACL rules has to be set
    """

    acl_rules: List[ACLRuleSpec]
    """
    ACLs rules to define for the cluster
    """


@dataclass
class AddAclRulesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    cluster_id: str
    """
    UUID of the cluster you want to add acl rules to
    """

    acl_rules: List[ACLRuleSpec]
    """
    ACLs rules to add to the cluster
    """


@dataclass
class DeleteAclRuleRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    acl_id: str
    """
    UUID of the acl rule you want to delete
    """


@dataclass
class GetAclRuleRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    acl_id: str
    """
    UUID of the acl rule you want to get
    """


@dataclass
class SetEndpointsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    cluster_id: str
    """
    UUID of the cluster where the endpoints has to be set
    """

    endpoints: List[EndpointSpec]
    """
    Endpoints to define for the cluster
    """


@dataclass
class AddEndpointsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    cluster_id: str
    """
    UUID of the cluster you want to add endpoints to
    """

    endpoints: List[EndpointSpec]
    """
    Endpoints to add to the cluster
    """


@dataclass
class DeleteEndpointRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    endpoint_id: str
    """
    UUID of the endpoint you want to delete
    """


@dataclass
class GetEndpointRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    endpoint_id: str
    """
    UUID of the endpoint you want to get
    """


@dataclass
class UpdateEndpointRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    endpoint_id: str

    private_network: Optional[EndpointSpecPrivateNetworkSpec]
    """
    One-of ('endpoint_type'): at most one of 'private_network', 'public_network' could be set.
    """

    public_network: Optional[EndpointSpecPublicNetworkSpec]
    """
    One-of ('endpoint_type'): at most one of 'private_network', 'public_network' could be set.
    """
