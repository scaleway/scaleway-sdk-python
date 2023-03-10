# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from scaleway_core.bridge import (
    Region,
    Zone,
)


class AutoscalerEstimator(str, Enum):
    UNKNOWN_ESTIMATOR = "unknown_estimator"
    BINPACKING = "binpacking"

    def __str__(self) -> str:
        return str(self.value)


class AutoscalerExpander(str, Enum):
    UNKNOWN_EXPANDER = "unknown_expander"
    RANDOM = "random"
    MOST_PODS = "most_pods"
    LEAST_WASTE = "least_waste"
    PRIORITY = "priority"
    PRICE = "price"

    def __str__(self) -> str:
        return str(self.value)


class CNI(str, Enum):
    UNKNOWN_CNI = "unknown_cni"
    CILIUM = "cilium"
    CALICO = "calico"
    WEAVE = "weave"
    FLANNEL = "flannel"
    KILO = "kilo"

    def __str__(self) -> str:
        return str(self.value)


class ClusterStatus(str, Enum):
    UNKNOWN = "unknown"
    CREATING = "creating"
    READY = "ready"
    DELETING = "deleting"
    DELETED = "deleted"
    UPDATING = "updating"
    LOCKED = "locked"
    POOL_REQUIRED = "pool_required"

    def __str__(self) -> str:
        return str(self.value)


class Ingress(str, Enum):
    UNKNOWN_INGRESS = "unknown_ingress"
    NONE = "none"
    NGINX = "nginx"
    TRAEFIK = "traefik"
    TRAEFIK2 = "traefik2"

    def __str__(self) -> str:
        return str(self.value)


class ListClustersRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"
    VERSION_ASC = "version_asc"
    VERSION_DESC = "version_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListNodesRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPoolsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"
    VERSION_ASC = "version_asc"
    VERSION_DESC = "version_desc"

    def __str__(self) -> str:
        return str(self.value)


class MaintenanceWindowDayOfTheWeek(str, Enum):
    ANY = "any"
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"

    def __str__(self) -> str:
        return str(self.value)


class NodeStatus(str, Enum):
    UNKNOWN = "unknown"
    CREATING = "creating"
    NOT_READY = "not_ready"
    READY = "ready"
    DELETING = "deleting"
    DELETED = "deleted"
    LOCKED = "locked"
    REBOOTING = "rebooting"
    CREATION_ERROR = "creation_error"
    UPGRADING = "upgrading"
    STARTING = "starting"
    REGISTERING = "registering"

    def __str__(self) -> str:
        return str(self.value)


class PoolStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    DELETED = "deleted"
    SCALING = "scaling"
    WARNING = "warning"
    LOCKED = "locked"
    UPGRADING = "upgrading"

    def __str__(self) -> str:
        return str(self.value)


class PoolVolumeType(str, Enum):
    DEFAULT_VOLUME_TYPE = "default_volume_type"
    L_SSD = "l_ssd"
    B_SSD = "b_ssd"

    def __str__(self) -> str:
        return str(self.value)


class Runtime(str, Enum):
    UNKNOWN_RUNTIME = "unknown_runtime"
    DOCKER = "docker"
    CONTAINERD = "containerd"
    CRIO = "crio"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Cluster:
    """
    Cluster.
    """

    id: str
    """
    ID of the cluster.
    """

    type_: str
    """
    Type of the cluster.
    """

    name: str
    """
    Name of the cluster.
    """

    status: ClusterStatus
    """
    Status of the cluster.
    """

    version: str
    """
    Kubernetes version of the cluster.
    """

    region: Region
    """
    Region in which the cluster is deployed.
    """

    organization_id: str
    """
    ID of the organization owning the cluster.
    """

    project_id: str
    """
    ID of the project owning the cluster.
    """

    tags: List[str]
    """
    Tags associated with the cluster.
    """

    cni: CNI
    """
    Container Network Interface (CNI) plugin running in the cluster.
    """

    description: str
    """
    Description of the cluster.
    """

    cluster_url: str
    """
    Kubernetes API server URL of the cluster.
    """

    dns_wildcard: str
    """
    DNS wildcard resovling all the ready nodes of the cluster.
    """

    created_at: Optional[datetime]
    """
    Date at which the cluster was created.
    """

    updated_at: Optional[datetime]
    """
    Date at which the cluster was last updated.
    """

    autoscaler_config: Optional[ClusterAutoscalerConfig]
    """
    Autoscaler config for the cluster.
    """

    dashboard_enabled: Optional[bool]
    """
    Defines whether the Kubernetes dashboard is enabled for the cluster.
    :deprecated
    """

    ingress: Optional[Ingress]
    """
    Ingress controller used in the cluster.
    :deprecated
    """

    auto_upgrade: Optional[ClusterAutoUpgrade]
    """
    Auto upgrade configuration of the cluster.
    """

    upgrade_available: bool
    """
    Defines whether a new Kubernetes version is available.
    """

    feature_gates: List[str]
    """
    List of enabled feature gates.
    """

    admission_plugins: List[str]
    """
    List of enabled admission plugins.
    """

    open_id_connect_config: Optional[ClusterOpenIDConnectConfig]
    """
    ALPHA - The OpenID Connect configuration of the cluster.
    This feature is in ALPHA state, it may be deleted or modified. This configuration is the [OpenID Connect configuration](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#openid-connect-tokens) of the Kubernetes API server.
    """

    apiserver_cert_sans: List[str]
    """
    Additional Subject Alternative Names for the Kubernetes API server certificate.
    """


