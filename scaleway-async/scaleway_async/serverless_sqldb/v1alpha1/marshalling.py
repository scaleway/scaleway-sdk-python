# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    DatabaseBackup,
    Database,
    ListDatabaseBackupsResponse,
    ListDatabasesResponse,
    CreateDatabaseRequest,
    RestoreDatabaseFromBackupRequest,
    UpdateDatabaseRequest,
)


def unmarshal_DatabaseBackup(data: Any) -> DatabaseBackup:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DatabaseBackup' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("database_id", None)
    if field is not None:
        args["database_id"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("expires_at", None)
    if field is not None:
        args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expires_at"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = None

    field = data.get("db_size", None)
    if field is not None:
        args["db_size"] = field
    else:
        args["db_size"] = None

    field = data.get("download_url", None)
    if field is not None:
        args["download_url"] = field
    else:
        args["download_url"] = None

    field = data.get("download_url_expires_at", None)
    if field is not None:
        args["download_url_expires_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["download_url_expires_at"] = None

    return DatabaseBackup(**args)


def unmarshal_Database(data: Any) -> Database:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Database' failed as data isn't a dictionary."
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

    field = data.get("endpoint", None)
    if field is not None:
        args["endpoint"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("cpu_min", None)
    if field is not None:
        args["cpu_min"] = field

    field = data.get("cpu_max", None)
    if field is not None:
        args["cpu_max"] = field

    field = data.get("cpu_current", None)
    if field is not None:
        args["cpu_current"] = field

    field = data.get("started", None)
    if field is not None:
        args["started"] = field

    field = data.get("engine_major_version", None)
    if field is not None:
        args["engine_major_version"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return Database(**args)


def unmarshal_ListDatabaseBackupsResponse(data: Any) -> ListDatabaseBackupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabaseBackupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("backups", None)
    if field is not None:
        args["backups"] = (
            [unmarshal_DatabaseBackup(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListDatabaseBackupsResponse(**args)


def unmarshal_ListDatabasesResponse(data: Any) -> ListDatabasesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabasesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("databases", None)
    if field is not None:
        args["databases"] = (
            [unmarshal_Database(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListDatabasesResponse(**args)


def marshal_CreateDatabaseRequest(
    request: CreateDatabaseRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.cpu_min is not None:
        output["cpu_min"] = request.cpu_min

    if request.cpu_max is not None:
        output["cpu_max"] = request.cpu_max

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.from_backup_id is not None:
        output["from_backup_id"] = request.from_backup_id

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

    if request.cpu_min is not None:
        output["cpu_min"] = request.cpu_min

    if request.cpu_max is not None:
        output["cpu_max"] = request.cpu_max

    return output
