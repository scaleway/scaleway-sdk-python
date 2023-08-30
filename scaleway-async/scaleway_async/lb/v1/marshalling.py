# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from dateutil import parser
from .types import (
    AclActionRedirectRedirectType,
    AclActionType,
    AclHttpFilter,
    ForwardPortAlgorithm,
    OnMarkedDownAction,
    Protocol,
    ProxyProtocol,
    SSLCompatibilityLevel,
    StickySessionsType,
    Acl,
    AclAction,
    AclActionRedirect,
    AclMatch,
    AclSpec,
    Backend,
    BackendServerStats,
    Certificate,
    CreateCertificateRequestCustomCertificate,
    CreateCertificateRequestLetsencryptConfig,
    Frontend,
    HealthCheck,
    HealthCheckHttpConfig,
    HealthCheckHttpsConfig,
    HealthCheckLdapConfig,
    HealthCheckMysqlConfig,
    HealthCheckPgsqlConfig,
    HealthCheckRedisConfig,
    HealthCheckTcpConfig,
    Instance,
    Ip,
    Lb,
    LbStats,
    LbType,
    ListAclResponse,
    ListBackendStatsResponse,
    ListBackendsResponse,
    ListCertificatesResponse,
    ListFrontendsResponse,
    ListIpsResponse,
    ListLbPrivateNetworksResponse,
    ListLbTypesResponse,
    ListLbsResponse,
    ListRoutesResponse,
    ListSubscriberResponse,
    PrivateNetwork,
    PrivateNetworkDHCPConfig,
    PrivateNetworkIpamConfig,
    PrivateNetworkStaticConfig,
    Route,
    RouteMatch,
    SetAclsResponse,
    Subscriber,
    SubscriberEmailConfig,
    SubscriberWebhookConfig,
    CreateLbRequest,
    UpdateLbRequest,
    MigrateLbRequest,
    CreateIpRequest,
    UpdateIpRequest,
    CreateBackendRequest,
    UpdateBackendRequest,
    AddBackendServersRequest,
    RemoveBackendServersRequest,
    SetBackendServersRequest,
    UpdateHealthCheckRequest,
    CreateFrontendRequest,
    UpdateFrontendRequest,
    CreateRouteRequest,
    UpdateRouteRequest,
    CreateAclRequest,
    UpdateAclRequest,
    CreateCertificateRequest,
    UpdateCertificateRequest,
    CreateSubscriberRequest,
    UpdateSubscriberRequest,
    SubscribeToLbRequest,
    AttachPrivateNetworkRequest,
    ZonedApiCreateLbRequest,
    ZonedApiUpdateLbRequest,
    ZonedApiMigrateLbRequest,
    ZonedApiCreateIpRequest,
    ZonedApiUpdateIpRequest,
    ZonedApiCreateBackendRequest,
    ZonedApiUpdateBackendRequest,
    ZonedApiAddBackendServersRequest,
    ZonedApiRemoveBackendServersRequest,
    ZonedApiSetBackendServersRequest,
    ZonedApiUpdateHealthCheckRequest,
    ZonedApiCreateFrontendRequest,
    ZonedApiUpdateFrontendRequest,
    ZonedApiCreateRouteRequest,
    ZonedApiUpdateRouteRequest,
    ZonedApiCreateAclRequest,
    ZonedApiUpdateAclRequest,
    ZonedApiSetAclsRequest,
    ZonedApiCreateCertificateRequest,
    ZonedApiUpdateCertificateRequest,
    ZonedApiCreateSubscriberRequest,
    ZonedApiUpdateSubscriberRequest,
    ZonedApiSubscribeToLbRequest,
    ZonedApiAttachPrivateNetworkRequest,
)


def unmarshal_SubscriberEmailConfig(data: Any) -> SubscriberEmailConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SubscriberEmailConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("email", None)
    args["email"] = field

    return SubscriberEmailConfig(**args)


def unmarshal_SubscriberWebhookConfig(data: Any) -> SubscriberWebhookConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SubscriberWebhookConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("uri", None)
    args["uri"] = field

    return SubscriberWebhookConfig(**args)


def unmarshal_HealthCheckHttpConfig(data: Any) -> HealthCheckHttpConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckHttpConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("code", None)
    args["code"] = field

    field = data.get("host_header", None)
    args["host_header"] = field

    field = data.get("method", None)
    args["method"] = field

    field = data.get("uri", None)
    args["uri"] = field

    return HealthCheckHttpConfig(**args)


def unmarshal_HealthCheckHttpsConfig(data: Any) -> HealthCheckHttpsConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckHttpsConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("code", None)
    args["code"] = field

    field = data.get("host_header", None)
    args["host_header"] = field

    field = data.get("method", None)
    args["method"] = field

    field = data.get("sni", None)
    args["sni"] = field

    field = data.get("uri", None)
    args["uri"] = field

    return HealthCheckHttpsConfig(**args)


def unmarshal_HealthCheckLdapConfig(data: Any) -> HealthCheckLdapConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckLdapConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return HealthCheckLdapConfig(**args)


def unmarshal_HealthCheckMysqlConfig(data: Any) -> HealthCheckMysqlConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckMysqlConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("user", None)
    args["user"] = field

    return HealthCheckMysqlConfig(**args)


def unmarshal_HealthCheckPgsqlConfig(data: Any) -> HealthCheckPgsqlConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckPgsqlConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("user", None)
    args["user"] = field

    return HealthCheckPgsqlConfig(**args)


def unmarshal_HealthCheckRedisConfig(data: Any) -> HealthCheckRedisConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckRedisConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return HealthCheckRedisConfig(**args)


def unmarshal_HealthCheckTcpConfig(data: Any) -> HealthCheckTcpConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckTcpConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return HealthCheckTcpConfig(**args)