@dataclass
class ClusterAutoUpgrade:
    """
    Cluster. auto upgrade.
    """

    enabled: bool
    """
    Whether or not auto upgrade is enabled for the cluster.
    """

    maintenance_window: Optional[MaintenanceWindow]
    """
    Maintenance window of the cluster auto upgrades.
    """


@dataclass
class ClusterAutoscalerConfig:
    """
    Cluster. autoscaler config.
    """

    scale_down_disabled: bool
    """
    Disable the cluster autoscaler.
    """

    scale_down_delay_after_add: str
    """
    How long after scale up that scale down evaluation resumes.
    """

    estimator: AutoscalerEstimator
    """
    Type of resource estimator to be used in scale up.
    """

    expander: AutoscalerExpander
    """
    Type of node group expander to be used in scale up.
    """

    ignore_daemonsets_utilization: bool
    """
    Ignore DaemonSet pods when calculating resource utilization for scaling down.
    """

    balance_similar_node_groups: bool
    """
    Detect similar node groups and balance the number of nodes between them.
    """

    expendable_pods_priority_cutoff: int
    """
    Pods with priority below cutoff will be expendable.
    Pods with priority below cutoff will be expendable. They can be killed without any consideration during scale down and they don't cause scale up. Pods with null priority (PodPriority disabled) are non expendable.
    """

    scale_down_unneeded_time: str
    """
    How long a node should be unneeded before it is eligible for scale down.
    """

    scale_down_utilization_threshold: float
    """
    Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down.
    """

    max_graceful_termination_sec: int
    """
    Maximum number of seconds the cluster autoscaler waits for pod termination when trying to scale down a node.
    """


@dataclass
class ClusterOpenIDConnectConfig:
    """
    Cluster. open id connect config.
    """

    issuer_url: str
    """
    URL of the provider which allows the API server to discover public signing keys.
    URL of the provider which allows the API server to discover public signing keys. Only URLs which use the `https://` scheme are accepted. This is typically the provider's discovery URL without a path, for example "https://accounts.google.com" or "https://login.salesforce.com". This URL should point to the level below .well-known/openid-configuration.
    """

    client_id: str
    """
    A client id that all tokens must be issued for.
    """

    username_claim: str
    """
    JWT claim to use as the user name.
    JWT claim to use as the user name. By default `sub`, which is expected to be a unique identifier of the end user. Admins can choose other claims, such as `email` or `name`, depending on their provider. However, claims other than `email` will be prefixed with the issuer URL to prevent naming clashes with other plugins.
    """

    username_prefix: str
    """
    Prefix prepended to username.
    Prefix prepended to username claims to prevent clashes with existing names (such as `system:` users). For example, the value `oidc:` will create usernames like `oidc:jane.doe`. If this flag isn't provided and `username_claim` is a value other than `email` the prefix defaults to `( Issuer URL )#` where `( Issuer URL )` is the value of `issuer_url`. The value `-` can be used to disable all prefixing.
    """

    groups_claim: List[str]
    """
    JWT claim to use as the user's group.
    """

    groups_prefix: str
    """
    Prefix prepended to group claims.
    Prefix prepended to group claims to prevent clashes with existing names (such as `system:` groups). For example, the value `oidc:` will create group names like `oidc:engineering` and `oidc:infra`.
    """

    required_claim: List[str]
    """
    Multiple key=value pairs that describes a required claim in the ID token.
    Multiple key=value pairs that describes a required claim in the ID token. If set, the claims are verified to be present in the ID token with a matching value.
    """


