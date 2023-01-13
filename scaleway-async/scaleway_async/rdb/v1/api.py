# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
    ScwFile,
    unmarshal_ScwFile,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages_async,
    random_name,
    validate_path_param,
    wait_for_resource_async,
)
from .types import (
    ListDatabaseBackupsRequestOrderBy,
    ListDatabasesRequestOrderBy,
    ListInstanceLogsRequestOrderBy,
    ListInstancesRequestOrderBy,
    ListPrivilegesRequestOrderBy,
    ListSnapshotsRequestOrderBy,
    ListUsersRequestOrderBy,
    Permission,
    VolumeType,
    ACLRule,
    ACLRuleRequest,
    AddInstanceACLRulesResponse,
    AddInstanceSettingsResponse,
    Database,
    DatabaseBackup,
    DatabaseEngine,
    DeleteInstanceACLRulesResponse,
    DeleteInstanceSettingsResponse,
    Endpoint,
    EndpointSpec,
    Instance,
    InstanceLog,
    InstanceMetrics,
    InstanceSetting,
    ListDatabaseBackupsResponse,
    ListDatabaseEnginesResponse,
    ListDatabasesResponse,
    ListInstanceACLRulesResponse,
    ListInstanceLogsDetailsResponse,
    ListInstanceLogsResponse,
    ListInstancesResponse,
    ListNodeTypesResponse,
    ListPrivilegesResponse,
    ListSnapshotsResponse,
    ListUsersResponse,
    LogsPolicy,
    NodeType,
    PrepareInstanceLogsResponse,
    Privilege,
    ReadReplica,
    ReadReplicaEndpointSpec,
    SetInstanceACLRulesResponse,
    SetInstanceSettingsResponse,
    Snapshot,
    User,
    CreateDatabaseBackupRequest,
    UpdateDatabaseBackupRequest,
    RestoreDatabaseBackupRequest,
    UpgradeInstanceRequest,
    CreateInstanceRequest,
    UpdateInstanceRequest,
    CloneInstanceRequest,
    CreateReadReplicaRequest,
    CreateReadReplicaEndpointRequest,
    PrepareInstanceLogsRequest,
    PurgeInstanceLogsRequest,
    AddInstanceSettingsRequest,
    DeleteInstanceSettingsRequest,
    SetInstanceSettingsRequest,
    AddInstanceACLRulesRequest,
    SetInstanceACLRulesRequest,
    DeleteInstanceACLRulesRequest,
    CreateUserRequest,
    UpdateUserRequest,
    CreateDatabaseRequest,
    SetPrivilegeRequest,
    CreateSnapshotRequest,
    UpdateSnapshotRequest,
    CreateInstanceFromSnapshotRequest,
    CreateEndpointRequest,
)
from .content import (
    DATABASE_BACKUP_TRANSIENT_STATUSES,
    INSTANCE_LOG_TRANSIENT_STATUSES,
    INSTANCE_TRANSIENT_STATUSES,
    READ_REPLICA_TRANSIENT_STATUSES,
    SNAPSHOT_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_AddInstanceACLRulesRequest,
    marshal_AddInstanceSettingsRequest,
    marshal_CloneInstanceRequest,
    marshal_CreateDatabaseBackupRequest,
    marshal_CreateDatabaseRequest,
    marshal_CreateEndpointRequest,
    marshal_CreateInstanceFromSnapshotRequest,
    marshal_CreateInstanceRequest,
    marshal_CreateReadReplicaEndpointRequest,
    marshal_CreateReadReplicaRequest,
    marshal_CreateSnapshotRequest,
    marshal_CreateUserRequest,
    marshal_DeleteInstanceACLRulesRequest,
    marshal_DeleteInstanceSettingsRequest,
    marshal_PrepareInstanceLogsRequest,
    marshal_PurgeInstanceLogsRequest,
    marshal_RestoreDatabaseBackupRequest,
    marshal_SetInstanceACLRulesRequest,
    marshal_SetInstanceSettingsRequest,
    marshal_SetPrivilegeRequest,
    marshal_UpdateDatabaseBackupRequest,
    marshal_UpdateInstanceRequest,
    marshal_UpdateSnapshotRequest,
    marshal_UpdateUserRequest,
    marshal_UpgradeInstanceRequest,
    unmarshal_Endpoint,
    unmarshal_ReadReplica,
    unmarshal_Database,
    unmarshal_DatabaseBackup,
    unmarshal_Instance,
    unmarshal_InstanceLog,
    unmarshal_Privilege,
    unmarshal_Snapshot,
    unmarshal_User,
    unmarshal_AddInstanceACLRulesResponse,
    unmarshal_AddInstanceSettingsResponse,
    unmarshal_DeleteInstanceACLRulesResponse,
    unmarshal_DeleteInstanceSettingsResponse,
    unmarshal_InstanceMetrics,
    unmarshal_ListDatabaseBackupsResponse,
    unmarshal_ListDatabaseEnginesResponse,
    unmarshal_ListDatabasesResponse,
    unmarshal_ListInstanceACLRulesResponse,
    unmarshal_ListInstanceLogsDetailsResponse,
    unmarshal_ListInstanceLogsResponse,
    unmarshal_ListInstancesResponse,
    unmarshal_ListNodeTypesResponse,
    unmarshal_ListPrivilegesResponse,
    unmarshal_ListSnapshotsResponse,
    unmarshal_ListUsersResponse,
    unmarshal_PrepareInstanceLogsResponse,
    unmarshal_SetInstanceACLRulesResponse,
    unmarshal_SetInstanceSettingsResponse,
)


