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
    DeviceMessageFiltersRulePolicy,
    DeviceStatus,
    HubProductPlan,
    HubStatus,
    ListDevicesRequestOrderBy,
    ListHubsRequestOrderBy,
    ListNetworksRequestOrderBy,
    ListRoutesRequestOrderBy,
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

    args: Dict[str, Any] = {}

    field = data.get("policy", getattr(DeviceMessageFiltersRulePolicy, "UNKNOWN"))
    args["policy"] = field

    field = data.get("topics", None)
    args["topics"] = field

    return DeviceMessageFiltersRule(**args)

def unmarshal_DeviceMessageFilters(data: Any) -> DeviceMessageFilters:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeviceMessageFilters' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("publish", None)
    args["publish"] = unmarshal_DeviceMessageFiltersRule(field) if field is not None else None

    field = data.get("subscribe", None)
    args["subscribe"] = unmarshal_DeviceMessageFiltersRule(field) if field is not None else None

    return DeviceMessageFilters(**args)

def unmarshal_Device(data: Any) -> Device:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Device' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("status", getattr(DeviceStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("hub_id", str())
    args["hub_id"] = field

    field = data.get("last_activity_at", None)
    args["last_activity_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("is_connected", False)
    args["is_connected"] = field

    field = data.get("allow_insecure", False)
    args["allow_insecure"] = field

    field = data.get("allow_multiple_connections", False)
    args["allow_multiple_connections"] = field

    field = data.get("has_custom_certificate", False)
    args["has_custom_certificate"] = field

    field = data.get("message_filters", None)
    args["message_filters"] = unmarshal_DeviceMessageFilters(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Device(**args)

def unmarshal_Network(data: Any) -> Network:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Network' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("type", getattr(NetworkNetworkType, "UNKNOWN"))
    args["type_"] = field

    field = data.get("endpoint", str())
    args["endpoint"] = field

    field = data.get("hub_id", str())
    args["hub_id"] = field

    field = data.get("topic_prefix", str())
    args["topic_prefix"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Network(**args)

def unmarshal_HubTwinsGraphiteConfig(data: Any) -> HubTwinsGraphiteConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HubTwinsGraphiteConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("push_uri", str())
    args["push_uri"] = field

    return HubTwinsGraphiteConfig(**args)

def unmarshal_Hub(data: Any) -> Hub:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Hub' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("status", getattr(HubStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("product_plan", getattr(HubProductPlan, "PLAN_UNKNOWN"))
    args["product_plan"] = field

    field = data.get("enabled", False)
    args["enabled"] = field

    field = data.get("device_count", 0)
    args["device_count"] = field

    field = data.get("connected_device_count", 0)
    args["connected_device_count"] = field

    field = data.get("endpoint", str())
    args["endpoint"] = field

    field = data.get("disable_events", False)
    args["disable_events"] = field

    field = data.get("events_topic_prefix", str())
    args["events_topic_prefix"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("enable_device_auto_provisioning", False)
    args["enable_device_auto_provisioning"] = field

    field = data.get("has_custom_ca", False)
    args["has_custom_ca"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("twins_graphite_config", None)
    args["twins_graphite_config"] = unmarshal_HubTwinsGraphiteConfig(field) if field is not None else None

    return Hub(**args)

def unmarshal_Certificate(data: Any) -> Certificate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Certificate' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("crt", str())
    args["crt"] = field

    field = data.get("key", str())
    args["key"] = field

    return Certificate(**args)

def unmarshal_CreateDeviceResponse(data: Any) -> CreateDeviceResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateDeviceResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("device", None)
    args["device"] = unmarshal_Device(field) if field is not None else None

    field = data.get("certificate", None)
    args["certificate"] = unmarshal_Certificate(field) if field is not None else None

    return CreateDeviceResponse(**args)

def unmarshal_CreateNetworkResponse(data: Any) -> CreateNetworkResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateNetworkResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secret", str())
    args["secret"] = field

    field = data.get("network", None)
    args["network"] = unmarshal_Network(field) if field is not None else None

    return CreateNetworkResponse(**args)

def unmarshal_GetDeviceCertificateResponse(data: Any) -> GetDeviceCertificateResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDeviceCertificateResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("certificate_pem", str())
    args["certificate_pem"] = field

    field = data.get("device", None)
    args["device"] = unmarshal_Device(field) if field is not None else None

    return GetDeviceCertificateResponse(**args)

def unmarshal_GetDeviceMetricsResponse(data: Any) -> GetDeviceMetricsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDeviceMetricsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("metrics", [])
    args["metrics"] = [unmarshal_TimeSeries(v) for v in field] if field is not None else None

    return GetDeviceMetricsResponse(**args)

def unmarshal_GetHubCAResponse(data: Any) -> GetHubCAResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetHubCAResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ca_cert_pem", str())
    args["ca_cert_pem"] = field

    return GetHubCAResponse(**args)

def unmarshal_GetHubMetricsResponse(data: Any) -> GetHubMetricsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetHubMetricsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("metrics", [])
    args["metrics"] = [unmarshal_TimeSeries(v) for v in field] if field is not None else None

    return GetHubMetricsResponse(**args)

def unmarshal_ListDevicesResponse(data: Any) -> ListDevicesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDevicesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("devices", [])
    args["devices"] = [unmarshal_Device(v) for v in field] if field is not None else None

    return ListDevicesResponse(**args)

def unmarshal_ListHubsResponse(data: Any) -> ListHubsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListHubsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("hubs", [])
    args["hubs"] = [unmarshal_Hub(v) for v in field] if field is not None else None

    return ListHubsResponse(**args)

def unmarshal_ListNetworksResponse(data: Any) -> ListNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("networks", [])
    args["networks"] = [unmarshal_Network(v) for v in field] if field is not None else None

    return ListNetworksResponse(**args)

def unmarshal_RouteSummary(data: Any) -> RouteSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("hub_id", str())
    args["hub_id"] = field

    field = data.get("topic", str())
    args["topic"] = field

    field = data.get("type", getattr(RouteRouteType, "UNKNOWN"))
    args["type_"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return RouteSummary(**args)

def unmarshal_ListRoutesResponse(data: Any) -> ListRoutesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRoutesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("routes", [])
    args["routes"] = [unmarshal_RouteSummary(v) for v in field] if field is not None else None

    return ListRoutesResponse(**args)

def unmarshal_ListTwinDocumentsResponseDocumentSummary(data: Any) -> ListTwinDocumentsResponseDocumentSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTwinDocumentsResponseDocumentSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("document_name", str())
    args["document_name"] = field

    return ListTwinDocumentsResponseDocumentSummary(**args)

def unmarshal_ListTwinDocumentsResponse(data: Any) -> ListTwinDocumentsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTwinDocumentsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("documents", [])
    args["documents"] = [unmarshal_ListTwinDocumentsResponseDocumentSummary(v) for v in field] if field is not None else None

    return ListTwinDocumentsResponse(**args)

def unmarshal_RenewDeviceCertificateResponse(data: Any) -> RenewDeviceCertificateResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RenewDeviceCertificateResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("device", None)
    args["device"] = unmarshal_Device(field) if field is not None else None

    field = data.get("certificate", None)
    args["certificate"] = unmarshal_Certificate(field) if field is not None else None

    return RenewDeviceCertificateResponse(**args)

def unmarshal_RouteDatabaseConfig(data: Any) -> RouteDatabaseConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteDatabaseConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("engine", getattr(RouteDatabaseConfigEngine, "UNKNOWN"))
    args["engine"] = field

    field = data.get("host", str())
    args["host"] = field

    field = data.get("port", str())
    args["port"] = field

    field = data.get("dbname", str())
    args["dbname"] = field

    field = data.get("username", str())
    args["username"] = field

    field = data.get("password", str())
    args["password"] = field

    field = data.get("query", str())
    args["query"] = field

    return RouteDatabaseConfig(**args)

def unmarshal_RouteRestConfig(data: Any) -> RouteRestConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteRestConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("verb", getattr(RouteRestConfigHttpVerb, "UNKNOWN"))
    args["verb"] = field

    field = data.get("uri", str())
    args["uri"] = field

    field = data.get("headers", {})
    args["headers"] = field

    return RouteRestConfig(**args)

def unmarshal_RouteS3Config(data: Any) -> RouteS3Config:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteS3Config' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bucket_region", str())
    args["bucket_region"] = field

    field = data.get("bucket_name", str())
    args["bucket_name"] = field

    field = data.get("object_prefix", str())
    args["object_prefix"] = field

    field = data.get("strategy", getattr(RouteS3ConfigS3Strategy, "UNKNOWN"))
    args["strategy"] = field

    return RouteS3Config(**args)

def unmarshal_Route(data: Any) -> Route:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Route' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("hub_id", str())
    args["hub_id"] = field

    field = data.get("topic", str())
    args["topic"] = field

    field = data.get("type", getattr(RouteRouteType, "UNKNOWN"))
    args["type_"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("s3_config", None)
    args["s3_config"] = unmarshal_RouteS3Config(field) if field is not None else None

    field = data.get("db_config", None)
    args["db_config"] = unmarshal_RouteDatabaseConfig(field) if field is not None else None

    field = data.get("rest_config", None)
    args["rest_config"] = unmarshal_RouteRestConfig(field) if field is not None else None

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Route(**args)

def unmarshal_SetDeviceCertificateResponse(data: Any) -> SetDeviceCertificateResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetDeviceCertificateResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("certificate_pem", str())
    args["certificate_pem"] = field

    field = data.get("device", None)
    args["device"] = unmarshal_Device(field) if field is not None else None

    return SetDeviceCertificateResponse(**args)

def unmarshal_TwinDocument(data: Any) -> TwinDocument:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TwinDocument' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("twin_id", str())
    args["twin_id"] = field

    field = data.get("document_name", str())
    args["document_name"] = field

    field = data.get("version", 0)
    args["version"] = field

    field = data.get("data", None)
    args["data"] = field

    return TwinDocument(**args)

def marshal_DeviceMessageFiltersRule(
    request: DeviceMessageFiltersRule,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.policy is not None:
        output["policy"] = str(request.policy)
    else:
        output["policy"] = getattr(DeviceMessageFiltersRulePolicy, "UNKNOWN")

    if request.topics is not None:
        output["topics"] = request.topics
    else:
        output["topics"] = None


    return output

def marshal_DeviceMessageFilters(
    request: DeviceMessageFilters,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.publish is not None:
        output["publish"] = marshal_DeviceMessageFiltersRule(request.publish, defaults)
    else:
        output["publish"] = None

    if request.subscribe is not None:
        output["subscribe"] = marshal_DeviceMessageFiltersRule(request.subscribe, defaults)
    else:
        output["subscribe"] = None


    return output

def marshal_CreateDeviceRequest(
    request: CreateDeviceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.hub_id is not None:
        output["hub_id"] = request.hub_id
    else:
        output["hub_id"] = str()

    if request.allow_insecure is not None:
        output["allow_insecure"] = request.allow_insecure
    else:
        output["allow_insecure"] = False

    if request.allow_multiple_connections is not None:
        output["allow_multiple_connections"] = request.allow_multiple_connections
    else:
        output["allow_multiple_connections"] = False

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.message_filters is not None:
        output["message_filters"] = marshal_DeviceMessageFilters(request.message_filters, defaults)
    else:
        output["message_filters"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None


    return output

def marshal_HubTwinsGraphiteConfig(
    request: HubTwinsGraphiteConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.push_uri is not None:
        output["push_uri"] = request.push_uri
    else:
        output["push_uri"] = str()


    return output

def marshal_CreateHubRequest(
    request: CreateHubRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="twins_graphite_config", value=request.twins_graphite_config,marshal_func=marshal_HubTwinsGraphiteConfig
            ),
        ]),
    )

    if request.product_plan is not None:
        output["product_plan"] = str(request.product_plan)
    else:
        output["product_plan"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.disable_events is not None:
        output["disable_events"] = request.disable_events
    else:
        output["disable_events"] = None

    if request.events_topic_prefix is not None:
        output["events_topic_prefix"] = request.events_topic_prefix
    else:
        output["events_topic_prefix"] = None


    return output

def marshal_CreateNetworkRequest(
    request: CreateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = str()

    if request.hub_id is not None:
        output["hub_id"] = request.hub_id
    else:
        output["hub_id"] = str()

    if request.topic_prefix is not None:
        output["topic_prefix"] = request.topic_prefix
    else:
        output["topic_prefix"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None


    return output

def marshal_CreateRouteRequestDatabaseConfig(
    request: CreateRouteRequestDatabaseConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.host is not None:
        output["host"] = request.host
    else:
        output["host"] = str()

    if request.port is not None:
        output["port"] = request.port
    else:
        output["port"] = str()

    if request.dbname is not None:
        output["dbname"] = request.dbname
    else:
        output["dbname"] = str()

    if request.username is not None:
        output["username"] = request.username
    else:
        output["username"] = str()

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = str()

    if request.query is not None:
        output["query"] = request.query
    else:
        output["query"] = str()

    if request.engine is not None:
        output["engine"] = str(request.engine)
    else:
        output["engine"] = str()


    return output

def marshal_CreateRouteRequestRestConfig(
    request: CreateRouteRequestRestConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.verb is not None:
        output["verb"] = str(request.verb)
    else:
        output["verb"] = str()

    if request.uri is not None:
        output["uri"] = request.uri
    else:
        output["uri"] = str()

    if request.headers is not None:
        output["headers"] = {
            key: value
            for key, value in request.headers.items()
        }
    else:
        output["headers"] = str()


    return output

def marshal_CreateRouteRequestS3Config(
    request: CreateRouteRequestS3Config,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.bucket_region is not None:
        output["bucket_region"] = request.bucket_region
    else:
        output["bucket_region"] = str()

    if request.bucket_name is not None:
        output["bucket_name"] = request.bucket_name
    else:
        output["bucket_name"] = str()

    if request.object_prefix is not None:
        output["object_prefix"] = request.object_prefix
    else:
        output["object_prefix"] = str()

    if request.strategy is not None:
        output["strategy"] = str(request.strategy)
    else:
        output["strategy"] = str()


    return output

def marshal_CreateRouteRequest(
    request: CreateRouteRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="s3_config", value=request.s3_config,marshal_func=marshal_CreateRouteRequestS3Config
            ),
            OneOfPossibility(param="db_config", value=request.db_config,marshal_func=marshal_CreateRouteRequestDatabaseConfig
            ),
            OneOfPossibility(param="rest_config", value=request.rest_config,marshal_func=marshal_CreateRouteRequestRestConfig
            ),
        ]),
    )

    if request.hub_id is not None:
        output["hub_id"] = request.hub_id
    else:
        output["hub_id"] = str()

    if request.topic is not None:
        output["topic"] = request.topic
    else:
        output["topic"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None


    return output

def marshal_PatchTwinDocumentRequest(
    request: PatchTwinDocumentRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version
    else:
        output["version"] = None

    if request.data is not None:
        output["data"] = request.data
    else:
        output["data"] = None


    return output

def marshal_PutTwinDocumentRequest(
    request: PutTwinDocumentRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version
    else:
        output["version"] = None

    if request.data is not None:
        output["data"] = request.data
    else:
        output["data"] = None


    return output

def marshal_SetDeviceCertificateRequest(
    request: SetDeviceCertificateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.certificate_pem is not None:
        output["certificate_pem"] = request.certificate_pem
    else:
        output["certificate_pem"] = str()


    return output

def marshal_SetHubCARequest(
    request: SetHubCARequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ca_cert_pem is not None:
        output["ca_cert_pem"] = request.ca_cert_pem
    else:
        output["ca_cert_pem"] = str()

    if request.challenge_cert_pem is not None:
        output["challenge_cert_pem"] = request.challenge_cert_pem
    else:
        output["challenge_cert_pem"] = str()


    return output

def marshal_UpdateDeviceRequest(
    request: UpdateDeviceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.allow_insecure is not None:
        output["allow_insecure"] = request.allow_insecure
    else:
        output["allow_insecure"] = None

    if request.allow_multiple_connections is not None:
        output["allow_multiple_connections"] = request.allow_multiple_connections
    else:
        output["allow_multiple_connections"] = None

    if request.message_filters is not None:
        output["message_filters"] = marshal_DeviceMessageFilters(request.message_filters, defaults)
    else:
        output["message_filters"] = None

    if request.hub_id is not None:
        output["hub_id"] = request.hub_id
    else:
        output["hub_id"] = None


    return output

def marshal_UpdateHubRequest(
    request: UpdateHubRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="twins_graphite_config", value=request.twins_graphite_config,marshal_func=marshal_HubTwinsGraphiteConfig
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.product_plan is not None:
        output["product_plan"] = str(request.product_plan)
    else:
        output["product_plan"] = None

    if request.disable_events is not None:
        output["disable_events"] = request.disable_events
    else:
        output["disable_events"] = None

    if request.events_topic_prefix is not None:
        output["events_topic_prefix"] = request.events_topic_prefix
    else:
        output["events_topic_prefix"] = None

    if request.enable_device_auto_provisioning is not None:
        output["enable_device_auto_provisioning"] = request.enable_device_auto_provisioning
    else:
        output["enable_device_auto_provisioning"] = None


    return output

def marshal_UpdateRouteRequestDatabaseConfig(
    request: UpdateRouteRequestDatabaseConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.engine is not None:
        output["engine"] = str(request.engine)
    else:
        output["engine"] = str()

    if request.host is not None:
        output["host"] = request.host
    else:
        output["host"] = None

    if request.port is not None:
        output["port"] = request.port
    else:
        output["port"] = None

    if request.dbname is not None:
        output["dbname"] = request.dbname
    else:
        output["dbname"] = None

    if request.username is not None:
        output["username"] = request.username
    else:
        output["username"] = None

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = None

    if request.query is not None:
        output["query"] = request.query
    else:
        output["query"] = None


    return output

def marshal_UpdateRouteRequestRestConfig(
    request: UpdateRouteRequestRestConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.verb is not None:
        output["verb"] = str(request.verb)
    else:
        output["verb"] = str()

    if request.uri is not None:
        output["uri"] = request.uri
    else:
        output["uri"] = None

    if request.headers is not None:
        output["headers"] = request.headers
    else:
        output["headers"] = None


    return output

def marshal_UpdateRouteRequestS3Config(
    request: UpdateRouteRequestS3Config,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.strategy is not None:
        output["strategy"] = str(request.strategy)
    else:
        output["strategy"] = str()

    if request.bucket_region is not None:
        output["bucket_region"] = request.bucket_region
    else:
        output["bucket_region"] = None

    if request.bucket_name is not None:
        output["bucket_name"] = request.bucket_name
    else:
        output["bucket_name"] = None

    if request.object_prefix is not None:
        output["object_prefix"] = request.object_prefix
    else:
        output["object_prefix"] = None


    return output

def marshal_UpdateRouteRequest(
    request: UpdateRouteRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="s3_config", value=request.s3_config,marshal_func=marshal_UpdateRouteRequestS3Config
            ),
            OneOfPossibility(param="db_config", value=request.db_config,marshal_func=marshal_UpdateRouteRequestDatabaseConfig
            ),
            OneOfPossibility(param="rest_config", value=request.rest_config,marshal_func=marshal_UpdateRouteRequestRestConfig
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.topic is not None:
        output["topic"] = request.topic
    else:
        output["topic"] = None


    return output