@dataclass
class CreateClusterRequestAutoUpgrade:
    """
    Create cluster request. auto upgrade.
    """

    enable: bool
    """
    Whether or not auto upgrade is enabled for the cluster.
    """

    maintenance_window: Optional[MaintenanceWindow]
    """
    Maintenance window of the cluster auto upgrades.
    """


@dataclass
class CreateClusterRequestAutoscalerConfig:
    """
    Create cluster request. autoscaler config.
    """

    scale_down_disabled: Optional[bool]
    """
    Disable the cluster autoscaler.
    """

    scale_down_delay_after_add: Optional[str]
    """
    How long after scale up that scale down evaluation resumes.
    """

    estimator: AutoscalerEstimator
    """
    Type of resource estimator to be used in scale up.
    """

    expander: AutoscalerExpander
    """
    Type of node group expander to be used in scale up.
    """

    ignore_daemonsets_utilization: Optional[bool]
    """
    Ignore DaemonSet pods when calculating resource utilization for scaling down.
    """

    balance_similar_node_groups: Optional[bool]
    """
    Detect similar node groups and balance the number of nodes between them.
    """

    expendable_pods_priority_cutoff: Optional[int]
    """
    Pods with priority below cutoff will be expendable.
    Pods with priority below cutoff will be expendable. They can be killed without any consideration during scale down and they don't cause scale up. Pods with null priority (PodPriority disabled) are non expendable.
    """

    scale_down_unneeded_time: Optional[str]
    """
    How long a node should be unneeded before it is eligible for scale down.
    """

    scale_down_utilization_threshold: Optional[float]
    """
    Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down.
    """

    max_graceful_termination_sec: Optional[int]
    """
    Maximum number of seconds the cluster autoscaler waits for pod termination when trying to scale down a node.
    """


@dataclass
class CreateClusterRequestOpenIDConnectConfig:
    """
    Create cluster request. open id connect config.
    """

    issuer_url: str
    """
    URL of the provider which allows the API server to discover public signing keys.
    URL of the provider which allows the API server to discover public signing keys. Only URLs which use the `https://` scheme are accepted. This is typically the provider's discovery URL without a path, for example "https://accounts.google.com" or "https://login.salesforce.com". This URL should point to the level below .well-known/openid-configuration.
    """

    client_id: str
    """
    A client id that all tokens must be issued for.
    """

    username_claim: Optional[str]
    """
    JWT claim to use as the user name.
    JWT claim to use as the user name. By default `sub`, which is expected to be a unique identifier of the end user. Admins can choose other claims, such as `email` or `name`, depending on their provider. However, claims other than `email` will be prefixed with the issuer URL to prevent naming clashes with other plugins.
    """

    username_prefix: Optional[str]
    """
    Prefix prepended to username.
    Prefix prepended to username claims to prevent clashes with existing names (such as `system:` users). For example, the value `oidc:` will create usernames like `oidc:jane.doe`. If this flag isn't provided and `username_claim` is a value other than `email` the prefix defaults to `( Issuer URL )#` where `( Issuer URL )` is the value of `issuer_url`. The value `-` can be used to disable all prefixing.
    """

    groups_claim: Optional[List[str]]
    """
    JWT claim to use as the user's group.
    """

    groups_prefix: Optional[str]
    """
    Prefix prepended to group claims.
    Prefix prepended to group claims to prevent clashes with existing names (such as `system:` groups). For example, the value `oidc:` will create group names like `oidc:engineering` and `oidc:infra`.
    """

    required_claim: Optional[List[str]]
    """
    Multiple key=value pairs that describes a required claim in the ID token.
    Multiple key=value pairs that describes a required claim in the ID token. If set, the claims are verified to be present in the ID token with a matching value.
    """


