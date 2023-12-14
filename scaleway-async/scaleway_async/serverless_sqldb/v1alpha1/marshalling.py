# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from dateutil import parser
from .types import (
    Database,
    DatabaseBackup,
    ListDatabaseBackupsResponse,
    ListDatabasesResponse,
    CreateDatabaseRequest,
    UpdateDatabaseRequest,
    RestoreDatabaseFromBackupRequest,
)


def unmarshal_Database(data: Any) -> Database:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Database' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cpu_current", None)
    args["cpu_current"] = field

    field = data.get("cpu_max", None)
    args["cpu_max"] = field

    field = data.get("cpu_min", None)
    args["cpu_min"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("endpoint", None)
    args["endpoint"] = field

    field = data.get("engine_major_version", None)
    args["engine_major_version"] = field

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

    field = data.get("started", None)
    args["started"] = field

    field = data.get("status", None)
    args["status"] = field

    return Database(**args)


def unmarshal_DatabaseBackup(data: Any) -> DatabaseBackup:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DatabaseBackup' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("database_id", None)
    args["database_id"] = field

    field = data.get("download_url", None)
    args["download_url"] = field

    field = data.get("download_url_expires_at", None)
    args["download_url_expires_at"] = (
        parser.isoparse(field) if type(field) is str else field
    )

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("size", None)
    args["size"] = field

    field = data.get("status", None)
    args["status"] = field

    return DatabaseBackup(**args)


def unmarshal_ListDatabaseBackupsResponse(data: Any) -> ListDatabaseBackupsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDatabaseBackupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("backups", None)
    args["backups"] = (
        [unmarshal_DatabaseBackup(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListDatabaseBackupsResponse(**args)


def unmarshal_ListDatabasesResponse(data: Any) -> ListDatabasesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDatabasesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("databases", None)
    args["databases"] = (
        [unmarshal_Database(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListDatabasesResponse(**args)


def marshal_CreateDatabaseRequest(
    request: CreateDatabaseRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.cpu_max is not None:
        output["cpu_max"] = request.cpu_max

    if request.cpu_min is not None:
        output["cpu_min"] = request.cpu_min

    if request.from_backup_id is not None:
        output["from_backup_id"] = request.from_backup_id

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_RestoreDatabaseFromBackupRequest(
    request: RestoreDatabaseFromBackupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backup_id is not None:
        output["backup_id"] = request.backup_id

    return output


def marshal_UpdateDatabaseRequest(
    request: UpdateDatabaseRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.cpu_max is not None:
        output["cpu_max"] = request.cpu_max

    if request.cpu_min is not None:
        output["cpu_min"] = request.cpu_min

    return output
