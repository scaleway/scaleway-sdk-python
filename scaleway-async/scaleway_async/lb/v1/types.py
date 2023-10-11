# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Region,
    Zone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class AclActionRedirectRedirectType(str, Enum, metaclass=StrEnumMeta):
    LOCATION = "location"
    SCHEME = "scheme"

    def __str__(self) -> str:
        return str(self.value)


class AclActionType(str, Enum, metaclass=StrEnumMeta):
    ALLOW = "allow"
    DENY = "deny"
    REDIRECT = "redirect"

    def __str__(self) -> str:
        return str(self.value)


class AclHttpFilter(str, Enum, metaclass=StrEnumMeta):
    ACL_HTTP_FILTER_NONE = "acl_http_filter_none"
    PATH_BEGIN = "path_begin"
    PATH_END = "path_end"
    REGEX = "regex"
    HTTP_HEADER_MATCH = "http_header_match"

    def __str__(self) -> str:
        return str(self.value)


class BackendServerStatsHealthCheckStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    NEUTRAL = "neutral"
    FAILED = "failed"
    PASSED = "passed"
    CONDPASS = "condpass"

    def __str__(self) -> str:
        return str(self.value)


class BackendServerStatsServerState(str, Enum, metaclass=StrEnumMeta):
    STOPPED = "stopped"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"

    def __str__(self) -> str:
        return str(self.value)


class CertificateStatus(str, Enum, metaclass=StrEnumMeta):
    PENDING = "pending"
    READY = "ready"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class CertificateType(str, Enum, metaclass=StrEnumMeta):
    LETSENCRYT = "letsencryt"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)


class ForwardPortAlgorithm(str, Enum, metaclass=StrEnumMeta):
    ROUNDROBIN = "roundrobin"
    LEASTCONN = "leastconn"
    FIRST = "first"

    def __str__(self) -> str:
        return str(self.value)


class InstanceStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    PENDING = "pending"
    STOPPED = "stopped"
    ERROR = "error"
    LOCKED = "locked"
    MIGRATING = "migrating"

    def __str__(self) -> str:
        return str(self.value)


class LbStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    PENDING = "pending"
    STOPPED = "stopped"
    ERROR = "error"
    LOCKED = "locked"
    MIGRATING = "migrating"
    TO_CREATE = "to_create"
    CREATING = "creating"
    TO_DELETE = "to_delete"
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)


class LbTypeStock(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    LOW_STOCK = "low_stock"
    OUT_OF_STOCK = "out_of_stock"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)


class ListAclRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListBackendsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListCertificatesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListFrontendsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListLbsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPrivateNetworksRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRoutesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSubscriberRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class OnMarkedDownAction(str, Enum, metaclass=StrEnumMeta):
    ON_MARKED_DOWN_ACTION_NONE = "on_marked_down_action_none"
    SHUTDOWN_SESSIONS = "shutdown_sessions"

    def __str__(self) -> str:
        return str(self.value)


class PrivateNetworkStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    PENDING = "pending"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class Protocol(str, Enum, metaclass=StrEnumMeta):
    TCP = "tcp"
    HTTP = "http"

    def __str__(self) -> str:
        return str(self.value)


class ProxyProtocol(str, Enum, metaclass=StrEnumMeta):
    PROXY_PROTOCOL_UNKNOWN = "proxy_protocol_unknown"
    PROXY_PROTOCOL_NONE = "proxy_protocol_none"
    PROXY_PROTOCOL_V1 = "proxy_protocol_v1"
    PROXY_PROTOCOL_V2 = "proxy_protocol_v2"
    PROXY_PROTOCOL_V2_SSL = "proxy_protocol_v2_ssl"
    PROXY_PROTOCOL_V2_SSL_CN = "proxy_protocol_v2_ssl_cn"

    def __str__(self) -> str:
        return str(self.value)


class SSLCompatibilityLevel(str, Enum, metaclass=StrEnumMeta):
    SSL_COMPATIBILITY_LEVEL_UNKNOWN = "ssl_compatibility_level_unknown"
    SSL_COMPATIBILITY_LEVEL_INTERMEDIATE = "ssl_compatibility_level_intermediate"
    SSL_COMPATIBILITY_LEVEL_MODERN = "ssl_compatibility_level_modern"
    SSL_COMPATIBILITY_LEVEL_OLD = "ssl_compatibility_level_old"

    def __str__(self) -> str:
        return str(self.value)


class StickySessionsType(str, Enum, metaclass=StrEnumMeta):
    NONE = "none"
    COOKIE = "cookie"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class SubscriberEmailConfig:
    email: str
    """
    Email address to send alerts to.
    """


@dataclass
class SubscriberWebhookConfig:
    """
    Webhook alert of subscriber.
    """

    uri: str
    """
    URI to receive POST requests.
    """


@dataclass
class HealthCheckHttpConfig:
    host_header: str
    """
    The HTTP host header used when performing a health check on backend servers.
    """

    method: str
    """
    The HTTP method used when performing a health check on backend servers.
    """

    uri: str
    """
    The HTTP URI to use when performing a health check on backend servers.
    """

    code: Optional[int]
    """
    The HTTP response code that should be returned for a health check to be considered successful.
    """


@dataclass
class HealthCheckHttpsConfig:
    sni: str
    """
    The SNI value used when performing a health check on backend servers over SSL.
    """

    host_header: str
    """
    The HTTP host header used when performing a health check on backend servers.
    """

    method: str
    """
    The HTTP method used when performing a health check on backend servers.
    """

    uri: str
    """
    The HTTP URI to use when performing a health check on backend servers.
    """

    code: Optional[int]
    """
    The HTTP response code that should be returned for a health check to be considered successful.
    """


@dataclass
class HealthCheckLdapConfig:
    pass


@dataclass
class HealthCheckMysqlConfig:
    user: str
    """
    MySQL user to use for the health check.
    """


@dataclass
class HealthCheckPgsqlConfig:
    user: str
    """
    PostgreSQL user to use for the health check.
    """


@dataclass
class HealthCheckRedisConfig:
    pass


@dataclass
class HealthCheckTcpConfig:
    pass


@dataclass
class Instance:
    zone: Zone
    """
    The zone the Instance is in.
    """

    ip_address: str
    """
    Instance IP address.
    """

    status: InstanceStatus
    """
    Instance status.
    """

    id: str
    """
    Underlying Instance ID.
    """

    created_at: Optional[datetime]
    """
    Date on which the Instance was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the Instance was last updated.
    """

    region: Optional[Region]
    """
    The region the Instance is in.
    """


@dataclass
class Ip:
    zone: Zone
    """
    The zone the IP address is in.
    """

    reverse: str
    """
    Reverse DNS (domain name) of the IP address.
    """

    project_id: str
    """
    Project ID of the Scaleway Project the IP address is in.
    """

    organization_id: str
    """
    Organization ID of the Scaleway Organization the IP address is in.
    """

    ip_address: str
    """
    IP address.
    """

    id: str
    """
    IP address ID.
    """

    lb_id: Optional[str]
    """
    Load Balancer ID.
    """

    region: Optional[Region]
    """
    The region the IP address is in.
    """


