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


class AclActionRedirectRedirectType(str, Enum):
    LOCATION = "location"
    SCHEME = "scheme"

    def __str__(self) -> str:
        return str(self.value)


class AclActionType(str, Enum):
    ALLOW = "allow"
    DENY = "deny"
    REDIRECT = "redirect"

    def __str__(self) -> str:
        return str(self.value)


class AclHttpFilter(str, Enum):
    ACL_HTTP_FILTER_NONE = "acl_http_filter_none"
    PATH_BEGIN = "path_begin"
    PATH_END = "path_end"
    REGEX = "regex"
    HTTP_HEADER_MATCH = "http_header_match"

    def __str__(self) -> str:
        return str(self.value)


class BackendServerStatsHealthCheckStatus(str, Enum):
    UNKNOWN = "unknown"
    NEUTRAL = "neutral"
    FAILED = "failed"
    PASSED = "passed"
    CONDPASS = "condpass"

    def __str__(self) -> str:
        return str(self.value)


class BackendServerStatsServerState(str, Enum):
    STOPPED = "stopped"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"

    def __str__(self) -> str:
        return str(self.value)


class CertificateStatus(str, Enum):
    PENDING = "pending"
    READY = "ready"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class CertificateType(str, Enum):
    LETSENCRYT = "letsencryt"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)


class ForwardPortAlgorithm(str, Enum):
    ROUNDROBIN = "roundrobin"
    LEASTCONN = "leastconn"
    FIRST = "first"

    def __str__(self) -> str:
        return str(self.value)


class InstanceStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    PENDING = "pending"
    STOPPED = "stopped"
    ERROR = "error"
    LOCKED = "locked"
    MIGRATING = "migrating"

    def __str__(self) -> str:
        return str(self.value)


class LbStatus(str, Enum):
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


class LbTypeStock(str, Enum):
    UNKNOWN = "unknown"
    LOW_STOCK = "low_stock"
    OUT_OF_STOCK = "out_of_stock"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)


class ListAclRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListBackendsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListCertificatesRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListFrontendsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListLbsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPrivateNetworksRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRoutesRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSubscriberRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class OnMarkedDownAction(str, Enum):
    ON_MARKED_DOWN_ACTION_NONE = "on_marked_down_action_none"
    SHUTDOWN_SESSIONS = "shutdown_sessions"

    def __str__(self) -> str:
        return str(self.value)


class PrivateNetworkStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    PENDING = "pending"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class Protocol(str, Enum):
    TCP = "tcp"
    HTTP = "http"

    def __str__(self) -> str:
        return str(self.value)


class ProxyProtocol(str, Enum):
    """
    PROXY protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. PROXY protocol must be supported by the backend servers' software. For more information on the different protocols available, see the [dedicated documentation](https://www.scaleway.com/en/docs/network/load-balancer/reference-content/configuring-load-balancer/#choosing-a-proxy-protocol).
    Proxy protocol.
    """

    PROXY_PROTOCOL_UNKNOWN = "proxy_protocol_unknown"
    PROXY_PROTOCOL_NONE = "proxy_protocol_none"
    PROXY_PROTOCOL_V1 = "proxy_protocol_v1"
    PROXY_PROTOCOL_V2 = "proxy_protocol_v2"
    PROXY_PROTOCOL_V2_SSL = "proxy_protocol_v2_ssl"
    PROXY_PROTOCOL_V2_SSL_CN = "proxy_protocol_v2_ssl_cn"

    def __str__(self) -> str:
        return str(self.value)


class SSLCompatibilityLevel(str, Enum):
    SSL_COMPATIBILITY_LEVEL_UNKNOWN = "ssl_compatibility_level_unknown"
    SSL_COMPATIBILITY_LEVEL_INTERMEDIATE = "ssl_compatibility_level_intermediate"
    SSL_COMPATIBILITY_LEVEL_MODERN = "ssl_compatibility_level_modern"
    SSL_COMPATIBILITY_LEVEL_OLD = "ssl_compatibility_level_old"

    def __str__(self) -> str:
        return str(self.value)


class StickySessionsType(str, Enum):
    NONE = "none"
    COOKIE = "cookie"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Acl:
    """
    Acl.
    """

    id: str
    """
    ACL ID.
    """

    name: str
    """
    ACL name.
    """

    match: Optional[AclMatch]
    """
    ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
    """

    action: Optional[AclAction]
    """
    Action to take when incoming traffic matches an ACL filter.
    """

    frontend: Optional[Frontend]
    """
    ACL is attached to this frontend object.
    """

    index: int
    """
    Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
    """

    created_at: Optional[datetime]
    """
    Date on which the ACL was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the ACL was last updated.
    """

    description: str
    """
    ACL description.
    """


@dataclass
class AclAction:
    """
    Acl action.
    """

    type_: AclActionType
    """
    Action to take when incoming traffic matches an ACL filter.
    """

    redirect: Optional[AclActionRedirect]
    """
    Redirection parameters when using an ACL with a `redirect` action.
    """


@dataclass
class AclActionRedirect:
    """
    Acl action redirect.
    """

    type_: AclActionRedirectRedirectType
    """
    Redirect type.
    """

    target: str
    """
    Redirect target. For a location redirect, you can use a URL e.g. `https://scaleway.com`. Using a scheme name (e.g. `https`, `http`, `ftp`, `git`) will replace the request's original scheme. This can be useful to implement HTTP to HTTPS redirects. Valid placeholders that can be used in a `location` redirect to preserve parts of the original request in the redirection URL are \{\{ host \}\}, \{\{ query \}\}, \{\{ path \}\} and \{\{ scheme \}\}.
    """

    code: Optional[int]
    """
    HTTP redirect code to use. Valid values are 301, 302, 303, 307 and 308. Default value is 302.
    """


@dataclass
class AclMatch:
    """
    Acl match.
    """

    ip_subnet: List[str]
    """
    List of IPs or CIDR v4/v6 addresses to filter for from the client side.
    """

    http_filter: AclHttpFilter
    """
    Type of HTTP filter to match. Extracts the request's URL path, which starts at the first slash and ends before the question mark (without the host part). Defines where to filter for the http_filter_value. Only supported for HTTP backends.
    """

    http_filter_value: List[str]
    """
    List of values to filter for.
    """

    http_filter_option: Optional[str]
    """
    Name of the HTTP header to filter on if `http_header_match` was selected in `http_filter`.
    """

    invert: bool
    """
    Defines whether to invert the match condition. If set to `true`, the ACL carries out its action when the condition DOES NOT match.
    """


