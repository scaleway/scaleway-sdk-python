# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any

from scaleway_core.profile import ProfileDefaults
from .types import (
    ServerStatus,
    HardwareSpecs,
    NetworkSpecs,
    Offer,
    Server,
    Location,
    ListLocationsResponse,
    OS,
    ListOSResponse,
    ListOffersResponse,
    ListServersResponse,
    VpsApiChangeServerHostnameRequest,
    VpsApiChangeServerPasswordRequest,
    VpsApiCreateServerRequest,
    VpsApiManageServerPowerRequest,
    VpsApiReinstallServerRequest,
)


def unmarshal_HardwareSpecs(data: Any) -> HardwareSpecs:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HardwareSpecs' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("core_count", None)
    if field is not None:
        args["core_count"] = field
    else:
        args["core_count"] = 0

    field = data.get("storage_bytes", None)
    if field is not None:
        args["storage_bytes"] = field
    else:
        args["storage_bytes"] = 0

    field = data.get("ram_bytes", None)
    if field is not None:
        args["ram_bytes"] = field
    else:
        args["ram_bytes"] = 0

    return HardwareSpecs(**args)


def unmarshal_NetworkSpecs(data: Any) -> NetworkSpecs:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NetworkSpecs' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("bandwidth_max", None)
    if field is not None:
        args["bandwidth_max"] = field
    else:
        args["bandwidth_max"] = 0

    field = data.get("bandwidth_speed_gbps", None)
    if field is not None:
        args["bandwidth_speed_gbps"] = field
    else:
        args["bandwidth_speed_gbps"] = 0

    return NetworkSpecs(**args)


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

    field = data.get("available", None)
    if field is not None:
        args["available"] = field
    else:
        args["available"] = False

    field = data.get("srn", None)
    if field is not None:
        args["srn"] = field
    else:
        args["srn"] = None

    field = data.get("hardware_specs", None)
    if field is not None:
        args["hardware_specs"] = unmarshal_HardwareSpecs(field)
    else:
        args["hardware_specs"] = None

    field = data.get("network_specs", None)
    if field is not None:
        args["network_specs"] = unmarshal_NetworkSpecs(field)
    else:
        args["network_specs"] = None

    return Offer(**args)


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

    field = data.get("hostname", None)
    if field is not None:
        args["hostname"] = field
    else:
        args["hostname"] = None

    field = data.get("os_id", None)
    if field is not None:
        args["os_id"] = field
    else:
        args["os_id"] = None

    field = data.get("location_id", None)
    if field is not None:
        args["location_id"] = field
    else:
        args["location_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ServerStatus.UNKNOWN_STATUS

    field = data.get("ips", None)
    if field is not None:
        args["ips"] = field
    else:
        args["ips"] = []

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

    field = data.get("offer_id", None)
    if field is not None:
        args["offer_id"] = field
    else:
        args["offer_id"] = None

    field = data.get("srn", None)
    if field is not None:
        args["srn"] = field
    else:
        args["srn"] = None

    return Server(**args)


def unmarshal_Location(data: Any) -> Location:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Location' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("geographic_area", None)
    if field is not None:
        args["geographic_area"] = field
    else:
        args["geographic_area"] = None

    field = data.get("country_code", None)
    if field is not None:
        args["country_code"] = field
    else:
        args["country_code"] = None

    field = data.get("city_name", None)
    if field is not None:
        args["city_name"] = field
    else:
        args["city_name"] = None

    field = data.get("available_offer_ids", None)
    if field is not None:
        args["available_offer_ids"] = field
    else:
        args["available_offer_ids"] = []

    field = data.get("srn", None)
    if field is not None:
        args["srn"] = field
    else:
        args["srn"] = None

    return Location(**args)


def unmarshal_ListLocationsResponse(data: Any) -> ListLocationsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLocationsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("locations", None)
    if field is not None:
        args["locations"] = (
            [unmarshal_Location(v) for v in field] if field is not None else None
        )
    else:
        args["locations"] = []

    return ListLocationsResponse(**args)


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

    field = data.get("main_os", None)
    if field is not None:
        args["main_os"] = field
    else:
        args["main_os"] = None

    field = data.get("srn", None)
    if field is not None:
        args["srn"] = field
    else:
        args["srn"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    return OS(**args)


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


def marshal_VpsApiChangeServerHostnameRequest(
    request: VpsApiChangeServerHostnameRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.hostname is not None:
        output["hostname"] = request.hostname

    return output


def marshal_VpsApiChangeServerPasswordRequest(
    request: VpsApiChangeServerPasswordRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_VpsApiCreateServerRequest(
    request: VpsApiCreateServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id

    if request.os_id is not None:
        output["os_id"] = request.os_id

    if request.location_id is not None:
        output["location_id"] = request.location_id

    if request.hostname is not None:
        output["hostname"] = request.hostname

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.ssh_key_id is not None:
        output["ssh_key_id"] = request.ssh_key_id

    return output


def marshal_VpsApiManageServerPowerRequest(
    request: VpsApiManageServerPowerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.action is not None:
        output["action"] = request.action

    return output


def marshal_VpsApiReinstallServerRequest(
    request: VpsApiReinstallServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.os_id is not None:
        output["os_id"] = request.os_id

    if request.ssh_key_id is not None:
        output["ssh_key_id"] = request.ssh_key_id

    return output