@dataclass
class CreateClusterRequestPoolConfig:
    """
    Create cluster request. pool config.
    """

    name: str
    """
    Name of the pool.
    """

    node_type: str
    """
    Node type is the type of Scaleway Instance wanted for the pool.
    Node type is the type of Scaleway Instance wanted for the pool. Nodes with insufficient memory are not eligible (DEV1-S, PLAY2-PICO, STARDUST). 'external' is a special node type used to provision instances from other cloud providers.
    """

    placement_group_id: Optional[str]
    """
    Placement group ID in which all the nodes of the pool will be created.
    """

    autoscaling: bool
    """
    Defines whether the autoscaling feature is enabled for the pool.
    """

    size: int
    """
    Size (number of nodes) of the pool.
    """

    min_size: Optional[int]
    """
    Minimum size of the pool.
    Defines the minimum size of the pool. Note that this field will be used only when autoscaling is enabled.
    """

    max_size: Optional[int]
    """
    Maximum size of the pool.
    Defines the maximum size of the pool. Note that this field will be used only when autoscaling is enabled.
    """

    container_runtime: Runtime
    """
    Container runtime for the nodes of the pool.
    Customization of the container runtime is available for each pool. Note that `docker` is deprecated since 1.20 and will be removed in 1.24.
    """

    autohealing: bool
    """
    Defines whether the autohealing feature is enabled for the pool.
    """

    tags: List[str]
    """
    Tags associated with the pool.
    """

    kubelet_args: Dict[str, str]
    """
    Kubelet arguments to be used by this pool. Note that this feature is to be considered as experimental.
    """

    upgrade_policy: Optional[CreateClusterRequestPoolConfigUpgradePolicy]
    """
    Pool upgrade policy.
    """

    zone: Zone
    """
    Zone in which the pool's nodes will be spawned.
    """

    root_volume_type: PoolVolumeType
    """
    System volume disk type.
    Defines the system volume disk type, we provide two different types of volume (`volume_type`): `l_ssd` is a local block storage: your system is stored locally on the hypervisor of your node. `b_ssd` is a remote block storage: your system is stored on a centralised and resilient cluster.
    """

    root_volume_size: Optional[int]
    """
    System volume disk size.
    """


@dataclass
class CreateClusterRequestPoolConfigUpgradePolicy:
    """
    Create cluster request. pool config. upgrade policy.
    """

    max_unavailable: Optional[int]
    """
    The maximum number of nodes that can be not ready at the same time.
    """

    max_surge: Optional[int]
    """
    The maximum number of nodes to be created during the upgrade.
    """


@dataclass
class CreatePoolRequestUpgradePolicy:
    max_unavailable: Optional[int]

    max_surge: Optional[int]


@dataclass
class ExternalNode:
    id: str

    name: str

    cluster_url: str

    cluster_version: str

    cluster_ca: str

    kube_token: str

    kubelet_config: str


@dataclass
class ListClusterAvailableVersionsResponse:
    """
    List cluster available versions response.
    """

    versions: List[Version]
    """
    Available Kubernetes version for the cluster.
    """


@dataclass
class ListClustersResponse:
    """
    List clusters response.
    """

    total_count: int
    """
    Total number of clusters.
    """

    clusters: List[Cluster]
    """
    Paginated returned clusters.
    """


@dataclass
class ListNodesResponse:
    """
    List nodes response.
    """

    total_count: int
    """
    Total number of nodes.
    """

    nodes: List[Node]
    """
    Paginated returned nodes.
    """


@dataclass
class ListPoolsResponse:
    """
    List pools response.
    """

    total_count: int
    """
    Total number of pools that exists for the cluster.
    """

    pools: List[Pool]
    """
    Paginated returned pools.
    """


@dataclass
class ListVersionsResponse:
    """
    List versions response.
    """

    versions: List[Version]
    """
    Available Kubernetes versions.
    """


@dataclass
class MaintenanceWindow:
    """
    Maintenance window.
    """

    start_hour: int
    """
    Start time of the two-hour maintenance window.
    """

    day: MaintenanceWindowDayOfTheWeek
    """
    Day of the week for the maintenance window.
    """


@dataclass
class Node:
    """
    Node.
    """

    id: str
    """
    ID of the node.
    """

    pool_id: str
    """
    Pool ID of the node.
    """

    cluster_id: str
    """
    Cluster ID of the node.
    """

    provider_id: str
    """
    Underlying instance ID.
    It is prefixed by instance type and location information (see https://pkg.go.dev/k8s.io/api/core/v1#NodeSpec.ProviderID).
    """

    region: Region
    """
    Cluster region of the node.
    """

    name: str
    """
    Name of the node.
    """

    public_ip_v4: Optional[str]
    """
    Public IPv4 address of the node.
    :deprecated
    """

    public_ip_v6: Optional[str]
    """
    Public IPv6 address of the node.
    :deprecated
    """

    conditions: Optional[Dict[str, str]]
    """
    Conditions of the node.
    These conditions contains the Node Problem Detector conditions, as well as some in house conditions.
    :deprecated
    """

    status: NodeStatus
    """
    Status of the node.
    """

    error_message: Optional[str]
    """
    Details of the error, if any occured when managing the node.
    """

    created_at: Optional[datetime]
    """
    Date on which the node was created.
    """

    updated_at: Optional[datetime]
    """
    Date at which the node was last updated.
    """