@dataclass
class AclSpec:
    """
    Acl spec.
    """

    name: str
    """
    ACL name.
    """

    action: AclAction
    """
    Action to take when incoming traffic matches an ACL filter.
    """

    match: Optional[AclMatch]
    """
    ACL match filter object. One of `ip_subnet` or `http_filter` and `http_filter_value` are required.
    """

    index: int
    """
    Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
    """

    description: str
    """
    ACL description.
    """


@dataclass
class Backend:
    """
    Backend.
    """

    id: str
    """
    Backend ID.
    """

    name: str
    """
    Name of the backend.
    """

    forward_protocol: Protocol
    """
    Protocol used by the backend when forwarding traffic to backend servers.
    """

    forward_port: int
    """
    Port used by the backend when forwarding traffic to backend servers.
    """

    forward_port_algorithm: ForwardPortAlgorithm
    """
    Load balancing algorithm to use when determining which backend server to forward new traffic to.
    """

    sticky_sessions: StickySessionsType
    """
    Defines whether sticky sessions (binding a particular session to a particular backend server) are activated and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie to stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for cookie-based sticky sessions.
    """

    health_check: Optional[HealthCheck]
    """
    Object defining the health check to be carried out by the backend when checking the status and health of backend servers.
    """

    pool: List[str]
    """
    List of IP addresses of backend servers attached to this backend.
    """

    lb: Optional[Lb]
    """
    Load Balancer the backend is attached to.
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field.
    :deprecated
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

    on_marked_down_action: OnMarkedDownAction
    """
    Action to take when a backend server is marked as down.
    """

    proxy_protocol: ProxyProtocol
    """
    Protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. The PROXY protocol must be supported by the backend servers' software.
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
class BackendServerStats:
    """
    Backend server stats.
    """

    instance_id: str
    """
    ID of your Load Balancer's underlying Instance.
    """

    backend_id: str
    """
    Backend ID.
    """

    ip: str
    """
    IPv4 or IPv6 address of the backend server.
    """

    server_state: BackendServerStatsServerState
    """
    Server operational state (stopped/starting/running/stopping).
    """

    server_state_changed_at: Optional[datetime]
    """
    Time since last operational change.
    """

    last_health_check_status: BackendServerStatsHealthCheckStatus
    """
    Last health check status (unknown/neutral/failed/passed/condpass).
    """


