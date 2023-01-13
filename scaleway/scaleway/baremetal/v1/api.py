# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages,
    validate_path_param,
    wait_for_resource,
)
from .types import (
    ListServerEventsRequestOrderBy,
    ListServerPrivateNetworksRequestOrderBy,
    ListServersRequestOrderBy,
    ListSettingsRequestOrderBy,
    OfferSubscriptionPeriod,
    ServerBootType,
    BMCAccess,
    CreateServerRequestInstall,
    GetServerMetricsResponse,
    IP,
    ListOSResponse,
    ListOffersResponse,
    ListOptionsResponse,
    ListServerEventsResponse,
    ListServerPrivateNetworksResponse,
    ListServersResponse,
    ListSettingsResponse,
    OS,
    Offer,
    Option,
    Server,
    ServerEvent,
    ServerPrivateNetwork,
    SetServerPrivateNetworksResponse,
    Setting,
    CreateServerRequest,
    UpdateServerRequest,
    InstallServerRequest,
    RebootServerRequest,
    StartServerRequest,
    StartBMCAccessRequest,
    UpdateIPRequest,
    AddOptionServerRequest,
    UpdateSettingRequest,
    PrivateNetworkApiAddServerPrivateNetworkRequest,
    PrivateNetworkApiSetServerPrivateNetworksRequest,
)
from .content import (
    SERVER_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_AddOptionServerRequest,
    marshal_CreateServerRequest,
    marshal_InstallServerRequest,
    marshal_PrivateNetworkApiAddServerPrivateNetworkRequest,
    marshal_PrivateNetworkApiSetServerPrivateNetworksRequest,
    marshal_RebootServerRequest,
    marshal_StartBMCAccessRequest,
    marshal_StartServerRequest,
    marshal_UpdateIPRequest,
    marshal_UpdateServerRequest,
    marshal_UpdateSettingRequest,
    unmarshal_IP,
    unmarshal_OS,
    unmarshal_Offer,
    unmarshal_Option,
    unmarshal_Server,
    unmarshal_ServerPrivateNetwork,
    unmarshal_Setting,
    unmarshal_BMCAccess,
    unmarshal_GetServerMetricsResponse,
    unmarshal_ListOSResponse,
    unmarshal_ListOffersResponse,
    unmarshal_ListOptionsResponse,
    unmarshal_ListServerEventsResponse,
    unmarshal_ListServerPrivateNetworksResponse,
    unmarshal_ListServersResponse,
    unmarshal_ListSettingsResponse,
    unmarshal_SetServerPrivateNetworksResponse,
)


