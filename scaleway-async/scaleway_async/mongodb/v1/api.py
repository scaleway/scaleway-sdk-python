# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Awaitable, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
    ScwFile,
    unmarshal_ScwFile,
)
from scaleway_core.utils import (
    WaitForOptions,
    random_name,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    ListDatabasesRequestOrderBy,
    ListInstancesRequestOrderBy,
    ListMaintenancesRequestOrderBy,
    ListSnapshotsRequestOrderBy,
    ListUsersRequestOrderBy,
    VolumeType,
    CreateEndpointRequest,
    CreateInstanceRequest,
    CreateSnapshotRequest,
    CreateUserRequest,
    Database,
    Endpoint,
    EndpointSpec,
    Instance,
    ListDatabasesResponse,
    ListInstancesResponse,
    ListMaintenancesResponse,
    ListNodeTypesResponse,
    ListSnapshotsResponse,
    ListUsersResponse,
    ListVersionsResponse,
    Maintenance,
    NodeType,
    RestoreSnapshotRequest,
    SetUserRoleRequest,
    Snapshot,
    UpdateInstanceRequest,
    UpdateSnapshotRequest,
    UpdateUserRequest,
    UpgradeInstanceRequest,
    User,
    UserRole,
    Version,
    Volume,
)
from .content import (
    INSTANCE_TRANSIENT_STATUSES,
    MAINTENANCE_TRANSIENT_STATUSES,
    SNAPSHOT_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Endpoint,
    unmarshal_Instance,
    unmarshal_Maintenance,
    unmarshal_Snapshot,
    unmarshal_User,
    unmarshal_ListDatabasesResponse,
    unmarshal_ListInstancesResponse,
    unmarshal_ListMaintenancesResponse,
    unmarshal_ListNodeTypesResponse,
    unmarshal_ListSnapshotsResponse,
    unmarshal_ListUsersResponse,
    unmarshal_ListVersionsResponse,
    marshal_CreateEndpointRequest,
    marshal_CreateInstanceRequest,
    marshal_CreateSnapshotRequest,
    marshal_CreateUserRequest,
    marshal_RestoreSnapshotRequest,
    marshal_SetUserRoleRequest,
    marshal_UpdateInstanceRequest,
    marshal_UpdateSnapshotRequest,
    marshal_UpdateUserRequest,
    marshal_UpgradeInstanceRequest,
)


