# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    AclActionRedirectRedirectType,
    AclActionType,
    AclHttpFilter,
    BackendServerStatsHealthCheckStatus,
    BackendServerStatsServerState,
    CertificateStatus,
    CertificateType,
    ForwardPortAlgorithm,
    InstanceStatus,
    LbStatus,
    LbTypeStock,
    OnMarkedDownAction,
    PrivateNetworkStatus,
    Protocol,
    ProxyProtocol,
    SSLCompatibilityLevel,
    StickySessionsType,
    Ip,
    SubscriberEmailConfig,
    SubscriberWebhookConfig,
    Subscriber,
    HealthCheckHttpConfig,
    HealthCheckHttpsConfig,
    HealthCheckLdapConfig,
    HealthCheckMysqlConfig,
    HealthCheckPgsqlConfig,
    HealthCheckRedisConfig,
    HealthCheckTcpConfig,
    HealthCheck,
    Instance,
    Lb,
    Backend,
    Certificate,
    Frontend,
    AclActionRedirect,
    AclAction,
    AclMatch,
    Acl,
    PrivateNetworkDHCPConfig,
    PrivateNetworkIpamConfig,
    PrivateNetworkStaticConfig,
    PrivateNetwork,
    RouteMatch,
    Route,
    BackendServerStats,
    LbStats,
    ListAclResponse,
    ListBackendStatsResponse,
    ListBackendsResponse,
    ListCertificatesResponse,
    ListFrontendsResponse,
    ListIpsResponse,
    ListLbPrivateNetworksResponse,
    LbType,
    ListLbTypesResponse,
    ListLbsResponse,
    ListRoutesResponse,
    ListSubscriberResponse,
    SetAclsResponse,
    AddBackendServersRequest,
    AttachPrivateNetworkRequest,
    CreateAclRequest,
    CreateBackendRequest,
    CreateCertificateRequestCustomCertificate,
    CreateCertificateRequestLetsencryptConfig,
    CreateCertificateRequest,
    CreateFrontendRequest,
    CreateIpRequest,
    CreateLbRequest,
    CreateRouteRequest,
    CreateSubscriberRequest,
    MigrateLbRequest,
    RemoveBackendServersRequest,
    SetBackendServersRequest,
    SubscribeToLbRequest,
    UpdateAclRequest,
    UpdateBackendRequest,
    UpdateCertificateRequest,
    UpdateFrontendRequest,
    UpdateHealthCheckRequest,
    UpdateIpRequest,
    UpdateLbRequest,
    UpdateRouteRequest,
    UpdateSubscriberRequest,
    ZonedApiAddBackendServersRequest,
    ZonedApiAttachPrivateNetworkRequest,
    ZonedApiCreateAclRequest,
    ZonedApiCreateBackendRequest,
    ZonedApiCreateCertificateRequest,
    ZonedApiCreateFrontendRequest,
    ZonedApiCreateIpRequest,
    ZonedApiCreateLbRequest,
    ZonedApiCreateRouteRequest,
    ZonedApiCreateSubscriberRequest,
    ZonedApiDetachPrivateNetworkRequest,
    ZonedApiMigrateLbRequest,
    ZonedApiRemoveBackendServersRequest,
    AclSpec,
    ZonedApiSetAclsRequest,
    ZonedApiSetBackendServersRequest,
    ZonedApiSubscribeToLbRequest,
    ZonedApiUpdateAclRequest,
    ZonedApiUpdateBackendRequest,
    ZonedApiUpdateCertificateRequest,
    ZonedApiUpdateFrontendRequest,
    ZonedApiUpdateHealthCheckRequest,
    ZonedApiUpdateIpRequest,
    ZonedApiUpdateLbRequest,
    ZonedApiUpdateRouteRequest,
    ZonedApiUpdateSubscriberRequest,
)


