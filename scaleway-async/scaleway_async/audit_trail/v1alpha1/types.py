# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ListEventsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    RECORDED_AT_DESC = "recorded_at_desc"
    RECORDED_AT_ASC = "recorded_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ResourceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    SECM_SECRET = "secm_secret"
    SECM_SECRET_VERSION = "secm_secret_version"
    KUBE_CLUSTER = "kube_cluster"
    KUBE_POOL = "kube_pool"
    KUBE_NODE = "kube_node"
    KUBE_ACL = "kube_acl"
    KEYM_KEY = "keym_key"
    IAM_USER = "iam_user"
    IAM_APPLICATION = "iam_application"
    IAM_GROUP = "iam_group"
    IAM_POLICY = "iam_policy"
    IAM_API_KEY = "iam_api_key"
    IAM_SSH_KEY = "iam_ssh_key"
    IAM_RULE = "iam_rule"
    SECRET_MANAGER_SECRET = "secret_manager_secret"
    SECRET_MANAGER_VERSION = "secret_manager_version"
    KEY_MANAGER_KEY = "key_manager_key"
    ACCOUNT_USER = "account_user"
    ACCOUNT_ORGANIZATION = "account_organization"
    ACCOUNT_PROJECT = "account_project"
    INSTANCE_SERVER = "instance_server"
    INSTANCE_PLACEMENT_GROUP = "instance_placement_group"
    INSTANCE_SECURITY_GROUP = "instance_security_group"
    INSTANCE_VOLUME = "instance_volume"
    INSTANCE_SNAPSHOT = "instance_snapshot"
    INSTANCE_IMAGE = "instance_image"
    APPLE_SILICON_SERVER = "apple_silicon_server"
    BAREMETAL_SERVER = "baremetal_server"
    BAREMETAL_SETTING = "baremetal_setting"
    IPAM_IP = "ipam_ip"
    SBS_VOLUME = "sbs_volume"
    SBS_SNAPSHOT = "sbs_snapshot"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class AccountOrganizationInfo:
    pass


@dataclass
class AccountProjectInfo:
    description: str


@dataclass
class AccountUserInfo:
    email: str
    phone_number: Optional[str] = None


@dataclass
class AppleSiliconServerInfo:
    id: str
    name: str


@dataclass
class BaremetalServerInfo:
    description: str
    tags: List[str]


@dataclass
class BaremetalSettingInfo:
    type_: str


@dataclass
class InstanceServerInfo:
    name: str


@dataclass
class IpamIpInfo:
    address: str


@dataclass
class KeyManagerKeyInfo:
    pass


@dataclass
class KubernetesACLInfo:
    pass


@dataclass
class KubernetesClusterInfo:
    pass


@dataclass
class KubernetesNodeInfo:
    id: str
    name: str


@dataclass
class KubernetesPoolInfo:
    id: str
    name: str


@dataclass
class SecretManagerSecretInfo:
    path: str
    key_id: Optional[str] = None


@dataclass
class SecretManagerSecretVersionInfo:
    revision: int


@dataclass
class EventPrincipal:
    id: str


@dataclass
class EventSystem:
    name: str


@dataclass
class Resource:
    id: str
    type_: ResourceType
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    name: Optional[str] = None
    secm_secret_info: Optional[SecretManagerSecretInfo] = None

    secm_secret_version_info: Optional[SecretManagerSecretVersionInfo] = None

    kube_cluster_info: Optional[KubernetesClusterInfo] = None

    kube_pool_info: Optional[KubernetesPoolInfo] = None

    kube_node_info: Optional[KubernetesNodeInfo] = None

    kube_acl_info: Optional[KubernetesACLInfo] = None

    keym_key_info: Optional[KeyManagerKeyInfo] = None

    secret_manager_secret_info: Optional[SecretManagerSecretInfo] = None

    secret_manager_version_info: Optional[SecretManagerSecretVersionInfo] = None

    key_manager_key_info: Optional[KeyManagerKeyInfo] = None

    account_user_info: Optional[AccountUserInfo] = None

    account_organization_info: Optional[AccountOrganizationInfo] = None

    instance_server_info: Optional[InstanceServerInfo] = None

    apple_silicon_server_info: Optional[AppleSiliconServerInfo] = None

    account_project_info: Optional[AccountProjectInfo] = None

    baremetal_server_info: Optional[BaremetalServerInfo] = None

    baremetal_setting_info: Optional[BaremetalSettingInfo] = None

    ipam_ip_info: Optional[IpamIpInfo] = None


