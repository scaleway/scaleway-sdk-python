# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from dateutil import parser
from .types import (
    DeviceMessageFiltersRulePolicy,
    HubProductPlan,
    NetworkNetworkType,
    RouteDatabaseConfigEngine,
    RouteRestConfigHttpVerb,
    RouteS3ConfigS3Strategy,
    Certificate,
    CreateDeviceResponse,
    CreateNetworkResponse,
    CreateRouteRequestDatabaseConfig,
    CreateRouteRequestRestConfig,
    CreateRouteRequestS3Config,
    Device,
    DeviceMessageFilters,
    DeviceMessageFiltersRule,
    GetDeviceCertificateResponse,
    GetDeviceMetricsResponse,
    GetHubCAResponse,
    GetHubMetricsResponse,
    Hub,
    HubTwinsGraphiteConfig,
    ListDevicesResponse,
    ListHubsResponse,
    ListNetworksResponse,
    ListRoutesResponse,
    ListTwinDocumentsResponse,
    ListTwinDocumentsResponseDocumentSummary,
    Network,
    RenewDeviceCertificateResponse,
    Route,
    RouteDatabaseConfig,
    RouteRestConfig,
    RouteS3Config,
    RouteSummary,
    SetDeviceCertificateResponse,
    TwinDocument,
    UpdateRouteRequestDatabaseConfig,
    UpdateRouteRequestRestConfig,
    UpdateRouteRequestS3Config,
    CreateHubRequest,
    UpdateHubRequest,
    SetHubCARequest,
    CreateDeviceRequest,
    UpdateDeviceRequest,
    SetDeviceCertificateRequest,
    CreateRouteRequest,
    UpdateRouteRequest,
    CreateNetworkRequest,
    PutTwinDocumentRequest,
    PatchTwinDocumentRequest,
)


def unmarshal_DeviceMessageFiltersRule(data: Any) -> DeviceMessageFiltersRule:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DeviceMessageFiltersRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("policy")
    args["policy"] = field

    field = data.get("topics")
    args["topics"] = field

    return DeviceMessageFiltersRule(**args)


def unmarshal_DeviceMessageFilters(data: Any) -> DeviceMessageFilters:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DeviceMessageFilters' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("publish")
    args["publish"] = (
        unmarshal_DeviceMessageFiltersRule(field) if field is not None else None
    )

    field = data.get("subscribe")
    args["subscribe"] = (
        unmarshal_DeviceMessageFiltersRule(field) if field is not None else None
    )

    return DeviceMessageFilters(**args)


def unmarshal_HubTwinsGraphiteConfig(data: Any) -> HubTwinsGraphiteConfig:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'HubTwinsGraphiteConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("push_uri")
    args["push_uri"] = field

    return HubTwinsGraphiteConfig(**args)


def unmarshal_Certificate(data: Any) -> Certificate:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Certificate' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("crt")
    args["crt"] = field

    field = data.get("key")
    args["key"] = field

    return Certificate(**args)