class MongodbV1API(API):
    """
    This API allows you to manage your Managed Databases for MongoDB®.
    """

    async def list_node_types(
        self,
        *,
        region: Optional[ScwRegion] = None,
        include_disabled: Optional[bool] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListNodeTypesResponse:
        """
        List available node types.
        :param region: Region to target. If none is passed will use default region from the config.
        :param include_disabled: Defines whether or not to include disabled types.
        :param page:
        :param page_size:
        :return: :class:`ListNodeTypesResponse <ListNodeTypesResponse>`

        Usage:
        ::

            result = await api.list_node_types()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/mongodb/v1/regions/{param_region}/node-types",
            params={
                "include_disabled": include_disabled,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNodeTypesResponse(res.json())

    async def list_node_types_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        include_disabled: Optional[bool] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[NodeType]:
        """
        List available node types.
        :param region: Region to target. If none is passed will use default region from the config.
        :param include_disabled: Defines whether or not to include disabled types.
        :param page:
        :param page_size:
        :return: :class:`list[NodeType] <list[NodeType]>`

        Usage:
        ::

            result = await api.list_node_types_all()
        """

        return await fetch_all_pages_async(
            type=ListNodeTypesResponse,
            key="node_types",
            fetcher=self.list_node_types,
            args={
                "region": region,
                "include_disabled": include_disabled,
                "page": page,
                "page_size": page_size,
            },
        )

    async def list_versions(
        self,
        *,
        region: Optional[ScwRegion] = None,
        version: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListVersionsResponse:
        """
        List available MongoDB® major versions.
        :param region: Region to target. If none is passed will use default region from the config.
        :param version:
        :param page:
        :param page_size:
        :return: :class:`ListVersionsResponse <ListVersionsResponse>`

        Usage:
        ::

            result = await api.list_versions()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/mongodb/v1/regions/{param_region}/versions",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "version": version,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVersionsResponse(res.json())

    async def list_versions_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        version: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Version]:
        """
        List available MongoDB® major versions.
        :param region: Region to target. If none is passed will use default region from the config.
        :param version:
        :param page:
        :param page_size:
        :return: :class:`list[Version] <list[Version]>`

        Usage:
        ::

            result = await api.list_versions_all()
        """

        return await fetch_all_pages_async(
            type=ListVersionsResponse,
            key="versions",
            fetcher=self.list_versions,
            args={
                "region": region,
                "version": version,
                "page": page,
                "page_size": page_size,
            },
        )

    async def list_instances(
        self,
        *,
        region: Optional[ScwRegion] = None,
        tags: Optional[list[str]] = None,
        name: Optional[str] = None,
        order_by: Optional[ListInstancesRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListInstancesResponse:
        """
        List MongoDB® Database Instances.
        List all MongoDB® Database Instances in the specified region. By default, the MongoDB® Database Instances returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. You can define additional parameters for your query, such as `tags` and `name`. For the `name` parameter, the value you include will be checked against the whole name string to see if it includes the string you put in the parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tags: List Database Instances that have a given tag.
        :param name: Lists Database Instances that match a name pattern.
        :param order_by: Criteria to use when ordering Database Instance listings.
        :param organization_id: Organization ID of the Database Instance.
        :param project_id: Project ID to list the instances of.
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
            f"/mongodb/v1/regions/{param_region}/instances",
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
        region: Optional[ScwRegion] = None,
        tags: Optional[list[str]] = None,
        name: Optional[str] = None,
        order_by: Optional[ListInstancesRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Instance]:
        """
        List MongoDB® Database Instances.
        List all MongoDB® Database Instances in the specified region. By default, the MongoDB® Database Instances returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. You can define additional parameters for your query, such as `tags` and `name`. For the `name` parameter, the value you include will be checked against the whole name string to see if it includes the string you put in the parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tags: List Database Instances that have a given tag.
        :param name: Lists Database Instances that match a name pattern.
        :param order_by: Criteria to use when ordering Database Instance listings.
        :param organization_id: Organization ID of the Database Instance.
        :param project_id: Project ID to list the instances of.
        :param page:
        :param page_size:
        :return: :class:`list[Instance] <list[Instance]>`

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
        region: Optional[ScwRegion] = None,
    ) -> Instance:
        """
        Get a MongoDB® Database Instance.
        Retrieve information about a given MongoDB® Database Instance, specified by the `region` and `instance_id` parameters. Its full details, including name, status, IP address and port, are returned in the response object.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.get_instance(
                instance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "GET",
            f"/mongodb/v1/regions/{param_region}/instances/{param_instance_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    async def wait_for_instance(
        self,
        *,
        instance_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[
            WaitForOptions[Instance, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Instance:
        """
        Get a MongoDB® Database Instance.
        Retrieve information about a given MongoDB® Database Instance, specified by the `region` and `instance_id` parameters. Its full details, including name, status, IP address and port, are returned in the response object.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.get_instance(
                instance_id="example",
            )
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
        version: str,
        node_amount: int,
        node_type: str,
        user_name: str,
        password: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        volume: Optional[Volume] = None,
        endpoints: Optional[list[EndpointSpec]] = None,
    ) -> Instance:
        """
        Create a MongoDB® Database Instance.
        Create a new MongoDB® Database Instance.
        :param version: Major version of the MongoDB® engine.
        :param node_amount: Number of node to use for the Database Instance.
        :param node_type: Type of node to use for the Database Instance.
        :param user_name: Username created when the Database Instance is created.
        :param password: Password of the initial user.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: The Project ID on which the Database Instance will be created.
        :param name: Name of the Database Instance.
        :param tags: Tags to apply to the Database Instance.
        :param volume: Instance volume information.
        :param endpoints: One or multiple EndpointSpec used to expose your Database Instance.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.create_instance(
                version="example",
                node_amount=1,
                node_type="example",
                user_name="example",
                password="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/mongodb/v1/regions/{param_region}/instances",
            body=marshal_CreateInstanceRequest(
                CreateInstanceRequest(
                    version=version,
                    node_amount=node_amount,
                    node_type=node_type,
                    user_name=user_name,
                    password=password,
                    region=region,
                    project_id=project_id,
                    name=name or random_name(prefix="mgdb"),
                    tags=tags,
                    volume=volume,
                    endpoints=endpoints,
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
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        snapshot_schedule_frequency_hours: Optional[int] = None,
        snapshot_schedule_retention_days: Optional[int] = None,
        is_snapshot_schedule_enabled: Optional[bool] = None,
    ) -> Instance:
        """
        Update a MongoDB® Database Instance.
        Update the parameters of a MongoDB® Database Instance.
        :param instance_id: UUID of the Database Instance to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the Database Instance.
        :param tags: Tags of a Database Instance.
        :param snapshot_schedule_frequency_hours: In hours.
        :param snapshot_schedule_retention_days: In days.
        :param is_snapshot_schedule_enabled: Defines whether or not the snapshot schedule is enabled.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.update_instance(
                instance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "PATCH",
            f"/mongodb/v1/regions/{param_region}/instances/{param_instance_id}",
            body=marshal_UpdateInstanceRequest(
                UpdateInstanceRequest(
                    instance_id=instance_id,
                    region=region,
                    name=name,
                    tags=tags,
                    snapshot_schedule_frequency_hours=snapshot_schedule_frequency_hours,
                    snapshot_schedule_retention_days=snapshot_schedule_retention_days,
                    is_snapshot_schedule_enabled=is_snapshot_schedule_enabled,
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
        region: Optional[ScwRegion] = None,
    ) -> Instance:
        """
        Delete a MongoDB® Database Instance.
        Delete a given MongoDB® Database Instance, specified by the `region` and `instance_id` parameters. Deleting a MongoDB® Database Instance is permanent, and cannot be undone. Note that upon deletion all your data will be lost.
        :param instance_id: UUID of the Database Instance to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.delete_instance(
                instance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "DELETE",
            f"/mongodb/v1/regions/{param_region}/instances/{param_instance_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    async def upgrade_instance(
        self,
        *,
        instance_id: str,
        region: Optional[ScwRegion] = None,
        volume_size_bytes: Optional[int] = None,
        version_id: Optional[str] = None,
    ) -> Instance:
        """
        Upgrade a Database Instance.
        Upgrade your current Database Instance specifications like volume size.
        :param instance_id: UUID of the Database Instance you want to upgrade.
        :param region: Region to target. If none is passed will use default region from the config.
        :param volume_size_bytes: Increase your Block Storage volume size.
        One-Of ('upgrade_target'): at most one of 'volume_size_bytes', 'version_id' could be set.
        :param version_id:
        One-Of ('upgrade_target'): at most one of 'volume_size_bytes', 'version_id' could be set.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.upgrade_instance(
                instance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/mongodb/v1/regions/{param_region}/instances/{param_instance_id}/upgrade",
            body=marshal_UpgradeInstanceRequest(
                UpgradeInstanceRequest(
                    instance_id=instance_id,
                    region=region,
                    volume_size_bytes=volume_size_bytes,
                    version_id=version_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    async def get_instance_certificate(
        self,
        *,
        instance_id: str,
        region: Optional[ScwRegion] = None,
    ) -> ScwFile:
        """
        Get the certificate of a Database Instance.
        Retrieve the certificate of a given Database Instance, specified by the `instance_id` parameter.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = await api.get_instance_certificate(
                instance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "GET",
            f"/mongodb/v1/regions/{param_region}/instances/{param_instance_id}/certificate",
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())

    async def create_snapshot(
        self,
        *,
        instance_id: str,
        name: str,
        region: Optional[ScwRegion] = None,
        expires_at: Optional[datetime] = None,
    ) -> Snapshot:
        """
        Create a Database Instance snapshot.
        Create a new snapshot of a Database Instance. You must define the `name` and `instance_id` parameters in the request.
        :param instance_id: UUID of the Database Instance to snapshot.
        :param name: Name of the snapshot.
        :param region: Region to target. If none is passed will use default region from the config.
        :param expires_at: Expiration date of the snapshot (must follow the ISO 8601 format).
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = await api.create_snapshot(
                instance_id="example",
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/mongodb/v1/regions/{param_region}/snapshots",
            body=marshal_CreateSnapshotRequest(
                CreateSnapshotRequest(
                    instance_id=instance_id,
                    name=name,
                    region=region,
                    expires_at=expires_at,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    async def get_snapshot(
        self,
        *,
        snapshot_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Snapshot:
        """
        Get a Database Instance snapshot.
        Retrieve information about a given snapshot of a Database Instance. You must specify, in the endpoint, the `snapshot_id` parameter of the snapshot you want to retrieve.
        :param snapshot_id: UUID of the snapshot.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = await api.get_snapshot(
                snapshot_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "GET",
            f"/mongodb/v1/regions/{param_region}/snapshots/{param_snapshot_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    async def wait_for_snapshot(
        self,
        *,
        snapshot_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[
            WaitForOptions[Snapshot, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Snapshot:
        """
        Get a Database Instance snapshot.
        Retrieve information about a given snapshot of a Database Instance. You must specify, in the endpoint, the `snapshot_id` parameter of the snapshot you want to retrieve.
        :param snapshot_id: UUID of the snapshot.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = await api.get_snapshot(
                snapshot_id="example",
            )
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

    async def update_snapshot(
        self,
        *,
        snapshot_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> Snapshot:
        """
        Update a Database Instance snapshot.
        Update the parameters of a snapshot of a Database Instance. You can update the `name` and `expires_at` parameters.
        :param snapshot_id: UUID of the Snapshot.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the snapshot.
        :param expires_at: Expiration date of the snapshot (must follow the ISO 8601 format).
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = await api.update_snapshot(
                snapshot_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "PATCH",
            f"/mongodb/v1/regions/{param_region}/snapshots/{param_snapshot_id}",
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

    async def restore_snapshot(
        self,
        *,
        snapshot_id: str,
        instance_name: str,
        node_type: str,
        node_amount: int,
        volume_type: VolumeType,
        region: Optional[ScwRegion] = None,
    ) -> Instance:
        """
        Restore a Database Instance snapshot.
        Restore a given snapshot of a Database Instance. You must specify, in the endpoint, the `snapshot_id` parameter of the snapshot you want to restore, the `instance_name` of the new Database Instance, `node_type` of the new Database Instance and `node_amount` of the new Database Instance.
        :param snapshot_id: UUID of the snapshot.
        :param instance_name: Name of the new Database Instance.
        :param node_type: Node type to use for the new Database Instance.
        :param node_amount: Number of nodes to use for the new Database Instance.
        :param volume_type: Instance volume type.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Instance <Instance>`

        Usage:
        ::

            result = await api.restore_snapshot(
                snapshot_id="example",
                instance_name="example",
                node_type="example",
                node_amount=1,
                volume_type=VolumeType.unknown_type,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "POST",
            f"/mongodb/v1/regions/{param_region}/snapshots/{param_snapshot_id}/restore",
            body=marshal_RestoreSnapshotRequest(
                RestoreSnapshotRequest(
                    snapshot_id=snapshot_id,
                    instance_name=instance_name,
                    node_type=node_type,
                    node_amount=node_amount,
                    volume_type=volume_type,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Instance(res.json())

    async def list_snapshots(
        self,
        *,
        region: Optional[ScwRegion] = None,
        instance_id: Optional[str] = None,
        name: Optional[str] = None,
        order_by: Optional[ListSnapshotsRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListSnapshotsResponse:
        """
        List snapshots.
        List snapshots. You can include the `instance_id` or `project_id` in your query to get the list of snapshots for specific Database Instances and/or Projects. By default, the details returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param instance_id: Instance ID the snapshots belongs to.
        :param name: Lists database snapshots that match a name pattern.
        :param order_by: Criteria to use when ordering snapshot listings.
        :param organization_id: Organization ID the snapshots belongs to.
        :param project_id: Project ID to list the snapshots of.
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
            f"/mongodb/v1/regions/{param_region}/snapshots",
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
        region: Optional[ScwRegion] = None,
        instance_id: Optional[str] = None,
        name: Optional[str] = None,
        order_by: Optional[ListSnapshotsRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Snapshot]:
        """
        List snapshots.
        List snapshots. You can include the `instance_id` or `project_id` in your query to get the list of snapshots for specific Database Instances and/or Projects. By default, the details returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param instance_id: Instance ID the snapshots belongs to.
        :param name: Lists database snapshots that match a name pattern.
        :param order_by: Criteria to use when ordering snapshot listings.
        :param organization_id: Organization ID the snapshots belongs to.
        :param project_id: Project ID to list the snapshots of.
        :param page:
        :param page_size:
        :return: :class:`list[Snapshot] <list[Snapshot]>`

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
                "instance_id": instance_id,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
            },
        )

    async def delete_snapshot(
        self,
        *,
        snapshot_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Snapshot:
        """
        Delete a Database Instance snapshot.
        Delete a given snapshot of a Database Instance. You must specify, in the endpoint, the `snapshot_id` parameter of the snapshot you want to delete.
        :param snapshot_id: UUID of the snapshot.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = await api.delete_snapshot(
                snapshot_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "DELETE",
            f"/mongodb/v1/regions/{param_region}/snapshots/{param_snapshot_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    async def list_users(
        self,
        *,
        instance_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        order_by: Optional[ListUsersRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListUsersResponse:
        """
        List users of a Database Instance.
        List all users of a given Database Instance.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the user.
        :param order_by: Criteria to use when requesting user listing.
        :param page:
        :param page_size:
        :return: :class:`ListUsersResponse <ListUsersResponse>`

        Usage:
        ::

            result = await api.list_users(
                instance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "GET",
            f"/mongodb/v1/regions/{param_region}/instances/{param_instance_id}/users",
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
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        order_by: Optional[ListUsersRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[User]:
        """
        List users of a Database Instance.
        List all users of a given Database Instance.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the user.
        :param order_by: Criteria to use when requesting user listing.
        :param page:
        :param page_size:
        :return: :class:`list[User] <list[User]>`

        Usage:
        ::

            result = await api.list_users_all(
                instance_id="example",
            )
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
        region: Optional[ScwRegion] = None,
    ) -> User:
        """
        Create an user on a Database Instance.
        Create an user on a Database Instance. You must define the `name`, `password` of the user and `instance_id` parameters in the request.
        :param instance_id: UUID of the Database Instance the user belongs to.
        :param name: Name of the database user.
        :param password: Password of the database user.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`User <User>`

        Usage:
        ::

            result = await api.create_user(
                instance_id="example",
                name="example",
                password="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "POST",
            f"/mongodb/v1/regions/{param_region}/instances/{param_instance_id}/users",
            body=marshal_CreateUserRequest(
                CreateUserRequest(
                    instance_id=instance_id,
                    name=name,
                    password=password,
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
        region: Optional[ScwRegion] = None,
        password: Optional[str] = None,
    ) -> User:
        """
        Update a user on a Database Instance.
        Update the parameters of a user on a Database Instance. You can update the `password` parameter, but you cannot change the name of the user.
        :param instance_id: UUID of the Database Instance the user belongs to.
        :param name: Name of the database user.
        :param region: Region to target. If none is passed will use default region from the config.
        :param password: Password of the database user.
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
            f"/mongodb/v1/regions/{param_region}/instances/{param_instance_id}/users/{param_name}",
            body=marshal_UpdateUserRequest(
                UpdateUserRequest(
                    instance_id=instance_id,
                    name=name,
                    region=region,
                    password=password,
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
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a user on a Database Instance.
        Delete an existing user on a Database Instance.
        :param instance_id: UUID of the Database Instance the user belongs to.
        :param name: Name of the database user.
        :param region: Region to target. If none is passed will use default region from the config.

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
            f"/mongodb/v1/regions/{param_region}/instances/{param_instance_id}/users/{param_name}",
        )

        self._throw_on_error(res)

    async def set_user_role(
        self,
        *,
        instance_id: str,
        user_name: str,
        region: Optional[ScwRegion] = None,
        roles: Optional[list[UserRole]] = None,
    ) -> User:
        """
        Apply user roles.
        Apply preset roles for a user in a Database Instance.
        :param instance_id: UUID of the Database Instance the user belongs to.
        :param user_name: Name of the database user.
        :param region: Region to target. If none is passed will use default region from the config.
        :param roles: List of roles assigned to the user, along with the corresponding database where each role is granted.
        :return: :class:`User <User>`

        Usage:
        ::

            result = await api.set_user_role(
                instance_id="example",
                user_name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "PUT",
            f"/mongodb/v1/regions/{param_region}/instances/{param_instance_id}/set-user-roles",
            body=marshal_SetUserRoleRequest(
                SetUserRoleRequest(
                    instance_id=instance_id,
                    user_name=user_name,
                    region=region,
                    roles=roles,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    async def list_databases(
        self,
        *,
        instance_id: str,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListDatabasesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListDatabasesResponse:
        """
        List databases in a Database Instance.
        List all databases of a given Database Instance.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Criteria to use when requesting user listing.
        :param page:
        :param page_size:
        :return: :class:`ListDatabasesResponse <ListDatabasesResponse>`

        Usage:
        ::

            result = await api.list_databases(
                instance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_instance_id = validate_path_param("instance_id", instance_id)

        res = self._request(
            "GET",
            f"/mongodb/v1/regions/{param_region}/instances/{param_instance_id}/databases",
            params={
                "order_by": order_by,
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
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListDatabasesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Database]:
        """
        List databases in a Database Instance.
        List all databases of a given Database Instance.
        :param instance_id: UUID of the Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Criteria to use when requesting user listing.
        :param page:
        :param page_size:
        :return: :class:`list[Database] <list[Database]>`

        Usage:
        ::

            result = await api.list_databases_all(
                instance_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListDatabasesResponse,
            key="databases",
            fetcher=self.list_databases,
            args={
                "instance_id": instance_id,
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    async def delete_endpoint(
        self,
        *,
        endpoint_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a Database Instance endpoint.
        Delete the endpoint of a Database Instance. You must specify the `endpoint_id` parameter of the endpoint you want to delete. Note that you might need to update any environment configurations that point to the deleted endpoint.
        :param endpoint_id: UUID of the Endpoint to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_endpoint(
                endpoint_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_endpoint_id = validate_path_param("endpoint_id", endpoint_id)

        res = self._request(
            "DELETE",
            f"/mongodb/v1/regions/{param_region}/endpoints/{param_endpoint_id}",
        )

        self._throw_on_error(res)

    async def create_endpoint(
        self,
        *,
        instance_id: str,
        endpoint: EndpointSpec,
        region: Optional[ScwRegion] = None,
    ) -> Endpoint:
        """
        Create a new Instance endpoint.
        Create a new endpoint for a MongoDB® Database Instance. You can add `public_network` or `private_network` specifications to the body of the request.
        :param instance_id: UUID of the Database Instance.
        :param endpoint: EndpointSpec used to expose your Database Instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Endpoint <Endpoint>`

        Usage:
        ::

            result = await api.create_endpoint(
                instance_id="example",
                endpoint=EndpointSpec(),
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/mongodb/v1/regions/{param_region}/endpoints",
            body=marshal_CreateEndpointRequest(
                CreateEndpointRequest(
                    instance_id=instance_id,
                    endpoint=endpoint,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Endpoint(res.json())

    async def list_maintenances(
        self,
        *,
        instance_id: str,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListMaintenancesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListMaintenancesResponse:
        """
        List all the maintenances of a MongoDB® Database Instance.
        :param instance_id: ID of the instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Criteria to use when requesting user listing.
        :param page:
        :param page_size:
        :return: :class:`ListMaintenancesResponse <ListMaintenancesResponse>`

        Usage:
        ::

            result = await api.list_maintenances(
                instance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/mongodb/v1/regions/{param_region}/maintenances",
            params={
                "instance_id": instance_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListMaintenancesResponse(res.json())

    async def list_maintenances_all(
        self,
        *,
        instance_id: str,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListMaintenancesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Maintenance]:
        """
        List all the maintenances of a MongoDB® Database Instance.
        :param instance_id: ID of the instance.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Criteria to use when requesting user listing.
        :param page:
        :param page_size:
        :return: :class:`list[Maintenance] <list[Maintenance]>`

        Usage:
        ::

            result = await api.list_maintenances_all(
                instance_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListMaintenancesResponse,
            key="maintenances",
            fetcher=self.list_maintenances,
            args={
                "instance_id": instance_id,
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    async def get_maintenance(
        self,
        *,
        maintenance_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Maintenance:
        """
        Get a maintenance of a MongoDB® Database Instance.
        :param maintenance_id: ID of the maintenance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Maintenance <Maintenance>`

        Usage:
        ::

            result = await api.get_maintenance(
                maintenance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_maintenance_id = validate_path_param("maintenance_id", maintenance_id)

        res = self._request(
            "GET",
            f"/mongodb/v1/regions/{param_region}/maintenances/{param_maintenance_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Maintenance(res.json())

    async def wait_for_maintenance(
        self,
        *,
        maintenance_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[
            WaitForOptions[Maintenance, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Maintenance:
        """
        Get a maintenance of a MongoDB® Database Instance.
        :param maintenance_id: ID of the maintenance.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Maintenance <Maintenance>`

        Usage:
        ::

            result = await api.get_maintenance(
                maintenance_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in MAINTENANCE_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_maintenance,
            options=options,
            args={
                "maintenance_id": maintenance_id,
                "region": region,
            },
        )

    async def apply_maintenance(
        self,
        *,
        maintenance_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Maintenance:
        """
        Apply a maintenance of a MongoDB® Database Instance.
        :param maintenance_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Maintenance <Maintenance>`

        Usage:
        ::

            result = await api.apply_maintenance(
                maintenance_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_maintenance_id = validate_path_param("maintenance_id", maintenance_id)

        res = self._request(
            "POST",
            f"/mongodb/v1/regions/{param_region}/maintenances/{param_maintenance_id}/apply",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Maintenance(res.json())