@dataclass
class Subscriber:
    """
    Subscriber.
    """

    name: str
    """
    Subscriber name.
    """

    id: str
    """
    Subscriber ID.
    """

    email_config: Optional[SubscriberEmailConfig]

    webhook_config: Optional[SubscriberWebhookConfig]


@dataclass
class HealthCheck:
    check_send_proxy: bool
    """
    Defines whether proxy protocol should be activated for the health check.
    """

    check_max_retries: int
    """
    Number of consecutive unsuccessful health checks after which the server will be considered dead.
    """

    port: int
    """
    Port to use for the backend server health check.
    """

    check_delay: Optional[str]
    """
    Time to wait between two consecutive health checks.
    """

    check_timeout: Optional[str]
    """
    Maximum time a backend server has to reply to the health check.
    """

    transient_check_delay: Optional[str]
    """
    Time to wait between two consecutive health checks when a backend server is in a transient state (going UP or DOWN).
    """

    tcp_config: Optional[HealthCheckTcpConfig]

    mysql_config: Optional[HealthCheckMysqlConfig]

    pgsql_config: Optional[HealthCheckPgsqlConfig]

    ldap_config: Optional[HealthCheckLdapConfig]

    redis_config: Optional[HealthCheckRedisConfig]

    http_config: Optional[HealthCheckHttpConfig]

    https_config: Optional[HealthCheckHttpsConfig]


@dataclass
class Lb:
    type_: str
    """
    Load Balancer offer type.
    """

    id: str
    """
    Underlying Instance ID.
    """

    frontend_count: int
    """
    Number of frontends the Load Balancer has.
    """

    private_network_count: int
    """
    Number of Private Networks attached to the Load Balancer.
    """

    status: LbStatus
    """
    Load Balancer status.
    """

    ssl_compatibility_level: SSLCompatibilityLevel
    """
    Determines the minimal SSL version which needs to be supported on client side.
    """

    route_count: int
    """
    Number of routes configured on the Load Balancer.
    """

    instances: List[Instance]
    """
    List of underlying Instances.
    """

    ip: List[Ip]
    """
    List of IP addresses attached to the Load Balancer.
    """

    description: str
    """
    Load Balancer description.
    """

    name: str
    """
    Load Balancer name.
    """

    subscriber: Subscriber
    """
    Subscriber information.
    """

    zone: Zone
    """
    The zone the Load Balancer is in.
    """

    project_id: str
    """
    Scaleway Project ID.
    """

    organization_id: str
    """
    Scaleway Organization ID.
    """

    tags: List[str]
    """
    Load Balancer tags.
    """

    backend_count: int
    """
    Number of backends the Load Balancer has.
    """

    updated_at: Optional[datetime]
    """
    Date on which the Load Balancer was last updated.
    """

    region: Optional[Region]
    """
    The region the Load Balancer is in.
    """

    created_at: Optional[datetime]
    """
    Date on which the Load Balancer was created.
    """


@dataclass
class AclActionRedirect:
    target: str
    """
    Redirect target. For a location redirect, you can use a URL e.g. `https://scaleway.com`. Using a scheme name (e.g. `https`, `http`, `ftp`, `git`) will replace the request's original scheme. This can be useful to implement HTTP to HTTPS redirects. Valid placeholders that can be used in a `location` redirect to preserve parts of the original request in the redirection URL are \{\{host\}\}, \{\{query\}\}, \{\{path\}\} and \{\{scheme\}\}.
    """

    type_: AclActionRedirectRedirectType
    """
    Redirect type.
    """

    code: Optional[int]
    """
    HTTP redirect code to use. Valid values are 301, 302, 303, 307 and 308. Default value is 302.
    """


@dataclass
class Backend:
    on_marked_down_action: OnMarkedDownAction
    """
    Action to take when a backend server is marked as down.
    """

    proxy_protocol: ProxyProtocol
    """
    Protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. The PROXY protocol must be supported by the backend servers' software.
    """

    lb: Lb
    """
    Load Balancer the backend is attached to.
    """

    pool: List[str]
    """
    List of IP addresses of backend servers attached to this backend.
    """

    health_check: HealthCheck
    """
    Object defining the health check to be carried out by the backend when checking the status and health of backend servers.
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for cookie-based sticky sessions.
    """

    sticky_sessions: StickySessionsType
    """
    Defines whether sticky sessions (binding a particular session to a particular backend server) are activated and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie to stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
    """

    forward_port_algorithm: ForwardPortAlgorithm
    """
    Load balancing algorithm to use when determining which backend server to forward new traffic to.
    """

    forward_port: int
    """
    Port used by the backend when forwarding traffic to backend servers.
    """

    forward_protocol: Protocol
    """
    Protocol used by the backend when forwarding traffic to backend servers.
    """

    name: str
    """
    Name of the backend.
    """

    id: str
    """
    Backend ID.
    """

    timeout_connect: Optional[str]
    """
    Maximum allowed time for establishing a connection to a backend server.
    """

    timeout_tunnel: Optional[str]
    """
    Maximum allowed tunnel inactivity time after Websocket is established (takes precedence over client and server timeout).
    """

    timeout_server: Optional[str]
    """
    Maximum allowed time for a backend server to process a request.
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field.
    """

    created_at: Optional[datetime]
    """
    Date at which the backend was created.
    """

    updated_at: Optional[datetime]
    """
    Date at which the backend was updated.
    """

    failover_host: Optional[str]
    """
    Scaleway S3 bucket website to be served as failover if all backend servers are down, e.g. failover-website.s3-website.fr-par.scw.cloud.
    """

    ssl_bridging: Optional[bool]
    """
    Defines whether to enable SSL bridging between the Load Balancer and backend servers.
    """

    ignore_ssl_server_verify: Optional[bool]
    """
    Defines whether the server certificate verification should be ignored.
    """

    redispatch_attempt_count: Optional[int]
    """
    Whether to use another backend server on each attempt.
    """

    max_retries: Optional[int]
    """
    Number of retries when a backend server connection failed.
    """

    max_connections: Optional[int]
    """
    Maximum number of connections allowed per backend server.
    """

    timeout_queue: Optional[str]
    """
    Maximum time for a request to be left pending in queue when `max_connections` is reached.
    """


@dataclass
class Certificate:
    lb: Lb
    """
    Load Balancer object the certificate is attached to.
    """

    name: str
    """
    Certificate name.
    """

    fingerprint: str
    """
    Identifier (SHA-1) of the certificate.
    """

    type_: CertificateType
    """
    Certificate type (Let's Encrypt or custom).
    """

    common_name: str
    """
    Main domain name of certificate.
    """

    id: str
    """
    Certificate ID.
    """

    status: CertificateStatus
    """
    Certificate status.
    """

    subject_alternative_name: List[str]
    """
    Alternative domain names.
    """

    not_valid_after: Optional[datetime]
    """
    Upper validity bound.
    """

    not_valid_before: Optional[datetime]
    """
    Lower validity bound.
    """

    created_at: Optional[datetime]
    """
    Date on which the certificate was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the certificate was last updated.
    """

    status_details: Optional[str]
    """
    Additional information about the certificate status (useful in case of certificate generation failure, for example).
    """


