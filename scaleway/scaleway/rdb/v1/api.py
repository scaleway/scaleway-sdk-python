# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
    ScwFile,
    unmarshal_ScwFile,
)
from scaleway_core.utils import (
    WaitForOptions,
    random_name,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
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
    AddInstanceACLRulesRequest,
    AddInstanceACLRulesResponse,
    AddInstanceSettingsRequest,
    AddInstanceSettingsResponse,
    CloneInstanceRequest,
    CreateDatabaseBackupRequest,
    CreateDatabaseRequest,
    CreateEndpointRequest,
    CreateInstanceFromSnapshotRequest,
    CreateInstanceRequest,
    CreateReadReplicaEndpointRequest,
    CreateReadReplicaRequest,
    CreateSnapshotRequest,
    CreateUserRequest,
    Database,
    DatabaseBackup,
    DatabaseEngine,
    DeleteInstanceACLRulesRequest,
    DeleteInstanceACLRulesResponse,
    DeleteInstanceSettingsRequest,
    DeleteInstanceSettingsResponse,
    EncryptionAtRest,
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
    Maintenance,
    MigrateEndpointRequest,
    NodeType,
    PrepareInstanceLogsRequest,
    PrepareInstanceLogsResponse,
    Privilege,
    PurgeInstanceLogsRequest,
    ReadReplica,
    ReadReplicaEndpointSpec,
    RestoreDatabaseBackupRequest,
    SetInstanceACLRulesRequest,
    SetInstanceACLRulesResponse,
    SetInstanceSettingsRequest,
    SetInstanceSettingsResponse,
    SetPrivilegeRequest,
    Snapshot,
    UpdateDatabaseBackupRequest,
    UpdateInstanceRequest,
    UpdateSnapshotRequest,
    UpdateUserRequest,
    UpgradeInstanceRequest,
    UpgradeInstanceRequestMajorUpgradeWorkflow,
    User,
)
from .content import (
    DATABASE_BACKUP_TRANSIENT_STATUSES,
    INSTANCE_LOG_TRANSIENT_STATUSES,
    INSTANCE_TRANSIENT_STATUSES,
    READ_REPLICA_TRANSIENT_STATUSES,
    SNAPSHOT_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Endpoint,
    unmarshal_Maintenance,
    unmarshal_ReadReplica,
    unmarshal_DatabaseBackup,
    unmarshal_Database,
    unmarshal_InstanceLog,
    unmarshal_Instance,
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
    marshal_MigrateEndpointRequest,
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
)


