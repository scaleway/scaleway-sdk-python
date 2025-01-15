# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
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

    def __str__(self) -> str:
        return str(self.value)


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


@dataclass
class SecretManagerSecretVersionInfo:
    revision: int


@dataclass
class EventPrincipal:
    id: str


@dataclass
class Resource:
    id: str

    type_: ResourceType

    created_at: Optional[datetime]

    updated_at: Optional[datetime]

    deleted_at: Optional[datetime]

    name: Optional[str]

    secm_secret_info: Optional[SecretManagerSecretInfo]

    secm_secret_version_info: Optional[SecretManagerSecretVersionInfo]

    kube_cluster_info: Optional[KubernetesClusterInfo]

    kube_pool_info: Optional[KubernetesPoolInfo]

    kube_node_info: Optional[KubernetesNodeInfo]

    kube_acl_info: Optional[KubernetesACLInfo]


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

    recorded_at: Optional[datetime]
    """
    Timestamp of the event.
    """

    principal: Optional[EventPrincipal]
    """
    User or IAM application at the origin of the event.
    """

    project_id: Optional[str]
    """
    (Optional) Project of the resource attached to the event.
    """

    user_agent: Optional[str]
    """
    User Agent at the origin of the event.
    """

    service_name: str
    """
    API name called to trigger the event.
    """

    method_name: str
    """
    API method called to trigger the event.
    """

    request_id: str
    """
    Unique identifier of the request at the origin of the event.
    """

    status_code: int
    """
    HTTP status code resulting of the API call.
    """

    resource: Optional[Resource]
    """
    Resource attached to the event.
    """

    request_body: Optional[Dict[str, Any]]
    """
    Request at the origin of the event.
    """


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
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    (Optional) ID of the Project containing the Audit Trail events.
    """

    organization_id: Optional[str]
    """
    ID of the Organization containing the Audit Trail events.
    """

    resource_type: Optional[ResourceType]
    """
    (Optional) Returns a paginated list of Scaleway resources' features.
    """

    method_name: Optional[str]
    """
    (Optional) Name of the method or the API call performed.
    """

    status: Optional[int]
    """
    (Optional) HTTP status code of the request. Returns either `200` if the request was successful or `403` if the permission was denied.
    """

    recorded_after: Optional[datetime]
    """
    (Optional) The `recorded_after` parameter defines the earliest timestamp from which Audit Trail events are retrieved. Returns `one hour ago` by default.
    """

    recorded_before: Optional[datetime]
    """
    (Optional) The `recorded_before` parameter defines the latest timestamp up to which Audit Trail events are retrieved. Returns `now` by default.
    """

    order_by: Optional[ListEventsRequestOrderBy]

    page_size: Optional[int]

    page_token: Optional[str]

    product_name: Optional[str]
    """
    (Optional) Name of the Scaleway resource in a hyphenated format.
    """


@dataclass
class ListEventsResponse:
    events: List[Event]
    """
    Single page of events matching the requested criteria.
    """

    next_page_token: Optional[str]
    """
    Page token to use in following calls to keep listing.
    """


@dataclass
class ListProductsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
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
