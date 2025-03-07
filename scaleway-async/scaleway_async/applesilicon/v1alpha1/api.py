# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, Dict, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone as ScwZone,
)
from scaleway_core.utils import (
    WaitForOptions,
    random_name,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    CommitmentType,
    ListServerPrivateNetworksRequestOrderBy,
    ListServersRequestOrderBy,
    CommitmentTypeValue,
    ConnectivityDiagnostic,
    CreateServerRequest,
    ListOSResponse,
    ListServerPrivateNetworksResponse,
    ListServerTypesResponse,
    ListServersResponse,
    OS,
    PrivateNetworkApiAddServerPrivateNetworkRequest,
    PrivateNetworkApiSetServerPrivateNetworksRequest,
    ReinstallServerRequest,
    Server,
    ServerPrivateNetwork,
    ServerType,
    SetServerPrivateNetworksResponse,
    StartConnectivityDiagnosticRequest,
    StartConnectivityDiagnosticResponse,
    UpdateServerRequest,
)
from .content import (
    SERVER_PRIVATE_NETWORK_SERVER_TRANSIENT_STATUSES,
    SERVER_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_OS,
    unmarshal_ServerPrivateNetwork,
    unmarshal_ServerType,
    unmarshal_Server,
    unmarshal_ConnectivityDiagnostic,
    unmarshal_ListOSResponse,
    unmarshal_ListServerPrivateNetworksResponse,
    unmarshal_ListServerTypesResponse,
    unmarshal_ListServersResponse,
    unmarshal_SetServerPrivateNetworksResponse,
    unmarshal_StartConnectivityDiagnosticResponse,
    marshal_CreateServerRequest,
    marshal_PrivateNetworkApiAddServerPrivateNetworkRequest,
    marshal_PrivateNetworkApiSetServerPrivateNetworksRequest,
    marshal_ReinstallServerRequest,
    marshal_StartConnectivityDiagnosticRequest,
    marshal_UpdateServerRequest,
)


