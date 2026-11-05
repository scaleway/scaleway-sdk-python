# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, Optional, Union

from scaleway_core.api import API
from scaleway_core.utils import (
    OneOfPossibility,
    WaitForOptions,
    resolve_one_of,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    ManageServerPowerRequestAction,
    ListLocationsResponse,
    ListOSResponse,
    ListOffersResponse,
    ListServersResponse,
    Location,
    OS,
    Offer,
    Server,
    VpsApiChangeServerHostnameRequest,
    VpsApiChangeServerPasswordRequest,
    VpsApiCreateServerRequest,
    VpsApiManageServerPowerRequest,
    VpsApiReinstallServerRequest,
)
from .content import (
    SERVER_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Offer,
    unmarshal_Server,
    unmarshal_ListLocationsResponse,
    unmarshal_ListOSResponse,
    unmarshal_ListOffersResponse,
    unmarshal_ListServersResponse,
    marshal_VpsApiChangeServerHostnameRequest,
    marshal_VpsApiChangeServerPasswordRequest,
    marshal_VpsApiCreateServerRequest,
    marshal_VpsApiManageServerPowerRequest,
    marshal_VpsApiReinstallServerRequest,
)


class DediboxV1VpsAPI(API):
    """
    Virtual private server API.
    """

    async def list_servers(
        self,
        *,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListServersResponse:
        """
        List VPS for project.
        :param organization_id: Organization ID.
        One-Of ('scope'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Project ID.
        One-Of ('scope'): at most one of 'organization_id', 'project_id' could be set.
        :param page: Page number.
        :param page_size: Number of servers per page.
        :return: :class:`ListServersResponse <ListServersResponse>`

        Usage:
        ::

            result = await api.list_servers()
        """

        res = self._request(
            "GET",
            "/vps/v1/servers",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                **resolve_one_of(
                    [
                        OneOfPossibility("organization_id", organization_id),
                        OneOfPossibility("project_id", project_id),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServersResponse(res.json())

    async def list_servers_all(
        self,
        *,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Server]:
        """
        List VPS for project.
        :param organization_id: Organization ID.
        One-Of ('scope'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Project ID.
        One-Of ('scope'): at most one of 'organization_id', 'project_id' could be set.
        :param page: Page number.
        :param page_size: Number of servers per page.
        :return: :class:`list[Server] <list[Server]>`

        Usage:
        ::

            result = await api.list_servers_all()
        """

        return await fetch_all_pages_async(
            type=ListServersResponse,
            key="servers",
            fetcher=self.list_servers,
            args={
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    async def get_server(
        self,
        *,
        server_id: str,
    ) -> Server:
        """
        Get a specific VPS.
        Get the VPS associated with the given ID.
        :param server_id: ID of the server.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.get_server(
                server_id="example",
            )
        """

        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/vps/v1/servers/{param_server_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def wait_for_server(
        self,
        *,
        server_id: str,
        options: Optional[WaitForOptions[Server, Union[bool, Awaitable[bool]]]] = None,
    ) -> Server:
        """
        Get a specific VPS.
        Get the VPS associated with the given ID.
        :param server_id: ID of the server.
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
            },
        )

    async def create_server(
        self,
        *,
        offer_id: str,
        os_id: str,
        location_id: str,
        hostname: str,
        project_id: Optional[str] = None,
        ssh_key_id: Optional[str] = None,
    ) -> Server:
        """
        Create a VPS.
        Create a new VPS. The order return you a service ID to follow the provisioning status with GetServer.
        :param offer_id: Offer ID of the server.
        :param os_id: OS ID to install on the server.
        :param location_id: Location ID of the server.
        :param hostname: Hostname of the server.
        :param project_id: Project ID.
        :param ssh_key_id: SSH key to install on the server.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.create_server(
                offer_id="example",
                os_id="example",
                location_id="example",
                hostname="example",
            )
        """

        res = self._request(
            "POST",
            "/vps/v1/servers",
            body=marshal_VpsApiCreateServerRequest(
                VpsApiCreateServerRequest(
                    offer_id=offer_id,
                    os_id=os_id,
                    location_id=location_id,
                    hostname=hostname,
                    project_id=project_id,
                    ssh_key_id=ssh_key_id,
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
    ) -> Server:
        """
        Delete a VPS.
        Delete the VPS associated with the given ID.
        :param server_id: ID of the server to delete.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.delete_server(
                server_id="example",
            )
        """

        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "DELETE",
            f"/vps/v1/servers/{param_server_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def change_server_hostname(
        self,
        *,
        server_id: str,
        hostname: str,
    ) -> Server:
        """
        Change VPS hostname.
        Change a VPS's hostname.
        :param server_id: ID of the server.
        :param hostname: New hostname of the server.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.change_server_hostname(
                server_id="example",
                hostname="example",
            )
        """

        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/vps/v1/servers/{param_server_id}/change-hostname",
            body=marshal_VpsApiChangeServerHostnameRequest(
                VpsApiChangeServerHostnameRequest(
                    server_id=server_id,
                    hostname=hostname,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def change_server_password(
        self,
        *,
        server_id: str,
        password: str,
    ) -> Server:
        """
        Change VPS password.
        Change a VPS's root password.
        :param server_id: ID of the server.
        :param password: New root password of the server.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.change_server_password(
                server_id="example",
                password="example",
            )
        """

        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/vps/v1/servers/{param_server_id}/change-password",
            body=marshal_VpsApiChangeServerPasswordRequest(
                VpsApiChangeServerPasswordRequest(
                    server_id=server_id,
                    password=password,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def manage_server_power(
        self,
        *,
        server_id: str,
        action: ManageServerPowerRequestAction,
    ) -> Server:
        """
        Manage VPS power.
        Switch VM off/on or reboot.
        :param server_id: ID of the server.
        :param action: Action to perform (power_off, power_on, reboot).
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.manage_server_power(
                server_id="example",
                action=ManageServerPowerRequestAction.unknown_action,
            )
        """

        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/vps/v1/servers/{param_server_id}/manage-power",
            body=marshal_VpsApiManageServerPowerRequest(
                VpsApiManageServerPowerRequest(
                    server_id=server_id,
                    action=action,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def reinstall_server(
        self,
        *,
        server_id: str,
        os_id: str,
        ssh_key_id: Optional[str] = None,
    ) -> Server:
        """
        Reinstall VPS.
        Reinstall a given OS to the VPS.
        :param server_id: ID of the server.
        :param os_id: OS ID to reinstall on the server.
        :param ssh_key_id: SSH key to install on the server.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.reinstall_server(
                server_id="example",
                os_id="example",
            )
        """

        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/vps/v1/servers/{param_server_id}/reinstall",
            body=marshal_VpsApiReinstallServerRequest(
                VpsApiReinstallServerRequest(
                    server_id=server_id,
                    os_id=os_id,
                    ssh_key_id=ssh_key_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def list_offers(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListOffersResponse:
        """
        List VPS offers.
        :param page: Page number.
        :param page_size: Number of offers per page.
        :return: :class:`ListOffersResponse <ListOffersResponse>`

        Usage:
        ::

            result = await api.list_offers()
        """

        res = self._request(
            "GET",
            "/vps/v1/offers",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOffersResponse(res.json())

    async def list_offers_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Offer]:
        """
        List VPS offers.
        :param page: Page number.
        :param page_size: Number of offers per page.
        :return: :class:`list[Offer] <list[Offer]>`

        Usage:
        ::

            result = await api.list_offers_all()
        """

        return await fetch_all_pages_async(
            type=ListOffersResponse,
            key="offers",
            fetcher=self.list_offers,
            args={
                "page": page,
                "page_size": page_size,
            },
        )

    async def get_offer(
        self,
        *,
        offer_id: str,
    ) -> Offer:
        """
        Get offer.
        Return specific offer for the given ID.
        :param offer_id: ID of the offer.
        :return: :class:`Offer <Offer>`

        Usage:
        ::

            result = await api.get_offer(
                offer_id="example",
            )
        """

        param_offer_id = validate_path_param("offer_id", offer_id)

        res = self._request(
            "GET",
            f"/vps/v1/offers/{param_offer_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Offer(res.json())

    async def list_os(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListOSResponse:
        """
        List available OS.
        List all available OS.
        :param page: Page number.
        :param page_size: Number of OS per page.
        :return: :class:`ListOSResponse <ListOSResponse>`

        Usage:
        ::

            result = await api.list_os()
        """

        res = self._request(
            "GET",
            "/vps/v1/os",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOSResponse(res.json())

    async def list_os_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[OS]:
        """
        List available OS.
        List all available OS.
        :param page: Page number.
        :param page_size: Number of OS per page.
        :return: :class:`list[OS] <list[OS]>`

        Usage:
        ::

            result = await api.list_os_all()
        """

        return await fetch_all_pages_async(
            type=ListOSResponse,
            key="os",
            fetcher=self.list_os,
            args={
                "page": page,
                "page_size": page_size,
            },
        )

    async def list_locations(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListLocationsResponse:
        """
        List available locations.
        List available locations and their available offers.
        :param page: Page number.
        :param page_size: Number of locations per page.
        :return: :class:`ListLocationsResponse <ListLocationsResponse>`

        Usage:
        ::

            result = await api.list_locations()
        """

        res = self._request(
            "GET",
            "/vps/v1/locations",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLocationsResponse(res.json())

    async def list_locations_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Location]:
        """
        List available locations.
        List available locations and their available offers.
        :param page: Page number.
        :param page_size: Number of locations per page.
        :return: :class:`list[Location] <list[Location]>`

        Usage:
        ::

            result = await api.list_locations_all()
        """

        return await fetch_all_pages_async(
            type=ListLocationsResponse,
            key="locations",
            fetcher=self.list_locations,
            args={
                "page": page,
                "page_size": page_size,
            },
        )