@dataclass
class Pool:
    """
    Pool.
    """

    id: str
    """
    ID of the pool.
    """

    cluster_id: str
    """
    Cluster ID of the pool.
    """

    created_at: Optional[datetime]
    """
    Date at which the pool was created.
    """

    updated_at: Optional[datetime]
    """
    Date at which the pool was last updated.
    """

    name: str
    """
    Name of the pool.
    """

    status: PoolStatus
    """
    Status of the pool.
    """

    version: str
    """
    Version of the pool.
    """

    node_type: str
    """
    Node type is the type of Scaleway Instance wanted for the pool.
    Node type is the type of Scaleway Instance wanted for the pool. Nodes with insufficient memory are not eligible (DEV1-S, PLAY2-PICO, STARDUST). 'external' is a special node type used to provision instances from other cloud providers.
    """

    autoscaling: bool
    """
    Defines whether the autoscaling feature is enabled for the pool.
    """

    size: int
    """
    Size (number of nodes) of the pool.
    """

    min_size: int
    """
    Minimum size of the pool.
    Defines the minimum size of the pool. Note that this field will be used only when autoscaling is enabled.
    """

    max_size: int
    """
    Maximum size of the pool.
    Defines the maximum size of the pool. Note that this field will be used only when autoscaling is enabled.
    """

    container_runtime: Runtime
    """
    Container runtime for the nodes of the pool.
    Customization of the container runtime is available for each pool. Note that `docker` is deprecated since 1.20 and will be removed in 1.24.
    """

    autohealing: bool
    """
    Defines whether the autohealing feature is enabled for the pool.
    """

    tags: List[str]
    """
    Tags associated with the pool.
    """

    placement_group_id: Optional[str]
    """
    Placement group ID in which all the nodes of the pool will be created.
    """

    kubelet_args: Dict[str, str]
    """
    Kubelet arguments to be used by this pool. Note that this feature is to be considered as experimental.
    """

    upgrade_policy: Optional[PoolUpgradePolicy]
    """
    Pool upgrade policy.
    """

    zone: Zone
    """
    Zone in which the pool's nodes will be spawned.
    """

    root_volume_type: PoolVolumeType
    """
    System volume disk type.
    Defines the system volume disk type, we provide two different types of volume (`volume_type`): `l_ssd` is a local block storage: your system is stored locally on the hypervisor of your node. `b_ssd` is a remote block storage: your system is stored on a centralised and resilient cluster.
    """

    root_volume_size: Optional[int]
    """
    System volume disk size.
    """

    region: Region
    """
    Cluster region of the pool.
    """


@dataclass
class PoolUpgradePolicy:
    max_unavailable: int

    max_surge: int


@dataclass
class UpdateClusterRequestAutoUpgrade:
    """
    Update cluster request. auto upgrade.
    """

    enable: Optional[bool]
    """
    Whether or not auto upgrade is enabled for the cluster.
    """

    maintenance_window: Optional[MaintenanceWindow]
    """
    Maintenance window of the cluster auto upgrades.
    """


@dataclass
class UpdateClusterRequestAutoscalerConfig:
    """
    Update cluster request. autoscaler config.
    """

    scale_down_disabled: Optional[bool]
    """
    Disable the cluster autoscaler.
    """

    scale_down_delay_after_add: Optional[str]
    """
    How long after scale up that scale down evaluation resumes.
    """

    estimator: AutoscalerEstimator
    """
    Type of resource estimator to be used in scale up.
    """

    expander: AutoscalerExpander
    """
    Type of node group expander to be used in scale up.
    """

    ignore_daemonsets_utilization: Optional[bool]
    """
    Ignore DaemonSet pods when calculating resource utilization for scaling down.
    """

    balance_similar_node_groups: Optional[bool]
    """
    Detect similar node groups and balance the number of nodes between them.
    """

    expendable_pods_priority_cutoff: Optional[int]
    """
    Pods with priority below cutoff will be expendable.
    Pods with priority below cutoff will be expendable. They can be killed without any consideration during scale down and they don't cause scale up. Pods with null priority (PodPriority disabled) are non expendable.
    """

    scale_down_unneeded_time: Optional[str]
    """
    How long a node should be unneeded before it is eligible for scale down.
    """

    scale_down_utilization_threshold: Optional[float]
    """
    Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down.
    """

    max_graceful_termination_sec: Optional[int]
    """
    Maximum number of seconds the cluster autoscaler waits for pod termination when trying to scale down a node.
    """


