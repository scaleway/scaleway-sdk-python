# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from .types import (
    AccountOrganizationInfo,
    AccountProjectInfo,
    AccountUserInfo,
    AppleSiliconServerInfo,
    BaremetalServerInfo,
    BaremetalSettingInfo,
    InstanceServerInfo,
    IpamIpInfo,
    KeyManagerKeyInfo,
    KubernetesACLInfo,
    KubernetesClusterInfo,
    KubernetesNodeInfo,
    KubernetesPoolInfo,
    SecretManagerSecretInfo,
    SecretManagerSecretVersionInfo,
    EventPrincipal,
    EventSystem,
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


def unmarshal_AccountProjectInfo(data: Any) -> AccountProjectInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AccountProjectInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    return AccountProjectInfo(**args)


def unmarshal_AccountUserInfo(data: Any) -> AccountUserInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AccountUserInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("email", None)
    if field is not None:
        args["email"] = field
    else:
        args["email"] = None

    field = data.get("phone_number", None)
    if field is not None:
        args["phone_number"] = field
    else:
        args["phone_number"] = None

    return AccountUserInfo(**args)


def unmarshal_AppleSiliconServerInfo(data: Any) -> AppleSiliconServerInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AppleSiliconServerInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return AppleSiliconServerInfo(**args)


def unmarshal_BaremetalServerInfo(data: Any) -> BaremetalServerInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BaremetalServerInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = None

    return BaremetalServerInfo(**args)


def unmarshal_BaremetalSettingInfo(data: Any) -> BaremetalSettingInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BaremetalSettingInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    return BaremetalSettingInfo(**args)


def unmarshal_InstanceServerInfo(data: Any) -> InstanceServerInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceServerInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return InstanceServerInfo(**args)


def unmarshal_IpamIpInfo(data: Any) -> IpamIpInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'IpamIpInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address", None)
    if field is not None:
        args["address"] = field
    else:
        args["address"] = None

    return IpamIpInfo(**args)


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

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return KubernetesNodeInfo(**args)


def unmarshal_KubernetesPoolInfo(data: Any) -> KubernetesPoolInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KubernetesPoolInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return KubernetesPoolInfo(**args)


def unmarshal_SecretManagerSecretInfo(data: Any) -> SecretManagerSecretInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecretManagerSecretInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("path", None)
    if field is not None:
        args["path"] = field
    else:
        args["path"] = None

    field = data.get("key_id", None)
    if field is not None:
        args["key_id"] = field
    else:
        args["key_id"] = None

    return SecretManagerSecretInfo(**args)


def unmarshal_SecretManagerSecretVersionInfo(
    data: Any,
) -> SecretManagerSecretVersionInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecretManagerSecretVersionInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("revision", None)
    if field is not None:
        args["revision"] = field
    else:
        args["revision"] = None

    return SecretManagerSecretVersionInfo(**args)


def unmarshal_EventPrincipal(data: Any) -> EventPrincipal:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EventPrincipal' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    return EventPrincipal(**args)


def unmarshal_EventSystem(data: Any) -> EventSystem:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EventSystem' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return EventSystem(**args)