@dataclass
class AclAction:
    redirect: AclActionRedirect
    """
    Redirection parameters when using an ACL with a `redirect` action.
    """

    type_: AclActionType
    """
    Action to take when incoming traffic matches an ACL filter.
    """


@dataclass
class AclMatch:
    invert: bool
    """
    Defines whether to invert the match condition. If set to `true`, the ACL carries out its action when the condition DOES NOT match.
    """

    http_filter_value: List[str]
    """
    List of values to filter for.
    """

    http_filter: AclHttpFilter
    """
    Type of HTTP filter to match. Extracts the request's URL path, which starts at the first slash and ends before the question mark (without the host part). Defines where to filter for the http_filter_value. Only supported for HTTP backends.
    """

    ip_subnet: List[str]
    """
    List of IPs or CIDR v4/v6 addresses to filter for from the client side.
    """

    http_filter_option: Optional[str]
    """
    Name of the HTTP header to filter on if `http_header_match` was selected in `http_filter`.
    """


@dataclass
class Frontend:
    enable_http3: bool
    """
    Defines whether to enable HTTP/3 protocol on the frontend.
    """

    certificate_ids: List[str]
    """
    List of SSL/TLS certificate IDs to bind to the frontend.
    """

    lb: Lb
    """
    Load Balancer object the frontend is attached to.
    """

    backend: Backend
    """
    Backend object the frontend is attached to.
    """

    inbound_port: int
    """
    Port the frontend listens on.
    """

    name: str
    """
    Name of the frontend.
    """

    id: str
    """
    Frontend ID.
    """

    timeout_client: Optional[str]
    """
    Maximum allowed inactivity time on the client side.
    """

    certificate: Optional[Certificate]
    """
    Certificate, deprecated in favor of certificate_ids array.
    """

    created_at: Optional[datetime]
    """
    Date on which the frontend was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the frontend was last updated.
    """


@dataclass
class PrivateNetworkDHCPConfig:
    ip_id: Optional[str]


@dataclass
class PrivateNetworkIpamConfig:
    pass


@dataclass
class PrivateNetworkStaticConfig:
    ip_address: Optional[List[str]]
    """
    Array of a local IP address for the Load Balancer on this Private Network.
    """


@dataclass
class RouteMatch:
    sni: Optional[str]

    host_header: Optional[str]


@dataclass
class CreateCertificateRequestCustomCertificate:
    certificate_chain: str
    """
    Full PEM-formatted certificate, consisting of the entire certificate chain including public key, private key, and (optionally) Certificate Authorities.
    """


@dataclass
class CreateCertificateRequestLetsencryptConfig:
    subject_alternative_name: List[str]
    """
    Alternative domain names (all domain names must exist and resolve to your Load Balancer IP address).
    """

    common_name: str
    """
    Main domain name of certificate (this domain must exist and resolve to your Load Balancer IP address).
    """


@dataclass
class BackendServerStats:
    last_health_check_status: BackendServerStatsHealthCheckStatus
    """
    Last health check status (unknown/neutral/failed/passed/condpass).
    """

    server_state: BackendServerStatsServerState
    """
    Server operational state (stopped/starting/running/stopping).
    """

    ip: str
    """
    IPv4 or IPv6 address of the backend server.
    """

    backend_id: str
    """
    Backend ID.
    """

    instance_id: str
    """
    ID of your Load Balancer's underlying Instance.
    """

    server_state_changed_at: Optional[datetime]
    """
    Time since last operational change.
    """


@dataclass
class Acl:
    description: str
    """
    ACL description.
    """

    index: int
    """
    Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
    """

    frontend: Frontend
    """
    ACL is attached to this frontend object.
    """

    action: AclAction
    """
    Action to take when incoming traffic matches an ACL filter.
    """

    match: AclMatch
    """
    ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
    """

    name: str
    """
    ACL name.
    """

    id: str
    """
    ACL ID.
    """

    created_at: Optional[datetime]
    """
    Date on which the ACL was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the ACL was last updated.
    """


@dataclass
class PrivateNetwork:
    status: PrivateNetworkStatus
    """
    Status of Private Network connection.
    """

    private_network_id: str
    """
    Private Network ID.
    """

    ipam_ids: List[str]
    """
    IPAM IDs of the booked IP addresses.
    """

    lb: Lb
    """
    Load Balancer object which is attached to the Private Network.
    """

    created_at: Optional[datetime]
    """
    Date on which the Private Network was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the PN was last updated.
    """

    static_config: Optional[PrivateNetworkStaticConfig]

    dhcp_config: Optional[PrivateNetworkDHCPConfig]

    ipam_config: Optional[PrivateNetworkIpamConfig]


@dataclass
class LbType:
    zone: Zone
    """
    The zone the Load Balancer stock is in.
    """

    description: str
    """
    Load Balancer commercial offer type description.
    """

    stock_status: LbTypeStock
    """
    Current stock status for a given Load Balancer type.
    """

    name: str
    """
    Load Balancer commercial offer type name.
    """

    region: Optional[Region]
    """
    The region the Load Balancer stock is in.
    """


@dataclass
class Route:
    match: RouteMatch
    """
    Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
    """

    backend_id: str
    """
    ID of the target backend.
    """

    frontend_id: str
    """
    ID of the source frontend.
    """

    id: str
    """
    Route ID.
    """

    created_at: Optional[datetime]
    """
    Date on which the route was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the route was last updated.
    """


@dataclass
class AclSpec:
    description: str
    """
    ACL description.
    """

    index: int
    """
    Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
    """

    match: AclMatch
    """
    ACL match filter object. One of `ip_subnet` or `http_filter` and `http_filter_value` are required.
    """

    action: AclAction
    """
    Action to take when incoming traffic matches an ACL filter.
    """

    name: str
    """
    ACL name.
    """