@dataclass
class UpdateClusterRequestOpenIDConnectConfig:
    """
    Update cluster request. open id connect config.
    """

    issuer_url: Optional[str]
    """
    URL of the provider which allows the API server to discover public signing keys.
    URL of the provider which allows the API server to discover public signing keys. Only URLs which use the `https://` scheme are accepted. This is typically the provider's discovery URL without a path, for example "https://accounts.google.com" or "https://login.salesforce.com". This URL should point to the level below .well-known/openid-configuration.
    """

    client_id: Optional[str]
    """
    A client id that all tokens must be issued for.
    """

    username_claim: Optional[str]
    """
    JWT claim to use as the user name.
    JWT claim to use as the user name. By default `sub`, which is expected to be a unique identifier of the end user. Admins can choose other claims, such as `email` or `name`, depending on their provider. However, claims other than `email` will be prefixed with the issuer URL to prevent naming clashes with other plugins.
    """

    username_prefix: Optional[str]
    """
    Prefix prepended to username.
    Prefix prepended to username claims to prevent clashes with existing names (such as `system:` users). For example, the value `oidc:` will create usernames like `oidc:jane.doe`. If this flag isn't provided and `username_claim` is a value other than `email` the prefix defaults to `( Issuer URL )#` where `( Issuer URL )` is the value of `issuer_url`. The value `-` can be used to disable all prefixing.
    """

    groups_claim: Optional[List[str]]
    """
    JWT claim to use as the user's group.
    """

    groups_prefix: Optional[str]
    """
    Prefix prepended to group claims.
    Prefix prepended to group claims to prevent clashes with existing names (such as `system:` groups). For example, the value `oidc:` will create group names like `oidc:engineering` and `oidc:infra`.
    """

    required_claim: Optional[List[str]]
    """
    Multiple key=value pairs that describes a required claim in the ID token.
    Multiple key=value pairs that describes a required claim in the ID token. If set, the claims are verified to be present in the ID token with a matching value.
    """


@dataclass
class UpdatePoolRequestUpgradePolicy:
    max_unavailable: Optional[int]

    max_surge: Optional[int]


@dataclass
class Version:
    """
    Version.
    """

    name: str
    """
    Name of the Kubernetes version.
    """

    label: str
    """
    Label of the Kubernetes version.
    """

    region: Region
    """
    Region in which this version is available.
    """

    available_cnis: List[CNI]
    """
    Supported Container Network Interface (CNI) plugins for this version.
    """

    available_ingresses: Optional[List[Ingress]]
    """
    Supported Ingress Controllers for this version.
    :deprecated
    """

    available_container_runtimes: List[Runtime]
    """
    Supported container runtimes for this version.
    """

    available_feature_gates: List[str]
    """
    Supported feature gates for this version.
    """

    available_admission_plugins: List[str]
    """
    Supported admission plugins for this version.
    """

    available_kubelet_args: Dict[str, str]
    """
    Supported kubelet arguments for this version.
    """


@dataclass
class ListClustersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str]
    """
    Organization ID on which to filter the returned clusters.
    """

    project_id: Optional[str]
    """
    Project ID on which to filter the returned clusters.
    """

    order_by: Optional[ListClustersRequestOrderBy]
    """
    Sort order of the returned clusters.
    """

    page: Optional[int]
    """
    Page number for the returned clusters.
    """

    page_size: Optional[int]
    """
    Maximum number of clusters per page.
    """

    name: Optional[str]
    """
    Name on which to filter the returned clusters.
    """

    status: Optional[ClusterStatus]
    """
    Status on which to filter the returned clusters.
    """

    type_: Optional[str]
    """
    Type on which to filter the returned clusters.
    """


@dataclass
class CreateClusterRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str]
    """
    Organization ID in which the cluster will be created.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Project ID in which the cluster will be created.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """

    type_: str
    """
    Type of the cluster.
    Type of the cluster (possible values are kapsule, multicloud).
    """

    name: Optional[str]
    """
    Name of the cluster.
    """

    description: str
    """
    Description of the cluster.
    """

    tags: Optional[List[str]]
    """
    Tags associated with the cluster.
    """

    version: str
    """
    Kubernetes version of the cluster.
    """

    cni: Optional[CNI]
    """
    Container Network Interface (CNI) plugin that will run in the cluster.
    """

    enable_dashboard: Optional[bool]
    """
    Defines if the Kubernetes Dashboard is enabled in the cluster.
    :deprecated
    """

    ingress: Optional[Ingress]
    """
    Ingress Controller that will run in the cluster.
    :deprecated
    """

    pools: Optional[List[CreateClusterRequestPoolConfig]]
    """
    Pools to be created along with the cluster.
    """

    autoscaler_config: Optional[CreateClusterRequestAutoscalerConfig]
    """
    Autoscaler config for the cluster.
    This field allows to specify some configuration for the autoscaler, which is an implementation of the [cluster-autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler/).
    """

    auto_upgrade: Optional[CreateClusterRequestAutoUpgrade]
    """
    Auto upgrade configuration of the cluster.
    This configuration enables to set a specific 2-hour time window in which the cluster can be automatically updated to the latest patch version in the current minor one.
    """

    feature_gates: Optional[List[str]]
    """
    List of feature gates to enable.
    """

    admission_plugins: Optional[List[str]]
    """
    List of admission plugins to enable.
    """

    open_id_connect_config: Optional[CreateClusterRequestOpenIDConnectConfig]
    """
    ALPHA - OpenID Connect configuration of the cluster.
    This feature is in ALPHA state, it may be deleted or modified. This configuration enables to set the [OpenID Connect configuration](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#openid-connect-tokens) of the Kubernetes API server.
    """

    apiserver_cert_sans: Optional[List[str]]
    """
    Additional Subject Alternative Names for the Kubernetes API server certificate.
    """


