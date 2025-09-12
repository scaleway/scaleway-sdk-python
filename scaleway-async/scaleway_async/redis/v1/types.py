# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    TimeSeries,
    Zone as ScwZone,
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

    service_ips: list[str]
    """
    List of IPv4 CIDR notation addresses of the endpoint.
    """

    zone: ScwZone
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

    service_ips: list[str]
    """
    Endpoint IPv4 address with a CIDR notation. You must provide at least one IPv4 per node.
    """

    ipam_config: Optional[EndpointSpecPrivateNetworkSpecIpamConfig] = None
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

    default_value: Optional[str] = None
    """
    Default value of the setting.
    """

    max_value: Optional[int] = 0
    """
    Optional maximum value of the setting.
    """

    min_value: Optional[int] = 0
    """
    Optional minimum value of the setting.
    """

    regex: Optional[str] = None
    """
    Optional validation rule of the setting.
    """


@dataclass
class ACLRule:
    id: str
    """
    ID of the rule.
    """

    ip_cidr: Optional[str] = None
    """
    IPv4 network address of the rule.
    """

    description: Optional[str] = None
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

    ips: list[str]
    """
    List of IPv4 addresses of the endpoint.
    """

    id: str
    """
    UUID of the endpoint.
    """

    private_network: Optional[PrivateNetwork] = None

    public_network: Optional[PublicNetwork] = None


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
    private_network: Optional[EndpointSpecPrivateNetworkSpec] = None

    public_network: Optional[EndpointSpecPublicNetworkSpec] = None


@dataclass
class ClusterVersion:
    version: str
    """
    Redis™ engine version.
    """

    available_settings: list[AvailableClusterSetting]
    """
    Cluster settings available to be updated.
    """

    logo_url: str
    """
    Redis™ logo url.
    """

    zone: ScwZone
    """
    Zone of the Redis™ Database Instance.
    """

    end_of_life_at: Optional[datetime] = None
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

    endpoints: list[Endpoint]
    """
    List of Database Instance endpoints.
    """

    tags: list[str]
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

    cluster_settings: list[ClusterSetting]
    """
    List of Database Instance settings.
    """

    acl_rules: list[ACLRule]
    """
    List of ACL rules.
    """

    cluster_size: int
    """
    Number of nodes of the Database Instance cluster.
    """

    zone: ScwZone
    """
    Zone of the Database Instance.
    """

    user_name: str
    """
    Name of the user associated to the cluster.
    """

    upgradable_versions: list[str]
    """
    List of engine versions the Database Instance can upgrade to.
    """

    created_at: Optional[datetime] = None
    """
    Creation date (Format ISO 8601).
    """

    updated_at: Optional[datetime] = None
    """
    Update date (Format ISO 8601).
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

    zone: ScwZone
    """
    Zone of the node type.
    """


@dataclass
class AddAclRulesRequest:
    cluster_id: str
    """
    UUID of the Database Instance you want to add ACL rules to.
    """

    acl_rules: list[ACLRuleSpec]
    """
    ACLs rules to add to the cluster.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AddAclRulesResponse:
    acl_rules: list[ACLRule]
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

    settings: list[ClusterSetting]
    """
    Settings to add to the cluster.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AddEndpointsRequest:
    cluster_id: str
    """
    UUID of the Database Instance you want to add endpoints to.
    """

    endpoints: list[EndpointSpec]
    """
    Endpoints to add to the Database Instance.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AddEndpointsResponse:
    endpoints: list[Endpoint]
    """
    Endpoints defined on the Database Instance.
    """

    total_count: int
    """
    Total count of endpoints of the Database Instance.
    """


@dataclass
class ClusterMetricsResponse:
    timeseries: list[TimeSeries]
    """
    Time series of metrics of a given cluster.
    """


