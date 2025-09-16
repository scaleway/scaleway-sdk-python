# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    DeploymentStatus,
    EndpointPrivateNetworkDetails,
    EndpointPublicDetails,
    EndpointService,
    Endpoint,
    Database,
    Deployment,
    User,
    ListDatabasesResponse,
    ListDeploymentsResponse,
    Preset,
    ListPresetsResponse,
    ListUsersResponse,
    Version,
    ListVersionsResponse,
    CreateDatabaseRequest,
    EndpointSpecPrivateNetworkDetails,
    EndpointSpecPublicDetails,
    EndpointSpec,
    CreateDeploymentRequest,
    CreateEndpointRequest,
    CreateUserRequest,
    UpdateDeploymentRequest,
    UpdateUserRequest,
)


def unmarshal_EndpointPrivateNetworkDetails(data: Any) -> EndpointPrivateNetworkDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointPrivateNetworkDetails' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    return EndpointPrivateNetworkDetails(**args)


def unmarshal_EndpointPublicDetails(data: Any) -> EndpointPublicDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointPublicDetails' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return EndpointPublicDetails(**args)


def unmarshal_EndpointService(data: Any) -> EndpointService:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointService' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("protocol", None)
    if field is not None:
        args["protocol"] = field
    else:
        args["protocol"] = None

    field = data.get("port", None)
    if field is not None:
        args["port"] = field
    else:
        args["port"] = None

    return EndpointService(**args)


def unmarshal_Endpoint(data: Any) -> Endpoint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Endpoint' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("dns_record", None)
    if field is not None:
        args["dns_record"] = field
    else:
        args["dns_record"] = None

    field = data.get("services", None)
    if field is not None:
        args["services"] = (
            [unmarshal_EndpointService(v) for v in field] if field is not None else None
        )
    else:
        args["services"] = []

    field = data.get("private_network", None)
    if field is not None:
        args["private_network"] = unmarshal_EndpointPrivateNetworkDetails(field)
    else:
        args["private_network"] = None

    field = data.get("public", None)
    if field is not None:
        args["public"] = unmarshal_EndpointPublicDetails(field)
    else:
        args["public"] = None

    return Endpoint(**args)


def unmarshal_Database(data: Any) -> Database:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Database' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = 0

    return Database(**args)


def unmarshal_Deployment(data: Any) -> Deployment:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Deployment' failed as data isn't a dictionary."
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

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DeploymentStatus.UNKNOWN_STATUS

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = None

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

    field = data.get("replica_count", None)
    if field is not None:
        args["replica_count"] = field
    else:
        args["replica_count"] = 0

    field = data.get("cpu_min", None)
    if field is not None:
        args["cpu_min"] = field
    else:
        args["cpu_min"] = 0

    field = data.get("cpu_max", None)
    if field is not None:
        args["cpu_max"] = field
    else:
        args["cpu_max"] = 0

    field = data.get("endpoints", None)
    if field is not None:
        args["endpoints"] = (
            [unmarshal_Endpoint(v) for v in field] if field is not None else None
        )
    else:
        args["endpoints"] = []

    field = data.get("ram_per_cpu", None)
    if field is not None:
        args["ram_per_cpu"] = field
    else:
        args["ram_per_cpu"] = 0

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    return Deployment(**args)


def unmarshal_User(data: Any) -> User:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'User' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("is_admin", None)
    if field is not None:
        args["is_admin"] = field
    else:
        args["is_admin"] = False

    return User(**args)