@dataclass
class GetClusterRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cluster_id: str
    """
    The ID of the requested cluster.
    """


@dataclass
class UpdateClusterRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cluster_id: str
    """
    ID of the cluster to update.
    """

    name: Optional[str]
    """
    New external name of the cluster.
    """

    description: Optional[str]
    """
    New description of the cluster.
    """

    tags: Optional[List[str]]
    """
    New tags associated with the cluster.
    """

    autoscaler_config: Optional[UpdateClusterRequestAutoscalerConfig]
    """
    New autoscaler config for the cluster.
    Object defining the configuration for the autoscaler, which is an implementation of the [cluster-autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler/).
    """

    enable_dashboard: Optional[bool]
    """
    New value of the Kubernetes Dashboard enablement.
    :deprecated
    """

    ingress: Optional[Ingress]
    """
    New Ingress Controller for the cluster.
    :deprecated
    """

    auto_upgrade: Optional[UpdateClusterRequestAutoUpgrade]
    """
    New auto upgrade configuration of the cluster.
    New auto upgrade configuration of the cluster. Note that all fields need to be set.
    """

    feature_gates: Optional[List[str]]
    """
    List of feature gates to enable.
    """

    admission_plugins: Optional[List[str]]
    """
    List of admission plugins to enable.
    """

    open_id_connect_config: Optional[UpdateClusterRequestOpenIDConnectConfig]
    """
    ALPHA - New OpenID Connect configuration of the cluster.
    This feature is in ALPHA state, it may be deleted or modified. This configuration enables to update the [OpenID Connect configuration](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#openid-connect-tokens) of the Kubernetes API server.
    """

    apiserver_cert_sans: Optional[List[str]]
    """
    Additional Subject Alternative Names for the Kubernetes API server certificate.
    """


@dataclass
class DeleteClusterRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cluster_id: str
    """
    ID of the cluster to delete.
    """

    with_additional_resources: bool
    """
    Set true if you want to delete all volumes (including retain volume type) and loadbalancers whose name start with cluster ID.
    """


@dataclass
class UpgradeClusterRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cluster_id: str
    """
    ID of the cluster to upgrade.
    """

    version: str
    """
    New Kubernetes version of the cluster.
    New Kubernetes version of the cluster. Note that the version shoud either be a higher patch version of the same minor version or the direct minor version after the current one.
    """

    upgrade_pools: bool
    """
    Enablement of the pools upgrade.
    This field makes the upgrade upgrades the pool once the Kubernetes master in upgrade.
    """


@dataclass
class ListClusterAvailableVersionsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cluster_id: str
    """
    ID of the cluster which the available Kuberentes versions will be listed from.
    """


@dataclass
class ResetClusterAdminTokenRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cluster_id: str
    """
    ID of the cluster on which the admin token will be renewed.
    """


@dataclass
class ListPoolsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cluster_id: str
    """
    ID of the cluster from which the pools will be listed from.
    """

    order_by: Optional[ListPoolsRequestOrderBy]
    """
    Sort order of the returned pools.
    """

    page: Optional[int]
    """
    Page number for the returned pools.
    """

    page_size: Optional[int]
    """
    Maximum number of pools per page.
    """

    name: Optional[str]
    """
    Name on which to filter the returned pools.
    """

    status: Optional[PoolStatus]
    """
    Status on which to filter the returned pools.
    """


