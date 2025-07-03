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
    IPReverseStatus,
    IPVersion,
    ListServerEventsRequestOrderBy,
    ListServerPrivateNetworksRequestOrderBy,
    ListServersRequestOrderBy,
    ListSettingsRequestOrderBy,
    OfferStock,
    OfferSubscriptionPeriod,
    SchemaFilesystemFormat,
    SchemaPartitionLabel,
    SchemaPoolType,
    SchemaRAIDLevel,
    ServerBootType,
    ServerInstallStatus,
    ServerOptionOptionStatus,
    ServerPingStatus,
    ServerPrivateNetworkStatus,
    ServerStatus,
    SettingType,
    SchemaPartition,
    SchemaPool,
    SchemaDisk,
    SchemaFilesystem,
    SchemaRAID,
    SchemaZFS,
    Schema,
    IP,
    OSOSField,
    OS,
    CertificationOption,
    LicenseOption,
    PrivateNetworkOption,
    PublicBandwidthOption,
    RemoteAccessOption,
    CPU,
    Disk,
    GPU,
    Memory,
    OfferOptionOffer,
    PersistentMemory,
    RaidController,
    Offer,
    Option,
    ServerPrivateNetwork,
    ServerInstall,
    ServerOption,
    ServerRescueServer,
    Server,
    Setting,
    BMCAccess,
    GetServerMetricsResponse,
    ListOSResponse,
    ListOffersResponse,
    ListOptionsResponse,
    ServerEvent,
    ListServerEventsResponse,
    ListServerPrivateNetworksResponse,
    ListServersResponse,
    ListSettingsResponse,
    SetServerPrivateNetworksResponse,
    AddOptionServerRequest,
    CreateServerRequestInstall,
    CreateServerRequest,
    InstallServerRequest,
    PrivateNetworkApiAddServerPrivateNetworkRequest,
    PrivateNetworkApiSetServerPrivateNetworksRequest,
    RebootServerRequest,
    StartBMCAccessRequest,
    StartServerRequest,
    UpdateIPRequest,
    UpdateServerRequest,
    UpdateSettingRequest,
    ValidatePartitioningSchemaRequest,
)

def unmarshal_SchemaPartition(data: Any) -> SchemaPartition:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SchemaPartition' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("label", str())
    args["label"] = field

    field = data.get("number", str())
    args["number"] = field

    field = data.get("size", str())
    args["size"] = field

    field = data.get("use_all_available_space", str())
    args["use_all_available_space"] = field

    return SchemaPartition(**args)

def unmarshal_SchemaPool(data: Any) -> SchemaPool:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SchemaPool' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("devices", str())
    args["devices"] = field

    field = data.get("options", str())
    args["options"] = field

    field = data.get("filesystem_options", str())
    args["filesystem_options"] = field

    return SchemaPool(**args)

def unmarshal_SchemaDisk(data: Any) -> SchemaDisk:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SchemaDisk' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("device", str())
    args["device"] = field

    field = data.get("partitions", str())
    args["partitions"] = [unmarshal_SchemaPartition(v) for v in field] if field is not None else None

    return SchemaDisk(**args)

def unmarshal_SchemaFilesystem(data: Any) -> SchemaFilesystem:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SchemaFilesystem' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("device", str())
    args["device"] = field

    field = data.get("format", str())
    args["format"] = field

    field = data.get("mountpoint", str())
    args["mountpoint"] = field

    return SchemaFilesystem(**args)

def unmarshal_SchemaRAID(data: Any) -> SchemaRAID:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SchemaRAID' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("level", str())
    args["level"] = field

    field = data.get("devices", str())
    args["devices"] = field

    return SchemaRAID(**args)

def unmarshal_SchemaZFS(data: Any) -> SchemaZFS:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SchemaZFS' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pools", str())
    args["pools"] = [unmarshal_SchemaPool(v) for v in field] if field is not None else None

    return SchemaZFS(**args)

def unmarshal_Schema(data: Any) -> Schema:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Schema' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("disks", str())
    args["disks"] = [unmarshal_SchemaDisk(v) for v in field] if field is not None else None

    field = data.get("raids", str())
    args["raids"] = [unmarshal_SchemaRAID(v) for v in field] if field is not None else None

    field = data.get("filesystems", str())
    args["filesystems"] = [unmarshal_SchemaFilesystem(v) for v in field] if field is not None else None

    field = data.get("zfs", None)
    args["zfs"] = unmarshal_SchemaZFS(field) if field is not None else None

    return Schema(**args)