@dataclass
class AddBackendServersRequest:
    backend_id: str
    """
    Backend ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    server_ip: Optional[List[str]]
    """
    List of IP addresses to add to backend servers.
    """


@dataclass
class AttachPrivateNetworkRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    static_config: Optional[PrivateNetworkStaticConfig]

    dhcp_config: Optional[PrivateNetworkDHCPConfig]

    ipam_config: Optional[PrivateNetworkIpamConfig]


@dataclass
class CreateAclRequest:
    """
    Add an ACL to a Load Balancer frontend.
    """

    description: str
    """
    ACL description.
    """

    index: int
    """
    Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
    """

    match: AclMatch
    """
    ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
    """

    action: AclAction
    """
    Action to take when incoming traffic matches an ACL filter.
    """

    frontend_id: str
    """
    Frontend ID to attach the ACL to.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    ACL name.
    """


@dataclass
class CreateBackendRequest:
    forward_port: int
    """
    Port to be used by the backend when forwarding traffic to backend servers.
    """

    health_check: HealthCheck
    """
    Object defining the health check to be carried out by the backend when checking the status and health of backend servers.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for cookie-based sticky sessions.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field.
    """

    on_marked_down_action: Optional[OnMarkedDownAction]
    """
    Action to take when a backend server is marked as down.
    """

    forward_port_algorithm: Optional[ForwardPortAlgorithm]
    """
    Load balancing algorithm to be used when determining which backend server to forward new traffic to.
    """

    forward_protocol: Optional[Protocol]
    """
    Protocol to be used by the backend when forwarding traffic to backend servers.
    """

    server_ip: Optional[List[str]]
    """
    List of backend server IP addresses (IPv4 or IPv6) the backend should forward traffic to.
    """

    name: Optional[str]
    """
    Name for the backend.
    """

    timeout_server: Optional[str]
    """
    Maximum allowed time for a backend server to process a request.
    """

    timeout_connect: Optional[str]
    """
    Maximum allowed time for establishing a connection to a backend server.
    """

    timeout_tunnel: Optional[str]
    """
    Maximum allowed tunnel inactivity time after Websocket is established (takes precedence over client and server timeout).
    """

    sticky_sessions: Optional[StickySessionsType]
    """
    Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie TO stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
    """

    proxy_protocol: Optional[ProxyProtocol]
    """
    Protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. The PROXY protocol must be supported by the backend servers' software.
    """

    failover_host: Optional[str]
    """
    Scaleway S3 bucket website to be served as failover if all backend servers are down, e.g. failover-website.s3-website.fr-par.scw.cloud.
    """

    ssl_bridging: Optional[bool]
    """
    Defines whether to enable SSL bridging between the Load Balancer and backend servers.
    """

    ignore_ssl_server_verify: Optional[bool]
    """
    Defines whether the server certificate verification should be ignored.
    """

    redispatch_attempt_count: Optional[int]
    """
    Whether to use another backend server on each attempt.
    """

    max_retries: Optional[int]
    """
    Number of retries when a backend server connection failed.
    """

    max_connections: Optional[int]
    """
    Maximum number of connections allowed per backend server.
    """

    timeout_queue: Optional[str]
    """
    Maximum time for a request to be left pending in queue when `max_connections` is reached.
    """


@dataclass
class CreateCertificateRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name for the certificate.
    """

    letsencrypt: Optional[CreateCertificateRequestLetsencryptConfig]

    custom_certificate: Optional[CreateCertificateRequestCustomCertificate]


@dataclass
class CreateFrontendRequest:
    enable_http3: bool
    """
    Defines whether to enable HTTP/3 protocol on the frontend.
    """

    backend_id: str
    """
    Backend ID (ID of the backend the frontend should pass traffic to).
    """

    inbound_port: int
    """
    Port the frontend should listen on.
    """

    lb_id: str
    """
    Load Balancer ID (ID of the Load Balancer to attach the frontend to).
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name for the frontend.
    """

    timeout_client: Optional[str]
    """
    Maximum allowed inactivity time on the client side.
    """

    certificate_id: Optional[str]
    """
    Certificate ID, deprecated in favor of certificate_ids array.
    """

    certificate_ids: Optional[List[str]]
    """
    List of SSL/TLS certificate IDs to bind to the frontend.
    """


@dataclass
class CreateIpRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    reverse: Optional[str]
    """
    Reverse DNS (domain name) for the IP address.
    """

    organization_id: Optional[str]

    project_id: Optional[str]


@dataclass
class CreateLbRequest:
    type_: str
    """
    Load Balancer commercial offer type. Use the Load Balancer types endpoint to retrieve a list of available offer types.
    """

    description: str
    """
    Description for the Load Balancer.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name for the Load Balancer.
    """

    ip_id: Optional[str]
    """
    ID of an existing flexible IP address to attach to the Load Balancer.
    """

    assign_flexible_ip: Optional[bool]
    """
    Defines whether to automatically assign a flexible public IP to lb. Default value is `false` (do not assign).
    """

    tags: Optional[List[str]]
    """
    List of tags for the Load Balancer.
    """

    ssl_compatibility_level: Optional[SSLCompatibilityLevel]
    """
    Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and do not need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
    """

    organization_id: Optional[str]

    project_id: Optional[str]


@dataclass
class CreateRouteRequest:
    backend_id: str
    """
    ID of the target backend for the route.
    """

    frontend_id: str
    """
    ID of the source frontend to create the route on.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    match: Optional[RouteMatch]
    """
    Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
    """


@dataclass
class CreateSubscriberRequest:
    """
    Create a new alert subscriber (webhook or email).
    """

    name: str
    """
    Subscriber name.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str]

    project_id: Optional[str]

    email_config: Optional[SubscriberEmailConfig]

    webhook_config: Optional[SubscriberWebhookConfig]


@dataclass
class DeleteAclRequest:
    acl_id: str
    """
    ACL ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteBackendRequest:
    backend_id: str
    """
    ID of the backend to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteCertificateRequest:
    certificate_id: str
    """
    Certificate ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteFrontendRequest:
    frontend_id: str
    """
    ID of the frontend to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteLbRequest:
    release_ip: bool
    """
    Defines whether the Load Balancer's flexible IP should be deleted. Set to true to release the flexible IP, or false to keep it available in your account for future Load Balancers.
    """

    lb_id: str
    """
    ID of the Load Balancer to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteRouteRequest:
    route_id: str
    """
    Route ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteSubscriberRequest:
    subscriber_id: str
    """
    Subscriber ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DetachPrivateNetworkRequest:
    private_network_id: str
    """
    Set your instance private network id.
    """

    lb_id: str
    """
    Load balancer ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetAclRequest:
    acl_id: str
    """
    ACL ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetBackendRequest:
    backend_id: str
    """
    Backend ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetCertificateRequest:
    certificate_id: str
    """
    Certificate ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetFrontendRequest:
    frontend_id: str
    """
    Frontend ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetIpRequest:
    ip_id: str
    """
    IP address ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetLbRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetLbStatsRequest:
    """
    Get Load Balancer stats.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    backend_id: Optional[str]
    """
    ID of the backend.
    """


@dataclass
class GetRouteRequest:
    route_id: str
    """
    Route ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetSubscriberRequest:
    subscriber_id: str
    """
    Subscriber ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class LbStats:
    backend_servers_stats: List[BackendServerStats]
    """
    List of objects containing Load Balancer statistics.
    """


@dataclass
class ListAclResponse:
    total_count: int
    """
    The total number of objects.
    """

    acls: List[Acl]
    """
    List of ACL objects.
    """


@dataclass
class ListAclsRequest:
    frontend_id: str
    """
    Frontend ID (ACLs attached to this frontend will be returned in the response).
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListAclRequestOrderBy]
    """
    Sort order of ACLs in the response.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    The number of ACLs to return.
    """

    name: Optional[str]
    """
    ACL name to filter for.
    """


@dataclass
class ListBackendStatsRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of items to return.
    """

    backend_id: Optional[str]
    """
    ID of the backend.
    """


@dataclass
class ListBackendStatsResponse:
    total_count: int
    """
    The total number of objects.
    """

    backend_servers_stats: List[BackendServerStats]
    """
    List of objects containing backend server statistics.
    """