class RdbV1API(API):
    """
    Database RDB API.
    """

    async def list_database_engines(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        version: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListDatabaseEnginesResponse:
        """
        List available database engines
        :param region: Region to target. If none is passed will use default region from the config
        :param name: Name of the Database Engine
        :param version: Version of the Database Engine
        :param page:
        :param page_size:
        :return: :class:`ListDatabaseEnginesResponse <ListDatabaseEnginesResponse>`

        Usage:
        ::

            result = await api.list_database_engines()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/database-engines",
            params={
                "name": name,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "version": version,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDatabaseEnginesResponse(res.json())

    async def list_database_engines_all(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        version: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DatabaseEngine]:
        """
        List available database engines
        :param region: Region to target. If none is passed will use default region from the config
        :param name: Name of the Database Engine
        :param version: Version of the Database Engine
        :param page:
        :param page_size:
        :return: :class:`List[ListDatabaseEnginesResponse] <List[ListDatabaseEnginesResponse]>`

        Usage:
        ::

            result = await api.list_database_engines_all()
        """

        return await fetch_all_pages_async(
            type=ListDatabaseEnginesResponse,
            key="engines",
            fetcher=self.list_database_engines,
            args={
                "region": region,
                "name": name,
                "version": version,
                "page": page,
                "page_size": page_size,
            },
        )

    async def list_node_types(
        self,
        *,
        include_disabled_types: bool,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListNodeTypesResponse:
        """
        List available node types
        :param region: Region to target. If none is passed will use default region from the config
        :param include_disabled_types: Whether or not to include disabled types
        :param page:
        :param page_size:
        :return: :class:`ListNodeTypesResponse <ListNodeTypesResponse>`

        Usage:
        ::

            result = await api.list_node_types(include_disabled_types=True)
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/node-types",
            params={
                "include_disabled_types": include_disabled_types,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNodeTypesResponse(res.json())

    async def list_node_types_all(
        self,
        *,
        include_disabled_types: bool,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[NodeType]:
        """
        List available node types
        :param region: Region to target. If none is passed will use default region from the config
        :param include_disabled_types: Whether or not to include disabled types
        :param page:
        :param page_size:
        :return: :class:`List[ListNodeTypesResponse] <List[ListNodeTypesResponse]>`

        Usage:
        ::

            result = await api.list_node_types_all(include_disabled_types=True)
        """

        return await fetch_all_pages_async(
            type=ListNodeTypesResponse,
            key="node_types",
            fetcher=self.list_node_types,
            args={
                "include_disabled_types": include_disabled_types,
                "region": region,
                "page": page,
                "page_size": page_size,
            },
        )

    async def list_database_backups(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: ListDatabaseBackupsRequestOrderBy = ListDatabaseBackupsRequestOrderBy.CREATED_AT_ASC,
        instance_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListDatabaseBackupsResponse:
        """
        List database backups
        :param region: Region to target. If none is passed will use default region from the config
        :param name: Name of the database backups
        :param order_by: Criteria to use when ordering database backups listing
        :param instance_id: UUID of the instance
        :param organization_id: Organization ID the database backups belongs to
        :param project_id: Project ID the database backups belongs to
        :param page:
        :param page_size:
        :return: :class:`ListDatabaseBackupsResponse <ListDatabaseBackupsResponse>`

        Usage:
        ::

            result = await api.list_database_backups()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/backups",
            params={
                "instance_id": instance_id,
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
        return unmarshal_ListDatabaseBackupsResponse(res.json())

    async def list_database_backups_all(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: Optional[ListDatabaseBackupsRequestOrderBy] = None,
        instance_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DatabaseBackup]:
        """
        List database backups
        :param region: Region to target. If none is passed will use default region from the config
        :param name: Name of the database backups
        :param order_by: Criteria to use when ordering database backups listing
        :param instance_id: UUID of the instance
        :param organization_id: Organization ID the database backups belongs to
        :param project_id: Project ID the database backups belongs to
        :param page:
        :param page_size:
        :return: :class:`List[ListDatabaseBackupsResponse] <List[ListDatabaseBackupsResponse]>`

        Usage:
        ::

            result = await api.list_database_backups_all()
        """

        return await fetch_all_pages_async(
            type=ListDatabaseBackupsResponse,
            key="database_backups",
            fetcher=self.list_database_backups,
            args={
                "region": region,
                "name": name,
                "order_by": order_by,
                "instance_id": instance_id,
                "organization_id": organization_id,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
            },
        )

    async def create_database_backup(
        self,
        *,
        instance_id: str,
        database_name: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> DatabaseBackup:
        """
        Create a database backup
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance
        :param database_name: Name of the database you want to make a backup of
        :param name: Name of the backup
        :param expires_at: Expiration date (Format ISO 8601)
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = await api.create_database_backup(
                instance_id="example",
                database_name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/backups",
            body=marshal_CreateDatabaseBackupRequest(
                CreateDatabaseBackupRequest(
                    instance_id=instance_id,
                    database_name=database_name,
                    region=region,
                    name=name or random_name(prefix="bkp"),
                    expires_at=expires_at,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseBackup(res.json())

    async def get_database_backup(
        self,
        *,
        database_backup_id: str,
        region: Optional[Region] = None,
    ) -> DatabaseBackup:
        """
        Get a database backup
        :param region: Region to target. If none is passed will use default region from the config
        :param database_backup_id: UUID of the database backup
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = await api.get_database_backup(database_backup_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_database_backup_id = validate_path_param(
            "database_backup_id", database_backup_id
        )

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/backups/{param_database_backup_id}",
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseBackup(res.json())

    async def wait_for_database_backup(
        self,
        *,
        database_backup_id: str,
        region: Optional[Region] = None,
        options: Optional[
            WaitForOptions[DatabaseBackup, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> DatabaseBackup:
        """
        Waits for :class:`DatabaseBackup <DatabaseBackup>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param database_backup_id: UUID of the database backup
        :param options: The options for the waiter
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = api.wait_for_database_backup(database_backup_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = (
                lambda res: res.status not in DATABASE_BACKUP_TRANSIENT_STATUSES
            )

        return await wait_for_resource_async(
            fetcher=self.get_database_backup,
            options=options,
            args={
                "database_backup_id": database_backup_id,
                "region": region,
            },
        )

    async def update_database_backup(
        self,
        *,
        database_backup_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> DatabaseBackup:
        """
        Update a database backup
        :param region: Region to target. If none is passed will use default region from the config
        :param database_backup_id: UUID of the database backup to update
        :param name: Name of the Database Backup
        :param expires_at: Expiration date (Format ISO 8601)
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = await api.update_database_backup(database_backup_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_database_backup_id = validate_path_param(
            "database_backup_id", database_backup_id
        )

        res = self._request(
            "PATCH",
            f"/rdb/v1/regions/{param_region}/backups/{param_database_backup_id}",
            body=marshal_UpdateDatabaseBackupRequest(
                UpdateDatabaseBackupRequest(
                    database_backup_id=database_backup_id,
                    region=region,
                    name=name,
                    expires_at=expires_at,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseBackup(res.json())

    async def delete_database_backup(
        self,
        *,
        database_backup_id: str,
        region: Optional[Region] = None,
    ) -> DatabaseBackup:
        """
        Delete a database backup
        :param region: Region to target. If none is passed will use default region from the config
        :param database_backup_id: UUID of the database backup to delete
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = await api.delete_database_backup(database_backup_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_database_backup_id = validate_path_param(
            "database_backup_id", database_backup_id
        )

        res = self._request(
            "DELETE",
            f"/rdb/v1/regions/{param_region}/backups/{param_database_backup_id}",
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseBackup(res.json())

    async def restore_database_backup(
        self,
        *,
        database_backup_id: str,
        instance_id: str,
        region: Optional[Region] = None,
        database_name: Optional[str] = None,
    ) -> DatabaseBackup:
        """
        Restore a database backup
        :param region: Region to target. If none is passed will use default region from the config
        :param database_backup_id: Backup of a logical database
        :param database_name: Defines the destination database in order to restore into a specified database, the default destination is set to the origin database of the backup
        :param instance_id: Defines the rdb instance where the backup has to be restored
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = await api.restore_database_backup(
                database_backup_id="example",
                instance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_database_backup_id = validate_path_param(
            "database_backup_id", database_backup_id
        )

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/backups/{param_database_backup_id}/restore",
            body=marshal_RestoreDatabaseBackupRequest(
                RestoreDatabaseBackupRequest(
                    database_backup_id=database_backup_id,
                    instance_id=instance_id,
                    region=region,
                    database_name=database_name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseBackup(res.json())

    async def export_database_backup(
        self,
        *,
        database_backup_id: str,
        region: Optional[Region] = None,
    ) -> DatabaseBackup:
        """
        Export a database backup
        :param region: Region to target. If none is passed will use default region from the config
        :param database_backup_id: UUID of the database backup you want to export
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = await api.export_database_backup(database_backup_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_database_backup_id = validate_path_param(
            "database_backup_id", database_backup_id
        )

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/backups/{param_database_backup_id}/export",
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseBackup(res.json())

    async def upgrade_instance(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        node_type: Optional[str] = None,
        enable_ha: Optional[bool] = None,
        volume_size: Optional[int] = None,
        volume_type: Optional[VolumeType] = None,
        upgradable_version_id: Optional[str] = None,
    ) -> Instance:
        """
        Upgrade your current instance specifications like node type, high availability, volume, or db engine version.
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance you want to upgrade
        :param node_type: Node type of the instance you want to upgrade to.

        One-of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id' could be set.
        :param enable_ha: Set to true to enable high availability on your instance.

        One-of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id' could be set.
        :param volume_size: Increase your block storage volume size.

        One-of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id' could be set.
        :param volume_type: Change your instance storage type.

        One-of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id' could be set.
        :param upgradable_version_id: This will create a new Database Instance with same instance specification as the current one and perform a Database Engine upgrade.

        One-of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id' could be set.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.upgrade_instance(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/upgrade",
            body=marshal_UpgradeInstanceRequest(
                UpgradeInstanceRequest(
                    instance_id=instance_id,
                    region=region,
                    node_type=node_type,
                    enable_ha=enable_ha,
                    volume_size=volume_size,
                    volume_type=volume_type,
                    upgradable_version_id=upgradable_version_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    async def list_instances(
        self,
        *,
        region: Optional[Region] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
        order_by: ListInstancesRequestOrderBy = ListInstancesRequestOrderBy.CREATED_AT_ASC,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListInstancesResponse:
        """
        List instances
        :param region: Region to target. If none is passed will use default region from the config
        :param tags: List instance that have a given tags
        :param name: List instance that match a given name pattern
        :param order_by: Criteria to use when ordering instance listing
        :param organization_id: Please use `project_id` instead
        :param project_id: Project ID to list the instance of
        :param page:
        :param page_size:
        :return: :class:`ListInstancesResponse <ListInstancesResponse>`

        Usage:
        ::

            result = await api.list_instances()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/instances",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListInstancesResponse(res.json())

    async def list_instances_all(
        self,
        *,
        region: Optional[Region] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
        order_by: Optional[ListInstancesRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Instance]:
        """
        List instances
        :param region: Region to target. If none is passed will use default region from the config
        :param tags: List instance that have a given tags
        :param name: List instance that match a given name pattern
        :param order_by: Criteria to use when ordering instance listing
        :param organization_id: Please use `project_id` instead
        :param project_id: Project ID to list the instance of
        :param page:
        :param page_size:
        :return: :class:`List[ListInstancesResponse] <List[ListInstancesResponse]>`

        Usage:
        ::

            result = await api.list_instances_all()
        """

        return await fetch_all_pages_async(
            type=ListInstancesResponse,
            key="instances",
            fetcher=self.list_instances,
            args={
                "region": region,
                "tags": tags,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
            },
        )

    async def get_instance(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
    ) -> Instance:
        """
        Get an instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.get_instance(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    async def wait_for_instance(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        options: Optional[
            WaitForOptions[Instance, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Instance:
        """
        Waits for :class:`Instance <Instance>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance
        :param options: The options for the waiter
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = api.wait_for_instance(instance_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in INSTANCE_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_instance,
            options=options,
            args={
                "instance_id": instance_id,
                "region": region,
            },
        )

    async def create_instance(
        self,
        *,
        engine: str,
        user_name: str,
        password: str,
        node_type: str,
        is_ha_cluster: bool,
        disable_backup: bool,
        volume_type: VolumeType,
        volume_size: int,
        backup_same_region: bool,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        init_settings: Optional[List[InstanceSetting]] = None,
        init_endpoints: Optional[List[EndpointSpec]] = None,
    ) -> Instance:
        """
        Create an instance
        :param region: Region to target. If none is passed will use default region from the config
        :param organization_id: Please use `project_id` instead.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: The project ID on which to create the instance.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param name: Name of the instance
        :param engine: Database engine of the database (PostgreSQL, MySQL, ...)
        :param user_name: Name of the user created when the instance is created
        :param password: Password of the user
        :param node_type: Type of node to use for the instance
        :param is_ha_cluster: Whether or not High-Availability is enabled
        :param disable_backup: Whether or not backups are disabled
        :param tags: Tags to apply to the instance
        :param init_settings: List of engine settings to be set at database initialisation
        :param volume_type: Type of volume where data are stored (lssd, bssd, ...)
        :param volume_size: Volume size when volume_type is not lssd
        :param init_endpoints: One or multiple EndpointSpec used to expose your database instance. A load_balancer public endpoint is systematically created
        :param backup_same_region: Store logical backups in the same region as the database instance
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.create_instance(
                engine="example",
                user_name="example",
                password="example",
                node_type="example",
                is_ha_cluster=True,
                disable_backup=True,
                volume_type=lssd,
                volume_size=1,
                backup_same_region=True,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances",
            body=marshal_CreateInstanceRequest(
                CreateInstanceRequest(
                    engine=engine,
                    user_name=user_name,
                    password=password,
                    node_type=node_type,
                    is_ha_cluster=is_ha_cluster,
                    disable_backup=disable_backup,
                    volume_type=volume_type,
                    volume_size=volume_size,
                    backup_same_region=backup_same_region,
                    region=region,
                    organization_id=organization_id,
                    project_id=project_id,
                    name=name or random_name(prefix="ins"),
                    tags=tags,
                    init_settings=init_settings,
                    init_endpoints=init_endpoints,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    async def update_instance(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        backup_schedule_frequency: Optional[int] = None,
        backup_schedule_retention: Optional[int] = None,
        is_backup_schedule_disabled: Optional[bool] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        logs_policy: Optional[LogsPolicy] = None,
        backup_same_region: Optional[bool] = None,
    ) -> Instance:
        """
        Update an instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance to update
        :param backup_schedule_frequency: In hours
        :param backup_schedule_retention: In days
        :param is_backup_schedule_disabled: Whether or not the backup schedule is disabled
        :param name: Name of the instance
        :param tags: Tags of a given instance
        :param logs_policy: Logs policy of the instance
        :param backup_same_region: Store logical backups in the same region as the database instance
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.update_instance(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "PATCH",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}",
            body=marshal_UpdateInstanceRequest(
                UpdateInstanceRequest(
                    instance_id=instance_id,
                    region=region,
                    backup_schedule_frequency=backup_schedule_frequency,
                    backup_schedule_retention=backup_schedule_retention,
                    is_backup_schedule_disabled=is_backup_schedule_disabled,
                    name=name,
                    tags=tags,
                    logs_policy=logs_policy,
                    backup_same_region=backup_same_region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    async def delete_instance(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
    ) -> Instance:
        """
        Delete an instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance to delete
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.delete_instance(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "DELETE",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    async def clone_instance(
        self,
        *,
        instance_id: str,
        name: str,
        region: Optional[Region] = None,
        node_type: Optional[str] = None,
    ) -> Instance:
        """
        Clone an instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance you want to clone
        :param name: Name of the clone instance
        :param node_type: Node type of the clone
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.clone_instance(
                instance_id="example",
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/clone",
            body=marshal_CloneInstanceRequest(
                CloneInstanceRequest(
                    instance_id=instance_id,
                    name=name,
                    region=region,
                    node_type=node_type,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    async def restart_instance(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
    ) -> Instance:
        """
        Restart an instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance you want to restart
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.restart_instance(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/restart",
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    async def get_instance_certificate(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
    ) -> Optional[ScwFile]:
        """
        Get the TLS certificate of an instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance
        :return: :class:`Optional[ScwFile] <Optional[ScwFile]>`

        Usage:
        ::

            result = await api.get_instance_certificate(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/certificate",
        )

        self._throw_on_error(res)
        json = res.json()
        return unmarshal_ScwFile(json) if json is not None else None

    async def renew_instance_certificate(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Renew the TLS certificate of an instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance you want logs of

        Usage:
        ::

            result = await api.renew_instance_certificate(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/renew-certificate",
        )

        self._throw_on_error(res)
        return None

    async def get_instance_metrics(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        metric_name: Optional[str] = None,
    ) -> InstanceMetrics:
        """
        Get database instance metrics.
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance
        :param start_date: Start date to gather metrics from
        :param end_date: End date to gather metrics from
        :param metric_name: Name of the metric to gather
        :return: :class:`InstanceMetrics <InstanceMetrics>`

        Usage:
        ::

            result = await api.get_instance_metrics(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/metrics",
            params={
                "end_date": end_date,
                "metric_name": metric_name,
                "start_date": start_date,
            },
        )

        self._throw_on_error(res)
        return unmarshal_InstanceMetrics(res.json())

    async def create_read_replica(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        endpoint_spec: Optional[List[ReadReplicaEndpointSpec]] = None,
    ) -> ReadReplica:
        """
        You can only create a maximum of 3 read replicas for one instance.
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance you want a read replica of
        :param endpoint_spec: Specification of the endpoint you want to create
        :return: :class:`ReadReplica <ReadReplica>`

        Usage:
        ::

            result = await api.create_read_replica(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/read-replicas",
            body=marshal_CreateReadReplicaRequest(
                CreateReadReplicaRequest(
                    instance_id=instance_id,
                    region=region,
                    endpoint_spec=endpoint_spec,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ReadReplica(res.json())

    async def get_read_replica(
        self,
        *,
        read_replica_id: str,
        region: Optional[Region] = None,
    ) -> ReadReplica:
        """
        Get a read replica
        :param region: Region to target. If none is passed will use default region from the config
        :param read_replica_id: UUID of the read replica
        :return: :class:`ReadReplica <ReadReplica>`

        Usage:
        ::

            result = await api.get_read_replica(read_replica_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_read_replica_id = validate_path_param("read_replica_id", read_replica_id)

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/read-replicas/{param_read_replica_id}",
        )

        self._throw_on_error(res)
        return unmarshal_ReadReplica(res.json())

    async def wait_for_read_replica(
        self,
        *,
        read_replica_id: str,
        region: Optional[Region] = None,
        options: Optional[
            WaitForOptions[ReadReplica, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> ReadReplica:
        """
        Waits for :class:`ReadReplica <ReadReplica>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param read_replica_id: UUID of the read replica
        :param options: The options for the waiter
        :return: :class:`ReadReplica <ReadReplica>`

        Usage:
        ::

            result = api.wait_for_read_replica(read_replica_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in READ_REPLICA_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_read_replica,
            options=options,
            args={
                "read_replica_id": read_replica_id,
                "region": region,
            },
        )

    async def delete_read_replica(
        self,
        *,
        read_replica_id: str,
        region: Optional[Region] = None,
    ) -> ReadReplica:
        """
        Delete a read replica
        :param region: Region to target. If none is passed will use default region from the config
        :param read_replica_id: UUID of the read replica
        :return: :class:`ReadReplica <ReadReplica>`

        Usage:
        ::

            result = await api.delete_read_replica(read_replica_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_read_replica_id = validate_path_param("read_replica_id", read_replica_id)

        res = self._request(
            "DELETE",
            f"/rdb/v1/regions/{param_region}/read-replicas/{param_read_replica_id}",
        )

        self._throw_on_error(res)
        return unmarshal_ReadReplica(res.json())

    async def reset_read_replica(
        self,
        *,
        read_replica_id: str,
        region: Optional[Region] = None,
    ) -> ReadReplica:
        """
        When you resync a read replica, first it is reset, and then its data is resynchronized from the primary node.
        Your read replica will be unavailable during the resync process. The duration of this process is proportional to your Database Instance size.
        The configured endpoints will not change.

        :param region: Region to target. If none is passed will use default region from the config
        :param read_replica_id: UUID of the read replica
        :return: :class:`ReadReplica <ReadReplica>`

        Usage:
        ::

            result = await api.reset_read_replica(read_replica_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_read_replica_id = validate_path_param("read_replica_id", read_replica_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/read-replicas/{param_read_replica_id}/reset",
        )

        self._throw_on_error(res)
        return unmarshal_ReadReplica(res.json())

    async def create_read_replica_endpoint(
        self,
        *,
        read_replica_id: str,
        endpoint_spec: List[ReadReplicaEndpointSpec],
        region: Optional[Region] = None,
    ) -> ReadReplica:
        """
        A read replica can have at most one direct access and one private network endpoint.
        :param region: Region to target. If none is passed will use default region from the config
        :param read_replica_id: UUID of the read replica
        :param endpoint_spec: Specification of the endpoint you want to create
        :return: :class:`ReadReplica <ReadReplica>`

        Usage:
        ::

            result = await api.create_read_replica_endpoint(
                read_replica_id="example",
                endpoint_spec=[ReadReplicaEndpointSpec(...)],
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_read_replica_id = validate_path_param("read_replica_id", read_replica_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/read-replicas/{param_read_replica_id}/endpoints",
            body=marshal_CreateReadReplicaEndpointRequest(
                CreateReadReplicaEndpointRequest(
                    read_replica_id=read_replica_id,
                    endpoint_spec=endpoint_spec,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ReadReplica(res.json())

    async def prepare_instance_logs(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> PrepareInstanceLogsResponse:
        """
        Prepare your instance logs. Logs will be grouped on a minimum interval of a day.
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance you want logs of
        :param start_date: Start datetime of your log. Format: `{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z`
        :param end_date: End datetime of your log. Format: `{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z`
        :return: :class:`PrepareInstanceLogsResponse <PrepareInstanceLogsResponse>`

        Usage:
        ::

            result = await api.prepare_instance_logs(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/prepare-logs",
            body=marshal_PrepareInstanceLogsRequest(
                PrepareInstanceLogsRequest(
                    instance_id=instance_id,
                    region=region,
                    start_date=start_date,
                    end_date=end_date,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PrepareInstanceLogsResponse(res.json())

    async def list_instance_logs(
        self,
        *,
        instance_id: str,
        order_by: ListInstanceLogsRequestOrderBy,
        region: Optional[Region] = None,
    ) -> ListInstanceLogsResponse:
        """
        List available logs of a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance you want logs of
        :param order_by: Criteria to use when ordering instance logs listing
        :return: :class:`ListInstanceLogsResponse <ListInstanceLogsResponse>`

        Usage:
        ::

            result = await api.list_instance_logs(
                instance_id="example",
                order_by=created_at_asc,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/logs",
            params={
                "order_by": order_by,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListInstanceLogsResponse(res.json())

    async def get_instance_log(
        self,
        *,
        instance_log_id: str,
        region: Optional[Region] = None,
    ) -> InstanceLog:
        """
        Get specific logs of a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_log_id: UUID of the instance_log you want
        :return: :class:`InstanceLog <InstanceLog>`

        Usage:
        ::

            result = await api.get_instance_log(instance_log_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_log_id = validate_path_param("instance_log_id", instance_log_id)

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/logs/{param_instance_log_id}",
        )

        self._throw_on_error(res)
        return unmarshal_InstanceLog(res.json())

    async def wait_for_instance_log(
        self,
        *,
        instance_log_id: str,
        region: Optional[Region] = None,
        options: Optional[
            WaitForOptions[InstanceLog, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> InstanceLog:
        """
        Waits for :class:`InstanceLog <InstanceLog>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_log_id: UUID of the instance_log you want
        :param options: The options for the waiter
        :return: :class:`InstanceLog <InstanceLog>`

        Usage:
        ::

            result = api.wait_for_instance_log(instance_log_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in INSTANCE_LOG_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_instance_log,
            options=options,
            args={
                "instance_log_id": instance_log_id,
                "region": region,
            },
        )

    async def purge_instance_logs(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        log_name: Optional[str] = None,
    ) -> Optional[None]:
        """
        purge remote instances logs
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance you want logs of
        :param log_name: Specific log name to purge

        Usage:
        ::

            result = await api.purge_instance_logs(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/purge-logs",
            body=marshal_PurgeInstanceLogsRequest(
                PurgeInstanceLogsRequest(
                    instance_id=instance_id,
                    region=region,
                    log_name=log_name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return None

    async def list_instance_logs_details(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
    ) -> ListInstanceLogsDetailsResponse:
        """
        List remote instances logs details
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance you want logs of
        :return: :class:`ListInstanceLogsDetailsResponse <ListInstanceLogsDetailsResponse>`

        Usage:
        ::

            result = await api.list_instance_logs_details(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/logs-details",
        )

        self._throw_on_error(res)
        return unmarshal_ListInstanceLogsDetailsResponse(res.json())

    async def add_instance_settings(
        self,
        *,
        instance_id: str,
        settings: List[InstanceSetting],
        region: Optional[Region] = None,
    ) -> AddInstanceSettingsResponse:
        """
        Add an instance setting
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance you want to add settings to
        :param settings: Settings to add on the instance
        :return: :class:`AddInstanceSettingsResponse <AddInstanceSettingsResponse>`

        Usage:
        ::

            result = await api.add_instance_settings(
                instance_id="example",
                settings=[InstanceSetting(...)],
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/settings",
            body=marshal_AddInstanceSettingsRequest(
                AddInstanceSettingsRequest(
                    instance_id=instance_id,
                    settings=settings,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AddInstanceSettingsResponse(res.json())

    async def delete_instance_settings(
        self,
        *,
        instance_id: str,
        setting_names: List[str],
        region: Optional[Region] = None,
    ) -> DeleteInstanceSettingsResponse:
        """
        Delete an instance setting
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance to delete settings from
        :param setting_names: Settings names to delete
        :return: :class:`DeleteInstanceSettingsResponse <DeleteInstanceSettingsResponse>`

        Usage:
        ::

            result = await api.delete_instance_settings(
                instance_id="example",
                setting_names=["example"],
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "DELETE",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/settings",
            body=marshal_DeleteInstanceSettingsRequest(
                DeleteInstanceSettingsRequest(
                    instance_id=instance_id,
                    setting_names=setting_names,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DeleteInstanceSettingsResponse(res.json())

    async def set_instance_settings(
        self,
        *,
        instance_id: str,
        settings: List[InstanceSetting],
        region: Optional[Region] = None,
    ) -> SetInstanceSettingsResponse:
        """
        Set a given instance setting
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance where the settings has to be set
        :param settings: Settings to define for the instance
        :return: :class:`SetInstanceSettingsResponse <SetInstanceSettingsResponse>`

        Usage:
        ::

            result = await api.set_instance_settings(
                instance_id="example",
                settings=[InstanceSetting(...)],
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "PUT",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/settings",
            body=marshal_SetInstanceSettingsRequest(
                SetInstanceSettingsRequest(
                    instance_id=instance_id,
                    settings=settings,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetInstanceSettingsResponse(res.json())

    async def list_instance_acl_rules(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListInstanceACLRulesResponse:
        """
        List ACL rules of a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance
        :param page:
        :param page_size:
        :return: :class:`ListInstanceACLRulesResponse <ListInstanceACLRulesResponse>`

        Usage:
        ::

            result = await api.list_instance_acl_rules(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/acls",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListInstanceACLRulesResponse(res.json())

    async def list_instance_acl_rules_all(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ACLRule]:
        """
        List ACL rules of a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance
        :param page:
        :param page_size:
        :return: :class:`List[ListInstanceACLRulesResponse] <List[ListInstanceACLRulesResponse]>`

        Usage:
        ::

            result = await api.list_instance_acl_rules_all(instance_id="example")
        """

        return await fetch_all_pages_async(
            type=ListInstanceACLRulesResponse,
            key="rules",
            fetcher=self.list_instance_acl_rules,
            args={
                "instance_id": instance_id,
                "region": region,
                "page": page,
                "page_size": page_size,
            },
        )

    async def add_instance_acl_rules(
        self,
        *,
        instance_id: str,
        rules: List[ACLRuleRequest],
        region: Optional[Region] = None,
    ) -> AddInstanceACLRulesResponse:
        """
        Add an additional ACL rule to a database instance.
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance you want to add acl rules to
        :param rules: ACLs rules to add to the instance
        :return: :class:`AddInstanceACLRulesResponse <AddInstanceACLRulesResponse>`

        Usage:
        ::

            result = await api.add_instance_acl_rules(
                instance_id="example",
                rules=[ACLRuleRequest(...)],
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/acls",
            body=marshal_AddInstanceACLRulesRequest(
                AddInstanceACLRulesRequest(
                    instance_id=instance_id,
                    rules=rules,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AddInstanceACLRulesResponse(res.json())

    async def set_instance_acl_rules(
        self,
        *,
        instance_id: str,
        rules: List[ACLRuleRequest],
        region: Optional[Region] = None,
    ) -> SetInstanceACLRulesResponse:
        """
        Replace all the ACL rules of a database instance.
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance where the ACL rules has to be set
        :param rules: ACL rules to define for the instance
        :return: :class:`SetInstanceACLRulesResponse <SetInstanceACLRulesResponse>`

        Usage:
        ::

            result = await api.set_instance_acl_rules(
                instance_id="example",
                rules=[ACLRuleRequest(...)],
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "PUT",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/acls",
            body=marshal_SetInstanceACLRulesRequest(
                SetInstanceACLRulesRequest(
                    instance_id=instance_id,
                    rules=rules,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetInstanceACLRulesResponse(res.json())

    async def delete_instance_acl_rules(
        self,
        *,
        instance_id: str,
        acl_rule_ips: List[str],
        region: Optional[Region] = None,
    ) -> DeleteInstanceACLRulesResponse:
        """
        Delete ACL rules of a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance you want to delete an ACL rules from
        :param acl_rule_ips: ACL rules IP present on the instance
        :return: :class:`DeleteInstanceACLRulesResponse <DeleteInstanceACLRulesResponse>`

        Usage:
        ::

            result = await api.delete_instance_acl_rules(
                instance_id="example",
                acl_rule_ips=["example"],
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "DELETE",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/acls",
            body=marshal_DeleteInstanceACLRulesRequest(
                DeleteInstanceACLRulesRequest(
                    instance_id=instance_id,
                    acl_rule_ips=acl_rule_ips,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DeleteInstanceACLRulesResponse(res.json())

    async def list_users(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: ListUsersRequestOrderBy = ListUsersRequestOrderBy.NAME_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListUsersResponse:
        """
        List users of a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance
        :param name: Name of the user
        :param order_by: Criteria to use when ordering users listing
        :param page:
        :param page_size:
        :return: :class:`ListUsersResponse <ListUsersResponse>`

        Usage:
        ::

            result = await api.list_users(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/users",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListUsersResponse(res.json())

    async def list_users_all(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: Optional[ListUsersRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[User]:
        """
        List users of a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance
        :param name: Name of the user
        :param order_by: Criteria to use when ordering users listing
        :param page:
        :param page_size:
        :return: :class:`List[ListUsersResponse] <List[ListUsersResponse]>`

        Usage:
        ::

            result = await api.list_users_all(instance_id="example")
        """

        return await fetch_all_pages_async(
            type=ListUsersResponse,
            key="users",
            fetcher=self.list_users,
            args={
                "instance_id": instance_id,
                "region": region,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    async def create_user(
        self,
        *,
        instance_id: str,
        name: str,
        password: str,
        is_admin: bool,
        region: Optional[Region] = None,
    ) -> User:
        """
        Create a user on a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance you want to create a user in
        :param name: Name of the user you want to create
        :param password: Password of the user you want to create
        :param is_admin: Whether the user you want to create will have administrative privileges
        :return: :class:`User <User>`

        Usage:
        ::

            result = await api.create_user(
                instance_id="example",
                name="example",
                password="example",
                is_admin=True,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/users",
            body=marshal_CreateUserRequest(
                CreateUserRequest(
                    instance_id=instance_id,
                    name=name,
                    password=password,
                    is_admin=is_admin,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    async def update_user(
        self,
        *,
        instance_id: str,
        name: str,
        region: Optional[Region] = None,
        password: Optional[str] = None,
        is_admin: Optional[bool] = None,
    ) -> User:
        """
        Update a user on a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance the user belongs to
        :param name: Name of the database user
        :param password: Password of the database user
        :param is_admin: Whether or not this user got administrative privileges
        :return: :class:`User <User>`

        Usage:
        ::

            result = await api.update_user(
                instance_id="example",
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)
        param_name = validate_path_param("name", name)

        res = self._request(
            "PATCH",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/users/{param_name}",
            body=marshal_UpdateUserRequest(
                UpdateUserRequest(
                    instance_id=instance_id,
                    name=name,
                    region=region,
                    password=password,
                    is_admin=is_admin,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    async def delete_user(
        self,
        *,
        instance_id: str,
        name: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a user on a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance to delete a user from
        :param name: Name of the user

        Usage:
        ::

            result = await api.delete_user(
                instance_id="example",
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)
        param_name = validate_path_param("name", name)

        res = self._request(
            "DELETE",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/users/{param_name}",
        )

        self._throw_on_error(res)
        return None

    async def list_databases(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        managed: Optional[bool] = None,
        owner: Optional[str] = None,
        order_by: ListDatabasesRequestOrderBy = ListDatabasesRequestOrderBy.NAME_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListDatabasesResponse:
        """
        List all database in a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance to list database of
        :param name: Name of the database
        :param managed: Whether or not the database is managed
        :param owner: User that owns this database
        :param order_by: Criteria to use when ordering database listing
        :param page:
        :param page_size:
        :return: :class:`ListDatabasesResponse <ListDatabasesResponse>`

        Usage:
        ::

            result = await api.list_databases(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/databases",
            params={
                "managed": managed,
                "name": name,
                "order_by": order_by,
                "owner": owner,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDatabasesResponse(res.json())

    async def list_databases_all(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        managed: Optional[bool] = None,
        owner: Optional[str] = None,
        order_by: Optional[ListDatabasesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Database]:
        """
        List all database in a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance to list database of
        :param name: Name of the database
        :param managed: Whether or not the database is managed
        :param owner: User that owns this database
        :param order_by: Criteria to use when ordering database listing
        :param page:
        :param page_size:
        :return: :class:`List[ListDatabasesResponse] <List[ListDatabasesResponse]>`

        Usage:
        ::

            result = await api.list_databases_all(instance_id="example")
        """

        return await fetch_all_pages_async(
            type=ListDatabasesResponse,
            key="databases",
            fetcher=self.list_databases,
            args={
                "instance_id": instance_id,
                "region": region,
                "name": name,
                "managed": managed,
                "owner": owner,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    async def create_database(
        self,
        *,
        instance_id: str,
        name: str,
        region: Optional[Region] = None,
    ) -> Database:
        """
        Create a database in a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance where to create the database
        :param name: Name of the database
        :return: :class:`Database <Database>`

        Usage:
        ::

            result = await api.create_database(
                instance_id="example",
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/databases",
            body=marshal_CreateDatabaseRequest(
                CreateDatabaseRequest(
                    instance_id=instance_id,
                    name=name,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Database(res.json())

    async def delete_database(
        self,
        *,
        instance_id: str,
        name: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a database in a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance where to delete the database
        :param name: Name of the database to delete

        Usage:
        ::

            result = await api.delete_database(
                instance_id="example",
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)
        param_name = validate_path_param("name", name)

        res = self._request(
            "DELETE",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/databases/{param_name}",
        )

        self._throw_on_error(res)
        return None

    async def list_privileges(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        order_by: ListPrivilegesRequestOrderBy = ListPrivilegesRequestOrderBy.USER_NAME_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        database_name: Optional[str] = None,
        user_name: Optional[str] = None,
    ) -> ListPrivilegesResponse:
        """
        List privileges of a given user for a given database on a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance
        :param order_by: Criteria to use when ordering privileges listing
        :param page:
        :param page_size:
        :param database_name: Name of the database
        :param user_name: Name of the user
        :return: :class:`ListPrivilegesResponse <ListPrivilegesResponse>`

        Usage:
        ::

            result = await api.list_privileges(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/privileges",
            params={
                "database_name": database_name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "user_name": user_name,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPrivilegesResponse(res.json())

    async def list_privileges_all(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListPrivilegesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        database_name: Optional[str] = None,
        user_name: Optional[str] = None,
    ) -> List[Privilege]:
        """
        List privileges of a given user for a given database on a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance
        :param order_by: Criteria to use when ordering privileges listing
        :param page:
        :param page_size:
        :param database_name: Name of the database
        :param user_name: Name of the user
        :return: :class:`List[ListPrivilegesResponse] <List[ListPrivilegesResponse]>`

        Usage:
        ::

            result = await api.list_privileges_all(instance_id="example")
        """

        return await fetch_all_pages_async(
            type=ListPrivilegesResponse,
            key="privileges",
            fetcher=self.list_privileges,
            args={
                "instance_id": instance_id,
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "database_name": database_name,
                "user_name": user_name,
            },
        )

    async def set_privilege(
        self,
        *,
        instance_id: str,
        database_name: str,
        user_name: str,
        permission: Permission,
        region: Optional[Region] = None,
    ) -> Privilege:
        """
        Set privileges of a given user for a given database on a given instance
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance
        :param database_name: Name of the database
        :param user_name: Name of the user
        :param permission: Permission to set (Read, Read/Write, All, Custom)
        :return: :class:`Privilege <Privilege>`

        Usage:
        ::

            result = await api.set_privilege(
                instance_id="example",
                database_name="example",
                user_name="example",
                permission=readonly,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "PUT",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/privileges",
            body=marshal_SetPrivilegeRequest(
                SetPrivilegeRequest(
                    instance_id=instance_id,
                    database_name=database_name,
                    user_name=user_name,
                    permission=permission,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Privilege(res.json())

    async def list_snapshots(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: ListSnapshotsRequestOrderBy = ListSnapshotsRequestOrderBy.CREATED_AT_ASC,
        instance_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListSnapshotsResponse:
        """
        List instance snapshots
        :param region: Region to target. If none is passed will use default region from the config
        :param name: Name of the snapshot
        :param order_by: Criteria to use when ordering snapshot listing
        :param instance_id: UUID of the instance
        :param organization_id: Organization ID the snapshots belongs to
        :param project_id: Project ID the snapshots belongs to
        :param page:
        :param page_size:
        :return: :class:`ListSnapshotsResponse <ListSnapshotsResponse>`

        Usage:
        ::

            result = await api.list_snapshots()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/snapshots",
            params={
                "instance_id": instance_id,
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
        return unmarshal_ListSnapshotsResponse(res.json())

    async def list_snapshots_all(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: Optional[ListSnapshotsRequestOrderBy] = None,
        instance_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Snapshot]:
        """
        List instance snapshots
        :param region: Region to target. If none is passed will use default region from the config
        :param name: Name of the snapshot
        :param order_by: Criteria to use when ordering snapshot listing
        :param instance_id: UUID of the instance
        :param organization_id: Organization ID the snapshots belongs to
        :param project_id: Project ID the snapshots belongs to
        :param page:
        :param page_size:
        :return: :class:`List[ListSnapshotsResponse] <List[ListSnapshotsResponse]>`

        Usage:
        ::

            result = await api.list_snapshots_all()
        """

        return await fetch_all_pages_async(
            type=ListSnapshotsResponse,
            key="snapshots",
            fetcher=self.list_snapshots,
            args={
                "region": region,
                "name": name,
                "order_by": order_by,
                "instance_id": instance_id,
                "organization_id": organization_id,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
            },
        )

    async def get_snapshot(
        self,
        *,
        snapshot_id: str,
        region: Optional[Region] = None,
    ) -> Snapshot:
        """
        Get an instance snapshot
        :param region: Region to target. If none is passed will use default region from the config
        :param snapshot_id: UUID of the snapshot
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = await api.get_snapshot(snapshot_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/snapshots/{param_snapshot_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    async def wait_for_snapshot(
        self,
        *,
        snapshot_id: str,
        region: Optional[Region] = None,
        options: Optional[
            WaitForOptions[Snapshot, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Snapshot:
        """
        Waits for :class:`Snapshot <Snapshot>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param snapshot_id: UUID of the snapshot
        :param options: The options for the waiter
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.wait_for_snapshot(snapshot_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in SNAPSHOT_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_snapshot,
            options=options,
            args={
                "snapshot_id": snapshot_id,
                "region": region,
            },
        )

    async def create_snapshot(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> Snapshot:
        """
        Create an instance snapshot
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance
        :param name: Name of the snapshot
        :param expires_at: Expiration date (Format ISO 8601)
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = await api.create_snapshot(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/snapshots",
            body=marshal_CreateSnapshotRequest(
                CreateSnapshotRequest(
                    instance_id=instance_id,
                    region=region,
                    name=name or random_name(prefix="snp"),
                    expires_at=expires_at,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    async def update_snapshot(
        self,
        *,
        snapshot_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> Snapshot:
        """
        Update an instance snapshot
        :param region: Region to target. If none is passed will use default region from the config
        :param snapshot_id: UUID of the snapshot to update
        :param name: Name of the snapshot
        :param expires_at: Expiration date (Format ISO 8601)
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = await api.update_snapshot(snapshot_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "PATCH",
            f"/rdb/v1/regions/{param_region}/snapshots/{param_snapshot_id}",
            body=marshal_UpdateSnapshotRequest(
                UpdateSnapshotRequest(
                    snapshot_id=snapshot_id,
                    region=region,
                    name=name,
                    expires_at=expires_at,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    async def delete_snapshot(
        self,
        *,
        snapshot_id: str,
        region: Optional[Region] = None,
    ) -> Snapshot:
        """
        Delete an instance snapshot
        :param region: Region to target. If none is passed will use default region from the config
        :param snapshot_id: UUID of the snapshot to delete
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = await api.delete_snapshot(snapshot_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "DELETE",
            f"/rdb/v1/regions/{param_region}/snapshots/{param_snapshot_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    async def create_instance_from_snapshot(
        self,
        *,
        snapshot_id: str,
        instance_name: str,
        region: Optional[Region] = None,
        is_ha_cluster: Optional[bool] = None,
        node_type: Optional[str] = None,
    ) -> Instance:
        """
        Create a new instance from a given snapshot
        :param region: Region to target. If none is passed will use default region from the config
        :param snapshot_id: Block snapshot of the instance
        :param instance_name: Name of the instance created with the snapshot
        :param is_ha_cluster: Whether or not High-Availability is enabled on the new instance
        :param node_type: The node type used to restore the snapshot
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.create_instance_from_snapshot(
                snapshot_id="example",
                instance_name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/snapshots/{param_snapshot_id}/create-instance",
            body=marshal_CreateInstanceFromSnapshotRequest(
                CreateInstanceFromSnapshotRequest(
                    snapshot_id=snapshot_id,
                    instance_name=instance_name,
                    region=region,
                    is_ha_cluster=is_ha_cluster,
                    node_type=node_type,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    async def create_endpoint(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        endpoint_spec: Optional[EndpointSpec] = None,
    ) -> Endpoint:
        """
        Create a new instance endpoint
        :param region: Region to target. If none is passed will use default region from the config
        :param instance_id: UUID of the instance you want to add endpoint to
        :param endpoint_spec: Specification of the endpoint you want to create
        :return: :class:`Endpoint <Endpoint>`

        Usage:
        ::

            result = await api.create_endpoint(instance_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/endpoints",
            body=marshal_CreateEndpointRequest(
                CreateEndpointRequest(
                    instance_id=instance_id,
                    region=region,
                    endpoint_spec=endpoint_spec,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Endpoint(res.json())

    async def delete_endpoint(
        self,
        *,
        endpoint_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete an instance endpoint
        :param region: Region to target. If none is passed will use default region from the config
        :param endpoint_id: This endpoint can also be used to delete a read replica endpoint.

        Usage:
        ::

            result = await api.delete_endpoint(endpoint_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_endpoint_id = validate_path_param("endpoint_id", endpoint_id)

        res = self._request(
            "DELETE",
            f"/rdb/v1/regions/{param_region}/endpoints/{param_endpoint_id}",
        )

        self._throw_on_error(res)
        return None

    async def get_endpoint(
        self,
        *,
        endpoint_id: str,
        region: Optional[Region] = None,
    ) -> Endpoint:
        """
        Get an instance endpoint
        :param region: Region to target. If none is passed will use default region from the config
        :param endpoint_id: UUID of the endpoint you want to get
        :return: :class:`Endpoint <Endpoint>`

        Usage:
        ::

            result = await api.get_endpoint(endpoint_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_endpoint_id = validate_path_param("endpoint_id", endpoint_id)

        res = self._request(
            "GET",
            f"/rdb/v1/regions/{param_region}/endpoints/{param_endpoint_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Endpoint(res.json())