@dataclass
class ClusterSettingsResponse:
    settings: list[ClusterSetting]
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

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID in which to create the Database Instance.
    """

    name: Optional[str] = None
    """
    Name of the Database Instance.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to apply to the Database Instance.
    """

    cluster_size: Optional[int] = 0
    """
    Number of nodes in the Redis™ cluster.
    """

    acl_rules: Optional[list[ACLRuleSpec]] = field(default_factory=list)
    """
    List of ACLRuleSpec used to secure your publicly exposed cluster.
    """

    endpoints: Optional[list[EndpointSpec]] = field(default_factory=list)
    """
    Zero or multiple EndpointSpec used to expose your cluster publicly and inside private networks. If no EndpoindSpec is given the cluster will be publicly exposed by default.
    """

    cluster_settings: Optional[list[ClusterSetting]] = field(default_factory=list)
    """
    List of advanced settings to be set upon Database Instance initialization.
    """


@dataclass
class DeleteAclRuleRequest:
    acl_id: str
    """
    UUID of the ACL rule you want to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteClusterRequest:
    cluster_id: str
    """
    UUID of the Database Instance to delete.
    """

    zone: Optional[ScwZone] = None
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

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteEndpointRequest:
    endpoint_id: str
    """
    UUID of the endpoint you want to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetAclRuleRequest:
    acl_id: str
    """
    UUID of the ACL rule you want to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetClusterCertificateRequest:
    cluster_id: str
    """
    UUID of the cluster.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetClusterMetricsRequest:
    cluster_id: str
    """
    UUID of the cluster.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    start_at: Optional[datetime] = None
    """
    Start date.
    """

    end_at: Optional[datetime] = None
    """
    End date.
    """

    metric_name: Optional[str] = None
    """
    Name of the metric to gather.
    """


@dataclass
class GetClusterRequest:
    cluster_id: str
    """
    UUID of the cluster.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetEndpointRequest:
    endpoint_id: str
    """
    UUID of the endpoint you want to get.
    """

    zone: Optional[ScwZone] = None
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

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    version: Optional[str] = None
    """
    List Redis™ engine versions that match a given name pattern.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0


@dataclass
class ListClusterVersionsResponse:
    versions: list[ClusterVersion]
    """
    List of available Redis™ engine versions.
    """

    total_count: int
    """
    Total count of available Redis™ engine versions.
    """


@dataclass
class ListClustersRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Filter by Database Instance tags.
    """

    name: Optional[str] = None
    """
    Filter by Database Instance names.
    """

    order_by: Optional[ListClustersRequestOrderBy] = (
        ListClustersRequestOrderBy.CREATED_AT_ASC
    )
    """
    Criteria to use when ordering the list.
    """

    project_id: Optional[str] = None
    """
    Filter by Project ID.
    """

    organization_id: Optional[str] = None
    """
    Filter by Organization ID.
    """

    version: Optional[str] = None
    """
    Filter by Redis™ engine version.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0


@dataclass
class ListClustersResponse:
    clusters: list[Cluster]
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

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0


@dataclass
class ListNodeTypesResponse:
    node_types: list[NodeType]
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

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    version: Optional[str] = None

    node_type: Optional[str] = None

    cluster_size: Optional[int] = 0


@dataclass
class RenewClusterCertificateRequest:
    cluster_id: str
    """
    UUID of the cluster.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetAclRulesRequest:
    cluster_id: str
    """
    UUID of the Database Instance where the ACL rules have to be set.
    """

    acl_rules: list[ACLRuleSpec]
    """
    ACLs rules to define for the cluster.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetAclRulesResponse:
    acl_rules: list[ACLRule]
    """
    ACL Rules enabled for the Database Instance.
    """


@dataclass
class SetClusterSettingsRequest:
    cluster_id: str
    """
    UUID of the Database Instance where the settings must be set.
    """

    settings: list[ClusterSetting]
    """
    Settings to define for the Database Instance.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetEndpointsRequest:
    cluster_id: str
    """
    UUID of the Database Instance where the endpoints have to be set.
    """

    endpoints: list[EndpointSpec]
    """
    Endpoints to define for the Database Instance.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetEndpointsResponse:
    endpoints: list[Endpoint]
    """
    Endpoints defined on the Database Instance.
    """


@dataclass
class UpdateClusterRequest:
    cluster_id: str
    """
    UUID of the Database Instance to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Name of the Database Instance.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Database Instance tags.
    """

    user_name: Optional[str] = None
    """
    Name of the Database Instance user.
    """

    password: Optional[str] = None
    """
    Password of the Database Instance user.
    """


@dataclass
class UpdateEndpointRequest:
    endpoint_id: str
    """
    UUID of the endpoint you want to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    private_network: Optional[EndpointSpecPrivateNetworkSpec] = None

    public_network: Optional[EndpointSpecPublicNetworkSpec] = None
