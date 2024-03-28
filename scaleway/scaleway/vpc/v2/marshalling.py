# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    Subnet,
    PrivateNetwork,
    VPC,
    AddSubnetsResponse,
    DeleteSubnetsResponse,
    ListPrivateNetworksResponse,
    ListVPCsResponse,
    SetSubnetsResponse,
    AddSubnetsRequest,
    CreatePrivateNetworkRequest,
    CreateVPCRequest,
    DeleteSubnetsRequest,
    MigrateZonalPrivateNetworksRequest,
    SetSubnetsRequest,
    UpdatePrivateNetworkRequest,
    UpdateVPCRequest,
)


def unmarshal_Subnet(data: Any) -> Subnet:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Subnet' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("subnet", None)
    if field is not None:
        args["subnet"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Subnet(**args)


def unmarshal_PrivateNetwork(data: Any) -> PrivateNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("subnets", None)
    if field is not None:
        args["subnets"] = (
            [unmarshal_Subnet(v) for v in field] if field is not None else None
        )

    field = data.get("vpc_id", None)
    if field is not None:
        args["vpc_id"] = field

    field = data.get("dhcp_enabled", None)
    if field is not None:
        args["dhcp_enabled"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return PrivateNetwork(**args)


def unmarshal_VPC(data: Any) -> VPC:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VPC' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("is_default", None)
    if field is not None:
        args["is_default"] = field

    field = data.get("private_network_count", None)
    if field is not None:
        args["private_network_count"] = field

    field = data.get("routing_enabled", None)
    if field is not None:
        args["routing_enabled"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return VPC(**args)


def unmarshal_AddSubnetsResponse(data: Any) -> AddSubnetsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddSubnetsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subnets", None)
    if field is not None:
        args["subnets"] = field

    return AddSubnetsResponse(**args)


def unmarshal_DeleteSubnetsResponse(data: Any) -> DeleteSubnetsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteSubnetsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subnets", None)
    if field is not None:
        args["subnets"] = field

    return DeleteSubnetsResponse(**args)


def unmarshal_ListPrivateNetworksResponse(data: Any) -> ListPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_networks", None)
    if field is not None:
        args["private_networks"] = (
            [unmarshal_PrivateNetwork(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListPrivateNetworksResponse(**args)


def unmarshal_ListVPCsResponse(data: Any) -> ListVPCsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVPCsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("vpcs", None)
    if field is not None:
        args["vpcs"] = [unmarshal_VPC(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListVPCsResponse(**args)


def unmarshal_SetSubnetsResponse(data: Any) -> SetSubnetsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetSubnetsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subnets", None)
    if field is not None:
        args["subnets"] = field

    return SetSubnetsResponse(**args)


def marshal_AddSubnetsRequest(
    request: AddSubnetsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subnets is not None:
        output["subnets"] = request.subnets

    return output


def marshal_CreatePrivateNetworkRequest(
    request: CreatePrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.subnets is not None:
        output["subnets"] = request.subnets

    if request.vpc_id is not None:
        output["vpc_id"] = request.vpc_id

    return output


def marshal_CreateVPCRequest(
    request: CreateVPCRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.enable_routing is not None:
        output["enable_routing"] = request.enable_routing

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_DeleteSubnetsRequest(
    request: DeleteSubnetsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subnets is not None:
        output["subnets"] = request.subnets

    return output


def marshal_MigrateZonalPrivateNetworksRequest(
    request: MigrateZonalPrivateNetworksRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "organization_id",
                    request.organization_id,
                    defaults.default_organization_id,
                ),
                OneOfPossibility(
                    "project_id", request.project_id, defaults.default_project_id
                ),
            ]
        ),
    )

    if request.private_network_ids is not None:
        output["private_network_ids"] = request.private_network_ids

    return output


def marshal_SetSubnetsRequest(
    request: SetSubnetsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subnets is not None:
        output["subnets"] = request.subnets

    return output


def marshal_UpdatePrivateNetworkRequest(
    request: UpdatePrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateVPCRequest(
    request: UpdateVPCRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    return output