@dataclass
class Certificate:
    """
    Certificate.
    """

    type_: CertificateType
    """
    Certificate type (Let's Encrypt or custom).
    """

    id: str
    """
    Certificate ID.
    """

    common_name: str
    """
    Main domain name of certificate.
    """

    subject_alternative_name: List[str]
    """
    Alternative domain names.
    """

    fingerprint: str
    """
    Identifier (SHA-1) of the certificate.
    """

    not_valid_before: Optional[datetime]
    """
    Lower validity bound.
    """

    not_valid_after: Optional[datetime]
    """
    Upper validity bound.
    """

    status: CertificateStatus
    """
    Certificate status.
    """

    lb: Optional[Lb]
    """
    Load Balancer object the certificate is attached to.
    """

    name: str
    """
    Certificate name.
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
class CreateCertificateRequestCustomCertificate:
    """
    Create certificate request. custom certificate.
    """

    certificate_chain: str
    """
    Full PEM-formatted certificate, consisting of the entire certificate chain including public key, private key, and (optionally) Certificate Authorities.
    """


@dataclass
class CreateCertificateRequestLetsencryptConfig:
    """
    Create certificate request. letsencrypt config.
    """

    common_name: str
    """
    Main domain name of certificate (this domain must exist and resolve to your Load Balancer IP address).
    """

    subject_alternative_name: List[str]
    """
    Alternative domain names (all domain names must exist and resolve to your Load Balancer IP address).
    """


@dataclass
class Frontend:
    """
    Frontend.
    """

    id: str
    """
    Frontend ID.
    """

    name: str
    """
    Name of the frontend.
    """

    inbound_port: int
    """
    Port the frontend listens on.
    """

    backend: Optional[Backend]
    """
    Backend object the frontend is attached to.
    """

    lb: Optional[Lb]
    """
    Load Balancer object the frontend is attached to.
    """

    timeout_client: Optional[str]
    """
    Maximum allowed inactivity time on the client side.
    """

    certificate: Optional[Certificate]
    """
    Certificate, deprecated in favor of certificate_ids array.
    :deprecated
    """

    certificate_ids: List[str]
    """
    List of SSL/TLS certificate IDs to bind to the frontend.
    """

    created_at: Optional[datetime]
    """
    Date on which the frontend was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the frontend was last updated.
    """

    enable_http3: bool
    """
    Defines whether to enable HTTP/3 protocol on the frontend.
    """


@dataclass
class HealthCheck:
    """
    Health check.
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

    check_max_retries: int
    """
    Number of consecutive unsuccessful health checks after which the server will be considered dead.
    """

    tcp_config: Optional[HealthCheckTcpConfig]
    """
    Object to configure a basic TCP health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    mysql_config: Optional[HealthCheckMysqlConfig]
    """
    Object to configure a MySQL health check. The check requires MySQL >=3.22, for older versions, use a TCP health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    pgsql_config: Optional[HealthCheckPgsqlConfig]
    """
    Object to configure a PostgreSQL health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    ldap_config: Optional[HealthCheckLdapConfig]
    """
    Object to configure an LDAP health check. The response is analyzed to find the LDAPv3 response message.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    redis_config: Optional[HealthCheckRedisConfig]
    """
    Object to configure a Redis health check. The response is analyzed to find the +PONG response message.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    http_config: Optional[HealthCheckHttpConfig]
    """
    Object to configure an HTTP health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    https_config: Optional[HealthCheckHttpsConfig]
    """
    Object to configure an HTTPS health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    check_send_proxy: bool
    """
    Defines whether proxy protocol should be activated for the health check.
    """

    transient_check_delay: Optional[str]
    """
    Time to wait between two consecutive health checks when a backend server is in a transient state (going UP or DOWN).
    """


@dataclass
class HealthCheckHttpConfig:
    """
    Health check. http config.
    """

    uri: str
    """
    HTTP URI used for the health check.
    The HTTP URI to use when performing a health check on backend servers.
    """

    method: str
    """
    HTTP method used for the health check.
    The HTTP method used when performing a health check on backend servers.
    """

    code: Optional[int]
    """
    HTTP response code expected for a successful health check.
    The HTTP response code that should be returned for a health check to be considered successful.
    """

    host_header: str
    """
    HTTP host header used for the health check.
    The HTTP host header used when performing a health check on backend servers.
    """


@dataclass
class HealthCheckHttpsConfig:
    """
    Health check. https config.
    """

    uri: str
    """
    HTTP URI used for the health check.
    The HTTP URI to use when performing a health check on backend servers.
    """

    method: str
    """
    HTTP method used for the health check.
    The HTTP method used when performing a health check on backend servers.
    """

    code: Optional[int]
    """
    HTTP response code expected for a successful health check.
    The HTTP response code that should be returned for a health check to be considered successful.
    """

    host_header: str
    """
    HTTP host header used for the health check.
    The HTTP host header used when performing a health check on backend servers.
    """

    sni: str
    """
    SNI used for SSL health checks.
    The SNI value used when performing a health check on backend servers over SSL.
    """


@dataclass
class HealthCheckLdapConfig:
    pass


@dataclass
class HealthCheckMysqlConfig:
    """
    Health check. mysql config.
    """

    user: str
    """
    MySQL user to use for the health check.
    """


@dataclass
class HealthCheckPgsqlConfig:
    """
    Health check. pgsql config.
    """

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
    """
    Instance.
    """

    id: str
    """
    Underlying Instance ID.
    """

    status: InstanceStatus
    """
    Instance status.
    """

    ip_address: str
    """
    Instance IP address.
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
    :deprecated
    """

    zone: Zone
    """
    The zone the Instance is in.
    """


@dataclass
class Ip:
    """
    Ip.
    """

    id: str
    """
    IP address ID.
    """

    ip_address: str
    """
    IP address.
    """

    organization_id: str
    """
    Organization ID of the Scaleway Organization the IP address is in.
    """

    project_id: str
    """
    Project ID of the Scaleway Project the IP address is in.
    """

    lb_id: Optional[str]
    """
    Load Balancer ID.
    """

    reverse: str
    """
    Reverse DNS (domain name) of the IP address.
    """

    region: Optional[Region]
    """
    The region the IP address is in.
    :deprecated
    """

    zone: Zone
    """
    The zone the IP address is in.
    """


@dataclass
class Lb:
    """
    Lb.
    """

    id: str
    """
    Underlying Instance ID.
    """

    name: str
    """
    Load Balancer name.
    """

    description: str
    """
    Load Balancer description.
    """

    status: LbStatus
    """
    Load Balancer status.
    """

    instances: List[Instance]
    """
    List of underlying Instances.
    """

    organization_id: str
    """
    Scaleway Organization ID.
    """

    project_id: str
    """
    Scaleway Project ID.
    """

    ip: List[Ip]
    """
    List of IP addresses attached to the Load Balancer.
    """

    tags: List[str]
    """
    Load Balancer tags.
    """

    frontend_count: int
    """
    Number of frontends the Load Balancer has.
    """

    backend_count: int
    """
    Number of backends the Load Balancer has.
    """

    type_: str
    """
    Load Balancer offer type.
    """

    subscriber: Optional[Subscriber]
    """
    Subscriber information.
    """

    ssl_compatibility_level: SSLCompatibilityLevel
    """
    Determines the minimal SSL version which needs to be supported on client side.
    """

    created_at: Optional[datetime]
    """
    Date on which the Load Balancer was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the Load Balancer was last updated.
    """

    private_network_count: int
    """
    Number of Private Networks attached to the Load Balancer.
    """

    route_count: int
    """
    Number of routes configured on the Load Balancer.
    """

    region: Optional[Region]
    """
    The region the Load Balancer is in.
    :deprecated
    """

    zone: Zone
    """
    The zone the Load Balancer is in.
    """


@dataclass
class LbStats:
    """
    Lb stats.
    """

    backend_servers_stats: List[BackendServerStats]
    """
    List of objects containing Load Balancer statistics.
    """


@dataclass
class LbType:
    """
    Lb type.
    """

    name: str
    """
    Load Balancer commercial offer type name.
    """

    stock_status: LbTypeStock
    """
    Current stock status for a given Load Balancer type.
    """

    description: str
    """
    Load Balancer commercial offer type description.
    """

    region: Optional[Region]
    """
    The region the Load Balancer stock is in.
    :deprecated
    """

    zone: Zone
    """
    The zone the Load Balancer stock is in.
    """


@dataclass
class ListAclResponse:
    """
    List acl response.
    """

    acls: List[Acl]
    """
    List of ACL objects.
    """

    total_count: int
    """
    The total number of objects.
    """


@dataclass
class ListBackendStatsResponse:
    """
    List backend stats response.
    """

    backend_servers_stats: List[BackendServerStats]
    """
    List of objects containing backend server statistics.
    """

    total_count: int
    """
    The total number of objects.
    """


@dataclass
class ListBackendsResponse:
    """
    List backends response.
    """

    backends: List[Backend]
    """
    List of backend objects of a given Load Balancer.
    """

    total_count: int
    """
    Total count of backend objects, without pagination.
    """


@dataclass
class ListCertificatesResponse:
    """
    List certificates response.
    """

    certificates: List[Certificate]
    """
    List of certificate objects.
    """

    total_count: int
    """
    The total number of objects.
    """


@dataclass
class ListFrontendsResponse:
    """
    List frontends response.
    """

    frontends: List[Frontend]
    """
    List of frontend objects of a given Load Balancer.
    """

    total_count: int
    """
    Total count of frontend objects, without pagination.
    """


@dataclass
class ListIpsResponse:
    """
    List ips response.
    """

    ips: List[Ip]
    """
    List of IP address objects.
    """

    total_count: int
    """
    Total count of IP address objects, without pagination.
    """


@dataclass
class ListLbPrivateNetworksResponse:
    """
    List lb private networks response.
    """

    private_network: List[PrivateNetwork]
    """
    List of Private Network objects attached to the Load Balancer.
    """

    total_count: int
    """
    Total number of objects in the response.
    """


@dataclass
class ListLbTypesResponse:
    """
    List lb types response.
    """

    lb_types: List[LbType]
    """
    List of Load Balancer commercial offer type objects.
    """

    total_count: int
    """
    Total number of Load Balancer offer type objects.
    """


@dataclass
class ListLbsResponse:
    """
    List lbs response.
    """

    lbs: List[Lb]
    """
    List of Load Balancer objects.
    """

    total_count: int
    """
    The total number of Load Balancer objects.
    """


@dataclass
class ListRoutesResponse:
    """
    List routes response.
    """

    routes: List[Route]
    """
    List of route objects.
    """

    total_count: int
    """
    The total number of route objects.
    """


@dataclass
class ListSubscriberResponse:
    """
    List subscriber response.
    """

    subscribers: List[Subscriber]
    """
    List of subscriber objects.
    """

    total_count: int
    """
    The total number of objects.
    """


@dataclass
class PrivateNetwork:
    """
    Private network.
    """

    lb: Optional[Lb]
    """
    Load Balancer object which is attached to the Private Network.
    """

    static_config: Optional[PrivateNetworkStaticConfig]
    """
    Object containing an array of a local IP address for the Load Balancer on this Private Network.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
    """

    dhcp_config: Optional[PrivateNetworkDHCPConfig]
    """
    Defines whether to let DHCP assign IP addresses.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
    """

    ipam_config: Optional[PrivateNetworkIpamConfig]
    """
    For internal use only.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
    """

    private_network_id: str
    """
    Private Network ID.
    """

    status: PrivateNetworkStatus
    """
    Status of Private Network connection.
    """

    created_at: Optional[datetime]
    """
    Date on which the Private Network was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the PN was last updated.
    """


@dataclass
class PrivateNetworkDHCPConfig:
    pass


@dataclass
class PrivateNetworkIpamConfig:
    pass


@dataclass
class PrivateNetworkStaticConfig:
    """
    Private network. static config.
    """

    ip_address: List[str]
    """
    Array of a local IP address for the Load Balancer on this Private Network.
    """


@dataclass
class Route:
    """
    Route.
    """

    id: str
    """
    Route ID.
    """

    frontend_id: str
    """
    ID of the source frontend.
    """

    backend_id: str
    """
    ID of the target backend.
    """

    match: Optional[RouteMatch]
    """
    Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
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
class RouteMatch:
    """
    Route. match.
    """

    sni: Optional[str]
    """
    Server Name Indication (SNI) value to match.
    Value to match in the Server Name Indication TLS extension (SNI) field from an incoming connection made via an SSL/TLS transport layer. This field should be set for routes on TCP Load Balancers.
    
    One-of ('match_type'): at most one of 'sni', 'host_header' could be set.
    """

    host_header: Optional[str]
    """
    HTTP host header to match.
    Value to match in the HTTP Host request header from an incoming connection. This field should be set for routes on HTTP Load Balancers.
    
    One-of ('match_type'): at most one of 'sni', 'host_header' could be set.
    """