@dataclass
class ProductService:
    name: str
    methods: List[str]


@dataclass
class Event:
    id: str
    """
    ID of the event.
    """

    locality: str
    """
    Locality of the resource attached to the event.
    """

    organization_id: str
    """
    Organization ID containing the event.
    """

    source_ip: str
    """
    IP address at the origin of the event.
    """

    product_name: str
    """
    Product name of the resource attached to the event.
    """

    service_name: str
    """
    API name called to trigger the event.
    """

    method_name: str
    """
    API method called to trigger the event.
    """

    resources: List[Resource]
    """
    Resources attached to the event.
    """

    request_id: str
    """
    Unique identifier of the request at the origin of the event.
    """

    status_code: int
    """
    HTTP status code resulting of the API call.
    """

    recorded_at: Optional[datetime] = None
    """
    Timestamp of the event.
    """

    project_id: Optional[str] = None
    """
    (Optional) Project of the resource attached to the event.
    """

    user_agent: Optional[str] = None
    """
    User Agent at the origin of the event.
    """

    request_body: Optional[Dict[str, Any]] = field(default_factory=dict)
    """
    Request at the origin of the event.
    """

    principal: Optional[EventPrincipal] = None

    system: Optional[EventSystem] = None


@dataclass
class Product:
    title: str
    """
    Product title.
    """

    name: str
    """
    Product name.
    """

    services: List[ProductService]
    """
    Specifies the API versions of the products integrated with Audit Trail. Each version defines the methods logged by Audit Trail.
    """


@dataclass
class ListEventsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    (Optional) ID of the Project containing the Audit Trail events.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization containing the Audit Trail events.
    """

    resource_type: Optional[ResourceType] = ResourceType.UNKNOWN_TYPE
    """
    (Optional) Returns a paginated list of Scaleway resources' features.
    """

    method_name: Optional[str] = None
    """
    (Optional) Name of the method of the API call performed.
    """

    status: Optional[int] = 0
    """
    (Optional) HTTP status code of the request. Returns either `200` if the request was successful or `403` if the permission was denied.
    """

    recorded_after: Optional[datetime] = None
    """
    (Optional) The `recorded_after` parameter defines the earliest timestamp from which Audit Trail events are retrieved. Returns `one hour ago` by default.
    """

    recorded_before: Optional[datetime] = None
    """
    (Optional) The `recorded_before` parameter defines the latest timestamp up to which Audit Trail events are retrieved. Returns `now` by default.
    """

    order_by: Optional[ListEventsRequestOrderBy] = (
        ListEventsRequestOrderBy.RECORDED_AT_DESC
    )
    page_size: Optional[int] = 0
    page_token: Optional[str] = None
    product_name: Optional[str] = None
    """
    (Optional) Name of the Scaleway resource in a hyphenated format.
    """

    service_name: Optional[str] = None
    """
    (Optional) Name of the service of the API call performed.
    """


@dataclass
class ListEventsResponse:
    events: List[Event]
    """
    Single page of events matching the requested criteria.
    """

    next_page_token: Optional[str] = None
    """
    Page token to use in following calls to keep listing.
    """


@dataclass
class ListProductsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization containing the Audit Trail events.
    """


@dataclass
class ListProductsResponse:
    products: List[Product]
    """
    List of all products integrated with Audit Trail.
    """

    total_count: int
    """
    Number of integrated products.
    """