def unmarshal_IP(data: Any) -> IP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'IP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("address", str())
    args["address"] = field

    field = data.get("reverse", str())
    args["reverse"] = field

    field = data.get("version", getattr(IPVersion, "IPV4"))
    args["version"] = field

    field = data.get("reverse_status", getattr(IPReverseStatus, "UNKNOWN"))
    args["reverse_status"] = field

    field = data.get("reverse_status_message", str())
    args["reverse_status_message"] = field

    return IP(**args)

def unmarshal_OSOSField(data: Any) -> OSOSField:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OSOSField' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("editable", str())
    args["editable"] = field

    field = data.get("required", str())
    args["required"] = field

    field = data.get("default_value", None)
    args["default_value"] = field

    return OSOSField(**args)

def unmarshal_OS(data: Any) -> OS:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OS' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("version", str())
    args["version"] = field

    field = data.get("logo_url", str())
    args["logo_url"] = field

    field = data.get("ssh", None)
    args["ssh"] = unmarshal_OSOSField(field) if field is not None else None

    field = data.get("user", None)
    args["user"] = unmarshal_OSOSField(field) if field is not None else None

    field = data.get("password", None)
    args["password"] = unmarshal_OSOSField(field) if field is not None else None

    field = data.get("service_user", None)
    args["service_user"] = unmarshal_OSOSField(field) if field is not None else None

    field = data.get("service_password", None)
    args["service_password"] = unmarshal_OSOSField(field) if field is not None else None

    field = data.get("enabled", False)
    args["enabled"] = field

    field = data.get("license_required", False)
    args["license_required"] = field

    field = data.get("allowed", False)
    args["allowed"] = field

    field = data.get("custom_partitioning_supported", False)
    args["custom_partitioning_supported"] = field

    return OS(**args)

def unmarshal_CertificationOption(data: Any) -> CertificationOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CertificationOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return CertificationOption(**args)

def unmarshal_LicenseOption(data: Any) -> LicenseOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LicenseOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("os_id", str())
    args["os_id"] = field

    return LicenseOption(**args)

def unmarshal_PrivateNetworkOption(data: Any) -> PrivateNetworkOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetworkOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bandwidth_in_bps", str())
    args["bandwidth_in_bps"] = field

    return PrivateNetworkOption(**args)

def unmarshal_PublicBandwidthOption(data: Any) -> PublicBandwidthOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicBandwidthOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bandwidth_in_bps", str())
    args["bandwidth_in_bps"] = field

    return PublicBandwidthOption(**args)

def unmarshal_RemoteAccessOption(data: Any) -> RemoteAccessOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RemoteAccessOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return RemoteAccessOption(**args)

def unmarshal_CPU(data: Any) -> CPU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CPU' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("core_count", 0)
    args["core_count"] = field

    field = data.get("thread_count", 0)
    args["thread_count"] = field

    field = data.get("frequency", 0)
    args["frequency"] = field

    field = data.get("benchmark", str())
    args["benchmark"] = field

    return CPU(**args)

def unmarshal_Disk(data: Any) -> Disk:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Disk' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", 0)
    args["capacity"] = field

    field = data.get("type", str())
    args["type_"] = field

    return Disk(**args)

def unmarshal_GPU(data: Any) -> GPU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GPU' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("vram", 0)
    args["vram"] = field

    return GPU(**args)