@dataclass
class SetAclsResponse:
    """
    Set acls response.
    """

    acls: List[Acl]
    """
    List of ACL objects.
    """

    total_count: int
    """
    The total number of ACL objects.
    """


@dataclass
class Subscriber:
    """
    Subscriber.
    """

    id: str
    """
    Subscriber ID.
    """

    name: str
    """
    Subscriber name.
    """

    email_config: Optional[SubscriberEmailConfig]
    """
    Email address of subscriber.
    
    One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
    """

    webhook_config: Optional[SubscriberWebhookConfig]
    """
    Webhook URI of subscriber.
    
    One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
    """


@dataclass
class SubscriberEmailConfig:
    """
    Subscriber. email config.
    """

    email: str
    """
    Email address to send alerts to.
    """


@dataclass
class SubscriberWebhookConfig:
    """
    Webhook alert of subscriber.
    Subscriber. webhook config.
    """

    uri: str
    """
    URI to receive POST requests.
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
class CreateLbRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str]
    """
    Scaleway Organization to create the Load Balancer in.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Scaleway Project to create the Load Balancer in.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """

    name: Optional[str]
    """
    Name for the Load Balancer.
    """

    description: str
    """
    Description for the Load Balancer.
    """

    ip_id: Optional[str]
    """
    ID of an existing flexible IP address to attach to the Load Balancer.
    :deprecated
    """

    assign_flexible_ip: Optional[bool]
    """
    Defines whether to automatically assign a flexible public IP to lb. Default value is `false` (do not assign).
    """

    tags: Optional[List[str]]
    """
    List of tags for the Load Balancer.
    """

    type_: str
    """
    Load Balancer commercial offer type. Use the Load Balancer types endpoint to retrieve a list of available offer types.
    """

    ssl_compatibility_level: SSLCompatibilityLevel
    """
    Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and do not need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
    """


@dataclass
class GetLbRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """


@dataclass
class UpdateLbRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    name: str
    """
    Load Balancer name.
    """

    description: str
    """
    Load Balancer description.
    """

    tags: Optional[List[str]]
    """
    List of tags for the Load Balancer.
    """

    ssl_compatibility_level: SSLCompatibilityLevel
    """
    Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and don't need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
    """


@dataclass
class DeleteLbRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    ID of the Load Balancer to delete.
    """

    release_ip: bool
    """
    Defines whether the Load Balancer's flexible IP should be deleted. Set to true to release the flexible IP, or false to keep it available in your account for future Load Balancers.
    """


@dataclass
class MigrateLbRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    type_: str
    """
    Load Balancer type to migrate to (use the List all Load Balancer offer types endpoint to get a list of available offer types).
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
class CreateIpRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str]
    """
    Organization ID of the Organization where the IP address should be created.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Project ID of the Project where the IP address should be created.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """

    reverse: Optional[str]
    """
    Reverse DNS (domain name) for the IP address.
    """


