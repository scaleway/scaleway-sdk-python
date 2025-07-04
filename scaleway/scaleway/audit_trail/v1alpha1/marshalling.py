# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    ListEventsRequestOrderBy,
    ResourceType,
    AccountOrganizationInfo,
    AccountUserInfo,
    InstanceServerInfo,
    KeyManagerKeyInfo,
    KubernetesACLInfo,
    KubernetesClusterInfo,
    KubernetesNodeInfo,
    KubernetesPoolInfo,
    SecretManagerSecretInfo,
    SecretManagerSecretVersionInfo,
    EventPrincipal,
    Resource,
    Event,
    ListEventsResponse,
    ProductService,
    Product,
    ListProductsResponse,
)

def unmarshal_AccountOrganizationInfo(data: Any) -> AccountOrganizationInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AccountOrganizationInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return AccountOrganizationInfo(**args)

def unmarshal_AccountUserInfo(data: Any) -> AccountUserInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AccountUserInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("email", str())
    args["email"] = field

    field = data.get("phone_number", None)
    args["phone_number"] = field

    return AccountUserInfo(**args)

def unmarshal_InstanceServerInfo(data: Any) -> InstanceServerInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceServerInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    return InstanceServerInfo(**args)

def unmarshal_KeyManagerKeyInfo(data: Any) -> KeyManagerKeyInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KeyManagerKeyInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return KeyManagerKeyInfo(**args)

def unmarshal_KubernetesACLInfo(data: Any) -> KubernetesACLInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KubernetesACLInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return KubernetesACLInfo(**args)

def unmarshal_KubernetesClusterInfo(data: Any) -> KubernetesClusterInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KubernetesClusterInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return KubernetesClusterInfo(**args)

def unmarshal_KubernetesNodeInfo(data: Any) -> KubernetesNodeInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KubernetesNodeInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    return KubernetesNodeInfo(**args)

def unmarshal_KubernetesPoolInfo(data: Any) -> KubernetesPoolInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KubernetesPoolInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    return KubernetesPoolInfo(**args)

def unmarshal_SecretManagerSecretInfo(data: Any) -> SecretManagerSecretInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecretManagerSecretInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("path", str())
    args["path"] = field

    field = data.get("key_id", None)
    args["key_id"] = field

    return SecretManagerSecretInfo(**args)

def unmarshal_SecretManagerSecretVersionInfo(data: Any) -> SecretManagerSecretVersionInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecretManagerSecretVersionInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("revision", str())
    args["revision"] = field

    return SecretManagerSecretVersionInfo(**args)

def unmarshal_EventPrincipal(data: Any) -> EventPrincipal:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EventPrincipal' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    return EventPrincipal(**args)

def unmarshal_Resource(data: Any) -> Resource:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Resource' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("deleted_at", None)
    args["deleted_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("secm_secret_info", None)
    args["secm_secret_info"] = unmarshal_SecretManagerSecretInfo(field) if field is not None else None

    field = data.get("secm_secret_version_info", None)
    args["secm_secret_version_info"] = unmarshal_SecretManagerSecretVersionInfo(field) if field is not None else None

    field = data.get("kube_cluster_info", None)
    args["kube_cluster_info"] = unmarshal_KubernetesClusterInfo(field) if field is not None else None

    field = data.get("kube_pool_info", None)
    args["kube_pool_info"] = unmarshal_KubernetesPoolInfo(field) if field is not None else None

    field = data.get("kube_node_info", None)
    args["kube_node_info"] = unmarshal_KubernetesNodeInfo(field) if field is not None else None

    field = data.get("kube_acl_info", None)
    args["kube_acl_info"] = unmarshal_KubernetesACLInfo(field) if field is not None else None

    field = data.get("keym_key_info", None)
    args["keym_key_info"] = unmarshal_KeyManagerKeyInfo(field) if field is not None else None

    field = data.get("secret_manager_secret_info", None)
    args["secret_manager_secret_info"] = unmarshal_SecretManagerSecretInfo(field) if field is not None else None

    field = data.get("secret_manager_version_info", None)
    args["secret_manager_version_info"] = unmarshal_SecretManagerSecretVersionInfo(field) if field is not None else None

    field = data.get("key_manager_key_info", None)
    args["key_manager_key_info"] = unmarshal_KeyManagerKeyInfo(field) if field is not None else None

    field = data.get("account_user_info", None)
    args["account_user_info"] = unmarshal_AccountUserInfo(field) if field is not None else None

    field = data.get("account_organization_info", None)
    args["account_organization_info"] = unmarshal_AccountOrganizationInfo(field) if field is not None else None

    field = data.get("instance_server_info", None)
    args["instance_server_info"] = unmarshal_InstanceServerInfo(field) if field is not None else None

    return Resource(**args)

def unmarshal_Event(data: Any) -> Event:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Event' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("locality", str())
    args["locality"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("source_ip", str())
    args["source_ip"] = field

    field = data.get("recorded_at", None)
    args["recorded_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("principal", None)
    args["principal"] = unmarshal_EventPrincipal(field) if field is not None else None

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("user_agent", None)
    args["user_agent"] = field

    field = data.get("product_name", str())
    args["product_name"] = field

    field = data.get("service_name", str())
    args["service_name"] = field

    field = data.get("method_name", str())
    args["method_name"] = field

    field = data.get("resources", [])
    args["resources"] = [unmarshal_Resource(v) for v in field] if field is not None else None

    field = data.get("request_id", str())
    args["request_id"] = field

    field = data.get("status_code", 0)
    args["status_code"] = field

    field = data.get("resource", None)
    args["resource"] = unmarshal_Resource(field) if field is not None else None

    field = data.get("request_body", None)
    args["request_body"] = field

    return Event(**args)

def unmarshal_ListEventsResponse(data: Any) -> ListEventsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListEventsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("events", [])
    args["events"] = [unmarshal_Event(v) for v in field] if field is not None else None

    field = data.get("next_page_token", None)
    args["next_page_token"] = field

    return ListEventsResponse(**args)

def unmarshal_ProductService(data: Any) -> ProductService:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProductService' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("methods", str())
    args["methods"] = field

    return ProductService(**args)

def unmarshal_Product(data: Any) -> Product:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Product' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("title", str())
    args["title"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("services", [])
    args["services"] = [unmarshal_ProductService(v) for v in field] if field is not None else None

    return Product(**args)

def unmarshal_ListProductsResponse(data: Any) -> ListProductsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListProductsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("products", [])
    args["products"] = [unmarshal_Product(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListProductsResponse(**args)