class RdbV1API(API):
    """
    This API allows you to manage your Managed Databases for PostgreSQL and MySQL.
    """

    def list_database_engines(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        version: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListDatabaseEnginesResponse:
        """
        List available database engines.
        List the PostgreSQL and MySQL database engines available at Scaleway.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the database engine.
        :param version: Version of the database engine.
        :param page:
        :param page_size:
        :return: :class:`ListDatabaseEnginesResponse <ListDatabaseEnginesResponse>`

        Usage:
        ::

            result = api.list_database_engines()
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

    def list_database_engines_all(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        version: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DatabaseEngine]:
        """
        List available database engines.
        List the PostgreSQL and MySQL database engines available at Scaleway.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the database engine.
        :param version: Version of the database engine.
        :param page:
        :param page_size:
        :return: :class:`List[DatabaseEngine] <List[DatabaseEngine]>`

        Usage:
        ::

            result = api.list_database_engines_all()
        """

        return fetch_all_pages(
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

    def list_node_types(
        self,
        *,
        include_disabled_types: bool,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListNodeTypesResponse:
        """
        List available node types.
        List all available node types. By default, the node types returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param include_disabled_types: Defines whether or not to include disabled types.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :return: :class:`ListNodeTypesResponse <ListNodeTypesResponse>`

        Usage:
        ::

            result = api.list_node_types(
                include_disabled_types=False,
            )
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

    def list_node_types_all(
        self,
        *,
        include_disabled_types: bool,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[NodeType]:
        """
        List available node types.
        List all available node types. By default, the node types returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param include_disabled_types: Defines whether or not to include disabled types.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :return: :class:`List[NodeType] <List[NodeType]>`

        Usage:
        ::

            result = api.list_node_types_all(
                include_disabled_types=False,
            )
        """

        return fetch_all_pages(
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

    def list_database_backups(
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
    ) -> ListDatabaseBackupsResponse:
        """
        List database backups.
        List all backups in a specified region, for a given Scaleway Organization or Scaleway Project. By default, the backups listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the database backups.
        :param order_by: Criteria to use when ordering database backups listing.
        :param instance_id: UUID of the Database Instance.
        :param organization_id: Organization ID of the Organization the database backups belong to.
        :param project_id: Project ID of the Project the database backups belong to.
        :param page:
        :param page_size:
        :return: :class:`ListDatabaseBackupsResponse <ListDatabaseBackupsResponse>`

        Usage:
        ::

            result = api.list_database_backups()
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

    def list_database_backups_all(
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
        List database backups.
        List all backups in a specified region, for a given Scaleway Organization or Scaleway Project. By default, the backups listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the database backups.
        :param order_by: Criteria to use when ordering database backups listing.
        :param instance_id: UUID of the Database Instance.
        :param organization_id: Organization ID of the Organization the database backups belong to.
        :param project_id: Project ID of the Project the database backups belong to.
        :param page:
        :param page_size:
        :return: :class:`List[DatabaseBackup] <List[DatabaseBackup]>`

        Usage:
        ::

            result = api.list_database_backups_all()
        """

        return fetch_all_pages(
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

    def create_database_backup(
        self,
        *,
        instance_id: str,
        database_name: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> DatabaseBackup:
        """
        Create a database backup.
        Create a new backup. You must set the `instance_id`, `database_name`, `name` and `expires_at` parameters.
        :param instance_id: UUID of the Database Instance.
        :param database_name: Name of the database you want to back up.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the backup.
        :param expires_at: Expiration date (must follow the ISO 8601 format).
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = api.create_database_backup(
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

    def get_database_backup(
        self,
        *,
        database_backup_id: str,
        region: Optional[Region] = None,
    ) -> DatabaseBackup:
        """
        Get a database backup.
        Retrieve information about a given backup, specified by its database backup ID and region. Full details about the backup, like size, URL and expiration date, are returned in the response.
        :param database_backup_id: UUID of the database backup.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = api.get_database_backup(
                database_backup_id="example",
            )
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

    def wait_for_database_backup(
        self,
        *,
        database_backup_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[DatabaseBackup, bool]] = None,
    ) -> DatabaseBackup:
        """
        Get a database backup.
        Retrieve information about a given backup, specified by its database backup ID and region. Full details about the backup, like size, URL and expiration date, are returned in the response.
        :param database_backup_id: UUID of the database backup.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = api.get_database_backup(
                database_backup_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = (
                lambda res: res.status not in DATABASE_BACKUP_TRANSIENT_STATUSES
            )

        return wait_for_resource(
            fetcher=self.get_database_backup,
            options=options,
            args={
                "database_backup_id": database_backup_id,
                "region": region,
            },
        )

    def update_database_backup(
        self,
        *,
        database_backup_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> DatabaseBackup:
        """
        Update a database backup.
        Update the parameters of a backup, including name and expiration date.
        :param database_backup_id: UUID of the database backup to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the Database Backup.
        :param expires_at: Expiration date (must follow the ISO 8601 format).
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = api.update_database_backup(
                database_backup_id="example",
            )
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

    def delete_database_backup(
        self,
        *,
        database_backup_id: str,
        region: Optional[Region] = None,
    ) -> DatabaseBackup:
        """
        Delete a database backup.
        Delete a backup, specified by its database backup ID and region. Deleting a backup is permanent, and cannot be undone.
        :param database_backup_id: UUID of the database backup to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = api.delete_database_backup(
                database_backup_id="example",
            )
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

    def restore_database_backup(
        self,
        *,
        database_backup_id: str,
        instance_id: str,
        region: Optional[Region] = None,
        database_name: Optional[str] = None,
    ) -> DatabaseBackup:
        """
        Restore a database backup.
        Launch the process of restoring database backup. You must specify the `instance_id` of the Database Instance of destination, where the backup will be restored. Note that large database backups can take up to several hours to restore.
        :param database_backup_id: Backup of a logical database.
        :param instance_id: Defines the Database Instance where the backup has to be restored.
        :param region: Region to target. If none is passed will use default region from the config.
        :param database_name: Defines the destination database to restore into a specified database (the default destination is set to the origin database of the backup).
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = api.restore_database_backup(
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

    def export_database_backup(
        self,
        *,
        database_backup_id: str,
        region: Optional[Region] = None,
    ) -> DatabaseBackup:
        """
        Export a database backup.
        Export a backup, specified by the `database_backup_id` and the `region` parameters. The download URL is returned in the response.
        :param database_backup_id: UUID of the database backup you want to export.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DatabaseBackup <DatabaseBackup>`

        Usage:
        ::

            result = api.export_database_backup(
                database_backup_id="example",
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
            f"/rdb/v1/regions/{param_region}/backups/{param_database_backup_id}/export",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseBackup(res.json())

    def upgrade_instance(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        node_type: Optional[str] = None,
        enable_ha: Optional[bool] = None,
        volume_size: Optional[int] = None,
        volume_type: Optional[VolumeType] = None,
        upgradable_version_id: Optional[str] = None,
        major_upgrade_workflow: Optional[
            UpgradeInstanceRequestMajorUpgradeWorkflow
        ] = None,
    ) -> Instance:
        """
        Upgrade a Database Instance.
        Upgrade your current Database Instance specifications like node type, high availability, volume, or the database engine version. Note that upon upgrade the `enable_ha` parameter can only be set to `true`.
        :param instance_id: UUID of the Database Instance you want to upgrade.
        :param region: Region to target. If none is passed will use default region from the config.
        :param node_type: Node type of the Database Instance you want to upgrade to.
        One-Of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id', 'major_upgrade_workflow' could be set.
        :param enable_ha: Defines whether or not high availability should be enabled on the Database Instance.
        One-Of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id', 'major_upgrade_workflow' could be set.
        :param volume_size: Increase your block storage volume size.
        One-Of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id', 'major_upgrade_workflow' could be set.
        :param volume_type: Change your Database Instance storage type.
        One-Of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id', 'major_upgrade_workflow' could be set.
        :param upgradable_version_id: This will create a new Database Instance with same specifications as the current one and perform a Database Engine upgrade.
        One-Of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id', 'major_upgrade_workflow' could be set.
        :param major_upgrade_workflow: Upgrade your database engine to a new major version including instance endpoints.
        One-Of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id', 'major_upgrade_workflow' could be set.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = api.upgrade_instance(
                instance_id="example",
            )
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
                    major_upgrade_workflow=major_upgrade_workflow,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    def list_instances(
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
    ) -> ListInstancesResponse:
        """
        List Database Instances.
        List all Database Instances in the specified region, for a given Scaleway Organization or Scaleway Project. By default, the Database Instances returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. You can define additional parameters for your query, such as `tags` and `name`. For the `name` parameter, the value you include will be checked against the whole name string to see if it includes the string you put in the parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tags: List Database Instances that have a given tag.
        :param name: Lists Database Instances that match a name pattern.
        :param order_by: Criteria to use when ordering Database Instance listings.
        :param organization_id: Please use project_id instead.
        :param project_id: Project ID to list the Database Instance of.
        :param page:
        :param page_size:
        :return: :class:`ListInstancesResponse <ListInstancesResponse>`

        Usage:
        ::

            result = api.list_instances()
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

    def list_instances_all(
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
        List Database Instances.
        List all Database Instances in the specified region, for a given Scaleway Organization or Scaleway Project. By default, the Database Instances returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. You can define additional parameters for your query, such as `tags` and `name`. For the `name` parameter, the value you include will be checked against the whole name string to see if it includes the string you put in the parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tags: List Database Instances that have a given tag.
        :param name: Lists Database Instances that match a name pattern.
        :param order_by: Criteria to use when ordering Database Instance listings.
        :param organization_id: Please use project_id instead.
        :param project_id: Project ID to list the Database Instance of.
        :param page:
        :param page_size:
        :return: :class:`List[Instance] <List[Instance]>`

        Usage:
        ::

            result = api.list_instances_all()
        """

        return fetch_all_pages(
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

    def get_instance(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
    ) -> Instance:
        """
        Get a Database Instance.
        Retrieve information about a given Database Instance, specified by the `region` and `instance_id` parameters. Its full details, including name, status, IP address and port, are returned in the response object.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = api.get_instance(
                instance_id="example",
            )
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

    def wait_for_instance(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Instance, bool]] = None,
    ) -> Instance:
        """
        Get a Database Instance.
        Retrieve information about a given Database Instance, specified by the `region` and `instance_id` parameters. Its full details, including name, status, IP address and port, are returned in the response object.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = api.get_instance(
                instance_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in INSTANCE_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_instance,
            options=options,
            args={
                "instance_id": instance_id,
                "region": region,
            },
        )

    def create_instance(
        self,
        *,
        engine: str,
        user_name: str,
        password: str,
        node_type: str,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        is_ha_cluster: bool,
        disable_backup: bool,
        volume_size: int,
        backup_same_region: bool,
        tags: Optional[List[str]] = None,
        init_settings: Optional[List[InstanceSetting]] = None,
        volume_type: Optional[VolumeType] = None,
        init_endpoints: Optional[List[EndpointSpec]] = None,
        encryption: Optional[EncryptionAtRest] = None,
    ) -> Instance:
        """
        Create a Database Instance.
        Create a new Database Instance. You must set the `engine`, `user_name`, `password` and `node_type` parameters. Optionally, you can specify the volume type and size.
        :param engine: Database engine of the Database Instance (PostgreSQL, MySQL, ...).
        :param user_name: Username created when the Database Instance is created.
        :param password: Password of the user.
        :param node_type: Type of node to use for the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Please use project_id instead.
        One-Of ('project_identifier'): at most one of 'project_id', 'organization_id' could be set.
        :param project_id: The Project ID on which the Database Instance will be created.
        One-Of ('project_identifier'): at most one of 'project_id', 'organization_id' could be set.
        :param name: Name of the Database Instance.
        :param is_ha_cluster: Defines whether or not High-Availability is enabled.
        :param disable_backup: Defines whether or not backups are disabled.
        :param volume_size: Volume size when volume_type is not lssd.
        :param backup_same_region: Defines whether to or not to store logical backups in the same region as the Database Instance.
        :param tags: Tags to apply to the Database Instance.
        :param init_settings: List of engine settings to be set upon Database Instance initialization.
        :param volume_type: Type of volume where data is stored (lssd, bssd, ...).
        :param init_endpoints: One or multiple EndpointSpec used to expose your Database Instance. A load_balancer public endpoint is systematically created.
        :param encryption: Encryption at rest settings for your Database Instance.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = api.create_instance(
                engine="example",
                user_name="example",
                password="example",
                node_type="example",
                is_ha_cluster=False,
                disable_backup=False,
                volume_size=1,
                backup_same_region=False,
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
                    region=region,
                    name=name or random_name(prefix="ins"),
                    is_ha_cluster=is_ha_cluster,
                    disable_backup=disable_backup,
                    volume_size=volume_size,
                    backup_same_region=backup_same_region,
                    tags=tags,
                    init_settings=init_settings,
                    volume_type=volume_type,
                    init_endpoints=init_endpoints,
                    encryption=encryption,
                    project_id=project_id,
                    organization_id=organization_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    def update_instance(
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
        backup_schedule_start_hour: Optional[int] = None,
    ) -> Instance:
        """
        Update a Database Instance.
        Update the parameters of a Database Instance, including name, tags and backup schedule details.
        :param instance_id: UUID of the Database Instance to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param backup_schedule_frequency: In hours.
        :param backup_schedule_retention: In days.
        :param is_backup_schedule_disabled: Defines whether or not the backup schedule is disabled.
        :param name: Name of the Database Instance.
        :param tags: Tags of a Database Instance.
        :param logs_policy: Logs policy of the Database Instance.
        :param backup_same_region: Store logical backups in the same region as the Database Instance.
        :param backup_schedule_start_hour: Defines the start time of the autobackup.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = api.update_instance(
                instance_id="example",
            )
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
                    backup_schedule_start_hour=backup_schedule_start_hour,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    def delete_instance(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
    ) -> Instance:
        """
        Delete a Database Instance.
        Delete a given Database Instance, specified by the `region` and `instance_id` parameters. Deleting a Database Instance is permanent, and cannot be undone. Note that upon deletion all your data will be lost.
        :param instance_id: UUID of the Database Instance to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = api.delete_instance(
                instance_id="example",
            )
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

    def clone_instance(
        self,
        *,
        instance_id: str,
        name: str,
        region: Optional[Region] = None,
        node_type: Optional[str] = None,
    ) -> Instance:
        """
        Clone a Database Instance.
        Clone a given Database Instance, specified by the `region` and `instance_id` parameters. The clone feature allows you to create a new Database Instance from an existing one. The clone includes all existing databases, users and permissions. You can create a clone on a Database Instance bigger than your current one.
        :param instance_id: UUID of the Database Instance you want to clone.
        :param name: Name of the Database Instance clone.
        :param region: Region to target. If none is passed will use default region from the config.
        :param node_type: Node type of the clone.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = api.clone_instance(
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

    def restart_instance(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
    ) -> Instance:
        """
        Restart Database Instance.
        Restart a given Database Instance, specified by the `region` and `instance_id` parameters. The status of the Database Instance returned in the response.
        :param instance_id: UUID of the Database Instance you want to restart.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = api.restart_instance(
                instance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/restart",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    def get_instance_certificate(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
    ) -> ScwFile:
        """
        Get the TLS certificate of a Database Instance.
        Retrieve information about the TLS certificate of a given Database Instance. Details like name and content are returned in the response.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = api.get_instance_certificate(
                instance_id="example",
            )
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
        return unmarshal_ScwFile(res.json())

    def renew_instance_certificate(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Renew the TLS certificate of a Database Instance.
        Renew a TLS for a Database Instance. Renewing a certificate means that you will not be able to connect to your Database Instance using the previous certificate. You will also need to download and update the new certificate for all database clients.
        :param instance_id: UUID of the Database Instance you want logs of.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.renew_instance_certificate(
                instance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/renew-certificate",
            body={},
        )

        self._throw_on_error(res)

    def get_instance_metrics(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        metric_name: Optional[str] = None,
    ) -> InstanceMetrics:
        """
        Get Database Instance metrics.
        Retrieve the time series metrics of a given Database Instance. You can define the period from which to retrieve metrics by specifying the `start_date` and `end_date`.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param start_date: Start date to gather metrics from.
        :param end_date: End date to gather metrics from.
        :param metric_name: Name of the metric to gather.
        :return: :class:`InstanceMetrics <InstanceMetrics>`

        Usage:
        ::

            result = api.get_instance_metrics(
                instance_id="example",
            )
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

    def create_read_replica(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        endpoint_spec: Optional[List[ReadReplicaEndpointSpec]] = None,
        same_zone: Optional[bool] = None,
    ) -> ReadReplica:
        """
        Create a Read Replica.
        Create a new Read Replica of a Database Instance. You must specify the `region` and the `instance_id`. You can only create a maximum of 3 Read Replicas per Database Instance.
        :param instance_id: UUID of the Database Instance you want to create a Read Replica from.
        :param region: Region to target. If none is passed will use default region from the config.
        :param endpoint_spec: Specification of the endpoint you want to create.
        :param same_zone: Defines whether to create the replica in the same availability zone as the main instance nodes or not.
        :return: :class:`ReadReplica <ReadReplica>`

        Usage:
        ::

            result = api.create_read_replica(
                instance_id="example",
            )
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
                    same_zone=same_zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ReadReplica(res.json())

    def get_read_replica(
        self,
        *,
        read_replica_id: str,
        region: Optional[Region] = None,
    ) -> ReadReplica:
        """
        Get a Read Replica.
        Retrieve information about a Database Instance Read Replica. Full details about the Read Replica, like `endpoints`, `status`  and `region` are returned in the response.
        :param read_replica_id: UUID of the Read Replica.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ReadReplica <ReadReplica>`

        Usage:
        ::

            result = api.get_read_replica(
                read_replica_id="example",
            )
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

    def wait_for_read_replica(
        self,
        *,
        read_replica_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[ReadReplica, bool]] = None,
    ) -> ReadReplica:
        """
        Get a Read Replica.
        Retrieve information about a Database Instance Read Replica. Full details about the Read Replica, like `endpoints`, `status`  and `region` are returned in the response.
        :param read_replica_id: UUID of the Read Replica.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ReadReplica <ReadReplica>`

        Usage:
        ::

            result = api.get_read_replica(
                read_replica_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in READ_REPLICA_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_read_replica,
            options=options,
            args={
                "read_replica_id": read_replica_id,
                "region": region,
            },
        )

    def delete_read_replica(
        self,
        *,
        read_replica_id: str,
        region: Optional[Region] = None,
    ) -> ReadReplica:
        """
        Delete a Read Replica.
        Delete a Read Replica of a Database Instance. You must specify the `region` and `read_replica_id` parameters of the Read Replica you want to delete.
        :param read_replica_id: UUID of the Read Replica.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ReadReplica <ReadReplica>`

        Usage:
        ::

            result = api.delete_read_replica(
                read_replica_id="example",
            )
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

    def reset_read_replica(
        self,
        *,
        read_replica_id: str,
        region: Optional[Region] = None,
    ) -> ReadReplica:
        """
        Resync a Read Replica.
        When you resync a Read Replica, first it is reset, then its data is resynchronized from the primary node. Your Read Replica remains unavailable during the resync process. The duration of this process is proportional to the size of your Database Instance.
        The configured endpoints do not change.
        :param read_replica_id: UUID of the Read Replica.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ReadReplica <ReadReplica>`

        Usage:
        ::

            result = api.reset_read_replica(
                read_replica_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_read_replica_id = validate_path_param("read_replica_id", read_replica_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/read-replicas/{param_read_replica_id}/reset",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_ReadReplica(res.json())

    def promote_read_replica(
        self,
        *,
        read_replica_id: str,
        region: Optional[Region] = None,
    ) -> Instance:
        """
        Promote a Read Replica.
        Promote a Read Replica to Database Instance automatically.
        :param read_replica_id: UUID of the Read Replica.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = api.promote_read_replica(
                read_replica_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_read_replica_id = validate_path_param("read_replica_id", read_replica_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/read-replicas/{param_read_replica_id}/promote",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    def create_read_replica_endpoint(
        self,
        *,
        read_replica_id: str,
        endpoint_spec: List[ReadReplicaEndpointSpec],
        region: Optional[Region] = None,
    ) -> ReadReplica:
        """
        Create an endpoint for a Read Replica.
        Create a new endpoint for a Read Replica. Read Replicas can have at most one direct access and one Private Network endpoint.
        :param read_replica_id: UUID of the Read Replica.
        :param endpoint_spec: Specification of the endpoint you want to create.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ReadReplica <ReadReplica>`

        Usage:
        ::

            result = api.create_read_replica_endpoint(
                read_replica_id="example",
                endpoint_spec=[],
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

    def prepare_instance_logs(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> PrepareInstanceLogsResponse:
        """
        Prepare logs of a Database Instance.
        Prepare your Database Instance logs. You can define the `start_date` and `end_date` parameters for your query. The download URL is returned in the response. Logs are recorded from 00h00 to 23h59 and then aggregated in a `.log` file once a day. Therefore, even if you specify a timeframe from which you want to get the logs, you will receive logs from the full 24 hours.
        :param instance_id: UUID of the Database Instance you want logs of.
        :param region: Region to target. If none is passed will use default region from the config.
        :param start_date: Start datetime of your log. (RFC 3339 format).
        :param end_date: End datetime of your log. (RFC 3339 format).
        :return: :class:`PrepareInstanceLogsResponse <PrepareInstanceLogsResponse>`

        Usage:
        ::

            result = api.prepare_instance_logs(
                instance_id="example",
            )
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

    def list_instance_logs(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListInstanceLogsRequestOrderBy] = None,
    ) -> ListInstanceLogsResponse:
        """
        List available logs of a Database Instance.
        List the available logs of a Database Instance. By default, the logs returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field.
        :param instance_id: UUID of the Database Instance you want logs of.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Criteria to use when ordering Database Instance logs listing.
        :return: :class:`ListInstanceLogsResponse <ListInstanceLogsResponse>`

        Usage:
        ::

            result = api.list_instance_logs(
                instance_id="example",
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

    def get_instance_log(
        self,
        *,
        instance_log_id: str,
        region: Optional[Region] = None,
    ) -> InstanceLog:
        """
        Get given logs of a Database Instance.
        Retrieve information about the logs of a Database Instance. Specify the `instance_log_id` and `region` in your request to get information such as `download_url`, `status`, `expires_at` and `created_at` about your logs in the response.
        :param instance_log_id: UUID of the instance_log you want.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`InstanceLog <InstanceLog>`

        Usage:
        ::

            result = api.get_instance_log(
                instance_log_id="example",
            )
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

    def wait_for_instance_log(
        self,
        *,
        instance_log_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[InstanceLog, bool]] = None,
    ) -> InstanceLog:
        """
        Get given logs of a Database Instance.
        Retrieve information about the logs of a Database Instance. Specify the `instance_log_id` and `region` in your request to get information such as `download_url`, `status`, `expires_at` and `created_at` about your logs in the response.
        :param instance_log_id: UUID of the instance_log you want.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`InstanceLog <InstanceLog>`

        Usage:
        ::

            result = api.get_instance_log(
                instance_log_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in INSTANCE_LOG_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_instance_log,
            options=options,
            args={
                "instance_log_id": instance_log_id,
                "region": region,
            },
        )

    def purge_instance_logs(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        log_name: Optional[str] = None,
    ) -> None:
        """
        Purge remote Database Instance logs.
        Purge a given remote log from a Database Instance. You can specify the `log_name` of the log you wish to clean from your Database Instance.
        :param instance_id: UUID of the Database Instance you want logs of.
        :param region: Region to target. If none is passed will use default region from the config.
        :param log_name: Given log name to purge.

        Usage:
        ::

            result = api.purge_instance_logs(
                instance_id="example",
            )
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

    def list_instance_logs_details(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
    ) -> ListInstanceLogsDetailsResponse:
        """
        List remote Database Instance logs details.
        List remote log details. By default, the details returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field.
        :param instance_id: UUID of the Database Instance you want logs of.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ListInstanceLogsDetailsResponse <ListInstanceLogsDetailsResponse>`

        Usage:
        ::

            result = api.list_instance_logs_details(
                instance_id="example",
            )
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

    def add_instance_settings(
        self,
        *,
        instance_id: str,
        settings: List[InstanceSetting],
        region: Optional[Region] = None,
    ) -> AddInstanceSettingsResponse:
        """
        Add Database Instance advanced settings.
        Add an advanced setting to a Database Instance. You must set the `name` and the `value` of each setting.
        :param instance_id: UUID of the Database Instance you want to add settings to.
        :param settings: Settings to add to the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`AddInstanceSettingsResponse <AddInstanceSettingsResponse>`

        Usage:
        ::

            result = api.add_instance_settings(
                instance_id="example",
                settings=[],
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

    def delete_instance_settings(
        self,
        *,
        instance_id: str,
        setting_names: List[str],
        region: Optional[Region] = None,
    ) -> DeleteInstanceSettingsResponse:
        """
        Delete Database Instance advanced settings.
        Delete an advanced setting in a Database Instance. You must specify the names of the settings you want to delete in the request.
        :param instance_id: UUID of the Database Instance to delete settings from.
        :param setting_names: Settings names to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DeleteInstanceSettingsResponse <DeleteInstanceSettingsResponse>`

        Usage:
        ::

            result = api.delete_instance_settings(
                instance_id="example",
                setting_names=[],
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

    def set_instance_settings(
        self,
        *,
        instance_id: str,
        settings: List[InstanceSetting],
        region: Optional[Region] = None,
    ) -> SetInstanceSettingsResponse:
        """
        Set Database Instance advanced settings.
        Update an advanced setting for a Database Instance. Settings added upon database engine initalization can only be defined once, and cannot, therefore, be updated.
        :param instance_id: UUID of the Database Instance where the settings must be set.
        :param settings: Settings to define for the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`SetInstanceSettingsResponse <SetInstanceSettingsResponse>`

        Usage:
        ::

            result = api.set_instance_settings(
                instance_id="example",
                settings=[],
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

    def list_instance_acl_rules(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListInstanceACLRulesResponse:
        """
        List ACL rules of a Database Instance.
        List the ACL rules for a given Database Instance. The response is an array of ACL objects, each one representing an ACL that denies, allows or redirects traffic based on certain conditions.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :return: :class:`ListInstanceACLRulesResponse <ListInstanceACLRulesResponse>`

        Usage:
        ::

            result = api.list_instance_acl_rules(
                instance_id="example",
            )
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

    def list_instance_acl_rules_all(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ACLRule]:
        """
        List ACL rules of a Database Instance.
        List the ACL rules for a given Database Instance. The response is an array of ACL objects, each one representing an ACL that denies, allows or redirects traffic based on certain conditions.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :return: :class:`List[ACLRule] <List[ACLRule]>`

        Usage:
        ::

            result = api.list_instance_acl_rules_all(
                instance_id="example",
            )
        """

        return fetch_all_pages(
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

    def add_instance_acl_rules(
        self,
        *,
        instance_id: str,
        rules: List[ACLRuleRequest],
        region: Optional[Region] = None,
    ) -> AddInstanceACLRulesResponse:
        """
        Add an ACL rule to a Database Instance.
        Add an additional ACL rule to a Database Instance.
        :param instance_id: UUID of the Database Instance you want to add ACL rules to.
        :param rules: ACL rules to add to the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`AddInstanceACLRulesResponse <AddInstanceACLRulesResponse>`

        Usage:
        ::

            result = api.add_instance_acl_rules(
                instance_id="example",
                rules=[],
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

    def set_instance_acl_rules(
        self,
        *,
        instance_id: str,
        rules: List[ACLRuleRequest],
        region: Optional[Region] = None,
    ) -> SetInstanceACLRulesResponse:
        """
        Set ACL rules for a Database Instance.
        Replace all the ACL rules of a Database Instance.
        :param instance_id: UUID of the Database Instance where the ACL rules must be set.
        :param rules: ACL rules to define for the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`SetInstanceACLRulesResponse <SetInstanceACLRulesResponse>`

        Usage:
        ::

            result = api.set_instance_acl_rules(
                instance_id="example",
                rules=[],
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

    def delete_instance_acl_rules(
        self,
        *,
        instance_id: str,
        acl_rule_ips: List[str],
        region: Optional[Region] = None,
    ) -> DeleteInstanceACLRulesResponse:
        """
        Delete ACL rules of a Database Instance.
        Delete one or more ACL rules of a Database Instance.
        :param instance_id: UUID of the Database Instance you want to delete an ACL rule from.
        :param acl_rule_ips: IP addresses defined in the ACL rules of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DeleteInstanceACLRulesResponse <DeleteInstanceACLRulesResponse>`

        Usage:
        ::

            result = api.delete_instance_acl_rules(
                instance_id="example",
                acl_rule_ips=[],
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

    def list_users(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: Optional[ListUsersRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListUsersResponse:
        """
        List users of a Database Instance.
        List all users of a given Database Instance. By default, the users returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the user.
        :param order_by: Criteria to use when requesting user listing.
        :param page:
        :param page_size:
        :return: :class:`ListUsersResponse <ListUsersResponse>`

        Usage:
        ::

            result = api.list_users(
                instance_id="example",
            )
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

    def list_users_all(
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
        List users of a Database Instance.
        List all users of a given Database Instance. By default, the users returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the user.
        :param order_by: Criteria to use when requesting user listing.
        :param page:
        :param page_size:
        :return: :class:`List[User] <List[User]>`

        Usage:
        ::

            result = api.list_users_all(
                instance_id="example",
            )
        """

        return fetch_all_pages(
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

    def create_user(
        self,
        *,
        instance_id: str,
        name: str,
        password: str,
        is_admin: bool,
        region: Optional[Region] = None,
    ) -> User:
        """
        Create a user for a Database Instance.
        Create a new user for a Database Instance. You must define the `name`, `password` and `is_admin` parameters.
        :param instance_id: UUID of the Database Instance in which you want to create a user.
        :param name: Name of the user you want to create.
        :param password: Password of the user you want to create.
        :param is_admin: Defines whether the user will have administrative privileges.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`User <User>`

        Usage:
        ::

            result = api.create_user(
                instance_id="example",
                name="example",
                password="example",
                is_admin=False,
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

    def update_user(
        self,
        *,
        instance_id: str,
        name: str,
        region: Optional[Region] = None,
        password: Optional[str] = None,
        is_admin: Optional[bool] = None,
    ) -> User:
        """
        Update a user on a Database Instance.
        Update the parameters of a user on a Database Instance. You can update the `password` and `is_admin` parameters, but you cannot change the name of the user.
        :param instance_id: UUID of the Database Instance the user belongs to.
        :param name: Name of the database user.
        :param region: Region to target. If none is passed will use default region from the config.
        :param password: Password of the database user.
        :param is_admin: Defines whether or not this user got administrative privileges.
        :return: :class:`User <User>`

        Usage:
        ::

            result = api.update_user(
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

    def delete_user(
        self,
        *,
        instance_id: str,
        name: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a user on a Database Instance.
        Delete a given user on a Database Instance. You must specify, in the endpoint,  the `region`, `instance_id` and `name` parameters of the user you want to delete.
        :param instance_id: UUID of the Database Instance to delete the user from.
        :param name: Name of the user.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_user(
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

    def list_databases(
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
    ) -> ListDatabasesResponse:
        """
        List databases in a Database Instance.
        List all databases of a given Database Instance. By default, the databases returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. You can define additional parameters for your query, such as `name`, `managed` and `owner`.
        :param instance_id: UUID of the Database Instance to list the databases of.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the database.
        :param managed: Defines whether or not the database is managed.
        :param owner: User that owns this database.
        :param order_by: Criteria to use when ordering database listing.
        :param page:
        :param page_size:
        :return: :class:`ListDatabasesResponse <ListDatabasesResponse>`

        Usage:
        ::

            result = api.list_databases(
                instance_id="example",
            )
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

    def list_databases_all(
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
        List databases in a Database Instance.
        List all databases of a given Database Instance. By default, the databases returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. You can define additional parameters for your query, such as `name`, `managed` and `owner`.
        :param instance_id: UUID of the Database Instance to list the databases of.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the database.
        :param managed: Defines whether or not the database is managed.
        :param owner: User that owns this database.
        :param order_by: Criteria to use when ordering database listing.
        :param page:
        :param page_size:
        :return: :class:`List[Database] <List[Database]>`

        Usage:
        ::

            result = api.list_databases_all(
                instance_id="example",
            )
        """

        return fetch_all_pages(
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

    def create_database(
        self,
        *,
        instance_id: str,
        name: str,
        region: Optional[Region] = None,
    ) -> Database:
        """
        Create a database in a Database Instance.
        Create a new database. You must define the `name` parameter in the request.
        :param instance_id: UUID of the Database Instance where to create the database.
        :param name: Name of the database.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Database <Database>`

        Usage:
        ::

            result = api.create_database(
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

    def delete_database(
        self,
        *,
        instance_id: str,
        name: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a database in a Database Instance.
        Delete a given database on a Database Instance. You must specify, in the endpoint, the `region`, `instance_id` and `name` parameters of the database you want to delete.
        :param instance_id: UUID of the Database Instance where to delete the database.
        :param name: Name of the database to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_database(
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

    def list_privileges(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListPrivilegesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        database_name: Optional[str] = None,
        user_name: Optional[str] = None,
    ) -> ListPrivilegesResponse:
        """
        List user privileges for a database.
        List privileges of a user on a database. By default, the details returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. You can define additional parameters for your query, such as `database_name` and `user_name`.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Criteria to use when ordering privileges listing.
        :param page:
        :param page_size:
        :param database_name: Name of the database.
        :param user_name: Name of the user.
        :return: :class:`ListPrivilegesResponse <ListPrivilegesResponse>`

        Usage:
        ::

            result = api.list_privileges(
                instance_id="example",
            )
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

    def list_privileges_all(
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
        List user privileges for a database.
        List privileges of a user on a database. By default, the details returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. You can define additional parameters for your query, such as `database_name` and `user_name`.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Criteria to use when ordering privileges listing.
        :param page:
        :param page_size:
        :param database_name: Name of the database.
        :param user_name: Name of the user.
        :return: :class:`List[Privilege] <List[Privilege]>`

        Usage:
        ::

            result = api.list_privileges_all(
                instance_id="example",
            )
        """

        return fetch_all_pages(
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

    def set_privilege(
        self,
        *,
        instance_id: str,
        database_name: str,
        user_name: str,
        region: Optional[Region] = None,
        permission: Optional[Permission] = None,
    ) -> Privilege:
        """
        Set user privileges for a database.
        Set the privileges of a user on a database. You must define `database_name`, `user_name` and `permission` in the request body.
        :param instance_id: UUID of the Database Instance.
        :param database_name: Name of the database.
        :param user_name: Name of the user.
        :param region: Region to target. If none is passed will use default region from the config.
        :param permission: Permission to set (Read, Read/Write, All, Custom).
        :return: :class:`Privilege <Privilege>`

        Usage:
        ::

            result = api.set_privilege(
                instance_id="example",
                database_name="example",
                user_name="example",
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
                    region=region,
                    permission=permission,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Privilege(res.json())

    def list_snapshots(
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
    ) -> ListSnapshotsResponse:
        """
        List snapshots.
        List snapshots. You can include the `instance_id` or `project_id` in your query to get the list of snapshots for specific Database Instances and/or Projects. By default, the details returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the snapshot.
        :param order_by: Criteria to use when ordering snapshot listing.
        :param instance_id: UUID of the Database Instance.
        :param organization_id: Organization ID the snapshots belongs to.
        :param project_id: Project ID the snapshots belongs to.
        :param page:
        :param page_size:
        :return: :class:`ListSnapshotsResponse <ListSnapshotsResponse>`

        Usage:
        ::

            result = api.list_snapshots()
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

    def list_snapshots_all(
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
        List snapshots.
        List snapshots. You can include the `instance_id` or `project_id` in your query to get the list of snapshots for specific Database Instances and/or Projects. By default, the details returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the snapshot.
        :param order_by: Criteria to use when ordering snapshot listing.
        :param instance_id: UUID of the Database Instance.
        :param organization_id: Organization ID the snapshots belongs to.
        :param project_id: Project ID the snapshots belongs to.
        :param page:
        :param page_size:
        :return: :class:`List[Snapshot] <List[Snapshot]>`

        Usage:
        ::

            result = api.list_snapshots_all()
        """

        return fetch_all_pages(
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

    def get_snapshot(
        self,
        *,
        snapshot_id: str,
        region: Optional[Region] = None,
    ) -> Snapshot:
        """
        Get a Database Instance snapshot.
        Retrieve information about a given snapshot, specified by its `snapshot_id` and `region`. Full details about the snapshot, like size and expiration date, are returned in the response.
        :param snapshot_id: UUID of the snapshot.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.get_snapshot(
                snapshot_id="example",
            )
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

    def wait_for_snapshot(
        self,
        *,
        snapshot_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Snapshot, bool]] = None,
    ) -> Snapshot:
        """
        Get a Database Instance snapshot.
        Retrieve information about a given snapshot, specified by its `snapshot_id` and `region`. Full details about the snapshot, like size and expiration date, are returned in the response.
        :param snapshot_id: UUID of the snapshot.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.get_snapshot(
                snapshot_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in SNAPSHOT_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_snapshot,
            options=options,
            args={
                "snapshot_id": snapshot_id,
                "region": region,
            },
        )

    def create_snapshot(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> Snapshot:
        """
        Create a Database Instance snapshot.
        Create a new snapshot of a Database Instance. You must define the `name` parameter in the request.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the snapshot.
        :param expires_at: Expiration date (must follow the ISO 8601 format).
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.create_snapshot(
                instance_id="example",
            )
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

    def update_snapshot(
        self,
        *,
        snapshot_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> Snapshot:
        """
        Update a Database Instance snapshot.
        Update the parameters of a snapshot of a Database Instance. You can update the `name` and `expires_at` parameters.
        :param snapshot_id: UUID of the snapshot to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the snapshot.
        :param expires_at: Expiration date (must follow the ISO 8601 format).
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.update_snapshot(
                snapshot_id="example",
            )
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

    def delete_snapshot(
        self,
        *,
        snapshot_id: str,
        region: Optional[Region] = None,
    ) -> Snapshot:
        """
        Delete a Database Instance snapshot.
        Delete a given snapshot of a Database Instance. You must specify, in the endpoint,  the `region` and `snapshot_id` parameters of the snapshot you want to delete.
        :param snapshot_id: UUID of the snapshot to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.delete_snapshot(
                snapshot_id="example",
            )
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

    def create_instance_from_snapshot(
        self,
        *,
        snapshot_id: str,
        instance_name: str,
        region: Optional[Region] = None,
        is_ha_cluster: Optional[bool] = None,
        node_type: Optional[str] = None,
    ) -> Instance:
        """
        Create a new Database Instance from a snapshot.
        Restore a snapshot. When you restore a snapshot, a new Instance is created and billed to your account. Note that is possible to select a larger node type for your new Database Instance. However, the Block volume size will be the same as the size of the restored snapshot. All Instance settings will be restored if you chose a node type with the same or more memory size than the initial Instance. Settings will be reset to the default if your node type has less memory.
        :param snapshot_id: Block snapshot of the Database Instance.
        :param instance_name: Name of the Database Instance created with the snapshot.
        :param region: Region to target. If none is passed will use default region from the config.
        :param is_ha_cluster: Defines whether or not High-Availability is enabled on the new Database Instance.
        :param node_type: The node type used to restore the snapshot.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = api.create_instance_from_snapshot(
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

    def create_endpoint(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
        endpoint_spec: Optional[EndpointSpec] = None,
    ) -> Endpoint:
        """
        Create a new Database Instance endpoint.
        Create a new endpoint for a Database Instance. You can add `load_balancer` and `private_network` specifications to the body of the request.
        :param instance_id: UUID of the Database Instance you to which you want to add an endpoint.
        :param region: Region to target. If none is passed will use default region from the config.
        :param endpoint_spec: Specification of the endpoint you want to create.
        :return: :class:`Endpoint <Endpoint>`

        Usage:
        ::

            result = api.create_endpoint(
                instance_id="example",
            )
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

    def delete_endpoint(
        self,
        *,
        endpoint_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a Database Instance endpoint.
        Delete the endpoint of a Database Instance. You must specify the `region` and `endpoint_id` parameters of the endpoint you want to delete. Note that might need to update any environment configurations that point to the deleted endpoint.
        :param endpoint_id: This endpoint can also be used to delete a Read Replica endpoint.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_endpoint(
                endpoint_id="example",
            )
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

    def get_endpoint(
        self,
        *,
        endpoint_id: str,
        region: Optional[Region] = None,
    ) -> Endpoint:
        """
        Get a Database Instance endpoint.
        Retrieve information about a Database Instance endpoint. Full details about the endpoint, like `ip`, `port`, `private_network` and `load_balancer` specifications are returned in the response.
        :param endpoint_id: UUID of the endpoint you want to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Endpoint <Endpoint>`

        Usage:
        ::

            result = api.get_endpoint(
                endpoint_id="example",
            )
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

    def migrate_endpoint(
        self,
        *,
        endpoint_id: str,
        instance_id: str,
        region: Optional[Region] = None,
    ) -> Endpoint:
        """
        Migrate an existing instance endpoint to another instance.
        :param endpoint_id: UUID of the endpoint you want to migrate.
        :param instance_id: UUID of the instance you want to attach the endpoint to.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Endpoint <Endpoint>`

        Usage:
        ::

            result = api.migrate_endpoint(
                endpoint_id="example",
                instance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_endpoint_id = validate_path_param("endpoint_id", endpoint_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/endpoints/{param_endpoint_id}/migrate",
            body=marshal_MigrateEndpointRequest(
                MigrateEndpointRequest(
                    endpoint_id=endpoint_id,
                    instance_id=instance_id,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Endpoint(res.json())

    def apply_instance_maintenance(
        self,
        *,
        instance_id: str,
        region: Optional[Region] = None,
    ) -> Maintenance:
        """
        Apply Database Instance maintenance.
        Apply maintenance tasks to your Database Instance. This will trigger pending maintenance tasks to start in your Database Instance and can generate service interruption. Maintenance tasks can be applied between `starts_at` and `stops_at` times, and are run directly by Scaleway at `forced_at` timestamp.
        :param instance_id: UUID of the Database Instance you want to apply maintenance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Maintenance <Maintenance>`

        Usage:
        ::

            result = api.apply_instance_maintenance(
                instance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/rdb/v1/regions/{param_region}/instances/{param_instance_id}/apply-maintenance",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Maintenance(res.json())
