# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    random_name,
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    ListProjectsRequestOrderBy,
    CreateProjectRequest,
    ListProjectsResponse,
    Project,
    UpdateProjectRequest,
)
from .marshalling import (
    unmarshal_Project,
    unmarshal_ListProjectsResponse,
    marshal_CreateProjectRequest,
    marshal_UpdateProjectRequest,
)


class AccountV2API(API):
    """
    This API allows you to manage your Scaleway Projects.
    """

    async def create_project(
        self,
        *,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Project:
        """
        Create a new Project for an Organization.
        Deprecated in favor of Account API v3.
        Generate a new Project for an Organization, specifying its configuration including name and description.
        :param name: Name of the Project.
        :param organization_id: Organization ID of the Project.
        :param description: Description of the Project.
        :return: :class:`Project <Project>`
        :deprecated

        Usage:
        ::

            result = await api.create_project()
        """

        res = self._request(
            "POST",
            "/account/v2/projects",
            body=marshal_CreateProjectRequest(
                CreateProjectRequest(
                    name=name or random_name(prefix="proj"),
                    organization_id=organization_id,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Project(res.json())

    async def list_projects(
        self,
        *,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListProjectsRequestOrderBy] = None,
        project_ids: Optional[List[str]] = None,
    ) -> ListProjectsResponse:
        """
        List all Projects of an Organization.
        Deprecated in favor of Account API v3.
        List all Projects of an Organization. The response will include the total number of Projects as well as their associated Organizations, names and IDs. Other information include the creation and update date of the Project.
        :param organization_id: Organization ID of the Project.
        :param name: Name of the Project.
        :param page: Page number for the returned Projects.
        :param page_size: Maximum number of Project per page.
        :param order_by: Sort order of the returned Projects.
        :param project_ids: Project IDs to filter for. The results will be limited to any Projects with an ID in this array.
        :return: :class:`ListProjectsResponse <ListProjectsResponse>`
        :deprecated

        Usage:
        ::

            result = await api.list_projects()
        """

        res = self._request(
            "GET",
            "/account/v2/projects",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_ids": project_ids,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListProjectsResponse(res.json())

    async def list_projects_all(
        self,
        *,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListProjectsRequestOrderBy] = None,
        project_ids: Optional[List[str]] = None,
    ) -> List[Project]:
        """
        List all Projects of an Organization.
        Deprecated in favor of Account API v3.
        List all Projects of an Organization. The response will include the total number of Projects as well as their associated Organizations, names and IDs. Other information include the creation and update date of the Project.
        :param organization_id: Organization ID of the Project.
        :param name: Name of the Project.
        :param page: Page number for the returned Projects.
        :param page_size: Maximum number of Project per page.
        :param order_by: Sort order of the returned Projects.
        :param project_ids: Project IDs to filter for. The results will be limited to any Projects with an ID in this array.
        :return: :class:`List[Project] <List[Project]>`
        :deprecated

        Usage:
        ::

            result = await api.list_projects_all()
        """

        return await fetch_all_pages_async(
            type=ListProjectsResponse,
            key="projects",
            fetcher=self.list_projects,
            args={
                "organization_id": organization_id,
                "name": name,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_ids": project_ids,
            },
        )

    async def get_project(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Project:
        """
        Get an existing Project.
        Deprecated in favor of Account API v3.
        Retrieve information about an existing Project, specified by its Project ID. Its full details, including ID, name and description, are returned in the response object.
        :param project_id: Project ID of the Project.
        :return: :class:`Project <Project>`
        :deprecated

        Usage:
        ::

            result = await api.get_project()
        """

        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "GET",
            f"/account/v2/projects/{param_project_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Project(res.json())

    async def delete_project(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> None:
        """
        Delete an existing Project.
        Deprecated in favor of Account API v3.
        Delete an existing Project, specified by its Project ID. The Project needs to be empty (meaning there are no resources left in it) to be deleted effectively. Note that deleting a Project is permanent, and cannot be undone.
        :param project_id: Project ID of the Project.
        :deprecated

        Usage:
        ::

            result = await api.delete_project()
        """

        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "DELETE",
            f"/account/v2/projects/{param_project_id}",
        )

        self._throw_on_error(res)

    async def update_project(
        self,
        *,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Project:
        """
        Update Project.
        Deprecated in favor of Account API v3.
        Update the parameters of an existing Project, specified by its Project ID. These parameters include the name and description.
        :param project_id: Project ID of the Project.
        :param name: Name of the Project.
        :param description: Description of the Project.
        :return: :class:`Project <Project>`
        :deprecated

        Usage:
        ::

            result = await api.update_project()
        """

        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "PATCH",
            f"/account/v2/projects/{param_project_id}",
            body=marshal_UpdateProjectRequest(
                UpdateProjectRequest(
                    project_id=project_id,
                    name=name,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Project(res.json())
