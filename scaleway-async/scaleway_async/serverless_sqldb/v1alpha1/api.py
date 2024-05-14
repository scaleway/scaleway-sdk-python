# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    ListDatabaseBackupsRequestOrderBy,
    ListDatabasesRequestOrderBy,
    CreateDatabaseRequest,
    Database,
    DatabaseBackup,
    ListDatabaseBackupsResponse,
    ListDatabasesResponse,
    RestoreDatabaseFromBackupRequest,
    UpdateDatabaseRequest,
)
from .content import (
    DATABASE_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_DatabaseBackup,
    unmarshal_Database,
    unmarshal_ListDatabaseBackupsResponse,
    unmarshal_ListDatabasesResponse,
    marshal_CreateDatabaseRequest,
    marshal_RestoreDatabaseFromBackupRequest,
    marshal_UpdateDatabaseRequest,
)


class ServerlessSqldbV1Alpha1API(API):
    """
    This API allows you to manage your Serverless SQL Databases.
    """

    async def create_database(
        self,
        *,
        name: str,
        cpu_min: int,
        cpu_max: int,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        from_backup_id: Optional[str] = None,
    ) -> Database:
        """
        Create a new Serverless SQL Database.
        You must provide the following parameters: `organization_id`, `project_id`, `name`, `cpu_min`, `cpu_max`. You can also provide `from_backup_id` to create a database from a backup.
        :param name: The name of the Serverless SQL Database to be created.
        :param cpu_min: The minimum number of CPU units for your Serverless SQL Database.
        :param cpu_max: The maximum number of CPU units for your Serverless SQL Database.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: The ID of your Scaleway project.
        :param from_backup_id: The ID of the backup to create the database from.
        :return: :class:`Database <Database>`

        Usage:
        ::

            result = await api.create_database(
                name="example",
                cpu_min=1,
                cpu_max=1,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/serverless-sqldb/v1alpha1/regions/{param_region}/databases",
            body=marshal_CreateDatabaseRequest(
                CreateDatabaseRequest(
                    name=name,
                    cpu_min=cpu_min,
                    cpu_max=cpu_max,
                    region=region,
                    project_id=project_id,
                    from_backup_id=from_backup_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Database(res.json())

    async def get_database(
        self,
        *,
        database_id: str,
        region: Optional[Region] = None,
    ) -> Database:
        """
        Get a database information.
        Retrieve information about your Serverless SQL Database. You must provide the `database_id` parameter.
        :param database_id: UUID of the Serverless SQL DB database.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Database <Database>`

        Usage:
        ::

            result = await api.get_database(
                database_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_database_id = validate_path_param("database_id", database_id)

        res = self._request(
            "GET",
            f"/serverless-sqldb/v1alpha1/regions/{param_region}/databases/{param_database_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Database(res.json())

    async def wait_for_database(
        self,
        *,
        database_id: str,
        region: Optional[Region] = None,
        options: Optional[
            WaitForOptions[Database, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Database:
        """
        Get a database information.
        Retrieve information about your Serverless SQL Database. You must provide the `database_id` parameter.
        :param database_id: UUID of the Serverless SQL DB database.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Database <Database>`

        Usage:
        ::

            result = await api.get_database(
                database_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in DATABASE_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_database,
            options=options,
            args={
                "database_id": database_id,
                "region": region,
            },
        )

    async def delete_database(
        self,
        *,
        database_id: str,
        region: Optional[Region] = None,
    ) -> Database:
        """
        Delete a database.
        Deletes a database. You must provide the `database_id` parameter. All data stored in the database will be permanently deleted.
        :param database_id: UUID of the Serverless SQL Database.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Database <Database>`

        Usage:
        ::

            result = await api.delete_database(
                database_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_database_id = validate_path_param("database_id", database_id)

        res = self._request(
            "DELETE",
            f"/serverless-sqldb/v1alpha1/regions/{param_region}/databases/{param_database_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Database(res.json())

    async def list_databases(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        order_by: Optional[ListDatabasesRequestOrderBy] = None,
    ) -> ListDatabasesResponse:
        """
        List your Serverless SQL Databases.
        List all Serverless SQL Databases for a given Scaleway Organization or Scaleway Project. By default, the databases returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. For the `name` parameter, the value you include will be checked against the whole name string to see if it includes the string you put in the parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Filter by the UUID of the Scaleway organization.
        :param project_id: UUID of the Scaleway project.
        :param page: Page number.
        :param page_size: Page size.
        :param name: Filter by the name of the database.
        :param order_by: Sorting criteria. One of `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`.
        :return: :class:`ListDatabasesResponse <ListDatabasesResponse>`

        Usage:
        ::

            result = await api.list_databases()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/serverless-sqldb/v1alpha1/regions/{param_region}/databases",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDatabasesResponse(res.json())

    async def list_databases_all(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        order_by: Optional[ListDatabasesRequestOrderBy] = None,
    ) -> List[Database]:
        """
        List your Serverless SQL Databases.
        List all Serverless SQL Databases for a given Scaleway Organization or Scaleway Project. By default, the databases returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. For the `name` parameter, the value you include will be checked against the whole name string to see if it includes the string you put in the parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Filter by the UUID of the Scaleway organization.
        :param project_id: UUID of the Scaleway project.
        :param page: Page number.
        :param page_size: Page size.
        :param name: Filter by the name of the database.
        :param order_by: Sorting criteria. One of `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`.
        :return: :class:`List[Database] <List[Database]>`

        Usage:
        ::

            result = await api.list_databases_all()
        """

        return await fetch_all_pages_async(
            type=ListDatabasesResponse,
            key="databases",
            fetcher=self.list_databases,
            args={
                "region": region,
                "organization_id": organization_id,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
                "name": name,
                "order_by": order_by,
            },
        )

    async def update_database(
        self,
        *,
        database_id: str,
        region: Optional[Region] = None,
        cpu_min: Optional[int] = None,
        cpu_max: Optional[int] = None,
    ) -> Database:
        """
        Update database information.
        Update CPU limits of your Serverless SQL Database. You must provide the `database_id` parameter.
        :param database_id: UUID of the Serverless SQL Database.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cpu_min: The minimum number of CPU units for your Serverless SQL Database.
        :param cpu_max: The maximum number of CPU units for your Serverless SQL Database.
        :return: :class:`Database <Database>`

        Usage:
        ::

            result = await api.update_database(
                database_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_database_id = validate_path_param("database_id", database_id)

        res = self._request(
            "PATCH",
            f"/serverless-sqldb/v1alpha1/regions/{param_region}/databases/{param_database_id}",
            body=marshal_UpdateDatabaseRequest(
                UpdateDatabaseRequest(
                    database_id=database_id,
                    region=region,
                    cpu_min=cpu_min,
                    cpu_max=cpu_max,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Database(res.json())

    async def restore_database_from_backup(
        self,
        *,
        database_id: str,
        backup_id: str,
        region: Optional[Region] = None,
    ) -> Database:
        """
        Restore a database from a backup.
        Restore a database from a backup. You must provide the `backup_id` parameter.
        :param database_id: UUID of the Serverless SQL Database.
        :param backup_id: UUID of the Serverless SQL Database backup to restore.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Database <Database>`

        Usage:
        ::

            result = await api.restore_database_from_backup(
                database_id="example",
                backup_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_database_id = validate_path_param("database_id", database_id)

        res = self._request(
            "POST",
            f"/serverless-sqldb/v1alpha1/regions/{param_region}/databases/{param_database_id}/restore",
            body=marshal_RestoreDatabaseFromBackupRequest(
                RestoreDatabaseFromBackupRequest(
                    database_id=database_id,
                    backup_id=backup_id,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Database(res.json())

    async def get_database_backup(
        self,
        *,
        backup_id: str,
        region: Optional[Region] = None,
    ) -> DatabaseBackup:
        """
        Get a database backup information.
        Retrieve information about your Serverless SQL Database backup. You must provide the `backup_id` parameter.
        :param backup_id: UUID of the Serverless SQL Database backup.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = await api.get_database_backup(
                backup_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backup_id = validate_path_param("backup_id", backup_id)

        res = self._request(
            "GET",
            f"/serverless-sqldb/v1alpha1/regions/{param_region}/backups/{param_backup_id}",
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseBackup(res.json())

    async def list_database_backups(
        self,
        *,
        database_id: str,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDatabaseBackupsRequestOrderBy] = None,
    ) -> ListDatabaseBackupsResponse:
        """
        List your Serverless SQL Database backups.
        List all Serverless SQL Database backups for a given Scaleway Project or Database. By default, the backups returned in the list are ordered by creation date in descending order, though this can be modified via the order_by field.
        :param database_id: Filter by the UUID of the Serverless SQL Database.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Filter by the UUID of the Scaleway organization.
        :param project_id: Filter by the UUID of the Scaleway project.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by: Sorting criteria. One of `created_at_asc`, `created_at_desc`.
        :return: :class:`ListDatabaseBackupsResponse <ListDatabaseBackupsResponse>`

        Usage:
        ::

            result = await api.list_database_backups(
                database_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/serverless-sqldb/v1alpha1/regions/{param_region}/backups",
            params={
                "database_id": database_id,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDatabaseBackupsResponse(res.json())

    async def list_database_backups_all(
        self,
        *,
        database_id: str,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDatabaseBackupsRequestOrderBy] = None,
    ) -> List[DatabaseBackup]:
        """
        List your Serverless SQL Database backups.
        List all Serverless SQL Database backups for a given Scaleway Project or Database. By default, the backups returned in the list are ordered by creation date in descending order, though this can be modified via the order_by field.
        :param database_id: Filter by the UUID of the Serverless SQL Database.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Filter by the UUID of the Scaleway organization.
        :param project_id: Filter by the UUID of the Scaleway project.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by: Sorting criteria. One of `created_at_asc`, `created_at_desc`.
        :return: :class:`List[DatabaseBackup] <List[DatabaseBackup]>`

        Usage:
        ::

            result = await api.list_database_backups_all(
                database_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListDatabaseBackupsResponse,
            key="backups",
            fetcher=self.list_database_backups,
            args={
                "database_id": database_id,
                "region": region,
                "organization_id": organization_id,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def export_database_backup(
        self,
        *,
        backup_id: str,
        region: Optional[Region] = None,
    ) -> DatabaseBackup:
        """
        Export a database backup.
        Export a database backup providing a download link once the export process is completed. You must provide the `backup_id` parameter.
        :param backup_id: UUID of the Serverless SQL Database backup.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = await api.export_database_backup(
                backup_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backup_id = validate_path_param("backup_id", backup_id)

        res = self._request(
            "POST",
            f"/serverless-sqldb/v1alpha1/regions/{param_region}/backups/{param_backup_id}/export",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseBackup(res.json())
