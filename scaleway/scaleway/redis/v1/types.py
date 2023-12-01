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
from scaleway_core.utils import (
    StrEnumMeta,
)


class AvailableClusterSettingPropertyType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    BOOLEAN = "boolean"
    INT = "int"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)


class ClusterStatus(str, Enum, metaclass=StrEnumMeta):
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


class ListClustersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class NodeTypeStock(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    LOW_STOCK = "low_stock"
    OUT_OF_STOCK = "out_of_stock"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)


class PrivateNetworkProvisioningMode(str, Enum, metaclass=StrEnumMeta):
    STATIC = "static"
    IPAM = "ipam"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class EndpointSpecPrivateNetworkSpecIpamConfig:
    pass


@dataclass
class PrivateNetwork:
    id: str
    """
    UUID of the Private Network.
    """

    service_ips: List[str]
    """
    List of IPv4 CIDR notation addresses of the endpoint.
    """

    zone: Zone
    """
    Zone of the Private Network.
    """

    provisioning_mode: PrivateNetworkProvisioningMode
    """
    How your endpoint ips are provisioned.
    """


@dataclass
class PublicNetwork:
    pass


@dataclass
class EndpointSpecPrivateNetworkSpec:
    id: str
    """
    UUID of the Private Network to connect to the Database Instance.
    """

    service_ips: List[str]
    """
    Endpoint IPv4 address with a CIDR notation. You must provide at least one IPv4 per node.
    """

    ipam_config: Optional[EndpointSpecPrivateNetworkSpecIpamConfig]
    """
    Automated configuration of your Private Network endpoint with Scaleway IPAM service.
    """


@dataclass
class EndpointSpecPublicNetworkSpec:
    pass


@dataclass
class AvailableClusterSetting:
    name: str
    """
    Name of the setting.
    """

    type_: AvailableClusterSettingPropertyType
    """
    Type of setting.
    """

    description: str
    """
    Description of the setting.
    """

    deprecated: bool
    """
    Defines whether or not the setting is deprecated.
    """

    default_value: Optional[str]
    """
    Default value of the setting.
    """

    max_value: Optional[int]
    """
    Optional maximum value of the setting.
    """

    min_value: Optional[int]
    """
    Optional minimum value of the setting.
    """

    regex: Optional[str]
    """
    Optional validation rule of the setting.
    """


@dataclass
class ACLRule:
    id: str
    """
    ID of the rule.
    """

    ip_cidr: Optional[str]
    """
    IPv4 network address of the rule.
    """

    description: Optional[str]
    """
    Description of the rule.
    """


@dataclass
class ClusterSetting:
    value: str
    """
    Value of the setting.
    """

    name: str
    """
    Name of the setting.
    """


@dataclass
class Endpoint:
    port: int
    """
    TCP port of the endpoint.
    """

    ips: List[str]
    """
    List of IPv4 addresses of the endpoint.
    """

    id: str
    """
    UUID of the endpoint.
    """

    private_network: Optional[PrivateNetwork]

    public_network: Optional[PublicNetwork]


@dataclass
class ACLRuleSpec:
    ip_cidr: str
    """
    IPv4 network address of the rule.
    """

    description: str
    """
    Description of the rule.
    """


@dataclass
class EndpointSpec:
    private_network: Optional[EndpointSpecPrivateNetworkSpec]

    public_network: Optional[EndpointSpecPublicNetworkSpec]


@dataclass
class ClusterVersion:
    version: str
    """
    Redis™ engine version.
    """

    available_settings: List[AvailableClusterSetting]
    """
    Cluster settings available to be updated.
    """

    logo_url: str
    """
    Redis™ logo url.
    """

    zone: Zone
    """
    Zone of the Redis™ Database Instance.
    """

    end_of_life_at: Optional[datetime]
    """
    Date of End of Life.
    """


