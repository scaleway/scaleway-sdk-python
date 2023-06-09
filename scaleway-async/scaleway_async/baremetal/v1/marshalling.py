# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_Money,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from dateutil import parser
from .types import (
    ServerBootType,
    BMCAccess,
    CPU,
    CreateServerRequestInstall,
    Disk,
    GetServerMetricsResponse,
    IP,
    ListOSResponse,
    ListOffersResponse,
    ListOptionsResponse,
    ListServerEventsResponse,
    ListServerPrivateNetworksResponse,
    ListServersResponse,
    ListSettingsResponse,
    Memory,
    OS,
    OSOSField,
    Offer,
    OfferOptionOffer,
    Option,
    PersistentMemory,
    RaidController,
    Server,
    ServerEvent,
    ServerInstall,
    ServerOption,
    ServerPrivateNetwork,
    ServerRescueServer,
    SetServerPrivateNetworksResponse,
    Setting,
    CreateServerRequest,
    UpdateServerRequest,
    InstallServerRequest,
    RebootServerRequest,
    StartServerRequest,
    StartBMCAccessRequest,
    UpdateIPRequest,
    AddOptionServerRequest,
    UpdateSettingRequest,
    PrivateNetworkApiAddServerPrivateNetworkRequest,
    PrivateNetworkApiSetServerPrivateNetworksRequest,
)


