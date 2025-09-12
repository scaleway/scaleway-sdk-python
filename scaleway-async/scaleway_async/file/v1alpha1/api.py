# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
    Zone as ScwZone,
)
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    AttachmentResourceType,
    ListFileSystemsRequestOrderBy,
    Attachment,
    CreateFileSystemRequest,
    FileSystem,
    ListAttachmentsResponse,
    ListFileSystemsResponse,
    UpdateFileSystemRequest,
)
from .content import (
    FILE_SYSTEM_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_FileSystem,
    unmarshal_ListAttachmentsResponse,
    unmarshal_ListFileSystemsResponse,
    marshal_CreateFileSystemRequest,
    marshal_UpdateFileSystemRequest,
)


class FileV1Alpha1API(API):
    """
    This API allows you to manage your File Storage resources.
    """

    async def get_file_system(
        self,
        *,
        filesystem_id: str,
        region: Optional[ScwRegion] = None,
    ) -> FileSystem:
        """
        Get filesystem details.
        Retrieve all properties and current status of a specific filesystem identified by its ID.
        :param filesystem_id: UUID of the filesystem.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`FileSystem <FileSystem>`

        Usage:
        ::

            result = await api.get_file_system(
                filesystem_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_filesystem_id = validate_path_param("filesystem_id", filesystem_id)

        res = self._request(
            "GET",
            f"/file/v1alpha1/regions/{param_region}/filesystems/{param_filesystem_id}",
        )

        self._throw_on_error(res)
        return unmarshal_FileSystem(res.json())

    async def wait_for_file_system(
        self,
        *,
        filesystem_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[
            WaitForOptions[FileSystem, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> FileSystem:
        """
        Get filesystem details.
        Retrieve all properties and current status of a specific filesystem identified by its ID.
        :param filesystem_id: UUID of the filesystem.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`FileSystem <FileSystem>`

        Usage:
        ::

            result = await api.get_file_system(
                filesystem_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in FILE_SYSTEM_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_file_system,
            options=options,
            args={
                "filesystem_id": filesystem_id,
                "region": region,
            },
        )

    async def list_file_systems(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListFileSystemsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> ListFileSystemsResponse:
        """
        List all filesystems.
        Retrieve all filesystems in the specified region. By default, the filesystems listed are ordered by creation date in ascending order. This can be modified using the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Criteria to use when ordering the list.
        :param project_id: Filter by project ID.
        :param organization_id: Filter by organization ID.
        :param page: Page number (starting at 1).
        :param page_size: Number of entries per page (default: 20, max: 100).
        :param name: Filter the returned filesystems by their names.
        :param tags: Filter by tags. Only filesystems with one or more matching tags will be returned.
        :return: :class:`ListFileSystemsResponse <ListFileSystemsResponse>`

        Usage:
        ::

            result = await api.list_file_systems()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/file/v1alpha1/regions/{param_region}/filesystems",
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
        return unmarshal_ListFileSystemsResponse(res.json())

    async def list_file_systems_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListFileSystemsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> list[FileSystem]:
        """
        List all filesystems.
        Retrieve all filesystems in the specified region. By default, the filesystems listed are ordered by creation date in ascending order. This can be modified using the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Criteria to use when ordering the list.
        :param project_id: Filter by project ID.
        :param organization_id: Filter by organization ID.
        :param page: Page number (starting at 1).
        :param page_size: Number of entries per page (default: 20, max: 100).
        :param name: Filter the returned filesystems by their names.
        :param tags: Filter by tags. Only filesystems with one or more matching tags will be returned.
        :return: :class:`list[FileSystem] <list[FileSystem]>`

        Usage:
        ::

            result = await api.list_file_systems_all()
        """

        return await fetch_all_pages_async(
            type=ListFileSystemsResponse,
            key="filesystems",
            fetcher=self.list_file_systems,
            args={
                "region": region,
                "order_by": order_by,
                "project_id": project_id,
                "organization_id": organization_id,
                "page": page,
                "page_size": page_size,
                "name": name,
                "tags": tags,
            },
        )

    async def list_attachments(
        self,
        *,
        region: Optional[ScwRegion] = None,
        filesystem_id: Optional[str] = None,
        resource_id: Optional[str] = None,
        resource_type: Optional[AttachmentResourceType] = None,
        zone: Optional[ScwZone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListAttachmentsResponse:
        """
        List filesystems attachments.
        List all existing attachments in a specified region.
        By default, the attachments listed are ordered by creation date in ascending order. This can be modified using the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param filesystem_id: UUID of the File Storage volume.
        :param resource_id: Filter by resource ID.
        :param resource_type: Filter by resource type.
        :param zone: Filter by resource zone.
        :param page: Page number (starting at 1).
        :param page_size: Number of entries per page (default: 20, max: 100).
        :return: :class:`ListAttachmentsResponse <ListAttachmentsResponse>`

        Usage:
        ::

            result = await api.list_attachments()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/file/v1alpha1/regions/{param_region}/attachments",
            params={
                "filesystem_id": filesystem_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "resource_id": resource_id,
                "resource_type": resource_type,
                "zone": zone or self.client.default_zone,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListAttachmentsResponse(res.json())

    async def list_attachments_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        filesystem_id: Optional[str] = None,
        resource_id: Optional[str] = None,
        resource_type: Optional[AttachmentResourceType] = None,
        zone: Optional[ScwZone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Attachment]:
        """
        List filesystems attachments.
        List all existing attachments in a specified region.
        By default, the attachments listed are ordered by creation date in ascending order. This can be modified using the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param filesystem_id: UUID of the File Storage volume.
        :param resource_id: Filter by resource ID.
        :param resource_type: Filter by resource type.
        :param zone: Filter by resource zone.
        :param page: Page number (starting at 1).
        :param page_size: Number of entries per page (default: 20, max: 100).
        :return: :class:`list[Attachment] <list[Attachment]>`

        Usage:
        ::

            result = await api.list_attachments_all()
        """

        return await fetch_all_pages_async(
            type=ListAttachmentsResponse,
            key="attachments",
            fetcher=self.list_attachments,
            args={
                "region": region,
                "filesystem_id": filesystem_id,
                "resource_id": resource_id,
                "resource_type": resource_type,
                "zone": zone,
                "page": page,
                "page_size": page_size,
            },
        )

    async def create_file_system(
        self,
        *,
        name: str,
        size: int,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> FileSystem:
        """
        Create a new filesystem.
        To create a new filesystem, you must specify a name, a size, and a project ID.
        :param name: Name of the filesystem.
        :param size: Must be compliant with the minimum (100 GB) and maximum (10 TB) allowed size.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: UUID of the project the filesystem belongs to.
        :param tags: List of tags assigned to the filesystem.
        :return: :class:`FileSystem <FileSystem>`

        Usage:
        ::

            result = await api.create_file_system(
                name="example",
                size=1,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/file/v1alpha1/regions/{param_region}/filesystems",
            body=marshal_CreateFileSystemRequest(
                CreateFileSystemRequest(
                    name=name,
                    size=size,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_FileSystem(res.json())

    async def delete_file_system(
        self,
        *,
        filesystem_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a detached filesystem.
        You must specify the `filesystem_id` of the filesystem you want to delete.
        :param filesystem_id: UUID of the filesystem.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_file_system(
                filesystem_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_filesystem_id = validate_path_param("filesystem_id", filesystem_id)

        res = self._request(
            "DELETE",
            f"/file/v1alpha1/regions/{param_region}/filesystems/{param_filesystem_id}",
        )

        self._throw_on_error(res)

    async def update_file_system(
        self,
        *,
        filesystem_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        size: Optional[int] = None,
        tags: Optional[list[str]] = None,
    ) -> FileSystem:
        """
        Update filesystem properties.
        Update the technical details of a filesystem, such as its name, tags or its new size.
        :param filesystem_id: UUID of the filesystem.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: When defined, is the new name of the filesystem.
        :param size: Size in bytes, with a granularity of 100 GB (10^11 bytes).
        Must be compliant with the minimum (100 GB) and maximum (10 TB) allowed size.
        :param tags: List of tags assigned to the filesystem.
        :return: :class:`FileSystem <FileSystem>`

        Usage:
        ::

            result = await api.update_file_system(
                filesystem_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_filesystem_id = validate_path_param("filesystem_id", filesystem_id)

        res = self._request(
            "PATCH",
            f"/file/v1alpha1/regions/{param_region}/filesystems/{param_filesystem_id}",
            body=marshal_UpdateFileSystemRequest(
                UpdateFileSystemRequest(
                    filesystem_id=filesystem_id,
                    region=region,
                    name=name,
                    size=size,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_FileSystem(res.json())
