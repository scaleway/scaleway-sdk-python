# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any

from .types import (
    ResourceType,
    BrmServerInfo,
    ObsDatasourceInfo,
    ObsExporterInfo,
    ServerlessContainersContainerInfo,
    ServerlessFunctionsFunctionInfo,
    ServerlessSqldbBackupInfo,
    VpcPrivateNetworkInfo,
    Resource,
    SearchResourcesResponse,
)


def unmarshal_BrmServerInfo(data: Any) -> BrmServerInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BrmServerInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = field
    else:
        args["ip"] = None

    return BrmServerInfo(**args)


def unmarshal_ObsDatasourceInfo(data: Any) -> ObsDatasourceInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ObsDatasourceInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    return ObsDatasourceInfo(**args)


def unmarshal_ObsExporterInfo(data: Any) -> ObsExporterInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ObsExporterInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("destination_type", None)
    if field is not None:
        args["destination_type"] = field
    else:
        args["destination_type"] = None

    return ObsExporterInfo(**args)


def unmarshal_ServerlessContainersContainerInfo(
    data: Any,
) -> ServerlessContainersContainerInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerlessContainersContainerInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("namespace_id", None)
    if field is not None:
        args["namespace_id"] = field
    else:
        args["namespace_id"] = None

    return ServerlessContainersContainerInfo(**args)


def unmarshal_ServerlessFunctionsFunctionInfo(
    data: Any,
) -> ServerlessFunctionsFunctionInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerlessFunctionsFunctionInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("namespace_id", None)
    if field is not None:
        args["namespace_id"] = field
    else:
        args["namespace_id"] = None

    return ServerlessFunctionsFunctionInfo(**args)


def unmarshal_ServerlessSqldbBackupInfo(data: Any) -> ServerlessSqldbBackupInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerlessSqldbBackupInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("database_id", None)
    if field is not None:
        args["database_id"] = field
    else:
        args["database_id"] = None

    return ServerlessSqldbBackupInfo(**args)


def unmarshal_VpcPrivateNetworkInfo(data: Any) -> VpcPrivateNetworkInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VpcPrivateNetworkInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("vpc_id", None)
    if field is not None:
        args["vpc_id"] = field
    else:
        args["vpc_id"] = None

    return VpcPrivateNetworkInfo(**args)


def unmarshal_Resource(data: Any) -> Resource:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Resource' failed as data isn't a dictionary."
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

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = ResourceType.UNKNOWN_TYPE

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("global", None)
    if field is not None:
        args["global_"] = field
    else:
        args["global_"] = False

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("vpc_private_network_info", None)
    if field is not None:
        args["vpc_private_network_info"] = unmarshal_VpcPrivateNetworkInfo(field)
    else:
        args["vpc_private_network_info"] = None

    field = data.get("serverless_functions_function_info", None)
    if field is not None:
        args["serverless_functions_function_info"] = (
            unmarshal_ServerlessFunctionsFunctionInfo(field)
        )
    else:
        args["serverless_functions_function_info"] = None

    field = data.get("serverless_containers_container_info", None)
    if field is not None:
        args["serverless_containers_container_info"] = (
            unmarshal_ServerlessContainersContainerInfo(field)
        )
    else:
        args["serverless_containers_container_info"] = None

    field = data.get("baremetal_server_info", None)
    if field is not None:
        args["baremetal_server_info"] = unmarshal_BrmServerInfo(field)
    else:
        args["baremetal_server_info"] = None

    field = data.get("serverless_sqldb_backup_info", None)
    if field is not None:
        args["serverless_sqldb_backup_info"] = unmarshal_ServerlessSqldbBackupInfo(
            field
        )
    else:
        args["serverless_sqldb_backup_info"] = None

    field = data.get("obs_datasource_info", None)
    if field is not None:
        args["obs_datasource_info"] = unmarshal_ObsDatasourceInfo(field)
    else:
        args["obs_datasource_info"] = None

    field = data.get("obs_exporter_info", None)
    if field is not None:
        args["obs_exporter_info"] = unmarshal_ObsExporterInfo(field)
    else:
        args["obs_exporter_info"] = None

    return Resource(**args)


def unmarshal_SearchResourcesResponse(data: Any) -> SearchResourcesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SearchResourcesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("resources", None)
    if field is not None:
        args["resources"] = (
            [unmarshal_Resource(v) for v in field] if field is not None else None
        )
    else:
        args["resources"] = []

    return SearchResourcesResponse(**args)
