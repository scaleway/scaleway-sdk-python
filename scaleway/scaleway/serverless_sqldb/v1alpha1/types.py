# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class DatabaseBackupStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ERROR = "error"
    READY = "ready"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class DatabaseStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ERROR = "error"
    CREATING = "creating"
    READY = "ready"
    DELETING = "deleting"
    RESTORING = "restoring"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class ListDatabaseBackupsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListDatabasesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class DatabaseBackup:
    id: str
    """
    UUID that uniquely identifies a Serverless SQL Database backup.
    """

    status: DatabaseBackupStatus
    """
    Status of the Serverless SQL Database backup. One of `unknown_status` | `error` | `ready` | `locked`.
    """

    organization_id: str
    """
    The ID of your Scaleway organization.
    """

    project_id: str
    """
    UUID of the Scaleway project.
    """

    database_id: str
    """
    UUID of the source Serverless SQL Database the backup is created from.
    """

    region: Region
    """
    Region of the database backup.
    """

    created_at: Optional[datetime]
    """
    Creation date.
    """

    expires_at: Optional[datetime]
    """
    Expiration date.
    """

    size: Optional[int]
    """
    Size (in bytes) of the database backup file.
    """

    db_size: Optional[int]
    """
    Size (in bytes) of the database when backup has been done.
    """

    download_url: Optional[str]
    """
    Download URL of the exported database backup.
    """

    download_url_expires_at: Optional[datetime]
    """
    Expiration date of the download URL.
    """


@dataclass
class Database:
    id: str
    """
    UUID that uniquely identifies your Serverless SQL DB Database.
    """

    name: str
    """
    Name of the database.
    """

    status: DatabaseStatus
    """
    Status of the Serverless SQL Ddatabase. One of `unknown_status` | `ready` | `creating` | `deleting` | `error` | `restoring` | `locked`.
    """

    endpoint: str
    """
    Endpoint of the database.
    """

    organization_id: str
    """
    The ID of your Scaleway organization.
    """

    project_id: str
    """
    Project ID the database belongs to.
    """

    region: Region
    """
    Region of the database.
    """

    cpu_min: int
    """
    The minimum number of CPU units for your Serverless SQL Database.
    """

    cpu_max: int
    """
    The maximum number of CPU units for your Serverless SQL Database.
    """

    cpu_current: int
    """
    The current number of CPU units allocated to your Serverless SQL Database.
    """

    started: bool
    """
    Whether your Serverless SQL Database is running or not.
    """

    engine_major_version: int
    """
    The major version of the underlying database engine.
    """

    created_at: Optional[datetime]
    """
    Creation date.
    """


@dataclass
class CreateDatabaseRequest:
    name: str
    """
    The name of the Serverless SQL Database to be created.
    """

    cpu_min: int
    """
    The minimum number of CPU units for your Serverless SQL Database.
    """

    cpu_max: int
    """
    The maximum number of CPU units for your Serverless SQL Database.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    The ID of your Scaleway project.
    """

    from_backup_id: Optional[str]
    """
    The ID of the backup to create the database from.
    """


@dataclass
class DeleteDatabaseRequest:
    database_id: str
    """
    UUID of the Serverless SQL Database.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ExportDatabaseBackupRequest:
    backup_id: str
    """
    UUID of the Serverless SQL Database backup.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDatabaseBackupRequest:
    backup_id: str
    """
    UUID of the Serverless SQL Database backup.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDatabaseRequest:
    database_id: str
    """
    UUID of the Serverless SQL DB database.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListDatabaseBackupsRequest:
    database_id: str
    """
    Filter by the UUID of the Serverless SQL Database.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str]
    """
    Filter by the UUID of the Scaleway organization.
    """

    project_id: Optional[str]
    """
    Filter by the UUID of the Scaleway project.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Page size.
    """

    order_by: Optional[ListDatabaseBackupsRequestOrderBy]
    """
    Sorting criteria. One of `created_at_asc`, `created_at_desc`.
    """


@dataclass
class ListDatabaseBackupsResponse:
    backups: List[DatabaseBackup]
    """
    List of the backups.
    """

    total_count: int
    """
    Length of the backups list.
    """


@dataclass
class ListDatabasesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str]
    """
    Filter by the UUID of the Scaleway organization.
    """

    project_id: Optional[str]
    """
    UUID of the Scaleway project.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Page size.
    """

    name: Optional[str]
    """
    Filter by the name of the database.
    """

    order_by: Optional[ListDatabasesRequestOrderBy]
    """
    Sorting criteria. One of `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`.
    """


@dataclass
class ListDatabasesResponse:
    databases: List[Database]
    """
    List of the databases.
    """

    total_count: int
    """
    Total count of Serverless SQL Databases.
    """


@dataclass
class RestoreDatabaseFromBackupRequest:
    database_id: str
    """
    UUID of the Serverless SQL Database.
    """

    backup_id: str
    """
    UUID of the Serverless SQL Database backup to restore.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UpdateDatabaseRequest:
    database_id: str
    """
    UUID of the Serverless SQL Database.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cpu_min: Optional[int]
    """
    The minimum number of CPU units for your Serverless SQL Database.
    """

    cpu_max: Optional[int]
    """
    The maximum number of CPU units for your Serverless SQL Database.
    """
