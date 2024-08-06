# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    WaitForOptions,
    random_name,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    ListServersRequestOrderBy,
    CreateServerRequest,
    ListOSResponse,
    ListServerTypesResponse,
    ListServersResponse,
    OS,
    ReinstallServerRequest,
    Server,
    ServerType,
    UpdateServerRequest,
)
from .content import (
    SERVER_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_OS,
    unmarshal_ServerType,
    unmarshal_Server,
    unmarshal_ListOSResponse,
    unmarshal_ListServerTypesResponse,
    unmarshal_ListServersResponse,
    marshal_CreateServerRequest,
    marshal_ReinstallServerRequest,
    marshal_UpdateServerRequest,
)


class ApplesiliconV1Alpha1API(API):
    """
    This API allows you to manage your Apple silicon machines.
    """

    async def list_server_types(
        self,
        *,
        zone: Optional[Zone] = None,
    ) -> ListServerTypesResponse:
        """
        List server types.
        List all technical details about Apple silicon server types available in the specified zone. Since there is only one Availability Zone for Apple silicon servers, the targeted value is `fr-par-3`.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ListServerTypesResponse <ListServerTypesResponse>`

        Usage:
        ::

            result = await api.list_server_types()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/server-types",
        )

        self._throw_on_error(res)
        return unmarshal_ListServerTypesResponse(res.json())

    async def get_server_type(
        self,
        *,
        server_type: str,
        zone: Optional[Zone] = None,
    ) -> ServerType:
        """
        Get a server type.
        Get technical details (CPU, disk size etc.) of a server type.
        :param server_type: Server type identifier.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ServerType <ServerType>`

        Usage:
        ::

            result = await api.get_server_type(
                server_type="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_type = validate_path_param("server_type", server_type)

        res = self._request(
            "GET",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/server-type/{param_server_type}",
        )

        self._throw_on_error(res)
        return unmarshal_ServerType(res.json())

    async def create_server(
        self,
        *,
        type_: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        os_id: Optional[str] = None,
    ) -> Server:
        """
        Create a server.
        Create a new server in the targeted zone, specifying its configuration including name and type.
        :param type_: Create a server of the given type.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Create a server with this given name.
        :param project_id: Create a server in the given project ID.
        :param os_id: Create a server & install the given os_id, when no os_id provided the default OS for this server type is chosen. Requesting a non-default OS will induce an extended delivery time.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.create_server(
                type="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/servers",
            body=marshal_CreateServerRequest(
                CreateServerRequest(
                    type_=type_,
                    zone=zone,
                    name=name or random_name(prefix="as"),
                    project_id=project_id,
                    os_id=os_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def list_servers(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListServersRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListServersResponse:
        """
        List all servers.
        List all servers in the specified zone. By default, returned servers in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of the returned servers.
        :param project_id: Only list servers of this project ID.
        :param organization_id: Only list servers of this Organization ID.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :return: :class:`ListServersResponse <ListServersResponse>`

        Usage:
        ::

            result = await api.list_servers()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/servers",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServersResponse(res.json())

    async def list_servers_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListServersRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Server]:
        """
        List all servers.
        List all servers in the specified zone. By default, returned servers in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of the returned servers.
        :param project_id: Only list servers of this project ID.
        :param organization_id: Only list servers of this Organization ID.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :return: :class:`List[Server] <List[Server]>`

        Usage:
        ::

            result = await api.list_servers_all()
        """

        return await fetch_all_pages_async(
            type=ListServersResponse,
            key="servers",
            fetcher=self.list_servers,
            args={
                "zone": zone,
                "order_by": order_by,
                "project_id": project_id,
                "organization_id": organization_id,
                "page": page,
                "page_size": page_size,
            },
        )

    async def list_os(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        server_type: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ListOSResponse:
        """
        List all Operating Systems (OS).
        List all Operating Systems (OS). The response will include the total number of OS as well as their associated IDs, names and labels.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param server_type: List of compatible server types.
        :param name: Filter OS by name (note that "11.1" will return "11.1.2" and "11.1" but not "12")).
        :return: :class:`ListOSResponse <ListOSResponse>`

        Usage:
        ::

            result = await api.list_os()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/os",
            params={
                "name": name,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "server_type": server_type,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOSResponse(res.json())

    async def list_os_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        server_type: Optional[str] = None,
        name: Optional[str] = None,
    ) -> List[OS]:
        """
        List all Operating Systems (OS).
        List all Operating Systems (OS). The response will include the total number of OS as well as their associated IDs, names and labels.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param server_type: List of compatible server types.
        :param name: Filter OS by name (note that "11.1" will return "11.1.2" and "11.1" but not "12")).
        :return: :class:`List[OS] <List[OS]>`

        Usage:
        ::

            result = await api.list_os_all()
        """

        return await fetch_all_pages_async(
            type=ListOSResponse,
            key="os",
            fetcher=self.list_os,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "server_type": server_type,
                "name": name,
            },
        )

    async def get_os(
        self,
        *,
        os_id: str,
        zone: Optional[Zone] = None,
    ) -> OS:
        """
        Get an Operating System (OS).
        Get an Operating System (OS).  The response will include the OS's unique ID as well as its name and label.
        :param os_id: UUID of the OS you want to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`OS <OS>`

        Usage:
        ::

            result = await api.get_os(
                os_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_os_id = validate_path_param("os_id", os_id)

        res = self._request(
            "GET",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/os/{param_os_id}",
        )

        self._throw_on_error(res)
        return unmarshal_OS(res.json())

    async def get_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Get a server.
        Retrieve information about an existing Apple silicon server, specified by its server ID. Its full details, including name, status and IP address, are returned in the response object.
        :param server_id: UUID of the server you want to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.get_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/servers/{param_server_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def wait_for_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[Server, Union[bool, Awaitable[bool]]]] = None,
    ) -> Server:
        """
        Get a server.
        Retrieve information about an existing Apple silicon server, specified by its server ID. Its full details, including name, status and IP address, are returned in the response object.
        :param server_id: UUID of the server you want to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.get_server(
                server_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in SERVER_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_server,
            options=options,
            args={
                "server_id": server_id,
                "zone": zone,
            },
        )

    async def update_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        schedule_deletion: Optional[bool] = None,
    ) -> Server:
        """
        Update a server.
        Update the parameters of an existing Apple silicon server, specified by its server ID.
        :param server_id: UUID of the server you want to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Updated name for your server.
        :param schedule_deletion: Specify whether the server should be flagged for automatic deletion.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.update_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "PATCH",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/servers/{param_server_id}",
            body=marshal_UpdateServerRequest(
                UpdateServerRequest(
                    server_id=server_id,
                    zone=zone,
                    name=name,
                    schedule_deletion=schedule_deletion,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def delete_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a server.
        Delete an existing Apple silicon server, specified by its server ID. Deleting a server is permanent, and cannot be undone. Note that the minimum allocation period for Apple silicon-as-a-service is 24 hours, meaning you cannot delete your server prior to that.
        :param server_id: UUID of the server you want to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "DELETE",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/servers/{param_server_id}",
        )

        self._throw_on_error(res)

    async def reboot_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Reboot a server.
        Reboot an existing Apple silicon server, specified by its server ID.
        :param server_id: UUID of the server you want to reboot.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.reboot_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/servers/{param_server_id}/reboot",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def reinstall_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        os_id: Optional[str] = None,
    ) -> Server:
        """
        Reinstall a server.
        Reinstall an existing Apple silicon server (specified by its server ID) from a new image (OS). All the data on the disk is deleted and all configuration is reset to the defailt configuration values of the image (OS).
        :param server_id: UUID of the server you want to reinstall.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param os_id: Reinstall the server with the target OS, when no os_id provided the default OS for the server type is used.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.reinstall_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/servers/{param_server_id}/reinstall",
            body=marshal_ReinstallServerRequest(
                ReinstallServerRequest(
                    server_id=server_id,
                    zone=zone,
                    os_id=os_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())