def unmarshal_CPU(data: Any) -> CPU:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CPU' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("benchmark", None)
    args["benchmark"] = field

    field = data.get("core_count", None)
    args["core_count"] = field

    field = data.get("frequency", None)
    args["frequency"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("thread_count", None)
    args["thread_count"] = field

    return CPU(**args)


def unmarshal_Disk(data: Any) -> Disk:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Disk' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", None)
    args["capacity"] = field

    field = data.get("type_", None)
    args["type_"] = field

    return Disk(**args)


def unmarshal_IP(data: Any) -> IP:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'IP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address", None)
    args["address"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("reverse", None)
    args["reverse"] = field

    field = data.get("reverse_status", None)
    args["reverse_status"] = field

    field = data.get("reverse_status_message", None)
    args["reverse_status_message"] = field

    field = data.get("version", None)
    args["version"] = field

    return IP(**args)


def unmarshal_Memory(data: Any) -> Memory:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Memory' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", None)
    args["capacity"] = field

    field = data.get("frequency", None)
    args["frequency"] = field

    field = data.get("is_ecc", None)
    args["is_ecc"] = field

    field = data.get("type_", None)
    args["type_"] = field

    return Memory(**args)


def unmarshal_OSOSField(data: Any) -> OSOSField:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'OSOSField' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("default_value", None)
    args["default_value"] = field

    field = data.get("editable", None)
    args["editable"] = field

    field = data.get("required", None)
    args["required"] = field

    return OSOSField(**args)


def unmarshal_OfferOptionOffer(data: Any) -> OfferOptionOffer:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'OfferOptionOffer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("enabled", None)
    args["enabled"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("manageable", None)
    args["manageable"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("os_id", None)
    args["os_id"] = field

    field = data.get("price", None)
    args["price"] = unmarshal_Money(field) if field is not None else None

    field = data.get("subscription_period", None)
    args["subscription_period"] = field

    return OfferOptionOffer(**args)


def unmarshal_PersistentMemory(data: Any) -> PersistentMemory:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'PersistentMemory' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", None)
    args["capacity"] = field

    field = data.get("frequency", None)
    args["frequency"] = field

    field = data.get("type_", None)
    args["type_"] = field

    return PersistentMemory(**args)


def unmarshal_RaidController(data: Any) -> RaidController:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RaidController' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("model", None)
    args["model"] = field

    field = data.get("raid_level", None)
    args["raid_level"] = field

    return RaidController(**args)


def unmarshal_ServerInstall(data: Any) -> ServerInstall:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerInstall' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hostname", None)
    args["hostname"] = field

    field = data.get("os_id", None)
    args["os_id"] = field

    field = data.get("service_url", None)
    args["service_url"] = field

    field = data.get("service_user", None)
    args["service_user"] = field

    field = data.get("ssh_key_ids", None)
    args["ssh_key_ids"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("user", None)
    args["user"] = field

    return ServerInstall(**args)


def unmarshal_ServerOption(data: Any) -> ServerOption:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("manageable", None)
    args["manageable"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("status", None)
    args["status"] = field

    return ServerOption(**args)


def unmarshal_ServerRescueServer(data: Any) -> ServerRescueServer:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerRescueServer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("password", None)
    args["password"] = field

    field = data.get("user", None)
    args["user"] = field

    return ServerRescueServer(**args)


def unmarshal_OS(data: Any) -> OS:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'OS' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("allowed", None)
    args["allowed"] = field

    field = data.get("enabled", None)
    args["enabled"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("license_required", None)
    args["license_required"] = field

    field = data.get("logo_url", None)
    args["logo_url"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("password", None)
    args["password"] = unmarshal_OSOSField(field) if field is not None else None

    field = data.get("service_password", None)
    args["service_password"] = unmarshal_OSOSField(field) if field is not None else None

    field = data.get("service_user", None)
    args["service_user"] = unmarshal_OSOSField(field) if field is not None else None

    field = data.get("ssh", None)
    args["ssh"] = unmarshal_OSOSField(field) if field is not None else None

    field = data.get("user", None)
    args["user"] = unmarshal_OSOSField(field) if field is not None else None

    field = data.get("version", None)
    args["version"] = field

    return OS(**args)


def unmarshal_Offer(data: Any) -> Offer:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Offer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bandwidth", None)
    args["bandwidth"] = field

    field = data.get("commercial_range", None)
    args["commercial_range"] = field

    field = data.get("cpus", None)
    args["cpus"] = [unmarshal_CPU(v) for v in field] if field is not None else None

    field = data.get("disks", None)
    args["disks"] = [unmarshal_Disk(v) for v in field] if field is not None else None

    field = data.get("enable", None)
    args["enable"] = field

    field = data.get("fee", None)
    args["fee"] = unmarshal_Money(field) if field is not None else None

    field = data.get("id", None)
    args["id"] = field

    field = data.get("incompatible_os_ids", None)
    args["incompatible_os_ids"] = field

    field = data.get("memories", None)
    args["memories"] = (
        [unmarshal_Memory(v) for v in field] if field is not None else None
    )

    field = data.get("name", None)
    args["name"] = field

    field = data.get("operation_path", None)
    args["operation_path"] = field

    field = data.get("options", None)
    args["options"] = (
        [unmarshal_OfferOptionOffer(v) for v in field] if field is not None else None
    )

    field = data.get("persistent_memories", None)
    args["persistent_memories"] = (
        [unmarshal_PersistentMemory(v) for v in field] if field is not None else None
    )

    field = data.get("price_per_hour", None)
    args["price_per_hour"] = unmarshal_Money(field) if field is not None else None

    field = data.get("price_per_month", None)
    args["price_per_month"] = unmarshal_Money(field) if field is not None else None

    field = data.get("private_bandwidth", None)
    args["private_bandwidth"] = field

    field = data.get("quota_name", None)
    args["quota_name"] = field

    field = data.get("raid_controllers", None)
    args["raid_controllers"] = (
        [unmarshal_RaidController(v) for v in field] if field is not None else None
    )

    field = data.get("shared_bandwidth", None)
    args["shared_bandwidth"] = field

    field = data.get("stock", None)
    args["stock"] = field

    field = data.get("subscription_period", None)
    args["subscription_period"] = field

    field = data.get("tags", None)
    args["tags"] = field

    return Offer(**args)


def unmarshal_Option(data: Any) -> Option:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Option' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("manageable", None)
    args["manageable"] = field

    field = data.get("name", None)
    args["name"] = field

    return Option(**args)


def unmarshal_Server(data: Any) -> Server:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Server' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("boot_type", None)
    args["boot_type"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("domain", None)
    args["domain"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("install", None)
    args["install"] = unmarshal_ServerInstall(field) if field is not None else None

    field = data.get("ips", None)
    args["ips"] = [unmarshal_IP(v) for v in field] if field is not None else None

    field = data.get("name", None)
    args["name"] = field

    field = data.get("offer_id", None)
    args["offer_id"] = field

    field = data.get("offer_name", None)
    args["offer_name"] = field

    field = data.get("options", None)
    args["options"] = (
        [unmarshal_ServerOption(v) for v in field] if field is not None else None
    )

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("ping_status", None)
    args["ping_status"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("rescue_server", None)
    args["rescue_server"] = (
        unmarshal_ServerRescueServer(field) if field is not None else None
    )

    field = data.get("status", None)
    args["status"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("zone", None)
    args["zone"] = field

    return Server(**args)


def unmarshal_ServerEvent(data: Any) -> ServerEvent:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerEvent' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("action", None)
    args["action"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return ServerEvent(**args)


def unmarshal_ServerPrivateNetwork(data: Any) -> ServerPrivateNetwork:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerPrivateNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("private_network_id", None)
    args["private_network_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("server_id", None)
    args["server_id"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("vlan", None)
    args["vlan"] = field

    return ServerPrivateNetwork(**args)


def unmarshal_Setting(data: Any) -> Setting:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Setting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("enabled", None)
    args["enabled"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("type_", None)
    args["type_"] = field

    return Setting(**args)


def unmarshal_BMCAccess(data: Any) -> BMCAccess:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'BMCAccess' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("login", None)
    args["login"] = field

    field = data.get("password", None)
    args["password"] = field

    field = data.get("url", None)
    args["url"] = field

    return BMCAccess(**args)


def unmarshal_GetServerMetricsResponse(data: Any) -> GetServerMetricsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetServerMetricsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pings", None)
    args["pings"] = unmarshal_TimeSeries(field) if field is not None else None

    return GetServerMetricsResponse(**args)


def unmarshal_ListOSResponse(data: Any) -> ListOSResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListOSResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("os", None)
    args["os"] = [unmarshal_OS(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListOSResponse(**args)


def unmarshal_ListOffersResponse(data: Any) -> ListOffersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListOffersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("offers", None)
    args["offers"] = [unmarshal_Offer(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListOffersResponse(**args)


def unmarshal_ListOptionsResponse(data: Any) -> ListOptionsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListOptionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("options", None)
    args["options"] = (
        [unmarshal_Option(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListOptionsResponse(**args)


def unmarshal_ListServerEventsResponse(data: Any) -> ListServerEventsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListServerEventsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("events", None)
    args["events"] = (
        [unmarshal_ServerEvent(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListServerEventsResponse(**args)


def unmarshal_ListServerPrivateNetworksResponse(
    data: Any,
) -> ListServerPrivateNetworksResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListServerPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server_private_networks", None)
    args["server_private_networks"] = (
        [unmarshal_ServerPrivateNetwork(v) for v in field]
        if field is not None
        else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListServerPrivateNetworksResponse(**args)


def unmarshal_ListServersResponse(data: Any) -> ListServersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("servers", None)
    args["servers"] = (
        [unmarshal_Server(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListServersResponse(**args)


def unmarshal_ListSettingsResponse(data: Any) -> ListSettingsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSettingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("settings", None)
    args["settings"] = (
        [unmarshal_Setting(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListSettingsResponse(**args)


def unmarshal_SetServerPrivateNetworksResponse(
    data: Any,
) -> SetServerPrivateNetworksResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetServerPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server_private_networks", None)
    args["server_private_networks"] = (
        [unmarshal_ServerPrivateNetwork(v) for v in field]
        if field is not None
        else None
    )

    return SetServerPrivateNetworksResponse(**args)


def marshal_CreateServerRequestInstall(
    request: CreateServerRequestInstall,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "hostname": request.hostname,
        "os_id": request.os_id,
        "password": request.password,
        "service_password": request.service_password,
        "service_user": request.service_user,
        "ssh_key_ids": request.ssh_key_ids,
        "user": request.user,
    }


def marshal_AddOptionServerRequest(
    request: AddOptionServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "expires_at": request.expires_at,
    }


def marshal_CreateServerRequest(
    request: CreateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
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
        "description": request.description,
        "install": marshal_CreateServerRequestInstall(request.install, defaults)
        if request.install is not None
        else None,
        "name": request.name,
        "offer_id": request.offer_id,
        "option_ids": request.option_ids,
        "tags": request.tags,
    }


def marshal_InstallServerRequest(
    request: InstallServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "hostname": request.hostname,
        "os_id": request.os_id,
        "password": request.password,
        "service_password": request.service_password,
        "service_user": request.service_user,
        "ssh_key_ids": request.ssh_key_ids,
        "user": request.user,
    }


def marshal_PrivateNetworkApiAddServerPrivateNetworkRequest(
    request: PrivateNetworkApiAddServerPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "private_network_id": request.private_network_id,
    }


def marshal_PrivateNetworkApiSetServerPrivateNetworksRequest(
    request: PrivateNetworkApiSetServerPrivateNetworksRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "private_network_ids": request.private_network_ids,
    }


def marshal_RebootServerRequest(
    request: RebootServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "boot_type": ServerBootType(request.boot_type),
    }


def marshal_StartBMCAccessRequest(
    request: StartBMCAccessRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "ip": request.ip,
    }


def marshal_StartServerRequest(
    request: StartServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "boot_type": ServerBootType(request.boot_type),
    }


def marshal_UpdateIPRequest(
    request: UpdateIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "reverse": request.reverse,
    }


def marshal_UpdateServerRequest(
    request: UpdateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "name": request.name,
        "tags": request.tags,
    }


def marshal_UpdateSettingRequest(
    request: UpdateSettingRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "enabled": request.enabled,
    }
