# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    ListSnapshotsRequestOrderBy,
    ListVolumesRequestOrderBy,
    CreateSnapshotRequest,
    CreateVolumeRequest,
    CreateVolumeRequestFromEmpty,
    CreateVolumeRequestFromSnapshot,
    ExportSnapshotToObjectStorageRequest,
    ImportSnapshotFromObjectStorageRequest,
    ImportSnapshotFromS3Request,
    ListSnapshotsResponse,
    ListVolumeTypesResponse,
    ListVolumesResponse,
    Snapshot,
    UpdateSnapshotRequest,
    UpdateVolumeRequest,
    Volume,
    VolumeType,
)
from .content import (
    SNAPSHOT_TRANSIENT_STATUSES,
    VOLUME_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Snapshot,
    unmarshal_Volume,
    unmarshal_ListSnapshotsResponse,
    unmarshal_ListVolumeTypesResponse,
    unmarshal_ListVolumesResponse,
    marshal_CreateSnapshotRequest,
    marshal_CreateVolumeRequest,
    marshal_ExportSnapshotToObjectStorageRequest,
    marshal_ImportSnapshotFromObjectStorageRequest,
    marshal_ImportSnapshotFromS3Request,
    marshal_UpdateSnapshotRequest,
    marshal_UpdateVolumeRequest,
)