class ApplesiliconV1Alpha1API(API):
    """
    This API allows you to manage your Apple silicon machines.
    """

    async def list_server_types(
        self,
        *,
        zone: Optional[ScwZone] = None,
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
        zone: Optional[ScwZone] = None,
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
        enable_vpc: bool,
        zone: Optional[ScwZone] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        os_id: Optional[str] = None,
        commitment_type: Optional[CommitmentType] = None,
    ) -> Server:
        """
        Create a server.
        Create a new server in the targeted zone, specifying its configuration including name and type.
        :param type_: Create a server of the given type.
        :param enable_vpc: Activate the Private Network feature for this server. This feature is configured through the Apple Silicon - Private Networks API.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Create a server with this given name.
        :param project_id: Create a server in the given project ID.
        :param os_id: Create a server & install the given os_id, when no os_id provided the default OS for this server type is chosen. Requesting a non-default OS will induce an extended delivery time.
        :param commitment_type: Activate commitment for this server. If not specified, there is a 24h commitment due to Apple licensing. It can be updated with the Update Server request. Available commitment depends on server type.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.create_server(
                type="example",
                enable_vpc=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/servers",
            body=marshal_CreateServerRequest(
                CreateServerRequest(
                    type_=type_,
                    enable_vpc=enable_vpc,
                    zone=zone,
                    name=name or random_name(prefix="as"),
                    project_id=project_id,
                    os_id=os_id,
                    commitment_type=commitment_type,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def list_servers(
        self,
        *,
        zone: Optional[ScwZone] = None,
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
        zone: Optional[ScwZone] = None,
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
        zone: Optional[ScwZone] = None,
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
        zone: Optional[ScwZone] = None,
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
        zone: Optional[ScwZone] = None,
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
        zone: Optional[ScwZone] = None,
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
        zone: Optional[ScwZone] = None,
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
        zone: Optional[ScwZone] = None,
        name: Optional[str] = None,
        schedule_deletion: Optional[bool] = None,
        enable_vpc: Optional[bool] = None,
        commitment_type: Optional[CommitmentTypeValue] = None,
    ) -> Server:
        """
        Update a server.
        Update the parameters of an existing Apple silicon server, specified by its server ID.
        :param server_id: UUID of the server you want to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Updated name for your server.
        :param schedule_deletion: Specify whether the server should be flagged for automatic deletion.
        :param enable_vpc: Activate or deactivate Private Network support for this server.
        :param commitment_type: Change commitment. Use 'none' to automatically cancel a renewing commitment.
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
                    enable_vpc=enable_vpc,
                    commitment_type=commitment_type,
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
        zone: Optional[ScwZone] = None,
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
        zone: Optional[ScwZone] = None,
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
        zone: Optional[ScwZone] = None,
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

    async def start_connectivity_diagnostic(
        self,
        *,
        server_id: str,
        zone: Optional[ScwZone] = None,
    ) -> StartConnectivityDiagnosticResponse:
        """
        :param server_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`StartConnectivityDiagnosticResponse <StartConnectivityDiagnosticResponse>`

        Usage:
        ::

            result = await api.start_connectivity_diagnostic(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/connectivity-diagnostics",
            body=marshal_StartConnectivityDiagnosticRequest(
                StartConnectivityDiagnosticRequest(
                    server_id=server_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_StartConnectivityDiagnosticResponse(res.json())

    async def get_connectivity_diagnostic(
        self,
        *,
        diagnostic_id: str,
        zone: Optional[ScwZone] = None,
    ) -> ConnectivityDiagnostic:
        """
        :param diagnostic_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ConnectivityDiagnostic <ConnectivityDiagnostic>`

        Usage:
        ::

            result = await api.get_connectivity_diagnostic(
                diagnostic_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_diagnostic_id = validate_path_param("diagnostic_id", diagnostic_id)

        res = self._request(
            "GET",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/connectivity-diagnostics/{param_diagnostic_id}",
        )

        self._throw_on_error(res)
        return unmarshal_ConnectivityDiagnostic(res.json())


class ApplesiliconV1Alpha1PrivateNetworkAPI(API):
    """
    Apple silicon - Private Networks API.
    """

    async def get_server_private_network(
        self,
        *,
        server_id: str,
        private_network_id: str,
        zone: Optional[ScwZone] = None,
    ) -> ServerPrivateNetwork:
        """
        :param server_id:
        :param private_network_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ServerPrivateNetwork <ServerPrivateNetwork>`

        Usage:
        ::

            result = await api.get_server_private_network(
                server_id="example",
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "GET",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/servers/{param_server_id}/private-networks/{param_private_network_id}",
        )

        self._throw_on_error(res)
        return unmarshal_ServerPrivateNetwork(res.json())

    async def wait_for_server_private_network(
        self,
        *,
        server_id: str,
        private_network_id: str,
        zone: Optional[ScwZone] = None,
        options: Optional[
            WaitForOptions[ServerPrivateNetwork, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> ServerPrivateNetwork:
        """
        :param server_id:
        :param private_network_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ServerPrivateNetwork <ServerPrivateNetwork>`

        Usage:
        ::

            result = await api.get_server_private_network(
                server_id="example",
                private_network_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = (
                lambda res: res.status
                not in SERVER_PRIVATE_NETWORK_SERVER_TRANSIENT_STATUSES
            )

        return await wait_for_resource_async(
            fetcher=self.get_server_private_network,
            options=options,
            args={
                "server_id": server_id,
                "private_network_id": private_network_id,
                "zone": zone,
            },
        )

    async def add_server_private_network(
        self,
        *,
        server_id: str,
        private_network_id: str,
        zone: Optional[ScwZone] = None,
        ipam_ip_ids: Optional[List[str]] = None,
    ) -> ServerPrivateNetwork:
        """
        Add a server to a Private Network.
        Add an Apple silicon server to a Private Network.
        :param server_id: ID of the server.
        :param private_network_id: ID of the Private Network.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param ipam_ip_ids: IPAM IDs of IPs to attach to the server.
        :return: :class:`ServerPrivateNetwork <ServerPrivateNetwork>`

        Usage:
        ::

            result = await api.add_server_private_network(
                server_id="example",
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/servers/{param_server_id}/private-networks",
            body=marshal_PrivateNetworkApiAddServerPrivateNetworkRequest(
                PrivateNetworkApiAddServerPrivateNetworkRequest(
                    server_id=server_id,
                    private_network_id=private_network_id,
                    zone=zone,
                    ipam_ip_ids=ipam_ip_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ServerPrivateNetwork(res.json())

    async def set_server_private_networks(
        self,
        *,
        server_id: str,
        per_private_network_ipam_ip_ids: Dict[str, List[str]],
        zone: Optional[ScwZone] = None,
    ) -> SetServerPrivateNetworksResponse:
        """
        Set multiple Private Networks on a server.
        Configure multiple Private Networks on an Apple silicon server.
        :param server_id: ID of the server.
        :param per_private_network_ipam_ip_ids: Object where the keys are the IDs of Private Networks and the values are arrays of IPAM IDs representing the IPs to assign to this Apple silicon server on the Private Network. If the array supplied for a Private Network is empty, the next available IP from the Private Network's CIDR block will automatically be used for attachment.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`SetServerPrivateNetworksResponse <SetServerPrivateNetworksResponse>`

        Usage:
        ::

            result = await api.set_server_private_networks(
                server_id="example",
                per_private_network_ipam_ip_ids={},
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "PUT",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/servers/{param_server_id}/private-networks",
            body=marshal_PrivateNetworkApiSetServerPrivateNetworksRequest(
                PrivateNetworkApiSetServerPrivateNetworksRequest(
                    server_id=server_id,
                    per_private_network_ipam_ip_ids=per_private_network_ipam_ip_ids,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetServerPrivateNetworksResponse(res.json())

    async def list_server_private_networks(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListServerPrivateNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        server_id: Optional[str] = None,
        private_network_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        ipam_ip_ids: Optional[List[str]] = None,
    ) -> ListServerPrivateNetworksResponse:
        """
        List the Private Networks of a server.
        List the Private Networks of an Apple silicon server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order for the returned Private Networks.
        :param page: Page number for the returned Private Networks.
        :param page_size: Maximum number of Private Networks per page.
        :param server_id: Filter Private Networks by server ID.
        :param private_network_id: Filter Private Networks by Private Network ID.
        :param organization_id: Filter Private Networks by Organization ID.
        :param project_id: Filter Private Networks by Project ID.
        :param ipam_ip_ids: Filter Private Networks by IPAM IP IDs.
        :return: :class:`ListServerPrivateNetworksResponse <ListServerPrivateNetworksResponse>`

        Usage:
        ::

            result = await api.list_server_private_networks()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/server-private-networks",
            params={
                "ipam_ip_ids": ipam_ip_ids,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "private_network_id": private_network_id,
                "project_id": project_id or self.client.default_project_id,
                "server_id": server_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServerPrivateNetworksResponse(res.json())

    async def list_server_private_networks_all(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListServerPrivateNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        server_id: Optional[str] = None,
        private_network_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        ipam_ip_ids: Optional[List[str]] = None,
    ) -> List[ServerPrivateNetwork]:
        """
        List the Private Networks of a server.
        List the Private Networks of an Apple silicon server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order for the returned Private Networks.
        :param page: Page number for the returned Private Networks.
        :param page_size: Maximum number of Private Networks per page.
        :param server_id: Filter Private Networks by server ID.
        :param private_network_id: Filter Private Networks by Private Network ID.
        :param organization_id: Filter Private Networks by Organization ID.
        :param project_id: Filter Private Networks by Project ID.
        :param ipam_ip_ids: Filter Private Networks by IPAM IP IDs.
        :return: :class:`List[ServerPrivateNetwork] <List[ServerPrivateNetwork]>`

        Usage:
        ::

            result = await api.list_server_private_networks_all()
        """

        return await fetch_all_pages_async(
            type=ListServerPrivateNetworksResponse,
            key="server_private_networks",
            fetcher=self.list_server_private_networks,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "server_id": server_id,
                "private_network_id": private_network_id,
                "organization_id": organization_id,
                "project_id": project_id,
                "ipam_ip_ids": ipam_ip_ids,
            },
        )

    async def delete_server_private_network(
        self,
        *,
        server_id: str,
        private_network_id: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete a Private Network.
        :param server_id: ID of the server.
        :param private_network_id: ID of the Private Network.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_server_private_network(
                server_id="example",
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "DELETE",
            f"/apple-silicon/v1alpha1/zones/{param_zone}/servers/{param_server_id}/private-networks/{param_private_network_id}",
        )

        self._throw_on_error(res)
