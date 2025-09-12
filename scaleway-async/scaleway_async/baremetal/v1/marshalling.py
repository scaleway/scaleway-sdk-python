# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_Money,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    IPReverseStatus,
    IPVersion,
    OfferStock,
    OfferSubscriptionPeriod,
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
    CertificationOption,
    LicenseOption,
    PrivateNetworkOption,
    PublicBandwidthOption,
    RemoteAccessOption,
    ServerInstall,
    ServerOption,
    ServerRescueServer,
    Server,
    OSOSField,
    OS,
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
    CreateServerRequestInstall,
    CreateServerRequest,
    AddOptionServerRequest,
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

    args: dict[str, Any] = {}

    field = data.get("label", None)
    if field is not None:
        args["label"] = field
    else:
        args["label"] = None

    field = data.get("number", None)
    if field is not None:
        args["number"] = field
    else:
        args["number"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = None

    field = data.get("use_all_available_space", None)
    if field is not None:
        args["use_all_available_space"] = field
    else:
        args["use_all_available_space"] = None

    return SchemaPartition(**args)


def unmarshal_SchemaPool(data: Any) -> SchemaPool:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SchemaPool' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("devices", None)
    if field is not None:
        args["devices"] = field
    else:
        args["devices"] = None

    field = data.get("options", None)
    if field is not None:
        args["options"] = field
    else:
        args["options"] = None

    field = data.get("filesystem_options", None)
    if field is not None:
        args["filesystem_options"] = field
    else:
        args["filesystem_options"] = None

    return SchemaPool(**args)


def unmarshal_SchemaDisk(data: Any) -> SchemaDisk:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SchemaDisk' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("device", None)
    if field is not None:
        args["device"] = field
    else:
        args["device"] = None

    field = data.get("partitions", None)
    if field is not None:
        args["partitions"] = (
            [unmarshal_SchemaPartition(v) for v in field] if field is not None else None
        )
    else:
        args["partitions"] = None

    return SchemaDisk(**args)


def unmarshal_SchemaFilesystem(data: Any) -> SchemaFilesystem:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SchemaFilesystem' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("device", None)
    if field is not None:
        args["device"] = field
    else:
        args["device"] = None

    field = data.get("format", None)
    if field is not None:
        args["format"] = field
    else:
        args["format"] = None

    field = data.get("mountpoint", None)
    if field is not None:
        args["mountpoint"] = field
    else:
        args["mountpoint"] = None

    return SchemaFilesystem(**args)


def unmarshal_SchemaRAID(data: Any) -> SchemaRAID:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SchemaRAID' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("level", None)
    if field is not None:
        args["level"] = field
    else:
        args["level"] = None

    field = data.get("devices", None)
    if field is not None:
        args["devices"] = field
    else:
        args["devices"] = None

    return SchemaRAID(**args)


def unmarshal_SchemaZFS(data: Any) -> SchemaZFS:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SchemaZFS' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("pools", None)
    if field is not None:
        args["pools"] = (
            [unmarshal_SchemaPool(v) for v in field] if field is not None else None
        )
    else:
        args["pools"] = None

    return SchemaZFS(**args)


def unmarshal_Schema(data: Any) -> Schema:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Schema' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("disks", None)
    if field is not None:
        args["disks"] = (
            [unmarshal_SchemaDisk(v) for v in field] if field is not None else None
        )
    else:
        args["disks"] = None

    field = data.get("raids", None)
    if field is not None:
        args["raids"] = (
            [unmarshal_SchemaRAID(v) for v in field] if field is not None else None
        )
    else:
        args["raids"] = None

    field = data.get("filesystems", None)
    if field is not None:
        args["filesystems"] = (
            [unmarshal_SchemaFilesystem(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["filesystems"] = None

    field = data.get("zfs", None)
    if field is not None:
        args["zfs"] = unmarshal_SchemaZFS(field)
    else:
        args["zfs"] = None

    return Schema(**args)


def unmarshal_IP(data: Any) -> IP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'IP' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("address", None)
    if field is not None:
        args["address"] = field
    else:
        args["address"] = None

    field = data.get("reverse", None)
    if field is not None:
        args["reverse"] = field
    else:
        args["reverse"] = None

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = IPVersion.I_PV4

    field = data.get("reverse_status", None)
    if field is not None:
        args["reverse_status"] = field
    else:
        args["reverse_status"] = IPReverseStatus.UNKNOWN

    field = data.get("reverse_status_message", None)
    if field is not None:
        args["reverse_status_message"] = field
    else:
        args["reverse_status_message"] = None

    return IP(**args)


def unmarshal_CertificationOption(data: Any) -> CertificationOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CertificationOption' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return CertificationOption(**args)


def unmarshal_LicenseOption(data: Any) -> LicenseOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LicenseOption' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("os_id", None)
    if field is not None:
        args["os_id"] = field
    else:
        args["os_id"] = None

    return LicenseOption(**args)


def unmarshal_PrivateNetworkOption(data: Any) -> PrivateNetworkOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetworkOption' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("bandwidth_in_bps", None)
    if field is not None:
        args["bandwidth_in_bps"] = field
    else:
        args["bandwidth_in_bps"] = None

    return PrivateNetworkOption(**args)


def unmarshal_PublicBandwidthOption(data: Any) -> PublicBandwidthOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicBandwidthOption' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("bandwidth_in_bps", None)
    if field is not None:
        args["bandwidth_in_bps"] = field
    else:
        args["bandwidth_in_bps"] = None

    return PublicBandwidthOption(**args)


def unmarshal_RemoteAccessOption(data: Any) -> RemoteAccessOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RemoteAccessOption' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return RemoteAccessOption(**args)


def unmarshal_ServerInstall(data: Any) -> ServerInstall:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerInstall' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("os_id", None)
    if field is not None:
        args["os_id"] = field
    else:
        args["os_id"] = None

    field = data.get("hostname", None)
    if field is not None:
        args["hostname"] = field
    else:
        args["hostname"] = None

    field = data.get("ssh_key_ids", None)
    if field is not None:
        args["ssh_key_ids"] = field
    else:
        args["ssh_key_ids"] = []

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ServerInstallStatus.UNKNOWN

    field = data.get("user", None)
    if field is not None:
        args["user"] = field
    else:
        args["user"] = None

    field = data.get("service_user", None)
    if field is not None:
        args["service_user"] = field
    else:
        args["service_user"] = None

    field = data.get("service_url", None)
    if field is not None:
        args["service_url"] = field
    else:
        args["service_url"] = None

    field = data.get("partitioning_schema", None)
    if field is not None:
        args["partitioning_schema"] = unmarshal_Schema(field)
    else:
        args["partitioning_schema"] = None

    return ServerInstall(**args)


def unmarshal_ServerOption(data: Any) -> ServerOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerOption' failed as data isn't a dictionary."
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

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ServerOptionOptionStatus.OPTION_STATUS_UNKNOWN

    field = data.get("manageable", None)
    if field is not None:
        args["manageable"] = field
    else:
        args["manageable"] = False

    field = data.get("expires_at", None)
    if field is not None:
        args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expires_at"] = None

    field = data.get("license", None)
    if field is not None:
        args["license"] = unmarshal_LicenseOption(field)
    else:
        args["license"] = None

    field = data.get("public_bandwidth", None)
    if field is not None:
        args["public_bandwidth"] = unmarshal_PublicBandwidthOption(field)
    else:
        args["public_bandwidth"] = None

    field = data.get("private_network", None)
    if field is not None:
        args["private_network"] = unmarshal_PrivateNetworkOption(field)
    else:
        args["private_network"] = None

    field = data.get("remote_access", None)
    if field is not None:
        args["remote_access"] = unmarshal_RemoteAccessOption(field)
    else:
        args["remote_access"] = None

    field = data.get("certification", None)
    if field is not None:
        args["certification"] = unmarshal_CertificationOption(field)
    else:
        args["certification"] = None

    return ServerOption(**args)


def unmarshal_ServerRescueServer(data: Any) -> ServerRescueServer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerRescueServer' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("user", None)
    if field is not None:
        args["user"] = field
    else:
        args["user"] = None

    field = data.get("password", None)
    if field is not None:
        args["password"] = field
    else:
        args["password"] = None

    return ServerRescueServer(**args)


def unmarshal_Server(data: Any) -> Server:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Server' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

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
        args["status"] = ServerStatus.UNKNOWN

    field = data.get("offer_id", None)
    if field is not None:
        args["offer_id"] = field
    else:
        args["offer_id"] = None

    field = data.get("offer_name", None)
    if field is not None:
        args["offer_name"] = field
    else:
        args["offer_name"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("ips", None)
    if field is not None:
        args["ips"] = [unmarshal_IP(v) for v in field] if field is not None else None
    else:
        args["ips"] = []

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("boot_type", None)
    if field is not None:
        args["boot_type"] = field
    else:
        args["boot_type"] = ServerBootType.UNKNOWN_BOOT_TYPE

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("ping_status", None)
    if field is not None:
        args["ping_status"] = field
    else:
        args["ping_status"] = ServerPingStatus.PING_STATUS_UNKNOWN

    field = data.get("options", None)
    if field is not None:
        args["options"] = (
            [unmarshal_ServerOption(v) for v in field] if field is not None else None
        )
    else:
        args["options"] = []

    field = data.get("protected", None)
    if field is not None:
        args["protected"] = field
    else:
        args["protected"] = False

    field = data.get("install", None)
    if field is not None:
        args["install"] = unmarshal_ServerInstall(field)
    else:
        args["install"] = None

    field = data.get("rescue_server", None)
    if field is not None:
        args["rescue_server"] = unmarshal_ServerRescueServer(field)
    else:
        args["rescue_server"] = None

    return Server(**args)


def unmarshal_OSOSField(data: Any) -> OSOSField:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OSOSField' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("editable", None)
    if field is not None:
        args["editable"] = field
    else:
        args["editable"] = None

    field = data.get("required", None)
    if field is not None:
        args["required"] = field
    else:
        args["required"] = None

    field = data.get("default_value", None)
    if field is not None:
        args["default_value"] = field
    else:
        args["default_value"] = None

    return OSOSField(**args)


def unmarshal_OS(data: Any) -> OS:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OS' failed as data isn't a dictionary."
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

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = None

    field = data.get("logo_url", None)
    if field is not None:
        args["logo_url"] = field
    else:
        args["logo_url"] = None

    field = data.get("ssh", None)
    if field is not None:
        args["ssh"] = unmarshal_OSOSField(field)
    else:
        args["ssh"] = None

    field = data.get("user", None)
    if field is not None:
        args["user"] = unmarshal_OSOSField(field)
    else:
        args["user"] = None

    field = data.get("password", None)
    if field is not None:
        args["password"] = unmarshal_OSOSField(field)
    else:
        args["password"] = None

    field = data.get("service_user", None)
    if field is not None:
        args["service_user"] = unmarshal_OSOSField(field)
    else:
        args["service_user"] = None

    field = data.get("service_password", None)
    if field is not None:
        args["service_password"] = unmarshal_OSOSField(field)
    else:
        args["service_password"] = None

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field
    else:
        args["enabled"] = False

    field = data.get("license_required", None)
    if field is not None:
        args["license_required"] = field
    else:
        args["license_required"] = False

    field = data.get("allowed", None)
    if field is not None:
        args["allowed"] = field
    else:
        args["allowed"] = False

    field = data.get("custom_partitioning_supported", None)
    if field is not None:
        args["custom_partitioning_supported"] = field
    else:
        args["custom_partitioning_supported"] = False

    return OS(**args)


def unmarshal_CPU(data: Any) -> CPU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CPU' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("core_count", None)
    if field is not None:
        args["core_count"] = field
    else:
        args["core_count"] = 0

    field = data.get("thread_count", None)
    if field is not None:
        args["thread_count"] = field
    else:
        args["thread_count"] = 0

    field = data.get("frequency", None)
    if field is not None:
        args["frequency"] = field
    else:
        args["frequency"] = 0

    field = data.get("benchmark", None)
    if field is not None:
        args["benchmark"] = field
    else:
        args["benchmark"] = None

    return CPU(**args)


def unmarshal_Disk(data: Any) -> Disk:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Disk' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("capacity", None)
    if field is not None:
        args["capacity"] = field
    else:
        args["capacity"] = 0

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    return Disk(**args)


def unmarshal_GPU(data: Any) -> GPU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GPU' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("vram", None)
    if field is not None:
        args["vram"] = field
    else:
        args["vram"] = 0

    return GPU(**args)


def unmarshal_Memory(data: Any) -> Memory:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Memory' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("capacity", None)
    if field is not None:
        args["capacity"] = field
    else:
        args["capacity"] = 0

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("frequency", None)
    if field is not None:
        args["frequency"] = field
    else:
        args["frequency"] = 0

    field = data.get("is_ecc", None)
    if field is not None:
        args["is_ecc"] = field
    else:
        args["is_ecc"] = False

    return Memory(**args)


def unmarshal_OfferOptionOffer(data: Any) -> OfferOptionOffer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferOptionOffer' failed as data isn't a dictionary."
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

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field
    else:
        args["enabled"] = False

    field = data.get("subscription_period", None)
    if field is not None:
        args["subscription_period"] = field
    else:
        args["subscription_period"] = (
            OfferSubscriptionPeriod.UNKNOWN_SUBSCRIPTION_PERIOD
        )

    field = data.get("manageable", None)
    if field is not None:
        args["manageable"] = field
    else:
        args["manageable"] = False

    field = data.get("price", None)
    if field is not None:
        args["price"] = unmarshal_Money(field)
    else:
        args["price"] = None

    field = data.get("os_id", None)
    if field is not None:
        args["os_id"] = field
    else:
        args["os_id"] = None

    field = data.get("license", None)
    if field is not None:
        args["license"] = unmarshal_LicenseOption(field)
    else:
        args["license"] = None

    field = data.get("public_bandwidth", None)
    if field is not None:
        args["public_bandwidth"] = unmarshal_PublicBandwidthOption(field)
    else:
        args["public_bandwidth"] = None

    field = data.get("private_network", None)
    if field is not None:
        args["private_network"] = unmarshal_PrivateNetworkOption(field)
    else:
        args["private_network"] = None

    field = data.get("remote_access", None)
    if field is not None:
        args["remote_access"] = unmarshal_RemoteAccessOption(field)
    else:
        args["remote_access"] = None

    field = data.get("certification", None)
    if field is not None:
        args["certification"] = unmarshal_CertificationOption(field)
    else:
        args["certification"] = None

    return OfferOptionOffer(**args)


def unmarshal_PersistentMemory(data: Any) -> PersistentMemory:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PersistentMemory' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("capacity", None)
    if field is not None:
        args["capacity"] = field
    else:
        args["capacity"] = 0

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("frequency", None)
    if field is not None:
        args["frequency"] = field
    else:
        args["frequency"] = 0

    return PersistentMemory(**args)


def unmarshal_RaidController(data: Any) -> RaidController:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RaidController' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("model", None)
    if field is not None:
        args["model"] = field
    else:
        args["model"] = None

    field = data.get("raid_level", None)
    if field is not None:
        args["raid_level"] = field
    else:
        args["raid_level"] = None

    return RaidController(**args)


def unmarshal_Offer(data: Any) -> Offer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Offer' failed as data isn't a dictionary."
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

    field = data.get("stock", None)
    if field is not None:
        args["stock"] = field
    else:
        args["stock"] = OfferStock.EMPTY

    field = data.get("bandwidth", None)
    if field is not None:
        args["bandwidth"] = field
    else:
        args["bandwidth"] = 0

    field = data.get("max_bandwidth", None)
    if field is not None:
        args["max_bandwidth"] = field
    else:
        args["max_bandwidth"] = 0

    field = data.get("commercial_range", None)
    if field is not None:
        args["commercial_range"] = field
    else:
        args["commercial_range"] = None

    field = data.get("disks", None)
    if field is not None:
        args["disks"] = (
            [unmarshal_Disk(v) for v in field] if field is not None else None
        )
    else:
        args["disks"] = []

    field = data.get("enable", None)
    if field is not None:
        args["enable"] = field
    else:
        args["enable"] = False

    field = data.get("cpus", None)
    if field is not None:
        args["cpus"] = [unmarshal_CPU(v) for v in field] if field is not None else None
    else:
        args["cpus"] = []

    field = data.get("memories", None)
    if field is not None:
        args["memories"] = (
            [unmarshal_Memory(v) for v in field] if field is not None else None
        )
    else:
        args["memories"] = []

    field = data.get("price_per_hour", None)
    if field is not None:
        args["price_per_hour"] = unmarshal_Money(field)
    else:
        args["price_per_hour"] = None

    field = data.get("price_per_month", None)
    if field is not None:
        args["price_per_month"] = unmarshal_Money(field)
    else:
        args["price_per_month"] = None

    field = data.get("quota_name", None)
    if field is not None:
        args["quota_name"] = field
    else:
        args["quota_name"] = None

    field = data.get("persistent_memories", None)
    if field is not None:
        args["persistent_memories"] = (
            [unmarshal_PersistentMemory(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["persistent_memories"] = []

    field = data.get("raid_controllers", None)
    if field is not None:
        args["raid_controllers"] = (
            [unmarshal_RaidController(v) for v in field] if field is not None else None
        )
    else:
        args["raid_controllers"] = []

    field = data.get("incompatible_os_ids", None)
    if field is not None:
        args["incompatible_os_ids"] = field
    else:
        args["incompatible_os_ids"] = []

    field = data.get("subscription_period", None)
    if field is not None:
        args["subscription_period"] = field
    else:
        args["subscription_period"] = (
            OfferSubscriptionPeriod.UNKNOWN_SUBSCRIPTION_PERIOD
        )

    field = data.get("operation_path", None)
    if field is not None:
        args["operation_path"] = field
    else:
        args["operation_path"] = None

    field = data.get("options", None)
    if field is not None:
        args["options"] = (
            [unmarshal_OfferOptionOffer(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["options"] = []

    field = data.get("private_bandwidth", None)
    if field is not None:
        args["private_bandwidth"] = field
    else:
        args["private_bandwidth"] = 0

    field = data.get("shared_bandwidth", None)
    if field is not None:
        args["shared_bandwidth"] = field
    else:
        args["shared_bandwidth"] = False

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("gpus", None)
    if field is not None:
        args["gpus"] = [unmarshal_GPU(v) for v in field] if field is not None else None
    else:
        args["gpus"] = []

    field = data.get("fee", None)
    if field is not None:
        args["fee"] = unmarshal_Money(field)
    else:
        args["fee"] = None

    field = data.get("monthly_offer_id", None)
    if field is not None:
        args["monthly_offer_id"] = field
    else:
        args["monthly_offer_id"] = None

    return Offer(**args)


def unmarshal_Option(data: Any) -> Option:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Option' failed as data isn't a dictionary."
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

    field = data.get("manageable", None)
    if field is not None:
        args["manageable"] = field
    else:
        args["manageable"] = False

    field = data.get("license", None)
    if field is not None:
        args["license"] = unmarshal_LicenseOption(field)
    else:
        args["license"] = None

    field = data.get("public_bandwidth", None)
    if field is not None:
        args["public_bandwidth"] = unmarshal_PublicBandwidthOption(field)
    else:
        args["public_bandwidth"] = None

    field = data.get("private_network", None)
    if field is not None:
        args["private_network"] = unmarshal_PrivateNetworkOption(field)
    else:
        args["private_network"] = None

    field = data.get("remote_access", None)
    if field is not None:
        args["remote_access"] = unmarshal_RemoteAccessOption(field)
    else:
        args["remote_access"] = None

    field = data.get("certification", None)
    if field is not None:
        args["certification"] = unmarshal_CertificationOption(field)
    else:
        args["certification"] = None

    return Option(**args)


def unmarshal_ServerPrivateNetwork(data: Any) -> ServerPrivateNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerPrivateNetwork' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("server_id", None)
    if field is not None:
        args["server_id"] = field
    else:
        args["server_id"] = None

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ServerPrivateNetworkStatus.UNKNOWN

    field = data.get("vlan", None)
    if field is not None:
        args["vlan"] = field
    else:
        args["vlan"] = 0

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

    return ServerPrivateNetwork(**args)


def unmarshal_Setting(data: Any) -> Setting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Setting' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = SettingType.UNKNOWN

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field
    else:
        args["enabled"] = False

    return Setting(**args)


def unmarshal_BMCAccess(data: Any) -> BMCAccess:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BMCAccess' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("url", None)
    if field is not None:
        args["url"] = field
    else:
        args["url"] = None

    field = data.get("login", None)
    if field is not None:
        args["login"] = field
    else:
        args["login"] = None

    field = data.get("password", None)
    if field is not None:
        args["password"] = field
    else:
        args["password"] = None

    field = data.get("expires_at", None)
    if field is not None:
        args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expires_at"] = None

    return BMCAccess(**args)


def unmarshal_GetServerMetricsResponse(data: Any) -> GetServerMetricsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetServerMetricsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("pings", None)
    if field is not None:
        args["pings"] = unmarshal_TimeSeries(field)
    else:
        args["pings"] = None

    return GetServerMetricsResponse(**args)


def unmarshal_ListOSResponse(data: Any) -> ListOSResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOSResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("os", None)
    if field is not None:
        args["os"] = [unmarshal_OS(v) for v in field] if field is not None else None
    else:
        args["os"] = []

    return ListOSResponse(**args)


def unmarshal_ListOffersResponse(data: Any) -> ListOffersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOffersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("offers", None)
    if field is not None:
        args["offers"] = (
            [unmarshal_Offer(v) for v in field] if field is not None else None
        )
    else:
        args["offers"] = []

    return ListOffersResponse(**args)


def unmarshal_ListOptionsResponse(data: Any) -> ListOptionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOptionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("options", None)
    if field is not None:
        args["options"] = (
            [unmarshal_Option(v) for v in field] if field is not None else None
        )
    else:
        args["options"] = []

    return ListOptionsResponse(**args)


def unmarshal_ServerEvent(data: Any) -> ServerEvent:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerEvent' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("action", None)
    if field is not None:
        args["action"] = field
    else:
        args["action"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return ServerEvent(**args)


def unmarshal_ListServerEventsResponse(data: Any) -> ListServerEventsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerEventsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("events", None)
    if field is not None:
        args["events"] = (
            [unmarshal_ServerEvent(v) for v in field] if field is not None else None
        )
    else:
        args["events"] = []

    return ListServerEventsResponse(**args)


def unmarshal_ListServerPrivateNetworksResponse(
    data: Any,
) -> ListServerPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server_private_networks", None)
    if field is not None:
        args["server_private_networks"] = (
            [unmarshal_ServerPrivateNetwork(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["server_private_networks"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListServerPrivateNetworksResponse(**args)


def unmarshal_ListServersResponse(data: Any) -> ListServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("servers", None)
    if field is not None:
        args["servers"] = (
            [unmarshal_Server(v) for v in field] if field is not None else None
        )
    else:
        args["servers"] = []

    return ListServersResponse(**args)


def unmarshal_ListSettingsResponse(data: Any) -> ListSettingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSettingsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("settings", None)
    if field is not None:
        args["settings"] = (
            [unmarshal_Setting(v) for v in field] if field is not None else None
        )
    else:
        args["settings"] = []

    return ListSettingsResponse(**args)


def unmarshal_SetServerPrivateNetworksResponse(
    data: Any,
) -> SetServerPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetServerPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server_private_networks", None)
    if field is not None:
        args["server_private_networks"] = (
            [unmarshal_ServerPrivateNetwork(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["server_private_networks"] = None

    return SetServerPrivateNetworksResponse(**args)


def marshal_SchemaPartition(
    request: SchemaPartition,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.label is not None:
        output["label"] = request.label

    if request.number is not None:
        output["number"] = request.number

    if request.size is not None:
        output["size"] = request.size

    if request.use_all_available_space is not None:
        output["use_all_available_space"] = request.use_all_available_space

    return output


def marshal_SchemaPool(
    request: SchemaPool,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.type_ is not None:
        output["type"] = request.type_

    if request.devices is not None:
        output["devices"] = request.devices

    if request.options is not None:
        output["options"] = request.options

    if request.filesystem_options is not None:
        output["filesystem_options"] = request.filesystem_options

    return output


def marshal_SchemaDisk(
    request: SchemaDisk,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.device is not None:
        output["device"] = request.device

    if request.partitions is not None:
        output["partitions"] = [
            marshal_SchemaPartition(item, defaults) for item in request.partitions
        ]

    return output


def marshal_SchemaFilesystem(
    request: SchemaFilesystem,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.device is not None:
        output["device"] = request.device

    if request.format is not None:
        output["format"] = request.format

    if request.mountpoint is not None:
        output["mountpoint"] = request.mountpoint

    return output


def marshal_SchemaRAID(
    request: SchemaRAID,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.level is not None:
        output["level"] = request.level

    if request.devices is not None:
        output["devices"] = request.devices

    return output


def marshal_SchemaZFS(
    request: SchemaZFS,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.pools is not None:
        output["pools"] = [marshal_SchemaPool(item, defaults) for item in request.pools]

    return output


def marshal_Schema(
    request: Schema,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.disks is not None:
        output["disks"] = [marshal_SchemaDisk(item, defaults) for item in request.disks]

    if request.raids is not None:
        output["raids"] = [marshal_SchemaRAID(item, defaults) for item in request.raids]

    if request.filesystems is not None:
        output["filesystems"] = [
            marshal_SchemaFilesystem(item, defaults) for item in request.filesystems
        ]

    if request.zfs is not None:
        output["zfs"] = marshal_SchemaZFS(request.zfs, defaults)

    return output


def marshal_CreateServerRequestInstall(
    request: CreateServerRequestInstall,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.os_id is not None:
        output["os_id"] = request.os_id

    if request.hostname is not None:
        output["hostname"] = request.hostname

    if request.ssh_key_ids is not None:
        output["ssh_key_ids"] = request.ssh_key_ids

    if request.user is not None:
        output["user"] = request.user

    if request.password is not None:
        output["password"] = request.password

    if request.service_user is not None:
        output["service_user"] = request.service_user

    if request.service_password is not None:
        output["service_password"] = request.service_password

    if request.partitioning_schema is not None:
        output["partitioning_schema"] = marshal_Schema(
            request.partitioning_schema, defaults
        )

    return output


def marshal_CreateServerRequest(
    request: CreateServerRequest,
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

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.protected is not None:
        output["protected"] = request.protected

    if request.tags is not None:
        output["tags"] = request.tags

    if request.install is not None:
        output["install"] = marshal_CreateServerRequestInstall(
            request.install, defaults
        )

    if request.option_ids is not None:
        output["option_ids"] = request.option_ids

    return output


def marshal_AddOptionServerRequest(
    request: AddOptionServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()

    return output


def marshal_InstallServerRequest(
    request: InstallServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.os_id is not None:
        output["os_id"] = request.os_id

    if request.hostname is not None:
        output["hostname"] = request.hostname

    if request.ssh_key_ids is not None:
        output["ssh_key_ids"] = request.ssh_key_ids

    if request.user is not None:
        output["user"] = request.user

    if request.password is not None:
        output["password"] = request.password

    if request.service_user is not None:
        output["service_user"] = request.service_user

    if request.service_password is not None:
        output["service_password"] = request.service_password

    if request.partitioning_schema is not None:
        output["partitioning_schema"] = marshal_Schema(
            request.partitioning_schema, defaults
        )

    return output


def marshal_PrivateNetworkApiAddServerPrivateNetworkRequest(
    request: PrivateNetworkApiAddServerPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    return output


def marshal_PrivateNetworkApiSetServerPrivateNetworksRequest(
    request: PrivateNetworkApiSetServerPrivateNetworksRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.private_network_ids is not None:
        output["private_network_ids"] = request.private_network_ids

    return output


def marshal_RebootServerRequest(
    request: RebootServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.boot_type is not None:
        output["boot_type"] = request.boot_type

    if request.ssh_key_ids is not None:
        output["ssh_key_ids"] = request.ssh_key_ids

    return output


def marshal_StartBMCAccessRequest(
    request: StartBMCAccessRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ip is not None:
        output["ip"] = request.ip

    return output


def marshal_StartServerRequest(
    request: StartServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.boot_type is not None:
        output["boot_type"] = request.boot_type

    if request.ssh_key_ids is not None:
        output["ssh_key_ids"] = request.ssh_key_ids

    return output


def marshal_UpdateIPRequest(
    request: UpdateIPRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.reverse is not None:
        output["reverse"] = request.reverse

    return output


def marshal_UpdateServerRequest(
    request: UpdateServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.tags is not None:
        output["tags"] = request.tags

    if request.protected is not None:
        output["protected"] = request.protected

    return output


def marshal_UpdateSettingRequest(
    request: UpdateSettingRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.enabled is not None:
        output["enabled"] = request.enabled

    return output


def marshal_ValidatePartitioningSchemaRequest(
    request: ValidatePartitioningSchemaRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id

    if request.os_id is not None:
        output["os_id"] = request.os_id

    if request.partitioning_schema is not None:
        output["partitioning_schema"] = marshal_Schema(
            request.partitioning_schema, defaults
        )

    return output