def unmarshal_Device(data: Any) -> Device:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Device' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("allow_insecure")
    args["allow_insecure"] = field

    field = data.get("allow_multiple_connections")
    args["allow_multiple_connections"] = field

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description")
    args["description"] = field

    field = data.get("has_custom_certificate")
    args["has_custom_certificate"] = field

    field = data.get("hub_id")
    args["hub_id"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("is_connected")
    args["is_connected"] = field

    field = data.get("last_activity_at")
    args["last_activity_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("message_filters")
    args["message_filters"] = (
        unmarshal_DeviceMessageFilters(field) if field is not None else None
    )

    field = data.get("name")
    args["name"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Device(**args)


def unmarshal_Hub(data: Any) -> Hub:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Hub' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("connected_device_count")
    args["connected_device_count"] = field

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("device_count")
    args["device_count"] = field

    field = data.get("disable_events")
    args["disable_events"] = field

    field = data.get("enable_device_auto_provisioning")
    args["enable_device_auto_provisioning"] = field

    field = data.get("enabled")
    args["enabled"] = field

    field = data.get("endpoint")
    args["endpoint"] = field

    field = data.get("events_topic_prefix")
    args["events_topic_prefix"] = field

    field = data.get("has_custom_ca")
    args["has_custom_ca"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("product_plan")
    args["product_plan"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("region")
    args["region"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("twins_graphite_config")
    args["twins_graphite_config"] = (
        unmarshal_HubTwinsGraphiteConfig(field) if field is not None else None
    )

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Hub(**args)


def unmarshal_ListTwinDocumentsResponseDocumentSummary(
    data: Any,
) -> ListTwinDocumentsResponseDocumentSummary:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListTwinDocumentsResponseDocumentSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("document_name")
    args["document_name"] = field

    return ListTwinDocumentsResponseDocumentSummary(**args)


def unmarshal_Network(data: Any) -> Network:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Network' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("endpoint")
    args["endpoint"] = field

    field = data.get("hub_id")
    args["hub_id"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("topic_prefix")
    args["topic_prefix"] = field

    field = data.get("type_")
    args["type_"] = field

    return Network(**args)


def unmarshal_RouteDatabaseConfig(data: Any) -> RouteDatabaseConfig:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RouteDatabaseConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dbname")
    args["dbname"] = field

    field = data.get("engine")
    args["engine"] = field

    field = data.get("host")
    args["host"] = field

    field = data.get("password")
    args["password"] = field

    field = data.get("port")
    args["port"] = field

    field = data.get("query")
    args["query"] = field

    field = data.get("username")
    args["username"] = field

    return RouteDatabaseConfig(**args)


def unmarshal_RouteRestConfig(data: Any) -> RouteRestConfig:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RouteRestConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("headers")
    args["headers"] = field

    field = data.get("uri")
    args["uri"] = field

    field = data.get("verb")
    args["verb"] = field

    return RouteRestConfig(**args)


def unmarshal_RouteS3Config(data: Any) -> RouteS3Config:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RouteS3Config' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bucket_name")
    args["bucket_name"] = field

    field = data.get("bucket_region")
    args["bucket_region"] = field

    field = data.get("object_prefix")
    args["object_prefix"] = field

    field = data.get("strategy")
    args["strategy"] = field

    return RouteS3Config(**args)


def unmarshal_RouteSummary(data: Any) -> RouteSummary:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RouteSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("hub_id")
    args["hub_id"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("topic")
    args["topic"] = field

    field = data.get("type_")
    args["type_"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return RouteSummary(**args)


def unmarshal_CreateDeviceResponse(data: Any) -> CreateDeviceResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateDeviceResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("certificate")
    args["certificate"] = unmarshal_Certificate(field) if field is not None else None

    field = data.get("device")
    args["device"] = unmarshal_Device(field) if field is not None else None

    return CreateDeviceResponse(**args)


def unmarshal_CreateNetworkResponse(data: Any) -> CreateNetworkResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateNetworkResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("network")
    args["network"] = unmarshal_Network(field) if field is not None else None

    field = data.get("secret")
    args["secret"] = field

    return CreateNetworkResponse(**args)


def unmarshal_GetDeviceCertificateResponse(data: Any) -> GetDeviceCertificateResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetDeviceCertificateResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("certificate_pem")
    args["certificate_pem"] = field

    field = data.get("device")
    args["device"] = unmarshal_Device(field) if field is not None else None

    return GetDeviceCertificateResponse(**args)


def unmarshal_GetDeviceMetricsResponse(data: Any) -> GetDeviceMetricsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetDeviceMetricsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("metrics")
    args["metrics"] = [unmarshal_TimeSeries(v) for v in data["metrics"]]

    return GetDeviceMetricsResponse(**args)


def unmarshal_GetHubCAResponse(data: Any) -> GetHubCAResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetHubCAResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ca_cert_pem")
    args["ca_cert_pem"] = field

    return GetHubCAResponse(**args)


def unmarshal_GetHubMetricsResponse(data: Any) -> GetHubMetricsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetHubMetricsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("metrics")
    args["metrics"] = [unmarshal_TimeSeries(v) for v in data["metrics"]]

    return GetHubMetricsResponse(**args)


def unmarshal_ListDevicesResponse(data: Any) -> ListDevicesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDevicesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("devices")
    args["devices"] = [unmarshal_Device(v) for v in data["devices"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListDevicesResponse(**args)


def unmarshal_ListHubsResponse(data: Any) -> ListHubsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListHubsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hubs")
    args["hubs"] = [unmarshal_Hub(v) for v in data["hubs"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListHubsResponse(**args)


def unmarshal_ListNetworksResponse(data: Any) -> ListNetworksResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("networks")
    args["networks"] = [unmarshal_Network(v) for v in data["networks"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListNetworksResponse(**args)


def unmarshal_ListRoutesResponse(data: Any) -> ListRoutesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListRoutesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("routes")
    args["routes"] = [unmarshal_RouteSummary(v) for v in data["routes"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListRoutesResponse(**args)


def unmarshal_ListTwinDocumentsResponse(data: Any) -> ListTwinDocumentsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListTwinDocumentsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("documents")
    args["documents"] = [
        unmarshal_ListTwinDocumentsResponseDocumentSummary(v) for v in data["documents"]
    ]

    return ListTwinDocumentsResponse(**args)


def unmarshal_RenewDeviceCertificateResponse(
    data: Any,
) -> RenewDeviceCertificateResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RenewDeviceCertificateResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("certificate")
    args["certificate"] = unmarshal_Certificate(field) if field is not None else None

    field = data.get("device")
    args["device"] = unmarshal_Device(field) if field is not None else None

    return RenewDeviceCertificateResponse(**args)


def unmarshal_Route(data: Any) -> Route:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Route' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("db_config")
    args["db_config"] = (
        unmarshal_RouteDatabaseConfig(field) if field is not None else None
    )

    field = data.get("hub_id")
    args["hub_id"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("rest_config")
    args["rest_config"] = (
        unmarshal_RouteRestConfig(field) if field is not None else None
    )

    field = data.get("s3_config")
    args["s3_config"] = unmarshal_RouteS3Config(field) if field is not None else None

    field = data.get("topic")
    args["topic"] = field

    field = data.get("type_")
    args["type_"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Route(**args)


def unmarshal_SetDeviceCertificateResponse(data: Any) -> SetDeviceCertificateResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetDeviceCertificateResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("certificate_pem")
    args["certificate_pem"] = field

    field = data.get("device")
    args["device"] = unmarshal_Device(field) if field is not None else None

    return SetDeviceCertificateResponse(**args)


def unmarshal_TwinDocument(data: Any) -> TwinDocument:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'TwinDocument' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("data")
    args["data"] = field

    field = data.get("document_name")
    args["document_name"] = field

    field = data.get("twin_id")
    args["twin_id"] = field

    field = data.get("version")
    args["version"] = field

    return TwinDocument(**args)


def marshal_DeviceMessageFiltersRule(
    request: DeviceMessageFiltersRule,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "policy": DeviceMessageFiltersRulePolicy(request.policy),
        "topics": request.topics,
    }


def marshal_CreateRouteRequestDatabaseConfig(
    request: CreateRouteRequestDatabaseConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "dbname": request.dbname,
        "engine": RouteDatabaseConfigEngine(request.engine),
        "host": request.host,
        "password": request.password,
        "port": request.port,
        "query": request.query,
        "username": request.username,
    }


def marshal_CreateRouteRequestRestConfig(
    request: CreateRouteRequestRestConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "headers": request.headers,
        "uri": request.uri,
        "verb": RouteRestConfigHttpVerb(request.verb),
    }


def marshal_CreateRouteRequestS3Config(
    request: CreateRouteRequestS3Config,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "bucket_name": request.bucket_name,
        "bucket_region": request.bucket_region,
        "object_prefix": request.object_prefix,
        "strategy": RouteS3ConfigS3Strategy(request.strategy),
    }


def marshal_DeviceMessageFilters(
    request: DeviceMessageFilters,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "publish": marshal_DeviceMessageFiltersRule(request.publish, defaults)
        if request.publish is not None
        else None,
        "subscribe": marshal_DeviceMessageFiltersRule(request.subscribe, defaults)
        if request.subscribe is not None
        else None,
    }


def marshal_HubTwinsGraphiteConfig(
    request: HubTwinsGraphiteConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "push_uri": request.push_uri,
    }


def marshal_UpdateRouteRequestDatabaseConfig(
    request: UpdateRouteRequestDatabaseConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "dbname": request.dbname,
        "engine": RouteDatabaseConfigEngine(request.engine),
        "host": request.host,
        "password": request.password,
        "port": request.port,
        "query": request.query,
        "username": request.username,
    }


def marshal_UpdateRouteRequestRestConfig(
    request: UpdateRouteRequestRestConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "headers": request.headers,
        "uri": request.uri,
        "verb": RouteRestConfigHttpVerb(request.verb),
    }


def marshal_UpdateRouteRequestS3Config(
    request: UpdateRouteRequestS3Config,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "bucket_name": request.bucket_name,
        "bucket_region": request.bucket_region,
        "object_prefix": request.object_prefix,
        "strategy": RouteS3ConfigS3Strategy(request.strategy),
    }


def marshal_CreateDeviceRequest(
    request: CreateDeviceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "allow_insecure": request.allow_insecure,
        "allow_multiple_connections": request.allow_multiple_connections,
        "description": request.description,
        "hub_id": request.hub_id,
        "message_filters": marshal_DeviceMessageFilters(
            request.message_filters, defaults
        )
        if request.message_filters is not None
        else None,
        "name": request.name,
    }


def marshal_CreateHubRequest(
    request: CreateHubRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "twins_graphite_config", request.twins_graphite_config
                ),
            ]
        ),
        "disable_events": request.disable_events,
        "events_topic_prefix": request.events_topic_prefix,
        "name": request.name,
        "product_plan": HubProductPlan(request.product_plan)
        if request.product_plan is not None
        else None,
        "project_id": request.project_id or defaults.default_project_id,
    }


def marshal_CreateNetworkRequest(
    request: CreateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "hub_id": request.hub_id,
        "name": request.name,
        "topic_prefix": request.topic_prefix,
        "type": NetworkNetworkType(request.type_)
        if request.type_ is not None
        else None,
    }


def marshal_CreateRouteRequest(
    request: CreateRouteRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("s3_config", request.s3_config),
                OneOfPossibility("db_config", request.db_config),
                OneOfPossibility("rest_config", request.rest_config),
            ]
        ),
        "hub_id": request.hub_id,
        "name": request.name,
        "topic": request.topic,
    }


def marshal_PatchTwinDocumentRequest(
    request: PatchTwinDocumentRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "data": request.data,
        "version": request.version,
    }


def marshal_PutTwinDocumentRequest(
    request: PutTwinDocumentRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "data": request.data,
        "version": request.version,
    }


def marshal_SetDeviceCertificateRequest(
    request: SetDeviceCertificateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "certificate_pem": request.certificate_pem,
    }


def marshal_SetHubCARequest(
    request: SetHubCARequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "ca_cert_pem": request.ca_cert_pem,
        "challenge_cert_pem": request.challenge_cert_pem,
    }


def marshal_UpdateDeviceRequest(
    request: UpdateDeviceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "allow_insecure": request.allow_insecure,
        "allow_multiple_connections": request.allow_multiple_connections,
        "description": request.description,
        "hub_id": request.hub_id,
        "message_filters": marshal_DeviceMessageFilters(
            request.message_filters, defaults
        )
        if request.message_filters is not None
        else None,
    }


def marshal_UpdateHubRequest(
    request: UpdateHubRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "twins_graphite_config", request.twins_graphite_config
                ),
            ]
        ),
        "disable_events": request.disable_events,
        "enable_device_auto_provisioning": request.enable_device_auto_provisioning,
        "events_topic_prefix": request.events_topic_prefix,
        "name": request.name,
        "product_plan": HubProductPlan(request.product_plan),
    }


def marshal_UpdateRouteRequest(
    request: UpdateRouteRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("s3_config", request.s3_config),
                OneOfPossibility("db_config", request.db_config),
                OneOfPossibility("rest_config", request.rest_config),
            ]
        ),
        "name": request.name,
        "topic": request.topic,
    }
