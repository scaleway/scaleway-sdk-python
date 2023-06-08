# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from dateutil import parser
from .types import (
    AddSubnetsResponse,
    DeleteSubnetsResponse,
    ListPrivateNetworksResponse,
    ListVPCsResponse,
    PrivateNetwork,
    SetSubnetsResponse,
    Subnet,
    VPC,
    CreateVPCRequest,
    UpdateVPCRequest,
    CreatePrivateNetworkRequest,
    UpdatePrivateNetworkRequest,
    MigrateZonalPrivateNetworksRequest,
    SetSubnetsRequest,
    AddSubnetsRequest,
    DeleteSubnetsRequest,
)


def unmarshal_Subnet(data: Any) -> Subnet:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Subnet' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("subnet", None)
    args["subnet"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Subnet(**args)


def unmarshal_PrivateNetwork(data: Any) -> PrivateNetwork:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'PrivateNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("subnets", None)
    args["subnets"] = (
        [unmarshal_Subnet(v) for v in field] if field is not None else None
    )

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("vpc_id", None)
    args["vpc_id"] = field

    return PrivateNetwork(**args)


def unmarshal_VPC(data: Any) -> VPC:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'VPC' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("is_default", None)
    args["is_default"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("private_network_count", None)
    args["private_network_count"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return VPC(**args)


def unmarshal_AddSubnetsResponse(data: Any) -> AddSubnetsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'AddSubnetsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subnets", None)
    args["subnets"] = field

    return AddSubnetsResponse(**args)


def unmarshal_DeleteSubnetsResponse(data: Any) -> DeleteSubnetsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DeleteSubnetsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subnets", None)
    args["subnets"] = field

    return DeleteSubnetsResponse(**args)


def unmarshal_ListPrivateNetworksResponse(data: Any) -> ListPrivateNetworksResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_networks", None)
    args["private_networks"] = (
        [unmarshal_PrivateNetwork(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListPrivateNetworksResponse(**args)


def unmarshal_ListVPCsResponse(data: Any) -> ListVPCsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListVPCsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("vpcs", None)
    args["vpcs"] = [unmarshal_VPC(v) for v in field] if field is not None else None

    return ListVPCsResponse(**args)


def unmarshal_SetSubnetsResponse(data: Any) -> SetSubnetsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetSubnetsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subnets", None)
    args["subnets"] = field

    return SetSubnetsResponse(**args)


def marshal_AddSubnetsRequest(
    request: AddSubnetsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "subnets": request.subnets,
    }


def marshal_CreatePrivateNetworkRequest(
    request: CreatePrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "project_id": request.project_id or defaults.default_project_id,
        "subnets": request.subnets,
        "tags": request.tags,
        "vpc_id": request.vpc_id,
    }


def marshal_CreateVPCRequest(
    request: CreateVPCRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "default_private_network_name": request.default_private_network_name,
        "name": request.name,
        "project_id": request.project_id or defaults.default_project_id,
        "tags": request.tags,
    }


def marshal_DeleteSubnetsRequest(
    request: DeleteSubnetsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "subnets": request.subnets,
    }


def marshal_MigrateZonalPrivateNetworksRequest(
    request: MigrateZonalPrivateNetworksRequest,
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
        "private_network_ids": request.private_network_ids,
    }


def marshal_SetSubnetsRequest(
    request: SetSubnetsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "subnets": request.subnets,
    }


def marshal_UpdatePrivateNetworkRequest(
    request: UpdatePrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "tags": request.tags,
    }


def marshal_UpdateVPCRequest(
    request: UpdateVPCRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "tags": request.tags,
    }