@dataclass
class ListBackendsRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the backend to filter for.
    """

    order_by: Optional[ListBackendsRequestOrderBy]
    """
    Sort order of backends in the response.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of backends to return.
    """


@dataclass
class ListBackendsResponse:
    total_count: int
    """
    Total count of backend objects, without pagination.
    """

    backends: List[Backend]
    """
    List of backend objects of a given Load Balancer.
    """


@dataclass
class ListCertificatesRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListCertificatesRequestOrderBy]
    """
    Sort order of certificates in the response.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of certificates to return.
    """

    name: Optional[str]
    """
    Certificate name to filter for, only certificates of this name will be returned.
    """


@dataclass
class ListCertificatesResponse:
    total_count: int
    """
    The total number of objects.
    """

    certificates: List[Certificate]
    """
    List of certificate objects.
    """


@dataclass
class ListFrontendsRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the frontend to filter for.
    """

    order_by: Optional[ListFrontendsRequestOrderBy]
    """
    Sort order of frontends in the response.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of frontends to return.
    """


@dataclass
class ListFrontendsResponse:
    total_count: int
    """
    Total count of frontend objects, without pagination.
    """

    frontends: List[Frontend]
    """
    List of frontend objects of a given Load Balancer.
    """


@dataclass
class ListIPsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of IP addresses to return.
    """

    ip_address: Optional[str]
    """
    IP address to filter for.
    """

    organization_id: Optional[str]
    """
    Organization ID to filter for, only Load Balancer IP addresses from this Organization will be returned.
    """

    project_id: Optional[str]
    """
    Project ID to filter for, only Load Balancer IP addresses from this Project will be returned.
    """


@dataclass
class ListIpsResponse:
    total_count: int
    """
    Total count of IP address objects, without pagination.
    """

    ips: List[Ip]
    """
    List of IP address objects.
    """


@dataclass
class ListLbPrivateNetworksRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListPrivateNetworksRequestOrderBy]
    """
    Sort order of Private Network objects in the response.
    """

    page_size: Optional[int]
    """
    Number of objects to return.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """


@dataclass
class ListLbPrivateNetworksResponse:
    total_count: int
    """
    Total number of objects in the response.
    """

    private_network: List[PrivateNetwork]
    """
    List of Private Network objects attached to the Load Balancer.
    """


@dataclass
class ListLbTypesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    The number of items to return.
    """


@dataclass
class ListLbTypesResponse:
    total_count: int
    """
    Total number of Load Balancer offer type objects.
    """

    lb_types: List[LbType]
    """
    List of Load Balancer commercial offer type objects.
    """


@dataclass
class ListLbsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Load Balancer name to filter for.
    """

    order_by: Optional[ListLbsRequestOrderBy]
    """
    Sort order of Load Balancers in the response.
    """

    page_size: Optional[int]
    """
    Number of Load Balancers to return.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    organization_id: Optional[str]
    """
    Organization ID to filter for, only Load Balancers from this Organization will be returned.
    """

    project_id: Optional[str]
    """
    Project ID to filter for, only Load Balancers from this Project will be returned.
    """


@dataclass
class ListLbsResponse:
    total_count: int
    """
    The total number of Load Balancer objects.
    """

    lbs: List[Lb]
    """
    List of Load Balancer objects.
    """


@dataclass
class ListRoutesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListRoutesRequestOrderBy]
    """
    Sort order of routes in the response.
    """

    page_size: Optional[int]
    """
    The number of route objects to return.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    frontend_id: Optional[str]
    """
    Frontend ID to filter for, only Routes from this Frontend will be returned.
    """


@dataclass
class ListRoutesResponse:
    total_count: int
    """
    The total number of route objects.
    """

    routes: List[Route]
    """
    List of route objects.
    """


@dataclass
class ListSubscriberRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListSubscriberRequestOrderBy]
    """
    Sort order of subscribers in the response.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    The number of items to return.
    """

    name: Optional[str]
    """
    Subscriber name to search for.
    """

    organization_id: Optional[str]
    """
    Filter subscribers by Organization ID.
    """

    project_id: Optional[str]
    """
    Filter subscribers by Project ID.
    """


@dataclass
class ListSubscriberResponse:
    total_count: int
    """
    The total number of objects.
    """

    subscribers: List[Subscriber]
    """
    List of subscriber objects.
    """


@dataclass
class MigrateLbRequest:
    type_: str
    """
    Load Balancer type to migrate to (use the List all Load Balancer offer types endpoint to get a list of available offer types).
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ReleaseIpRequest:
    ip_id: str
    """
    IP address ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RemoveBackendServersRequest:
    backend_id: str
    """
    Backend ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    server_ip: Optional[List[str]]
    """
    List of IP addresses to remove from backend servers.
    """


@dataclass
class SetAclsResponse:
    total_count: int
    """
    The total number of ACL objects.
    """

    acls: List[Acl]
    """
    List of ACL objects.
    """


@dataclass
class SetBackendServersRequest:
    backend_id: str
    """
    Backend ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    server_ip: Optional[List[str]]
    """
    List of IP addresses for backend servers. Any other existing backend servers will be removed.
    """


@dataclass
class SubscribeToLbRequest:
    subscriber_id: str
    """
    Subscriber ID.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UnsubscribeFromLbRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UpdateAclRequest:
    index: int
    """
    Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
    """

    match: AclMatch
    """
    ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
    """

    action: AclAction
    """
    Action to take when incoming traffic matches an ACL filter.
    """

    name: str
    """
    ACL name.
    """

    acl_id: str
    """
    ACL ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    description: Optional[str]
    """
    ACL description.
    """


@dataclass
class UpdateBackendRequest:
    forward_port: int
    """
    Port to be used by the backend when forwarding traffic to backend servers.
    """

    name: str
    """
    Backend name.
    """

    backend_id: str
    """
    Backend ID.
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for cookie-based sticky sessions.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    timeout_connect: Optional[str]
    """
    Maximum allowed time for establishing a connection to a backend server.
    """

    on_marked_down_action: Optional[OnMarkedDownAction]
    """
    Action to take when a backend server is marked as down.
    """

    forward_port_algorithm: Optional[ForwardPortAlgorithm]
    """
    Load balancing algorithm to be used when determining which backend server to forward new traffic to.
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field.
    """

    timeout_server: Optional[str]
    """
    Maximum allowed time for a backend server to process a request.
    """

    forward_protocol: Optional[Protocol]
    """
    Protocol to be used by the backend when forwarding traffic to backend servers.
    """

    timeout_tunnel: Optional[str]
    """
    Maximum allowed tunnel inactivity time after Websocket is established (takes precedence over client and server timeout).
    """

    sticky_sessions: Optional[StickySessionsType]
    """
    Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie to stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
    """

    proxy_protocol: Optional[ProxyProtocol]
    """
    Protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. The PROXY protocol must be supported by the backend servers' software.
    """

    failover_host: Optional[str]
    """
    Scaleway S3 bucket website to be served as failover if all backend servers are down, e.g. failover-website.s3-website.fr-par.scw.cloud.
    """

    ssl_bridging: Optional[bool]
    """
    Defines whether to enable SSL bridging between the Load Balancer and backend servers.
    """

    ignore_ssl_server_verify: Optional[bool]
    """
    Defines whether the server certificate verification should be ignored.
    """

    redispatch_attempt_count: Optional[int]
    """
    Whether to use another backend server on each attempt.
    """

    max_retries: Optional[int]
    """
    Number of retries when a backend server connection failed.
    """

    max_connections: Optional[int]
    """
    Maximum number of connections allowed per backend server.
    """

    timeout_queue: Optional[str]
    """
    Maximum time for a request to be left pending in queue when `max_connections` is reached.
    """