@dataclass
class GetIpRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    ip_id: str
    """
    IP address ID.
    """


@dataclass
class ReleaseIpRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    ip_id: str
    """
    IP address ID.
    """


@dataclass
class UpdateIpRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    ip_id: str
    """
    IP address ID.
    """

    reverse: Optional[str]
    """
    Reverse DNS (domain name) for the IP address.
    """


@dataclass
class ListBackendsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
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
class CreateBackendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    name: Optional[str]
    """
    Name for the backend.
    """

    forward_protocol: Optional[Protocol]
    """
    Protocol to be used by the backend when forwarding traffic to backend servers.
    """

    forward_port: int
    """
    Port to be used by the backend when forwarding traffic to backend servers.
    """

    forward_port_algorithm: Optional[ForwardPortAlgorithm]
    """
    Load balancing algorithm to be used when determining which backend server to forward new traffic to.
    """

    sticky_sessions: Optional[StickySessionsType]
    """
    Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie TO stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for cookie-based sticky sessions.
    """

    health_check: HealthCheck
    """
    Object defining the health check to be carried out by the backend when checking the status and health of backend servers.
    """

    server_ip: List[str]
    """
    List of backend server IP addresses (IPv4 or IPv6) the backend should forward traffic to.
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field.
    :deprecated
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

    on_marked_down_action: OnMarkedDownAction
    """
    Action to take when a backend server is marked as down.
    """

    proxy_protocol: ProxyProtocol
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
class GetBackendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    backend_id: str
    """
    Backend ID.
    """


@dataclass
class UpdateBackendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    backend_id: str
    """
    Backend ID.
    """

    name: str
    """
    Backend name.
    """

    forward_protocol: Optional[Protocol]
    """
    Protocol to be used by the backend when forwarding traffic to backend servers.
    """

    forward_port: int
    """
    Port to be used by the backend when forwarding traffic to backend servers.
    """

    forward_port_algorithm: Optional[ForwardPortAlgorithm]
    """
    Load balancing algorithm to be used when determining which backend server to forward new traffic to.
    """

    sticky_sessions: Optional[StickySessionsType]
    """
    Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie to stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for cookie-based sticky sessions.
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field.
    :deprecated
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

    on_marked_down_action: OnMarkedDownAction
    """
    Action to take when a backend server is marked as down.
    """

    proxy_protocol: ProxyProtocol
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
class DeleteBackendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    backend_id: str
    """
    ID of the backend to delete.
    """


@dataclass
class AddBackendServersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    backend_id: str
    """
    Backend ID.
    """

    server_ip: List[str]
    """
    List of IP addresses to add to backend servers.
    """


@dataclass
class RemoveBackendServersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    backend_id: str
    """
    Backend ID.
    """

    server_ip: List[str]
    """
    List of IP addresses to remove from backend servers.
    """


@dataclass
class SetBackendServersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    backend_id: str
    """
    Backend ID.
    """

    server_ip: List[str]
    """
    List of IP addresses for backend servers. Any other existing backend servers will be removed.
    """


@dataclass
class UpdateHealthCheckRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    backend_id: str
    """
    Backend ID.
    """

    port: int
    """
    Port to use for the backend server health check.
    """

    check_delay: str
    """
    Time to wait between two consecutive health checks.
    """

    check_timeout: str
    """
    Maximum time a backend server has to reply to the health check.
    """

    check_max_retries: int
    """
    Number of consecutive unsuccessful health checks after which the server will be considered dead.
    """

    check_send_proxy: bool
    """
    Defines whether proxy protocol should be activated for the health check.
    """

    tcp_config: Optional[HealthCheckTcpConfig]
    """
    Object to configure a basic TCP health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    mysql_config: Optional[HealthCheckMysqlConfig]
    """
    Object to configure a MySQL health check. The check requires MySQL >=3.22, for older versions, use a TCP health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    pgsql_config: Optional[HealthCheckPgsqlConfig]
    """
    Object to configure a PostgreSQL health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    ldap_config: Optional[HealthCheckLdapConfig]
    """
    Object to configure an LDAP health check. The response is analyzed to find the LDAPv3 response message.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    redis_config: Optional[HealthCheckRedisConfig]
    """
    Object to configure a Redis health check. The response is analyzed to find the +PONG response message.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    http_config: Optional[HealthCheckHttpConfig]
    """
    Object to configure an HTTP health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    https_config: Optional[HealthCheckHttpsConfig]
    """
    Object to configure an HTTPS health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    transient_check_delay: Optional[str]
    """
    Time to wait between two consecutive health checks when a backend server is in a transient state (going UP or DOWN).
    """


@dataclass
class ListFrontendsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
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
class CreateFrontendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID (ID of the Load Balancer to attach the frontend to).
    """

    name: Optional[str]
    """
    Name for the frontend.
    """

    inbound_port: int
    """
    Port the frontend should listen on.
    """

    backend_id: str
    """
    Backend ID (ID of the backend the frontend should pass traffic to).
    """

    timeout_client: Optional[str]
    """
    Maximum allowed inactivity time on the client side.
    """

    certificate_id: Optional[str]
    """
    Certificate ID, deprecated in favor of certificate_ids array.
    :deprecated
    """

    certificate_ids: Optional[List[str]]
    """
    List of SSL/TLS certificate IDs to bind to the frontend.
    """

    enable_http3: bool
    """
    Defines whether to enable HTTP/3 protocol on the frontend.
    """


@dataclass
class GetFrontendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    frontend_id: str
    """
    Frontend ID.
    """


@dataclass
class UpdateFrontendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    frontend_id: str
    """
    Frontend ID.
    """

    name: str
    """
    Frontend name.
    """

    inbound_port: int
    """
    Port the frontend should listen on.
    """

    backend_id: str
    """
    Backend ID (ID of the backend the frontend should pass traffic to).
    """

    timeout_client: Optional[str]
    """
    Maximum allowed inactivity time on the client side.
    """

    certificate_id: Optional[str]
    """
    Certificate ID, deprecated in favor of certificate_ids array.
    :deprecated
    """

    certificate_ids: Optional[List[str]]
    """
    List of SSL/TLS certificate IDs to bind to the frontend.
    """

    enable_http3: bool
    """
    Defines whether to enable HTTP/3 protocol on the frontend.
    """