def unmarshal_Resource(data: Any) -> Resource:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Resource' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("deleted_at", None)
    if field is not None:
        args["deleted_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["deleted_at"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("secm_secret_info", None)
    if field is not None:
        args["secm_secret_info"] = unmarshal_SecretManagerSecretInfo(field)
    else:
        args["secm_secret_info"] = None

    field = data.get("secm_secret_version_info", None)
    if field is not None:
        args["secm_secret_version_info"] = unmarshal_SecretManagerSecretVersionInfo(
            field
        )
    else:
        args["secm_secret_version_info"] = None

    field = data.get("kube_cluster_info", None)
    if field is not None:
        args["kube_cluster_info"] = unmarshal_KubernetesClusterInfo(field)
    else:
        args["kube_cluster_info"] = None

    field = data.get("kube_pool_info", None)
    if field is not None:
        args["kube_pool_info"] = unmarshal_KubernetesPoolInfo(field)
    else:
        args["kube_pool_info"] = None

    field = data.get("kube_node_info", None)
    if field is not None:
        args["kube_node_info"] = unmarshal_KubernetesNodeInfo(field)
    else:
        args["kube_node_info"] = None

    field = data.get("kube_acl_info", None)
    if field is not None:
        args["kube_acl_info"] = unmarshal_KubernetesACLInfo(field)
    else:
        args["kube_acl_info"] = None

    field = data.get("keym_key_info", None)
    if field is not None:
        args["keym_key_info"] = unmarshal_KeyManagerKeyInfo(field)
    else:
        args["keym_key_info"] = None

    field = data.get("secret_manager_secret_info", None)
    if field is not None:
        args["secret_manager_secret_info"] = unmarshal_SecretManagerSecretInfo(field)
    else:
        args["secret_manager_secret_info"] = None

    field = data.get("secret_manager_version_info", None)
    if field is not None:
        args["secret_manager_version_info"] = unmarshal_SecretManagerSecretVersionInfo(
            field
        )
    else:
        args["secret_manager_version_info"] = None

    field = data.get("key_manager_key_info", None)
    if field is not None:
        args["key_manager_key_info"] = unmarshal_KeyManagerKeyInfo(field)
    else:
        args["key_manager_key_info"] = None

    field = data.get("account_user_info", None)
    if field is not None:
        args["account_user_info"] = unmarshal_AccountUserInfo(field)
    else:
        args["account_user_info"] = None

    field = data.get("account_organization_info", None)
    if field is not None:
        args["account_organization_info"] = unmarshal_AccountOrganizationInfo(field)
    else:
        args["account_organization_info"] = None

    field = data.get("instance_server_info", None)
    if field is not None:
        args["instance_server_info"] = unmarshal_InstanceServerInfo(field)
    else:
        args["instance_server_info"] = None

    field = data.get("apple_silicon_server_info", None)
    if field is not None:
        args["apple_silicon_server_info"] = unmarshal_AppleSiliconServerInfo(field)
    else:
        args["apple_silicon_server_info"] = None

    field = data.get("account_project_info", None)
    if field is not None:
        args["account_project_info"] = unmarshal_AccountProjectInfo(field)
    else:
        args["account_project_info"] = None

    field = data.get("baremetal_server_info", None)
    if field is not None:
        args["baremetal_server_info"] = unmarshal_BaremetalServerInfo(field)
    else:
        args["baremetal_server_info"] = None

    field = data.get("baremetal_setting_info", None)
    if field is not None:
        args["baremetal_setting_info"] = unmarshal_BaremetalSettingInfo(field)
    else:
        args["baremetal_setting_info"] = None

    field = data.get("ipam_ip_info", None)
    if field is not None:
        args["ipam_ip_info"] = unmarshal_IpamIpInfo(field)
    else:
        args["ipam_ip_info"] = None

    return Resource(**args)


def unmarshal_Event(data: Any) -> Event:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Event' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("locality", None)
    if field is not None:
        args["locality"] = field
    else:
        args["locality"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("source_ip", None)
    if field is not None:
        args["source_ip"] = field
    else:
        args["source_ip"] = None

    field = data.get("product_name", None)
    if field is not None:
        args["product_name"] = field
    else:
        args["product_name"] = None

    field = data.get("service_name", None)
    if field is not None:
        args["service_name"] = field
    else:
        args["service_name"] = None

    field = data.get("method_name", None)
    if field is not None:
        args["method_name"] = field
    else:
        args["method_name"] = None

    field = data.get("recorded_at", None)
    if field is not None:
        args["recorded_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["recorded_at"] = None

    field = data.get("principal", None)
    if field is not None:
        args["principal"] = unmarshal_EventPrincipal(field)
    else:
        args["principal"] = None

    field = data.get("resources", None)
    if field is not None:
        args["resources"] = (
            [unmarshal_Resource(v) for v in field] if field is not None else None
        )
    else:
        args["resources"] = []

    field = data.get("request_id", None)
    if field is not None:
        args["request_id"] = field
    else:
        args["request_id"] = None

    field = data.get("status_code", None)
    if field is not None:
        args["status_code"] = field
    else:
        args["status_code"] = 0

    field = data.get("system", None)
    if field is not None:
        args["system"] = unmarshal_EventSystem(field)
    else:
        args["system"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("user_agent", None)
    if field is not None:
        args["user_agent"] = field
    else:
        args["user_agent"] = None

    field = data.get("request_body", None)
    if field is not None:
        args["request_body"] = field
    else:
        args["request_body"] = {}

    return Event(**args)


def unmarshal_ListEventsResponse(data: Any) -> ListEventsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListEventsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("events", None)
    if field is not None:
        args["events"] = (
            [unmarshal_Event(v) for v in field] if field is not None else None
        )
    else:
        args["events"] = []

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListEventsResponse(**args)


def unmarshal_ProductService(data: Any) -> ProductService:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProductService' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("methods", None)
    if field is not None:
        args["methods"] = field
    else:
        args["methods"] = None

    return ProductService(**args)


def unmarshal_Product(data: Any) -> Product:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Product' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("title", None)
    if field is not None:
        args["title"] = field
    else:
        args["title"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("services", None)
    if field is not None:
        args["services"] = (
            [unmarshal_ProductService(v) for v in field] if field is not None else None
        )
    else:
        args["services"] = []

    return Product(**args)


def unmarshal_ListProductsResponse(data: Any) -> ListProductsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListProductsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("products", None)
    if field is not None:
        args["products"] = (
            [unmarshal_Product(v) for v in field] if field is not None else None
        )
    else:
        args["products"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListProductsResponse(**args)