@dataclass
class UpdateCertificateRequest:
    name: str
    """
    Certificate name.
    """

    certificate_id: str
    """
    Certificate ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UpdateFrontendRequest:
    enable_http3: bool
    """
    Defines whether to enable HTTP/3 protocol on the frontend.
    """

    backend_id: str
    """
    Backend ID (ID of the backend the frontend should pass traffic to).
    """

    inbound_port: int
    """
    Port the frontend should listen on.
    """

    name: str
    """
    Frontend name.
    """

    frontend_id: str
    """
    Frontend ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    timeout_client: Optional[str]
    """
    Maximum allowed inactivity time on the client side.
    """

    certificate_id: Optional[str]
    """
    Certificate ID, deprecated in favor of certificate_ids array.
    """

    certificate_ids: Optional[List[str]]
    """
    List of SSL/TLS certificate IDs to bind to the frontend.
    """


@dataclass
class UpdateHealthCheckRequest:
    check_send_proxy: bool
    """
    Defines whether proxy protocol should be activated for the health check.
    """

    check_max_retries: int
    """
    Number of consecutive unsuccessful health checks after which the server will be considered dead.
    """

    port: int
    """
    Port to use for the backend server health check.
    """

    backend_id: str
    """
    Backend ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    check_delay: Optional[str]
    """
    Time to wait between two consecutive health checks.
    """

    check_timeout: Optional[str]
    """
    Maximum time a backend server has to reply to the health check.
    """

    transient_check_delay: Optional[str]
    """
    Time to wait between two consecutive health checks when a backend server is in a transient state (going UP or DOWN).
    """

    tcp_config: Optional[HealthCheckTcpConfig]

    mysql_config: Optional[HealthCheckMysqlConfig]

    pgsql_config: Optional[HealthCheckPgsqlConfig]

    ldap_config: Optional[HealthCheckLdapConfig]

    redis_config: Optional[HealthCheckRedisConfig]

    http_config: Optional[HealthCheckHttpConfig]

    https_config: Optional[HealthCheckHttpsConfig]


@dataclass
class UpdateIpRequest:
    ip_id: str
    """
    IP address ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    reverse: Optional[str]
    """
    Reverse DNS (domain name) for the IP address.
    """


@dataclass
class UpdateLbRequest:
    description: str
    """
    Load Balancer description.
    """

    name: str
    """
    Load Balancer name.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    tags: Optional[List[str]]
    """
    List of tags for the Load Balancer.
    """

    ssl_compatibility_level: Optional[SSLCompatibilityLevel]
    """
    Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and don't need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
    """


@dataclass
class UpdateRouteRequest:
    backend_id: str
    """
    ID of the target backend for the route.
    """

    route_id: str
    """
    Route ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    match: Optional[RouteMatch]
    """
    Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
    """


@dataclass
class UpdateSubscriberRequest:
    name: str
    """
    Subscriber name.
    """

    subscriber_id: str
    """
    Subscriber ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    email_config: Optional[SubscriberEmailConfig]

    webhook_config: Optional[SubscriberWebhookConfig]


@dataclass
class ZonedApiAddBackendServersRequest:
    backend_id: str
    """
    Backend ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_ip: Optional[List[str]]
    """
    List of IP addresses to add to backend servers.
    """


@dataclass
class ZonedApiAttachPrivateNetworkRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    static_config: Optional[PrivateNetworkStaticConfig]

    dhcp_config: Optional[PrivateNetworkDHCPConfig]

    ipam_config: Optional[PrivateNetworkIpamConfig]


@dataclass
class ZonedApiCreateAclRequest:
    """
    Add an ACL to a Load Balancer frontend.
    """

    description: str
    """
    ACL description.
    """

    index: int
    """
    Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
    """

    match: AclMatch
    """
    ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
    """

    action: AclAction
    """
    Action to take when incoming traffic matches an ACL filter.
    """

    frontend_id: str
    """
    Frontend ID to attach the ACL to.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    ACL name.
    """


@dataclass
class ZonedApiCreateBackendRequest:
    forward_port: int
    """
    Port to be used by the backend when forwarding traffic to backend servers.
    """

    health_check: HealthCheck
    """
    Object defining the health check to be carried out by the backend when checking the status and health of backend servers.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for cookie-based sticky sessions.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field.
    """

    on_marked_down_action: Optional[OnMarkedDownAction]
    """
    Action to take when a backend server is marked as down.
    """

    forward_port_algorithm: Optional[ForwardPortAlgorithm]
    """
    Load balancing algorithm to be used when determining which backend server to forward new traffic to.
    """

    forward_protocol: Optional[Protocol]
    """
    Protocol to be used by the backend when forwarding traffic to backend servers.
    """

    server_ip: Optional[List[str]]
    """
    List of backend server IP addresses (IPv4 or IPv6) the backend should forward traffic to.
    """

    name: Optional[str]
    """
    Name for the backend.
    """

    timeout_server: Optional[str]
    """
    Maximum allowed time for a backend server to process a request.
    """

    timeout_connect: Optional[str]
    """
    Maximum allowed time for establishing a connection to a backend server.
    """

    timeout_tunnel: Optional[str]
    """
    Maximum allowed tunnel inactivity time after Websocket is established (takes precedence over client and server timeout).
    """

    sticky_sessions: Optional[StickySessionsType]
    """
    Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie TO stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
    """

    proxy_protocol: Optional[ProxyProtocol]
    """
    Protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. The PROXY protocol must be supported by the backend servers' software.
    """

    failover_host: Optional[str]
    """
    Scaleway S3 bucket website to be served as failover if all backend servers are down, e.g. failover-website.s3-website.fr-par.scw.cloud.
    """

    ssl_bridging: Optional[bool]
    """
    Defines whether to enable SSL bridging between the Load Balancer and backend servers.
    """

    ignore_ssl_server_verify: Optional[bool]
    """
    Defines whether the server certificate verification should be ignored.
    """

    redispatch_attempt_count: Optional[int]
    """
    Whether to use another backend server on each attempt.
    """

    max_retries: Optional[int]
    """
    Number of retries when a backend server connection failed.
    """

    max_connections: Optional[int]
    """
    Maximum number of connections allowed per backend server.
    """

    timeout_queue: Optional[str]
    """
    Maximum time for a request to be left pending in queue when `max_connections` is reached.
    """


