# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    DeviceMessageFiltersRulePolicy,
    DeviceStatus,
    HubProductPlan,
    HubStatus,
    NetworkNetworkType,
    RouteDatabaseConfigEngine,
    RouteRestConfigHttpVerb,
    RouteRouteType,
    RouteS3ConfigS3Strategy,
    DeviceMessageFiltersRule,
    DeviceMessageFilters,
    Device,
    Network,
    HubTwinsGraphiteConfig,
    Hub,
    Certificate,
    CreateDeviceResponse,
    CreateNetworkResponse,
    GetDeviceCertificateResponse,
    GetDeviceMetricsResponse,
    GetHubCAResponse,
    GetHubMetricsResponse,
    ListDevicesResponse,
    ListHubsResponse,
    ListNetworksResponse,
    RouteSummary,
    ListRoutesResponse,
    ListTwinDocumentsResponseDocumentSummary,
    ListTwinDocumentsResponse,
    RenewDeviceCertificateResponse,
    RouteDatabaseConfig,
    RouteRestConfig,
    RouteS3Config,
    Route,
    SetDeviceCertificateResponse,
    TwinDocument,
    CreateDeviceRequest,
    CreateHubRequest,
    CreateNetworkRequest,
    CreateRouteRequestDatabaseConfig,
    CreateRouteRequestRestConfig,
    CreateRouteRequestS3Config,
    CreateRouteRequest,
    PatchTwinDocumentRequest,
    PutTwinDocumentRequest,
    SetDeviceCertificateRequest,
    SetHubCARequest,
    UpdateDeviceRequest,
    UpdateHubRequest,
    UpdateRouteRequestDatabaseConfig,
    UpdateRouteRequestRestConfig,
    UpdateRouteRequestS3Config,
    UpdateRouteRequest,
)


def unmarshal_DeviceMessageFiltersRule(data: Any) -> DeviceMessageFiltersRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeviceMessageFiltersRule' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("policy", None)
    if field is not None:
        args["policy"] = field
    else:
        args["policy"] = DeviceMessageFiltersRulePolicy.UNKNOWN

    field = data.get("topics", None)
    if field is not None:
        args["topics"] = field
    else:
        args["topics"] = []

    return DeviceMessageFiltersRule(**args)


def unmarshal_DeviceMessageFilters(data: Any) -> DeviceMessageFilters:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeviceMessageFilters' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("publish", None)
    if field is not None:
        args["publish"] = unmarshal_DeviceMessageFiltersRule(field)
    else:
        args["publish"] = None

    field = data.get("subscribe", None)
    if field is not None:
        args["subscribe"] = unmarshal_DeviceMessageFiltersRule(field)
    else:
        args["subscribe"] = None

    return DeviceMessageFilters(**args)


