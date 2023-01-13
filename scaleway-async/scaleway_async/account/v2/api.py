# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    fetch_all_pages_async,
    validate_path_param,
)
from .types import (
    ListProjectsRequestOrderBy,
    ListProjectsResponse,
    Project,
    CreateProjectRequest,
    UpdateProjectRequest,
)
from .marshalling import (
    marshal_CreateProjectRequest,
    marshal_UpdateProjectRequest,
    unmarshal_Project,
    unmarshal_ListProjectsResponse,
)


class AccountV2API(API):
    """
    Account API.

    This API allows you to manage projects.
    """

    async def create_project(
        self,
        *,
        name: str,
        organization_id: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Project:
        """
        Create project
        :param name: The name of the project
        :param organization_id: The organization ID of the project
        :param description: The description of the project
        :return: :class:`Project <Project>`

        Usage:
        ::

            result = await api.create_project(name="example")
        """

        res = self._request(
            "POST",
            f"/account/v2/projects",
            body=marshal_CreateProjectRequest(
                CreateProjectRequest(
                    name=name,
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
        order_by: ListProjectsRequestOrderBy = ListProjectsRequestOrderBy.CREATED_AT_ASC,
        project_ids: Optional[List[str]] = None,
    ) -> ListProjectsResponse:
        """
        List projects
        :param organization_id: The organization ID of the project
        :param name: The name of the project
        :param page: The page number for the returned projects
        :param page_size: The maximum number of project per page
        :param order_by: The sort order of the returned projects
        :param project_ids: Filter out by a list of project ID
        :return: :class:`ListProjectsResponse <ListProjectsResponse>`

        Usage:
        ::

            result = await api.list_projects()
        """

        res = self._request(
            "GET",
            f"/account/v2/projects",
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
        List projects
        :param organization_id: The organization ID of the project
        :param name: The name of the project
        :param page: The page number for the returned projects
        :param page_size: The maximum number of project per page
        :param order_by: The sort order of the returned projects
        :param project_ids: Filter out by a list of project ID
        :return: :class:`List[ListProjectsResponse] <List[ListProjectsResponse]>`

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
        Get project
        :param project_id: The project ID of the project
        :return: :class:`Project <Project>`

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
    ) -> Optional[None]:
        """
        Delete project
        :param project_id: The project ID of the project

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
        return None

    async def update_project(
        self,
        *,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Project:
        """
        Update project
        :param project_id: The project ID of the project
        :param name: The name of the project
        :param description: The description of the project
        :return: :class:`Project <Project>`

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