@dataclass
class ZonedApiCreateCertificateRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name for the certificate.
    """

    letsencrypt: Optional[CreateCertificateRequestLetsencryptConfig]

    custom_certificate: Optional[CreateCertificateRequestCustomCertificate]


@dataclass
class ZonedApiCreateFrontendRequest:
    enable_http3: bool
    """
    Defines whether to enable HTTP/3 protocol on the frontend.
    """

    backend_id: str
    """
    Backend ID (ID of the backend the frontend should pass traffic to).
    """

    inbound_port: int
    """
    Port the frontend should listen on.
    """

    lb_id: str
    """
    Load Balancer ID (ID of the Load Balancer to attach the frontend to).
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name for the frontend.
    """

    timeout_client: Optional[str]
    """
    Maximum allowed inactivity time on the client side.
    """

    certificate_id: Optional[str]
    """
    Certificate ID, deprecated in favor of certificate_ids array.
    """

    certificate_ids: Optional[List[str]]
    """
    List of SSL/TLS certificate IDs to bind to the frontend.
    """


@dataclass
class ZonedApiCreateIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    reverse: Optional[str]
    """
    Reverse DNS (domain name) for the IP address.
    """

    organization_id: Optional[str]

    project_id: Optional[str]


@dataclass
class ZonedApiCreateLbRequest:
    type_: str
    """
    Load Balancer commercial offer type. Use the Load Balancer types endpoint to retrieve a list of available offer types.
    """

    description: str
    """
    Description for the Load Balancer.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name for the Load Balancer.
    """

    ip_id: Optional[str]
    """
    ID of an existing flexible IP address to attach to the Load Balancer.
    """

    assign_flexible_ip: Optional[bool]
    """
    Defines whether to automatically assign a flexible public IP to lb. Default value is `false` (do not assign).
    """

    tags: Optional[List[str]]
    """
    List of tags for the Load Balancer.
    """

    ssl_compatibility_level: Optional[SSLCompatibilityLevel]
    """
    Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and do not need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
    """

    organization_id: Optional[str]

    project_id: Optional[str]


@dataclass
class ZonedApiCreateRouteRequest:
    backend_id: str
    """
    ID of the target backend for the route.
    """

    frontend_id: str
    """
    ID of the source frontend to create the route on.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    match: Optional[RouteMatch]
    """
    Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
    """


@dataclass
class ZonedApiCreateSubscriberRequest:
    """
    Create a new alert subscriber (webhook or email).
    """

    name: str
    """
    Subscriber name.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization_id: Optional[str]

    project_id: Optional[str]

    email_config: Optional[SubscriberEmailConfig]

    webhook_config: Optional[SubscriberWebhookConfig]


@dataclass
class ZonedApiDeleteAclRequest:
    acl_id: str
    """
    ACL ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiDeleteBackendRequest:
    backend_id: str
    """
    ID of the backend to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiDeleteCertificateRequest:
    certificate_id: str
    """
    Certificate ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiDeleteFrontendRequest:
    frontend_id: str
    """
    ID of the frontend to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiDeleteLbRequest:
    release_ip: bool
    """
    Defines whether the Load Balancer's flexible IP should be deleted. Set to true to release the flexible IP, or false to keep it available in your account for future Load Balancers.
    """

    lb_id: str
    """
    ID of the Load Balancer to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiDeleteRouteRequest:
    route_id: str
    """
    Route ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiDeleteSubscriberRequest:
    subscriber_id: str
    """
    Subscriber ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiDetachPrivateNetworkRequest:
    private_network_id: str
    """
    Set your instance private network id.
    """

    lb_id: str
    """
    Load balancer ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiGetAclRequest:
    acl_id: str
    """
    ACL ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiGetBackendRequest:
    backend_id: str
    """
    Backend ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiGetCertificateRequest:
    certificate_id: str
    """
    Certificate ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiGetFrontendRequest:
    frontend_id: str
    """
    Frontend ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiGetIpRequest:
    ip_id: str
    """
    IP address ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiGetLbRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiGetLbStatsRequest:
    """
    Get Load Balancer stats.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    backend_id: Optional[str]
    """
    ID of the backend.
    """


@dataclass
class ZonedApiGetRouteRequest:
    route_id: str
    """
    Route ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiGetSubscriberRequest:
    subscriber_id: str
    """
    Subscriber ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiListAclsRequest:
    frontend_id: str
    """
    Frontend ID (ACLs attached to this frontend will be returned in the response).
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListAclRequestOrderBy]
    """
    Sort order of ACLs in the response.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    The number of ACLs to return.
    """

    name: Optional[str]
    """
    ACL name to filter for.
    """


@dataclass
class ZonedApiListBackendStatsRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of items to return.
    """

    backend_id: Optional[str]
    """
    ID of the backend.
    """


@dataclass
class ZonedApiListBackendsRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the backend to filter for.
    """

    order_by: Optional[ListBackendsRequestOrderBy]
    """
    Sort order of backends in the response.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of backends to return.
    """


@dataclass
class ZonedApiListCertificatesRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListCertificatesRequestOrderBy]
    """
    Sort order of certificates in the response.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of certificates to return.
    """

    name: Optional[str]
    """
    Certificate name to filter for, only certificates of this name will be returned.
    """


@dataclass
class ZonedApiListFrontendsRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the frontend to filter for.
    """

    order_by: Optional[ListFrontendsRequestOrderBy]
    """
    Sort order of frontends in the response.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of frontends to return.
    """


@dataclass
class ZonedApiListIPsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of IP addresses to return.
    """

    ip_address: Optional[str]
    """
    IP address to filter for.
    """

    organization_id: Optional[str]
    """
    Organization ID to filter for, only Load Balancer IP addresses from this Organization will be returned.
    """

    project_id: Optional[str]
    """
    Project ID to filter for, only Load Balancer IP addresses from this Project will be returned.
    """


@dataclass
class ZonedApiListLbPrivateNetworksRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListPrivateNetworksRequestOrderBy]
    """
    Sort order of Private Network objects in the response.
    """

    page_size: Optional[int]
    """
    Number of objects to return.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """


@dataclass
class ZonedApiListLbTypesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    The number of items to return.
    """


@dataclass
class ZonedApiListLbsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Load Balancer name to filter for.
    """

    order_by: Optional[ListLbsRequestOrderBy]
    """
    Sort order of Load Balancers in the response.
    """

    page_size: Optional[int]
    """
    Number of Load Balancers to return.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    organization_id: Optional[str]
    """
    Organization ID to filter for, only Load Balancers from this Organization will be returned.
    """

    project_id: Optional[str]
    """
    Project ID to filter for, only Load Balancers from this Project will be returned.
    """


@dataclass
class ZonedApiListRoutesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListRoutesRequestOrderBy]
    """
    Sort order of routes in the response.
    """

    page_size: Optional[int]
    """
    The number of route objects to return.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    frontend_id: Optional[str]
    """
    Frontend ID to filter for, only Routes from this Frontend will be returned.
    """