def unmarshal_Device(data: Any) -> Device:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Device' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

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

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DeviceStatus.UNKNOWN

    field = data.get("hub_id", None)
    if field is not None:
        args["hub_id"] = field
    else:
        args["hub_id"] = None

    field = data.get("last_activity_at", None)
    if field is not None:
        args["last_activity_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["last_activity_at"] = None

    field = data.get("is_connected", None)
    if field is not None:
        args["is_connected"] = field
    else:
        args["is_connected"] = False

    field = data.get("allow_insecure", None)
    if field is not None:
        args["allow_insecure"] = field
    else:
        args["allow_insecure"] = False

    field = data.get("allow_multiple_connections", None)
    if field is not None:
        args["allow_multiple_connections"] = field
    else:
        args["allow_multiple_connections"] = False

    field = data.get("has_custom_certificate", None)
    if field is not None:
        args["has_custom_certificate"] = field
    else:
        args["has_custom_certificate"] = False

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("message_filters", None)
    if field is not None:
        args["message_filters"] = unmarshal_DeviceMessageFilters(field)
    else:
        args["message_filters"] = None

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

    return Device(**args)


def unmarshal_Network(data: Any) -> Network:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Network' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

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

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = NetworkNetworkType.UNKNOWN

    field = data.get("endpoint", None)
    if field is not None:
        args["endpoint"] = field
    else:
        args["endpoint"] = None

    field = data.get("hub_id", None)
    if field is not None:
        args["hub_id"] = field
    else:
        args["hub_id"] = None

    field = data.get("topic_prefix", None)
    if field is not None:
        args["topic_prefix"] = field
    else:
        args["topic_prefix"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return Network(**args)


def unmarshal_HubTwinsGraphiteConfig(data: Any) -> HubTwinsGraphiteConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HubTwinsGraphiteConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("push_uri", None)
    if field is not None:
        args["push_uri"] = field
    else:
        args["push_uri"] = None

    return HubTwinsGraphiteConfig(**args)


def unmarshal_Hub(data: Any) -> Hub:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Hub' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

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

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = HubStatus.UNKNOWN

    field = data.get("product_plan", None)
    if field is not None:
        args["product_plan"] = field
    else:
        args["product_plan"] = HubProductPlan.PLAN_UNKNOWN

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field
    else:
        args["enabled"] = False

    field = data.get("device_count", None)
    if field is not None:
        args["device_count"] = field
    else:
        args["device_count"] = 0

    field = data.get("connected_device_count", None)
    if field is not None:
        args["connected_device_count"] = field
    else:
        args["connected_device_count"] = 0

    field = data.get("endpoint", None)
    if field is not None:
        args["endpoint"] = field
    else:
        args["endpoint"] = None

    field = data.get("disable_events", None)
    if field is not None:
        args["disable_events"] = field
    else:
        args["disable_events"] = False

    field = data.get("events_topic_prefix", None)
    if field is not None:
        args["events_topic_prefix"] = field
    else:
        args["events_topic_prefix"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("enable_device_auto_provisioning", None)
    if field is not None:
        args["enable_device_auto_provisioning"] = field
    else:
        args["enable_device_auto_provisioning"] = False

    field = data.get("has_custom_ca", None)
    if field is not None:
        args["has_custom_ca"] = field
    else:
        args["has_custom_ca"] = False

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

    field = data.get("twins_graphite_config", None)
    if field is not None:
        args["twins_graphite_config"] = unmarshal_HubTwinsGraphiteConfig(field)
    else:
        args["twins_graphite_config"] = None

    return Hub(**args)


def unmarshal_Certificate(data: Any) -> Certificate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Certificate' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("crt", None)
    if field is not None:
        args["crt"] = field
    else:
        args["crt"] = None

    field = data.get("key", None)
    if field is not None:
        args["key"] = field
    else:
        args["key"] = None

    return Certificate(**args)


def unmarshal_CreateDeviceResponse(data: Any) -> CreateDeviceResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateDeviceResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("device", None)
    if field is not None:
        args["device"] = unmarshal_Device(field)
    else:
        args["device"] = None

    field = data.get("certificate", None)
    if field is not None:
        args["certificate"] = unmarshal_Certificate(field)
    else:
        args["certificate"] = None

    return CreateDeviceResponse(**args)


def unmarshal_CreateNetworkResponse(data: Any) -> CreateNetworkResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateNetworkResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("secret", None)
    if field is not None:
        args["secret"] = field
    else:
        args["secret"] = None

    field = data.get("network", None)
    if field is not None:
        args["network"] = unmarshal_Network(field)
    else:
        args["network"] = None

    return CreateNetworkResponse(**args)


def unmarshal_GetDeviceCertificateResponse(data: Any) -> GetDeviceCertificateResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDeviceCertificateResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("certificate_pem", None)
    if field is not None:
        args["certificate_pem"] = field
    else:
        args["certificate_pem"] = None

    field = data.get("device", None)
    if field is not None:
        args["device"] = unmarshal_Device(field)
    else:
        args["device"] = None

    return GetDeviceCertificateResponse(**args)


def unmarshal_GetDeviceMetricsResponse(data: Any) -> GetDeviceMetricsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDeviceMetricsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("metrics", None)
    if field is not None:
        args["metrics"] = (
            [unmarshal_TimeSeries(v) for v in field] if field is not None else None
        )
    else:
        args["metrics"] = []

    return GetDeviceMetricsResponse(**args)


def unmarshal_GetHubCAResponse(data: Any) -> GetHubCAResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetHubCAResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ca_cert_pem", None)
    if field is not None:
        args["ca_cert_pem"] = field
    else:
        args["ca_cert_pem"] = None

    return GetHubCAResponse(**args)


def unmarshal_GetHubMetricsResponse(data: Any) -> GetHubMetricsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetHubMetricsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("metrics", None)
    if field is not None:
        args["metrics"] = (
            [unmarshal_TimeSeries(v) for v in field] if field is not None else None
        )
    else:
        args["metrics"] = []

    return GetHubMetricsResponse(**args)


def unmarshal_ListDevicesResponse(data: Any) -> ListDevicesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDevicesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("devices", None)
    if field is not None:
        args["devices"] = (
            [unmarshal_Device(v) for v in field] if field is not None else None
        )
    else:
        args["devices"] = []

    return ListDevicesResponse(**args)


def unmarshal_ListHubsResponse(data: Any) -> ListHubsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListHubsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("hubs", None)
    if field is not None:
        args["hubs"] = [unmarshal_Hub(v) for v in field] if field is not None else None
    else:
        args["hubs"] = []

    return ListHubsResponse(**args)


def unmarshal_ListNetworksResponse(data: Any) -> ListNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNetworksResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("networks", None)
    if field is not None:
        args["networks"] = (
            [unmarshal_Network(v) for v in field] if field is not None else None
        )
    else:
        args["networks"] = []

    return ListNetworksResponse(**args)


def unmarshal_RouteSummary(data: Any) -> RouteSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteSummary' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

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

    field = data.get("hub_id", None)
    if field is not None:
        args["hub_id"] = field
    else:
        args["hub_id"] = None

    field = data.get("topic", None)
    if field is not None:
        args["topic"] = field
    else:
        args["topic"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = RouteRouteType.UNKNOWN

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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

    return RouteSummary(**args)


def unmarshal_ListRoutesResponse(data: Any) -> ListRoutesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRoutesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("routes", None)
    if field is not None:
        args["routes"] = (
            [unmarshal_RouteSummary(v) for v in field] if field is not None else None
        )
    else:
        args["routes"] = []

    return ListRoutesResponse(**args)


def unmarshal_ListTwinDocumentsResponseDocumentSummary(
    data: Any,
) -> ListTwinDocumentsResponseDocumentSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTwinDocumentsResponseDocumentSummary' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("document_name", None)
    if field is not None:
        args["document_name"] = field
    else:
        args["document_name"] = None

    return ListTwinDocumentsResponseDocumentSummary(**args)


def unmarshal_ListTwinDocumentsResponse(data: Any) -> ListTwinDocumentsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTwinDocumentsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("documents", None)
    if field is not None:
        args["documents"] = (
            [unmarshal_ListTwinDocumentsResponseDocumentSummary(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["documents"] = []

    return ListTwinDocumentsResponse(**args)


def unmarshal_RenewDeviceCertificateResponse(
    data: Any,
) -> RenewDeviceCertificateResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RenewDeviceCertificateResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("device", None)
    if field is not None:
        args["device"] = unmarshal_Device(field)
    else:
        args["device"] = None

    field = data.get("certificate", None)
    if field is not None:
        args["certificate"] = unmarshal_Certificate(field)
    else:
        args["certificate"] = None

    return RenewDeviceCertificateResponse(**args)


def unmarshal_RouteDatabaseConfig(data: Any) -> RouteDatabaseConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteDatabaseConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("engine", None)
    if field is not None:
        args["engine"] = field
    else:
        args["engine"] = RouteDatabaseConfigEngine.UNKNOWN

    field = data.get("host", None)
    if field is not None:
        args["host"] = field
    else:
        args["host"] = None

    field = data.get("port", None)
    if field is not None:
        args["port"] = field
    else:
        args["port"] = None

    field = data.get("dbname", None)
    if field is not None:
        args["dbname"] = field
    else:
        args["dbname"] = None

    field = data.get("username", None)
    if field is not None:
        args["username"] = field
    else:
        args["username"] = None

    field = data.get("password", None)
    if field is not None:
        args["password"] = field
    else:
        args["password"] = None

    field = data.get("query", None)
    if field is not None:
        args["query"] = field
    else:
        args["query"] = None

    return RouteDatabaseConfig(**args)


def unmarshal_RouteRestConfig(data: Any) -> RouteRestConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteRestConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("verb", None)
    if field is not None:
        args["verb"] = field
    else:
        args["verb"] = RouteRestConfigHttpVerb.UNKNOWN

    field = data.get("uri", None)
    if field is not None:
        args["uri"] = field
    else:
        args["uri"] = None

    field = data.get("headers", None)
    if field is not None:
        args["headers"] = field
    else:
        args["headers"] = {}

    return RouteRestConfig(**args)


def unmarshal_RouteS3Config(data: Any) -> RouteS3Config:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteS3Config' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("bucket_region", None)
    if field is not None:
        args["bucket_region"] = field
    else:
        args["bucket_region"] = None

    field = data.get("bucket_name", None)
    if field is not None:
        args["bucket_name"] = field
    else:
        args["bucket_name"] = None

    field = data.get("object_prefix", None)
    if field is not None:
        args["object_prefix"] = field
    else:
        args["object_prefix"] = None

    field = data.get("strategy", None)
    if field is not None:
        args["strategy"] = field
    else:
        args["strategy"] = RouteS3ConfigS3Strategy.UNKNOWN

    return RouteS3Config(**args)


def unmarshal_Route(data: Any) -> Route:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Route' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

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

    field = data.get("hub_id", None)
    if field is not None:
        args["hub_id"] = field
    else:
        args["hub_id"] = None

    field = data.get("topic", None)
    if field is not None:
        args["topic"] = field
    else:
        args["topic"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = RouteRouteType.UNKNOWN

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("s3_config", None)
    if field is not None:
        args["s3_config"] = unmarshal_RouteS3Config(field)
    else:
        args["s3_config"] = None

    field = data.get("db_config", None)
    if field is not None:
        args["db_config"] = unmarshal_RouteDatabaseConfig(field)
    else:
        args["db_config"] = None

    field = data.get("rest_config", None)
    if field is not None:
        args["rest_config"] = unmarshal_RouteRestConfig(field)
    else:
        args["rest_config"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return Route(**args)


def unmarshal_SetDeviceCertificateResponse(data: Any) -> SetDeviceCertificateResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetDeviceCertificateResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("certificate_pem", None)
    if field is not None:
        args["certificate_pem"] = field
    else:
        args["certificate_pem"] = None

    field = data.get("device", None)
    if field is not None:
        args["device"] = unmarshal_Device(field)
    else:
        args["device"] = None

    return SetDeviceCertificateResponse(**args)


def unmarshal_TwinDocument(data: Any) -> TwinDocument:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TwinDocument' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("twin_id", None)
    if field is not None:
        args["twin_id"] = field
    else:
        args["twin_id"] = None

    field = data.get("document_name", None)
    if field is not None:
        args["document_name"] = field
    else:
        args["document_name"] = None

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = 0

    field = data.get("data", None)
    if field is not None:
        args["data"] = field
    else:
        args["data"] = {}

    return TwinDocument(**args)


def marshal_DeviceMessageFiltersRule(
    request: DeviceMessageFiltersRule,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.policy is not None:
        output["policy"] = request.policy

    if request.topics is not None:
        output["topics"] = request.topics

    return output


def marshal_DeviceMessageFilters(
    request: DeviceMessageFilters,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.publish is not None:
        output["publish"] = marshal_DeviceMessageFiltersRule(request.publish, defaults)

    if request.subscribe is not None:
        output["subscribe"] = marshal_DeviceMessageFiltersRule(
            request.subscribe, defaults
        )

    return output


def marshal_CreateDeviceRequest(
    request: CreateDeviceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.hub_id is not None:
        output["hub_id"] = request.hub_id

    if request.allow_insecure is not None:
        output["allow_insecure"] = request.allow_insecure

    if request.allow_multiple_connections is not None:
        output["allow_multiple_connections"] = request.allow_multiple_connections

    if request.name is not None:
        output["name"] = request.name

    if request.message_filters is not None:
        output["message_filters"] = marshal_DeviceMessageFilters(
            request.message_filters, defaults
        )

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_HubTwinsGraphiteConfig(
    request: HubTwinsGraphiteConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.push_uri is not None:
        output["push_uri"] = request.push_uri

    return output


def marshal_CreateHubRequest(
    request: CreateHubRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="twins_graphite_config",
                    value=request.twins_graphite_config,
                    marshal_func=marshal_HubTwinsGraphiteConfig,
                ),
            ]
        ),
    )

    if request.product_plan is not None:
        output["product_plan"] = request.product_plan

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.disable_events is not None:
        output["disable_events"] = request.disable_events

    if request.events_topic_prefix is not None:
        output["events_topic_prefix"] = request.events_topic_prefix

    return output


def marshal_CreateNetworkRequest(
    request: CreateNetworkRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    if request.hub_id is not None:
        output["hub_id"] = request.hub_id

    if request.topic_prefix is not None:
        output["topic_prefix"] = request.topic_prefix

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_CreateRouteRequestDatabaseConfig(
    request: CreateRouteRequestDatabaseConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.host is not None:
        output["host"] = request.host

    if request.port is not None:
        output["port"] = request.port

    if request.dbname is not None:
        output["dbname"] = request.dbname

    if request.username is not None:
        output["username"] = request.username

    if request.password is not None:
        output["password"] = request.password

    if request.query is not None:
        output["query"] = request.query

    if request.engine is not None:
        output["engine"] = request.engine

    return output


def marshal_CreateRouteRequestRestConfig(
    request: CreateRouteRequestRestConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.verb is not None:
        output["verb"] = request.verb

    if request.uri is not None:
        output["uri"] = request.uri

    if request.headers is not None:
        output["headers"] = {key: value for key, value in request.headers.items()}

    return output


def marshal_CreateRouteRequestS3Config(
    request: CreateRouteRequestS3Config,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.bucket_region is not None:
        output["bucket_region"] = request.bucket_region

    if request.bucket_name is not None:
        output["bucket_name"] = request.bucket_name

    if request.object_prefix is not None:
        output["object_prefix"] = request.object_prefix

    if request.strategy is not None:
        output["strategy"] = request.strategy

    return output


def marshal_CreateRouteRequest(
    request: CreateRouteRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="s3_config",
                    value=request.s3_config,
                    marshal_func=marshal_CreateRouteRequestS3Config,
                ),
                OneOfPossibility(
                    param="db_config",
                    value=request.db_config,
                    marshal_func=marshal_CreateRouteRequestDatabaseConfig,
                ),
                OneOfPossibility(
                    param="rest_config",
                    value=request.rest_config,
                    marshal_func=marshal_CreateRouteRequestRestConfig,
                ),
            ]
        ),
    )

    if request.hub_id is not None:
        output["hub_id"] = request.hub_id

    if request.topic is not None:
        output["topic"] = request.topic

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_PatchTwinDocumentRequest(
    request: PatchTwinDocumentRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version

    if request.data is not None:
        output["data"] = request.data

    return output


def marshal_PutTwinDocumentRequest(
    request: PutTwinDocumentRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version

    if request.data is not None:
        output["data"] = request.data

    return output


def marshal_SetDeviceCertificateRequest(
    request: SetDeviceCertificateRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.certificate_pem is not None:
        output["certificate_pem"] = request.certificate_pem

    return output


def marshal_SetHubCARequest(
    request: SetHubCARequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ca_cert_pem is not None:
        output["ca_cert_pem"] = request.ca_cert_pem

    if request.challenge_cert_pem is not None:
        output["challenge_cert_pem"] = request.challenge_cert_pem

    return output


def marshal_UpdateDeviceRequest(
    request: UpdateDeviceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.allow_insecure is not None:
        output["allow_insecure"] = request.allow_insecure

    if request.allow_multiple_connections is not None:
        output["allow_multiple_connections"] = request.allow_multiple_connections

    if request.message_filters is not None:
        output["message_filters"] = marshal_DeviceMessageFilters(
            request.message_filters, defaults
        )

    if request.hub_id is not None:
        output["hub_id"] = request.hub_id

    return output


def marshal_UpdateHubRequest(
    request: UpdateHubRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="twins_graphite_config",
                    value=request.twins_graphite_config,
                    marshal_func=marshal_HubTwinsGraphiteConfig,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.product_plan is not None:
        output["product_plan"] = request.product_plan

    if request.disable_events is not None:
        output["disable_events"] = request.disable_events

    if request.events_topic_prefix is not None:
        output["events_topic_prefix"] = request.events_topic_prefix

    if request.enable_device_auto_provisioning is not None:
        output["enable_device_auto_provisioning"] = (
            request.enable_device_auto_provisioning
        )

    return output


def marshal_UpdateRouteRequestDatabaseConfig(
    request: UpdateRouteRequestDatabaseConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.engine is not None:
        output["engine"] = request.engine

    if request.host is not None:
        output["host"] = request.host

    if request.port is not None:
        output["port"] = request.port

    if request.dbname is not None:
        output["dbname"] = request.dbname

    if request.username is not None:
        output["username"] = request.username

    if request.password is not None:
        output["password"] = request.password

    if request.query is not None:
        output["query"] = request.query

    return output


def marshal_UpdateRouteRequestRestConfig(
    request: UpdateRouteRequestRestConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.verb is not None:
        output["verb"] = request.verb

    if request.uri is not None:
        output["uri"] = request.uri

    if request.headers is not None:
        output["headers"] = request.headers

    return output


def marshal_UpdateRouteRequestS3Config(
    request: UpdateRouteRequestS3Config,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.strategy is not None:
        output["strategy"] = request.strategy

    if request.bucket_region is not None:
        output["bucket_region"] = request.bucket_region

    if request.bucket_name is not None:
        output["bucket_name"] = request.bucket_name

    if request.object_prefix is not None:
        output["object_prefix"] = request.object_prefix

    return output


def marshal_UpdateRouteRequest(
    request: UpdateRouteRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="s3_config",
                    value=request.s3_config,
                    marshal_func=marshal_UpdateRouteRequestS3Config,
                ),
                OneOfPossibility(
                    param="db_config",
                    value=request.db_config,
                    marshal_func=marshal_UpdateRouteRequestDatabaseConfig,
                ),
                OneOfPossibility(
                    param="rest_config",
                    value=request.rest_config,
                    marshal_func=marshal_UpdateRouteRequestRestConfig,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.topic is not None:
        output["topic"] = request.topic

    return output