def unmarshal_Instance(data: Any) -> Instance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Instance' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("ip_address", None)
    args["ip_address"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("zone", None)
    args["zone"] = field

    return Instance(**args)


def unmarshal_Ip(data: Any) -> Ip:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Ip' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("ip_address", None)
    args["ip_address"] = field

    field = data.get("lb_id", None)
    args["lb_id"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("reverse", None)
    args["reverse"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return Ip(**args)


def unmarshal_Subscriber(data: Any) -> Subscriber:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Subscriber' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("email_config", None)
    args["email_config"] = (
        unmarshal_SubscriberEmailConfig(field) if field is not None else None
    )

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("webhook_config", None)
    args["webhook_config"] = (
        unmarshal_SubscriberWebhookConfig(field) if field is not None else None
    )

    return Subscriber(**args)


def unmarshal_HealthCheck(data: Any) -> HealthCheck:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheck' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("check_delay", None)
    args["check_delay"] = field

    field = data.get("check_max_retries", None)
    args["check_max_retries"] = field

    field = data.get("check_send_proxy", None)
    args["check_send_proxy"] = field

    field = data.get("check_timeout", None)
    args["check_timeout"] = field

    field = data.get("http_config", None)
    args["http_config"] = (
        unmarshal_HealthCheckHttpConfig(field) if field is not None else None
    )

    field = data.get("https_config", None)
    args["https_config"] = (
        unmarshal_HealthCheckHttpsConfig(field) if field is not None else None
    )

    field = data.get("ldap_config", None)
    args["ldap_config"] = (
        unmarshal_HealthCheckLdapConfig(field) if field is not None else None
    )

    field = data.get("mysql_config", None)
    args["mysql_config"] = (
        unmarshal_HealthCheckMysqlConfig(field) if field is not None else None
    )

    field = data.get("pgsql_config", None)
    args["pgsql_config"] = (
        unmarshal_HealthCheckPgsqlConfig(field) if field is not None else None
    )

    field = data.get("port", None)
    args["port"] = field

    field = data.get("redis_config", None)
    args["redis_config"] = (
        unmarshal_HealthCheckRedisConfig(field) if field is not None else None
    )

    field = data.get("tcp_config", None)
    args["tcp_config"] = (
        unmarshal_HealthCheckTcpConfig(field) if field is not None else None
    )

    field = data.get("transient_check_delay", None)
    args["transient_check_delay"] = field

    return HealthCheck(**args)


def unmarshal_Lb(data: Any) -> Lb:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Lb' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("backend_count", None)
    args["backend_count"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("frontend_count", None)
    args["frontend_count"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("instances", None)
    args["instances"] = (
        [unmarshal_Instance(v) for v in field] if field is not None else None
    )

    field = data.get("ip", None)
    args["ip"] = [unmarshal_Ip(v) for v in field] if field is not None else None

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("private_network_count", None)
    args["private_network_count"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("route_count", None)
    args["route_count"] = field

    field = data.get("ssl_compatibility_level", None)
    args["ssl_compatibility_level"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("subscriber", None)
    args["subscriber"] = unmarshal_Subscriber(field) if field is not None else None

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("type", None)
    args["type_"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("zone", None)
    args["zone"] = field

    return Lb(**args)


def unmarshal_AclActionRedirect(data: Any) -> AclActionRedirect:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AclActionRedirect' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("code", None)
    args["code"] = field

    field = data.get("target", None)
    args["target"] = field

    field = data.get("type", None)
    args["type_"] = field

    return AclActionRedirect(**args)


def unmarshal_Backend(data: Any) -> Backend:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Backend' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("failover_host", None)
    args["failover_host"] = field

    field = data.get("forward_port", None)
    args["forward_port"] = field

    field = data.get("forward_port_algorithm", None)
    args["forward_port_algorithm"] = field

    field = data.get("forward_protocol", None)
    args["forward_protocol"] = field

    field = data.get("health_check", None)
    args["health_check"] = unmarshal_HealthCheck(field) if field is not None else None

    field = data.get("id", None)
    args["id"] = field

    field = data.get("ignore_ssl_server_verify", None)
    args["ignore_ssl_server_verify"] = field

    field = data.get("lb", None)
    args["lb"] = unmarshal_Lb(field) if field is not None else None

    field = data.get("max_connections", None)
    args["max_connections"] = field

    field = data.get("max_retries", None)
    args["max_retries"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("on_marked_down_action", None)
    args["on_marked_down_action"] = field

    field = data.get("pool", None)
    args["pool"] = field

    field = data.get("proxy_protocol", None)
    args["proxy_protocol"] = field

    field = data.get("redispatch_attempt_count", None)
    args["redispatch_attempt_count"] = field

    field = data.get("send_proxy_v2", None)
    args["send_proxy_v2"] = field

    field = data.get("ssl_bridging", None)
    args["ssl_bridging"] = field

    field = data.get("sticky_sessions", None)
    args["sticky_sessions"] = field

    field = data.get("sticky_sessions_cookie_name", None)
    args["sticky_sessions_cookie_name"] = field

    field = data.get("timeout_connect", None)
    args["timeout_connect"] = field

    field = data.get("timeout_queue", None)
    args["timeout_queue"] = field

    field = data.get("timeout_server", None)
    args["timeout_server"] = field

    field = data.get("timeout_tunnel", None)
    args["timeout_tunnel"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Backend(**args)


def unmarshal_Certificate(data: Any) -> Certificate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Certificate' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("common_name", None)
    args["common_name"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("fingerprint", None)
    args["fingerprint"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("lb", None)
    args["lb"] = unmarshal_Lb(field) if field is not None else None

    field = data.get("name", None)
    args["name"] = field

    field = data.get("not_valid_after", None)
    args["not_valid_after"] = (
        parser.isoparse(field) if isinstance(field, str) else field
    )

    field = data.get("not_valid_before", None)
    args["not_valid_before"] = (
        parser.isoparse(field) if isinstance(field, str) else field
    )

    field = data.get("status", None)
    args["status"] = field

    field = data.get("status_details", None)
    args["status_details"] = field

    field = data.get("subject_alternative_name", None)
    args["subject_alternative_name"] = field

    field = data.get("type", None)
    args["type_"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Certificate(**args)


def unmarshal_AclAction(data: Any) -> AclAction:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AclAction' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("redirect", None)
    args["redirect"] = unmarshal_AclActionRedirect(field) if field is not None else None

    field = data.get("type", None)
    args["type_"] = field

    return AclAction(**args)


def unmarshal_AclMatch(data: Any) -> AclMatch:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AclMatch' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("http_filter", None)
    args["http_filter"] = field

    field = data.get("http_filter_option", None)
    args["http_filter_option"] = field

    field = data.get("http_filter_value", None)
    args["http_filter_value"] = field

    field = data.get("invert", None)
    args["invert"] = field

    field = data.get("ip_subnet", None)
    args["ip_subnet"] = field

    return AclMatch(**args)


def unmarshal_Frontend(data: Any) -> Frontend:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Frontend' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("backend", None)
    args["backend"] = unmarshal_Backend(field) if field is not None else None

    field = data.get("certificate", None)
    args["certificate"] = unmarshal_Certificate(field) if field is not None else None

    field = data.get("certificate_ids", None)
    args["certificate_ids"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("enable_http3", None)
    args["enable_http3"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("inbound_port", None)
    args["inbound_port"] = field

    field = data.get("lb", None)
    args["lb"] = unmarshal_Lb(field) if field is not None else None

    field = data.get("name", None)
    args["name"] = field

    field = data.get("timeout_client", None)
    args["timeout_client"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Frontend(**args)


def unmarshal_PrivateNetworkDHCPConfig(data: Any) -> PrivateNetworkDHCPConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetworkDHCPConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip_id", None)
    args["ip_id"] = field

    return PrivateNetworkDHCPConfig(**args)


def unmarshal_PrivateNetworkIpamConfig(data: Any) -> PrivateNetworkIpamConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetworkIpamConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return PrivateNetworkIpamConfig(**args)


def unmarshal_PrivateNetworkStaticConfig(data: Any) -> PrivateNetworkStaticConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetworkStaticConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip_address", None)
    args["ip_address"] = field

    return PrivateNetworkStaticConfig(**args)


def unmarshal_RouteMatch(data: Any) -> RouteMatch:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteMatch' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("host_header", None)
    args["host_header"] = field

    field = data.get("sni", None)
    args["sni"] = field

    return RouteMatch(**args)


def unmarshal_Acl(data: Any) -> Acl:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Acl' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("action", None)
    args["action"] = unmarshal_AclAction(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("frontend", None)
    args["frontend"] = unmarshal_Frontend(field) if field is not None else None

    field = data.get("id", None)
    args["id"] = field

    field = data.get("index", None)
    args["index"] = field

    field = data.get("match", None)
    args["match"] = unmarshal_AclMatch(field) if field is not None else None

    field = data.get("name", None)
    args["name"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Acl(**args)


def unmarshal_BackendServerStats(data: Any) -> BackendServerStats:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BackendServerStats' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("backend_id", None)
    args["backend_id"] = field

    field = data.get("instance_id", None)
    args["instance_id"] = field

    field = data.get("ip", None)
    args["ip"] = field

    field = data.get("last_health_check_status", None)
    args["last_health_check_status"] = field

    field = data.get("server_state", None)
    args["server_state"] = field

    field = data.get("server_state_changed_at", None)
    args["server_state_changed_at"] = (
        parser.isoparse(field) if isinstance(field, str) else field
    )

    return BackendServerStats(**args)


def unmarshal_LbType(data: Any) -> LbType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LbType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", None)
    args["description"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("stock_status", None)
    args["stock_status"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return LbType(**args)


def unmarshal_PrivateNetwork(data: Any) -> PrivateNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("dhcp_config", None)
    args["dhcp_config"] = (
        unmarshal_PrivateNetworkDHCPConfig(field) if field is not None else None
    )

    field = data.get("ipam_config", None)
    args["ipam_config"] = (
        unmarshal_PrivateNetworkIpamConfig(field) if field is not None else None
    )

    field = data.get("lb", None)
    args["lb"] = unmarshal_Lb(field) if field is not None else None

    field = data.get("private_network_id", None)
    args["private_network_id"] = field

    field = data.get("static_config", None)
    args["static_config"] = (
        unmarshal_PrivateNetworkStaticConfig(field) if field is not None else None
    )

    field = data.get("status", None)
    args["status"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return PrivateNetwork(**args)


def unmarshal_Route(data: Any) -> Route:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Route' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("backend_id", None)
    args["backend_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("frontend_id", None)
    args["frontend_id"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("match", None)
    args["match"] = unmarshal_RouteMatch(field) if field is not None else None

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Route(**args)


def unmarshal_LbStats(data: Any) -> LbStats:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LbStats' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("backend_servers_stats", None)
    args["backend_servers_stats"] = (
        [unmarshal_BackendServerStats(v) for v in field] if field is not None else None
    )

    return LbStats(**args)


def unmarshal_ListAclResponse(data: Any) -> ListAclResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAclResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("acls", None)
    args["acls"] = [unmarshal_Acl(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListAclResponse(**args)


def unmarshal_ListBackendStatsResponse(data: Any) -> ListBackendStatsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBackendStatsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("backend_servers_stats", None)
    args["backend_servers_stats"] = (
        [unmarshal_BackendServerStats(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListBackendStatsResponse(**args)


def unmarshal_ListBackendsResponse(data: Any) -> ListBackendsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBackendsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("backends", None)
    args["backends"] = (
        [unmarshal_Backend(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListBackendsResponse(**args)


def unmarshal_ListCertificatesResponse(data: Any) -> ListCertificatesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCertificatesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("certificates", None)
    args["certificates"] = (
        [unmarshal_Certificate(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListCertificatesResponse(**args)


def unmarshal_ListFrontendsResponse(data: Any) -> ListFrontendsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFrontendsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("frontends", None)
    args["frontends"] = (
        [unmarshal_Frontend(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListFrontendsResponse(**args)


def unmarshal_ListIpsResponse(data: Any) -> ListIpsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListIpsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ips", None)
    args["ips"] = [unmarshal_Ip(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListIpsResponse(**args)


def unmarshal_ListLbPrivateNetworksResponse(data: Any) -> ListLbPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLbPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_network", None)
    args["private_network"] = (
        [unmarshal_PrivateNetwork(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListLbPrivateNetworksResponse(**args)


def unmarshal_ListLbTypesResponse(data: Any) -> ListLbTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLbTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("lb_types", None)
    args["lb_types"] = (
        [unmarshal_LbType(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListLbTypesResponse(**args)


def unmarshal_ListLbsResponse(data: Any) -> ListLbsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLbsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("lbs", None)
    args["lbs"] = [unmarshal_Lb(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListLbsResponse(**args)


def unmarshal_ListRoutesResponse(data: Any) -> ListRoutesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRoutesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("routes", None)
    args["routes"] = [unmarshal_Route(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListRoutesResponse(**args)


def unmarshal_ListSubscriberResponse(data: Any) -> ListSubscriberResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSubscriberResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subscribers", None)
    args["subscribers"] = (
        [unmarshal_Subscriber(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListSubscriberResponse(**args)


def unmarshal_SetAclsResponse(data: Any) -> SetAclsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetAclsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("acls", None)
    args["acls"] = [unmarshal_Acl(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return SetAclsResponse(**args)


def marshal_AclActionRedirect(
    request: AclActionRedirect,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.code is not None:
        output["code"] = request.code

    if request.target is not None:
        output["target"] = request.target

    if request.type_ is not None:
        output["type"] = AclActionRedirectRedirectType(request.type_)

    return output


def marshal_AclAction(
    request: AclAction,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.redirect is not None:
        output["redirect"] = marshal_AclActionRedirect(request.redirect, defaults)

    if request.type_ is not None:
        output["type"] = AclActionType(request.type_)

    return output


def marshal_AclMatch(
    request: AclMatch,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.http_filter is not None:
        output["http_filter"] = AclHttpFilter(request.http_filter)

    if request.http_filter_option is not None:
        output["http_filter_option"] = request.http_filter_option

    if request.http_filter_value is not None:
        output["http_filter_value"] = request.http_filter_value

    if request.invert is not None:
        output["invert"] = request.invert

    if request.ip_subnet is not None:
        output["ip_subnet"] = request.ip_subnet

    return output


def marshal_HealthCheckHttpConfig(
    request: HealthCheckHttpConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.code is not None:
        output["code"] = request.code

    if request.host_header is not None:
        output["host_header"] = request.host_header

    if request.method is not None:
        output["method"] = request.method

    if request.uri is not None:
        output["uri"] = request.uri

    return output


def marshal_HealthCheckHttpsConfig(
    request: HealthCheckHttpsConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.code is not None:
        output["code"] = request.code

    if request.host_header is not None:
        output["host_header"] = request.host_header

    if request.method is not None:
        output["method"] = request.method

    if request.sni is not None:
        output["sni"] = request.sni

    if request.uri is not None:
        output["uri"] = request.uri

    return output


def marshal_HealthCheckLdapConfig(
    request: HealthCheckLdapConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    return output


def marshal_HealthCheckMysqlConfig(
    request: HealthCheckMysqlConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.user is not None:
        output["user"] = request.user

    return output


def marshal_HealthCheckPgsqlConfig(
    request: HealthCheckPgsqlConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.user is not None:
        output["user"] = request.user

    return output


def marshal_HealthCheckRedisConfig(
    request: HealthCheckRedisConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    return output


def marshal_HealthCheckTcpConfig(
    request: HealthCheckTcpConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    return output


def marshal_AclSpec(
    request: AclSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)

    if request.description is not None:
        output["description"] = request.description

    if request.index is not None:
        output["index"] = request.index

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_CreateCertificateRequestCustomCertificate(
    request: CreateCertificateRequestCustomCertificate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.certificate_chain is not None:
        output["certificate_chain"] = request.certificate_chain

    return output


def marshal_CreateCertificateRequestLetsencryptConfig(
    request: CreateCertificateRequestLetsencryptConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.common_name is not None:
        output["common_name"] = request.common_name

    if request.subject_alternative_name is not None:
        output["subject_alternative_name"] = request.subject_alternative_name

    return output


def marshal_HealthCheck(
    request: HealthCheck,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "tcp_config",
                    marshal_HealthCheckTcpConfig(request.tcp_config, defaults)
                    if request.tcp_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "mysql_config",
                    marshal_HealthCheckMysqlConfig(request.mysql_config, defaults)
                    if request.mysql_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "pgsql_config",
                    marshal_HealthCheckPgsqlConfig(request.pgsql_config, defaults)
                    if request.pgsql_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "ldap_config",
                    marshal_HealthCheckLdapConfig(request.ldap_config, defaults)
                    if request.ldap_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "redis_config",
                    marshal_HealthCheckRedisConfig(request.redis_config, defaults)
                    if request.redis_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "http_config",
                    marshal_HealthCheckHttpConfig(request.http_config, defaults)
                    if request.http_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "https_config",
                    marshal_HealthCheckHttpsConfig(request.https_config, defaults)
                    if request.https_config is not None
                    else None,
                ),
            ]
        ),
    )

    if request.check_delay is not None:
        output["check_delay"] = request.check_delay

    if request.check_max_retries is not None:
        output["check_max_retries"] = request.check_max_retries

    if request.check_send_proxy is not None:
        output["check_send_proxy"] = request.check_send_proxy

    if request.check_timeout is not None:
        output["check_timeout"] = request.check_timeout

    if request.port is not None:
        output["port"] = request.port

    if request.transient_check_delay is not None:
        output["transient_check_delay"] = request.transient_check_delay

    return output


def marshal_PrivateNetworkDHCPConfig(
    request: PrivateNetworkDHCPConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id

    return output


def marshal_PrivateNetworkIpamConfig(
    request: PrivateNetworkIpamConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    return output


def marshal_PrivateNetworkStaticConfig(
    request: PrivateNetworkStaticConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_address is not None:
        output["ip_address"] = request.ip_address

    return output


def marshal_RouteMatch(
    request: RouteMatch,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "sni", request.sni if request.sni is not None else None
                ),
                OneOfPossibility(
                    "host_header",
                    request.host_header if request.host_header is not None else None,
                ),
            ]
        ),
    )

    return output


def marshal_SubscriberEmailConfig(
    request: SubscriberEmailConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email

    return output


def marshal_SubscriberWebhookConfig(
    request: SubscriberWebhookConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.uri is not None:
        output["uri"] = request.uri

    return output


def marshal_AddBackendServersRequest(
    request: AddBackendServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    return output


def marshal_AttachPrivateNetworkRequest(
    request: AttachPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "static_config",
                    marshal_PrivateNetworkStaticConfig(request.static_config, defaults)
                    if request.static_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "dhcp_config",
                    marshal_PrivateNetworkDHCPConfig(request.dhcp_config, defaults)
                    if request.dhcp_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "ipam_config",
                    marshal_PrivateNetworkIpamConfig(request.ipam_config, defaults)
                    if request.ipam_config is not None
                    else None,
                ),
            ]
        ),
    )

    return output


def marshal_CreateAclRequest(
    request: CreateAclRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)

    if request.description is not None:
        output["description"] = request.description

    if request.index is not None:
        output["index"] = request.index

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_CreateBackendRequest(
    request: CreateBackendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.failover_host is not None:
        output["failover_host"] = request.failover_host

    if request.forward_port is not None:
        output["forward_port"] = request.forward_port

    if request.forward_port_algorithm is not None:
        output["forward_port_algorithm"] = ForwardPortAlgorithm(
            request.forward_port_algorithm
        )

    if request.forward_protocol is not None:
        output["forward_protocol"] = Protocol(request.forward_protocol)

    if request.health_check is not None:
        output["health_check"] = marshal_HealthCheck(request.health_check, defaults)

    if request.ignore_ssl_server_verify is not None:
        output["ignore_ssl_server_verify"] = request.ignore_ssl_server_verify

    if request.max_connections is not None:
        output["max_connections"] = request.max_connections

    if request.max_retries is not None:
        output["max_retries"] = request.max_retries

    if request.name is not None:
        output["name"] = request.name

    if request.on_marked_down_action is not None:
        output["on_marked_down_action"] = OnMarkedDownAction(
            request.on_marked_down_action
        )

    if request.proxy_protocol is not None:
        output["proxy_protocol"] = ProxyProtocol(request.proxy_protocol)

    if request.redispatch_attempt_count is not None:
        output["redispatch_attempt_count"] = request.redispatch_attempt_count

    if request.send_proxy_v2 is not None:
        output["send_proxy_v2"] = request.send_proxy_v2

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    if request.ssl_bridging is not None:
        output["ssl_bridging"] = request.ssl_bridging

    if request.sticky_sessions is not None:
        output["sticky_sessions"] = StickySessionsType(request.sticky_sessions)

    if request.sticky_sessions_cookie_name is not None:
        output["sticky_sessions_cookie_name"] = request.sticky_sessions_cookie_name

    if request.timeout_connect is not None:
        output["timeout_connect"] = request.timeout_connect

    if request.timeout_queue is not None:
        output["timeout_queue"] = request.timeout_queue

    if request.timeout_server is not None:
        output["timeout_server"] = request.timeout_server

    if request.timeout_tunnel is not None:
        output["timeout_tunnel"] = request.timeout_tunnel

    return output


def marshal_CreateCertificateRequest(
    request: CreateCertificateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "letsencrypt",
                    marshal_CreateCertificateRequestLetsencryptConfig(
                        request.letsencrypt, defaults
                    )
                    if request.letsencrypt is not None
                    else None,
                ),
                OneOfPossibility(
                    "custom_certificate",
                    marshal_CreateCertificateRequestCustomCertificate(
                        request.custom_certificate, defaults
                    )
                    if request.custom_certificate is not None
                    else None,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_CreateFrontendRequest(
    request: CreateFrontendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.certificate_id is not None:
        output["certificate_id"] = request.certificate_id

    if request.certificate_ids is not None:
        output["certificate_ids"] = request.certificate_ids

    if request.enable_http3 is not None:
        output["enable_http3"] = request.enable_http3

    if request.inbound_port is not None:
        output["inbound_port"] = request.inbound_port

    if request.name is not None:
        output["name"] = request.name

    if request.timeout_client is not None:
        output["timeout_client"] = request.timeout_client

    return output


def marshal_CreateIpRequest(
    request: CreateIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project_id",
                    request.project_id or defaults.default_project_id
                    if request.project_id is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization_id",
                    request.organization_id or defaults.default_organization_id
                    if request.organization_id is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )

    if request.reverse is not None:
        output["reverse"] = request.reverse

    return output


def marshal_CreateLbRequest(
    request: CreateLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project_id",
                    request.project_id or defaults.default_project_id
                    if request.project_id is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization_id",
                    request.organization_id or defaults.default_organization_id
                    if request.organization_id is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )

    if request.assign_flexible_ip is not None:
        output["assign_flexible_ip"] = request.assign_flexible_ip

    if request.description is not None:
        output["description"] = request.description

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id

    if request.name is not None:
        output["name"] = request.name

    if request.ssl_compatibility_level is not None:
        output["ssl_compatibility_level"] = SSLCompatibilityLevel(
            request.ssl_compatibility_level
        )

    if request.tags is not None:
        output["tags"] = request.tags

    if request.type_ is not None:
        output["type"] = request.type_

    return output


def marshal_CreateRouteRequest(
    request: CreateRouteRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.frontend_id is not None:
        output["frontend_id"] = request.frontend_id

    if request.match is not None:
        output["match"] = marshal_RouteMatch(request.match, defaults)

    return output


def marshal_CreateSubscriberRequest(
    request: CreateSubscriberRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project_id",
                    request.project_id or defaults.default_project_id
                    if request.project_id is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization_id",
                    request.organization_id or defaults.default_organization_id
                    if request.organization_id is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "email_config",
                    marshal_SubscriberEmailConfig(request.email_config, defaults)
                    if request.email_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "webhook_config",
                    marshal_SubscriberWebhookConfig(request.webhook_config, defaults)
                    if request.webhook_config is not None
                    else None,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_MigrateLbRequest(
    request: MigrateLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    return output


def marshal_RemoveBackendServersRequest(
    request: RemoveBackendServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    return output


def marshal_SetBackendServersRequest(
    request: SetBackendServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    return output


def marshal_SubscribeToLbRequest(
    request: SubscribeToLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subscriber_id is not None:
        output["subscriber_id"] = request.subscriber_id

    return output


def marshal_UpdateAclRequest(
    request: UpdateAclRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)

    if request.description is not None:
        output["description"] = request.description

    if request.index is not None:
        output["index"] = request.index

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_UpdateBackendRequest(
    request: UpdateBackendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.failover_host is not None:
        output["failover_host"] = request.failover_host

    if request.forward_port is not None:
        output["forward_port"] = request.forward_port

    if request.forward_port_algorithm is not None:
        output["forward_port_algorithm"] = ForwardPortAlgorithm(
            request.forward_port_algorithm
        )

    if request.forward_protocol is not None:
        output["forward_protocol"] = Protocol(request.forward_protocol)

    if request.ignore_ssl_server_verify is not None:
        output["ignore_ssl_server_verify"] = request.ignore_ssl_server_verify

    if request.max_connections is not None:
        output["max_connections"] = request.max_connections

    if request.max_retries is not None:
        output["max_retries"] = request.max_retries

    if request.name is not None:
        output["name"] = request.name

    if request.on_marked_down_action is not None:
        output["on_marked_down_action"] = OnMarkedDownAction(
            request.on_marked_down_action
        )

    if request.proxy_protocol is not None:
        output["proxy_protocol"] = ProxyProtocol(request.proxy_protocol)

    if request.redispatch_attempt_count is not None:
        output["redispatch_attempt_count"] = request.redispatch_attempt_count

    if request.send_proxy_v2 is not None:
        output["send_proxy_v2"] = request.send_proxy_v2

    if request.ssl_bridging is not None:
        output["ssl_bridging"] = request.ssl_bridging

    if request.sticky_sessions is not None:
        output["sticky_sessions"] = StickySessionsType(request.sticky_sessions)

    if request.sticky_sessions_cookie_name is not None:
        output["sticky_sessions_cookie_name"] = request.sticky_sessions_cookie_name

    if request.timeout_connect is not None:
        output["timeout_connect"] = request.timeout_connect

    if request.timeout_queue is not None:
        output["timeout_queue"] = request.timeout_queue

    if request.timeout_server is not None:
        output["timeout_server"] = request.timeout_server

    if request.timeout_tunnel is not None:
        output["timeout_tunnel"] = request.timeout_tunnel

    return output


def marshal_UpdateCertificateRequest(
    request: UpdateCertificateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_UpdateFrontendRequest(
    request: UpdateFrontendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.certificate_id is not None:
        output["certificate_id"] = request.certificate_id

    if request.certificate_ids is not None:
        output["certificate_ids"] = request.certificate_ids

    if request.enable_http3 is not None:
        output["enable_http3"] = request.enable_http3

    if request.inbound_port is not None:
        output["inbound_port"] = request.inbound_port

    if request.name is not None:
        output["name"] = request.name

    if request.timeout_client is not None:
        output["timeout_client"] = request.timeout_client

    return output


def marshal_UpdateHealthCheckRequest(
    request: UpdateHealthCheckRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "tcp_config",
                    marshal_HealthCheckTcpConfig(request.tcp_config, defaults)
                    if request.tcp_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "mysql_config",
                    marshal_HealthCheckMysqlConfig(request.mysql_config, defaults)
                    if request.mysql_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "pgsql_config",
                    marshal_HealthCheckPgsqlConfig(request.pgsql_config, defaults)
                    if request.pgsql_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "ldap_config",
                    marshal_HealthCheckLdapConfig(request.ldap_config, defaults)
                    if request.ldap_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "redis_config",
                    marshal_HealthCheckRedisConfig(request.redis_config, defaults)
                    if request.redis_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "http_config",
                    marshal_HealthCheckHttpConfig(request.http_config, defaults)
                    if request.http_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "https_config",
                    marshal_HealthCheckHttpsConfig(request.https_config, defaults)
                    if request.https_config is not None
                    else None,
                ),
            ]
        ),
    )

    if request.check_delay is not None:
        output["check_delay"] = request.check_delay

    if request.check_max_retries is not None:
        output["check_max_retries"] = request.check_max_retries

    if request.check_send_proxy is not None:
        output["check_send_proxy"] = request.check_send_proxy

    if request.check_timeout is not None:
        output["check_timeout"] = request.check_timeout

    if request.port is not None:
        output["port"] = request.port

    if request.transient_check_delay is not None:
        output["transient_check_delay"] = request.transient_check_delay

    return output


def marshal_UpdateIpRequest(
    request: UpdateIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.reverse is not None:
        output["reverse"] = request.reverse

    return output


def marshal_UpdateLbRequest(
    request: UpdateLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    if request.ssl_compatibility_level is not None:
        output["ssl_compatibility_level"] = SSLCompatibilityLevel(
            request.ssl_compatibility_level
        )

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateRouteRequest(
    request: UpdateRouteRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.match is not None:
        output["match"] = marshal_RouteMatch(request.match, defaults)

    return output


def marshal_UpdateSubscriberRequest(
    request: UpdateSubscriberRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "email_config",
                    marshal_SubscriberEmailConfig(request.email_config, defaults)
                    if request.email_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "webhook_config",
                    marshal_SubscriberWebhookConfig(request.webhook_config, defaults)
                    if request.webhook_config is not None
                    else None,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_ZonedApiAddBackendServersRequest(
    request: ZonedApiAddBackendServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    return output


def marshal_ZonedApiAttachPrivateNetworkRequest(
    request: ZonedApiAttachPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "static_config",
                    marshal_PrivateNetworkStaticConfig(request.static_config, defaults)
                    if request.static_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "dhcp_config",
                    marshal_PrivateNetworkDHCPConfig(request.dhcp_config, defaults)
                    if request.dhcp_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "ipam_config",
                    marshal_PrivateNetworkIpamConfig(request.ipam_config, defaults)
                    if request.ipam_config is not None
                    else None,
                ),
            ]
        ),
    )

    return output


def marshal_ZonedApiCreateAclRequest(
    request: ZonedApiCreateAclRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)

    if request.description is not None:
        output["description"] = request.description

    if request.index is not None:
        output["index"] = request.index

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_ZonedApiCreateBackendRequest(
    request: ZonedApiCreateBackendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.failover_host is not None:
        output["failover_host"] = request.failover_host

    if request.forward_port is not None:
        output["forward_port"] = request.forward_port

    if request.forward_port_algorithm is not None:
        output["forward_port_algorithm"] = ForwardPortAlgorithm(
            request.forward_port_algorithm
        )

    if request.forward_protocol is not None:
        output["forward_protocol"] = Protocol(request.forward_protocol)

    if request.health_check is not None:
        output["health_check"] = marshal_HealthCheck(request.health_check, defaults)

    if request.ignore_ssl_server_verify is not None:
        output["ignore_ssl_server_verify"] = request.ignore_ssl_server_verify

    if request.max_connections is not None:
        output["max_connections"] = request.max_connections

    if request.max_retries is not None:
        output["max_retries"] = request.max_retries

    if request.name is not None:
        output["name"] = request.name

    if request.on_marked_down_action is not None:
        output["on_marked_down_action"] = OnMarkedDownAction(
            request.on_marked_down_action
        )

    if request.proxy_protocol is not None:
        output["proxy_protocol"] = ProxyProtocol(request.proxy_protocol)

    if request.redispatch_attempt_count is not None:
        output["redispatch_attempt_count"] = request.redispatch_attempt_count

    if request.send_proxy_v2 is not None:
        output["send_proxy_v2"] = request.send_proxy_v2

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    if request.ssl_bridging is not None:
        output["ssl_bridging"] = request.ssl_bridging

    if request.sticky_sessions is not None:
        output["sticky_sessions"] = StickySessionsType(request.sticky_sessions)

    if request.sticky_sessions_cookie_name is not None:
        output["sticky_sessions_cookie_name"] = request.sticky_sessions_cookie_name

    if request.timeout_connect is not None:
        output["timeout_connect"] = request.timeout_connect

    if request.timeout_queue is not None:
        output["timeout_queue"] = request.timeout_queue

    if request.timeout_server is not None:
        output["timeout_server"] = request.timeout_server

    if request.timeout_tunnel is not None:
        output["timeout_tunnel"] = request.timeout_tunnel

    return output


def marshal_ZonedApiCreateCertificateRequest(
    request: ZonedApiCreateCertificateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "letsencrypt",
                    marshal_CreateCertificateRequestLetsencryptConfig(
                        request.letsencrypt, defaults
                    )
                    if request.letsencrypt is not None
                    else None,
                ),
                OneOfPossibility(
                    "custom_certificate",
                    marshal_CreateCertificateRequestCustomCertificate(
                        request.custom_certificate, defaults
                    )
                    if request.custom_certificate is not None
                    else None,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_ZonedApiCreateFrontendRequest(
    request: ZonedApiCreateFrontendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.certificate_id is not None:
        output["certificate_id"] = request.certificate_id

    if request.certificate_ids is not None:
        output["certificate_ids"] = request.certificate_ids

    if request.enable_http3 is not None:
        output["enable_http3"] = request.enable_http3

    if request.inbound_port is not None:
        output["inbound_port"] = request.inbound_port

    if request.name is not None:
        output["name"] = request.name

    if request.timeout_client is not None:
        output["timeout_client"] = request.timeout_client

    return output


def marshal_ZonedApiCreateIpRequest(
    request: ZonedApiCreateIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project_id",
                    request.project_id or defaults.default_project_id
                    if request.project_id is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization_id",
                    request.organization_id or defaults.default_organization_id
                    if request.organization_id is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )

    if request.reverse is not None:
        output["reverse"] = request.reverse

    return output


def marshal_ZonedApiCreateLbRequest(
    request: ZonedApiCreateLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project_id",
                    request.project_id or defaults.default_project_id
                    if request.project_id is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization_id",
                    request.organization_id or defaults.default_organization_id
                    if request.organization_id is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )

    if request.assign_flexible_ip is not None:
        output["assign_flexible_ip"] = request.assign_flexible_ip

    if request.description is not None:
        output["description"] = request.description

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id

    if request.name is not None:
        output["name"] = request.name

    if request.ssl_compatibility_level is not None:
        output["ssl_compatibility_level"] = SSLCompatibilityLevel(
            request.ssl_compatibility_level
        )

    if request.tags is not None:
        output["tags"] = request.tags

    if request.type_ is not None:
        output["type"] = request.type_

    return output


def marshal_ZonedApiCreateRouteRequest(
    request: ZonedApiCreateRouteRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.frontend_id is not None:
        output["frontend_id"] = request.frontend_id

    if request.match is not None:
        output["match"] = marshal_RouteMatch(request.match, defaults)

    return output


def marshal_ZonedApiCreateSubscriberRequest(
    request: ZonedApiCreateSubscriberRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project_id",
                    request.project_id or defaults.default_project_id
                    if request.project_id is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization_id",
                    request.organization_id or defaults.default_organization_id
                    if request.organization_id is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "email_config",
                    marshal_SubscriberEmailConfig(request.email_config, defaults)
                    if request.email_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "webhook_config",
                    marshal_SubscriberWebhookConfig(request.webhook_config, defaults)
                    if request.webhook_config is not None
                    else None,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_ZonedApiMigrateLbRequest(
    request: ZonedApiMigrateLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    return output


def marshal_ZonedApiRemoveBackendServersRequest(
    request: ZonedApiRemoveBackendServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    return output


def marshal_ZonedApiSetAclsRequest(
    request: ZonedApiSetAclsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.acls is not None:
        output["acls"] = [marshal_AclSpec(v, defaults) for v in request.acls]

    return output


def marshal_ZonedApiSetBackendServersRequest(
    request: ZonedApiSetBackendServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    return output


def marshal_ZonedApiSubscribeToLbRequest(
    request: ZonedApiSubscribeToLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subscriber_id is not None:
        output["subscriber_id"] = request.subscriber_id

    return output


def marshal_ZonedApiUpdateAclRequest(
    request: ZonedApiUpdateAclRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)

    if request.description is not None:
        output["description"] = request.description

    if request.index is not None:
        output["index"] = request.index

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_ZonedApiUpdateBackendRequest(
    request: ZonedApiUpdateBackendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.failover_host is not None:
        output["failover_host"] = request.failover_host

    if request.forward_port is not None:
        output["forward_port"] = request.forward_port

    if request.forward_port_algorithm is not None:
        output["forward_port_algorithm"] = ForwardPortAlgorithm(
            request.forward_port_algorithm
        )

    if request.forward_protocol is not None:
        output["forward_protocol"] = Protocol(request.forward_protocol)

    if request.ignore_ssl_server_verify is not None:
        output["ignore_ssl_server_verify"] = request.ignore_ssl_server_verify

    if request.max_connections is not None:
        output["max_connections"] = request.max_connections

    if request.max_retries is not None:
        output["max_retries"] = request.max_retries

    if request.name is not None:
        output["name"] = request.name

    if request.on_marked_down_action is not None:
        output["on_marked_down_action"] = OnMarkedDownAction(
            request.on_marked_down_action
        )

    if request.proxy_protocol is not None:
        output["proxy_protocol"] = ProxyProtocol(request.proxy_protocol)

    if request.redispatch_attempt_count is not None:
        output["redispatch_attempt_count"] = request.redispatch_attempt_count

    if request.send_proxy_v2 is not None:
        output["send_proxy_v2"] = request.send_proxy_v2

    if request.ssl_bridging is not None:
        output["ssl_bridging"] = request.ssl_bridging

    if request.sticky_sessions is not None:
        output["sticky_sessions"] = StickySessionsType(request.sticky_sessions)

    if request.sticky_sessions_cookie_name is not None:
        output["sticky_sessions_cookie_name"] = request.sticky_sessions_cookie_name

    if request.timeout_connect is not None:
        output["timeout_connect"] = request.timeout_connect

    if request.timeout_queue is not None:
        output["timeout_queue"] = request.timeout_queue

    if request.timeout_server is not None:
        output["timeout_server"] = request.timeout_server

    if request.timeout_tunnel is not None:
        output["timeout_tunnel"] = request.timeout_tunnel

    return output


def marshal_ZonedApiUpdateCertificateRequest(
    request: ZonedApiUpdateCertificateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_ZonedApiUpdateFrontendRequest(
    request: ZonedApiUpdateFrontendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.certificate_id is not None:
        output["certificate_id"] = request.certificate_id

    if request.certificate_ids is not None:
        output["certificate_ids"] = request.certificate_ids

    if request.enable_http3 is not None:
        output["enable_http3"] = request.enable_http3

    if request.inbound_port is not None:
        output["inbound_port"] = request.inbound_port

    if request.name is not None:
        output["name"] = request.name

    if request.timeout_client is not None:
        output["timeout_client"] = request.timeout_client

    return output


def marshal_ZonedApiUpdateHealthCheckRequest(
    request: ZonedApiUpdateHealthCheckRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "tcp_config",
                    marshal_HealthCheckTcpConfig(request.tcp_config, defaults)
                    if request.tcp_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "mysql_config",
                    marshal_HealthCheckMysqlConfig(request.mysql_config, defaults)
                    if request.mysql_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "pgsql_config",
                    marshal_HealthCheckPgsqlConfig(request.pgsql_config, defaults)
                    if request.pgsql_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "ldap_config",
                    marshal_HealthCheckLdapConfig(request.ldap_config, defaults)
                    if request.ldap_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "redis_config",
                    marshal_HealthCheckRedisConfig(request.redis_config, defaults)
                    if request.redis_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "http_config",
                    marshal_HealthCheckHttpConfig(request.http_config, defaults)
                    if request.http_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "https_config",
                    marshal_HealthCheckHttpsConfig(request.https_config, defaults)
                    if request.https_config is not None
                    else None,
                ),
            ]
        ),
    )

    if request.check_delay is not None:
        output["check_delay"] = request.check_delay

    if request.check_max_retries is not None:
        output["check_max_retries"] = request.check_max_retries

    if request.check_send_proxy is not None:
        output["check_send_proxy"] = request.check_send_proxy

    if request.check_timeout is not None:
        output["check_timeout"] = request.check_timeout

    if request.port is not None:
        output["port"] = request.port

    if request.transient_check_delay is not None:
        output["transient_check_delay"] = request.transient_check_delay

    return output


def marshal_ZonedApiUpdateIpRequest(
    request: ZonedApiUpdateIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.reverse is not None:
        output["reverse"] = request.reverse

    return output


def marshal_ZonedApiUpdateLbRequest(
    request: ZonedApiUpdateLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    if request.ssl_compatibility_level is not None:
        output["ssl_compatibility_level"] = SSLCompatibilityLevel(
            request.ssl_compatibility_level
        )

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_ZonedApiUpdateRouteRequest(
    request: ZonedApiUpdateRouteRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.match is not None:
        output["match"] = marshal_RouteMatch(request.match, defaults)

    return output


def marshal_ZonedApiUpdateSubscriberRequest(
    request: ZonedApiUpdateSubscriberRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "email_config",
                    marshal_SubscriberEmailConfig(request.email_config, defaults)
                    if request.email_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "webhook_config",
                    marshal_SubscriberWebhookConfig(request.webhook_config, defaults)
                    if request.webhook_config is not None
                    else None,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    return output
