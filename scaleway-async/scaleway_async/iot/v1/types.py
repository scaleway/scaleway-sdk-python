# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from scaleway_core.bridge import (
    Region,
    TimeSeries,
)


class DeviceMessageFiltersRulePolicy(str, Enum):
    UNKNOWN = "unknown"
    ACCEPT = "accept"
    REJECT = "reject"

    def __str__(self) -> str:
        return str(self.value)


class DeviceStatus(str, Enum):
    UNKNOWN = "unknown"
    ERROR = "error"
    ENABLED = "enabled"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)


class HubProductPlan(str, Enum):
    PLAN_UNKNOWN = "plan_unknown"
    PLAN_SHARED = "plan_shared"
    PLAN_DEDICATED = "plan_dedicated"
    PLAN_HA = "plan_ha"

    def __str__(self) -> str:
        return str(self.value)


class HubStatus(str, Enum):
    UNKNOWN = "unknown"
    ERROR = "error"
    ENABLING = "enabling"
    READY = "ready"
    DISABLING = "disabling"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)


class ListDevicesRequestOrderBy(str, Enum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"
    HUB_ID_ASC = "hub_id_asc"
    HUB_ID_DESC = "hub_id_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    ALLOW_INSECURE_ASC = "allow_insecure_asc"
    ALLOW_INSECURE_DESC = "allow_insecure_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListHubsRequestOrderBy(str, Enum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"
    PRODUCT_PLAN_ASC = "product_plan_asc"
    PRODUCT_PLAN_DESC = "product_plan_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListNetworksRequestOrderBy(str, Enum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    TYPE_ASC = "type_asc"
    TYPE_DESC = "type_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRoutesRequestOrderBy(str, Enum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    HUB_ID_ASC = "hub_id_asc"
    HUB_ID_DESC = "hub_id_desc"
    TYPE_ASC = "type_asc"
    TYPE_DESC = "type_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class NetworkNetworkType(str, Enum):
    UNKNOWN = "unknown"
    SIGFOX = "sigfox"
    REST = "rest"

    def __str__(self) -> str:
        return str(self.value)


class NullValue(str, Enum):
    NULL_VALUE = "NULL_VALUE"

    def __str__(self) -> str:
        return str(self.value)


class RouteDatabaseConfigEngine(str, Enum):
    UNKNOWN = "unknown"
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"

    def __str__(self) -> str:
        return str(self.value)


class RouteRestConfigHttpVerb(str, Enum):
    UNKNOWN = "unknown"
    GET = "get"
    POST = "post"
    PUT = "put"
    PATCH = "patch"
    DELETE = "delete"

    def __str__(self) -> str:
        return str(self.value)


class RouteRouteType(str, Enum):
    UNKNOWN = "unknown"
    S3 = "s3"
    DATABASE = "database"
    REST = "rest"

    def __str__(self) -> str:
        return str(self.value)


class RouteS3ConfigS3Strategy(str, Enum):
    UNKNOWN = "unknown"
    PER_TOPIC = "per_topic"
    PER_MESSAGE = "per_message"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Certificate:
    crt: str

    key: str


@dataclass
class CreateDeviceResponse:
    """
    Create device response
    """

    device: Optional[Device]
    """
    Created device information
    """

    certificate: Optional[Certificate]
    """
    Device certificate
    """


@dataclass
class CreateNetworkResponse:
    """
    Create network response
    """

    network: Optional[Network]
    """
    Created network
    """

    secret: str
    """
    Endpoint Key to keep secret. This cannot be retrieved later
    """


@dataclass
class CreateRouteRequestDatabaseConfig:
    host: str

    port: int

    dbname: str

    username: str

    password: str

    query: str

    engine: RouteDatabaseConfigEngine


@dataclass
class CreateRouteRequestRestConfig:
    verb: RouteRestConfigHttpVerb

    uri: str

    headers: Dict[str, str]


@dataclass
class CreateRouteRequestS3Config:
    bucket_region: str

    bucket_name: str

    object_prefix: str

    strategy: RouteS3ConfigS3Strategy


@dataclass
class Device:
    """
    Device
    """

    id: str
    """
    Device ID, also used as MQTT Client ID or Username
    """

    name: str
    """
    Device name
    """

    description: str
    """
    Device description
    """

    status: DeviceStatus
    """
    Device status
    """

    hub_id: str
    """
    Hub ID
    """

    last_activity_at: Optional[datetime]
    """
    Device last connection/activity date
    """

    is_connected: bool
    """
    Whether the device is connected to the Hub or not
    """

    allow_insecure: bool
    """
    Whether to allow device to connect without TLS mutual authentication
    """

    allow_multiple_connections: bool
    """
    Whether to allow multiple physical devices to connect with this device's credentials
    """

    message_filters: Optional[DeviceMessageFilters]
    """
    Filter-sets to restrict the topics the device can publish/subscribe to
    """

    has_custom_certificate: bool
    """
    Assigning a custom certificate allows a device to authenticate using that specific certificate without checking the hub's CA certificate.
    """

    created_at: Optional[datetime]
    """
    Device add date
    """

    updated_at: Optional[datetime]
    """
    Device last modification date
    """


@dataclass
class DeviceMessageFilters:
    """
    Device. message filters
    """

    publish: Optional[DeviceMessageFiltersRule]
    """
    Filtering rule to restrict topics the device can publish to
    """

    subscribe: Optional[DeviceMessageFiltersRule]
    """
    Filtering rule to restrict topics the device can subscribe to
    """


@dataclass
class DeviceMessageFiltersRule:
    """
    Device. message filters. rule
    """

    policy: DeviceMessageFiltersRulePolicy
    """
    If accept, the set will accept all topics in the topics list, but no other.
    If reject, the set will deny all topics in the topics list, but all others will be allowed.
    
    """

    topics: Optional[List[str]]
    """
    List of topics to accept or reject. It must be valid MQTT topics and up to 65535 characters
    """


@dataclass
class GetDeviceCertificateResponse:
    """
    Get device certificate response
    """

    device: Optional[Device]
    """
    Created device information
    """

    certificate_pem: str
    """
    Device certificate
    """


@dataclass
class GetDeviceMetricsResponse:
    """
    Get device metrics response
    """

    metrics: List[TimeSeries]
    """
    Metrics for a device over the requested period
    """


@dataclass
class GetHubCAResponse:
    ca_cert_pem: str


@dataclass
class GetHubMetricsResponse:
    """
    Get hub metrics response
    """

    metrics: List[TimeSeries]
    """
    Metrics for a hub over the requested period
    """


@dataclass
class Hub:
    """
    Hub
    """

    id: str
    """
    Hub ID
    """

    name: str
    """
    Hub name
    """

    status: HubStatus
    """
    Current status of the Hub
    """

    product_plan: HubProductPlan
    """
    Hub feature set
    """

    enabled: bool
    """
    Whether the hub has been enabled
    """

    device_count: int
    """
    Number of registered devices
    """

    connected_device_count: int
    """
    Number of currently connected devices
    """

    endpoint: str
    """
    Devices should be connected to this host, port may be 1883 (MQTT), 8883 (MQTT over TLS), 80 (MQTT over Websocket) or 443 (MQTT over Websocket over TLS).
    """

    disable_events: bool
    """
    Disable Hub events
    """

    events_topic_prefix: str
    """
    Hub events topic prefix
    """

    region: Region
    """
    Region of the Hub
    """

    created_at: Optional[datetime]
    """
    Hub creation date
    """

    updated_at: Optional[datetime]
    """
    Hub last modification date
    """

    project_id: str
    """
    Project owning the resource
    """

    organization_id: str
    """
    Organization owning the resource
    """

    enable_device_auto_provisioning: bool
    """
    When an unknown device connects to your hub using a valid certificate chain, it will be automatically provisioned inside your hub. The hub uses the common name of the device certifcate to find out if a device with the same name already exists. This setting can only be enabled on a hub with a custom certificate authority.
    """

    has_custom_ca: bool
    """
    After creating a hub, this flag is set to False as the hub certificates are managed by Scaleway. Once a custom certificate authority is installed, this flag will be set to true.
    """

    twins_graphite_config: Optional[HubTwinsGraphiteConfig]
    """
    BETA - not implemented yet.
    
    One-of ('twins_db_config'): at most one of 'twins_graphite_config' could be set.
    """


@dataclass
class HubTwinsGraphiteConfig:
    push_uri: str


@dataclass
class ListDevicesResponse:
    """
    List devices response
    """

    total_count: int
    """
    Total number of devices
    """

    devices: List[Device]
    """
    A page of devices
    """


@dataclass
class ListHubsResponse:
    """
    List hubs response
    """

    total_count: int
    """
    Total number of hubs
    """

    hubs: List[Hub]
    """
    A page of hubs
    """


@dataclass
class ListNetworksResponse:
    """
    List networks response
    """

    total_count: int
    """
    Total number of Networks
    """

    networks: List[Network]
    """
    A page of networks
    """


@dataclass
class ListRoutesResponse:
    """
    List routes response
    """

    total_count: int
    """
    Total number of routes
    """

    routes: List[RouteSummary]
    """
    A page of routes
    """


@dataclass
class ListTwinDocumentsResponse:
    """
    List twin documents response
    """

    documents: List[ListTwinDocumentsResponseDocumentSummary]
    """
    Twin's document list
    """


@dataclass
class ListTwinDocumentsResponseDocumentSummary:
    """
    List twin documents response. document summary
    """

    document_name: str
    """
    Document's name
    """


@dataclass
class Network:
    """
    Network
    """

    id: str
    """
    Network ID
    """

    name: str
    """
    Network name
    """

    type_: NetworkNetworkType
    """
    Type of network to connect with
    """

    endpoint: str
    """
    Endpoint to use for interacting with the network
    """

    hub_id: str
    """
    Hub ID to connect the Network to
    """

    created_at: Optional[datetime]
    """
    Network creation date
    """

    topic_prefix: str
    """
    This prefix will be prepended to all topics for this Network.
    """


@dataclass
class RenewDeviceCertificateResponse:
    """
    Renew device certificate response
    """

    device: Optional[Device]
    """
    Created device information
    """

    certificate: Optional[Certificate]
    """
    Device certificate
    """


@dataclass
class Route:
    """
    Route
    """

    id: str
    """
    Route ID
    """

    name: str
    """
    Route name
    """

    hub_id: str
    """
    ID of the route's hub
    """

    topic: str
    """
    Topic the route subscribes to. It must be a valid MQTT topic and up to 65535 characters
    """

    type_: RouteRouteType
    """
    Route type
    """

    created_at: Optional[datetime]
    """
    Route creation date
    """

    s3_config: Optional[RouteS3Config]
    """
    When using S3 Route, S3-specific configuration fields.
    
    One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
    """

    db_config: Optional[RouteDatabaseConfig]
    """
    When using Database Route, DB-specific configuration fields.
    
    One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
    """

    rest_config: Optional[RouteRestConfig]
    """
    When using Rest Route, Rest-specific configuration fields.
    
    One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
    """

    updated_at: Optional[datetime]
    """
    Route last update date
    """


@dataclass
class RouteDatabaseConfig:
    """
    Route. database config
    """

    engine: RouteDatabaseConfigEngine
    """
    Database engine the route will connect to. If not specified, will default to 'PostgreSQL'
    """

    host: str
    """
    Database host
    """

    port: int
    """
    Database port
    """

    dbname: str
    """
    Database name
    """

    username: str
    """
    Database username. Make sure this account can execute the provided query
    """

    password: str
    """
    Database password
    """

    query: str
    """
    SQL query to be executed ($TOPIC and $PAYLOAD variables are available, see documentation)
    """


@dataclass
class RouteRestConfig:
    """
    Route. rest config
    """

    verb: RouteRestConfigHttpVerb
    """
    HTTP Verb used to call REST URI
    """

    uri: str
    """
    URI of the REST endpoint
    """

    headers: Dict[str, str]
    """
    HTTP call extra headers
    """


@dataclass
class RouteS3Config:
    """
    Route.s3 config
    """

    bucket_region: str
    """
    Region of the S3 route's destination bucket (eg 'fr-par')
    """

    bucket_name: str
    """
    Name of the S3 route's destination bucket
    """

    object_prefix: str
    """
    Optional string to prefix object names with
    """

    strategy: RouteS3ConfigS3Strategy
    """
    How the S3 route's objects will be created: one per topic or one per message
    """


@dataclass
class RouteSummary:
    """
    Route summary
    """

    id: str
    """
    Route ID
    """

    name: str
    """
    Route name
    """

    hub_id: str
    """
    ID of the route's hub
    """

    topic: str
    """
    Topic the route subscribes to. It must be a valid MQTT topic and up to 65535 characters
    """

    type_: RouteRouteType
    """
    Route type
    """

    created_at: Optional[datetime]
    """
    Route creation date
    """

    updated_at: Optional[datetime]
    """
    Route last update date
    """


@dataclass
class SetDeviceCertificateResponse:
    device: Optional[Device]

    certificate_pem: str


@dataclass
class TwinDocument:
    """
    Twin document
    """

    twin_id: str
    """
    Document's parent twin ID
    """

    document_name: str
    """
    Document's name
    """

    version: int
    """
    Document's new version
    """

    data: Optional[Dict[str, Any]]
    """
    Document's new data
    """


@dataclass
class UpdateRouteRequestDatabaseConfig:
    host: Optional[str]

    port: Optional[int]

    dbname: Optional[str]

    username: Optional[str]

    password: Optional[str]

    query: Optional[str]

    engine: RouteDatabaseConfigEngine


@dataclass
class UpdateRouteRequestRestConfig:
    verb: RouteRestConfigHttpVerb

    uri: Optional[str]

    headers: Optional[Dict[str, str]]


@dataclass
class UpdateRouteRequestS3Config:
    bucket_region: Optional[str]

    bucket_name: Optional[str]

    object_prefix: Optional[str]

    strategy: RouteS3ConfigS3Strategy


@dataclass
class ListHubsRequest:
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
    Page size. The maximum value is 100
    """

    order_by: Optional[ListHubsRequestOrderBy]
    """
    Ordering of requested hub
    """

    project_id: Optional[str]
    """
    Filter on project
    """

    organization_id: Optional[str]
    """
    Filter on the organization
    """

    name: Optional[str]
    """
    Filter on the name
    """


@dataclass
class CreateHubRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    name: Optional[str]
    """
    Hub name (up to 255 characters)
    """

    project_id: Optional[str]
    """
    Organization/project owning the resource
    """

    product_plan: Optional[HubProductPlan]
    """
    Hub feature set
    """

    disable_events: Optional[bool]
    """
    Disable Hub events
    """

    events_topic_prefix: Optional[str]
    """
    Hub events topic prefix (default '$SCW/events')
    """

    twins_graphite_config: Optional[HubTwinsGraphiteConfig]
    """
    BETA - not implemented yet.
    
    One-of ('twins_db_config'): at most one of 'twins_graphite_config' could be set.
    """


@dataclass
class GetHubRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    hub_id: str
    """
    Hub ID
    """


@dataclass
class UpdateHubRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    hub_id: str
    """
    Hub ID
    """

    name: Optional[str]
    """
    Hub name (up to 255 characters)
    """

    product_plan: HubProductPlan
    """
    Hub feature set
    """

    disable_events: Optional[bool]
    """
    Disable Hub events
    """

    events_topic_prefix: Optional[str]
    """
    Hub events topic prefix
    """

    enable_device_auto_provisioning: Optional[bool]
    """
    Enable device auto provisioning
    """

    twins_graphite_config: Optional[HubTwinsGraphiteConfig]
    """
    BETA - not implemented yet.
    
    One-of ('twins_db_config'): at most one of 'twins_graphite_config' could be set.
    """


@dataclass
class EnableHubRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    hub_id: str
    """
    Hub ID
    """


@dataclass
class DisableHubRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    hub_id: str
    """
    Hub ID
    """


@dataclass
class DeleteHubRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    hub_id: str
    """
    Hub ID
    """

    delete_devices: Optional[bool]
    """
    Force deletion of devices added to this hub instead of rejecting operation
    """


@dataclass
class GetHubMetricsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    hub_id: str
    """
    Hub ID
    """

    start_date: datetime
    """
    Start date used to compute the best scale for the returned metrics
    """


@dataclass
class SetHubCARequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    hub_id: str
    """
    Hub ID
    """

    ca_cert_pem: str
    """
    The CA's PEM-encoded certificate
    """

    challenge_cert_pem: str
    """
    The challenge is a PEM-encoded certificate to prove the possession of the CA. It must be signed by the CA, and have a Common Name equal to the Hub ID.
    """


@dataclass
class GetHubCARequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    hub_id: str


@dataclass
class ListDevicesRequest:
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
    Page size. The maximum value is 100
    """

    order_by: Optional[ListDevicesRequestOrderBy]
    """
    Ordering of requested devices
    """

    name: Optional[str]
    """
    Filter on the name
    """

    hub_id: Optional[str]
    """
    Filter on the hub
    """

    allow_insecure: Optional[bool]
    """
    Filter on the allow_insecure flag
    """

    status: Optional[DeviceStatus]
    """
    Device status (enabled, disabled, etc.)
    """


@dataclass
class CreateDeviceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    name: Optional[str]
    """
    Device name
    """

    hub_id: str
    """
    ID of the device's hub
    """

    allow_insecure: bool
    """
    Allow plain and server-authenticated SSL connections in addition to mutually-authenticated ones
    """

    allow_multiple_connections: bool
    """
    Allow multiple physical devices to connect with this device's credentials
    """

    message_filters: Optional[DeviceMessageFilters]
    """
    Filter-sets to authorize or deny the device to publish/subscribe to specific topics
    """

    description: Optional[str]
    """
    Device description
    """


@dataclass
class GetDeviceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    device_id: str
    """
    Device ID
    """


@dataclass
class UpdateDeviceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    device_id: str
    """
    Device ID
    """

    description: Optional[str]
    """
    Device description
    """

    allow_insecure: Optional[bool]
    """
    Allow plain and server-authenticated SSL connections in addition to mutually-authenticated ones
    """

    allow_multiple_connections: Optional[bool]
    """
    Allow multiple physical devices to connect with this device's credentials
    """

    message_filters: Optional[DeviceMessageFilters]
    """
    Filter-sets to restrict the topics the device can publish/subscribe to
    """

    hub_id: Optional[str]
    """
    Change Hub for this device, additional fees may apply, see IoT Hub pricing
    """


@dataclass
class EnableDeviceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    device_id: str
    """
    Device ID
    """


@dataclass
class DisableDeviceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    device_id: str
    """
    Device ID
    """


@dataclass
class RenewDeviceCertificateRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    device_id: str
    """
    Device ID
    """


@dataclass
class SetDeviceCertificateRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    device_id: str
    """
    Device ID
    """

    certificate_pem: str
    """
    The PEM-encoded custom certificate
    """


@dataclass
class GetDeviceCertificateRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    device_id: str
    """
    Device ID
    """


@dataclass
class DeleteDeviceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    device_id: str
    """
    Device ID
    """


@dataclass
class GetDeviceMetricsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    device_id: str
    """
    Device ID
    """

    start_date: datetime
    """
    Start date used to compute the best scale for the returned metrics
    """


@dataclass
class ListRoutesRequest:
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
    Page size. The maximum value is 100
    """

    order_by: Optional[ListRoutesRequestOrderBy]
    """
    Ordering of requested routes
    """

    hub_id: Optional[str]
    """
    Filter on the hub
    """

    name: Optional[str]
    """
    Filter on route's name
    """


@dataclass
class CreateRouteRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    name: Optional[str]
    """
    Route name
    """

    hub_id: str
    """
    ID of the route's hub
    """

    topic: str
    """
    Topic the route subscribes to. It must be a valid MQTT topic and up to 65535 characters
    """

    s3_config: Optional[CreateRouteRequestS3Config]
    """
    If creating S3 Route, S3-specific configuration fields.
    
    One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
    """

    db_config: Optional[CreateRouteRequestDatabaseConfig]
    """
    If creating Database Route, DB-specific configuration fields.
    
    One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
    """

    rest_config: Optional[CreateRouteRequestRestConfig]
    """
    If creating Rest Route, Rest-specific configuration fields.
    
    One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
    """


@dataclass
class UpdateRouteRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    route_id: str
    """
    Route id
    """

    name: Optional[str]
    """
    Route name
    """

    topic: Optional[str]
    """
    Topic the route subscribes to. It must be a valid MQTT topic and up to 65535 characters
    """

    s3_config: Optional[UpdateRouteRequestS3Config]
    """
    When updating S3 Route, S3-specific configuration fields.
    
    One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
    """

    db_config: Optional[UpdateRouteRequestDatabaseConfig]
    """
    When updating Database Route, DB-specific configuration fields.
    
    One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
    """

    rest_config: Optional[UpdateRouteRequestRestConfig]
    """
    When updating Rest Route, Rest-specific configuration fields.
    
    One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
    """


@dataclass
class GetRouteRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    route_id: str
    """
    Route ID
    """


@dataclass
class DeleteRouteRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    route_id: str
    """
    Route ID
    """


@dataclass
class ListNetworksRequest:
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
    Page size. The maximum value is 100
    """

    order_by: Optional[ListNetworksRequestOrderBy]
    """
    Ordering of requested routes
    """

    name: Optional[str]
    """
    Filter on Network name
    """

    hub_id: Optional[str]
    """
    Filter on the hub
    """

    topic_prefix: Optional[str]
    """
    Filter on the topic prefix
    """


@dataclass
class CreateNetworkRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    name: Optional[str]
    """
    Network name
    """

    type_: Optional[NetworkNetworkType]
    """
    Type of network to connect with
    """

    hub_id: str
    """
    Hub ID to connect the Network to
    """

    topic_prefix: str
    """
    Topic prefix for the Network
    """


@dataclass
class GetNetworkRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    network_id: str
    """
    Network ID
    """


@dataclass
class DeleteNetworkRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    network_id: str
    """
    Network ID
    """


@dataclass
class GetTwinDocumentRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    twin_id: str
    """
    Twin ID
    """

    document_name: str
    """
    Document name
    """


@dataclass
class PutTwinDocumentRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    twin_id: str
    """
    Twin ID
    """

    document_name: str
    """
    Document name
    """

    version: Optional[int]
    """
    If set, ensures that the document's current version matches before persisting the update.
    """

    data: Optional[Dict[str, Any]]
    """
    The new data that will replace the contents of the document.
    """


@dataclass
class PatchTwinDocumentRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    twin_id: str
    """
    Twin ID
    """

    document_name: str
    """
    Document name
    """

    version: Optional[int]
    """
    If set, ensures that the document's current version matches before persisting the update.
    """

    data: Optional[Dict[str, Any]]
    """
    A json data that will be applied on the document's current data.
    Patching rules:
    * The patch goes recursively through the patch objects.
    * If the patch object property is null, then it is removed from the final object.
    * If the patch object property is a value (number, strings, bool, arrays), it is replaced.
    * If the patch object property is an object, the previous rules will be applied recursively on it.
    
    """


@dataclass
class DeleteTwinDocumentRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    twin_id: str
    """
    Twin ID
    """

    document_name: str
    """
    Document name
    """


@dataclass
class ListTwinDocumentsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    twin_id: str
    """
    Twin ID
    """


@dataclass
class DeleteTwinDocumentsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    twin_id: str
    """
    Twin ID
    """