@dataclass
class ZonedApiListSubscriberRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListSubscriberRequestOrderBy]
    """
    Sort order of subscribers in the response.
    """

    page: Optional[int]
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    The number of items to return.
    """

    name: Optional[str]
    """
    Subscriber name to search for.
    """

    organization_id: Optional[str]
    """
    Filter subscribers by Organization ID.
    """

    project_id: Optional[str]
    """
    Filter subscribers by Project ID.
    """


@dataclass
class ZonedApiMigrateLbRequest:
    type_: str
    """
    Load Balancer type to migrate to (use the List all Load Balancer offer types endpoint to get a list of available offer types).
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiReleaseIpRequest:
    ip_id: str
    """
    IP address ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiRemoveBackendServersRequest:
    backend_id: str
    """
    Backend ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_ip: Optional[List[str]]
    """
    List of IP addresses to remove from backend servers.
    """


@dataclass
class ZonedApiSetAclsRequest:
    frontend_id: str
    """
    Frontend ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    acls: Optional[List[AclSpec]]
    """
    List of ACLs for this frontend. Any other existing ACLs on this frontend will be removed.
    """


@dataclass
class ZonedApiSetBackendServersRequest:
    backend_id: str
    """
    Backend ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_ip: Optional[List[str]]
    """
    List of IP addresses for backend servers. Any other existing backend servers will be removed.
    """


@dataclass
class ZonedApiSubscribeToLbRequest:
    subscriber_id: str
    """
    Subscriber ID.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiUnsubscribeFromLbRequest:
    lb_id: str
    """
    Load Balancer ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiUpdateAclRequest:
    index: int
    """
    Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
    """

    match: AclMatch
    """
    ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
    """

    action: AclAction
    """
    Action to take when incoming traffic matches an ACL filter.
    """

    name: str
    """
    ACL name.
    """

    acl_id: str
    """
    ACL ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    description: Optional[str]
    """
    ACL description.
    """


@dataclass
class ZonedApiUpdateBackendRequest:
    forward_port: int
    """
    Port to be used by the backend when forwarding traffic to backend servers.
    """

    name: str
    """
    Backend name.
    """

    backend_id: str
    """
    Backend ID.
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for cookie-based sticky sessions.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    timeout_connect: Optional[str]
    """
    Maximum allowed time for establishing a connection to a backend server.
    """

    on_marked_down_action: Optional[OnMarkedDownAction]
    """
    Action to take when a backend server is marked as down.
    """

    forward_port_algorithm: Optional[ForwardPortAlgorithm]
    """
    Load balancing algorithm to be used when determining which backend server to forward new traffic to.
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field.
    """

    timeout_server: Optional[str]
    """
    Maximum allowed time for a backend server to process a request.
    """

    forward_protocol: Optional[Protocol]
    """
    Protocol to be used by the backend when forwarding traffic to backend servers.
    """

    timeout_tunnel: Optional[str]
    """
    Maximum allowed tunnel inactivity time after Websocket is established (takes precedence over client and server timeout).
    """

    sticky_sessions: Optional[StickySessionsType]
    """
    Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie to stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
    """

    proxy_protocol: Optional[ProxyProtocol]
    """
    Protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. The PROXY protocol must be supported by the backend servers' software.
    """

    failover_host: Optional[str]
    """
    Scaleway S3 bucket website to be served as failover if all backend servers are down, e.g. failover-website.s3-website.fr-par.scw.cloud.
    """

    ssl_bridging: Optional[bool]
    """
    Defines whether to enable SSL bridging between the Load Balancer and backend servers.
    """

    ignore_ssl_server_verify: Optional[bool]
    """
    Defines whether the server certificate verification should be ignored.
    """

    redispatch_attempt_count: Optional[int]
    """
    Whether to use another backend server on each attempt.
    """

    max_retries: Optional[int]
    """
    Number of retries when a backend server connection failed.
    """

    max_connections: Optional[int]
    """
    Maximum number of connections allowed per backend server.
    """

    timeout_queue: Optional[str]
    """
    Maximum time for a request to be left pending in queue when `max_connections` is reached.
    """


@dataclass
class ZonedApiUpdateCertificateRequest:
    name: str
    """
    Certificate name.
    """

    certificate_id: str
    """
    Certificate ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZonedApiUpdateFrontendRequest:
    enable_http3: bool
    """
    Defines whether to enable HTTP/3 protocol on the frontend.
    """

    backend_id: str
    """
    Backend ID (ID of the backend the frontend should pass traffic to).
    """

    inbound_port: int
    """
    Port the frontend should listen on.
    """

    name: str
    """
    Frontend name.
    """

    frontend_id: str
    """
    Frontend ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    timeout_client: Optional[str]
    """
    Maximum allowed inactivity time on the client side.
    """

    certificate_id: Optional[str]
    """
    Certificate ID, deprecated in favor of certificate_ids array.
    """

    certificate_ids: Optional[List[str]]
    """
    List of SSL/TLS certificate IDs to bind to the frontend.
    """


@dataclass
class ZonedApiUpdateHealthCheckRequest:
    check_send_proxy: bool
    """
    Defines whether proxy protocol should be activated for the health check.
    """

    check_max_retries: int
    """
    Number of consecutive unsuccessful health checks after which the server will be considered dead.
    """

    port: int
    """
    Port to use for the backend server health check.
    """

    backend_id: str
    """
    Backend ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    check_delay: Optional[str]
    """
    Time to wait between two consecutive health checks.
    """

    check_timeout: Optional[str]
    """
    Maximum time a backend server has to reply to the health check.
    """

    transient_check_delay: Optional[str]
    """
    Time to wait between two consecutive health checks when a backend server is in a transient state (going UP or DOWN).
    """

    tcp_config: Optional[HealthCheckTcpConfig]

    mysql_config: Optional[HealthCheckMysqlConfig]

    pgsql_config: Optional[HealthCheckPgsqlConfig]

    ldap_config: Optional[HealthCheckLdapConfig]

    redis_config: Optional[HealthCheckRedisConfig]

    http_config: Optional[HealthCheckHttpConfig]

    https_config: Optional[HealthCheckHttpsConfig]


@dataclass
class ZonedApiUpdateIpRequest:
    ip_id: str
    """
    IP address ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    reverse: Optional[str]
    """
    Reverse DNS (domain name) for the IP address.
    """


@dataclass
class ZonedApiUpdateLbRequest:
    description: str
    """
    Load Balancer description.
    """

    name: str
    """
    Load Balancer name.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[List[str]]
    """
    List of tags for the Load Balancer.
    """

    ssl_compatibility_level: Optional[SSLCompatibilityLevel]
    """
    Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and don't need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
    """


@dataclass
class ZonedApiUpdateRouteRequest:
    backend_id: str
    """
    ID of the target backend for the route.
    """

    route_id: str
    """
    Route ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    match: Optional[RouteMatch]
    """
    Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
    """


@dataclass
class ZonedApiUpdateSubscriberRequest:
    name: str
    """
    Subscriber name.
    """

    subscriber_id: str
    """
    Subscriber ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    email_config: Optional[SubscriberEmailConfig]

    webhook_config: Optional[SubscriberWebhookConfig]
