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
    The PROXY protocol informs the other end about the incoming connection, so that it can know the client's address or the public address it accessed to, whatever the upper layer protocol.

    * `proxy_protocol_none` Disable proxy protocol.
    * `proxy_protocol_v1` Version one (text format).
    * `proxy_protocol_v2` Version two (binary format).
    * `proxy_protocol_v2_ssl` Version two with SSL connection.
    * `proxy_protocol_v2_ssl_cn` Version two with SSL connection and common name information.

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
    The use of Access Control Lists (ACL) provide a flexible solution to perform a action generally consist in blocking or allow a request based on ip (and URL on HTTP)
    """

    id: str
    """
    ID of your ACL ressource
    """

    name: str
    """
    Name of you ACL ressource
    """

    match: Optional[AclMatch]
    """
    The ACL match rule. At least `ip_subnet` or `http_filter` and `http_filter_value` are required
    """

    action: Optional[AclAction]
    """
    Action to undertake when an ACL filter matches
    """

    frontend: Optional[Frontend]
    """
    See the Frontend object description
    """

    index: int
    """
    Order between your Acls (ascending order, 0 is first acl executed)
    """

    created_at: Optional[datetime]
    """
    Date at which the ACL was created
    """

    updated_at: Optional[datetime]
    """
    Date at which the ACL was last updated
    """

    description: str
    """
    Description of your ACL ressource
    """


@dataclass
class AclAction:
    """
    Acl action
    """

    type_: AclActionType
    """
    The action type
    """

    redirect: Optional[AclActionRedirect]
    """
    Redirect parameters when using an ACL with `redirect` action
    """


@dataclass
class AclActionRedirect:
    """
    Acl action redirect
    """

    type_: AclActionRedirectRedirectType
    """
    Redirect type
    """

    target: str
    """
    An URL can be used in case of a location redirect (e.g. `https://scaleway.com` will redirect to this same URL).
    A scheme name (e.g. `https`, `http`, `ftp`, `git`) will replace the request's original scheme. This can be useful to implement HTTP to HTTPS redirects.
    Placeholders can be used when using a `location` redirect in order to insert original request's parts, these are:
    - `{{ host }}` for the current request's Host header
    - `{{ query }}` for the current request's query string
    - `{{ path }}` for the current request's URL path
    - `{{ scheme }}` for the current request's scheme
    
    """

    code: Optional[int]
    """
    HTTP redirect code to use. Valid values are 301, 302, 303, 307 and 308. Default value is 302
    """


@dataclass
class AclMatch:
    """
    Acl match
    """

    ip_subnet: List[str]
    """
    A list of IPs or CIDR v4/v6 addresses of the client of the session to match
    """

    http_filter: AclHttpFilter
    """
    The HTTP filter to match. This filter is supported only if your backend supports HTTP forwarding.
    It extracts the request's URL path, which starts at the first slash and ends before the question mark (without the host part).
    
    """

    http_filter_value: List[str]
    """
    A list of possible values to match for the given HTTP filter
    """

    http_filter_option: Optional[str]
    """
    A exra parameter. You can use this field with http_header_match acl type to set the header name to filter
    """

    invert: bool
    """
    If set to `true`, the ACL matching condition will be of type "UNLESS"
    """


@dataclass
class AclSpec:
    """
    Acl spec
    """

    name: str
    """
    Name of your ACL resource
    """

    action: AclAction
    """
    Action to undertake when an ACL filter matches
    """

    match: AclMatch
    """
    The ACL match rule. At least `ip_subnet` or `http_filter` and `http_filter_value` are required
    """

    index: int
    """
    Order between your Acls (ascending order, 0 is first acl executed)
    """

    description: str
    """
    Description of your ACL ressource
    """


@dataclass
class Backend:
    """
    Backend
    """

    id: str
    """
    Load balancer Backend ID
    """

    name: str
    """
    Load balancer Backend name
    """

    forward_protocol: Protocol
    """
    Type of backend protocol
    """

    forward_port: int
    """
    User sessions will be forwarded to this port of backend servers
    """

    forward_port_algorithm: ForwardPortAlgorithm
    """
    Load balancer algorithm used to select the backend server
    """

    sticky_sessions: StickySessionsType
    """
    Enables cookie-based session persistence
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for sticky sessions
    """

    health_check: Optional[HealthCheck]
    """
    Health Check used to verify backend servers status
    """

    pool: List[str]
    """
    Servers IP addresses attached to the backend
    """

    lb: Optional[Lb]
    """
    Load balancer the backend is attached to
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field
    :deprecated
    """

    timeout_server: Optional[str]
    """
    Maximum server connection inactivity time (allowed time the server has to process the request)
    """

    timeout_connect: Optional[str]
    """
    Maximum initial server connection establishment time
    """

    timeout_tunnel: Optional[str]
    """
    Maximum tunnel inactivity time after Websocket is established (take precedence over client and server timeout)
    """

    on_marked_down_action: OnMarkedDownAction
    """
    Defines what occurs when a backend server is marked down
    """

    proxy_protocol: ProxyProtocol
    """
    PROXY protocol, forward client's address (must be supported by backend servers software)
    """

    created_at: Optional[datetime]
    """
    Date at which the backend was created
    """

    updated_at: Optional[datetime]
    """
    Date at which the backend was updated
    """

    failover_host: Optional[str]
    """
    Scaleway S3 bucket website to be served in case all backend servers are down
    """

    ssl_bridging: Optional[bool]
    """
    Enable SSL between load balancer and backend servers
    """

    ignore_ssl_server_verify: Optional[bool]
    """
    Whether or not the server certificate should be verified
    """


@dataclass
class BackendServerStats:
    """
    State and statistics of your backend server like last health check status, server uptime, result state of your backend server
    """

    instance_id: str
    """
    ID of your Load balancer cluster server
    """

    backend_id: str
    """
    ID of your Backend
    """

    ip: str
    """
    IPv4 or IPv6 address of the server backend
    """

    server_state: BackendServerStatsServerState
    """
    Server operational state (stopped/starting/running/stopping)
    """

    server_state_changed_at: Optional[datetime]
    """
    Time since last operational change
    """

    last_health_check_status: BackendServerStatsHealthCheckStatus
    """
    Last health check status (unknown/neutral/failed/passed/condpass)
    """


@dataclass
class Certificate:
    """
    SSL certificate
    """

    type_: CertificateType
    """
    Type of certificate (Let's encrypt or custom)
    """

    id: str
    """
    Certificate ID
    """

    common_name: str
    """
    Main domain name of certificate
    """

    subject_alternative_name: List[str]
    """
    Alternative domain names
    """

    fingerprint: str
    """
    Identifier (SHA-1) of the certificate
    """

    not_valid_before: Optional[datetime]
    """
    Validity bounds
    """

    not_valid_after: Optional[datetime]
    """
    Validity bounds
    """

    status: CertificateStatus
    """
    Status of certificate
    """

    lb: Optional[Lb]
    """
    Load balancer object
    """

    name: str
    """
    Certificate name
    """

    created_at: Optional[datetime]
    """
    Date at which the certificate was created
    """

    updated_at: Optional[datetime]
    """
    Date at which the certificate was last updated
    """

    status_details: Optional[str]
    """
    Additional information on the status (e.g. in case of certificate generation failure)
    """


@dataclass
class CreateCertificateRequestCustomCertificate:
    """
    Import a custom SSL certificate
    """

    certificate_chain: str
    """
    The full PEM-formatted include an entire certificate chain including public key, private key, and optionally certificate authorities.
    """


@dataclass
class CreateCertificateRequestLetsencryptConfig:
    """
    Generate a new SSL certificate using Let's Encrypt.
    """

    common_name: str
    """
    Main domain name of certificate (make sure this domain exists and resolves to your load balancer HA IP)
    """

    subject_alternative_name: List[str]
    """
    Alternative domain names (make sure all domain names exists and resolves to your load balancer HA IP)
    """


@dataclass
class Frontend:
    """
    Frontend
    """

    id: str
    """
    Load balancer Frontend ID
    """

    name: str
    """
    Load balancer Frontend name
    """

    inbound_port: int
    """
    TCP port to listen on the front side
    """

    backend: Optional[Backend]
    """
    Backend resource the Frontend is attached to
    """

    lb: Optional[Lb]
    """
    Load balancer the frontend is attached to
    """

    timeout_client: Optional[str]
    """
    Maximum inactivity time on the client side
    """

    certificate: Optional[Certificate]
    """
    Certificate, deprecated in favor of certificate_ids array
    :deprecated
    """

    certificate_ids: List[str]
    """
    List of certificate IDs to bind on the frontend
    """

    created_at: Optional[datetime]
    """
    Date at which the frontend was created
    """

    updated_at: Optional[datetime]
    """
    Date at which the frontend was updated
    """

    enable_http3: bool
    """
    Whether or not HTTP3 protocol is enabled
    """


@dataclass
class HealthCheck:
    """
    Health check
    """

    mysql_config: Optional[HealthCheckMysqlConfig]
    """
    The check requires MySQL >=3.22, for older versions, use TCP check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'tcp_config', 'pgsql_config', 'http_config', 'https_config' could be set.
    """

    ldap_config: Optional[HealthCheckLdapConfig]
    """
    The response is analyzed to find an LDAPv3 response message.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'tcp_config', 'pgsql_config', 'http_config', 'https_config' could be set.
    """

    redis_config: Optional[HealthCheckRedisConfig]
    """
    The response is analyzed to find the +PONG response message.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'tcp_config', 'pgsql_config', 'http_config', 'https_config' could be set.
    """

    check_max_retries: int
    """
    Number of consecutive unsuccessful health checks, after which the server will be considered dead
    """

    tcp_config: Optional[HealthCheckTcpConfig]
    """
    Basic TCP health check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'tcp_config', 'pgsql_config', 'http_config', 'https_config' could be set.
    """

    pgsql_config: Optional[HealthCheckPgsqlConfig]
    """
    PostgreSQL health check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'tcp_config', 'pgsql_config', 'http_config', 'https_config' could be set.
    """

    http_config: Optional[HealthCheckHttpConfig]
    """
    HTTP health check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'tcp_config', 'pgsql_config', 'http_config', 'https_config' could be set.
    """

    https_config: Optional[HealthCheckHttpsConfig]
    """
    HTTPS health check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'tcp_config', 'pgsql_config', 'http_config', 'https_config' could be set.
    """

    port: int
    """
    TCP port to use for the backend server health check
    """

    check_timeout: Optional[str]
    """
    Maximum time a backend server has to reply to the health check
    """

    check_delay: Optional[str]
    """
    Time between two consecutive health checks
    """

    check_send_proxy: bool
    """
    It defines whether the health check should be done considering the proxy protocol
    """


@dataclass
class HealthCheckHttpConfig:
    """
    Health check. http config
    """

    uri: str
    """
    HTTP uri used for Healthcheck to the backend servers
    """

    method: str
    """
    HTTP method used for Healthcheck to the backend servers
    """

    code: Optional[int]
    """
    A health check response will be considered as valid if the response's status code match
    """

    host_header: str
    """
    HTTP host header used with the request
    """


@dataclass
class HealthCheckHttpsConfig:
    """
    Health check. https config
    """

    uri: str
    """
    HTTP uri used for Healthcheck to the backend servers
    """

    method: str
    """
    HTTP method used for Healthcheck to the backend servers
    """

    code: Optional[int]
    """
    A health check response will be considered as valid if the response's status code match
    """

    host_header: str
    """
    HTTP host header used with the request
    """

    sni: str
    """
    Specifies the SNI to use to do health checks over SSL
    """


@dataclass
class HealthCheckLdapConfig:
    pass


@dataclass
class HealthCheckMysqlConfig:
    user: str


@dataclass
class HealthCheckPgsqlConfig:
    user: str


@dataclass
class HealthCheckRedisConfig:
    pass


@dataclass
class HealthCheckTcpConfig:
    pass


@dataclass
class Instance:
    """
    Instance
    """

    id: str
    """
    Underlying Instance ID
    """

    status: InstanceStatus
    """
    Instance status
    """

    ip_address: str
    """
    Instance IP address
    """

    created_at: Optional[datetime]
    """
    Date at which the Instance was created
    """

    updated_at: Optional[datetime]
    """
    Date at which the Instance was updated
    """

    region: Optional[Region]
    """
    The region the instance is in
    :deprecated
    """

    zone: Zone
    """
    The zone the instance is in
    """


@dataclass
class Ip:
    """
    Ip
    """

    id: str
    """
    Flexible IP ID
    """

    ip_address: str
    """
    IP address
    """

    organization_id: str
    """
    Organization ID
    """

    project_id: str
    """
    Project ID
    """

    lb_id: Optional[str]
    """
    Load balancer ID
    """

    reverse: str
    """
    Reverse FQDN
    """

    region: Optional[Region]
    """
    The region the Flexible IP is in
    :deprecated
    """

    zone: Zone
    """
    The zone the Flexible IP is in
    """


@dataclass
class Lb:
    """
    Lb
    """

    id: str
    """
    Underlying Instance ID
    """

    name: str
    """
    Load balancer name
    """

    description: str
    """
    Load balancer description
    """

    status: LbStatus
    """
    Load balancer status
    """

    instances: List[Instance]
    """
    List of underlying instances
    """

    organization_id: str
    """
    Organization ID
    """

    project_id: str
    """
    Project ID
    """

    ip: List[Ip]
    """
    List of IPs attached to the Load balancer
    """

    tags: List[str]
    """
    Load balancer tags
    """

    frontend_count: int
    """
    Number of frontends the Load balancer has
    """

    backend_count: int
    """
    Number of backends the Load balancer has
    """

    type_: str
    """
    Load balancer offer type
    """

    subscriber: Optional[Subscriber]
    """
    Subscriber information
    """

    ssl_compatibility_level: SSLCompatibilityLevel
    """
    Determines the minimal SSL version which needs to be supported on client side
    """

    created_at: Optional[datetime]
    """
    Date at which the Load balancer was created
    """

    updated_at: Optional[datetime]
    """
    Date at which the Load balancer was updated
    """

    private_network_count: int
    """
    Number of private networks attached to the Load balancer
    """

    route_count: int
    """
    Number of routes the Load balancer has
    """

    region: Optional[Region]
    """
    The region the Load balancer is in
    :deprecated
    """

    zone: Zone
    """
    The zone the Load balancer is in
    """


@dataclass
class LbStats:
    """
    Lb stats
    """

    backend_servers_stats: List[BackendServerStats]
    """
    List stats object of your Load balancer
    """


@dataclass
class LbType:
    name: str

    stock_status: LbTypeStock

    description: str

    region: Optional[Region]
    """
    :deprecated
    """

    zone: Zone


@dataclass
class ListAclResponse:
    """
    List acl response
    """

    acls: List[Acl]
    """
    List of Acl object (see Acl object description)
    """

    total_count: int
    """
    The total number of items
    """


@dataclass
class ListBackendStatsResponse:
    """
    List backend stats response
    """

    backend_servers_stats: List[BackendServerStats]
    """
    List backend stats object of your Load balancer
    """

    total_count: int
    """
    The total number of items
    """


@dataclass
class ListBackendsResponse:
    """
    List backends response
    """

    backends: List[Backend]
    """
    List Backend objects of a load balancer
    """

    total_count: int
    """
    Total count, wihtout pagination
    """


@dataclass
class ListCertificatesResponse:
    """
    List certificates response
    """

    certificates: List[Certificate]
    """
    List of certificates
    """

    total_count: int
    """
    The total number of items
    """


@dataclass
class ListFrontendsResponse:
    """
    List frontends response
    """

    frontends: List[Frontend]
    """
    List frontends object of your Load balancer
    """

    total_count: int
    """
    Total count, wihtout pagination
    """


@dataclass
class ListIpsResponse:
    """
    List ips response
    """

    ips: List[Ip]
    """
    List IP address object
    """

    total_count: int
    """
    Total count, wihtout pagination
    """


@dataclass
class ListLbPrivateNetworksResponse:
    """
    List lb private networks response
    """

    private_network: List[PrivateNetwork]
    """
    Private networks of a given load balancer
    """

    total_count: int
    """
    The total number of items
    """


@dataclass
class ListLbTypesResponse:
    """
    List lb types response
    """

    lb_types: List[LbType]
    """
    Different types of LB
    """

    total_count: int
    """
    The total number of items
    """


@dataclass
class ListLbsResponse:
    """
    Get list of Load balancers
    """

    lbs: List[Lb]
    """
    List of Load balancer
    """

    total_count: int
    """
    The total number of items
    """


@dataclass
class ListRoutesResponse:
    """
    List routes response
    """

    routes: List[Route]
    """
    List of Routes object
    """

    total_count: int
    """
    The total number of items
    """


@dataclass
class ListSubscriberResponse:
    """
    List subscriber response
    """

    subscribers: List[Subscriber]
    """
    List of Subscribers object
    """

    total_count: int
    """
    The total number of items
    """


@dataclass
class PrivateNetwork:
    """
    Private network
    """

    lb: Optional[Lb]
    """
    LoadBalancer object
    """

    static_config: Optional[PrivateNetworkStaticConfig]
    """
    Local ip address of load balancer instance.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config' could be set.
    """

    dhcp_config: Optional[PrivateNetworkDHCPConfig]
    """
    Value set to true if load balancer instance use a DHCP.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config' could be set.
    """

    private_network_id: str
    """
    Instance private network id
    """

    status: PrivateNetworkStatus
    """
    Status (running, to create...) of private network connection
    """

    created_at: Optional[datetime]
    """
    Date at which the PN was created
    """

    updated_at: Optional[datetime]
    """
    Date at which the PN was last updated
    """


@dataclass
class PrivateNetworkDHCPConfig:
    pass


@dataclass
class PrivateNetworkStaticConfig:
    ip_address: List[str]


@dataclass
class Route:
    """
    Route
    """

    id: str
    """
    Id of match ressource
    """

    frontend_id: str
    """
    Id of frontend
    """

    backend_id: str
    """
    Id of backend
    """

    match: Optional[RouteMatch]
    """
    Value to match a redirection
    """

    created_at: Optional[datetime]
    """
    Date at which the route was created
    """

    updated_at: Optional[datetime]
    """
    Date at which the route was last updated
    """


@dataclass
class RouteMatch:
    """
    Route. match
    """

    sni: Optional[str]
    """
    Server Name Indication TLS extension (SNI) field from an incoming connection made via an SSL/TLS transport layer.
    
    One-of ('match_type'): at most one of 'sni', 'host_header' could be set.
    """

    host_header: Optional[str]
    """
    The Host request header specifies the host of the server to which the request is being sent.
    
    One-of ('match_type'): at most one of 'sni', 'host_header' could be set.
    """


@dataclass
class SetAclsResponse:
    """
    Set acls response
    """

    acls: List[Acl]
    """
    List of ACLs object (see ACL object description)
    """

    total_count: int
    """
    The total number of items
    """


@dataclass
class Subscriber:
    """
    Subscriber
    """

    id: str
    """
    Subscriber ID
    """

    name: str
    """
    Subscriber name
    """

    email_config: Optional[SubscriberEmailConfig]
    """
    Email address of subscriber.
    
    One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
    """

    webhook_config: Optional[SubscriberWebhookConfig]
    """
    WebHook URI of subscriber.
    
    One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
    """


@dataclass
class SubscriberEmailConfig:
    """
    Email alert of subscriber
    """

    email: str
    """
    Email who receive alert
    """


@dataclass
class SubscriberWebhookConfig:
    """
    Webhook alert of subscriber
    """

    uri: str
    """
    URI who receive POST request
    """


@dataclass
class ListLbsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    name: Optional[str]
    """
    Use this to search by name
    """

    order_by: Optional[ListLbsRequestOrderBy]
    """
    Response order
    """

    page_size: Optional[int]
    """
    The number of items to return
    """

    page: Optional[int]
    """
    Page number
    """

    organization_id: Optional[str]
    """
    Filter LBs by organization ID
    """

    project_id: Optional[str]
    """
    Filter LBs by project ID
    """


@dataclass
class CreateLbRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    organization_id: Optional[str]
    """
    Owner of resources.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Assign the resource to a project ID.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """

    name: Optional[str]
    """
    Resource names
    """

    description: str
    """
    Resource description
    """

    ip_id: Optional[str]
    """
    Just like for compute instances, when you destroy a load balancer, you can keep its highly available IP address and reuse it for another load balancer later
    """

    tags: Optional[List[str]]
    """
    List of keyword
    """

    type_: str
    """
    Load balancer offer type
    """

    ssl_compatibility_level: SSLCompatibilityLevel
    """
    Enforces minimal SSL version (in SSL/TLS offloading context).
    - `intermediate` General-purpose servers with a variety of clients, recommended for almost all systems (Supports Firefox 27, Android 4.4.2, Chrome 31, Edge, IE 11 on Windows 7, Java 8u31, OpenSSL 1.0.1, Opera 20, and Safari 9).
    - `modern` Services with clients that support TLS 1.3 and don't need backward compatibility (Firefox 63, Android 10.0, Chrome 70, Edge 75, Java 11, OpenSSL 1.1.1, Opera 57, and Safari 12.1).
    - `old` Compatible with a number of very old clients, and should be used only as a last resort (Firefox 1, Android 2.3, Chrome 1, Edge 12, IE8 on Windows XP, Java 6, OpenSSL 0.9.8, Opera 5, and Safari 1).
    
    """


@dataclass
class GetLbRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """


@dataclass
class UpdateLbRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    name: str
    """
    Resource name
    """

    description: str
    """
    Resource description
    """

    tags: Optional[List[str]]
    """
    List of keywords
    """

    ssl_compatibility_level: SSLCompatibilityLevel
    """
    Enforces minimal SSL version (in SSL/TLS offloading context).
    - `intermediate` General-purpose servers with a variety of clients, recommended for almost all systems (Supports Firefox 27, Android 4.4.2, Chrome 31, Edge, IE 11 on Windows 7, Java 8u31, OpenSSL 1.0.1, Opera 20, and Safari 9).
    - `modern` Services with clients that support TLS 1.3 and don't need backward compatibility (Firefox 63, Android 10.0, Chrome 70, Edge 75, Java 11, OpenSSL 1.1.1, Opera 57, and Safari 12.1).
    - `old` Compatible with a number of very old clients, and should be used only as a last resort (Firefox 1, Android 2.3, Chrome 1, Edge 12, IE8 on Windows XP, Java 6, OpenSSL 0.9.8, Opera 5, and Safari 1).
    
    """


@dataclass
class DeleteLbRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    release_ip: bool
    """
    Set true if you don't want to keep this IP address
    """


@dataclass
class MigrateLbRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    type_: str
    """
    Load balancer type (check /lb-types to list all type)
    """


@dataclass
class ListIPsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """

    ip_address: Optional[str]
    """
    Use this to search by IP address
    """

    organization_id: Optional[str]
    """
    Filter IPs by organization id
    """

    project_id: Optional[str]
    """
    Filter IPs by project ID
    """


@dataclass
class CreateIpRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    organization_id: Optional[str]
    """
    Owner of resources.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Assign the resource to a project ID.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """

    reverse: Optional[str]
    """
    Reverse domain name
    """


@dataclass
class GetIpRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    ip_id: str
    """
    IP address ID
    """


@dataclass
class ReleaseIpRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    ip_id: str
    """
    IP address ID
    """


@dataclass
class UpdateIpRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    ip_id: str
    """
    IP address ID
    """

    reverse: Optional[str]
    """
    Reverse DNS
    """


@dataclass
class ListBackendsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    name: Optional[str]
    """
    Use this to search by name
    """

    order_by: Optional[ListBackendsRequestOrderBy]
    """
    Response order
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """


@dataclass
class CreateBackendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    name: Optional[str]
    """
    Resource name
    """

    forward_protocol: Optional[Protocol]
    """
    Backend protocol. TCP or HTTP
    """

    forward_port: int
    """
    User sessions will be forwarded to this port of backend servers
    """

    forward_port_algorithm: Optional[ForwardPortAlgorithm]
    """
    Load balancing algorithm
    """

    sticky_sessions: Optional[StickySessionsType]
    """
    Enables cookie-based session persistence
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for sticky sessions
    """

    health_check: HealthCheck
    """
    See the Healthcheck object description
    """

    server_ip: List[str]
    """
    Backend server IP addresses list (IPv4 or IPv6)
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field !
    :deprecated
    """

    timeout_server: Optional[str]
    """
    Maximum server connection inactivity time (allowed time the server has to process the request)
    """

    timeout_connect: Optional[str]
    """
    Maximum initial server connection establishment time
    """

    timeout_tunnel: Optional[str]
    """
    Maximum tunnel inactivity time after Websocket is established (take precedence over client and server timeout)
    """

    on_marked_down_action: OnMarkedDownAction
    """
    Modify what occurs when a backend server is marked down
    """

    proxy_protocol: ProxyProtocol
    """
    The PROXY protocol informs the other end about the incoming connection, so that it can know the client's address or the public address it accessed to, whatever the upper layer protocol.
    
    * `proxy_protocol_none` Disable proxy protocol.
    * `proxy_protocol_v1` Version one (text format).
    * `proxy_protocol_v2` Version two (binary format).
    * `proxy_protocol_v2_ssl` Version two with SSL connection.
    * `proxy_protocol_v2_ssl_cn` Version two with SSL connection and common name information.
    
    """

    failover_host: Optional[str]
    """
    Only the host part of the Scaleway S3 bucket website is expected.
    E.g. `failover-website.s3-website.fr-par.scw.cloud` if your bucket website URL is `https://failover-website.s3-website.fr-par.scw.cloud/`.
    
    """

    ssl_bridging: Optional[bool]
    """
    Enable SSL between load balancer and backend servers
    """

    ignore_ssl_server_verify: Optional[bool]
    """
    Set to true to ignore server certificate verification
    """


@dataclass
class GetBackendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    backend_id: str
    """
    Backend ID
    """


@dataclass
class UpdateBackendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    backend_id: str
    """
    Backend ID to update
    """

    name: str
    """
    Resource name
    """

    forward_protocol: Optional[Protocol]
    """
    Backend protocol. TCP or HTTP
    """

    forward_port: int
    """
    User sessions will be forwarded to this port of backend servers
    """

    forward_port_algorithm: Optional[ForwardPortAlgorithm]
    """
    Load balancing algorithm
    """

    sticky_sessions: Optional[StickySessionsType]
    """
    Enable cookie-based session persistence
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for sticky sessions
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field!
    :deprecated
    """

    timeout_server: Optional[str]
    """
    Maximum server connection inactivity time (allowed time the server has to process the request)
    """

    timeout_connect: Optional[str]
    """
    Maximum initial server connection establishment time
    """

    timeout_tunnel: Optional[str]
    """
    Maximum tunnel inactivity time after Websocket is established (take precedence over client and server timeout)
    """

    on_marked_down_action: OnMarkedDownAction
    """
    Modify what occurs when a backend server is marked down
    """

    proxy_protocol: ProxyProtocol
    """
    The PROXY protocol informs the other end about the incoming connection, so that it can know the client's address or the public address it accessed to, whatever the upper layer protocol is.
    
    * `proxy_protocol_none` Disable proxy protocol.
    * `proxy_protocol_v1` Version one (text format).
    * `proxy_protocol_v2` Version two (binary format).
    * `proxy_protocol_v2_ssl` Version two with SSL connection.
    * `proxy_protocol_v2_ssl_cn` Version two with SSL connection and common name information.
    
    """

    failover_host: Optional[str]
    """
    Only the host part of the Scaleway S3 bucket website is expected.
    Example: `failover-website.s3-website.fr-par.scw.cloud` if your bucket website URL is `https://failover-website.s3-website.fr-par.scw.cloud/`.
    
    """

    ssl_bridging: Optional[bool]
    """
    Enable SSL between load balancer and backend servers
    """

    ignore_ssl_server_verify: Optional[bool]
    """
    Set to true to ignore server certificate verification
    """


@dataclass
class DeleteBackendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    backend_id: str
    """
    ID of the backend to delete
    """


@dataclass
class AddBackendServersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    backend_id: str
    """
    Backend ID
    """

    server_ip: List[str]
    """
    Set all IPs to add on your backend
    """


@dataclass
class RemoveBackendServersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    backend_id: str
    """
    Backend ID
    """

    server_ip: List[str]
    """
    Set all IPs to remove of your backend
    """


@dataclass
class SetBackendServersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    backend_id: str
    """
    Backend ID
    """

    server_ip: List[str]
    """
    Set all IPs to add on your backend and remove all other
    """


@dataclass
class UpdateHealthCheckRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    backend_id: str
    """
    Backend ID
    """

    port: int
    """
    Specify the port used to health check
    """

    check_delay: str
    """
    Time between two consecutive health checks
    """

    check_timeout: str
    """
    Maximum time a backend server has to reply to the health check
    """

    check_max_retries: int
    """
    Number of consecutive unsuccessful health checks, after which the server will be considered dead
    """

    mysql_config: Optional[HealthCheckMysqlConfig]
    """
    The check requires MySQL >=3.22, for older version, please use TCP check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
    """

    ldap_config: Optional[HealthCheckLdapConfig]
    """
    The response is analyzed to find an LDAPv3 response message.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
    """

    redis_config: Optional[HealthCheckRedisConfig]
    """
    The response is analyzed to find the +PONG response message.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
    """

    pgsql_config: Optional[HealthCheckPgsqlConfig]
    """
    PostgreSQL health check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
    """

    tcp_config: Optional[HealthCheckTcpConfig]
    """
    Basic TCP health check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
    """

    http_config: Optional[HealthCheckHttpConfig]
    """
    HTTP health check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
    """

    https_config: Optional[HealthCheckHttpsConfig]
    """
    HTTPS health check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
    """

    check_send_proxy: bool
    """
    It defines whether the health check should be done considering the proxy protocol
    """


@dataclass
class ListFrontendsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    name: Optional[str]
    """
    Use this to search by name
    """

    order_by: Optional[ListFrontendsRequestOrderBy]
    """
    Response order
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """


@dataclass
class CreateFrontendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    name: Optional[str]
    """
    Resource name
    """

    inbound_port: int
    """
    TCP port to listen on the front side
    """

    backend_id: str
    """
    Backend ID
    """

    timeout_client: Optional[str]
    """
    Set the maximum inactivity time on the client side
    """

    certificate_id: Optional[str]
    """
    Certificate ID, deprecated in favor of certificate_ids array !
    :deprecated
    """

    certificate_ids: Optional[List[str]]
    """
    List of certificate IDs to bind on the frontend
    """

    enable_http3: bool
    """
    Activate HTTP 3 protocol (beta)
    """


@dataclass
class GetFrontendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    frontend_id: str
    """
    Frontend ID
    """


@dataclass
class UpdateFrontendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    frontend_id: str
    """
    Frontend ID
    """

    name: str
    """
    Resource name
    """

    inbound_port: int
    """
    TCP port to listen on the front side
    """

    backend_id: str
    """
    Backend ID
    """

    timeout_client: Optional[str]
    """
    Client session maximum inactivity time
    """

    certificate_id: Optional[str]
    """
    Certificate ID, deprecated in favor of `certificate_ids` array!
    :deprecated
    """

    certificate_ids: Optional[List[str]]
    """
    List of certificate IDs to bind on the frontend
    """

    enable_http3: bool
    """
    Activate HTTP 3 protocol (beta)
    """


@dataclass
class DeleteFrontendRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    frontend_id: str
    """
    Frontend ID to delete
    """


@dataclass
class ListRoutesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    order_by: Optional[ListRoutesRequestOrderBy]
    """
    Response order
    """

    page_size: Optional[int]
    """
    The number of items to return
    """

    page: Optional[int]
    """
    Page number
    """

    frontend_id: Optional[str]


@dataclass
class CreateRouteRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    frontend_id: str
    """
    Origin of redirection
    """

    backend_id: str
    """
    Destination of destination
    """

    match: Optional[RouteMatch]
    """
    Value to match a redirection
    """


@dataclass
class GetRouteRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    route_id: str
    """
    Id of route to get
    """


@dataclass
class UpdateRouteRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    route_id: str
    """
    Route id to update
    """

    backend_id: str
    """
    Backend id of redirection
    """

    match: Optional[RouteMatch]
    """
    Value to match a redirection
    """


@dataclass
class DeleteRouteRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    route_id: str
    """
    Route id to delete
    """


@dataclass
class GetLbStatsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """


@dataclass
class ListBackendStatsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """


@dataclass
class ListAclsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    frontend_id: str
    """
    ID of your frontend
    """

    order_by: Optional[ListAclRequestOrderBy]
    """
    Response order
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """

    name: Optional[str]
    """
    Filter acl per name
    """


@dataclass
class CreateAclRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    frontend_id: str
    """
    ID of your frontend
    """

    name: Optional[str]
    """
    Name of your ACL ressource
    """

    action: AclAction
    """
    Action to undertake when an ACL filter matches
    """

    match: AclMatch
    """
    The ACL match rule. You can have one of those three cases:
    
      - `ip_subnet` is defined
      - `http_filter` and `http_filter_value` are defined
      - `ip_subnet`, `http_filter` and `http_filter_value` are defined
    
    """

    index: int
    """
    Order between your Acls (ascending order, 0 is first acl executed)
    """

    description: str
    """
    Description of your ACL ressource
    """


@dataclass
class GetAclRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    acl_id: str
    """
    ID of your ACL ressource
    """


@dataclass
class UpdateAclRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    acl_id: str
    """
    ID of your ACL ressource
    """

    name: str
    """
    Name of your ACL ressource
    """

    action: AclAction
    """
    Action to undertake when an ACL filter matches
    """

    match: AclMatch
    """
    The ACL match rule. At least `ip_subnet` or `http_filter` and `http_filter_value` are required
    """

    index: int
    """
    Order between your Acls (ascending order, 0 is first acl executed)
    """

    description: Optional[str]
    """
    Description of your ACL ressource
    """


@dataclass
class DeleteAclRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    acl_id: str
    """
    ID of your ACL ressource
    """


@dataclass
class CreateCertificateRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    name: Optional[str]
    """
    Certificate name
    """

    letsencrypt: Optional[CreateCertificateRequestLetsencryptConfig]
    """
    Let's Encrypt type.
    
    One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
    """

    custom_certificate: Optional[CreateCertificateRequestCustomCertificate]
    """
    Custom import certificate.
    
    One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
    """


@dataclass
class ListCertificatesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    order_by: Optional[ListCertificatesRequestOrderBy]
    """
    Response order
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """

    name: Optional[str]
    """
    Use this to search by name
    """


@dataclass
class GetCertificateRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    certificate_id: str
    """
    Certificate ID
    """


@dataclass
class UpdateCertificateRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    certificate_id: str
    """
    Certificate ID
    """

    name: str
    """
    Certificate name
    """


@dataclass
class DeleteCertificateRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    certificate_id: str
    """
    Certificate ID
    """


@dataclass
class ListLbTypesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """


@dataclass
class CreateSubscriberRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    name: str
    """
    Subscriber name
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
    Owner of resources.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Assign the resource to a project ID.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """


@dataclass
class GetSubscriberRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    subscriber_id: str
    """
    Subscriber ID
    """


@dataclass
class ListSubscriberRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    order_by: Optional[ListSubscriberRequestOrderBy]
    """
    Response order
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """

    name: str
    """
    Use this to search by name
    """

    organization_id: Optional[str]
    """
    Filter Subscribers by organization ID
    """

    project_id: Optional[str]
    """
    Filter Subscribers by project ID
    """


@dataclass
class UpdateSubscriberRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    subscriber_id: str
    """
    Assign the resource to a project IDs
    """

    name: str
    """
    Subscriber name
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


@dataclass
class DeleteSubscriberRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    subscriber_id: str
    """
    Subscriber ID
    """


@dataclass
class SubscribeToLbRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    subscriber_id: str
    """
    Subscriber ID
    """


@dataclass
class UnsubscribeFromLbRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """


@dataclass
class ListLbPrivateNetworksRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    order_by: Optional[ListPrivateNetworksRequestOrderBy]
    """
    Response order
    """

    page_size: Optional[int]
    """
    The number of items to return
    """

    page: Optional[int]
    """
    Page number
    """


@dataclass
class AttachPrivateNetworkRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    private_network_id: str
    """
    Set your instance private network id
    """

    static_config: Optional[PrivateNetworkStaticConfig]
    """
    Define two local ip address of your choice for each load balancer instance.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config' could be set.
    """

    dhcp_config: Optional[PrivateNetworkDHCPConfig]
    """
    Set to true if you want to let DHCP assign IP addresses.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config' could be set.
    """


@dataclass
class DetachPrivateNetworkRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    private_network_id: str
    """
    Set your instance private network id
    """


@dataclass
class ZonedApiListLbsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    name: Optional[str]
    """
    Use this to search by name
    """

    order_by: Optional[ListLbsRequestOrderBy]
    """
    Response order
    """

    page_size: Optional[int]
    """
    The number of items to return
    """

    page: Optional[int]
    """
    Page number
    """

    organization_id: Optional[str]
    """
    Filter LBs by organization ID
    """

    project_id: Optional[str]
    """
    Filter LBs by project ID
    """


@dataclass
class ZonedApiCreateLbRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    organization_id: Optional[str]
    """
    Owner of resources.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Assign the resource to a project ID.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """

    name: Optional[str]
    """
    Resource names
    """

    description: str
    """
    Resource description
    """

    ip_id: Optional[str]
    """
    Just like for compute instances, when you destroy a load balancer, you can keep its highly available IP address and reuse it for another load balancer later
    """

    tags: Optional[List[str]]
    """
    List of keyword
    """

    type_: str
    """
    Load balancer offer type
    """

    ssl_compatibility_level: SSLCompatibilityLevel
    """
    Enforces minimal SSL version (in SSL/TLS offloading context).
    - `intermediate` General-purpose servers with a variety of clients, recommended for almost all systems (Supports Firefox 27, Android 4.4.2, Chrome 31, Edge, IE 11 on Windows 7, Java 8u31, OpenSSL 1.0.1, Opera 20, and Safari 9).
    - `modern` Services with clients that support TLS 1.3 and don't need backward compatibility (Firefox 63, Android 10.0, Chrome 70, Edge 75, Java 11, OpenSSL 1.1.1, Opera 57, and Safari 12.1).
    - `old` Compatible with a number of very old clients, and should be used only as a last resort (Firefox 1, Android 2.3, Chrome 1, Edge 12, IE8 on Windows XP, Java 6, OpenSSL 0.9.8, Opera 5, and Safari 1).
    
    """


@dataclass
class ZonedApiGetLbRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """


@dataclass
class ZonedApiUpdateLbRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    name: str
    """
    Resource name
    """

    description: str
    """
    Resource description
    """

    tags: Optional[List[str]]
    """
    List of keywords
    """

    ssl_compatibility_level: SSLCompatibilityLevel
    """
    Enforces minimal SSL version (in SSL/TLS offloading context).
    - `intermediate` General-purpose servers with a variety of clients, recommended for almost all systems (Supports Firefox 27, Android 4.4.2, Chrome 31, Edge, IE 11 on Windows 7, Java 8u31, OpenSSL 1.0.1, Opera 20, and Safari 9).
    - `modern` Services with clients that support TLS 1.3 and don't need backward compatibility (Firefox 63, Android 10.0, Chrome 70, Edge 75, Java 11, OpenSSL 1.1.1, Opera 57, and Safari 12.1).
    - `old` Compatible with a number of very old clients, and should be used only as a last resort (Firefox 1, Android 2.3, Chrome 1, Edge 12, IE8 on Windows XP, Java 6, OpenSSL 0.9.8, Opera 5, and Safari 1).
    
    """


@dataclass
class ZonedApiDeleteLbRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    release_ip: bool
    """
    Set true if you don't want to keep this IP address
    """


@dataclass
class ZonedApiMigrateLbRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    type_: str
    """
    Load balancer type (check /lb-types to list all type)
    """


@dataclass
class ZonedApiListIPsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """

    ip_address: Optional[str]
    """
    Use this to search by IP address
    """

    organization_id: Optional[str]
    """
    Filter IPs by organization id
    """

    project_id: Optional[str]
    """
    Filter IPs by project ID
    """


@dataclass
class ZonedApiCreateIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    organization_id: Optional[str]
    """
    Owner of resources.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Assign the resource to a project ID.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """

    reverse: Optional[str]
    """
    Reverse domain name
    """


@dataclass
class ZonedApiGetIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    ip_id: str
    """
    IP address ID
    """


@dataclass
class ZonedApiReleaseIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    ip_id: str
    """
    IP address ID
    """


@dataclass
class ZonedApiUpdateIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    ip_id: str
    """
    IP address ID
    """

    reverse: Optional[str]
    """
    Reverse DNS
    """


@dataclass
class ZonedApiListBackendsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    name: Optional[str]
    """
    Use this to search by name
    """

    order_by: Optional[ListBackendsRequestOrderBy]
    """
    Response order
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """


@dataclass
class ZonedApiCreateBackendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    name: Optional[str]
    """
    Resource name
    """

    forward_protocol: Optional[Protocol]
    """
    Backend protocol. TCP or HTTP
    """

    forward_port: int
    """
    User sessions will be forwarded to this port of backend servers
    """

    forward_port_algorithm: Optional[ForwardPortAlgorithm]
    """
    Load balancing algorithm
    """

    sticky_sessions: Optional[StickySessionsType]
    """
    Enables cookie-based session persistence
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for sticky sessions
    """

    health_check: HealthCheck
    """
    See the Healthcheck object description
    """

    server_ip: List[str]
    """
    Backend server IP addresses list (IPv4 or IPv6)
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field !
    :deprecated
    """

    timeout_server: Optional[str]
    """
    Maximum server connection inactivity time (allowed time the server has to process the request)
    """

    timeout_connect: Optional[str]
    """
    Maximum initial server connection establishment time
    """

    timeout_tunnel: Optional[str]
    """
    Maximum tunnel inactivity time after Websocket is established (take precedence over client and server timeout)
    """

    on_marked_down_action: OnMarkedDownAction
    """
    Modify what occurs when a backend server is marked down
    """

    proxy_protocol: ProxyProtocol
    """
    The PROXY protocol informs the other end about the incoming connection, so that it can know the client's address or the public address it accessed to, whatever the upper layer protocol.
    
    * `proxy_protocol_none` Disable proxy protocol.
    * `proxy_protocol_v1` Version one (text format).
    * `proxy_protocol_v2` Version two (binary format).
    * `proxy_protocol_v2_ssl` Version two with SSL connection.
    * `proxy_protocol_v2_ssl_cn` Version two with SSL connection and common name information.
    
    """

    failover_host: Optional[str]
    """
    Only the host part of the Scaleway S3 bucket website is expected.
    E.g. `failover-website.s3-website.fr-par.scw.cloud` if your bucket website URL is `https://failover-website.s3-website.fr-par.scw.cloud/`.
    
    """

    ssl_bridging: Optional[bool]
    """
    Enable SSL between load balancer and backend servers
    """

    ignore_ssl_server_verify: Optional[bool]
    """
    Set to true to ignore server certificate verification
    """


@dataclass
class ZonedApiGetBackendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    backend_id: str
    """
    Backend ID
    """


@dataclass
class ZonedApiUpdateBackendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    backend_id: str
    """
    Backend ID to update
    """

    name: str
    """
    Resource name
    """

    forward_protocol: Optional[Protocol]
    """
    Backend protocol. TCP or HTTP
    """

    forward_port: int
    """
    User sessions will be forwarded to this port of backend servers
    """

    forward_port_algorithm: Optional[ForwardPortAlgorithm]
    """
    Load balancing algorithm
    """

    sticky_sessions: Optional[StickySessionsType]
    """
    Enable cookie-based session persistence
    """

    sticky_sessions_cookie_name: str
    """
    Cookie name for sticky sessions
    """

    send_proxy_v2: Optional[bool]
    """
    Deprecated in favor of proxy_protocol field!
    :deprecated
    """

    timeout_server: Optional[str]
    """
    Maximum server connection inactivity time (allowed time the server has to process the request)
    """

    timeout_connect: Optional[str]
    """
    Maximum initial server connection establishment time
    """

    timeout_tunnel: Optional[str]
    """
    Maximum tunnel inactivity time after Websocket is established (take precedence over client and server timeout)
    """

    on_marked_down_action: OnMarkedDownAction
    """
    Modify what occurs when a backend server is marked down
    """

    proxy_protocol: ProxyProtocol
    """
    The PROXY protocol informs the other end about the incoming connection, so that it can know the client's address or the public address it accessed to, whatever the upper layer protocol is.
    
    * `proxy_protocol_none` Disable proxy protocol.
    * `proxy_protocol_v1` Version one (text format).
    * `proxy_protocol_v2` Version two (binary format).
    * `proxy_protocol_v2_ssl` Version two with SSL connection.
    * `proxy_protocol_v2_ssl_cn` Version two with SSL connection and common name information.
    
    """

    failover_host: Optional[str]
    """
    Only the host part of the Scaleway S3 bucket website is expected.
    Example: `failover-website.s3-website.fr-par.scw.cloud` if your bucket website URL is `https://failover-website.s3-website.fr-par.scw.cloud/`.
    
    """

    ssl_bridging: Optional[bool]
    """
    Enable SSL between load balancer and backend servers
    """

    ignore_ssl_server_verify: Optional[bool]
    """
    Set to true to ignore server certificate verification
    """


@dataclass
class ZonedApiDeleteBackendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    backend_id: str
    """
    ID of the backend to delete
    """


@dataclass
class ZonedApiAddBackendServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    backend_id: str
    """
    Backend ID
    """

    server_ip: List[str]
    """
    Set all IPs to add on your backend
    """


@dataclass
class ZonedApiRemoveBackendServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    backend_id: str
    """
    Backend ID
    """

    server_ip: List[str]
    """
    Set all IPs to remove of your backend
    """


@dataclass
class ZonedApiSetBackendServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    backend_id: str
    """
    Backend ID
    """

    server_ip: List[str]
    """
    Set all IPs to add on your backend and remove all other
    """


@dataclass
class ZonedApiUpdateHealthCheckRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    backend_id: str
    """
    Backend ID
    """

    port: int
    """
    Specify the port used to health check
    """

    check_delay: str
    """
    Time between two consecutive health checks
    """

    check_timeout: str
    """
    Maximum time a backend server has to reply to the health check
    """

    check_max_retries: int
    """
    Number of consecutive unsuccessful health checks, after which the server will be considered dead
    """

    mysql_config: Optional[HealthCheckMysqlConfig]
    """
    The check requires MySQL >=3.22, for older version, please use TCP check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
    """

    ldap_config: Optional[HealthCheckLdapConfig]
    """
    The response is analyzed to find an LDAPv3 response message.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
    """

    redis_config: Optional[HealthCheckRedisConfig]
    """
    The response is analyzed to find the +PONG response message.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
    """

    pgsql_config: Optional[HealthCheckPgsqlConfig]
    """
    PostgreSQL health check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
    """

    tcp_config: Optional[HealthCheckTcpConfig]
    """
    Basic TCP health check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
    """

    http_config: Optional[HealthCheckHttpConfig]
    """
    HTTP health check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
    """

    https_config: Optional[HealthCheckHttpsConfig]
    """
    HTTPS health check.
    
    One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
    """

    check_send_proxy: bool
    """
    It defines whether the health check should be done considering the proxy protocol
    """


@dataclass
class ZonedApiListFrontendsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    name: Optional[str]
    """
    Use this to search by name
    """

    order_by: Optional[ListFrontendsRequestOrderBy]
    """
    Response order
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """


@dataclass
class ZonedApiCreateFrontendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    name: Optional[str]
    """
    Resource name
    """

    inbound_port: int
    """
    TCP port to listen on the front side
    """

    backend_id: str
    """
    Backend ID
    """

    timeout_client: Optional[str]
    """
    Set the maximum inactivity time on the client side
    """

    certificate_id: Optional[str]
    """
    Certificate ID, deprecated in favor of certificate_ids array !
    :deprecated
    """

    certificate_ids: Optional[List[str]]
    """
    List of certificate IDs to bind on the frontend
    """

    enable_http3: bool
    """
    Activate HTTP 3 protocol (beta)
    """


@dataclass
class ZonedApiGetFrontendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    frontend_id: str
    """
    Frontend ID
    """


@dataclass
class ZonedApiUpdateFrontendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    frontend_id: str
    """
    Frontend ID
    """

    name: str
    """
    Resource name
    """

    inbound_port: int
    """
    TCP port to listen on the front side
    """

    backend_id: str
    """
    Backend ID
    """

    timeout_client: Optional[str]
    """
    Client session maximum inactivity time
    """

    certificate_id: Optional[str]
    """
    Certificate ID, deprecated in favor of `certificate_ids` array!
    :deprecated
    """

    certificate_ids: Optional[List[str]]
    """
    List of certificate IDs to bind on the frontend
    """

    enable_http3: bool
    """
    Activate HTTP 3 protocol (beta)
    """


@dataclass
class ZonedApiDeleteFrontendRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    frontend_id: str
    """
    Frontend ID to delete
    """


@dataclass
class ZonedApiListRoutesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    order_by: Optional[ListRoutesRequestOrderBy]
    """
    Response order
    """

    page_size: Optional[int]
    """
    The number of items to return
    """

    page: Optional[int]
    """
    Page number
    """

    frontend_id: Optional[str]


@dataclass
class ZonedApiCreateRouteRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    frontend_id: str
    """
    Origin of redirection
    """

    backend_id: str
    """
    Destination of destination
    """

    match: Optional[RouteMatch]
    """
    Value to match a redirection
    """


@dataclass
class ZonedApiGetRouteRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    route_id: str
    """
    Id of route to get
    """


@dataclass
class ZonedApiUpdateRouteRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    route_id: str
    """
    Route id to update
    """

    backend_id: str
    """
    Backend id of redirection
    """

    match: Optional[RouteMatch]
    """
    Value to match a redirection
    """


@dataclass
class ZonedApiDeleteRouteRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    route_id: str
    """
    Route id to delete
    """


@dataclass
class ZonedApiGetLbStatsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """


@dataclass
class ZonedApiListBackendStatsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """


@dataclass
class ZonedApiListAclsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    frontend_id: str
    """
    ID of your frontend
    """

    order_by: Optional[ListAclRequestOrderBy]
    """
    Response order
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """

    name: Optional[str]
    """
    Filter acl per name
    """


@dataclass
class ZonedApiCreateAclRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    frontend_id: str
    """
    ID of your frontend
    """

    name: Optional[str]
    """
    Name of your ACL ressource
    """

    action: AclAction
    """
    Action to undertake when an ACL filter matches
    """

    match: AclMatch
    """
    The ACL match rule. You can have one of those three cases:
    
      - `ip_subnet` is defined
      - `http_filter` and `http_filter_value` are defined
      - `ip_subnet`, `http_filter` and `http_filter_value` are defined
    
    """

    index: int
    """
    Order between your Acls (ascending order, 0 is first acl executed)
    """

    description: str
    """
    Description of your ACL ressource
    """


@dataclass
class ZonedApiGetAclRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    acl_id: str
    """
    ID of your ACL ressource
    """


@dataclass
class ZonedApiUpdateAclRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    acl_id: str
    """
    ID of your ACL ressource
    """

    name: str
    """
    Name of your ACL ressource
    """

    action: AclAction
    """
    Action to undertake when an ACL filter matches
    """

    match: AclMatch
    """
    The ACL match rule. At least `ip_subnet` or `http_filter` and `http_filter_value` are required
    """

    index: int
    """
    Order between your Acls (ascending order, 0 is first acl executed)
    """

    description: Optional[str]
    """
    Description of your ACL ressource
    """


@dataclass
class ZonedApiDeleteAclRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    acl_id: str
    """
    ID of your ACL ressource
    """


@dataclass
class ZonedApiSetAclsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    frontend_id: str
    """
    The Frontend to change ACL to
    """

    acls: List[AclSpec]
    """
    Array of ACLs to erease the existing ACLs
    """


@dataclass
class ZonedApiCreateCertificateRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    name: Optional[str]
    """
    Certificate name
    """

    letsencrypt: Optional[CreateCertificateRequestLetsencryptConfig]
    """
    Let's Encrypt type.
    
    One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
    """

    custom_certificate: Optional[CreateCertificateRequestCustomCertificate]
    """
    Custom import certificate.
    
    One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
    """


@dataclass
class ZonedApiListCertificatesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    order_by: Optional[ListCertificatesRequestOrderBy]
    """
    Response order
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """

    name: Optional[str]
    """
    Use this to search by name
    """


@dataclass
class ZonedApiGetCertificateRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    certificate_id: str
    """
    Certificate ID
    """


@dataclass
class ZonedApiUpdateCertificateRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    certificate_id: str
    """
    Certificate ID
    """

    name: str
    """
    Certificate name
    """


@dataclass
class ZonedApiDeleteCertificateRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    certificate_id: str
    """
    Certificate ID
    """


@dataclass
class ZonedApiListLbTypesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """


@dataclass
class ZonedApiCreateSubscriberRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    name: str
    """
    Subscriber name
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
    Owner of resources.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Assign the resource to a project ID.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """


@dataclass
class ZonedApiGetSubscriberRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    subscriber_id: str
    """
    Subscriber ID
    """


@dataclass
class ZonedApiListSubscriberRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    order_by: Optional[ListSubscriberRequestOrderBy]
    """
    Response order
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    The number of items to return
    """

    name: str
    """
    Use this to search by name
    """

    organization_id: Optional[str]
    """
    Filter Subscribers by organization ID
    """

    project_id: Optional[str]
    """
    Filter Subscribers by project ID
    """


@dataclass
class ZonedApiUpdateSubscriberRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    subscriber_id: str
    """
    Assign the resource to a project IDs
    """

    name: str
    """
    Subscriber name
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


@dataclass
class ZonedApiDeleteSubscriberRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    subscriber_id: str
    """
    Subscriber ID
    """


@dataclass
class ZonedApiSubscribeToLbRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    subscriber_id: str
    """
    Subscriber ID
    """


@dataclass
class ZonedApiUnsubscribeFromLbRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """


@dataclass
class ZonedApiListLbPrivateNetworksRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    order_by: Optional[ListPrivateNetworksRequestOrderBy]
    """
    Response order
    """

    page_size: Optional[int]
    """
    The number of items to return
    """

    page: Optional[int]
    """
    Page number
    """


@dataclass
class ZonedApiAttachPrivateNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    private_network_id: str
    """
    Set your instance private network id
    """

    static_config: Optional[PrivateNetworkStaticConfig]
    """
    Define two local ip address of your choice for each load balancer instance.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config' could be set.
    """

    dhcp_config: Optional[PrivateNetworkDHCPConfig]
    """
    Set to true if you want to let DHCP assign IP addresses.
    
    One-of ('config'): at most one of 'static_config', 'dhcp_config' could be set.
    """


@dataclass
class ZonedApiDetachPrivateNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    lb_id: str
    """
    Load balancer ID
    """

    private_network_id: str
    """
    Set your instance private network id
    """