@dataclass
class CreatePoolRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cluster_id: str
    """
    ID of the cluster in which the pool will be created.
    """

    name: Optional[str]
    """
    Name of the pool.
    """

    node_type: str
    """
    Node type is the type of Scaleway Instance wanted for the pool.
    Node type is the type of Scaleway Instance wanted for the pool. Nodes with insufficient memory are not eligible (DEV1-S, PLAY2-PICO, STARDUST). 'external' is a special node type used to provision instances from other cloud providers.
    """

    placement_group_id: Optional[str]
    """
    Placement group ID in which all the nodes of the pool will be created.
    """

    autoscaling: bool
    """
    Defines whether the autoscaling feature is enabled for the pool.
    """

    size: int
    """
    Size (number of nodes) of the pool.
    """

    min_size: Optional[int]
    """
    Minimum size of the pool.
    Defines the minimum size of the pool. Note that this field will be used only when autoscaling is enabled.
    """

    max_size: Optional[int]
    """
    Maximum size of the pool.
    Defines the maximum size of the pool. Note that this field will be used only when autoscaling is enabled.
    """

    container_runtime: Runtime
    """
    Container runtime for the nodes of the pool.
    Customization of the container runtime is available for each pool. Note that `docker` is deprecated since 1.20 and will be removed in 1.24.
    """

    autohealing: bool
    """
    Defines whether the autohealing feature is enabled for the pool.
    """

    tags: Optional[List[str]]
    """
    Tags associated with the pool.
    """

    kubelet_args: Optional[Dict[str, str]]
    """
    Kubelet arguments to be used by this pool. Note that this feature is to be considered as experimental.
    """

    upgrade_policy: Optional[CreatePoolRequestUpgradePolicy]
    """
    Pool upgrade policy.
    """

    zone: Optional[Zone]
    """
    Zone in which the pool's nodes will be spawned.
    """

    root_volume_type: PoolVolumeType
    """
    System volume disk type.
    Defines the system volume disk type, we provide two different types of volume (`volume_type`): `l_ssd` is a local block storage: your system is stored locally on the hypervisor of your node. `b_ssd` is a remote block storage: your system is stored on a centralised and resilient cluster.
    """

    root_volume_size: Optional[int]
    """
    System volume disk size.
    """


@dataclass
class GetPoolRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    pool_id: str
    """
    ID of the requested pool.
    """


@dataclass
class UpgradePoolRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    pool_id: str
    """
    ID of the pool to upgrade.
    """

    version: str
    """
    New Kubernetes version for the pool.
    """


@dataclass
class UpdatePoolRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    pool_id: str
    """
    ID of the pool to update.
    """

    autoscaling: Optional[bool]
    """
    New value for the enablement of autoscaling for the pool.
    """

    size: Optional[int]
    """
    New size for the pool.
    """

    min_size: Optional[int]
    """
    New minimun size for the pool.
    """

    max_size: Optional[int]
    """
    New maximum size for the pool.
    """

    autohealing: Optional[bool]
    """
    New value for the enablement of autohealing for the pool.
    """

    tags: Optional[List[str]]
    """
    New tags associated with the pool.
    """

    kubelet_args: Optional[Dict[str, str]]
    """
    New Kubelet arguments to be used by this pool. Note that this feature is to be considered as experimental.
    """

    upgrade_policy: Optional[UpdatePoolRequestUpgradePolicy]
    """
    Upgrade policy for the pool.
    """


@dataclass
class DeletePoolRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    pool_id: str
    """
    ID of the pool to delete.
    """


@dataclass
class CreateExternalNodeRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    pool_id: str


@dataclass
class ListNodesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cluster_id: str
    """
    Cluster ID from which the nodes will be listed from.
    """

    pool_id: Optional[str]
    """
    Pool ID on which to filter the returned nodes.
    """

    order_by: Optional[ListNodesRequestOrderBy]
    """
    Sort order of the returned nodes.
    """

    page: Optional[int]
    """
    Page number for the returned nodes.
    """

    page_size: Optional[int]
    """
    Maximum number of nodes per page.
    """

    name: Optional[str]
    """
    Name on which to filter the returned nodes.
    """

    status: Optional[NodeStatus]
    """
    Status on which to filter the returned nodes.
    """


@dataclass
class GetNodeRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    node_id: str
    """
    ID of the requested node.
    """


@dataclass
class ReplaceNodeRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    node_id: str
    """
    ID of the node to replace.
    """


@dataclass
class RebootNodeRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    node_id: str
    """
    ID of the node to reboot.
    """


@dataclass
class DeleteNodeRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    node_id: str
    """
    ID of the node to replace.
    """

    skip_drain: bool
    """
    Skip draining node from its workload.
    """

    replace: bool
    """
    Add a new node after the deletion of this node.
    """


@dataclass
class ListVersionsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    version_name: str
    """
    Requested version name.
    """