def unmarshal_Memory(data: Any) -> Memory:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Memory' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", 0)
    args["capacity"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("frequency", 0)
    args["frequency"] = field

    field = data.get("is_ecc", False)
    args["is_ecc"] = field

    return Memory(**args)

def unmarshal_OfferOptionOffer(data: Any) -> OfferOptionOffer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferOptionOffer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("enabled", False)
    args["enabled"] = field

    field = data.get("subscription_period", getattr(OfferSubscriptionPeriod, "UNKNOWN_SUBSCRIPTION_PERIOD"))
    args["subscription_period"] = field

    field = data.get("manageable", False)
    args["manageable"] = field

    field = data.get("price", None)
    args["price"] = unmarshal_Money(field) if field is not None else None

    field = data.get("os_id", None)
    args["os_id"] = field

    field = data.get("license", None)
    args["license"] = unmarshal_LicenseOption(field) if field is not None else None

    field = data.get("public_bandwidth", None)
    args["public_bandwidth"] = unmarshal_PublicBandwidthOption(field) if field is not None else None

    field = data.get("private_network", None)
    args["private_network"] = unmarshal_PrivateNetworkOption(field) if field is not None else None

    field = data.get("remote_access", None)
    args["remote_access"] = unmarshal_RemoteAccessOption(field) if field is not None else None

    field = data.get("certification", None)
    args["certification"] = unmarshal_CertificationOption(field) if field is not None else None

    return OfferOptionOffer(**args)

def unmarshal_PersistentMemory(data: Any) -> PersistentMemory:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PersistentMemory' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", 0)
    args["capacity"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("frequency", 0)
    args["frequency"] = field

    return PersistentMemory(**args)

def unmarshal_RaidController(data: Any) -> RaidController:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RaidController' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("model", str())
    args["model"] = field

    field = data.get("raid_level", str())
    args["raid_level"] = field

    return RaidController(**args)

def unmarshal_Offer(data: Any) -> Offer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Offer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("stock", getattr(OfferStock, "EMPTY"))
    args["stock"] = field

    field = data.get("bandwidth", 0)
    args["bandwidth"] = field

    field = data.get("max_bandwidth", 0)
    args["max_bandwidth"] = field

    field = data.get("commercial_range", str())
    args["commercial_range"] = field

    field = data.get("disks", [])
    args["disks"] = [unmarshal_Disk(v) for v in field] if field is not None else None

    field = data.get("enable", False)
    args["enable"] = field

    field = data.get("cpus", [])
    args["cpus"] = [unmarshal_CPU(v) for v in field] if field is not None else None

    field = data.get("memories", [])
    args["memories"] = [unmarshal_Memory(v) for v in field] if field is not None else None

    field = data.get("price_per_hour", None)
    args["price_per_hour"] = unmarshal_Money(field) if field is not None else None

    field = data.get("price_per_month", None)
    args["price_per_month"] = unmarshal_Money(field) if field is not None else None

    field = data.get("quota_name", str())
    args["quota_name"] = field

    field = data.get("persistent_memories", [])
    args["persistent_memories"] = [unmarshal_PersistentMemory(v) for v in field] if field is not None else None

    field = data.get("raid_controllers", [])
    args["raid_controllers"] = [unmarshal_RaidController(v) for v in field] if field is not None else None

    field = data.get("incompatible_os_ids", [])
    args["incompatible_os_ids"] = field

    field = data.get("subscription_period", getattr(OfferSubscriptionPeriod, "UNKNOWN_SUBSCRIPTION_PERIOD"))
    args["subscription_period"] = field

    field = data.get("operation_path", str())
    args["operation_path"] = field

    field = data.get("options", [])
    args["options"] = [unmarshal_OfferOptionOffer(v) for v in field] if field is not None else None

    field = data.get("private_bandwidth", 0)
    args["private_bandwidth"] = field

    field = data.get("shared_bandwidth", False)
    args["shared_bandwidth"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("gpus", [])
    args["gpus"] = [unmarshal_GPU(v) for v in field] if field is not None else None

    field = data.get("fee", None)
    args["fee"] = unmarshal_Money(field) if field is not None else None

    field = data.get("monthly_offer_id", None)
    args["monthly_offer_id"] = field

    return Offer(**args)

def unmarshal_Option(data: Any) -> Option:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Option' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("manageable", False)
    args["manageable"] = field

    field = data.get("license", None)
    args["license"] = unmarshal_LicenseOption(field) if field is not None else None

    field = data.get("public_bandwidth", None)
    args["public_bandwidth"] = unmarshal_PublicBandwidthOption(field) if field is not None else None

    field = data.get("private_network", None)
    args["private_network"] = unmarshal_PrivateNetworkOption(field) if field is not None else None

    field = data.get("remote_access", None)
    args["remote_access"] = unmarshal_RemoteAccessOption(field) if field is not None else None

    field = data.get("certification", None)
    args["certification"] = unmarshal_CertificationOption(field) if field is not None else None

    return Option(**args)

def unmarshal_ServerPrivateNetwork(data: Any) -> ServerPrivateNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerPrivateNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("server_id", str())
    args["server_id"] = field

    field = data.get("private_network_id", str())
    args["private_network_id"] = field

    field = data.get("status", getattr(ServerPrivateNetworkStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("vlan", None)
    args["vlan"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return ServerPrivateNetwork(**args)

def unmarshal_ServerInstall(data: Any) -> ServerInstall:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerInstall' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("os_id", str())
    args["os_id"] = field

    field = data.get("hostname", str())
    args["hostname"] = field

    field = data.get("ssh_key_ids", [])
    args["ssh_key_ids"] = field

    field = data.get("status", getattr(ServerInstallStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("user", str())
    args["user"] = field

    field = data.get("service_user", str())
    args["service_user"] = field

    field = data.get("service_url", str())
    args["service_url"] = field

    field = data.get("partitioning_schema", None)
    args["partitioning_schema"] = unmarshal_Schema(field) if field is not None else None

    return ServerInstall(**args)

def unmarshal_ServerOption(data: Any) -> ServerOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("status", getattr(ServerOptionOptionStatus, "OPTION_STATUS_UNKNOWN"))
    args["status"] = field

    field = data.get("manageable", False)
    args["manageable"] = field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("license", None)
    args["license"] = unmarshal_LicenseOption(field) if field is not None else None

    field = data.get("public_bandwidth", None)
    args["public_bandwidth"] = unmarshal_PublicBandwidthOption(field) if field is not None else None

    field = data.get("private_network", None)
    args["private_network"] = unmarshal_PrivateNetworkOption(field) if field is not None else None

    field = data.get("remote_access", None)
    args["remote_access"] = unmarshal_RemoteAccessOption(field) if field is not None else None

    field = data.get("certification", None)
    args["certification"] = unmarshal_CertificationOption(field) if field is not None else None

    return ServerOption(**args)

def unmarshal_ServerRescueServer(data: Any) -> ServerRescueServer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerRescueServer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("user", str())
    args["user"] = field

    field = data.get("password", str())
    args["password"] = field

    return ServerRescueServer(**args)

def unmarshal_Server(data: Any) -> Server:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Server' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("status", getattr(ServerStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("offer_id", str())
    args["offer_id"] = field

    field = data.get("offer_name", str())
    args["offer_name"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("ips", [])
    args["ips"] = [unmarshal_IP(v) for v in field] if field is not None else None

    field = data.get("domain", str())
    args["domain"] = field

    field = data.get("boot_type", getattr(ServerBootType, "UNKNOWN_BOOT_TYPE"))
    args["boot_type"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("ping_status", getattr(ServerPingStatus, "PING_STATUS_UNKNOWN"))
    args["ping_status"] = field

    field = data.get("options", [])
    args["options"] = [unmarshal_ServerOption(v) for v in field] if field is not None else None

    field = data.get("install", None)
    args["install"] = unmarshal_ServerInstall(field) if field is not None else None

    field = data.get("rescue_server", None)
    args["rescue_server"] = unmarshal_ServerRescueServer(field) if field is not None else None

    return Server(**args)

def unmarshal_Setting(data: Any) -> Setting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Setting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("type", getattr(SettingType, "UNKNOWN"))
    args["type_"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("enabled", False)
    args["enabled"] = field

    return Setting(**args)

def unmarshal_BMCAccess(data: Any) -> BMCAccess:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BMCAccess' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("url", str())
    args["url"] = field

    field = data.get("login", str())
    args["login"] = field

    field = data.get("password", str())
    args["password"] = field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return BMCAccess(**args)

def unmarshal_GetServerMetricsResponse(data: Any) -> GetServerMetricsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetServerMetricsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pings", None)
    args["pings"] = unmarshal_TimeSeries(field) if field is not None else None

    return GetServerMetricsResponse(**args)

def unmarshal_ListOSResponse(data: Any) -> ListOSResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOSResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("os", [])
    args["os"] = [unmarshal_OS(v) for v in field] if field is not None else None

    return ListOSResponse(**args)

def unmarshal_ListOffersResponse(data: Any) -> ListOffersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOffersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("offers", [])
    args["offers"] = [unmarshal_Offer(v) for v in field] if field is not None else None

    return ListOffersResponse(**args)

def unmarshal_ListOptionsResponse(data: Any) -> ListOptionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOptionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("options", [])
    args["options"] = [unmarshal_Option(v) for v in field] if field is not None else None

    return ListOptionsResponse(**args)

def unmarshal_ServerEvent(data: Any) -> ServerEvent:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerEvent' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("action", str())
    args["action"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return ServerEvent(**args)

def unmarshal_ListServerEventsResponse(data: Any) -> ListServerEventsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerEventsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("events", [])
    args["events"] = [unmarshal_ServerEvent(v) for v in field] if field is not None else None

    return ListServerEventsResponse(**args)

def unmarshal_ListServerPrivateNetworksResponse(data: Any) -> ListServerPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server_private_networks", str())
    args["server_private_networks"] = [unmarshal_ServerPrivateNetwork(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListServerPrivateNetworksResponse(**args)

def unmarshal_ListServersResponse(data: Any) -> ListServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("servers", [])
    args["servers"] = [unmarshal_Server(v) for v in field] if field is not None else None

    return ListServersResponse(**args)

def unmarshal_ListSettingsResponse(data: Any) -> ListSettingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSettingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("settings", [])
    args["settings"] = [unmarshal_Setting(v) for v in field] if field is not None else None

    return ListSettingsResponse(**args)

def unmarshal_SetServerPrivateNetworksResponse(data: Any) -> SetServerPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetServerPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server_private_networks", str())
    args["server_private_networks"] = [unmarshal_ServerPrivateNetwork(v) for v in field] if field is not None else None

    return SetServerPrivateNetworksResponse(**args)

def marshal_AddOptionServerRequest(
    request: AddOptionServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()
    else:
        output["expires_at"] = None


    return output

def marshal_SchemaPartition(
    request: SchemaPartition,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.label is not None:
        output["label"] = str(request.label)
    else:
        output["label"] = str()

    if request.number is not None:
        output["number"] = request.number
    else:
        output["number"] = str()

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = str()

    if request.use_all_available_space is not None:
        output["use_all_available_space"] = request.use_all_available_space
    else:
        output["use_all_available_space"] = str()


    return output

def marshal_SchemaPool(
    request: SchemaPool,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = str()

    if request.devices is not None:
        output["devices"] = request.devices
    else:
        output["devices"] = str()

    if request.options is not None:
        output["options"] = request.options
    else:
        output["options"] = str()

    if request.filesystem_options is not None:
        output["filesystem_options"] = request.filesystem_options
    else:
        output["filesystem_options"] = str()


    return output

def marshal_SchemaDisk(
    request: SchemaDisk,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.device is not None:
        output["device"] = request.device
    else:
        output["device"] = str()

    if request.partitions is not None:
        output["partitions"] = [marshal_SchemaPartition(item, defaults) for item in request.partitions]
    else:
        output["partitions"] = str()


    return output

def marshal_SchemaFilesystem(
    request: SchemaFilesystem,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.device is not None:
        output["device"] = request.device
    else:
        output["device"] = str()

    if request.format is not None:
        output["format"] = str(request.format)
    else:
        output["format"] = str()

    if request.mountpoint is not None:
        output["mountpoint"] = request.mountpoint
    else:
        output["mountpoint"] = str()


    return output

def marshal_SchemaRAID(
    request: SchemaRAID,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.level is not None:
        output["level"] = str(request.level)
    else:
        output["level"] = str()

    if request.devices is not None:
        output["devices"] = request.devices
    else:
        output["devices"] = str()


    return output

def marshal_SchemaZFS(
    request: SchemaZFS,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.pools is not None:
        output["pools"] = [marshal_SchemaPool(item, defaults) for item in request.pools]
    else:
        output["pools"] = str()


    return output

def marshal_Schema(
    request: Schema,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.disks is not None:
        output["disks"] = [marshal_SchemaDisk(item, defaults) for item in request.disks]
    else:
        output["disks"] = str()

    if request.raids is not None:
        output["raids"] = [marshal_SchemaRAID(item, defaults) for item in request.raids]
    else:
        output["raids"] = str()

    if request.filesystems is not None:
        output["filesystems"] = [marshal_SchemaFilesystem(item, defaults) for item in request.filesystems]
    else:
        output["filesystems"] = str()

    if request.zfs is not None:
        output["zfs"] = marshal_SchemaZFS(request.zfs, defaults)
    else:
        output["zfs"] = None


    return output

def marshal_CreateServerRequestInstall(
    request: CreateServerRequestInstall,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.os_id is not None:
        output["os_id"] = request.os_id
    else:
        output["os_id"] = str()

    if request.hostname is not None:
        output["hostname"] = request.hostname
    else:
        output["hostname"] = str()

    if request.ssh_key_ids is not None:
        output["ssh_key_ids"] = request.ssh_key_ids
    else:
        output["ssh_key_ids"] = []

    if request.user is not None:
        output["user"] = request.user
    else:
        output["user"] = None

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = None

    if request.service_user is not None:
        output["service_user"] = request.service_user
    else:
        output["service_user"] = None

    if request.service_password is not None:
        output["service_password"] = request.service_password
    else:
        output["service_password"] = None

    if request.partitioning_schema is not None:
        output["partitioning_schema"] = marshal_Schema(request.partitioning_schema, defaults)
    else:
        output["partitioning_schema"] = None


    return output

def marshal_CreateServerRequest(
    request: CreateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project_id", value=request.project_id, default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization_id", value=request.organization_id,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id
    else:
        output["offer_id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.install is not None:
        output["install"] = marshal_CreateServerRequestInstall(request.install, defaults)
    else:
        output["install"] = None

    if request.option_ids is not None:
        output["option_ids"] = request.option_ids
    else:
        output["option_ids"] = None


    return output

def marshal_InstallServerRequest(
    request: InstallServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.os_id is not None:
        output["os_id"] = request.os_id
    else:
        output["os_id"] = str()

    if request.hostname is not None:
        output["hostname"] = request.hostname
    else:
        output["hostname"] = str()

    if request.ssh_key_ids is not None:
        output["ssh_key_ids"] = request.ssh_key_ids
    else:
        output["ssh_key_ids"] = str()

    if request.user is not None:
        output["user"] = request.user
    else:
        output["user"] = None

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = None

    if request.service_user is not None:
        output["service_user"] = request.service_user
    else:
        output["service_user"] = None

    if request.service_password is not None:
        output["service_password"] = request.service_password
    else:
        output["service_password"] = None

    if request.partitioning_schema is not None:
        output["partitioning_schema"] = marshal_Schema(request.partitioning_schema, defaults)
    else:
        output["partitioning_schema"] = None


    return output

def marshal_PrivateNetworkApiAddServerPrivateNetworkRequest(
    request: PrivateNetworkApiAddServerPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = str()


    return output

def marshal_PrivateNetworkApiSetServerPrivateNetworksRequest(
    request: PrivateNetworkApiSetServerPrivateNetworksRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.private_network_ids is not None:
        output["private_network_ids"] = request.private_network_ids
    else:
        output["private_network_ids"] = str()


    return output

def marshal_RebootServerRequest(
    request: RebootServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.boot_type is not None:
        output["boot_type"] = str(request.boot_type)
    else:
        output["boot_type"] = None


    return output

def marshal_StartBMCAccessRequest(
    request: StartBMCAccessRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip is not None:
        output["ip"] = request.ip
    else:
        output["ip"] = str()


    return output

def marshal_StartServerRequest(
    request: StartServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.boot_type is not None:
        output["boot_type"] = str(request.boot_type)
    else:
        output["boot_type"] = None


    return output

def marshal_UpdateIPRequest(
    request: UpdateIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.reverse is not None:
        output["reverse"] = request.reverse
    else:
        output["reverse"] = None


    return output

def marshal_UpdateServerRequest(
    request: UpdateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_UpdateSettingRequest(
    request: UpdateSettingRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.enabled is not None:
        output["enabled"] = request.enabled
    else:
        output["enabled"] = None


    return output

def marshal_ValidatePartitioningSchemaRequest(
    request: ValidatePartitioningSchemaRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id
    else:
        output["offer_id"] = str()

    if request.os_id is not None:
        output["os_id"] = request.os_id
    else:
        output["os_id"] = str()

    if request.partitioning_schema is not None:
        output["partitioning_schema"] = marshal_Schema(request.partitioning_schema, defaults)
    else:
        output["partitioning_schema"] = None


    return output