@dataclass
class DeleteFrontendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    frontend_id: str
    """
    ID of the frontend to delete.
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
class CreateRouteRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    frontend_id: str
    """
    ID of the source frontend to create the route on.
    """

    backend_id: str
    """
    ID of the target backend for the route.
    """

    match: Optional[RouteMatch]
    """
    Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
    """


@dataclass
class GetRouteRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    route_id: str
    """
    Route ID.
    """


@dataclass
class UpdateRouteRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    route_id: str
    """
    Route ID.
    """

    backend_id: str
    """
    ID of the target backend for the route.
    """

    match: Optional[RouteMatch]
    """
    Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
    """


@dataclass
class DeleteRouteRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    route_id: str
    """
    Route ID.
    """


@dataclass
class GetLbStatsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    backend_id: Optional[str]
    """
    ID of the backend.
    """


@dataclass
class ListBackendStatsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
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
class ListAclsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    frontend_id: str
    """
    Frontend ID (ACLs attached to this frontend will be returned in the response).
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
class CreateAclRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    frontend_id: str
    """
    Frontend ID to attach the ACL to.
    """

    name: Optional[str]
    """
    ACL name.
    """

    action: AclAction
    """
    Action to take when incoming traffic matches an ACL filter.
    """

    match: Optional[AclMatch]
    """
    ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
    """

    index: int
    """
    Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
    """

    description: str
    """
    ACL description.
    """


@dataclass
class GetAclRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    acl_id: str
    """
    ACL ID.
    """


@dataclass
class UpdateAclRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    acl_id: str
    """
    ACL ID.
    """

    name: str
    """
    ACL name.
    """

    action: AclAction
    """
    Action to take when incoming traffic matches an ACL filter.
    """

    match: Optional[AclMatch]
    """
    ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
    """

    index: int
    """
    Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
    """

    description: Optional[str]
    """
    ACL description.
    """


@dataclass
class DeleteAclRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    acl_id: str
    """
    ACL ID.
    """


@dataclass
class CreateCertificateRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    name: Optional[str]
    """
    Name for the certificate.
    """

    letsencrypt: Optional[CreateCertificateRequestLetsencryptConfig]
    """
    Object to define a new Let's Encrypt certificate to be generated.
    
    One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
    """

    custom_certificate: Optional[CreateCertificateRequestCustomCertificate]
    """
    Object to define an existing custom certificate to be imported.
    
    One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
    """


@dataclass
class ListCertificatesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
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
class GetCertificateRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    certificate_id: str
    """
    Certificate ID.
    """


@dataclass
class UpdateCertificateRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    certificate_id: str
    """
    Certificate ID.
    """

    name: str
    """
    Certificate name.
    """


@dataclass
class DeleteCertificateRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    certificate_id: str
    """
    Certificate ID.
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
class CreateSubscriberRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: str
    """
    Subscriber name.
    """

    email_config: Optional[SubscriberEmailConfig]
    """
    Email address configuration.
    
    One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
    """

    webhook_config: Optional[SubscriberWebhookConfig]
    """
    WebHook URI configuration.
    
    One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
    """

    organization_id: Optional[str]
    """
    Organization ID to create the subscriber in.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Project ID to create the subscriber in.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """


@dataclass
class GetSubscriberRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    subscriber_id: str
    """
    Subscriber ID.
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

    name: str
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
class UpdateSubscriberRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    subscriber_id: str
    """
    Subscriber ID.
    """

    name: str
    """
    Subscriber name.
    """

    email_config: Optional[SubscriberEmailConfig]
    """
    Email address configuration.
    
    One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
    """

    webhook_config: Optional[SubscriberWebhookConfig]
    """
    Webhook URI configuration.
    
    One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
    """


@dataclass
class DeleteSubscriberRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    subscriber_id: str
    """
    Subscriber ID.
    """


@dataclass
class SubscribeToLbRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    subscriber_id: str
    """
    Subscriber ID.
    """


@dataclass
class UnsubscribeFromLbRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """


@dataclass
class ListLbPrivateNetworksRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
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
class AttachPrivateNetworkRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    private_network_id: str
    """
    Private Network ID.
    """

    static_config: Optional[PrivateNetworkStaticConfig]
    """
    Object containing an array of a local IP address for the Load Balancer on this Private Network.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
    """

    dhcp_config: Optional[PrivateNetworkDHCPConfig]
    """
    Defines whether to let DHCP assign IP addresses.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
    """

    ipam_config: Optional[PrivateNetworkIpamConfig]
    """
    For internal use only.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
    """


@dataclass
class DetachPrivateNetworkRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    lb_id: str
    """
    Load balancer ID.
    """

    private_network_id: str
    """
    Set your instance private network id.
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
class ZonedApiCreateLbRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization_id: Optional[str]
    """
    Scaleway Organization to create the Load Balancer in.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Scaleway Project to create the Load Balancer in.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """

    name: Optional[str]
    """
    Name for the Load Balancer.
    """

    description: str
    """
    Description for the Load Balancer.
    """

    ip_id: Optional[str]
    """
    ID of an existing flexible IP address to attach to the Load Balancer.
    :deprecated
    """

    assign_flexible_ip: Optional[bool]
    """
    Defines whether to automatically assign a flexible public IP to lb. Default value is `false` (do not assign).
    """

    tags: Optional[List[str]]
    """
    List of tags for the Load Balancer.
    """

    type_: str
    """
    Load Balancer commercial offer type. Use the Load Balancer types endpoint to retrieve a list of available offer types.
    """

    ssl_compatibility_level: SSLCompatibilityLevel
    """
    Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and do not need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
    """


@dataclass
class ZonedApiGetLbRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """


@dataclass
class ZonedApiUpdateLbRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    name: str
    """
    Load Balancer name.
    """

    description: str
    """
    Load Balancer description.
    """

    tags: Optional[List[str]]
    """
    List of tags for the Load Balancer.
    """

    ssl_compatibility_level: SSLCompatibilityLevel
    """
    Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and don't need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
    """


@dataclass
class ZonedApiDeleteLbRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    ID of the Load Balancer to delete.
    """

    release_ip: bool
    """
    Defines whether the Load Balancer's flexible IP should be deleted. Set to true to release the flexible IP, or false to keep it available in your account for future Load Balancers.
    """