def unmarshal_ListDatabasesResponse(data: Any) -> ListDatabasesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabasesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("databases", None)
    if field is not None:
        args["databases"] = (
            [unmarshal_Database(v) for v in field] if field is not None else None
        )
    else:
        args["databases"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListDatabasesResponse(**args)


def unmarshal_ListDeploymentsResponse(data: Any) -> ListDeploymentsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDeploymentsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("deployments", None)
    if field is not None:
        args["deployments"] = (
            [unmarshal_Deployment(v) for v in field] if field is not None else None
        )
    else:
        args["deployments"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListDeploymentsResponse(**args)


def unmarshal_Preset(data: Any) -> Preset:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Preset' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("category", None)
    if field is not None:
        args["category"] = field
    else:
        args["category"] = None

    field = data.get("cpu_min", None)
    if field is not None:
        args["cpu_min"] = field
    else:
        args["cpu_min"] = 0

    field = data.get("cpu_max", None)
    if field is not None:
        args["cpu_max"] = field
    else:
        args["cpu_max"] = 0

    field = data.get("ram_per_cpu", None)
    if field is not None:
        args["ram_per_cpu"] = field
    else:
        args["ram_per_cpu"] = 0

    field = data.get("replica_count", None)
    if field is not None:
        args["replica_count"] = field
    else:
        args["replica_count"] = 0

    return Preset(**args)


def unmarshal_ListPresetsResponse(data: Any) -> ListPresetsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPresetsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("presets", None)
    if field is not None:
        args["presets"] = (
            [unmarshal_Preset(v) for v in field] if field is not None else None
        )
    else:
        args["presets"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListPresetsResponse(**args)


def unmarshal_ListUsersResponse(data: Any) -> ListUsersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListUsersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("users", None)
    if field is not None:
        args["users"] = (
            [unmarshal_User(v) for v in field] if field is not None else None
        )
    else:
        args["users"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListUsersResponse(**args)


def unmarshal_Version(data: Any) -> Version:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Version' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = None

    field = data.get("end_of_life_at", None)
    if field is not None:
        args["end_of_life_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["end_of_life_at"] = None

    return Version(**args)


def unmarshal_ListVersionsResponse(data: Any) -> ListVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVersionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_Version(v) for v in field] if field is not None else None
        )
    else:
        args["versions"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListVersionsResponse(**args)


def marshal_CreateDatabaseRequest(
    request: CreateDatabaseRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_EndpointSpecPrivateNetworkDetails(
    request: EndpointSpecPrivateNetworkDetails,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    return output


def marshal_EndpointSpecPublicDetails(
    request: EndpointSpecPublicDetails,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    return output


def marshal_EndpointSpec(
    request: EndpointSpec,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="public",
                    value=request.public,
                    marshal_func=marshal_EndpointSpecPublicDetails,
                ),
                OneOfPossibility(
                    param="private_network",
                    value=request.private_network,
                    marshal_func=marshal_EndpointSpecPrivateNetworkDetails,
                ),
            ]
        ),
    )

    return output


def marshal_CreateDeploymentRequest(
    request: CreateDeploymentRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.version is not None:
        output["version"] = request.version

    if request.replica_count is not None:
        output["replica_count"] = request.replica_count

    if request.password is not None:
        output["password"] = request.password

    if request.cpu_min is not None:
        output["cpu_min"] = request.cpu_min

    if request.cpu_max is not None:
        output["cpu_max"] = request.cpu_max

    if request.ram_per_cpu is not None:
        output["ram_per_cpu"] = request.ram_per_cpu

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.endpoints is not None:
        output["endpoints"] = [
            marshal_EndpointSpec(item, defaults) for item in request.endpoints
        ]

    return output


def marshal_CreateEndpointRequest(
    request: CreateEndpointRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.deployment_id is not None:
        output["deployment_id"] = request.deployment_id

    if request.endpoint is not None:
        output["endpoint"] = marshal_EndpointSpec(request.endpoint, defaults)

    return output


def marshal_CreateUserRequest(
    request: CreateUserRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.password is not None:
        output["password"] = request.password

    if request.is_admin is not None:
        output["is_admin"] = request.is_admin

    return output


def marshal_UpdateDeploymentRequest(
    request: UpdateDeploymentRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.cpu_min is not None:
        output["cpu_min"] = request.cpu_min

    if request.cpu_max is not None:
        output["cpu_max"] = request.cpu_max

    if request.replica_count is not None:
        output["replica_count"] = request.replica_count

    return output


def marshal_UpdateUserRequest(
    request: UpdateUserRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password

    if request.is_admin is not None:
        output["is_admin"] = request.is_admin

    return output