class BaremetalV1API(API):
    """
    Elastic metal API.

    This API allows to manage your Bare metal server.
    """

    def list_servers(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListServersRequestOrderBy = ListServersRequestOrderBy.CREATED_AT_ASC,
        tags: Optional[List[str]] = None,
        status: Optional[List[str]] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        option_id: Optional[str] = None,
    ) -> ListServersResponse:
        """
        List elastic metal servers for organization.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param page: Page number
        :param page_size: Number of server per page
        :param order_by: Order of the servers
        :param tags: Filter by tags
        :param status: Filter by status
        :param name: Filter by name
        :param organization_id: Filter by organization ID
        :param project_id: Filter by project ID
        :param option_id: Filter by option ID
        :return: :class:`ListServersResponse <ListServersResponse>`

        Usage:
        ::

            result = api.list_servers()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/servers",
            params={
                "name": name,
                "option_id": option_id,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "status": status,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServersResponse(res.json())

    def list_servers_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListServersRequestOrderBy] = None,
        tags: Optional[List[str]] = None,
        status: Optional[List[str]] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        option_id: Optional[str] = None,
    ) -> List[Server]:
        """
        List elastic metal servers for organization.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param page: Page number
        :param page_size: Number of server per page
        :param order_by: Order of the servers
        :param tags: Filter by tags
        :param status: Filter by status
        :param name: Filter by name
        :param organization_id: Filter by organization ID
        :param project_id: Filter by project ID
        :param option_id: Filter by option ID
        :return: :class:`List[ListServersResponse] <List[ListServersResponse]>`

        Usage:
        ::

            result = api.list_servers_all()
        """

        return fetch_all_pages(
            type=ListServersResponse,
            key="servers",
            fetcher=self.list_servers,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "tags": tags,
                "status": status,
                "name": name,
                "organization_id": organization_id,
                "project_id": project_id,
                "option_id": option_id,
            },
        )

    def get_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Get the server associated with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.get_server(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def wait_for_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[Server, bool]] = None,
    ) -> Server:
        """
        Waits for :class:`Server <Server>` to be in a final state.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server
        :param options: The options for the waiter
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.wait_for_server(server_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in SERVER_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_server,
            options=options,
            args={
                "server_id": server_id,
                "zone": zone,
            },
        )

    def create_server(
        self,
        *,
        offer_id: str,
        name: str,
        description: str,
        zone: Optional[Zone] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        install: Optional[CreateServerRequestInstall] = None,
        option_ids: Optional[List[str]] = None,
    ) -> Server:
        """
        Create a new elastic metal server. Once the server is created, you probably want to install an OS.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param offer_id: Offer ID of the new server
        :param organization_id: Organization ID with which the server will be created.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Project ID with which the server will be created.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param name: Name of the server (≠hostname)
        :param description: Description associated to the server, max 255 characters
        :param tags: Tags to associate to the server
        :param install: Configuration of installation
        :param option_ids: IDs of options to enable on server
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.create_server(
                offer_id="example",
                name="example",
                description="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers",
            body=marshal_CreateServerRequest(
                CreateServerRequest(
                    offer_id=offer_id,
                    name=name,
                    description=description,
                    zone=zone,
                    organization_id=organization_id,
                    project_id=project_id,
                    tags=tags,
                    install=install,
                    option_ids=option_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def update_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Server:
        """
        Update the server associated with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server to update
        :param name: Name of the server (≠hostname), not updated if null
        :param description: Description associated to the server, max 255 characters, not updated if null
        :param tags: Tags associated to the server, not updated if null
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.update_server(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "PATCH",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}",
            body=marshal_UpdateServerRequest(
                UpdateServerRequest(
                    server_id=server_id,
                    zone=zone,
                    name=name,
                    description=description,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def install_server(
        self,
        *,
        server_id: str,
        os_id: str,
        hostname: str,
        ssh_key_ids: List[str],
        zone: Optional[Zone] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
        service_user: Optional[str] = None,
        service_password: Optional[str] = None,
    ) -> Server:
        """
        Install an OS on the server associated with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: Server ID to install
        :param os_id: ID of the OS to install on the server
        :param hostname: Hostname of the server
        :param ssh_key_ids: SSH key IDs authorized on the server
        :param user: User used for the installation
        :param password: Password used for the installation
        :param service_user: User used for the service to install
        :param service_password: Password used for the service to install
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.install_server(
                server_id="example",
                os_id="example",
                hostname="example",
                ssh_key_ids=["example"],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/install",
            body=marshal_InstallServerRequest(
                InstallServerRequest(
                    server_id=server_id,
                    os_id=os_id,
                    hostname=hostname,
                    ssh_key_ids=ssh_key_ids,
                    zone=zone,
                    user=user,
                    password=password,
                    service_user=service_user,
                    service_password=service_password,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def get_server_metrics(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> GetServerMetricsResponse:
        """
        Give the ping status on the server associated with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: Server ID to get the metrics
        :return: :class:`GetServerMetricsResponse <GetServerMetricsResponse>`

        Usage:
        ::

            result = api.get_server_metrics(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/metrics",
        )

        self._throw_on_error(res)
        return unmarshal_GetServerMetricsResponse(res.json())

    def delete_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Delete the server associated with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server to delete
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.delete_server(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "DELETE",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def reboot_server(
        self,
        *,
        server_id: str,
        boot_type: ServerBootType,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Reboot the server associated with the given ID, use boot param to reboot in rescue.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server to reboot
        :param boot_type: The type of boot
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.reboot_server(
                server_id="example",
                boot_type=unknown_boot_type,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/reboot",
            body=marshal_RebootServerRequest(
                RebootServerRequest(
                    server_id=server_id,
                    boot_type=boot_type,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def start_server(
        self,
        *,
        server_id: str,
        boot_type: ServerBootType,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Start the server associated with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server to start
        :param boot_type: The type of boot
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.start_server(
                server_id="example",
                boot_type=unknown_boot_type,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/start",
            body=marshal_StartServerRequest(
                StartServerRequest(
                    server_id=server_id,
                    boot_type=boot_type,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def stop_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Stop the server associated with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server to stop
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.stop_server(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/stop",
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def list_server_events(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListServerEventsRequestOrderBy = ListServerEventsRequestOrderBy.CREATED_AT_ASC,
    ) -> ListServerEventsResponse:
        """
        List events associated to the given server ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server events searched
        :param page: Page number
        :param page_size: Number of server events per page
        :param order_by: Order of the server events
        :return: :class:`ListServerEventsResponse <ListServerEventsResponse>`

        Usage:
        ::

            result = api.list_server_events(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/events",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServerEventsResponse(res.json())

    def list_server_events_all(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListServerEventsRequestOrderBy] = None,
    ) -> List[ServerEvent]:
        """
        List events associated to the given server ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server events searched
        :param page: Page number
        :param page_size: Number of server events per page
        :param order_by: Order of the server events
        :return: :class:`List[ListServerEventsResponse] <List[ListServerEventsResponse]>`

        Usage:
        ::

            result = api.list_server_events_all(server_id="example")
        """

        return fetch_all_pages(
            type=ListServerEventsResponse,
            key="events",
            fetcher=self.list_server_events,
            args={
                "server_id": server_id,
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    def start_bmc_access(
        self,
        *,
        server_id: str,
        ip: str,
        zone: Optional[Zone] = None,
    ) -> BMCAccess:
        """
        Start BMC (Baseboard Management Controller) access associated with the given ID.
        The BMC (Baseboard Management Controller) access is available one hour after the installation of the server.
        You need first to create an option Remote Access. You will find the ID and the price with a call to listOffers (https://developers.scaleway.com/en/products/baremetal/api/#get-78db92). Then you can add the option https://developers.scaleway.com/en/products/baremetal/api/#post-b14abd. Do not forget to delete the Option.
         After start BMC, you need to Get Remote Access to get the login/password https://developers.scaleway.com/en/products/baremetal/api/#get-cefc0f.

        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server
        :param ip: The IP authorized to connect to the given server
        :return: :class:`BMCAccess <BMCAccess>`

        Usage:
        ::

            result = api.start_bmc_access(
                server_id="example",
                ip="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/bmc-access",
            body=marshal_StartBMCAccessRequest(
                StartBMCAccessRequest(
                    server_id=server_id,
                    ip=ip,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_BMCAccess(res.json())

    def get_bmc_access(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> BMCAccess:
        """
        Get the BMC (Baseboard Management Controller) access associated with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server
        :return: :class:`BMCAccess <BMCAccess>`

        Usage:
        ::

            result = api.get_bmc_access(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/bmc-access",
        )

        self._throw_on_error(res)
        return unmarshal_BMCAccess(res.json())

    def stop_bmc_access(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Stop BMC (Baseboard Management Controller) access associated with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server

        Usage:
        ::

            result = api.stop_bmc_access(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "DELETE",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/bmc-access",
        )

        self._throw_on_error(res)
        return None

    def update_ip(
        self,
        *,
        server_id: str,
        ip_id: str,
        zone: Optional[Zone] = None,
        reverse: Optional[str] = None,
    ) -> IP:
        """
        Configure ip associated with the given server ID and ipID. You can use this method to set a reverse dns for an IP.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server
        :param ip_id: ID of the IP to update
        :param reverse: New reverse IP to update, not updated if null
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = api.update_ip(
                server_id="example",
                ip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "PATCH",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/ips/{param_ip_id}",
            body=marshal_UpdateIPRequest(
                UpdateIPRequest(
                    server_id=server_id,
                    ip_id=ip_id,
                    zone=zone,
                    reverse=reverse,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    def add_option_server(
        self,
        *,
        server_id: str,
        option_id: str,
        zone: Optional[Zone] = None,
        expires_at: Optional[datetime] = None,
    ) -> Server:
        """
        Add an option to a specific server.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server
        :param option_id: ID of the option to add
        :param expires_at: Auto expire the option after this date
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.add_option_server(
                server_id="example",
                option_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_option_id = validate_path_param("option_id", option_id)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/options/{param_option_id}",
            body=marshal_AddOptionServerRequest(
                AddOptionServerRequest(
                    server_id=server_id,
                    option_id=option_id,
                    zone=zone,
                    expires_at=expires_at,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def delete_option_server(
        self,
        *,
        server_id: str,
        option_id: str,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Delete an option from a specific server.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: ID of the server
        :param option_id: ID of the option to delete
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.delete_option_server(
                server_id="example",
                option_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_option_id = validate_path_param("option_id", option_id)

        res = self._request(
            "DELETE",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/options/{param_option_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def list_offers(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        subscription_period: OfferSubscriptionPeriod = OfferSubscriptionPeriod.UNKNOWN_SUBSCRIPTION_PERIOD,
    ) -> ListOffersResponse:
        """
        List all available server offers.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param page: Page number
        :param page_size: Number of offers per page
        :param subscription_period: Period of subscription to filter offers
        :return: :class:`ListOffersResponse <ListOffersResponse>`

        Usage:
        ::

            result = api.list_offers()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/offers",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "subscription_period": subscription_period,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOffersResponse(res.json())

    def list_offers_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        subscription_period: Optional[OfferSubscriptionPeriod] = None,
    ) -> List[Offer]:
        """
        List all available server offers.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param page: Page number
        :param page_size: Number of offers per page
        :param subscription_period: Period of subscription to filter offers
        :return: :class:`List[ListOffersResponse] <List[ListOffersResponse]>`

        Usage:
        ::

            result = api.list_offers_all()
        """

        return fetch_all_pages(
            type=ListOffersResponse,
            key="offers",
            fetcher=self.list_offers,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "subscription_period": subscription_period,
            },
        )

    def get_offer(
        self,
        *,
        offer_id: str,
        zone: Optional[Zone] = None,
    ) -> Offer:
        """
        Return specific offer for the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param offer_id: ID of the researched Offer
        :return: :class:`Offer <Offer>`

        Usage:
        ::

            result = api.get_offer(offer_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_offer_id = validate_path_param("offer_id", offer_id)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/offers/{param_offer_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Offer(res.json())

    def get_option(
        self,
        *,
        option_id: str,
        zone: Optional[Zone] = None,
    ) -> Option:
        """
        Return specific option for the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param option_id: ID of the option
        :return: :class:`Option <Option>`

        Usage:
        ::

            result = api.get_option(option_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_option_id = validate_path_param("option_id", option_id)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/options/{param_option_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Option(res.json())

    def list_options(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        offer_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ListOptionsResponse:
        """
        List all options matching with filters.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param page: Page number
        :param page_size: Number of options per page
        :param offer_id: Filter options by offer_id
        :param name: Filter options by name
        :return: :class:`ListOptionsResponse <ListOptionsResponse>`

        Usage:
        ::

            result = api.list_options()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/options",
            params={
                "name": name,
                "offer_id": offer_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOptionsResponse(res.json())

    def list_options_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        offer_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> List[Option]:
        """
        List all options matching with filters.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param page: Page number
        :param page_size: Number of options per page
        :param offer_id: Filter options by offer_id
        :param name: Filter options by name
        :return: :class:`List[ListOptionsResponse] <List[ListOptionsResponse]>`

        Usage:
        ::

            result = api.list_options_all()
        """

        return fetch_all_pages(
            type=ListOptionsResponse,
            key="options",
            fetcher=self.list_options,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "offer_id": offer_id,
                "name": name,
            },
        )

    def list_settings(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListSettingsRequestOrderBy = ListSettingsRequestOrderBy.CREATED_AT_ASC,
        project_id: Optional[str] = None,
    ) -> ListSettingsResponse:
        """
        Return all settings for a project ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param page: Page number
        :param page_size: Set the maximum list size
        :param order_by: Order the response
        :param project_id: ID of the project
        :return: :class:`ListSettingsResponse <ListSettingsResponse>`

        Usage:
        ::

            result = api.list_settings()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/settings",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSettingsResponse(res.json())

    def list_settings_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSettingsRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[Setting]:
        """
        Return all settings for a project ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param page: Page number
        :param page_size: Set the maximum list size
        :param order_by: Order the response
        :param project_id: ID of the project
        :return: :class:`List[ListSettingsResponse] <List[ListSettingsResponse]>`

        Usage:
        ::

            result = api.list_settings_all()
        """

        return fetch_all_pages(
            type=ListSettingsResponse,
            key="settings",
            fetcher=self.list_settings,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    def update_setting(
        self,
        *,
        setting_id: str,
        zone: Optional[Zone] = None,
        enabled: Optional[bool] = None,
    ) -> Setting:
        """
        Update a setting for a project ID (enable or disable).
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param setting_id: ID of the setting
        :param enabled: Enable/Disable the setting
        :return: :class:`Setting <Setting>`

        Usage:
        ::

            result = api.update_setting(setting_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_setting_id = validate_path_param("setting_id", setting_id)

        res = self._request(
            "PATCH",
            f"/baremetal/v1/zones/{param_zone}/settings/{param_setting_id}",
            body=marshal_UpdateSettingRequest(
                UpdateSettingRequest(
                    setting_id=setting_id,
                    zone=zone,
                    enabled=enabled,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Setting(res.json())

    def list_os(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        offer_id: Optional[str] = None,
    ) -> ListOSResponse:
        """
        List all available OS that can be install on an elastic metal server.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param page: Page number
        :param page_size: Number of OS per page
        :param offer_id: Filter OS by offer ID
        :return: :class:`ListOSResponse <ListOSResponse>`

        Usage:
        ::

            result = api.list_os()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/os",
            params={
                "offer_id": offer_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOSResponse(res.json())

    def list_os_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        offer_id: Optional[str] = None,
    ) -> List[OS]:
        """
        List all available OS that can be install on an elastic metal server.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param page: Page number
        :param page_size: Number of OS per page
        :param offer_id: Filter OS by offer ID
        :return: :class:`List[ListOSResponse] <List[ListOSResponse]>`

        Usage:
        ::

            result = api.list_os_all()
        """

        return fetch_all_pages(
            type=ListOSResponse,
            key="os",
            fetcher=self.list_os,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "offer_id": offer_id,
            },
        )

    def get_os(
        self,
        *,
        os_id: str,
        zone: Optional[Zone] = None,
    ) -> OS:
        """
        Return specific OS for the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param os_id: ID of the OS
        :return: :class:`OS <OS>`

        Usage:
        ::

            result = api.get_os(os_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_os_id = validate_path_param("os_id", os_id)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/os/{param_os_id}",
        )

        self._throw_on_error(res)
        return unmarshal_OS(res.json())


class BaremetalPrivateNetworkV1API(API):
    """
    Elastic Metal Private Network API.
    """

    def add_server_private_network(
        self,
        *,
        server_id: str,
        private_network_id: str,
        zone: Optional[Zone] = None,
    ) -> ServerPrivateNetwork:
        """
        Add a server to a private network
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: The ID of the server
        :param private_network_id: The ID of the private network
        :return: :class:`ServerPrivateNetwork <ServerPrivateNetwork>`

        Usage:
        ::

            result = api.add_server_private_network(
                server_id="example",
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/private-networks",
            body=marshal_PrivateNetworkApiAddServerPrivateNetworkRequest(
                PrivateNetworkApiAddServerPrivateNetworkRequest(
                    server_id=server_id,
                    private_network_id=private_network_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ServerPrivateNetwork(res.json())

    def set_server_private_networks(
        self,
        *,
        server_id: str,
        private_network_ids: List[str],
        zone: Optional[Zone] = None,
    ) -> SetServerPrivateNetworksResponse:
        """
        Set multiple private networks on a server
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: The ID of the server
        :param private_network_ids: The IDs of the private networks
        :return: :class:`SetServerPrivateNetworksResponse <SetServerPrivateNetworksResponse>`

        Usage:
        ::

            result = api.set_server_private_networks(
                server_id="example",
                private_network_ids=["example"],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "PUT",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/private-networks",
            body=marshal_PrivateNetworkApiSetServerPrivateNetworksRequest(
                PrivateNetworkApiSetServerPrivateNetworksRequest(
                    server_id=server_id,
                    private_network_ids=private_network_ids,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetServerPrivateNetworksResponse(res.json())

    def list_server_private_networks(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: ListServerPrivateNetworksRequestOrderBy = ListServerPrivateNetworksRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        server_id: Optional[str] = None,
        private_network_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListServerPrivateNetworksResponse:
        """
        List the private networks of a server
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: The sort order for the returned private networks
        :param page: The page number for the returned private networks
        :param page_size: The maximum number of private networks per page
        :param server_id: Filter private networks by server ID
        :param private_network_id: Filter private networks by private network ID
        :param organization_id: Filter private networks by organization ID
        :param project_id: Filter private networks by project ID
        :return: :class:`ListServerPrivateNetworksResponse <ListServerPrivateNetworksResponse>`

        Usage:
        ::

            result = api.list_server_private_networks()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/server-private-networks",
            params={
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

    def list_server_private_networks_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListServerPrivateNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        server_id: Optional[str] = None,
        private_network_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[ServerPrivateNetwork]:
        """
        List the private networks of a server
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: The sort order for the returned private networks
        :param page: The page number for the returned private networks
        :param page_size: The maximum number of private networks per page
        :param server_id: Filter private networks by server ID
        :param private_network_id: Filter private networks by private network ID
        :param organization_id: Filter private networks by organization ID
        :param project_id: Filter private networks by project ID
        :return: :class:`List[ListServerPrivateNetworksResponse] <List[ListServerPrivateNetworksResponse]>`

        Usage:
        ::

            result = api.list_server_private_networks_all()
        """

        return fetch_all_pages(
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
            },
        )

    def delete_server_private_network(
        self,
        *,
        server_id: str,
        private_network_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a private network
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: The ID of the server
        :param private_network_id: The ID of the private network

        Usage:
        ::

            result = api.delete_server_private_network(
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
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/private-networks/{param_private_network_id}",
        )

        self._throw_on_error(res)
        return None