@dataclass
class Cluster:
    id: str
    """
    UUID of the Database Instance.
    """

    name: str
    """
    Name of the Database Instance.
    """

    project_id: str
    """
    Project ID the Database Instance belongs to.
    """

    status: ClusterStatus
    """
    Status of the Database Instance.
    """

    version: str
    """
    Redis™ engine version of the Database Instance.
    """

    endpoints: List[Endpoint]
    """
    List of Database Instance endpoints.
    """

    tags: List[str]
    """
    List of tags applied to the Database Instance.
    """

    node_type: str
    """
    Node type of the Database Instance.
    """

    tls_enabled: bool
    """
    Defines whether or not TLS is enabled.
    """

    cluster_settings: List[ClusterSetting]
    """
    List of Database Instance settings.
    """

    created_at: Optional[datetime]
    """
    Creation date (Format ISO 8601).
    """

    updated_at: Optional[datetime]
    """
    Update date (Format ISO 8601).
    """

    acl_rules: List[ACLRule]
    """
    List of ACL rules.
    """

    cluster_size: int
    """
    Number of nodes of the Database Instance cluster.
    """

    zone: Zone
    """
    Zone of the Database Instance.
    """

    user_name: str
    """
    Name of the user associated to the cluster.
    """

    upgradable_versions: List[str]
    """
    List of engine versions the Database Instance can upgrade to.
    """


@dataclass
class NodeType:
    name: str
    """
    Node type name.
    """

    stock_status: NodeTypeStock
    """
    Current stock status of the node type.
    """

    description: str
    """
    Current specifications of the offer.
    """

    vcpus: int
    """
    Number of virtual CPUs.
    """

    memory: int
    """
    Quantity of RAM.
    """

    disabled: bool
    """
    Defines whether node type is currently disabled or not.
    """

    beta: bool
    """
    Defines whether node type is currently in beta.
    """

    zone: Zone
    """
    Zone of the node type.
    """


@dataclass
class AddAclRulesRequest:
    cluster_id: str
    """
    UUID of the Database Instance you want to add ACL rules to.
    """

    acl_rules: List[ACLRuleSpec]
    """
    ACLs rules to add to the cluster.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AddAclRulesResponse:
    acl_rules: List[ACLRule]
    """
    ACL Rules enabled for the Database Instance.
    """

    total_count: int
    """
    Total count of ACL rules of the Database Instance.
    """


@dataclass
class AddClusterSettingsRequest:
    cluster_id: str
    """
    UUID of the Database Instance you want to add settings to.
    """

    settings: List[ClusterSetting]
    """
    Settings to add to the cluster.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AddEndpointsRequest:
    cluster_id: str
    """
    UUID of the Database Instance you want to add endpoints to.
    """

    endpoints: List[EndpointSpec]
    """
    Endpoints to add to the Database Instance.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AddEndpointsResponse:
    endpoints: List[Endpoint]
    """
    Endpoints defined on the Database Instance.
    """

    total_count: int
    """
    Total count of endpoints of the Database Instance.
    """


@dataclass
class ClusterMetricsResponse:
    timeseries: List[TimeSeries]
    """
    Time series of metrics of a given cluster.
    """


@dataclass
class ClusterSettingsResponse:
    settings: List[ClusterSetting]
    """
    Settings configured for a given Database Instance.
    """


@dataclass
class CreateClusterRequest:
    version: str
    """
    Redis™ engine version of the Database Instance.
    """

    node_type: str
    """
    Type of node to use for the Database Instance.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    Project ID in which to create the Database Instance.
    """

    name: Optional[str]
    """
    Name of the Database Instance.
    """

    tags: Optional[List[str]]
    """
    Tags to apply to the Database Instance.
    """

    user_name: str
    """
    Name of the user created upon Database Instance creation.
    """

    password: str
    """
    Password of the user.
    """

    tls_enabled: bool
    """
    Defines whether or not TLS is enabled.
    """

    cluster_size: Optional[int]
    """
    Number of nodes in the Redis™ cluster.
    """

    acl_rules: Optional[List[ACLRuleSpec]]
    """
    List of ACLRuleSpec used to secure your publicly exposed cluster.
    """

    endpoints: Optional[List[EndpointSpec]]
    """
    Zero or multiple EndpointSpec used to expose your cluster publicly and inside private networks. If no EndpoindSpec is given the cluster will be publicly exposed by default.
    """

    cluster_settings: Optional[List[ClusterSetting]]
    """
    List of advanced settings to be set upon Database Instance initialization.
    """


@dataclass
class DeleteAclRuleRequest:
    acl_id: str
    """
    UUID of the ACL rule you want to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteClusterRequest:
    cluster_id: str
    """
    UUID of the Database Instance to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteClusterSettingRequest:
    cluster_id: str
    """
    UUID of the Database Instance where the settings must be set.
    """

    setting_name: str
    """
    Setting name to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteEndpointRequest:
    endpoint_id: str
    """
    UUID of the endpoint you want to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetAclRuleRequest:
    acl_id: str
    """
    UUID of the ACL rule you want to get.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetClusterCertificateRequest:
    cluster_id: str
    """
    UUID of the cluster.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetClusterMetricsRequest:
    cluster_id: str
    """
    UUID of the cluster.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    start_at: Optional[datetime]
    """
    Start date.
    """

    end_at: Optional[datetime]
    """
    End date.
    """

    metric_name: Optional[str]
    """
    Name of the metric to gather.
    """