@dataclass
class ZonedApiMigrateLbRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    type_: str
    """
    Load Balancer type to migrate to (use the List all Load Balancer offer types endpoint to get a list of available offer types).
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
class ZonedApiCreateIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization_id: Optional[str]
    """
    Organization ID of the Organization where the IP address should be created.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Project ID of the Project where the IP address should be created.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """

    reverse: Optional[str]
    """
    Reverse DNS (domain name) for the IP address.
    """


@dataclass
class ZonedApiGetIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    ip_id: str
    """
    IP address ID.
    """


@dataclass
class ZonedApiReleaseIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    ip_id: str
    """
    IP address ID.
    """


@dataclass
class ZonedApiUpdateIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    ip_id: str
    """
    IP address ID.
    """

    reverse: Optional[str]
    """
    Reverse DNS (domain name) for the IP address.
    """


@dataclass
class ZonedApiListBackendsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
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
class ZonedApiCreateBackendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    name: Optional[str]
    """
    Name for the backend.
    """

    forward_protocol: Optional[Protocol]
    """
    Protocol to be used by the backend when forwarding traffic to backend servers.
    """

    forward_port: int
    """
    Port to be used by the backend when forwarding traffic to backend servers.
    """

    forward_port_algorithm: Optional[ForwardPortAlgorithm]
    """
    Load balancing algorithm to be used when determining which backend server to forward new traffic to.
    """

    sticky_sessions: Optional[StickySessionsType]
    """
    Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie TO stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for cookie-based sticky sessions.
    """

    health_check: HealthCheck
    """
    Object defining the health check to be carried out by the backend when checking the status and health of backend servers.
    """

    server_ip: List[str]
    """
    List of backend server IP addresses (IPv4 or IPv6) the backend should forward traffic to.
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field.
    :deprecated
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

    on_marked_down_action: OnMarkedDownAction
    """
    Action to take when a backend server is marked as down.
    """

    proxy_protocol: ProxyProtocol
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
class ZonedApiGetBackendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    backend_id: str
    """
    Backend ID.
    """


@dataclass
class ZonedApiUpdateBackendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    backend_id: str
    """
    Backend ID.
    """

    name: str
    """
    Backend name.
    """

    forward_protocol: Optional[Protocol]
    """
    Protocol to be used by the backend when forwarding traffic to backend servers.
    """

    forward_port: int
    """
    Port to be used by the backend when forwarding traffic to backend servers.
    """

    forward_port_algorithm: Optional[ForwardPortAlgorithm]
    """
    Load balancing algorithm to be used when determining which backend server to forward new traffic to.
    """

    sticky_sessions: Optional[StickySessionsType]
    """
    Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie to stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for cookie-based sticky sessions.
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field.
    :deprecated
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

    on_marked_down_action: OnMarkedDownAction
    """
    Action to take when a backend server is marked as down.
    """

    proxy_protocol: ProxyProtocol
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
class ZonedApiDeleteBackendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    backend_id: str
    """
    ID of the backend to delete.
    """


@dataclass
class ZonedApiAddBackendServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    backend_id: str
    """
    Backend ID.
    """

    server_ip: List[str]
    """
    List of IP addresses to add to backend servers.
    """


@dataclass
class ZonedApiRemoveBackendServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    backend_id: str
    """
    Backend ID.
    """

    server_ip: List[str]
    """
    List of IP addresses to remove from backend servers.
    """


@dataclass
class ZonedApiSetBackendServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    backend_id: str
    """
    Backend ID.
    """

    server_ip: List[str]
    """
    List of IP addresses for backend servers. Any other existing backend servers will be removed.
    """


@dataclass
class ZonedApiUpdateHealthCheckRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    backend_id: str
    """
    Backend ID.
    """

    port: int
    """
    Port to use for the backend server health check.
    """

    check_delay: str
    """
    Time to wait between two consecutive health checks.
    """

    check_timeout: str
    """
    Maximum time a backend server has to reply to the health check.
    """

    check_max_retries: int
    """
    Number of consecutive unsuccessful health checks after which the server will be considered dead.
    """

    check_send_proxy: bool
    """
    Defines whether proxy protocol should be activated for the health check.
    """

    tcp_config: Optional[HealthCheckTcpConfig]
    """
    Object to configure a basic TCP health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    mysql_config: Optional[HealthCheckMysqlConfig]
    """
    Object to configure a MySQL health check. The check requires MySQL >=3.22, for older versions, use a TCP health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    pgsql_config: Optional[HealthCheckPgsqlConfig]
    """
    Object to configure a PostgreSQL health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    ldap_config: Optional[HealthCheckLdapConfig]
    """
    Object to configure an LDAP health check. The response is analyzed to find the LDAPv3 response message.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    redis_config: Optional[HealthCheckRedisConfig]
    """
    Object to configure a Redis health check. The response is analyzed to find the +PONG response message.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    http_config: Optional[HealthCheckHttpConfig]
    """
    Object to configure an HTTP health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    https_config: Optional[HealthCheckHttpsConfig]
    """
    Object to configure an HTTPS health check.
    
    One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
    """

    transient_check_delay: Optional[str]
    """
    Time to wait between two consecutive health checks when a backend server is in a transient state (going UP or DOWN).
    """


@dataclass
class ZonedApiListFrontendsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
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
class ZonedApiCreateFrontendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID (ID of the Load Balancer to attach the frontend to).
    """

    name: Optional[str]
    """
    Name for the frontend.
    """

    inbound_port: int
    """
    Port the frontend should listen on.
    """

    backend_id: str
    """
    Backend ID (ID of the backend the frontend should pass traffic to).
    """

    timeout_client: Optional[str]
    """
    Maximum allowed inactivity time on the client side.
    """

    certificate_id: Optional[str]
    """
    Certificate ID, deprecated in favor of certificate_ids array.
    :deprecated
    """

    certificate_ids: Optional[List[str]]
    """
    List of SSL/TLS certificate IDs to bind to the frontend.
    """

    enable_http3: bool
    """
    Defines whether to enable HTTP/3 protocol on the frontend.
    """


