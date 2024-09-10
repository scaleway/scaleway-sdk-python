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
from scaleway_core.utils import (
    StrEnumMeta,
)


class AutoscalerEstimator(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ESTIMATOR = "unknown_estimator"
    BINPACKING = "binpacking"

    def __str__(self) -> str:
        return str(self.value)


class AutoscalerExpander(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_EXPANDER = "unknown_expander"
    RANDOM = "random"
    MOST_PODS = "most_pods"
    LEAST_WASTE = "least_waste"
    PRIORITY = "priority"
    PRICE = "price"

    def __str__(self) -> str:
        return str(self.value)


class CNI(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_CNI = "unknown_cni"
    CILIUM = "cilium"
    CALICO = "calico"
    WEAVE = "weave"
    FLANNEL = "flannel"
    KILO = "kilo"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)


class ClusterStatus(str, Enum, metaclass=StrEnumMeta):
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


class ClusterTypeAvailability(str, Enum, metaclass=StrEnumMeta):
    AVAILABLE = "available"
    SCARCE = "scarce"
    SHORTAGE = "shortage"

    def __str__(self) -> str:
        return str(self.value)


class ClusterTypeResiliency(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_RESILIENCY = "unknown_resiliency"
    STANDARD = "standard"
    HIGH_AVAILABILITY = "high_availability"

    def __str__(self) -> str:
        return str(self.value)


class ListClustersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
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


class ListNodesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPoolsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
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


class MaintenanceWindowDayOfTheWeek(str, Enum, metaclass=StrEnumMeta):
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


class NodeStatus(str, Enum, metaclass=StrEnumMeta):
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


class PoolStatus(str, Enum, metaclass=StrEnumMeta):
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


class PoolVolumeType(str, Enum, metaclass=StrEnumMeta):
    DEFAULT_VOLUME_TYPE = "default_volume_type"
    L_SSD = "l_ssd"
    B_SSD = "b_ssd"

    def __str__(self) -> str:
        return str(self.value)


class Runtime(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_RUNTIME = "unknown_runtime"
    DOCKER = "docker"
    CONTAINERD = "containerd"
    CRIO = "crio"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class MaintenanceWindow:
    start_hour: int
    """
    Start time of the two-hour maintenance window.
    """

    day: MaintenanceWindowDayOfTheWeek
    """
    Day of the week for the maintenance window.
    """


@dataclass
class PoolUpgradePolicy:
    max_unavailable: int

    max_surge: int


@dataclass
class CreateClusterRequestPoolConfigUpgradePolicy:
    max_unavailable: Optional[int]
    """
    The maximum number of nodes that can be not ready at the same time.
    """

    max_surge: Optional[int]
    """
    The maximum number of nodes to be created during the upgrade.
    """


@dataclass
class ClusterAutoUpgrade:
    enabled: bool
    """
    Defines whether auto upgrade is enabled for the cluster.
    """

    maintenance_window: Optional[MaintenanceWindow]
    """
    Maintenance window of the cluster auto upgrades.
    """


@dataclass
class ClusterAutoscalerConfig:
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
    Pods with priority below cutoff will be expendable. They can be killed without any consideration during scale down and they won't cause scale up. Pods with null priority (PodPriority disabled) are non expendable.
    """

    scale_down_unneeded_time: str
    """
    How long a node should be unneeded before it is eligible to be scaled down.
    """

    scale_down_utilization_threshold: float
    """
    Node utilization level, defined as a sum of requested resources divided by capacity, below which a node can be considered for scale down.
    """

    max_graceful_termination_sec: int
    """
    Maximum number of seconds the cluster autoscaler waits for pod termination when trying to scale down a node.
    """


@dataclass
class ClusterOpenIDConnectConfig:
    issuer_url: str
    """
    URL of the provider which allows the API server to discover public signing keys. Only URLs using the `https://` scheme are accepted. This is typically the provider's discovery URL without a path, for example "https://accounts.google.com" or "https://login.salesforce.com".
    """

    client_id: str
    """
    A client ID that all tokens must be issued for.
    """

    username_claim: str
    """
    JWT claim to use as the user name. The default is `sub`, which is expected to be the end user's unique identifier. Admins can choose other claims, such as `email` or `name`, depending on their provider. However, claims other than `email` will be prefixed with the issuer URL to prevent name collision.
    """

    username_prefix: str
    """
    Prefix prepended to username claims to prevent name collision (such as `system:` users). For example, the value `oidc:` will create usernames like `oidc:jane.doe`. If this flag is not provided and `username_claim` is a value other than `email`, the prefix defaults to `( Issuer URL )#` where `( Issuer URL )` is the value of `issuer_url`. The value `-` can be used to disable all prefixing.
    """

    groups_claim: List[str]
    """
    JWT claim to use as the user's group.
    """

    groups_prefix: str
    """
    Prefix prepended to group claims to prevent name collision (such as `system:` groups). For example, the value `oidc:` will create group names like `oidc:engineering` and `oidc:infra`.
    """

    required_claim: List[str]
    """
    Multiple key=value pairs describing a required claim in the ID token. If set, the claims are verified to be present in the ID token with a matching value.
    """


@dataclass
class Pool:
    id: str
    """
    Pool ID.
    """

    cluster_id: str
    """
    Cluster ID of the pool.
    """

    name: str
    """
    Pool name.
    """

    status: PoolStatus
    """
    Pool status.
    """

    version: str
    """
    Pool version.
    """

    node_type: str
    """
    Node type is the type of Scaleway Instance wanted for the pool. Nodes with insufficient memory are not eligible (DEV1-S, PLAY2-PICO, STARDUST). 'external' is a special node type used to provision instances from other cloud providers in a Kosmos Cluster.
    """

    autoscaling: bool
    """
    Defines whether the autoscaling feature is enabled for the pool.
    """

    size: int
    """
    Size (number of nodes) of the pool.
    """

    created_at: Optional[datetime]
    """
    Date on which the pool was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the pool was last updated.
    """

    min_size: int
    """
    Defines the minimum size of the pool. Note that this field is only used when autoscaling is enabled on the pool.
    """

    max_size: int
    """
    Defines the maximum size of the pool. Note that this field is only used when autoscaling is enabled on the pool.
    """

    container_runtime: Runtime
    """
    Customization of the container runtime is available for each pool. Note that `docker` has been deprecated since version 1.20 and will be removed by version 1.24.
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
    Kubelet arguments to be used by this pool. Note that this feature is experimental.
    """

    zone: Zone
    """
    Zone in which the pool's nodes will be spawned.
    """

    root_volume_type: PoolVolumeType
    """
    Defines the system volume disk type. Two different types of volume (`volume_type`) are provided: `l_ssd` is a local block storage which means your system is stored locally on your node's hypervisor. `b_ssd` is a remote block storage which means your system is stored on a centralized and resilient cluster.
    """

    public_ip_disabled: bool
    """
    Defines if the public IP should be removed from Nodes. To use this feature, your Cluster must have an attached Private Network set up with a Public Gateway.
    """

    region: Region
    """
    Cluster region of the pool.
    """

    placement_group_id: Optional[str]
    """
    Placement group ID in which all the nodes of the pool will be created.
    """

    upgrade_policy: Optional[PoolUpgradePolicy]
    """
    Pool upgrade policy.
    """

    root_volume_size: Optional[int]
    """
    System volume disk size.
    """


@dataclass
class CreateClusterRequestAutoUpgrade:
    enable: bool
    """
    Defines whether auto upgrade is enabled for the cluster.
    """

    maintenance_window: Optional[MaintenanceWindow]
    """
    Maintenance window of the cluster auto upgrades.
    """


@dataclass
class CreateClusterRequestAutoscalerConfig:
    estimator: AutoscalerEstimator
    """
    Type of resource estimator to be used in scale up.
    """

    expander: AutoscalerExpander
    """
    Type of node group expander to be used in scale up.
    """

    scale_down_disabled: Optional[bool]
    """
    Disable the cluster autoscaler.
    """

    scale_down_delay_after_add: Optional[str]
    """
    How long after scale up that scale down evaluation resumes.
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
    Pods with priority below cutoff will be expendable. They can be killed without any consideration during scale down and they won't cause scale up. Pods with null priority (PodPriority disabled) are non expendable.
    """

    scale_down_unneeded_time: Optional[str]
    """
    How long a node should be unneeded before it is eligible to be scaled down.
    """

    scale_down_utilization_threshold: Optional[float]
    """
    Node utilization level, defined as a sum of requested resources divided by capacity, below which a node can be considered for scale down.
    """

    max_graceful_termination_sec: Optional[int]
    """
    Maximum number of seconds the cluster autoscaler waits for pod termination when trying to scale down a node.
    """


@dataclass
class CreateClusterRequestOpenIDConnectConfig:
    issuer_url: str
    """
    URL of the provider which allows the API server to discover public signing keys. Only URLs using the `https://` scheme are accepted. This is typically the provider's discovery URL without a path, for example "https://accounts.google.com" or "https://login.salesforce.com".
    """

    client_id: str
    """
    A client ID that all tokens must be issued for.
    """

    username_claim: Optional[str]
    """
    JWT claim to use as the user name. The default is `sub`, which is expected to be the end user's unique identifier. Admins can choose other claims, such as `email` or `name`, depending on their provider. However, claims other than `email` will be prefixed with the issuer URL to prevent name collision.
    """

    username_prefix: Optional[str]
    """
    Prefix prepended to username claims to prevent name collision (such as `system:` users). For example, the value `oidc:` will create usernames like `oidc:jane.doe`. If this flag is not provided and `username_claim` is a value other than `email`, the prefix defaults to `( Issuer URL )#` where `( Issuer URL )` is the value of `issuer_url`. The value `-` can be used to disable all prefixing.
    """

    groups_claim: Optional[List[str]]
    """
    JWT claim to use as the user's group.
    """

    groups_prefix: Optional[str]
    """
    Prefix prepended to group claims to prevent name collision (such as `system:` groups). For example, the value `oidc:` will create group names like `oidc:engineering` and `oidc:infra`.
    """

    required_claim: Optional[List[str]]
    """
    Multiple key=value pairs describing a required claim in the ID token. If set, the claims are verified to be present in the ID token with a matching value.
    """


@dataclass
class CreateClusterRequestPoolConfig:
    name: str
    """
    Name of the pool.
    """

    node_type: str
    """
    Node type is the type of Scaleway Instance wanted for the pool. Nodes with insufficient memory are not eligible (DEV1-S, PLAY2-PICO, STARDUST). 'external' is a special node type used to provision instances from other cloud providers in a Kosmos Cluster.
    """

    autoscaling: bool
    """
    Defines whether the autoscaling feature is enabled for the pool.
    """

    size: int
    """
    Size (number of nodes) of the pool.
    """

    container_runtime: Runtime
    """
    Customization of the container runtime is available for each pool. Note that `docker` has been deprecated since version 1.20 and will be removed by version 1.24.
    """

    placement_group_id: Optional[str]
    """
    Placement group ID in which all the nodes of the pool will be created.
    """

    min_size: Optional[int]
    """
    Defines the minimum size of the pool. Note that this field is only used when autoscaling is enabled on the pool.
    """

    max_size: Optional[int]
    """
    Defines the maximum size of the pool. Note that this field is only used when autoscaling is enabled on the pool.
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
    Kubelet arguments to be used by this pool. Note that this feature is experimental.
    """

    zone: Zone
    """
    Zone in which the pool's nodes will be spawned.
    """

    root_volume_type: PoolVolumeType
    """
    Defines the system volume disk type. Two different types of volume (`volume_type`) are provided: `l_ssd` is a local block storage which means your system is stored locally on your node's hypervisor. `b_ssd` is a remote block storage which means your system is stored on a centralized and resilient cluster.
    """

    public_ip_disabled: bool
    """
    Defines if the public IP should be removed from Nodes. To use this feature, your Cluster must have an attached Private Network set up with a Public Gateway.
    """

    upgrade_policy: Optional[CreateClusterRequestPoolConfigUpgradePolicy]
    """
    Pool upgrade policy.
    """

    root_volume_size: Optional[int]
    """
    System volume disk size.
    """


@dataclass
class CreatePoolRequestUpgradePolicy:
    max_unavailable: Optional[int]

    max_surge: Optional[int]


@dataclass
class ExternalNodeCoreV1Taint:
    key: str

    value: str

    effect: str


@dataclass
class ClusterType:
    name: str
    """
    Cluster type name.
    """

    availability: ClusterTypeAvailability
    """
    Cluster type availability.
    """

    max_nodes: int
    """
    Maximum number of nodes supported by the offer.
    """

    sla: float
    """
    Value of the Service Level Agreement of the offer.
    """

    resiliency: ClusterTypeResiliency
    """
    Resiliency offered by the offer.
    """

    memory: int
    """
    Max RAM allowed for the control plane.
    """

    dedicated: bool
    """
    Returns information if this offer uses dedicated resources.
    """

    audit_logs_supported: bool
    """
    True if the offer allows activation of the audit log functionality. Please note that audit logs are sent to Cockpit.
    """

    max_etcd_size: int
    """
    Maximum amount of data that can be stored in etcd for the offer.
    """

    commitment_delay: Optional[str]
    """
    Time period during which you can no longer switch to a lower offer.
    """


@dataclass
class Version:
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
class Cluster:
    id: str
    """
    Cluster ID.
    """

    type_: str
    """
    Cluster type.
    """

    name: str
    """
    Cluster name.
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
    ID of the Organization owning the cluster.
    """

    project_id: str
    """
    ID of the Project owning the cluster.
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
    Cluster description.
    """

    cluster_url: str
    """
    Kubernetes API server URL of the cluster.
    """

    dns_wildcard: str
    """
    Wildcard DNS resolving all the ready cluster nodes.
    """

    upgrade_available: bool
    """
    Defines whether a new Kubernetes version is available.
    """

    feature_gates: List[str]
    """
    List of enabled feature gates.
    """

    created_at: Optional[datetime]
    """
    Date on which the cluster was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the cluster was last updated.
    """

    autoscaler_config: Optional[ClusterAutoscalerConfig]
    """
    Autoscaler config for the cluster.
    """

    auto_upgrade: Optional[ClusterAutoUpgrade]
    """
    Auto upgrade configuration of the cluster.
    """

    admission_plugins: List[str]
    """
    List of enabled admission plugins.
    """

    apiserver_cert_sans: List[str]
    """
    Additional Subject Alternative Names for the Kubernetes API server certificate.
    """

    open_id_connect_config: Optional[ClusterOpenIDConnectConfig]
    """
    This configuration enables to update the OpenID Connect configuration of the Kubernetes API server.
    """

    private_network_id: Optional[str]
    """
    Private network ID for internal cluster communication.
    """

    commitment_ends_at: Optional[datetime]
    """
    Date on which it will be possible to switch to a smaller offer.
    """

    routed_ip_enabled: Optional[bool]
    """
    Defines whether routed IPs are enabled for nodes of this cluster.
    """

    sbs_csi_enabled: Optional[bool]
    """
    Defines whether the SBS-enabled CSI starting from v0.3 is installed on the cluster.
    """


@dataclass
class Node:
    id: str
    """
    Node ID.
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
    Underlying instance ID. It is prefixed by instance type and location information (see https://pkg.go.dev/k8s.io/api/core/v1#NodeSpec.ProviderID).
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
    """

    public_ip_v6: Optional[str]
    """
    Public IPv6 address of the node.
    """

    conditions: Optional[Dict[str, str]]
    """
    Conditions of the node. These conditions contain the Node Problem Detector conditions, as well as some in house conditions.
    """

    status: NodeStatus
    """
    Status of the node.
    """

    error_message: Optional[str]
    """
    Details of the error, if any occurred when managing the node.
    """

    created_at: Optional[datetime]
    """
    Date on which the node was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the node was last updated.
    """


@dataclass
class NodeMetadataCoreV1Taint:
    key: str

    value: str

    effect: str


@dataclass
class UpdateClusterRequestAutoUpgrade:
    enable: Optional[bool]
    """
    Defines whether auto upgrade is enabled for the cluster.
    """

    maintenance_window: Optional[MaintenanceWindow]
    """
    Maintenance window of the cluster auto upgrades.
    """


@dataclass
class UpdateClusterRequestAutoscalerConfig:
    estimator: AutoscalerEstimator
    """
    Type of resource estimator to be used in scale up.
    """

    expander: AutoscalerExpander
    """
    Type of node group expander to be used in scale up.
    """

    scale_down_disabled: Optional[bool]
    """
    Disable the cluster autoscaler.
    """

    scale_down_delay_after_add: Optional[str]
    """
    How long after scale up that scale down evaluation resumes.
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
    Pods with priority below cutoff will be expendable. They can be killed without any consideration during scale down and they won't cause scale up. Pods with null priority (PodPriority disabled) are non expendable.
    """

    scale_down_unneeded_time: Optional[str]
    """
    How long a node should be unneeded before it is eligible to be scaled down.
    """

    scale_down_utilization_threshold: Optional[float]
    """
    Node utilization level, defined as a sum of requested resources divided by capacity, below which a node can be considered for scale down.
    """

    max_graceful_termination_sec: Optional[int]
    """
    Maximum number of seconds the cluster autoscaler waits for pod termination when trying to scale down a node.
    """


@dataclass
class UpdateClusterRequestOpenIDConnectConfig:
    issuer_url: Optional[str]
    """
    URL of the provider which allows the API server to discover public signing keys. Only URLs using the `https://` scheme are accepted. This is typically the provider's discovery URL without a path, for example "https://accounts.google.com" or "https://login.salesforce.com".
    """

    client_id: Optional[str]
    """
    A client ID that all tokens must be issued for.
    """

    username_claim: Optional[str]
    """
    JWT claim to use as the user name. The default is `sub`, which is expected to be the end user's unique identifier. Admins can choose other claims, such as `email` or `name`, depending on their provider. However, claims other than `email` will be prefixed with the issuer URL to prevent name collision.
    """

    username_prefix: Optional[str]
    """
    Prefix prepended to username claims to prevent name collision (such as `system:` users). For example, the value `oidc:` will create usernames like `oidc:jane.doe`. If this flag is not provided and `username_claim` is a value other than `email`, the prefix defaults to `( Issuer URL )#` where `( Issuer URL )` is the value of `issuer_url`. The value `-` can be used to disable all prefixing.
    """

    groups_claim: Optional[List[str]]
    """
    JWT claim to use as the user's group.
    """

    groups_prefix: Optional[str]
    """
    Prefix prepended to group claims to prevent name collision (such as `system:` groups). For example, the value `oidc:` will create group names like `oidc:engineering` and `oidc:infra`.
    """

    required_claim: Optional[List[str]]
    """
    Multiple key=value pairs describing a required claim in the ID token. If set, the claims are verified to be present in the ID token with a matching value.
    """


@dataclass
class UpdatePoolRequestUpgradePolicy:
    max_unavailable: Optional[int]

    max_surge: Optional[int]


@dataclass
class AuthExternalNodeRequest:
    pool_id: str
    """
    Pool the node will be attached to.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CreateClusterRequest:
    type_: str
    """
    Type of the cluster (possible values are kapsule, multicloud, kapsule-dedicated-8, kapsule-dedicated-16).
    """

    description: str
    """
    Cluster description.
    """

    version: str
    """
    Kubernetes version of the cluster.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Cluster name.
    """

    tags: Optional[List[str]]
    """
    Tags associated with the cluster.
    """

    cni: CNI
    """
    Container Network Interface (CNI) plugin running in the cluster.
    """

    pools: Optional[List[CreateClusterRequestPoolConfig]]
    """
    Pools created along with the cluster.
    """

    autoscaler_config: Optional[CreateClusterRequestAutoscalerConfig]
    """
    Autoscaler configuration for the cluster. It allows you to set (to an extent) your preferred autoscaler configuration, which is an implementation of the cluster-autoscaler (https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler/).
    """

    auto_upgrade: Optional[CreateClusterRequestAutoUpgrade]
    """
    Auto upgrade configuration of the cluster. This configuration enables to set a specific 2-hour time window in which the cluster can be automatically updated to the latest patch version.
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
    OpenID Connect configuration of the cluster. This configuration enables to update the OpenID Connect configuration of the Kubernetes API server.
    """

    apiserver_cert_sans: Optional[List[str]]
    """
    Additional Subject Alternative Names for the Kubernetes API server certificate.
    """

    private_network_id: Optional[str]
    """
    Private network ID for internal cluster communication (cannot be changed later).
    """

    project_id: Optional[str]

    organization_id: Optional[str]


@dataclass
class CreateExternalNodeRequest:
    pool_id: str

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CreatePoolRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cluster_id: str
    """
    Cluster ID to which the pool will be attached.
    """

    node_type: str
    """
    Node type is the type of Scaleway Instance wanted for the pool. Nodes with insufficient memory are not eligible (DEV1-S, PLAY2-PICO, STARDUST). 'external' is a special node type used to provision instances from other cloud providers in a Kosmos Cluster.
    """

    autoscaling: bool
    """
    Defines whether the autoscaling feature is enabled for the pool.
    """

    size: int
    """
    Size (number of nodes) of the pool.
    """

    name: Optional[str]
    """
    Pool name.
    """

    placement_group_id: Optional[str]
    """
    Placement group ID in which all the nodes of the pool will be created.
    """

    min_size: Optional[int]
    """
    Defines the minimum size of the pool. Note that this field is only used when autoscaling is enabled on the pool.
    """

    autohealing: bool
    """
    Defines whether the autohealing feature is enabled for the pool.
    """

    public_ip_disabled: bool
    """
    Defines if the public IP should be removed from Nodes. To use this feature, your Cluster must have an attached Private Network set up with a Public Gateway.
    """

    max_size: Optional[int]
    """
    Defines the maximum size of the pool. Note that this field is only used when autoscaling is enabled on the pool.
    """

    container_runtime: Optional[Runtime]
    """
    Customization of the container runtime is available for each pool. Note that `docker` has been deprecated since version 1.20 and will be removed by version 1.24.
    """

    tags: Optional[List[str]]
    """
    Tags associated with the pool.
    """

    kubelet_args: Optional[Dict[str, str]]
    """
    Kubelet arguments to be used by this pool. Note that this feature is experimental.
    """

    upgrade_policy: Optional[CreatePoolRequestUpgradePolicy]
    """
    Pool upgrade policy.
    """

    zone: Optional[Zone]
    """
    Zone in which the pool's nodes will be spawned.
    """

    root_volume_type: Optional[PoolVolumeType]
    """
    Defines the system volume disk type. Two different types of volume (`volume_type`) are provided: `l_ssd` is a local block storage which means your system is stored locally on your node's hypervisor. `b_ssd` is a remote block storage which means your system is stored on a centralized and resilient cluster.
    """

    root_volume_size: Optional[int]
    """
    System volume disk size.
    """


@dataclass
class DeleteClusterRequest:
    cluster_id: str
    """
    ID of the cluster to delete.
    """

    with_additional_resources: bool
    """
    Defines whether all volumes (including retain volume type), empty Private Networks and Load Balancers with a name starting with the cluster ID will also be deleted.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteNodeRequest:
    node_id: str
    """
    ID of the node to replace.
    """

    skip_drain: bool
    """
    Skip draining node from its workload (Note: this parameter is currently inactive).
    """

    replace: bool
    """
    Add a new node after the deletion of this node.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeletePoolRequest:
    pool_id: str
    """
    ID of the pool to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ExternalNode:
    id: str

    name: str

    cluster_url: str

    pool_version: str

    cluster_ca: str

    kube_token: str

    kubelet_config: str

    external_ip: str

    containerd_version: str

    runc_version: str

    cni_plugins_version: str

    node_labels: Dict[str, str]

    node_taints: List[ExternalNodeCoreV1Taint]


@dataclass
class ExternalNodeAuth:
    node_token: str

    api_url: str


@dataclass
class GetClusterKubeConfigRequest:
    cluster_id: str
    """
    Cluster ID for which to download the kubeconfig.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    redacted: Optional[bool]
    """
    Hide the legacy token from the kubeconfig.
    """


@dataclass
class GetClusterRequest:
    cluster_id: str
    """
    ID of the requested cluster.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetNodeMetadataRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetNodeRequest:
    node_id: str
    """
    ID of the requested node.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetPoolRequest:
    pool_id: str
    """
    ID of the requested pool.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetVersionRequest:
    version_name: str
    """
    Requested version name.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListClusterAvailableTypesRequest:
    cluster_id: str
    """
    Cluster ID for which the available Kubernetes types will be listed.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListClusterAvailableTypesResponse:
    cluster_types: List[ClusterType]
    """
    Available cluster types for the cluster.
    """

    total_count: int
    """
    Total number of types.
    """


@dataclass
class ListClusterAvailableVersionsRequest:
    cluster_id: str
    """
    Cluster ID for which the available Kubernetes versions will be listed.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListClusterAvailableVersionsResponse:
    versions: List[Version]
    """
    Available Kubernetes versions for the cluster.
    """


@dataclass
class ListClusterTypesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number, from the paginated results, to return for cluster-types.
    """

    page_size: Optional[int]
    """
    Maximum number of clusters per page.
    """


@dataclass
class ListClusterTypesResponse:
    total_count: int
    """
    Total number of cluster-types.
    """

    cluster_types: List[ClusterType]
    """
    Paginated returned cluster-types.
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
    Sort order of returned clusters.
    """

    page: Optional[int]
    """
    Page number to return for clusters, from the paginated results.
    """

    page_size: Optional[int]
    """
    Maximum number of clusters per page.
    """

    name: Optional[str]
    """
    Name to filter on, only clusters containing this substring in their name will be returned.
    """

    status: Optional[ClusterStatus]
    """
    Status to filter on, only clusters with this status will be returned.
    """

    type_: Optional[str]
    """
    Type to filter on, only clusters with this type will be returned.
    """

    private_network_id: Optional[str]
    """
    Private Network ID to filter on, only clusters within this Private Network will be returned.
    """


@dataclass
class ListClustersResponse:
    total_count: int
    """
    Total number of clusters.
    """

    clusters: List[Cluster]
    """
    Paginated returned clusters.
    """


@dataclass
class ListNodesRequest:
    cluster_id: str
    """
    Cluster ID from which the nodes will be listed from.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
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
    Name to filter on, only nodes containing this substring in their name will be returned.
    """

    status: Optional[NodeStatus]
    """
    Status to filter on, only nodes with this status will be returned.
    """


@dataclass
class ListNodesResponse:
    total_count: int
    """
    Total number of nodes.
    """

    nodes: List[Node]
    """
    Paginated returned nodes.
    """


@dataclass
class ListPoolsRequest:
    cluster_id: str
    """
    ID of the cluster whose pools will be listed.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListPoolsRequestOrderBy]
    """
    Sort order of returned pools.
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
    Name to filter on, only pools containing this substring in their name will be returned.
    """

    status: Optional[PoolStatus]
    """
    Status to filter on, only pools with this status will be returned.
    """


@dataclass
class ListPoolsResponse:
    total_count: int
    """
    Total number of pools that exists for the cluster.
    """

    pools: List[Pool]
    """
    Paginated returned pools.
    """


@dataclass
class ListVersionsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListVersionsResponse:
    versions: List[Version]
    """
    Available Kubernetes versions.
    """


@dataclass
class MigrateClusterToRoutedIPsRequest:
    cluster_id: str
    """
    Cluster ID for which the routed ip will be enabled for the nodes.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class MigrateClusterToSBSCSIRequest:
    cluster_id: str
    """
    Cluster ID for which the latest CSI compatible with Scaleway Block Storage will be enabled.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class NodeMetadata:
    id: str

    name: str

    cluster_url: str

    cluster_ca: str

    credential_provider_config: str

    pool_version: str

    kubelet_config: str

    node_labels: Dict[str, str]

    node_taints: List[NodeMetadataCoreV1Taint]

    private_network_mode: str

    kapsule_iface_mac: str

    full_isolation: bool

    has_gpu: bool

    external_ip: str


@dataclass
class RebootNodeRequest:
    node_id: str
    """
    ID of the node to reboot.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ReplaceNodeRequest:
    node_id: str
    """
    ID of the node to replace.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ResetClusterAdminTokenRequest:
    cluster_id: str
    """
    Cluster ID on which the admin token will be renewed.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class SetClusterTypeRequest:
    cluster_id: str
    """
    ID of the cluster to migrate from one type to another.
    """

    type_: str
    """
    Type of the cluster. Note that some migrations are not possible (please refer to product documentation).
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UpdateClusterRequest:
    cluster_id: str
    """
    ID of the cluster to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    New external name for the cluster.
    """

    description: Optional[str]
    """
    New description for the cluster.
    """

    tags: Optional[List[str]]
    """
    New tags associated with the cluster.
    """

    autoscaler_config: Optional[UpdateClusterRequestAutoscalerConfig]
    """
    New autoscaler config for the cluster.
    """

    auto_upgrade: Optional[UpdateClusterRequestAutoUpgrade]
    """
    New auto upgrade configuration for the cluster. Note that all fields need to be set.
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
    OpenID Connect configuration of the cluster. This configuration enables to update the OpenID Connect configuration of the Kubernetes API server.
    """

    apiserver_cert_sans: Optional[List[str]]
    """
    Additional Subject Alternative Names for the Kubernetes API server certificate.
    """


@dataclass
class UpdatePoolRequest:
    pool_id: str
    """
    ID of the pool to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    autoscaling: Optional[bool]
    """
    New value for the pool autoscaling enablement.
    """

    size: Optional[int]
    """
    New desired pool size.
    """

    min_size: Optional[int]
    """
    New minimum size for the pool.
    """

    max_size: Optional[int]
    """
    New maximum size for the pool.
    """

    autohealing: Optional[bool]
    """
    New value for the pool autohealing enablement.
    """

    tags: Optional[List[str]]
    """
    New tags associated with the pool.
    """

    kubelet_args: Optional[Dict[str, str]]
    """
    New Kubelet arguments to be used by this pool. Note that this feature is experimental.
    """

    upgrade_policy: Optional[UpdatePoolRequestUpgradePolicy]
    """
    New upgrade policy for the pool.
    """


@dataclass
class UpgradeClusterRequest:
    cluster_id: str
    """
    ID of the cluster to upgrade.
    """

    version: str
    """
    New Kubernetes version of the cluster. Note that the version should either be a higher patch version of the same minor version or the direct minor version after the current one.
    """

    upgrade_pools: bool
    """
    Defines whether pools will also be upgraded once the control plane is upgraded.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UpgradePoolRequest:
    pool_id: str
    """
    ID of the pool to upgrade.
    """

    version: str
    """
    New Kubernetes version for the pool.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """
