# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
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
)


def unmarshal_IP(data: Any) -> IP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'IP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("address", None)
    if field is not None:
        args["address"] = field

    field = data.get("reverse", None)
    if field is not None:
        args["reverse"] = field

    field = data.get("version", None)
    if field is not None:
        args["version"] = field

    field = data.get("reverse_status", None)
    if field is not None:
        args["reverse_status"] = field

    field = data.get("reverse_status_message", None)
    if field is not None:
        args["reverse_status_message"] = field

    return IP(**args)


def unmarshal_OSOSField(data: Any) -> OSOSField:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OSOSField' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("editable", None)
    if field is not None:
        args["editable"] = field

    field = data.get("required", None)
    if field is not None:
        args["required"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("version", None)
    if field is not None:
        args["version"] = field

    field = data.get("logo_url", None)
    if field is not None:
        args["logo_url"] = field

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

    field = data.get("license_required", None)
    if field is not None:
        args["license_required"] = field

    field = data.get("allowed", None)
    if field is not None:
        args["allowed"] = field

    field = data.get("custom_partitioning_supported", None)
    if field is not None:
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

    field = data.get("os_id", None)
    if field is not None:
        args["os_id"] = field

    return LicenseOption(**args)


def unmarshal_PrivateNetworkOption(data: Any) -> PrivateNetworkOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetworkOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return PrivateNetworkOption(**args)


def unmarshal_PublicBandwidthOption(data: Any) -> PublicBandwidthOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicBandwidthOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bandwidth_in_bps", None)
    if field is not None:
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

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("core_count", None)
    if field is not None:
        args["core_count"] = field

    field = data.get("thread_count", None)
    if field is not None:
        args["thread_count"] = field

    field = data.get("frequency", None)
    if field is not None:
        args["frequency"] = field

    field = data.get("benchmark", None)
    if field is not None:
        args["benchmark"] = field

    return CPU(**args)


def unmarshal_Disk(data: Any) -> Disk:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Disk' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", None)
    if field is not None:
        args["capacity"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    return Disk(**args)


def unmarshal_Memory(data: Any) -> Memory:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Memory' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", None)
    if field is not None:
        args["capacity"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("frequency", None)
    if field is not None:
        args["frequency"] = field

    field = data.get("is_ecc", None)
    if field is not None:
        args["is_ecc"] = field

    return Memory(**args)


def unmarshal_OfferOptionOffer(data: Any) -> OfferOptionOffer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferOptionOffer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field

    field = data.get("subscription_period", None)
    if field is not None:
        args["subscription_period"] = field

    field = data.get("manageable", None)
    if field is not None:
        args["manageable"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("capacity", None)
    if field is not None:
        args["capacity"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("frequency", None)
    if field is not None:
        args["frequency"] = field

    return PersistentMemory(**args)


def unmarshal_RaidController(data: Any) -> RaidController:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RaidController' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("model", None)
    if field is not None:
        args["model"] = field

    field = data.get("raid_level", None)
    if field is not None:
        args["raid_level"] = field

    return RaidController(**args)


def unmarshal_Offer(data: Any) -> Offer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Offer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("stock", None)
    if field is not None:
        args["stock"] = field

    field = data.get("bandwidth", None)
    if field is not None:
        args["bandwidth"] = field

    field = data.get("max_bandwidth", None)
    if field is not None:
        args["max_bandwidth"] = field

    field = data.get("commercial_range", None)
    if field is not None:
        args["commercial_range"] = field

    field = data.get("disks", None)
    if field is not None:
        args["disks"] = (
            [unmarshal_Disk(v) for v in field] if field is not None else None
        )

    field = data.get("enable", None)
    if field is not None:
        args["enable"] = field

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

    field = data.get("cpus", None)
    if field is not None:
        args["cpus"] = [unmarshal_CPU(v) for v in field] if field is not None else None

    field = data.get("memories", None)
    if field is not None:
        args["memories"] = (
            [unmarshal_Memory(v) for v in field] if field is not None else None
        )

    field = data.get("quota_name", None)
    if field is not None:
        args["quota_name"] = field

    field = data.get("persistent_memories", None)
    if field is not None:
        args["persistent_memories"] = (
            [unmarshal_PersistentMemory(v) for v in field]
            if field is not None
            else None
        )

    field = data.get("raid_controllers", None)
    if field is not None:
        args["raid_controllers"] = (
            [unmarshal_RaidController(v) for v in field] if field is not None else None
        )

    field = data.get("incompatible_os_ids", None)
    if field is not None:
        args["incompatible_os_ids"] = field

    field = data.get("subscription_period", None)
    if field is not None:
        args["subscription_period"] = field

    field = data.get("operation_path", None)
    if field is not None:
        args["operation_path"] = field

    field = data.get("options", None)
    if field is not None:
        args["options"] = (
            [unmarshal_OfferOptionOffer(v) for v in field]
            if field is not None
            else None
        )

    field = data.get("private_bandwidth", None)
    if field is not None:
        args["private_bandwidth"] = field

    field = data.get("shared_bandwidth", None)
    if field is not None:
        args["shared_bandwidth"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("fee", None)
    if field is not None:
        args["fee"] = unmarshal_Money(field)
    else:
        args["fee"] = None

    return Offer(**args)


def unmarshal_Option(data: Any) -> Option:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Option' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("manageable", None)
    if field is not None:
        args["manageable"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("server_id", None)
    if field is not None:
        args["server_id"] = field

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("vlan", None)
    if field is not None:
        args["vlan"] = field
    else:
        args["vlan"] = None

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


def unmarshal_ServerInstall(data: Any) -> ServerInstall:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerInstall' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("os_id", None)
    if field is not None:
        args["os_id"] = field

    field = data.get("hostname", None)
    if field is not None:
        args["hostname"] = field

    field = data.get("ssh_key_ids", None)
    if field is not None:
        args["ssh_key_ids"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("user", None)
    if field is not None:
        args["user"] = field

    field = data.get("service_user", None)
    if field is not None:
        args["service_user"] = field

    field = data.get("service_url", None)
    if field is not None:
        args["service_url"] = field

    return ServerInstall(**args)


def unmarshal_ServerOption(data: Any) -> ServerOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("manageable", None)
    if field is not None:
        args["manageable"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("user", None)
    if field is not None:
        args["user"] = field

    field = data.get("password", None)
    if field is not None:
        args["password"] = field

    return ServerRescueServer(**args)


def unmarshal_Server(data: Any) -> Server:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Server' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

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

    field = data.get("offer_id", None)
    if field is not None:
        args["offer_id"] = field

    field = data.get("offer_name", None)
    if field is not None:
        args["offer_name"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("ips", None)
    if field is not None:
        args["ips"] = [unmarshal_IP(v) for v in field] if field is not None else None

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field

    field = data.get("boot_type", None)
    if field is not None:
        args["boot_type"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

    field = data.get("ping_status", None)
    if field is not None:
        args["ping_status"] = field

    field = data.get("options", None)
    if field is not None:
        args["options"] = (
            [unmarshal_ServerOption(v) for v in field] if field is not None else None
        )

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


def unmarshal_Setting(data: Any) -> Setting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Setting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field

    return Setting(**args)


def unmarshal_BMCAccess(data: Any) -> BMCAccess:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BMCAccess' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("url", None)
    if field is not None:
        args["url"] = field

    field = data.get("login", None)
    if field is not None:
        args["login"] = field

    field = data.get("password", None)
    if field is not None:
        args["password"] = field

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

    args: Dict[str, Any] = {}

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

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("os", None)
    if field is not None:
        args["os"] = [unmarshal_OS(v) for v in field] if field is not None else None

    return ListOSResponse(**args)


def unmarshal_ListOffersResponse(data: Any) -> ListOffersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOffersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("offers", None)
    if field is not None:
        args["offers"] = (
            [unmarshal_Offer(v) for v in field] if field is not None else None
        )

    return ListOffersResponse(**args)


def unmarshal_ListOptionsResponse(data: Any) -> ListOptionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOptionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("options", None)
    if field is not None:
        args["options"] = (
            [unmarshal_Option(v) for v in field] if field is not None else None
        )

    return ListOptionsResponse(**args)


def unmarshal_ServerEvent(data: Any) -> ServerEvent:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerEvent' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("action", None)
    if field is not None:
        args["action"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("events", None)
    if field is not None:
        args["events"] = (
            [unmarshal_ServerEvent(v) for v in field] if field is not None else None
        )

    return ListServerEventsResponse(**args)


def unmarshal_ListServerPrivateNetworksResponse(
    data: Any,
) -> ListServerPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server_private_networks", None)
    if field is not None:
        args["server_private_networks"] = (
            [unmarshal_ServerPrivateNetwork(v) for v in field]
            if field is not None
            else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListServerPrivateNetworksResponse(**args)


def unmarshal_ListServersResponse(data: Any) -> ListServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("servers", None)
    if field is not None:
        args["servers"] = (
            [unmarshal_Server(v) for v in field] if field is not None else None
        )

    return ListServersResponse(**args)


def unmarshal_ListSettingsResponse(data: Any) -> ListSettingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSettingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("settings", None)
    if field is not None:
        args["settings"] = (
            [unmarshal_Setting(v) for v in field] if field is not None else None
        )

    return ListSettingsResponse(**args)


def unmarshal_SetServerPrivateNetworksResponse(
    data: Any,
) -> SetServerPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetServerPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server_private_networks", None)
    if field is not None:
        args["server_private_networks"] = (
            [unmarshal_ServerPrivateNetwork(v) for v in field]
            if field is not None
            else None
        )

    return SetServerPrivateNetworksResponse(**args)


def marshal_AddOptionServerRequest(
    request: AddOptionServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()

    return output


def marshal_CreateServerRequestInstall(
    request: CreateServerRequestInstall,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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

    return output


def marshal_CreateServerRequest(
    request: CreateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project_id", request.project_id, defaults.default_project_id
                ),
                OneOfPossibility(
                    "organization_id",
                    request.organization_id,
                    defaults.default_organization_id,
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

    if request.tags is not None:
        output["tags"] = request.tags

    if request.install is not None:
        output["install"] = marshal_CreateServerRequestInstall(
            request.install, defaults
        )

    if request.option_ids is not None:
        output["option_ids"] = request.option_ids

    return output


def marshal_InstallServerRequest(
    request: InstallServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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

    return output


def marshal_PrivateNetworkApiAddServerPrivateNetworkRequest(
    request: PrivateNetworkApiAddServerPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    return output


def marshal_PrivateNetworkApiSetServerPrivateNetworksRequest(
    request: PrivateNetworkApiSetServerPrivateNetworksRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.private_network_ids is not None:
        output["private_network_ids"] = request.private_network_ids

    return output


def marshal_RebootServerRequest(
    request: RebootServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.boot_type is not None:
        output["boot_type"] = str(request.boot_type)

    return output


def marshal_StartBMCAccessRequest(
    request: StartBMCAccessRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip is not None:
        output["ip"] = request.ip

    return output


def marshal_StartServerRequest(
    request: StartServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.boot_type is not None:
        output["boot_type"] = str(request.boot_type)

    return output


def marshal_UpdateIPRequest(
    request: UpdateIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.reverse is not None:
        output["reverse"] = request.reverse

    return output


def marshal_UpdateServerRequest(
    request: UpdateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateSettingRequest(
    request: UpdateSettingRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.enabled is not None:
        output["enabled"] = request.enabled

    return output
