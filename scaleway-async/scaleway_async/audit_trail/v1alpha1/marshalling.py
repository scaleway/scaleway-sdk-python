# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from .types import (
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

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

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

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

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

    return EventPrincipal(**args)


def unmarshal_Resource(data: Any) -> Resource:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Resource' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

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

    field = data.get("locality", None)
    if field is not None:
        args["locality"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("source_ip", None)
    if field is not None:
        args["source_ip"] = field

    field = data.get("product_name", None)
    if field is not None:
        args["product_name"] = field

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

    field = data.get("service_name", None)
    if field is not None:
        args["service_name"] = field

    field = data.get("method_name", None)
    if field is not None:
        args["method_name"] = field

    field = data.get("request_id", None)
    if field is not None:
        args["request_id"] = field

    field = data.get("status_code", None)
    if field is not None:
        args["status_code"] = field

    field = data.get("resource", None)
    if field is not None:
        args["resource"] = unmarshal_Resource(field)
    else:
        args["resource"] = None

    field = data.get("request_body", None)
    if field is not None:
        args["request_body"] = field
    else:
        args["request_body"] = None

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

    field = data.get("methods", None)
    if field is not None:
        args["methods"] = field

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

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("services", None)
    if field is not None:
        args["services"] = (
            [unmarshal_ProductService(v) for v in field] if field is not None else None
        )

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

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListProductsResponse(**args)