class BlockV1Alpha1API(API):
    """
    This API allows you to manage your Block Storage volumes.
    """

    def list_volume_types(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListVolumeTypesResponse:
        """
        List volume types.
        List all available volume types in a specified zone. The volume types listed are ordered by name in ascending order.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Page size, defines how many entries are returned in one page, must be lower or equal to 100.
        :return: :class:`ListVolumeTypesResponse <ListVolumeTypesResponse>`

        Usage:
        ::

            result = api.list_volume_types()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/block/v1alpha1/zones/{param_zone}/volume-types",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVolumeTypesResponse(res.json())

    def list_volume_types_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[VolumeType]:
        """
        List volume types.
        List all available volume types in a specified zone. The volume types listed are ordered by name in ascending order.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Page size, defines how many entries are returned in one page, must be lower or equal to 100.
        :return: :class:`List[VolumeType] <List[VolumeType]>`

        Usage:
        ::

            result = api.list_volume_types_all()
        """

        return fetch_all_pages(
            type=ListVolumeTypesResponse,
            key="volume_types",
            fetcher=self.list_volume_types,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
            },
        )

    def list_volumes(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListVolumesRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        product_resource_id: Optional[str] = None,
    ) -> ListVolumesResponse:
        """
        List volumes.
        List all existing volumes in a specified zone. By default, the volumes listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Criteria to use when ordering the list.
        :param project_id: Filter by Project ID.
        :param organization_id: Filter by Organization ID.
        :param page: Page number.
        :param page_size: Page size, defines how many entries are returned in one page, must be lower or equal to 100.
        :param name: Filter the return volumes by their names.
        :param product_resource_id: Filter by a product resource ID linked to this volume (such as an Instance ID).
        :return: :class:`ListVolumesResponse <ListVolumesResponse>`

        Usage:
        ::

            result = api.list_volumes()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/block/v1alpha1/zones/{param_zone}/volumes",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "product_resource_id": product_resource_id,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVolumesResponse(res.json())

    def list_volumes_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListVolumesRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        product_resource_id: Optional[str] = None,
    ) -> List[Volume]:
        """
        List volumes.
        List all existing volumes in a specified zone. By default, the volumes listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Criteria to use when ordering the list.
        :param project_id: Filter by Project ID.
        :param organization_id: Filter by Organization ID.
        :param page: Page number.
        :param page_size: Page size, defines how many entries are returned in one page, must be lower or equal to 100.
        :param name: Filter the return volumes by their names.
        :param product_resource_id: Filter by a product resource ID linked to this volume (such as an Instance ID).
        :return: :class:`List[Volume] <List[Volume]>`

        Usage:
        ::

            result = api.list_volumes_all()
        """

        return fetch_all_pages(
            type=ListVolumesResponse,
            key="volumes",
            fetcher=self.list_volumes,
            args={
                "zone": zone,
                "order_by": order_by,
                "project_id": project_id,
                "organization_id": organization_id,
                "page": page,
                "page_size": page_size,
                "name": name,
                "product_resource_id": product_resource_id,
            },
        )

    def create_volume(
        self,
        *,
        name: str,
        zone: Optional[Zone] = None,
        perf_iops: Optional[int] = None,
        project_id: Optional[str] = None,
        from_empty: Optional[CreateVolumeRequestFromEmpty] = None,
        from_snapshot: Optional[CreateVolumeRequestFromSnapshot] = None,
        tags: Optional[List[str]] = None,
    ) -> Volume:
        """
        Create a volume.
        To create a new volume from scratch, you must specify `from_empty` and the `size`.
        To create a volume from an existing snapshot, specify `from_snapshot` and the `snapshot_id` in the request payload instead, size is optional and can be specified if you need to extend the original size. The volume will take on the same volume class and underlying IOPS limitations as the original snapshot.
        :param name: Name of the volume.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param perf_iops: The maximum IO/s expected, according to the different options available in stock (`5000 | 15000`).
        One-Of ('requirements'): at most one of 'perf_iops' could be set.
        :param project_id: UUID of the project the volume belongs to.
        :param from_empty: Specify the size of the new volume if creating a new one from scratch.
        One-Of ('from'): at most one of 'from_empty', 'from_snapshot' could be set.
        :param from_snapshot: Specify the snapshot ID of the original snapshot.
        One-Of ('from'): at most one of 'from_empty', 'from_snapshot' could be set.
        :param tags: List of tags assigned to the volume.
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = api.create_volume(
                name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/block/v1alpha1/zones/{param_zone}/volumes",
            body=marshal_CreateVolumeRequest(
                CreateVolumeRequest(
                    name=name,
                    zone=zone,
                    project_id=project_id,
                    tags=tags,
                    from_empty=from_empty,
                    from_snapshot=from_snapshot,
                    perf_iops=perf_iops,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Volume(res.json())

    def get_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[Zone] = None,
    ) -> Volume:
        """
        Get a volume.
        Retrieve technical information about a specific volume. Details such as size, type, and status are returned in the response.
        :param volume_id: UUID of the volume.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = api.get_volume(
                volume_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "GET",
            f"/block/v1alpha1/zones/{param_zone}/volumes/{param_volume_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Volume(res.json())

    def wait_for_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[Volume, bool]] = None,
    ) -> Volume:
        """
        Get a volume.
        Retrieve technical information about a specific volume. Details such as size, type, and status are returned in the response.
        :param volume_id: UUID of the volume.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = api.get_volume(
                volume_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in VOLUME_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_volume,
            options=options,
            args={
                "volume_id": volume_id,
                "zone": zone,
            },
        )

    def delete_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a detached volume.
        You must specify the `volume_id` of the volume you want to delete. The volume must not be in the `in_use` status.
        :param volume_id: UUID of the volume.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_volume(
                volume_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "DELETE",
            f"/block/v1alpha1/zones/{param_zone}/volumes/{param_volume_id}",
        )

        self._throw_on_error(res)

    def update_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        size: Optional[int] = None,
        tags: Optional[List[str]] = None,
        perf_iops: Optional[int] = None,
    ) -> Volume:
        """
        Update a volume.
        Update the technical details of a volume, such as its name, tags, or its new size and `volume_type` (within the same Block Storage class).
        You can only resize a volume to a larger size. It is currently not possible to change your Block Storage Class.
        :param volume_id: UUID of the volume.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: When defined, is the new name of the volume.
        :param size: Size in bytes of the volume, with a granularity of 1 GB (10^9 bytes).
        Must be compliant with the minimum (1GB) and maximum (10TB) allowed size.
        :param tags: List of tags assigned to the volume.
        :param perf_iops: The selected value must be available for the volume's current storage class.
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = api.update_volume(
                volume_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "PATCH",
            f"/block/v1alpha1/zones/{param_zone}/volumes/{param_volume_id}",
            body=marshal_UpdateVolumeRequest(
                UpdateVolumeRequest(
                    volume_id=volume_id,
                    zone=zone,
                    name=name,
                    size=size,
                    tags=tags,
                    perf_iops=perf_iops,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Volume(res.json())

    def list_snapshots(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListSnapshotsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        volume_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ListSnapshotsResponse:
        """
        List all snapshots.
        List all available snapshots in a specified zone. By default, the snapshots listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Criteria to use when ordering the list.
        :param project_id: Filter by Project ID.
        :param organization_id: Filter by Organization ID.
        :param page: Page number.
        :param page_size: Page size, defines how many entries are returned in one page, must be lower or equal to 100.
        :param volume_id: Filter snapshots by the ID of the original volume.
        :param name: Filter snapshots by their names.
        :return: :class:`ListSnapshotsResponse <ListSnapshotsResponse>`

        Usage:
        ::

            result = api.list_snapshots()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/block/v1alpha1/zones/{param_zone}/snapshots",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "volume_id": volume_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSnapshotsResponse(res.json())

    def list_snapshots_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListSnapshotsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        volume_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> List[Snapshot]:
        """
        List all snapshots.
        List all available snapshots in a specified zone. By default, the snapshots listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Criteria to use when ordering the list.
        :param project_id: Filter by Project ID.
        :param organization_id: Filter by Organization ID.
        :param page: Page number.
        :param page_size: Page size, defines how many entries are returned in one page, must be lower or equal to 100.
        :param volume_id: Filter snapshots by the ID of the original volume.
        :param name: Filter snapshots by their names.
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
                "zone": zone,
                "order_by": order_by,
                "project_id": project_id,
                "organization_id": organization_id,
                "page": page,
                "page_size": page_size,
                "volume_id": volume_id,
                "name": name,
            },
        )

    def get_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[Zone] = None,
    ) -> Snapshot:
        """
        Get a snapshot.
        Retrieve technical information about a specific snapshot. Details such as size, volume type, and status are returned in the response.
        :param snapshot_id: UUID of the snapshot.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.get_snapshot(
                snapshot_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "GET",
            f"/block/v1alpha1/zones/{param_zone}/snapshots/{param_snapshot_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    def wait_for_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[Snapshot, bool]] = None,
    ) -> Snapshot:
        """
        Get a snapshot.
        Retrieve technical information about a specific snapshot. Details such as size, volume type, and status are returned in the response.
        :param snapshot_id: UUID of the snapshot.
        :param zone: Zone to target. If none is passed will use default zone from the config.
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
                "zone": zone,
            },
        )

    def create_snapshot(
        self,
        *,
        volume_id: str,
        name: str,
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Snapshot:
        """
        Create a snapshot of a volume.
        To create a snapshot, the volume must be in the `in_use` or the `available` status.
        If your volume is in a transient state, you need to wait until the end of the current operation.
        :param volume_id: UUID of the volume to snapshot.
        :param name: Name of the snapshot.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: UUID of the project to which the volume and the snapshot belong.
        :param tags: List of tags assigned to the snapshot.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.create_snapshot(
                volume_id="example",
                name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/block/v1alpha1/zones/{param_zone}/snapshots",
            body=marshal_CreateSnapshotRequest(
                CreateSnapshotRequest(
                    volume_id=volume_id,
                    name=name,
                    zone=zone,
                    project_id=project_id,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    def import_snapshot_from_s3(
        self,
        *,
        bucket: str,
        key: str,
        name: str,
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        size: Optional[int] = None,
    ) -> Snapshot:
        """
        (Deprecated in favor of `ImportSnapshotFromObjectStorage`).
        Import a snapshot from a Scaleway Object Storage bucket
        The bucket must contain a QCOW2 image.
        The bucket can be imported into any Availability Zone as long as it is in the same region as the bucket.
        :param bucket: Scaleway Object Storage bucket where the object is stored.
        :param key: The object key inside the given bucket.
        :param name: Name of the snapshot.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: UUID of the Project to which the volume and the snapshot belong.
        :param tags: List of tags assigned to the snapshot.
        :param size: Size of the snapshot.
        :return: :class:`Snapshot <Snapshot>`
        :deprecated

        Usage:
        ::

            result = api.import_snapshot_from_s3(
                bucket="example",
                key="example",
                name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/block/v1alpha1/zones/{param_zone}/snapshots/import-from-s3",
            body=marshal_ImportSnapshotFromS3Request(
                ImportSnapshotFromS3Request(
                    bucket=bucket,
                    key=key,
                    name=name,
                    zone=zone,
                    project_id=project_id,
                    tags=tags,
                    size=size,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    def import_snapshot_from_object_storage(
        self,
        *,
        bucket: str,
        key: str,
        name: str,
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        size: Optional[int] = None,
    ) -> Snapshot:
        """
        Import a snapshot from a Scaleway Object Storage bucket.
        The bucket must contain a QCOW2 image.
        The bucket can be imported into any Availability Zone as long as it is in the same region as the bucket.
        :param bucket: Scaleway Object Storage bucket where the object is stored.
        :param key: The object key inside the given bucket.
        :param name: Name of the snapshot.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: UUID of the Project to which the volume and the snapshot belong.
        :param tags: List of tags assigned to the snapshot.
        :param size: Size of the snapshot.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.import_snapshot_from_object_storage(
                bucket="example",
                key="example",
                name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/block/v1alpha1/zones/{param_zone}/snapshots/import-from-object-storage",
            body=marshal_ImportSnapshotFromObjectStorageRequest(
                ImportSnapshotFromObjectStorageRequest(
                    bucket=bucket,
                    key=key,
                    name=name,
                    zone=zone,
                    project_id=project_id,
                    tags=tags,
                    size=size,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    def export_snapshot_to_object_storage(
        self,
        *,
        snapshot_id: str,
        bucket: str,
        key: str,
        zone: Optional[Zone] = None,
    ) -> Snapshot:
        """
        Export a snapshot to a Scaleway Object Storage bucket.
        The snapshot is exported in QCOW2 format.
        The snapshot must not be in transient state.
        :param snapshot_id: UUID of the snapshot.
        :param bucket: Scaleway Object Storage bucket where the object is stored.
        :param key: The object key inside the given bucket.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.export_snapshot_to_object_storage(
                snapshot_id="example",
                bucket="example",
                key="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "POST",
            f"/block/v1alpha1/zones/{param_zone}/snapshots/{param_snapshot_id}/export-to-object-storage",
            body=marshal_ExportSnapshotToObjectStorageRequest(
                ExportSnapshotToObjectStorageRequest(
                    snapshot_id=snapshot_id,
                    bucket=bucket,
                    key=key,
                    zone=zone,
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
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a snapshot.
        You must specify the `snapshot_id` of the snapshot you want to delete. The snapshot must not be in use.
        :param snapshot_id: UUID of the snapshot.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_snapshot(
                snapshot_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "DELETE",
            f"/block/v1alpha1/zones/{param_zone}/snapshots/{param_snapshot_id}",
        )

        self._throw_on_error(res)

    def update_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Snapshot:
        """
        Update a snapshot.
        Update the name or tags of the snapshot.
        :param snapshot_id: UUID of the snapshot.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: When defined, is the name of the snapshot.
        :param tags: List of tags assigned to the snapshot.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.update_snapshot(
                snapshot_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "PATCH",
            f"/block/v1alpha1/zones/{param_zone}/snapshots/{param_snapshot_id}",
            body=marshal_UpdateSnapshotRequest(
                UpdateSnapshotRequest(
                    snapshot_id=snapshot_id,
                    zone=zone,
                    name=name,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())
