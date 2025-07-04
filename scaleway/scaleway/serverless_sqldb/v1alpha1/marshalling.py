# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    DatabaseBackupStatus,
    DatabaseStatus,
    ListDatabaseBackupsRequestOrderBy,
    ListDatabasesRequestOrderBy,
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

    field = data.get("id", str())
    args["id"] = field

    field = data.get("status", getattr(DatabaseBackupStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("database_id", str())
    args["database_id"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("size", None)
    args["size"] = field

    field = data.get("db_size", None)
    args["db_size"] = field

    field = data.get("download_url", None)
    args["download_url"] = field

    field = data.get("download_url_expires_at", None)
    args["download_url_expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return DatabaseBackup(**args)

def unmarshal_Database(data: Any) -> Database:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Database' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("status", getattr(DatabaseStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("endpoint", str())
    args["endpoint"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("cpu_min", 0)
    args["cpu_min"] = field

    field = data.get("cpu_max", 0)
    args["cpu_max"] = field

    field = data.get("cpu_current", 0)
    args["cpu_current"] = field

    field = data.get("started", False)
    args["started"] = field

    field = data.get("engine_major_version", 0)
    args["engine_major_version"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Database(**args)

def unmarshal_ListDatabaseBackupsResponse(data: Any) -> ListDatabaseBackupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabaseBackupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("backups", [])
    args["backups"] = [unmarshal_DatabaseBackup(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListDatabaseBackupsResponse(**args)

def unmarshal_ListDatabasesResponse(data: Any) -> ListDatabasesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabasesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("databases", [])
    args["databases"] = [unmarshal_Database(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListDatabasesResponse(**args)

def marshal_CreateDatabaseRequest(
    request: CreateDatabaseRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.cpu_min is not None:
        output["cpu_min"] = request.cpu_min
    else:
        output["cpu_min"] = str()

    if request.cpu_max is not None:
        output["cpu_max"] = request.cpu_max
    else:
        output["cpu_max"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.from_backup_id is not None:
        output["from_backup_id"] = request.from_backup_id
    else:
        output["from_backup_id"] = None


    return output

def marshal_RestoreDatabaseFromBackupRequest(
    request: RestoreDatabaseFromBackupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backup_id is not None:
        output["backup_id"] = request.backup_id
    else:
        output["backup_id"] = str()


    return output

def marshal_UpdateDatabaseRequest(
    request: UpdateDatabaseRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.cpu_min is not None:
        output["cpu_min"] = request.cpu_min
    else:
        output["cpu_min"] = None

    if request.cpu_max is not None:
        output["cpu_max"] = request.cpu_max
    else:
        output["cpu_max"] = None


    return output