@dataclass
class GetClusterRequest:
    cluster_id: str
    """
    UUID of the cluster.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetEndpointRequest:
    endpoint_id: str
    """
    UUID of the endpoint you want to get.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListClusterVersionsRequest:
    include_disabled: bool
    """
    Defines whether or not to include disabled Redis™ engine versions.
    """

    include_beta: bool
    """
    Defines whether or not to include beta Redis™ engine versions.
    """

    include_deprecated: bool
    """
    Defines whether or not to include deprecated Redis™ engine versions.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    version: Optional[str]
    """
    List Redis™ engine versions that match a given name pattern.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListClusterVersionsResponse:
    versions: List[ClusterVersion]
    """
    List of available Redis™ engine versions.
    """

    total_count: int
    """
    Total count of available Redis™ engine versions.
    """


@dataclass
class ListClustersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[List[str]]
    """
    Filter by Database Instance tags.
    """

    name: Optional[str]
    """
    Filter by Database Instance names.
    """

    order_by: Optional[ListClustersRequestOrderBy]
    """
    Criteria to use when ordering the list.
    """

    project_id: Optional[str]
    """
    Filter by Project ID.
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID.
    """

    version: Optional[str]
    """
    Filter by Redis™ engine version.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListClustersResponse:
    clusters: List[Cluster]
    """
    List all Database Instances.
    """

    total_count: int
    """
    Total count of Database Instances.
    """


@dataclass
class ListNodeTypesRequest:
    include_disabled_types: bool
    """
    Defines whether or not to include disabled types.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListNodeTypesResponse:
    node_types: List[NodeType]
    """
    Types of node.
    """

    total_count: int
    """
    Total count of node types available.
    """


@dataclass
class MigrateClusterRequest:
    cluster_id: str
    """
    UUID of the Database Instance to update.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    version: Optional[str]

    node_type: Optional[str]

    cluster_size: Optional[int]


@dataclass
class RenewClusterCertificateRequest:
    cluster_id: str
    """
    UUID of the cluster.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetAclRulesRequest:
    cluster_id: str
    """
    UUID of the Database Instance where the ACL rules have to be set.
    """

    acl_rules: List[ACLRuleSpec]
    """
    ACLs rules to define for the cluster.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetAclRulesResponse:
    acl_rules: List[ACLRule]
    """
    ACL Rules enabled for the Database Instance.
    """


@dataclass
class SetClusterSettingsRequest:
    cluster_id: str
    """
    UUID of the Database Instance where the settings must be set.
    """

    settings: List[ClusterSetting]
    """
    Settings to define for the Database Instance.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetEndpointsRequest:
    cluster_id: str
    """
    UUID of the Database Instance where the endpoints have to be set.
    """

    endpoints: List[EndpointSpec]
    """
    Endpoints to define for the Database Instance.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetEndpointsResponse:
    endpoints: List[Endpoint]
    """
    Endpoints defined on the Database Instance.
    """


@dataclass
class UpdateClusterRequest:
    cluster_id: str
    """
    UUID of the Database Instance to update.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the Database Instance.
    """

    tags: Optional[List[str]]
    """
    Database Instance tags.
    """

    user_name: Optional[str]
    """
    Name of the Database Instance user.
    """

    password: Optional[str]
    """
    Password of the Database Instance user.
    """


@dataclass
class UpdateEndpointRequest:
    endpoint_id: str
    """
    UUID of the endpoint you want to get.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    private_network: Optional[EndpointSpecPrivateNetworkSpec]

    public_network: Optional[EndpointSpecPublicNetworkSpec]