def unmarshal_Ip(data: Any) -> Ip:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Ip' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("ip_address", None)
    if field is not None:
        args["ip_address"] = field
    else:
        args["ip_address"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("reverse", None)
    if field is not None:
        args["reverse"] = field
    else:
        args["reverse"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("lb_id", None)
    if field is not None:
        args["lb_id"] = field
    else:
        args["lb_id"] = None

    return Ip(**args)


def unmarshal_SubscriberEmailConfig(data: Any) -> SubscriberEmailConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SubscriberEmailConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("email", None)
    if field is not None:
        args["email"] = field
    else:
        args["email"] = None

    return SubscriberEmailConfig(**args)


def unmarshal_SubscriberWebhookConfig(data: Any) -> SubscriberWebhookConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SubscriberWebhookConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("uri", None)
    if field is not None:
        args["uri"] = field
    else:
        args["uri"] = None

    return SubscriberWebhookConfig(**args)


def unmarshal_Subscriber(data: Any) -> Subscriber:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Subscriber' failed as data isn't a dictionary."
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

    field = data.get("email_config", None)
    if field is not None:
        args["email_config"] = unmarshal_SubscriberEmailConfig(field)
    else:
        args["email_config"] = None

    field = data.get("webhook_config", None)
    if field is not None:
        args["webhook_config"] = unmarshal_SubscriberWebhookConfig(field)
    else:
        args["webhook_config"] = None

    return Subscriber(**args)


def unmarshal_HealthCheckHttpConfig(data: Any) -> HealthCheckHttpConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckHttpConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("uri", None)
    if field is not None:
        args["uri"] = field
    else:
        args["uri"] = None

    field = data.get("method", None)
    if field is not None:
        args["method"] = field
    else:
        args["method"] = None

    field = data.get("host_header", None)
    if field is not None:
        args["host_header"] = field
    else:
        args["host_header"] = None

    field = data.get("code", None)
    if field is not None:
        args["code"] = field
    else:
        args["code"] = 0

    return HealthCheckHttpConfig(**args)


def unmarshal_HealthCheckHttpsConfig(data: Any) -> HealthCheckHttpsConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckHttpsConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("uri", None)
    if field is not None:
        args["uri"] = field
    else:
        args["uri"] = None

    field = data.get("method", None)
    if field is not None:
        args["method"] = field
    else:
        args["method"] = None

    field = data.get("host_header", None)
    if field is not None:
        args["host_header"] = field
    else:
        args["host_header"] = None

    field = data.get("sni", None)
    if field is not None:
        args["sni"] = field
    else:
        args["sni"] = None

    field = data.get("code", None)
    if field is not None:
        args["code"] = field
    else:
        args["code"] = 0

    return HealthCheckHttpsConfig(**args)


def unmarshal_HealthCheckLdapConfig(data: Any) -> HealthCheckLdapConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckLdapConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return HealthCheckLdapConfig(**args)


def unmarshal_HealthCheckMysqlConfig(data: Any) -> HealthCheckMysqlConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckMysqlConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("user", None)
    if field is not None:
        args["user"] = field
    else:
        args["user"] = None

    return HealthCheckMysqlConfig(**args)


def unmarshal_HealthCheckPgsqlConfig(data: Any) -> HealthCheckPgsqlConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckPgsqlConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("user", None)
    if field is not None:
        args["user"] = field
    else:
        args["user"] = None

    return HealthCheckPgsqlConfig(**args)


def unmarshal_HealthCheckRedisConfig(data: Any) -> HealthCheckRedisConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckRedisConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return HealthCheckRedisConfig(**args)


def unmarshal_HealthCheckTcpConfig(data: Any) -> HealthCheckTcpConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckTcpConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return HealthCheckTcpConfig(**args)


def unmarshal_HealthCheck(data: Any) -> HealthCheck:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheck' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("port", None)
    if field is not None:
        args["port"] = field
    else:
        args["port"] = 0

    field = data.get("check_max_retries", None)
    if field is not None:
        args["check_max_retries"] = field
    else:
        args["check_max_retries"] = 0

    field = data.get("check_delay", None)
    if field is not None:
        args["check_delay"] = field
    else:
        args["check_delay"] = None

    field = data.get("check_timeout", None)
    if field is not None:
        args["check_timeout"] = field
    else:
        args["check_timeout"] = None

    field = data.get("tcp_config", None)
    if field is not None:
        args["tcp_config"] = unmarshal_HealthCheckTcpConfig(field)
    else:
        args["tcp_config"] = None

    field = data.get("mysql_config", None)
    if field is not None:
        args["mysql_config"] = unmarshal_HealthCheckMysqlConfig(field)
    else:
        args["mysql_config"] = None

    field = data.get("check_send_proxy", None)
    if field is not None:
        args["check_send_proxy"] = field
    else:
        args["check_send_proxy"] = False

    field = data.get("pgsql_config", None)
    if field is not None:
        args["pgsql_config"] = unmarshal_HealthCheckPgsqlConfig(field)
    else:
        args["pgsql_config"] = None

    field = data.get("ldap_config", None)
    if field is not None:
        args["ldap_config"] = unmarshal_HealthCheckLdapConfig(field)
    else:
        args["ldap_config"] = None

    field = data.get("redis_config", None)
    if field is not None:
        args["redis_config"] = unmarshal_HealthCheckRedisConfig(field)
    else:
        args["redis_config"] = None

    field = data.get("http_config", None)
    if field is not None:
        args["http_config"] = unmarshal_HealthCheckHttpConfig(field)
    else:
        args["http_config"] = None

    field = data.get("https_config", None)
    if field is not None:
        args["https_config"] = unmarshal_HealthCheckHttpsConfig(field)
    else:
        args["https_config"] = None

    field = data.get("transient_check_delay", None)
    if field is not None:
        args["transient_check_delay"] = field
    else:
        args["transient_check_delay"] = None

    return HealthCheck(**args)


def unmarshal_Instance(data: Any) -> Instance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Instance' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = InstanceStatus.UNKNOWN

    field = data.get("ip_address", None)
    if field is not None:
        args["ip_address"] = field
    else:
        args["ip_address"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

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

    return Instance(**args)


def unmarshal_Lb(data: Any) -> Lb:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Lb' failed as data isn't a dictionary."
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
        args["status"] = LbStatus.UNKNOWN

    field = data.get("instances", None)
    if field is not None:
        args["instances"] = (
            [unmarshal_Instance(v) for v in field] if field is not None else None
        )
    else:
        args["instances"] = []

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = [unmarshal_Ip(v) for v in field] if field is not None else None
    else:
        args["ip"] = []

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("frontend_count", None)
    if field is not None:
        args["frontend_count"] = field
    else:
        args["frontend_count"] = 0

    field = data.get("backend_count", None)
    if field is not None:
        args["backend_count"] = field
    else:
        args["backend_count"] = 0

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("ssl_compatibility_level", None)
    if field is not None:
        args["ssl_compatibility_level"] = field
    else:
        args["ssl_compatibility_level"] = (
            SSLCompatibilityLevel.SSL_COMPATIBILITY_LEVEL_UNKNOWN
        )

    field = data.get("private_network_count", None)
    if field is not None:
        args["private_network_count"] = field
    else:
        args["private_network_count"] = 0

    field = data.get("route_count", None)
    if field is not None:
        args["route_count"] = field
    else:
        args["route_count"] = 0

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("subscriber", None)
    if field is not None:
        args["subscriber"] = unmarshal_Subscriber(field)
    else:
        args["subscriber"] = None

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

    return Lb(**args)


def unmarshal_Backend(data: Any) -> Backend:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Backend' failed as data isn't a dictionary."
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

    field = data.get("forward_protocol", None)
    if field is not None:
        args["forward_protocol"] = field
    else:
        args["forward_protocol"] = Protocol.TCP

    field = data.get("forward_port", None)
    if field is not None:
        args["forward_port"] = field
    else:
        args["forward_port"] = 0

    field = data.get("forward_port_algorithm", None)
    if field is not None:
        args["forward_port_algorithm"] = field
    else:
        args["forward_port_algorithm"] = ForwardPortAlgorithm.ROUNDROBIN

    field = data.get("sticky_sessions", None)
    if field is not None:
        args["sticky_sessions"] = field
    else:
        args["sticky_sessions"] = StickySessionsType.NONE

    field = data.get("sticky_sessions_cookie_name", None)
    if field is not None:
        args["sticky_sessions_cookie_name"] = field
    else:
        args["sticky_sessions_cookie_name"] = None

    field = data.get("pool", None)
    if field is not None:
        args["pool"] = field
    else:
        args["pool"] = []

    field = data.get("send_proxy_v2", None)
    if field is not None:
        args["send_proxy_v2"] = field
    else:
        args["send_proxy_v2"] = False

    field = data.get("on_marked_down_action", None)
    if field is not None:
        args["on_marked_down_action"] = field
    else:
        args["on_marked_down_action"] = OnMarkedDownAction.ON_MARKED_DOWN_ACTION_NONE

    field = data.get("proxy_protocol", None)
    if field is not None:
        args["proxy_protocol"] = field
    else:
        args["proxy_protocol"] = ProxyProtocol.PROXY_PROTOCOL_UNKNOWN

    field = data.get("health_check", None)
    if field is not None:
        args["health_check"] = unmarshal_HealthCheck(field)
    else:
        args["health_check"] = None

    field = data.get("lb", None)
    if field is not None:
        args["lb"] = unmarshal_Lb(field)
    else:
        args["lb"] = None

    field = data.get("timeout_server", None)
    if field is not None:
        args["timeout_server"] = field
    else:
        args["timeout_server"] = None

    field = data.get("timeout_connect", None)
    if field is not None:
        args["timeout_connect"] = field
    else:
        args["timeout_connect"] = None

    field = data.get("timeout_tunnel", None)
    if field is not None:
        args["timeout_tunnel"] = field
    else:
        args["timeout_tunnel"] = None

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

    field = data.get("failover_host", None)
    if field is not None:
        args["failover_host"] = field
    else:
        args["failover_host"] = None

    field = data.get("ssl_bridging", None)
    if field is not None:
        args["ssl_bridging"] = field
    else:
        args["ssl_bridging"] = False

    field = data.get("ignore_ssl_server_verify", None)
    if field is not None:
        args["ignore_ssl_server_verify"] = field
    else:
        args["ignore_ssl_server_verify"] = False

    field = data.get("redispatch_attempt_count", None)
    if field is not None:
        args["redispatch_attempt_count"] = field
    else:
        args["redispatch_attempt_count"] = 0

    field = data.get("max_retries", None)
    if field is not None:
        args["max_retries"] = field
    else:
        args["max_retries"] = 0

    field = data.get("max_connections", None)
    if field is not None:
        args["max_connections"] = field
    else:
        args["max_connections"] = 0

    field = data.get("timeout_queue", None)
    if field is not None:
        args["timeout_queue"] = field
    else:
        args["timeout_queue"] = None

    return Backend(**args)


def unmarshal_Certificate(data: Any) -> Certificate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Certificate' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = CertificateType.LETSENCRYT

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("common_name", None)
    if field is not None:
        args["common_name"] = field
    else:
        args["common_name"] = None

    field = data.get("subject_alternative_name", None)
    if field is not None:
        args["subject_alternative_name"] = field
    else:
        args["subject_alternative_name"] = []

    field = data.get("fingerprint", None)
    if field is not None:
        args["fingerprint"] = field
    else:
        args["fingerprint"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = CertificateStatus.PENDING

    field = data.get("not_valid_before", None)
    if field is not None:
        args["not_valid_before"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["not_valid_before"] = None

    field = data.get("not_valid_after", None)
    if field is not None:
        args["not_valid_after"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["not_valid_after"] = None

    field = data.get("lb", None)
    if field is not None:
        args["lb"] = unmarshal_Lb(field)
    else:
        args["lb"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

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

    field = data.get("status_details", None)
    if field is not None:
        args["status_details"] = field
    else:
        args["status_details"] = None

    return Certificate(**args)


def unmarshal_Frontend(data: Any) -> Frontend:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Frontend' failed as data isn't a dictionary."
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

    field = data.get("inbound_port", None)
    if field is not None:
        args["inbound_port"] = field
    else:
        args["inbound_port"] = 0

    field = data.get("certificate_ids", None)
    if field is not None:
        args["certificate_ids"] = field
    else:
        args["certificate_ids"] = []

    field = data.get("backend", None)
    if field is not None:
        args["backend"] = unmarshal_Backend(field)
    else:
        args["backend"] = None

    field = data.get("lb", None)
    if field is not None:
        args["lb"] = unmarshal_Lb(field)
    else:
        args["lb"] = None

    field = data.get("timeout_client", None)
    if field is not None:
        args["timeout_client"] = field
    else:
        args["timeout_client"] = None

    field = data.get("enable_http3", None)
    if field is not None:
        args["enable_http3"] = field
    else:
        args["enable_http3"] = False

    field = data.get("enable_access_logs", None)
    if field is not None:
        args["enable_access_logs"] = field
    else:
        args["enable_access_logs"] = False

    field = data.get("certificate", None)
    if field is not None:
        args["certificate"] = unmarshal_Certificate(field)
    else:
        args["certificate"] = None

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

    field = data.get("connection_rate_limit", None)
    if field is not None:
        args["connection_rate_limit"] = field
    else:
        args["connection_rate_limit"] = 0

    return Frontend(**args)


def unmarshal_AclActionRedirect(data: Any) -> AclActionRedirect:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AclActionRedirect' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = AclActionRedirectRedirectType.LOCATION

    field = data.get("target", None)
    if field is not None:
        args["target"] = field
    else:
        args["target"] = None

    field = data.get("code", None)
    if field is not None:
        args["code"] = field
    else:
        args["code"] = 0

    return AclActionRedirect(**args)


def unmarshal_AclAction(data: Any) -> AclAction:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AclAction' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = AclActionType.ALLOW

    field = data.get("redirect", None)
    if field is not None:
        args["redirect"] = unmarshal_AclActionRedirect(field)
    else:
        args["redirect"] = None

    return AclAction(**args)


def unmarshal_AclMatch(data: Any) -> AclMatch:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AclMatch' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ip_subnet", None)
    if field is not None:
        args["ip_subnet"] = field
    else:
        args["ip_subnet"] = []

    field = data.get("ips_edge_services", None)
    if field is not None:
        args["ips_edge_services"] = field
    else:
        args["ips_edge_services"] = False

    field = data.get("http_filter", None)
    if field is not None:
        args["http_filter"] = field
    else:
        args["http_filter"] = AclHttpFilter.ACL_HTTP_FILTER_NONE

    field = data.get("http_filter_value", None)
    if field is not None:
        args["http_filter_value"] = field
    else:
        args["http_filter_value"] = []

    field = data.get("invert", None)
    if field is not None:
        args["invert"] = field
    else:
        args["invert"] = False

    field = data.get("http_filter_option", None)
    if field is not None:
        args["http_filter_option"] = field
    else:
        args["http_filter_option"] = None

    return AclMatch(**args)


def unmarshal_Acl(data: Any) -> Acl:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Acl' failed as data isn't a dictionary."
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

    field = data.get("index", None)
    if field is not None:
        args["index"] = field
    else:
        args["index"] = 0

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("match", None)
    if field is not None:
        args["match"] = unmarshal_AclMatch(field)
    else:
        args["match"] = None

    field = data.get("action", None)
    if field is not None:
        args["action"] = unmarshal_AclAction(field)
    else:
        args["action"] = None

    field = data.get("frontend", None)
    if field is not None:
        args["frontend"] = unmarshal_Frontend(field)
    else:
        args["frontend"] = None

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

    return Acl(**args)


def unmarshal_PrivateNetworkDHCPConfig(data: Any) -> PrivateNetworkDHCPConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetworkDHCPConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ip_id", None)
    if field is not None:
        args["ip_id"] = field
    else:
        args["ip_id"] = None

    return PrivateNetworkDHCPConfig(**args)


def unmarshal_PrivateNetworkIpamConfig(data: Any) -> PrivateNetworkIpamConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetworkIpamConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return PrivateNetworkIpamConfig(**args)


def unmarshal_PrivateNetworkStaticConfig(data: Any) -> PrivateNetworkStaticConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetworkStaticConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ip_address", None)
    if field is not None:
        args["ip_address"] = field
    else:
        args["ip_address"] = []

    return PrivateNetworkStaticConfig(**args)


def unmarshal_PrivateNetwork(data: Any) -> PrivateNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetwork' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ipam_ids", None)
    if field is not None:
        args["ipam_ids"] = field
    else:
        args["ipam_ids"] = []

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = PrivateNetworkStatus.UNKNOWN

    field = data.get("lb", None)
    if field is not None:
        args["lb"] = unmarshal_Lb(field)
    else:
        args["lb"] = None

    field = data.get("static_config", None)
    if field is not None:
        args["static_config"] = unmarshal_PrivateNetworkStaticConfig(field)
    else:
        args["static_config"] = None

    field = data.get("dhcp_config", None)
    if field is not None:
        args["dhcp_config"] = unmarshal_PrivateNetworkDHCPConfig(field)
    else:
        args["dhcp_config"] = None

    field = data.get("ipam_config", None)
    if field is not None:
        args["ipam_config"] = unmarshal_PrivateNetworkIpamConfig(field)
    else:
        args["ipam_config"] = None

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

    return PrivateNetwork(**args)


def unmarshal_RouteMatch(data: Any) -> RouteMatch:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteMatch' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("match_subdomains", None)
    if field is not None:
        args["match_subdomains"] = field
    else:
        args["match_subdomains"] = False

    field = data.get("sni", None)
    if field is not None:
        args["sni"] = field
    else:
        args["sni"] = None

    field = data.get("host_header", None)
    if field is not None:
        args["host_header"] = field
    else:
        args["host_header"] = None

    field = data.get("path_begin", None)
    if field is not None:
        args["path_begin"] = field
    else:
        args["path_begin"] = None

    return RouteMatch(**args)


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

    field = data.get("frontend_id", None)
    if field is not None:
        args["frontend_id"] = field
    else:
        args["frontend_id"] = None

    field = data.get("backend_id", None)
    if field is not None:
        args["backend_id"] = field
    else:
        args["backend_id"] = None

    field = data.get("match", None)
    if field is not None:
        args["match"] = unmarshal_RouteMatch(field)
    else:
        args["match"] = None

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

    return Route(**args)


def unmarshal_BackendServerStats(data: Any) -> BackendServerStats:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BackendServerStats' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("instance_id", None)
    if field is not None:
        args["instance_id"] = field
    else:
        args["instance_id"] = None

    field = data.get("backend_id", None)
    if field is not None:
        args["backend_id"] = field
    else:
        args["backend_id"] = None

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = field
    else:
        args["ip"] = None

    field = data.get("server_state", None)
    if field is not None:
        args["server_state"] = field
    else:
        args["server_state"] = BackendServerStatsServerState.STOPPED

    field = data.get("last_health_check_status", None)
    if field is not None:
        args["last_health_check_status"] = field
    else:
        args["last_health_check_status"] = BackendServerStatsHealthCheckStatus.UNKNOWN

    field = data.get("server_state_changed_at", None)
    if field is not None:
        args["server_state_changed_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["server_state_changed_at"] = None

    return BackendServerStats(**args)


def unmarshal_LbStats(data: Any) -> LbStats:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LbStats' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("backend_servers_stats", None)
    if field is not None:
        args["backend_servers_stats"] = (
            [unmarshal_BackendServerStats(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["backend_servers_stats"] = []

    return LbStats(**args)


def unmarshal_ListAclResponse(data: Any) -> ListAclResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAclResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("acls", None)
    if field is not None:
        args["acls"] = [unmarshal_Acl(v) for v in field] if field is not None else None
    else:
        args["acls"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListAclResponse(**args)


def unmarshal_ListBackendStatsResponse(data: Any) -> ListBackendStatsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBackendStatsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("backend_servers_stats", None)
    if field is not None:
        args["backend_servers_stats"] = (
            [unmarshal_BackendServerStats(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["backend_servers_stats"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListBackendStatsResponse(**args)


def unmarshal_ListBackendsResponse(data: Any) -> ListBackendsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBackendsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("backends", None)
    if field is not None:
        args["backends"] = (
            [unmarshal_Backend(v) for v in field] if field is not None else None
        )
    else:
        args["backends"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListBackendsResponse(**args)


def unmarshal_ListCertificatesResponse(data: Any) -> ListCertificatesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCertificatesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("certificates", None)
    if field is not None:
        args["certificates"] = (
            [unmarshal_Certificate(v) for v in field] if field is not None else None
        )
    else:
        args["certificates"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListCertificatesResponse(**args)


def unmarshal_ListFrontendsResponse(data: Any) -> ListFrontendsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFrontendsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("frontends", None)
    if field is not None:
        args["frontends"] = (
            [unmarshal_Frontend(v) for v in field] if field is not None else None
        )
    else:
        args["frontends"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListFrontendsResponse(**args)


def unmarshal_ListIpsResponse(data: Any) -> ListIpsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListIpsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ips", None)
    if field is not None:
        args["ips"] = [unmarshal_Ip(v) for v in field] if field is not None else None
    else:
        args["ips"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListIpsResponse(**args)


def unmarshal_ListLbPrivateNetworksResponse(data: Any) -> ListLbPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLbPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("private_network", None)
    if field is not None:
        args["private_network"] = (
            [unmarshal_PrivateNetwork(v) for v in field] if field is not None else None
        )
    else:
        args["private_network"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListLbPrivateNetworksResponse(**args)


def unmarshal_LbType(data: Any) -> LbType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LbType' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("stock_status", None)
    if field is not None:
        args["stock_status"] = field
    else:
        args["stock_status"] = LbTypeStock.UNKNOWN

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    return LbType(**args)


def unmarshal_ListLbTypesResponse(data: Any) -> ListLbTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLbTypesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("lb_types", None)
    if field is not None:
        args["lb_types"] = (
            [unmarshal_LbType(v) for v in field] if field is not None else None
        )
    else:
        args["lb_types"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListLbTypesResponse(**args)


def unmarshal_ListLbsResponse(data: Any) -> ListLbsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLbsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("lbs", None)
    if field is not None:
        args["lbs"] = [unmarshal_Lb(v) for v in field] if field is not None else None
    else:
        args["lbs"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListLbsResponse(**args)


def unmarshal_ListRoutesResponse(data: Any) -> ListRoutesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRoutesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("routes", None)
    if field is not None:
        args["routes"] = (
            [unmarshal_Route(v) for v in field] if field is not None else None
        )
    else:
        args["routes"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListRoutesResponse(**args)


def unmarshal_ListSubscriberResponse(data: Any) -> ListSubscriberResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSubscriberResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("subscribers", None)
    if field is not None:
        args["subscribers"] = (
            [unmarshal_Subscriber(v) for v in field] if field is not None else None
        )
    else:
        args["subscribers"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListSubscriberResponse(**args)


def unmarshal_SetAclsResponse(data: Any) -> SetAclsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetAclsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("acls", None)
    if field is not None:
        args["acls"] = [unmarshal_Acl(v) for v in field] if field is not None else None
    else:
        args["acls"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return SetAclsResponse(**args)


def marshal_AddBackendServersRequest(
    request: AddBackendServersRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    return output


def marshal_PrivateNetworkDHCPConfig(
    request: PrivateNetworkDHCPConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id

    return output


def marshal_PrivateNetworkIpamConfig(
    request: PrivateNetworkIpamConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    return output


def marshal_PrivateNetworkStaticConfig(
    request: PrivateNetworkStaticConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ip_address is not None:
        output["ip_address"] = request.ip_address

    return output


def marshal_AttachPrivateNetworkRequest(
    request: AttachPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="static_config",
                    value=request.static_config,
                    marshal_func=marshal_PrivateNetworkStaticConfig,
                ),
                OneOfPossibility(
                    param="dhcp_config",
                    value=request.dhcp_config,
                    marshal_func=marshal_PrivateNetworkDHCPConfig,
                ),
                OneOfPossibility(
                    param="ipam_config",
                    value=request.ipam_config,
                    marshal_func=marshal_PrivateNetworkIpamConfig,
                ),
            ]
        ),
    )

    if request.ipam_ids is not None:
        output["ipam_ids"] = request.ipam_ids

    return output


def marshal_AclActionRedirect(
    request: AclActionRedirect,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    if request.target is not None:
        output["target"] = request.target

    if request.code is not None:
        output["code"] = request.code

    return output


def marshal_AclAction(
    request: AclAction,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    if request.redirect is not None:
        output["redirect"] = marshal_AclActionRedirect(request.redirect, defaults)

    return output


def marshal_AclMatch(
    request: AclMatch,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ip_subnet is not None:
        output["ip_subnet"] = request.ip_subnet

    if request.ips_edge_services is not None:
        output["ips_edge_services"] = request.ips_edge_services

    if request.http_filter is not None:
        output["http_filter"] = request.http_filter

    if request.http_filter_value is not None:
        output["http_filter_value"] = request.http_filter_value

    if request.invert is not None:
        output["invert"] = request.invert

    if request.http_filter_option is not None:
        output["http_filter_option"] = request.http_filter_option

    return output


def marshal_CreateAclRequest(
    request: CreateAclRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)

    if request.index is not None:
        output["index"] = request.index

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)

    return output


def marshal_HealthCheckHttpConfig(
    request: HealthCheckHttpConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.uri is not None:
        output["uri"] = request.uri

    if request.method is not None:
        output["method"] = request.method

    if request.host_header is not None:
        output["host_header"] = request.host_header

    if request.code is not None:
        output["code"] = request.code

    return output


def marshal_HealthCheckHttpsConfig(
    request: HealthCheckHttpsConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.uri is not None:
        output["uri"] = request.uri

    if request.method is not None:
        output["method"] = request.method

    if request.host_header is not None:
        output["host_header"] = request.host_header

    if request.sni is not None:
        output["sni"] = request.sni

    if request.code is not None:
        output["code"] = request.code

    return output


def marshal_HealthCheckLdapConfig(
    request: HealthCheckLdapConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    return output


def marshal_HealthCheckMysqlConfig(
    request: HealthCheckMysqlConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.user is not None:
        output["user"] = request.user

    return output


def marshal_HealthCheckPgsqlConfig(
    request: HealthCheckPgsqlConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.user is not None:
        output["user"] = request.user

    return output


def marshal_HealthCheckRedisConfig(
    request: HealthCheckRedisConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    return output


def marshal_HealthCheckTcpConfig(
    request: HealthCheckTcpConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    return output


def marshal_HealthCheck(
    request: HealthCheck,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="tcp_config",
                    value=request.tcp_config,
                    marshal_func=marshal_HealthCheckTcpConfig,
                ),
                OneOfPossibility(
                    param="mysql_config",
                    value=request.mysql_config,
                    marshal_func=marshal_HealthCheckMysqlConfig,
                ),
                OneOfPossibility(
                    param="pgsql_config",
                    value=request.pgsql_config,
                    marshal_func=marshal_HealthCheckPgsqlConfig,
                ),
                OneOfPossibility(
                    param="ldap_config",
                    value=request.ldap_config,
                    marshal_func=marshal_HealthCheckLdapConfig,
                ),
                OneOfPossibility(
                    param="redis_config",
                    value=request.redis_config,
                    marshal_func=marshal_HealthCheckRedisConfig,
                ),
                OneOfPossibility(
                    param="http_config",
                    value=request.http_config,
                    marshal_func=marshal_HealthCheckHttpConfig,
                ),
                OneOfPossibility(
                    param="https_config",
                    value=request.https_config,
                    marshal_func=marshal_HealthCheckHttpsConfig,
                ),
            ]
        ),
    )

    if request.port is not None:
        output["port"] = request.port

    if request.check_max_retries is not None:
        output["check_max_retries"] = request.check_max_retries

    if request.check_send_proxy is not None:
        output["check_send_proxy"] = request.check_send_proxy

    if request.check_delay is not None:
        output["check_delay"] = request.check_delay

    if request.check_timeout is not None:
        output["check_timeout"] = request.check_timeout

    if request.transient_check_delay is not None:
        output["transient_check_delay"] = request.transient_check_delay

    return output


def marshal_CreateBackendRequest(
    request: CreateBackendRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.forward_protocol is not None:
        output["forward_protocol"] = request.forward_protocol

    if request.forward_port is not None:
        output["forward_port"] = request.forward_port

    if request.forward_port_algorithm is not None:
        output["forward_port_algorithm"] = request.forward_port_algorithm

    if request.sticky_sessions is not None:
        output["sticky_sessions"] = request.sticky_sessions

    if request.sticky_sessions_cookie_name is not None:
        output["sticky_sessions_cookie_name"] = request.sticky_sessions_cookie_name

    if request.health_check is not None:
        output["health_check"] = marshal_HealthCheck(request.health_check, defaults)

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    if request.name is not None:
        output["name"] = request.name

    if request.send_proxy_v2 is not None:
        output["send_proxy_v2"] = request.send_proxy_v2

    if request.timeout_server is not None:
        output["timeout_server"] = request.timeout_server

    if request.timeout_connect is not None:
        output["timeout_connect"] = request.timeout_connect

    if request.timeout_tunnel is not None:
        output["timeout_tunnel"] = request.timeout_tunnel

    if request.on_marked_down_action is not None:
        output["on_marked_down_action"] = request.on_marked_down_action

    if request.proxy_protocol is not None:
        output["proxy_protocol"] = request.proxy_protocol

    if request.failover_host is not None:
        output["failover_host"] = request.failover_host

    if request.ssl_bridging is not None:
        output["ssl_bridging"] = request.ssl_bridging

    if request.ignore_ssl_server_verify is not None:
        output["ignore_ssl_server_verify"] = request.ignore_ssl_server_verify

    if request.redispatch_attempt_count is not None:
        output["redispatch_attempt_count"] = request.redispatch_attempt_count

    if request.max_retries is not None:
        output["max_retries"] = request.max_retries

    if request.max_connections is not None:
        output["max_connections"] = request.max_connections

    if request.timeout_queue is not None:
        output["timeout_queue"] = request.timeout_queue

    return output


def marshal_CreateCertificateRequestCustomCertificate(
    request: CreateCertificateRequestCustomCertificate,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.certificate_chain is not None:
        output["certificate_chain"] = request.certificate_chain

    return output


def marshal_CreateCertificateRequestLetsencryptConfig(
    request: CreateCertificateRequestLetsencryptConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.common_name is not None:
        output["common_name"] = request.common_name

    if request.subject_alternative_name is not None:
        output["subject_alternative_name"] = request.subject_alternative_name

    return output


def marshal_CreateCertificateRequest(
    request: CreateCertificateRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="letsencrypt",
                    value=request.letsencrypt,
                    marshal_func=marshal_CreateCertificateRequestLetsencryptConfig,
                ),
                OneOfPossibility(
                    param="custom_certificate",
                    value=request.custom_certificate,
                    marshal_func=marshal_CreateCertificateRequestCustomCertificate,
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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.inbound_port is not None:
        output["inbound_port"] = request.inbound_port

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.enable_http3 is not None:
        output["enable_http3"] = request.enable_http3

    if request.enable_access_logs is not None:
        output["enable_access_logs"] = request.enable_access_logs

    if request.name is not None:
        output["name"] = request.name

    if request.timeout_client is not None:
        output["timeout_client"] = request.timeout_client

    if request.certificate_id is not None:
        output["certificate_id"] = request.certificate_id

    if request.certificate_ids is not None:
        output["certificate_ids"] = request.certificate_ids

    if request.connection_rate_limit is not None:
        output["connection_rate_limit"] = request.connection_rate_limit

    return output


def marshal_CreateIpRequest(
    request: CreateIpRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project_id",
                    value=request.project_id,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization_id",
                    value=request.organization_id,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6

    if request.reverse is not None:
        output["reverse"] = request.reverse

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateLbRequest(
    request: CreateLbRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project_id",
                    value=request.project_id,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization_id",
                    value=request.organization_id,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.description is not None:
        output["description"] = request.description

    if request.type_ is not None:
        output["type"] = request.type_

    if request.name is not None:
        output["name"] = request.name

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id

    if request.assign_flexible_ip is not None:
        output["assign_flexible_ip"] = request.assign_flexible_ip

    if request.assign_flexible_ipv6 is not None:
        output["assign_flexible_ipv6"] = request.assign_flexible_ipv6

    if request.ip_ids is not None:
        output["ip_ids"] = request.ip_ids

    if request.tags is not None:
        output["tags"] = request.tags

    if request.ssl_compatibility_level is not None:
        output["ssl_compatibility_level"] = request.ssl_compatibility_level

    return output


def marshal_RouteMatch(
    request: RouteMatch,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(param="sni", value=request.sni, marshal_func=None),
                OneOfPossibility(
                    param="host_header", value=request.host_header, marshal_func=None
                ),
                OneOfPossibility(
                    param="path_begin", value=request.path_begin, marshal_func=None
                ),
            ]
        ),
    )

    if request.match_subdomains is not None:
        output["match_subdomains"] = request.match_subdomains

    return output


def marshal_CreateRouteRequest(
    request: CreateRouteRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.frontend_id is not None:
        output["frontend_id"] = request.frontend_id

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.match is not None:
        output["match"] = marshal_RouteMatch(request.match, defaults)

    return output


def marshal_SubscriberEmailConfig(
    request: SubscriberEmailConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email

    return output


def marshal_SubscriberWebhookConfig(
    request: SubscriberWebhookConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.uri is not None:
        output["uri"] = request.uri

    return output


def marshal_CreateSubscriberRequest(
    request: CreateSubscriberRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project_id",
                    value=request.project_id,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization_id",
                    value=request.organization_id,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="email_config",
                    value=request.email_config,
                    marshal_func=marshal_SubscriberEmailConfig,
                ),
                OneOfPossibility(
                    param="webhook_config",
                    value=request.webhook_config,
                    marshal_func=marshal_SubscriberWebhookConfig,
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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    return output


def marshal_RemoveBackendServersRequest(
    request: RemoveBackendServersRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    return output


def marshal_SetBackendServersRequest(
    request: SetBackendServersRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    return output


def marshal_SubscribeToLbRequest(
    request: SubscribeToLbRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.subscriber_id is not None:
        output["subscriber_id"] = request.subscriber_id

    return output


def marshal_UpdateAclRequest(
    request: UpdateAclRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)

    if request.index is not None:
        output["index"] = request.index

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_UpdateBackendRequest(
    request: UpdateBackendRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.forward_protocol is not None:
        output["forward_protocol"] = request.forward_protocol

    if request.forward_port is not None:
        output["forward_port"] = request.forward_port

    if request.forward_port_algorithm is not None:
        output["forward_port_algorithm"] = request.forward_port_algorithm

    if request.sticky_sessions is not None:
        output["sticky_sessions"] = request.sticky_sessions

    if request.sticky_sessions_cookie_name is not None:
        output["sticky_sessions_cookie_name"] = request.sticky_sessions_cookie_name

    if request.send_proxy_v2 is not None:
        output["send_proxy_v2"] = request.send_proxy_v2

    if request.timeout_server is not None:
        output["timeout_server"] = request.timeout_server

    if request.timeout_connect is not None:
        output["timeout_connect"] = request.timeout_connect

    if request.timeout_tunnel is not None:
        output["timeout_tunnel"] = request.timeout_tunnel

    if request.on_marked_down_action is not None:
        output["on_marked_down_action"] = request.on_marked_down_action

    if request.proxy_protocol is not None:
        output["proxy_protocol"] = request.proxy_protocol

    if request.failover_host is not None:
        output["failover_host"] = request.failover_host

    if request.ssl_bridging is not None:
        output["ssl_bridging"] = request.ssl_bridging

    if request.ignore_ssl_server_verify is not None:
        output["ignore_ssl_server_verify"] = request.ignore_ssl_server_verify

    if request.redispatch_attempt_count is not None:
        output["redispatch_attempt_count"] = request.redispatch_attempt_count

    if request.max_retries is not None:
        output["max_retries"] = request.max_retries

    if request.max_connections is not None:
        output["max_connections"] = request.max_connections

    if request.timeout_queue is not None:
        output["timeout_queue"] = request.timeout_queue

    return output


def marshal_UpdateCertificateRequest(
    request: UpdateCertificateRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_UpdateFrontendRequest(
    request: UpdateFrontendRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.inbound_port is not None:
        output["inbound_port"] = request.inbound_port

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.enable_http3 is not None:
        output["enable_http3"] = request.enable_http3

    if request.timeout_client is not None:
        output["timeout_client"] = request.timeout_client

    if request.certificate_id is not None:
        output["certificate_id"] = request.certificate_id

    if request.certificate_ids is not None:
        output["certificate_ids"] = request.certificate_ids

    if request.connection_rate_limit is not None:
        output["connection_rate_limit"] = request.connection_rate_limit

    if request.enable_access_logs is not None:
        output["enable_access_logs"] = request.enable_access_logs

    return output


def marshal_UpdateHealthCheckRequest(
    request: UpdateHealthCheckRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="tcp_config",
                    value=request.tcp_config,
                    marshal_func=marshal_HealthCheckTcpConfig,
                ),
                OneOfPossibility(
                    param="mysql_config",
                    value=request.mysql_config,
                    marshal_func=marshal_HealthCheckMysqlConfig,
                ),
                OneOfPossibility(
                    param="pgsql_config",
                    value=request.pgsql_config,
                    marshal_func=marshal_HealthCheckPgsqlConfig,
                ),
                OneOfPossibility(
                    param="ldap_config",
                    value=request.ldap_config,
                    marshal_func=marshal_HealthCheckLdapConfig,
                ),
                OneOfPossibility(
                    param="redis_config",
                    value=request.redis_config,
                    marshal_func=marshal_HealthCheckRedisConfig,
                ),
                OneOfPossibility(
                    param="http_config",
                    value=request.http_config,
                    marshal_func=marshal_HealthCheckHttpConfig,
                ),
                OneOfPossibility(
                    param="https_config",
                    value=request.https_config,
                    marshal_func=marshal_HealthCheckHttpsConfig,
                ),
            ]
        ),
    )

    if request.port is not None:
        output["port"] = request.port

    if request.check_max_retries is not None:
        output["check_max_retries"] = request.check_max_retries

    if request.check_send_proxy is not None:
        output["check_send_proxy"] = request.check_send_proxy

    if request.check_delay is not None:
        output["check_delay"] = request.check_delay

    if request.check_timeout is not None:
        output["check_timeout"] = request.check_timeout

    if request.transient_check_delay is not None:
        output["transient_check_delay"] = request.transient_check_delay

    return output


def marshal_UpdateIpRequest(
    request: UpdateIpRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.reverse is not None:
        output["reverse"] = request.reverse

    if request.lb_id is not None:
        output["lb_id"] = request.lb_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateLbRequest(
    request: UpdateLbRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.tags is not None:
        output["tags"] = request.tags

    if request.ssl_compatibility_level is not None:
        output["ssl_compatibility_level"] = request.ssl_compatibility_level

    return output


def marshal_UpdateRouteRequest(
    request: UpdateRouteRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.match is not None:
        output["match"] = marshal_RouteMatch(request.match, defaults)

    return output


def marshal_UpdateSubscriberRequest(
    request: UpdateSubscriberRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="email_config",
                    value=request.email_config,
                    marshal_func=marshal_SubscriberEmailConfig,
                ),
                OneOfPossibility(
                    param="webhook_config",
                    value=request.webhook_config,
                    marshal_func=marshal_SubscriberWebhookConfig,
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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    return output


def marshal_ZonedApiAttachPrivateNetworkRequest(
    request: ZonedApiAttachPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="static_config",
                    value=request.static_config,
                    marshal_func=marshal_PrivateNetworkStaticConfig,
                ),
                OneOfPossibility(
                    param="dhcp_config",
                    value=request.dhcp_config,
                    marshal_func=marshal_PrivateNetworkDHCPConfig,
                ),
                OneOfPossibility(
                    param="ipam_config",
                    value=request.ipam_config,
                    marshal_func=marshal_PrivateNetworkIpamConfig,
                ),
            ]
        ),
    )

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.ipam_ids is not None:
        output["ipam_ids"] = request.ipam_ids

    return output


def marshal_ZonedApiCreateAclRequest(
    request: ZonedApiCreateAclRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)

    if request.index is not None:
        output["index"] = request.index

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)

    return output


def marshal_ZonedApiCreateBackendRequest(
    request: ZonedApiCreateBackendRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.forward_protocol is not None:
        output["forward_protocol"] = request.forward_protocol

    if request.forward_port is not None:
        output["forward_port"] = request.forward_port

    if request.forward_port_algorithm is not None:
        output["forward_port_algorithm"] = request.forward_port_algorithm

    if request.sticky_sessions is not None:
        output["sticky_sessions"] = request.sticky_sessions

    if request.sticky_sessions_cookie_name is not None:
        output["sticky_sessions_cookie_name"] = request.sticky_sessions_cookie_name

    if request.health_check is not None:
        output["health_check"] = marshal_HealthCheck(request.health_check, defaults)

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    if request.name is not None:
        output["name"] = request.name

    if request.send_proxy_v2 is not None:
        output["send_proxy_v2"] = request.send_proxy_v2

    if request.timeout_server is not None:
        output["timeout_server"] = request.timeout_server

    if request.timeout_connect is not None:
        output["timeout_connect"] = request.timeout_connect

    if request.timeout_tunnel is not None:
        output["timeout_tunnel"] = request.timeout_tunnel

    if request.on_marked_down_action is not None:
        output["on_marked_down_action"] = request.on_marked_down_action

    if request.proxy_protocol is not None:
        output["proxy_protocol"] = request.proxy_protocol

    if request.failover_host is not None:
        output["failover_host"] = request.failover_host

    if request.ssl_bridging is not None:
        output["ssl_bridging"] = request.ssl_bridging

    if request.ignore_ssl_server_verify is not None:
        output["ignore_ssl_server_verify"] = request.ignore_ssl_server_verify

    if request.redispatch_attempt_count is not None:
        output["redispatch_attempt_count"] = request.redispatch_attempt_count

    if request.max_retries is not None:
        output["max_retries"] = request.max_retries

    if request.max_connections is not None:
        output["max_connections"] = request.max_connections

    if request.timeout_queue is not None:
        output["timeout_queue"] = request.timeout_queue

    return output


def marshal_ZonedApiCreateCertificateRequest(
    request: ZonedApiCreateCertificateRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="letsencrypt",
                    value=request.letsencrypt,
                    marshal_func=marshal_CreateCertificateRequestLetsencryptConfig,
                ),
                OneOfPossibility(
                    param="custom_certificate",
                    value=request.custom_certificate,
                    marshal_func=marshal_CreateCertificateRequestCustomCertificate,
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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.inbound_port is not None:
        output["inbound_port"] = request.inbound_port

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.enable_http3 is not None:
        output["enable_http3"] = request.enable_http3

    if request.enable_access_logs is not None:
        output["enable_access_logs"] = request.enable_access_logs

    if request.name is not None:
        output["name"] = request.name

    if request.timeout_client is not None:
        output["timeout_client"] = request.timeout_client

    if request.certificate_id is not None:
        output["certificate_id"] = request.certificate_id

    if request.certificate_ids is not None:
        output["certificate_ids"] = request.certificate_ids

    if request.connection_rate_limit is not None:
        output["connection_rate_limit"] = request.connection_rate_limit

    return output


def marshal_ZonedApiCreateIpRequest(
    request: ZonedApiCreateIpRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project_id",
                    value=request.project_id,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization_id",
                    value=request.organization_id,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6

    if request.reverse is not None:
        output["reverse"] = request.reverse

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_ZonedApiCreateLbRequest(
    request: ZonedApiCreateLbRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project_id",
                    value=request.project_id,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization_id",
                    value=request.organization_id,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.description is not None:
        output["description"] = request.description

    if request.type_ is not None:
        output["type"] = request.type_

    if request.name is not None:
        output["name"] = request.name

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id

    if request.assign_flexible_ip is not None:
        output["assign_flexible_ip"] = request.assign_flexible_ip

    if request.assign_flexible_ipv6 is not None:
        output["assign_flexible_ipv6"] = request.assign_flexible_ipv6

    if request.ip_ids is not None:
        output["ip_ids"] = request.ip_ids

    if request.tags is not None:
        output["tags"] = request.tags

    if request.ssl_compatibility_level is not None:
        output["ssl_compatibility_level"] = request.ssl_compatibility_level

    return output


def marshal_ZonedApiCreateRouteRequest(
    request: ZonedApiCreateRouteRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.frontend_id is not None:
        output["frontend_id"] = request.frontend_id

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.match is not None:
        output["match"] = marshal_RouteMatch(request.match, defaults)

    return output


def marshal_ZonedApiCreateSubscriberRequest(
    request: ZonedApiCreateSubscriberRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project_id",
                    value=request.project_id,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization_id",
                    value=request.organization_id,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="email_config",
                    value=request.email_config,
                    marshal_func=marshal_SubscriberEmailConfig,
                ),
                OneOfPossibility(
                    param="webhook_config",
                    value=request.webhook_config,
                    marshal_func=marshal_SubscriberWebhookConfig,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_ZonedApiDetachPrivateNetworkRequest(
    request: ZonedApiDetachPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    return output


def marshal_ZonedApiMigrateLbRequest(
    request: ZonedApiMigrateLbRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    return output


def marshal_ZonedApiRemoveBackendServersRequest(
    request: ZonedApiRemoveBackendServersRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    return output


def marshal_AclSpec(
    request: AclSpec,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)

    if request.index is not None:
        output["index"] = request.index

    if request.description is not None:
        output["description"] = request.description

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)

    return output


def marshal_ZonedApiSetAclsRequest(
    request: ZonedApiSetAclsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.acls is not None:
        output["acls"] = [marshal_AclSpec(item, defaults) for item in request.acls]

    return output


def marshal_ZonedApiSetBackendServersRequest(
    request: ZonedApiSetBackendServersRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip

    return output


def marshal_ZonedApiSubscribeToLbRequest(
    request: ZonedApiSubscribeToLbRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.subscriber_id is not None:
        output["subscriber_id"] = request.subscriber_id

    return output


def marshal_ZonedApiUpdateAclRequest(
    request: ZonedApiUpdateAclRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)

    if request.index is not None:
        output["index"] = request.index

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_ZonedApiUpdateBackendRequest(
    request: ZonedApiUpdateBackendRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.forward_protocol is not None:
        output["forward_protocol"] = request.forward_protocol

    if request.forward_port is not None:
        output["forward_port"] = request.forward_port

    if request.forward_port_algorithm is not None:
        output["forward_port_algorithm"] = request.forward_port_algorithm

    if request.sticky_sessions is not None:
        output["sticky_sessions"] = request.sticky_sessions

    if request.sticky_sessions_cookie_name is not None:
        output["sticky_sessions_cookie_name"] = request.sticky_sessions_cookie_name

    if request.send_proxy_v2 is not None:
        output["send_proxy_v2"] = request.send_proxy_v2

    if request.timeout_server is not None:
        output["timeout_server"] = request.timeout_server

    if request.timeout_connect is not None:
        output["timeout_connect"] = request.timeout_connect

    if request.timeout_tunnel is not None:
        output["timeout_tunnel"] = request.timeout_tunnel

    if request.on_marked_down_action is not None:
        output["on_marked_down_action"] = request.on_marked_down_action

    if request.proxy_protocol is not None:
        output["proxy_protocol"] = request.proxy_protocol

    if request.failover_host is not None:
        output["failover_host"] = request.failover_host

    if request.ssl_bridging is not None:
        output["ssl_bridging"] = request.ssl_bridging

    if request.ignore_ssl_server_verify is not None:
        output["ignore_ssl_server_verify"] = request.ignore_ssl_server_verify

    if request.redispatch_attempt_count is not None:
        output["redispatch_attempt_count"] = request.redispatch_attempt_count

    if request.max_retries is not None:
        output["max_retries"] = request.max_retries

    if request.max_connections is not None:
        output["max_connections"] = request.max_connections

    if request.timeout_queue is not None:
        output["timeout_queue"] = request.timeout_queue

    return output


def marshal_ZonedApiUpdateCertificateRequest(
    request: ZonedApiUpdateCertificateRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_ZonedApiUpdateFrontendRequest(
    request: ZonedApiUpdateFrontendRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.inbound_port is not None:
        output["inbound_port"] = request.inbound_port

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.enable_http3 is not None:
        output["enable_http3"] = request.enable_http3

    if request.timeout_client is not None:
        output["timeout_client"] = request.timeout_client

    if request.certificate_id is not None:
        output["certificate_id"] = request.certificate_id

    if request.certificate_ids is not None:
        output["certificate_ids"] = request.certificate_ids

    if request.connection_rate_limit is not None:
        output["connection_rate_limit"] = request.connection_rate_limit

    if request.enable_access_logs is not None:
        output["enable_access_logs"] = request.enable_access_logs

    return output


def marshal_ZonedApiUpdateHealthCheckRequest(
    request: ZonedApiUpdateHealthCheckRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="tcp_config",
                    value=request.tcp_config,
                    marshal_func=marshal_HealthCheckTcpConfig,
                ),
                OneOfPossibility(
                    param="mysql_config",
                    value=request.mysql_config,
                    marshal_func=marshal_HealthCheckMysqlConfig,
                ),
                OneOfPossibility(
                    param="pgsql_config",
                    value=request.pgsql_config,
                    marshal_func=marshal_HealthCheckPgsqlConfig,
                ),
                OneOfPossibility(
                    param="ldap_config",
                    value=request.ldap_config,
                    marshal_func=marshal_HealthCheckLdapConfig,
                ),
                OneOfPossibility(
                    param="redis_config",
                    value=request.redis_config,
                    marshal_func=marshal_HealthCheckRedisConfig,
                ),
                OneOfPossibility(
                    param="http_config",
                    value=request.http_config,
                    marshal_func=marshal_HealthCheckHttpConfig,
                ),
                OneOfPossibility(
                    param="https_config",
                    value=request.https_config,
                    marshal_func=marshal_HealthCheckHttpsConfig,
                ),
            ]
        ),
    )

    if request.port is not None:
        output["port"] = request.port

    if request.check_max_retries is not None:
        output["check_max_retries"] = request.check_max_retries

    if request.check_send_proxy is not None:
        output["check_send_proxy"] = request.check_send_proxy

    if request.check_delay is not None:
        output["check_delay"] = request.check_delay

    if request.check_timeout is not None:
        output["check_timeout"] = request.check_timeout

    if request.transient_check_delay is not None:
        output["transient_check_delay"] = request.transient_check_delay

    return output


def marshal_ZonedApiUpdateIpRequest(
    request: ZonedApiUpdateIpRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.reverse is not None:
        output["reverse"] = request.reverse

    if request.lb_id is not None:
        output["lb_id"] = request.lb_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_ZonedApiUpdateLbRequest(
    request: ZonedApiUpdateLbRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.tags is not None:
        output["tags"] = request.tags

    if request.ssl_compatibility_level is not None:
        output["ssl_compatibility_level"] = request.ssl_compatibility_level

    return output


def marshal_ZonedApiUpdateRouteRequest(
    request: ZonedApiUpdateRouteRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.match is not None:
        output["match"] = marshal_RouteMatch(request.match, defaults)

    return output


def marshal_ZonedApiUpdateSubscriberRequest(
    request: ZonedApiUpdateSubscriberRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="email_config",
                    value=request.email_config,
                    marshal_func=marshal_SubscriberEmailConfig,
                ),
                OneOfPossibility(
                    param="webhook_config",
                    value=request.webhook_config,
                    marshal_func=marshal_SubscriberWebhookConfig,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    return output