@dataclass
class ZonedApiGetFrontendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    frontend_id: str
    """
    Frontend ID.
    """


@dataclass
class ZonedApiUpdateFrontendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    frontend_id: str
    """
    Frontend ID.
    """

    name: str
    """
    Frontend name.
    """

    inbound_port: int
    """
    Port the frontend should listen on.
    """

    backend_id: str
    """
    Backend ID (ID of the backend the frontend should pass traffic to).
    """

    timeout_client: Optional[str]
    """
    Maximum allowed inactivity time on the client side.
    """

    certificate_id: Optional[str]
    """
    Certificate ID, deprecated in favor of certificate_ids array.
    :deprecated
    """

    certificate_ids: Optional[List[str]]
    """
    List of SSL/TLS certificate IDs to bind to the frontend.
    """

    enable_http3: bool
    """
    Defines whether to enable HTTP/3 protocol on the frontend.
    """


@dataclass
class ZonedApiDeleteFrontendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    frontend_id: str
    """
    ID of the frontend to delete.
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
class ZonedApiCreateRouteRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    frontend_id: str
    """
    ID of the source frontend to create the route on.
    """

    backend_id: str
    """
    ID of the target backend for the route.
    """

    match: Optional[RouteMatch]
    """
    Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
    """


@dataclass
class ZonedApiGetRouteRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    route_id: str
    """
    Route ID.
    """


@dataclass
class ZonedApiUpdateRouteRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    route_id: str
    """
    Route ID.
    """

    backend_id: str
    """
    ID of the target backend for the route.
    """

    match: Optional[RouteMatch]
    """
    Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
    """


@dataclass
class ZonedApiDeleteRouteRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    route_id: str
    """
    Route ID.
    """


@dataclass
class ZonedApiGetLbStatsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    backend_id: Optional[str]
    """
    ID of the backend.
    """


@dataclass
class ZonedApiListBackendStatsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
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
class ZonedApiListAclsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    frontend_id: str
    """
    Frontend ID (ACLs attached to this frontend will be returned in the response).
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
class ZonedApiCreateAclRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    frontend_id: str
    """
    Frontend ID to attach the ACL to.
    """

    name: Optional[str]
    """
    ACL name.
    """

    action: AclAction
    """
    Action to take when incoming traffic matches an ACL filter.
    """

    match: Optional[AclMatch]
    """
    ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
    """

    index: int
    """
    Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
    """

    description: str
    """
    ACL description.
    """


@dataclass
class ZonedApiGetAclRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    acl_id: str
    """
    ACL ID.
    """


@dataclass
class ZonedApiUpdateAclRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    acl_id: str
    """
    ACL ID.
    """

    name: str
    """
    ACL name.
    """

    action: AclAction
    """
    Action to take when incoming traffic matches an ACL filter.
    """

    match: Optional[AclMatch]
    """
    ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
    """

    index: int
    """
    Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
    """

    description: Optional[str]
    """
    ACL description.
    """


@dataclass
class ZonedApiDeleteAclRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    acl_id: str
    """
    ACL ID.
    """


@dataclass
class ZonedApiSetAclsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    frontend_id: str
    """
    Frontend ID.
    """

    acls: List[AclSpec]
    """
    List of ACLs for this frontend. Any other existing ACLs on this frontend will be removed.
    """


@dataclass
class ZonedApiCreateCertificateRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    name: Optional[str]
    """
    Name for the certificate.
    """

    letsencrypt: Optional[CreateCertificateRequestLetsencryptConfig]
    """
    Object to define a new Let's Encrypt certificate to be generated.
    
    One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
    """

    custom_certificate: Optional[CreateCertificateRequestCustomCertificate]
    """
    Object to define an existing custom certificate to be imported.
    
    One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
    """


@dataclass
class ZonedApiListCertificatesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
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
class ZonedApiGetCertificateRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    certificate_id: str
    """
    Certificate ID.
    """


@dataclass
class ZonedApiUpdateCertificateRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    certificate_id: str
    """
    Certificate ID.
    """

    name: str
    """
    Certificate name.
    """


@dataclass
class ZonedApiDeleteCertificateRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    certificate_id: str
    """
    Certificate ID.
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
class ZonedApiCreateSubscriberRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: str
    """
    Subscriber name.
    """

    email_config: Optional[SubscriberEmailConfig]
    """
    Email address configuration.
    
    One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
    """

    webhook_config: Optional[SubscriberWebhookConfig]
    """
    WebHook URI configuration.
    
    One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
    """

    organization_id: Optional[str]
    """
    Organization ID to create the subscriber in.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Project ID to create the subscriber in.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """


@dataclass
class ZonedApiGetSubscriberRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    subscriber_id: str
    """
    Subscriber ID.
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

    name: str
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
class ZonedApiUpdateSubscriberRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    subscriber_id: str
    """
    Subscriber ID.
    """

    name: str
    """
    Subscriber name.
    """

    email_config: Optional[SubscriberEmailConfig]
    """
    Email address configuration.
    
    One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
    """

    webhook_config: Optional[SubscriberWebhookConfig]
    """
    Webhook URI configuration.
    
    One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
    """


@dataclass
class ZonedApiDeleteSubscriberRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    subscriber_id: str
    """
    Subscriber ID.
    """


@dataclass
class ZonedApiSubscribeToLbRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    subscriber_id: str
    """
    Subscriber ID.
    """


@dataclass
class ZonedApiUnsubscribeFromLbRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """


@dataclass
class ZonedApiListLbPrivateNetworksRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
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
class ZonedApiAttachPrivateNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load Balancer ID.
    """

    private_network_id: str
    """
    Private Network ID.
    """

    static_config: Optional[PrivateNetworkStaticConfig]
    """
    Object containing an array of a local IP address for the Load Balancer on this Private Network.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
    """

    dhcp_config: Optional[PrivateNetworkDHCPConfig]
    """
    Defines whether to let DHCP assign IP addresses.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
    """

    ipam_config: Optional[PrivateNetworkIpamConfig]
    """
    For internal use only.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
    """


@dataclass
class ZonedApiDetachPrivateNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    lb_id: str
    """
    Load balancer ID.
    """

    private_network_id: str
    """
    Set your instance private network id.
    """
