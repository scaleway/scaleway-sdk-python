# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
    TimeSeries,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class DeviceMessageFiltersRulePolicy(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    ACCEPT = "accept"
    REJECT = "reject"

    def __str__(self) -> str:
        return str(self.value)


class DeviceStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    ERROR = "error"
    ENABLED = "enabled"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)


class HubProductPlan(str, Enum, metaclass=StrEnumMeta):
    PLAN_UNKNOWN = "plan_unknown"
    PLAN_SHARED = "plan_shared"
    PLAN_DEDICATED = "plan_dedicated"
    PLAN_HA = "plan_ha"

    def __str__(self) -> str:
        return str(self.value)


class HubStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    ERROR = "error"
    ENABLING = "enabling"
    READY = "ready"
    DISABLING = "disabling"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)


class ListDevicesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
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


class ListHubsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
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


class ListNetworksRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    TYPE_ASC = "type_asc"
    TYPE_DESC = "type_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRoutesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
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


class NetworkNetworkType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    SIGFOX = "sigfox"
    REST = "rest"

    def __str__(self) -> str:
        return str(self.value)


class RouteDatabaseConfigEngine(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"

    def __str__(self) -> str:
        return str(self.value)


class RouteRestConfigHttpVerb(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    GET = "get"
    POST = "post"
    PUT = "put"
    PATCH = "patch"
    DELETE = "delete"

    def __str__(self) -> str:
        return str(self.value)


class RouteRouteType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    S3 = "s3"
    DATABASE = "database"
    REST = "rest"

    def __str__(self) -> str:
        return str(self.value)


class RouteS3ConfigS3Strategy(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    PER_TOPIC = "per_topic"
    PER_MESSAGE = "per_message"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class DeviceMessageFiltersRule:
    policy: DeviceMessageFiltersRulePolicy
    """
    If set to `accept`, all topics in the topics list will be allowed, with all other topics being denied.
If set to `reject`, all topics in the topics list will be denied, with all other topics being allowed.
    """

    topics: Optional[list[str]] = field(default_factory=list)
    """
    List of topics to accept or reject. It must be valid MQTT topics and up to 65535 characters.
    """


@dataclass
class DeviceMessageFilters:
    publish: Optional[DeviceMessageFiltersRule] = None
    """
    Filtering rule to restrict topics the device can publish to.
    """

    subscribe: Optional[DeviceMessageFiltersRule] = None
    """
    Filtering rule to restrict topics the device can subscribe to.
    """


@dataclass
class HubTwinsGraphiteConfig:
    push_uri: str


@dataclass
class Certificate:
    crt: str
    key: str


@dataclass
class Device:
    id: str
    """
    Device ID, also used as MQTT Client ID or username.
    """

    name: str
    """
    Device name.
    """

    description: str
    """
    Device description.
    """

    status: DeviceStatus
    """
    Device status.
    """

    hub_id: str
    """
    Hub ID.
    """

    is_connected: bool
    """
    Defines whether the device is connected to the Hub.
    """

    allow_insecure: bool
    """
    Defines whether to allow the device to connect to the Hub without TLS mutual authentication.
    """

    allow_multiple_connections: bool
    """
    Defines whether to allow multiple physical devices to connect to the Hub with this device's credentials.
    """

    has_custom_certificate: bool
    """
    Assigning a custom certificate allows a device to authenticate using that specific certificate without checking the Hub's CA certificate.
    """

    region: ScwRegion
    """
    Region of the device.
    """

    last_activity_at: Optional[datetime] = None
    """
    Last connection/activity date of a device.
    """

    message_filters: Optional[DeviceMessageFilters] = None
    """
    Filter-sets to restrict the topics the device can publish/subscribe to.
    """

    created_at: Optional[datetime] = None
    """
    Date at which the device was added.
    """

    updated_at: Optional[datetime] = None
    """
    Date at which the device was last modified.
    """


@dataclass
class Network:
    id: str
    """
    Network ID.
    """

    name: str
    """
    Network name.
    """

    type_: NetworkNetworkType
    """
    Type of network to connect with.
    """

    endpoint: str
    """
    Endpoint to use for interacting with the network.
    """

    hub_id: str
    """
    Hub ID to connect the Network to.
    """

    topic_prefix: str
    """
    This prefix will be prepended to all topics for this Network.
    """

    region: ScwRegion
    """
    Region of the network.
    """

    created_at: Optional[datetime] = None
    """
    Date at which the network was created.
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
    headers: dict[str, str]


@dataclass
class CreateRouteRequestS3Config:
    bucket_region: str
    bucket_name: str
    object_prefix: str
    strategy: RouteS3ConfigS3Strategy


@dataclass
class Hub:
    id: str
    """
    Hub ID.
    """

    name: str
    """
    Hub name.
    """

    status: HubStatus
    """
    Current status of the Hub.
    """

    product_plan: HubProductPlan
    """
    Hub feature set.
    """

    enabled: bool
    """
    Defines whether the hub has been enabled.
    """

    device_count: int
    """
    Number of registered devices.
    """

    connected_device_count: int
    """
    Number of currently connected devices.
    """

    endpoint: str
    """
    Devices should be connected to this host. Port may be 1883 (MQTT), 8883 (MQTT over TLS), 80 (MQTT over Websocket) or 443 (MQTT over Websocket over TLS).
    """

    disable_events: bool
    """
    Defines whether to disable Hub events.
    """

    events_topic_prefix: str
    """
    Hub events topic prefix.
    """

    region: ScwRegion
    """
    Region of the Hub.
    """

    project_id: str
    """
    Project owning the resource.
    """

    organization_id: str
    """
    Organization owning the resource.
    """

    enable_device_auto_provisioning: bool
    """
    When an unknown device connects to your hub using a valid certificate chain, it will be automatically provisioned inside your Hub. The Hub uses the common name of the device certifcate to find out if a device with the same name already exists. This setting can only be enabled on a hub with a custom certificate authority.
    """

    has_custom_ca: bool
    """
    Flag is automatically set to `false` after Hub creation, as Hub certificates are managed by Scaleway. Once a custom certificate authority is set, the flag will be set to `true`.
    """

    created_at: Optional[datetime] = None
    """
    Hub creation date.
    """

    updated_at: Optional[datetime] = None
    """
    Hub last modification date.
    """

    twins_graphite_config: Optional[HubTwinsGraphiteConfig] = None


@dataclass
class RouteSummary:
    id: str
    """
    Route ID.
    """

    name: str
    """
    Route name.
    """

    hub_id: str
    """
    Hub ID of the route.
    """

    topic: str
    """
    Topic the route subscribes to. It must be a valid MQTT topic and up to 65535 characters.
    """

    type_: RouteRouteType
    """
    Route type.
    """

    region: ScwRegion
    """
    Region of the route.
    """

    created_at: Optional[datetime] = None
    """
    Date at which the route was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date at which the route was last updated.
    """


@dataclass
class ListTwinDocumentsResponseDocumentSummary:
    document_name: str
    """
    Name of the document.
    """


@dataclass
class RouteDatabaseConfig:
    engine: RouteDatabaseConfigEngine
    """
    Database engine the route will connect to. If not specified, the default database will be 'PostgreSQL'.
    """

    host: str
    """
    Database host.
    """

    port: int
    """
    Database port.
    """

    dbname: str
    """
    Database name.
    """

    username: str
    """
    Database username. Make sure this account can execute the provided query.
    """

    password: str
    """
    Database password.
    """

    query: str
    """
    SQL query to be executed ($TOPIC and $PAYLOAD variables are available, see documentation).
    """


@dataclass
class RouteRestConfig:
    verb: RouteRestConfigHttpVerb
    """
    HTTP verb used to call REST URI.
    """

    uri: str
    """
    URI of the REST endpoint.
    """

    headers: dict[str, str]
    """
    HTTP call extra headers.
    """


@dataclass
class RouteS3Config:
    bucket_region: str
    """
    Region of the Amazon S3 route's destination bucket (e.g., 'fr-par').
    """

    bucket_name: str
    """
    Destination bucket name of the Amazon S3 route.
    """

    object_prefix: str
    """
    Optional string to prefix object names with.
    """

    strategy: RouteS3ConfigS3Strategy
    """
    How the Amazon S3 route's objects will be created: one per topic or one per message.
    """


@dataclass
class UpdateRouteRequestDatabaseConfig:
    engine: RouteDatabaseConfigEngine
    host: Optional[str] = None
    port: Optional[int] = None
    dbname: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    query: Optional[str] = None


@dataclass
class UpdateRouteRequestRestConfig:
    verb: RouteRestConfigHttpVerb
    uri: Optional[str] = None
    headers: Optional[dict[str, str]] = field(default_factory=dict)


@dataclass
class UpdateRouteRequestS3Config:
    strategy: RouteS3ConfigS3Strategy
    bucket_region: Optional[str] = None
    bucket_name: Optional[str] = None
    object_prefix: Optional[str] = None


@dataclass
class CreateDeviceRequest:
    hub_id: str
    """
    Hub ID of the device.
    """

    allow_insecure: bool
    """
    Defines whether to allow plain and server-authenticated SSL connections in addition to mutually-authenticated ones.
    """

    allow_multiple_connections: bool
    """
    Defines whether to allow multiple physical devices to connect with this device's credentials.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Device name.
    """

    message_filters: Optional[DeviceMessageFilters] = None
    """
    Filter-sets to authorize or deny the device to publish/subscribe to specific topics.
    """

    description: Optional[str] = None
    """
    Device description.
    """


@dataclass
class CreateDeviceResponse:
    device: Optional[Device] = None
    """
    Information related to the created device.
    """

    certificate: Optional[Certificate] = None
    """
    Device certificate.
    """


@dataclass
class CreateHubRequest:
    product_plan: HubProductPlan
    """
    Hub product plan.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Hub name (up to 255 characters).
    """

    project_id: Optional[str] = None
    """
    Project/Organization ID to filter for, only Hubs from this Project/Organization will be returned.
    """

    disable_events: Optional[bool] = False
    """
    Disable Hub events.
    """

    events_topic_prefix: Optional[str] = None
    """
    Topic prefix (default '$SCW/events') of Hub events.
    """

    twins_graphite_config: Optional[HubTwinsGraphiteConfig] = None


@dataclass
class CreateNetworkRequest:
    type_: NetworkNetworkType
    """
    Type of network to connect with.
    """

    hub_id: str
    """
    Hub ID to connect the Network to.
    """

    topic_prefix: str
    """
    Topic prefix for the Network.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Network name.
    """


@dataclass
class CreateNetworkResponse:
    secret: str
    """
    Endpoint Key to keep secret. This cannot be retrieved later.
    """

    network: Optional[Network] = None
    """
    Information related to the created network.
    """


@dataclass
class CreateRouteRequest:
    hub_id: str
    """
    Hub ID of the route.
    """

    topic: str
    """
    Topic the route subscribes to. It must be a valid MQTT topic and up to 65535 characters.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Route name.
    """

    s3_config: Optional[CreateRouteRequestS3Config] = None

    db_config: Optional[CreateRouteRequestDatabaseConfig] = None

    rest_config: Optional[CreateRouteRequestRestConfig] = None


@dataclass
class DeleteDeviceRequest:
    device_id: str
    """
    Device ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteHubRequest:
    hub_id: str
    """
    Hub ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    delete_devices: Optional[bool] = False
    """
    Defines whether to force the deletion of devices added to this Hub or reject the operation.
    """


@dataclass
class DeleteNetworkRequest:
    network_id: str
    """
    Network ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteRouteRequest:
    route_id: str
    """
    Route ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteTwinDocumentRequest:
    twin_id: str
    """
    Twin ID.
    """

    document_name: str
    """
    Name of the document.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteTwinDocumentsRequest:
    twin_id: str
    """
    Twin ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DisableDeviceRequest:
    device_id: str
    """
    Device ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DisableHubRequest:
    hub_id: str
    """
    Hub ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class EnableDeviceRequest:
    device_id: str
    """
    Device ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class EnableHubRequest:
    hub_id: str
    """
    Hub ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDeviceCertificateRequest:
    device_id: str
    """
    Device ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDeviceCertificateResponse:
    certificate_pem: str
    """
    Device certificate.
    """

    device: Optional[Device] = None
    """
    Information related to the created device.
    """


@dataclass
class GetDeviceMetricsRequest:
    device_id: str
    """
    Device ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    start_date: Optional[datetime] = None
    """
    Start date used to compute the best scale for the returned metrics.
    """


@dataclass
class GetDeviceMetricsResponse:
    metrics: list[TimeSeries]
    """
    Metrics for a device over the requested period.
    """


@dataclass
class GetDeviceRequest:
    device_id: str
    """
    Device ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetHubCARequest:
    hub_id: str
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetHubCAResponse:
    ca_cert_pem: str


@dataclass
class GetHubMetricsRequest:
    hub_id: str
    """
    Hub ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    start_date: Optional[datetime] = None
    """
    Start date used to compute the best scale for returned metrics.
    """


@dataclass
class GetHubMetricsResponse:
    metrics: list[TimeSeries]
    """
    Metrics for a Hub over the requested period.
    """


@dataclass
class GetHubRequest:
    hub_id: str
    """
    Hub ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetNetworkRequest:
    network_id: str
    """
    Network ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetRouteRequest:
    route_id: str
    """
    Route ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetTwinDocumentRequest:
    twin_id: str
    """
    Twin ID.
    """

    document_name: str
    """
    Name of the document.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListDevicesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of devices to return within a page. Maximum value is 100.
    """

    order_by: Optional[ListDevicesRequestOrderBy] = ListDevicesRequestOrderBy.NAME_ASC
    """
    Ordering of requested devices.
    """

    name: Optional[str] = None
    """
    Name to filter for, only devices with this name will be returned.
    """

    hub_id: Optional[str] = None
    """
    Hub ID to filter for, only devices attached to this Hub will be returned.
    """

    allow_insecure: Optional[bool] = False
    """
    Defines whether to filter the allow_insecure flag.
    """

    status: Optional[DeviceStatus] = DeviceStatus.UNKNOWN
    """
    Device status (enabled, disabled, etc.).
    """


@dataclass
class ListDevicesResponse:
    total_count: int
    """
    Total number of devices.
    """

    devices: list[Device]
    """
    Page of devices.
    """


@dataclass
class ListHubsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of Hubs to return within a page. Maximum value is 100.
    """

    order_by: Optional[ListHubsRequestOrderBy] = ListHubsRequestOrderBy.NAME_ASC
    """
    Sort order of Hubs in the response.
    """

    project_id: Optional[str] = None
    """
    Only list Hubs of this Project ID.
    """

    organization_id: Optional[str] = None
    """
    Only list Hubs of this Organization ID.
    """

    name: Optional[str] = None
    """
    Hub name.
    """


@dataclass
class ListHubsResponse:
    total_count: int
    """
    Total number of Hubs.
    """

    hubs: list[Hub]
    """
    A page of hubs.
    """


@dataclass
class ListNetworksRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of networks to return. The maximum value is 100.
    """

    order_by: Optional[ListNetworksRequestOrderBy] = ListNetworksRequestOrderBy.NAME_ASC
    """
    Ordering of requested routes.
    """

    name: Optional[str] = None
    """
    Network name to filter for.
    """

    hub_id: Optional[str] = None
    """
    Hub ID to filter for.
    """

    topic_prefix: Optional[str] = None
    """
    Topic prefix to filter for.
    """


@dataclass
class ListNetworksResponse:
    total_count: int
    """
    Total number of Networks.
    """

    networks: list[Network]
    """
    Page of networks.
    """


@dataclass
class ListRoutesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of routes to return within a page. Maximum value is 100.
    """

    order_by: Optional[ListRoutesRequestOrderBy] = ListRoutesRequestOrderBy.NAME_ASC
    """
    Ordering of requested routes.
    """

    hub_id: Optional[str] = None
    """
    Hub ID to filter for.
    """

    name: Optional[str] = None
    """
    Route name to filter for.
    """


@dataclass
class ListRoutesResponse:
    total_count: int
    """
    Total number of routes.
    """

    routes: list[RouteSummary]
    """
    Page of routes.
    """


@dataclass
class ListTwinDocumentsRequest:
    twin_id: str
    """
    Twin ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListTwinDocumentsResponse:
    documents: list[ListTwinDocumentsResponseDocumentSummary]
    """
    List of the twin document.
    """


@dataclass
class PatchTwinDocumentRequest:
    twin_id: str
    """
    Twin ID.
    """

    document_name: str
    """
    Name of the document.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    version: Optional[int] = 0
    """
    If set, ensures that the current version of the document matches before persisting the update.
    """

    data: Optional[dict[str, Any]] = field(default_factory=dict)
    """
    A json data that will be applied on the document's current data.
Patching rules:
* The patch goes recursively through the patch objects.
* If the patch object property is null, it is removed from the final object.
* If the patch object property is a value (number, strings, bool, arrays), it is replaced.
* If the patch object property is an object, the previous rules will be applied recursively on it.
    """


@dataclass
class PutTwinDocumentRequest:
    twin_id: str
    """
    Twin ID.
    """

    document_name: str
    """
    Name of the document.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    version: Optional[int] = 0
    """
    If set, ensures that the current version of the document matches before persisting the update.
    """

    data: Optional[dict[str, Any]] = field(default_factory=dict)
    """
    New data that will replace the contents of the document.
    """


@dataclass
class RenewDeviceCertificateRequest:
    device_id: str
    """
    Device ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RenewDeviceCertificateResponse:
    device: Optional[Device] = None
    """
    Information related to the created device.
    """

    certificate: Optional[Certificate] = None
    """
    Device certificate.
    """


@dataclass
class Route:
    id: str
    """
    Route ID.
    """

    name: str
    """
    Route name.
    """

    hub_id: str
    """
    Hub ID of the route.
    """

    topic: str
    """
    Topic the route subscribes to. It must be a valid MQTT topic and up to 65535 characters.
    """

    type_: RouteRouteType
    """
    Route type.
    """

    region: ScwRegion
    """
    Region of the route.
    """

    created_at: Optional[datetime] = None
    """
    Date at which the route was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date at which the route was last updated.
    """

    s3_config: Optional[RouteS3Config] = None

    db_config: Optional[RouteDatabaseConfig] = None

    rest_config: Optional[RouteRestConfig] = None


@dataclass
class SetDeviceCertificateRequest:
    device_id: str
    """
    Device ID.
    """

    certificate_pem: str
    """
    PEM-encoded custom certificate.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class SetDeviceCertificateResponse:
    certificate_pem: str
    device: Optional[Device] = None


@dataclass
class SetHubCARequest:
    hub_id: str
    """
    Hub ID.
    """

    ca_cert_pem: str
    """
    CA's PEM-encoded certificate.
    """

    challenge_cert_pem: str
    """
    Challenge is a PEM-encoded certificate that acts as proof of possession of the CA. It must be signed by the CA, and have a Common Name equal to the Hub ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class TwinDocument:
    twin_id: str
    """
    Parent twin ID of the document.
    """

    document_name: str
    """
    Name of the document.
    """

    version: int
    """
    New version of the document.
    """

    data: Optional[dict[str, Any]] = field(default_factory=dict)
    """
    New data related to the document.
    """


@dataclass
class UpdateDeviceRequest:
    device_id: str
    """
    Device ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    description: Optional[str] = None
    """
    Description for the device.
    """

    allow_insecure: Optional[bool] = False
    """
    Defines whether to allow plain and server-authenticated SSL connections in addition to mutually-authenticated ones.
    """

    allow_multiple_connections: Optional[bool] = False
    """
    Defines whether to allow multiple physical devices to connect with this device's credentials.
    """

    message_filters: Optional[DeviceMessageFilters] = None
    """
    Filter-sets to restrict the topics the device can publish/subscribe to.
    """

    hub_id: Optional[str] = None
    """
    Change Hub for this device, additional fees may apply, see IoT Hub pricing.
    """


@dataclass
class UpdateHubRequest:
    hub_id: str
    """
    ID of the Hub you want to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Hub name (up to 255 characters).
    """

    product_plan: Optional[HubProductPlan] = HubProductPlan.PLAN_UNKNOWN
    """
    Hub product plan.
    """

    disable_events: Optional[bool] = False
    """
    Disable Hub events.
    """

    events_topic_prefix: Optional[str] = None
    """
    Topic prefix of Hub events.
    """

    enable_device_auto_provisioning: Optional[bool] = False
    """
    Enable device auto provisioning.
    """

    twins_graphite_config: Optional[HubTwinsGraphiteConfig] = None


@dataclass
class UpdateRouteRequest:
    route_id: str
    """
    Route id.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Route name.
    """

    topic: Optional[str] = None
    """
    Topic the route subscribes to. It must be a valid MQTT topic and up to 65535 characters.
    """

    s3_config: Optional[UpdateRouteRequestS3Config] = None

    db_config: Optional[UpdateRouteRequestDatabaseConfig] = None

    rest_config: Optional[UpdateRouteRequestRestConfig] = None
