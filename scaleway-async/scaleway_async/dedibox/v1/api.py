# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    ScwFile,
    Zone,
    unmarshal_ScwFile,
)
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    AttachFailoverIPToMacAddressRequestMacType,
    ListFailoverIPsRequestOrderBy,
    ListInvoicesRequestOrderBy,
    ListOSRequestOrderBy,
    ListOffersRequestOrderBy,
    ListRefundsRequestOrderBy,
    ListRpnCapableSanServersRequestOrderBy,
    ListRpnCapableServersRequestOrderBy,
    ListRpnGroupMembersRequestOrderBy,
    ListRpnGroupsRequestOrderBy,
    ListRpnInvitesRequestOrderBy,
    ListRpnSansRequestOrderBy,
    ListRpnServerCapabilitiesRequestOrderBy,
    ListRpnV2CapableResourcesRequestOrderBy,
    ListRpnV2GroupLogsRequestOrderBy,
    ListRpnV2GroupsRequestOrderBy,
    ListRpnV2MembersRequestOrderBy,
    ListRpnV2MembersRequestType,
    ListServerDisksRequestOrderBy,
    ListServerEventsRequestOrderBy,
    ListServersRequestOrderBy,
    ListServicesRequestOrderBy,
    OSType,
    OfferCatalog,
    RpnSanIpType,
    RpnV2GroupType,
    AttachFailoverIPToMacAddressRequest,
    AttachFailoverIPsRequest,
    BMCAccess,
    Backup,
    CanOrderResponse,
    CreateFailoverIPsRequest,
    CreateFailoverIPsResponse,
    CreateServerRequest,
    DetachFailoverIPsRequest,
    FailoverIP,
    GetIPv6BlockQuotasResponse,
    GetRemainingQuotaResponse,
    GetRpnStatusResponse,
    IP,
    IPv6Block,
    IPv6BlockApiCreateIPv6BlockRequest,
    IPv6BlockApiCreateIPv6BlockSubnetRequest,
    IPv6BlockApiUpdateIPv6BlockRequest,
    InstallPartition,
    InstallServerRequest,
    Invoice,
    InvoiceSummary,
    ListFailoverIPsResponse,
    ListIPv6BlockSubnetsAvailableResponse,
    ListInvoicesResponse,
    ListIpsResponse,
    ListOSResponse,
    ListOffersResponse,
    ListRefundsResponse,
    ListRpnCapableSanServersResponse,
    ListRpnCapableServersResponse,
    ListRpnGroupMembersResponse,
    ListRpnGroupsResponse,
    ListRpnInvitesResponse,
    ListRpnSansResponse,
    ListRpnServerCapabilitiesResponse,
    ListRpnV2CapableResourcesResponse,
    ListRpnV2GroupLogsResponse,
    ListRpnV2GroupsResponse,
    ListRpnV2MembersResponse,
    ListServerDisksResponse,
    ListServerEventsResponse,
    ListServersResponse,
    ListServicesResponse,
    ListSubscribableServerOptionsResponse,
    Log,
    OS,
    Offer,
    Raid,
    Refund,
    RefundSummary,
    Rescue,
    RpnGroup,
    RpnGroupMember,
    RpnSan,
    RpnSanApiAddIpRequest,
    RpnSanApiCreateRpnSanRequest,
    RpnSanApiRemoveIpRequest,
    RpnSanServer,
    RpnSanSummary,
    RpnServerCapability,
    RpnV1ApiAddRpnGroupMembersRequest,
    RpnV1ApiCreateRpnGroupRequest,
    RpnV1ApiDeleteRpnGroupMembersRequest,
    RpnV1ApiLeaveRpnGroupRequest,
    RpnV1ApiRpnGroupInviteRequest,
    RpnV1ApiUpdateRpnGroupNameRequest,
    RpnV2ApiAddRpnV2MembersRequest,
    RpnV2ApiCreateRpnV2GroupRequest,
    RpnV2ApiDeleteRpnV2MembersRequest,
    RpnV2ApiEnableRpnV2GroupCompatibilityRequest,
    RpnV2ApiUpdateRpnV2GroupNameRequest,
    RpnV2ApiUpdateRpnV2VlanForMembersRequest,
    RpnV2Group,
    RpnV2Member,
    Server,
    ServerDefaultPartitioning,
    ServerDisk,
    ServerEvent,
    ServerInstall,
    ServerSummary,
    Service,
    StartBMCAccessRequest,
    StartRescueRequest,
    SubscribeServerOptionRequest,
    SubscribeStorageOptionsRequest,
    SubscribeStorageOptionsResponse,
    UpdatableRaidArray,
    UpdateRaidRequest,
    UpdateReverseRequest,
    UpdateServerBackupRequest,
    UpdateServerRequest,
    UpdateServerTagsRequest,
)
from .content import (
    BMC_ACCESS_TRANSIENT_STATUSES,
    RPN_SAN_TRANSIENT_STATUSES,
    RPN_V2_GROUP_TRANSIENT_STATUSES,
    SERVER_INSTALL_TRANSIENT_STATUSES,
    SERVER_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_IP,
    unmarshal_Offer,
    unmarshal_OS,
    unmarshal_RpnSan,
    unmarshal_RpnGroup,
    unmarshal_Server,
    unmarshal_RpnV2Group,
    unmarshal_Service,
    unmarshal_FailoverIP,
    unmarshal_BMCAccess,
    unmarshal_Backup,
    unmarshal_CanOrderResponse,
    unmarshal_CreateFailoverIPsResponse,
    unmarshal_GetIPv6BlockQuotasResponse,
    unmarshal_GetRemainingQuotaResponse,
    unmarshal_GetRpnStatusResponse,
    unmarshal_IPv6Block,
    unmarshal_Invoice,
    unmarshal_ListFailoverIPsResponse,
    unmarshal_ListIPv6BlockSubnetsAvailableResponse,
    unmarshal_ListInvoicesResponse,
    unmarshal_ListIpsResponse,
    unmarshal_ListOSResponse,
    unmarshal_ListOffersResponse,
    unmarshal_ListRefundsResponse,
    unmarshal_ListRpnCapableSanServersResponse,
    unmarshal_ListRpnCapableServersResponse,
    unmarshal_ListRpnGroupMembersResponse,
    unmarshal_ListRpnGroupsResponse,
    unmarshal_ListRpnInvitesResponse,
    unmarshal_ListRpnSansResponse,
    unmarshal_ListRpnServerCapabilitiesResponse,
    unmarshal_ListRpnV2CapableResourcesResponse,
    unmarshal_ListRpnV2GroupLogsResponse,
    unmarshal_ListRpnV2GroupsResponse,
    unmarshal_ListRpnV2MembersResponse,
    unmarshal_ListServerDisksResponse,
    unmarshal_ListServerEventsResponse,
    unmarshal_ListServersResponse,
    unmarshal_ListServicesResponse,
    unmarshal_ListSubscribableServerOptionsResponse,
    unmarshal_Raid,
    unmarshal_Refund,
    unmarshal_Rescue,
    unmarshal_ServerDefaultPartitioning,
    unmarshal_ServerInstall,
    unmarshal_SubscribeStorageOptionsResponse,
    marshal_AttachFailoverIPToMacAddressRequest,
    marshal_AttachFailoverIPsRequest,
    marshal_CreateFailoverIPsRequest,
    marshal_CreateServerRequest,
    marshal_DetachFailoverIPsRequest,
    marshal_IPv6BlockApiCreateIPv6BlockRequest,
    marshal_IPv6BlockApiCreateIPv6BlockSubnetRequest,
    marshal_IPv6BlockApiUpdateIPv6BlockRequest,
    marshal_InstallServerRequest,
    marshal_RpnSanApiAddIpRequest,
    marshal_RpnSanApiCreateRpnSanRequest,
    marshal_RpnSanApiRemoveIpRequest,
    marshal_RpnV1ApiAddRpnGroupMembersRequest,
    marshal_RpnV1ApiCreateRpnGroupRequest,
    marshal_RpnV1ApiDeleteRpnGroupMembersRequest,
    marshal_RpnV1ApiLeaveRpnGroupRequest,
    marshal_RpnV1ApiRpnGroupInviteRequest,
    marshal_RpnV1ApiUpdateRpnGroupNameRequest,
    marshal_RpnV2ApiAddRpnV2MembersRequest,
    marshal_RpnV2ApiCreateRpnV2GroupRequest,
    marshal_RpnV2ApiDeleteRpnV2MembersRequest,
    marshal_RpnV2ApiEnableRpnV2GroupCompatibilityRequest,
    marshal_RpnV2ApiUpdateRpnV2GroupNameRequest,
    marshal_RpnV2ApiUpdateRpnV2VlanForMembersRequest,
    marshal_StartBMCAccessRequest,
    marshal_StartRescueRequest,
    marshal_SubscribeServerOptionRequest,
    marshal_SubscribeStorageOptionsRequest,
    marshal_UpdateRaidRequest,
    marshal_UpdateReverseRequest,
    marshal_UpdateServerBackupRequest,
    marshal_UpdateServerRequest,
    marshal_UpdateServerTagsRequest,
)


class DediboxV1API(API):
    """
    Dedibox Phoenix API.
    """

    async def list_servers(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListServersRequestOrderBy] = None,
        project_id: Optional[str] = None,
        search: Optional[str] = None,
    ) -> ListServersResponse:
        """
        List baremetal servers for project.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of server per page.
        :param order_by: Order of the servers.
        :param project_id: Filter servers by project ID.
        :param search: Filter servers by hostname.
        :return: :class:`ListServersResponse <ListServersResponse>`

        Usage:
        ::

            result = await api.list_servers()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/servers",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "search": search,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServersResponse(res.json())

    async def list_servers_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListServersRequestOrderBy] = None,
        project_id: Optional[str] = None,
        search: Optional[str] = None,
    ) -> List[ServerSummary]:
        """
        List baremetal servers for project.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of server per page.
        :param order_by: Order of the servers.
        :param project_id: Filter servers by project ID.
        :param search: Filter servers by hostname.
        :return: :class:`List[ServerSummary] <List[ServerSummary]>`

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
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
                "search": search,
            },
        )

    async def get_server(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Get a specific baremetal server.
        Get the server associated with the given ID.
        :param server_id: ID of the server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.get_server(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def wait_for_server(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[Server, Union[bool, Awaitable[bool]]]] = None,
    ) -> Server:
        """
        Get a specific baremetal server.
        Get the server associated with the given ID.
        :param server_id: ID of the server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.get_server(
                server_id=1,
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

    async def get_server_backup(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
    ) -> Backup:
        """
        :param server_id: Server ID of the backup.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Backup <Backup>`

        Usage:
        ::

            result = await api.get_server_backup(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/backups",
        )

        self._throw_on_error(res)
        return unmarshal_Backup(res.json())

    async def update_server_backup(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
        password: Optional[str] = None,
        autologin: Optional[bool] = None,
        acl_enabled: Optional[bool] = None,
    ) -> Backup:
        """
        :param server_id: Server ID to update backup.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param password: Password of the server backup.
        :param autologin: Autologin of the server backup.
        :param acl_enabled: Boolean to enable or disable ACL.
        :return: :class:`Backup <Backup>`

        Usage:
        ::

            result = await api.update_server_backup(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "PATCH",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/backups",
            body=marshal_UpdateServerBackupRequest(
                UpdateServerBackupRequest(
                    server_id=server_id,
                    zone=zone,
                    password=password,
                    autologin=autologin,
                    acl_enabled=acl_enabled,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backup(res.json())

    async def list_subscribable_server_options(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListSubscribableServerOptionsResponse:
        """
        List subscribable server options.
        List subscribable options associated to the given server ID.
        :param server_id: Server ID of the subscribable server options.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of subscribable server option per page.
        :return: :class:`ListSubscribableServerOptionsResponse <ListSubscribableServerOptionsResponse>`

        Usage:
        ::

            result = await api.list_subscribable_server_options(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/subscribable-server-options",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSubscribableServerOptionsResponse(res.json())

    async def list_subscribable_server_options_all(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Offer]:
        """
        List subscribable server options.
        List subscribable options associated to the given server ID.
        :param server_id: Server ID of the subscribable server options.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of subscribable server option per page.
        :return: :class:`List[Offer] <List[Offer]>`

        Usage:
        ::

            result = await api.list_subscribable_server_options_all(
                server_id=1,
            )
        """

        return await fetch_all_pages_async(
            type=ListSubscribableServerOptionsResponse,
            key="server_options",
            fetcher=self.list_subscribable_server_options,
            args={
                "server_id": server_id,
                "zone": zone,
                "page": page,
                "page_size": page_size,
            },
        )

    async def subscribe_server_option(
        self,
        *,
        server_id: int,
        option_id: int,
        zone: Optional[Zone] = None,
    ) -> Service:
        """
        Subscribe server option.
        Subscribe option for the given server ID.
        :param server_id: Server ID to subscribe server option.
        :param option_id: Option ID to subscribe.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Service <Service>`

        Usage:
        ::

            result = await api.subscribe_server_option(
                server_id=1,
                option_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "PATCH",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/subscribe-server-option",
            body=marshal_SubscribeServerOptionRequest(
                SubscribeServerOptionRequest(
                    server_id=server_id,
                    option_id=option_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Service(res.json())

    async def create_server(
        self,
        *,
        offer_id: int,
        server_option_ids: List[int],
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
        datacenter_name: Optional[str] = None,
    ) -> Service:
        """
        Create a baremetal server.
        Create a new baremetal server. The order return you a service ID to follow the provisionning status you could call GetService.
        :param offer_id: Offer ID of the new server.
        :param server_option_ids: Server option IDs of the new server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID of the new server.
        :param datacenter_name: Datacenter name of the new server.
        :return: :class:`Service <Service>`

        Usage:
        ::

            result = await api.create_server(
                offer_id=1,
                server_option_ids=[],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/servers",
            body=marshal_CreateServerRequest(
                CreateServerRequest(
                    offer_id=offer_id,
                    server_option_ids=server_option_ids,
                    zone=zone,
                    project_id=project_id,
                    datacenter_name=datacenter_name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Service(res.json())

    async def subscribe_storage_options(
        self,
        *,
        server_id: int,
        options_ids: List[int],
        zone: Optional[Zone] = None,
    ) -> SubscribeStorageOptionsResponse:
        """
        Subscribe storage server option.
        Subscribe storage option for the given server ID.
        :param server_id: Server ID of the storage options to subscribe.
        :param options_ids: Option IDs of the storage options to subscribe.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`SubscribeStorageOptionsResponse <SubscribeStorageOptionsResponse>`

        Usage:
        ::

            result = await api.subscribe_storage_options(
                server_id=1,
                options_ids=[],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/subscribe-storage-options",
            body=marshal_SubscribeStorageOptionsRequest(
                SubscribeStorageOptionsRequest(
                    server_id=server_id,
                    options_ids=options_ids,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SubscribeStorageOptionsResponse(res.json())

    async def update_server(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
        hostname: Optional[str] = None,
        enable_ipv6: Optional[bool] = None,
    ) -> Server:
        """
        Update a baremetal server.
        Update the server associated with the given ID.
        :param server_id: Server ID to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param hostname: Hostname of the server to update.
        :param enable_ipv6: Flag to enable or not the IPv6 of server.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.update_server(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "PATCH",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}",
            body=marshal_UpdateServerRequest(
                UpdateServerRequest(
                    server_id=server_id,
                    zone=zone,
                    hostname=hostname,
                    enable_ipv6=enable_ipv6,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def update_server_tags(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
        tags: Optional[List[str]] = None,
    ) -> Server:
        """
        :param server_id: Server ID to update the tags.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param tags: Tags of server to update.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.update_server_tags(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/tags",
            body=marshal_UpdateServerTagsRequest(
                UpdateServerTagsRequest(
                    server_id=server_id,
                    zone=zone,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def reboot_server(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Reboot a baremetal server.
        Reboot the server associated with the given ID, use boot param to reboot in rescue.
        :param server_id: Server ID to reboot.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.reboot_server(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/reboot",
            body={},
        )

        self._throw_on_error(res)

    async def start_server(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Start a baremetal server.
        Start the server associated with the given ID.
        :param server_id: Server ID to start.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.start_server(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/start",
            body={},
        )

        self._throw_on_error(res)

    async def stop_server(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Stop a baremetal server.
        Stop the server associated with the given ID.
        :param server_id: Server ID to stop.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.stop_server(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/stop",
            body={},
        )

        self._throw_on_error(res)

    async def delete_server(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a baremetal server.
        Delete the server associated with the given ID.
        :param server_id: Server ID to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_server(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "DELETE",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}",
        )

        self._throw_on_error(res)

    async def list_server_events(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListServerEventsRequestOrderBy] = None,
    ) -> ListServerEventsResponse:
        """
        List server events.
        List events associated to the given server ID.
        :param server_id: Server ID of the server events.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of server event per page.
        :param order_by: Order of the server events.
        :return: :class:`ListServerEventsResponse <ListServerEventsResponse>`

        Usage:
        ::

            result = await api.list_server_events(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/events",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServerEventsResponse(res.json())

    async def list_server_events_all(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListServerEventsRequestOrderBy] = None,
    ) -> List[ServerEvent]:
        """
        List server events.
        List events associated to the given server ID.
        :param server_id: Server ID of the server events.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of server event per page.
        :param order_by: Order of the server events.
        :return: :class:`List[ServerEvent] <List[ServerEvent]>`

        Usage:
        ::

            result = await api.list_server_events_all(
                server_id=1,
            )
        """

        return await fetch_all_pages_async(
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

    async def list_server_disks(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListServerDisksRequestOrderBy] = None,
    ) -> ListServerDisksResponse:
        """
        List server disks.
        List disks associated to the given server ID.
        :param server_id: Server ID of the server disks.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of server disk per page.
        :param order_by: Order of the server disks.
        :return: :class:`ListServerDisksResponse <ListServerDisksResponse>`

        Usage:
        ::

            result = await api.list_server_disks(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/disks",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServerDisksResponse(res.json())

    async def list_server_disks_all(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListServerDisksRequestOrderBy] = None,
    ) -> List[ServerDisk]:
        """
        List server disks.
        List disks associated to the given server ID.
        :param server_id: Server ID of the server disks.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of server disk per page.
        :param order_by: Order of the server disks.
        :return: :class:`List[ServerDisk] <List[ServerDisk]>`

        Usage:
        ::

            result = await api.list_server_disks_all(
                server_id=1,
            )
        """

        return await fetch_all_pages_async(
            type=ListServerDisksResponse,
            key="disks",
            fetcher=self.list_server_disks,
            args={
                "server_id": server_id,
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def get_ordered_service(
        self,
        *,
        ordered_service_id: int,
        zone: Optional[Zone] = None,
    ) -> Service:
        """
        :param ordered_service_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Service <Service>`

        Usage:
        ::

            result = await api.get_ordered_service(
                ordered_service_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ordered_service_id = validate_path_param(
            "ordered_service_id", ordered_service_id
        )

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/ordered-services/{param_ordered_service_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Service(res.json())

    async def get_service(
        self,
        *,
        service_id: int,
        zone: Optional[Zone] = None,
    ) -> Service:
        """
        Get a specific service.
        Get the service associated with the given ID.
        :param service_id: ID of the service.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Service <Service>`

        Usage:
        ::

            result = await api.get_service(
                service_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_service_id = validate_path_param("service_id", service_id)

        res = self._request(
            "PATCH",
            f"/dedibox/v1/zones/{param_zone}/services/{param_service_id}",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Service(res.json())

    async def delete_service(
        self,
        *,
        service_id: int,
        zone: Optional[Zone] = None,
    ) -> Service:
        """
        Delete a specific service.
        Delete the service associated with the given ID.
        :param service_id: ID of the service.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Service <Service>`

        Usage:
        ::

            result = await api.delete_service(
                service_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_service_id = validate_path_param("service_id", service_id)

        res = self._request(
            "DELETE",
            f"/dedibox/v1/zones/{param_zone}/services/{param_service_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Service(res.json())

    async def list_services(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListServicesRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListServicesResponse:
        """
        List services.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of service per page.
        :param order_by: Order of the services.
        :param project_id: Project ID.
        :return: :class:`ListServicesResponse <ListServicesResponse>`

        Usage:
        ::

            result = await api.list_services()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/services",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServicesResponse(res.json())

    async def list_services_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListServicesRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[Service]:
        """
        List services.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of service per page.
        :param order_by: Order of the services.
        :param project_id: Project ID.
        :return: :class:`List[Service] <List[Service]>`

        Usage:
        ::

            result = await api.list_services_all()
        """

        return await fetch_all_pages_async(
            type=ListServicesResponse,
            key="services",
            fetcher=self.list_services,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def install_server(
        self,
        *,
        server_id: int,
        os_id: int,
        hostname: str,
        zone: Optional[Zone] = None,
        user_login: Optional[str] = None,
        user_password: Optional[str] = None,
        panel_password: Optional[str] = None,
        root_password: Optional[str] = None,
        partitions: Optional[List[InstallPartition]] = None,
        ssh_key_ids: Optional[List[str]] = None,
        license_offer_id: Optional[int] = None,
        ip_id: Optional[int] = None,
    ) -> ServerInstall:
        """
        Install a baremetal server.
        Install an OS on the server associated with the given ID.
        :param server_id: Server ID to install.
        :param os_id: OS ID to install on the server.
        :param hostname: Hostname of the server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param user_login: User to install on the server.
        :param user_password: User password to install on the server.
        :param panel_password: Panel password to install on the server.
        :param root_password: Root password to install on the server.
        :param partitions: Partitions to install on the server.
        :param ssh_key_ids: SSH key IDs authorized on the server.
        :param license_offer_id: Offer ID of license to install on server.
        :param ip_id: IP to link at the license to install on server.
        :return: :class:`ServerInstall <ServerInstall>`

        Usage:
        ::

            result = await api.install_server(
                server_id=1,
                os_id=1,
                hostname="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/install",
            body=marshal_InstallServerRequest(
                InstallServerRequest(
                    server_id=server_id,
                    os_id=os_id,
                    hostname=hostname,
                    zone=zone,
                    user_login=user_login,
                    user_password=user_password,
                    panel_password=panel_password,
                    root_password=root_password,
                    partitions=partitions,
                    ssh_key_ids=ssh_key_ids,
                    license_offer_id=license_offer_id,
                    ip_id=ip_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ServerInstall(res.json())

    async def get_server_install(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
    ) -> ServerInstall:
        """
        Get a specific server installation status.
        Get the server installation status associated with the given server ID.
        :param server_id: Server ID of the server to install.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ServerInstall <ServerInstall>`

        Usage:
        ::

            result = await api.get_server_install(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/install",
        )

        self._throw_on_error(res)
        return unmarshal_ServerInstall(res.json())

    async def wait_for_server_install(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
        options: Optional[
            WaitForOptions[ServerInstall, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> ServerInstall:
        """
        Get a specific server installation status.
        Get the server installation status associated with the given server ID.
        :param server_id: Server ID of the server to install.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ServerInstall <ServerInstall>`

        Usage:
        ::

            result = await api.get_server_install(
                server_id=1,
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = (
                lambda res: res.status not in SERVER_INSTALL_TRANSIENT_STATUSES
            )

        return await wait_for_resource_async(
            fetcher=self.get_server_install,
            options=options,
            args={
                "server_id": server_id,
                "zone": zone,
            },
        )

    async def cancel_server_install(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Cancels the current (running) server installation.
        Cancels the current server installation associated with the given server ID.
        :param server_id: Server ID of the server to cancel install.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.cancel_server_install(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/cancel-install",
        )

        self._throw_on_error(res)

    async def get_server_default_partitioning(
        self,
        *,
        server_id: int,
        os_id: int,
        zone: Optional[Zone] = None,
    ) -> ServerDefaultPartitioning:
        """
        Get server default partitioning.
        Get the server default partitioning schema associated with the given server ID and OS ID.
        :param server_id: ID of the server.
        :param os_id: OS ID of the default partitioning.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ServerDefaultPartitioning <ServerDefaultPartitioning>`

        Usage:
        ::

            result = await api.get_server_default_partitioning(
                server_id=1,
                os_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_os_id = validate_path_param("os_id", os_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/partitioning/{param_os_id}",
        )

        self._throw_on_error(res)
        return unmarshal_ServerDefaultPartitioning(res.json())

    async def start_bmc_access(
        self,
        *,
        server_id: int,
        ip: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Start BMC (Baseboard Management Controller) access for a given baremetal server.
        Start BMC (Baseboard Management Controller) access associated with the given ID.
        The BMC (Baseboard Management Controller) access is available one hour after the installation of the server.
        :param server_id: ID of the server to start the BMC access.
        :param ip: The IP authorized to connect to the given server.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.start_bmc_access(
                server_id=1,
                ip="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/bmc-access",
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

    async def get_bmc_access(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
    ) -> BMCAccess:
        """
        Get BMC (Baseboard Management Controller) access for a given baremetal server.
        Get the BMC (Baseboard Management Controller) access associated with the given ID.
        :param server_id: ID of the server to get BMC access.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`BMCAccess <BMCAccess>`

        Usage:
        ::

            result = await api.get_bmc_access(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/bmc-access",
        )

        self._throw_on_error(res)
        return unmarshal_BMCAccess(res.json())

    async def wait_for_bmc_access(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
        options: Optional[
            WaitForOptions[BMCAccess, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> BMCAccess:
        """
        Get BMC (Baseboard Management Controller) access for a given baremetal server.
        Get the BMC (Baseboard Management Controller) access associated with the given ID.
        :param server_id: ID of the server to get BMC access.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`BMCAccess <BMCAccess>`

        Usage:
        ::

            result = await api.get_bmc_access(
                server_id=1,
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in BMC_ACCESS_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_bmc_access,
            options=options,
            args={
                "server_id": server_id,
                "zone": zone,
            },
        )

    async def stop_bmc_access(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Stop BMC (Baseboard Management Controller) access for a given baremetal server.
        Stop BMC (Baseboard Management Controller) access associated with the given ID.
        :param server_id: ID of the server to stop BMC access.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.stop_bmc_access(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "DELETE",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/bmc-access",
        )

        self._throw_on_error(res)

    async def list_offers(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListOffersRequestOrderBy] = None,
        commercial_range: Optional[str] = None,
        catalog: Optional[OfferCatalog] = None,
        project_id: Optional[str] = None,
        is_failover_ip: Optional[bool] = None,
        is_failover_block: Optional[bool] = None,
        sold_in: Optional[List[str]] = None,
        available_only: Optional[bool] = None,
        is_rpn_san: Optional[bool] = None,
    ) -> ListOffersResponse:
        """
        List offers.
        List all available server offers.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of offer per page.
        :param order_by: Order of the offers.
        :param commercial_range: Filter on commercial range.
        :param catalog: Filter on catalog.
        :param project_id: Project ID.
        :param is_failover_ip: Get the current failover IP offer.
        :param is_failover_block: Get the current failover IP block offer.
        :param sold_in: Filter offers depending on their datacenter.
        :param available_only: Set this filter to true to only return available offers.
        :param is_rpn_san: Get the RPN SAN offers.
        :return: :class:`ListOffersResponse <ListOffersResponse>`

        Usage:
        ::

            result = await api.list_offers()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/offers",
            params={
                "available_only": available_only,
                "catalog": catalog,
                "commercial_range": commercial_range,
                "is_failover_block": is_failover_block,
                "is_failover_ip": is_failover_ip,
                "is_rpn_san": is_rpn_san,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "sold_in": ",".join(sold_in) if sold_in and len(sold_in) > 0 else None,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOffersResponse(res.json())

    async def list_offers_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListOffersRequestOrderBy] = None,
        commercial_range: Optional[str] = None,
        catalog: Optional[OfferCatalog] = None,
        project_id: Optional[str] = None,
        is_failover_ip: Optional[bool] = None,
        is_failover_block: Optional[bool] = None,
        sold_in: Optional[List[str]] = None,
        available_only: Optional[bool] = None,
        is_rpn_san: Optional[bool] = None,
    ) -> List[Offer]:
        """
        List offers.
        List all available server offers.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of offer per page.
        :param order_by: Order of the offers.
        :param commercial_range: Filter on commercial range.
        :param catalog: Filter on catalog.
        :param project_id: Project ID.
        :param is_failover_ip: Get the current failover IP offer.
        :param is_failover_block: Get the current failover IP block offer.
        :param sold_in: Filter offers depending on their datacenter.
        :param available_only: Set this filter to true to only return available offers.
        :param is_rpn_san: Get the RPN SAN offers.
        :return: :class:`List[Offer] <List[Offer]>`

        Usage:
        ::

            result = await api.list_offers_all()
        """

        return await fetch_all_pages_async(
            type=ListOffersResponse,
            key="offers",
            fetcher=self.list_offers,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "commercial_range": commercial_range,
                "catalog": catalog,
                "project_id": project_id,
                "is_failover_ip": is_failover_ip,
                "is_failover_block": is_failover_block,
                "sold_in": sold_in,
                "available_only": available_only,
                "is_rpn_san": is_rpn_san,
            },
        )

    async def get_offer(
        self,
        *,
        offer_id: int,
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
    ) -> Offer:
        """
        Get offer.
        Return specific offer for the given ID.
        :param offer_id: ID of offer.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID.
        :return: :class:`Offer <Offer>`

        Usage:
        ::

            result = await api.get_offer(
                offer_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_offer_id = validate_path_param("offer_id", offer_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/offers/{param_offer_id}",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_Offer(res.json())

    async def list_os(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListOSRequestOrderBy] = None,
        type_: Optional[OSType] = None,
        project_id: Optional[str] = None,
    ) -> ListOSResponse:
        """
        List all available OS that can be install on a baremetal server.
        :param server_id: Filter OS by compatible server ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of OS per page.
        :param order_by: Order of the OS.
        :param type_: Type of the OS.
        :param project_id: Project ID.
        :return: :class:`ListOSResponse <ListOSResponse>`

        Usage:
        ::

            result = await api.list_os(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/os",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "server_id": server_id,
                "type": type_,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOSResponse(res.json())

    async def list_os_all(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListOSRequestOrderBy] = None,
        type_: Optional[OSType] = None,
        project_id: Optional[str] = None,
    ) -> List[OS]:
        """
        List all available OS that can be install on a baremetal server.
        :param server_id: Filter OS by compatible server ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of OS per page.
        :param order_by: Order of the OS.
        :param type_: Type of the OS.
        :param project_id: Project ID.
        :return: :class:`List[OS] <List[OS]>`

        Usage:
        ::

            result = await api.list_os_all(
                server_id=1,
            )
        """

        return await fetch_all_pages_async(
            type=ListOSResponse,
            key="os",
            fetcher=self.list_os,
            args={
                "server_id": server_id,
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "type_": type_,
                "project_id": project_id,
            },
        )

    async def get_os(
        self,
        *,
        os_id: int,
        server_id: int,
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
    ) -> OS:
        """
        Get an OS with a given ID.
        Return specific OS for the given ID.
        :param os_id: ID of the OS.
        :param server_id: ID of the server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID.
        :return: :class:`OS <OS>`

        Usage:
        ::

            result = await api.get_os(
                os_id=1,
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_os_id = validate_path_param("os_id", os_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/os/{param_os_id}",
            params={
                "project_id": project_id or self.client.default_project_id,
                "server_id": server_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_OS(res.json())

    async def update_reverse(
        self,
        *,
        ip_id: int,
        reverse: str,
        zone: Optional[Zone] = None,
    ) -> IP:
        """
        Update reverse of ip.
        Update reverse of ip associated with the given ID.
        :param ip_id: ID of the IP.
        :param reverse: Reverse to apply on the IP.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = await api.update_reverse(
                ip_id=1,
                reverse="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "PATCH",
            f"/dedibox/v1/zones/{param_zone}/reverses/{param_ip_id}",
            body=marshal_UpdateReverseRequest(
                UpdateReverseRequest(
                    ip_id=ip_id,
                    reverse=reverse,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    async def create_failover_i_ps(
        self,
        *,
        offer_id: int,
        quantity: int,
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
    ) -> CreateFailoverIPsResponse:
        """
        Order failover IPs.
        Order X failover IPs.
        :param offer_id: Failover IP offer ID.
        :param quantity: Quantity.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID.
        :return: :class:`CreateFailoverIPsResponse <CreateFailoverIPsResponse>`

        Usage:
        ::

            result = await api.create_failover_i_ps(
                offer_id=1,
                quantity=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/failover-ips",
            body=marshal_CreateFailoverIPsRequest(
                CreateFailoverIPsRequest(
                    offer_id=offer_id,
                    quantity=quantity,
                    zone=zone,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateFailoverIPsResponse(res.json())

    async def attach_failover_i_ps(
        self,
        *,
        server_id: int,
        fips_ids: List[int],
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Attach failovers on baremetal server.
        Attach failovers on the server associated with the given ID.
        :param server_id: ID of the server.
        :param fips_ids: List of ID of failovers IP to attach.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.attach_failover_i_ps(
                server_id=1,
                fips_ids=[],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/failover-ips/attach",
            body=marshal_AttachFailoverIPsRequest(
                AttachFailoverIPsRequest(
                    server_id=server_id,
                    fips_ids=fips_ids,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def detach_failover_i_ps(
        self,
        *,
        fips_ids: List[int],
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Detach failovers on baremetal server.
        Detach failovers on the server associated with the given ID.
        :param fips_ids: List of IDs of failovers IP to detach.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.detach_failover_i_ps(
                fips_ids=[],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/failover-ips/detach",
            body=marshal_DetachFailoverIPsRequest(
                DetachFailoverIPsRequest(
                    fips_ids=fips_ids,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def attach_failover_ip_to_mac_address(
        self,
        *,
        ip_id: int,
        zone: Optional[Zone] = None,
        type_: Optional[AttachFailoverIPToMacAddressRequestMacType] = None,
        mac: Optional[str] = None,
    ) -> IP:
        """
        Attach a failover IP to a MAC address.
        :param ip_id: ID of the failover IP.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param type_: A mac type.
        :param mac: A valid mac address (existing or not).
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = await api.attach_failover_ip_to_mac_address(
                ip_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/failover-ips/{param_ip_id}/attach-to-mac-address",
            body=marshal_AttachFailoverIPToMacAddressRequest(
                AttachFailoverIPToMacAddressRequest(
                    ip_id=ip_id,
                    zone=zone,
                    type_=type_,
                    mac=mac,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    async def detach_failover_ip_from_mac_address(
        self,
        *,
        ip_id: int,
        zone: Optional[Zone] = None,
    ) -> IP:
        """
        Detach a failover IP from a MAC address.
        :param ip_id: ID of the failover IP.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = await api.detach_failover_ip_from_mac_address(
                ip_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/failover-ips/{param_ip_id}/detach-from-mac-address",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    async def delete_failover_ip(
        self,
        *,
        ip_id: int,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a failover server.
        Delete the failover associated with the given ID.
        :param ip_id: ID of the failover IP to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_failover_ip(
                ip_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "DELETE",
            f"/dedibox/v1/zones/{param_zone}/failover-ips/{param_ip_id}",
        )

        self._throw_on_error(res)

    async def list_failover_i_ps(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListFailoverIPsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        search: Optional[str] = None,
        only_available: Optional[bool] = None,
    ) -> ListFailoverIPsResponse:
        """
        List failovers for project.
        List failovers servers for project.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of failovers IP per page.
        :param order_by: Order of the failovers IP.
        :param project_id: Filter failovers IP by project ID.
        :param search: Filter failovers IP which matching with this field.
        :param only_available: True: return all failovers IP not attached on server
        false: return all failovers IP attached on server.
        :return: :class:`ListFailoverIPsResponse <ListFailoverIPsResponse>`

        Usage:
        ::

            result = await api.list_failover_i_ps()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/failover-ips",
            params={
                "only_available": only_available,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "search": search,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListFailoverIPsResponse(res.json())

    async def list_failover_i_ps_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListFailoverIPsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        search: Optional[str] = None,
        only_available: Optional[bool] = None,
    ) -> List[FailoverIP]:
        """
        List failovers for project.
        List failovers servers for project.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of failovers IP per page.
        :param order_by: Order of the failovers IP.
        :param project_id: Filter failovers IP by project ID.
        :param search: Filter failovers IP which matching with this field.
        :param only_available: True: return all failovers IP not attached on server
        false: return all failovers IP attached on server.
        :return: :class:`List[FailoverIP] <List[FailoverIP]>`

        Usage:
        ::

            result = await api.list_failover_i_ps_all()
        """

        return await fetch_all_pages_async(
            type=ListFailoverIPsResponse,
            key="failover_ips",
            fetcher=self.list_failover_i_ps,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
                "search": search,
                "only_available": only_available,
            },
        )

    async def get_failover_ip(
        self,
        *,
        ip_id: int,
        zone: Optional[Zone] = None,
    ) -> FailoverIP:
        """
        Get a specific baremetal server.
        Get the server associated with the given ID.
        :param ip_id: ID of the failover IP.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`FailoverIP <FailoverIP>`

        Usage:
        ::

            result = await api.get_failover_ip(
                ip_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/failover-ips/{param_ip_id}",
        )

        self._throw_on_error(res)
        return unmarshal_FailoverIP(res.json())

    async def get_remaining_quota(
        self,
        *,
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
    ) -> GetRemainingQuotaResponse:
        """
        Get remaining quota.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID.
        :return: :class:`GetRemainingQuotaResponse <GetRemainingQuotaResponse>`

        Usage:
        ::

            result = await api.get_remaining_quota()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/remaining-quota",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GetRemainingQuotaResponse(res.json())

    async def get_raid(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
    ) -> Raid:
        """
        Get raid.
        Return raid for the given server ID.
        :param server_id: ID of the server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Raid <Raid>`

        Usage:
        ::

            result = await api.get_raid(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/raid",
        )

        self._throw_on_error(res)
        return unmarshal_Raid(res.json())

    async def update_raid(
        self,
        *,
        server_id: int,
        raid_arrays: List[UpdatableRaidArray],
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Update RAID.
        Update RAID associated with the given server ID.
        :param server_id: ID of the server.
        :param raid_arrays: RAIDs to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.update_raid(
                server_id=1,
                raid_arrays=[],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/update-raid",
            body=marshal_UpdateRaidRequest(
                UpdateRaidRequest(
                    server_id=server_id,
                    raid_arrays=raid_arrays,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def start_rescue(
        self,
        *,
        server_id: int,
        os_id: int,
        zone: Optional[Zone] = None,
    ) -> Rescue:
        """
        Start in rescue baremetal server.
        Start in rescue the server associated with the given ID.
        :param server_id: ID of the server to start rescue.
        :param os_id: OS ID to use to start rescue.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Rescue <Rescue>`

        Usage:
        ::

            result = await api.start_rescue(
                server_id=1,
                os_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/rescue",
            body=marshal_StartRescueRequest(
                StartRescueRequest(
                    server_id=server_id,
                    os_id=os_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Rescue(res.json())

    async def get_rescue(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
    ) -> Rescue:
        """
        Get rescue information.
        Return rescue information for the given server ID.
        :param server_id: ID of the server to get rescue.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Rescue <Rescue>`

        Usage:
        ::

            result = await api.get_rescue(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/rescue",
        )

        self._throw_on_error(res)
        return unmarshal_Rescue(res.json())

    async def stop_rescue(
        self,
        *,
        server_id: int,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Stop rescue on baremetal server.
        Stop rescue on the server associated with the given ID.
        :param server_id: ID of the server to stop rescue.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.stop_rescue(
                server_id=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "DELETE",
            f"/dedibox/v1/zones/{param_zone}/servers/{param_server_id}/rescue",
        )

        self._throw_on_error(res)


class DediboxV1BillingAPI(API):
    """
    Dedibox Phoenix Billing API.
    """

    async def list_invoices(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListInvoicesRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListInvoicesResponse:
        """
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :return: :class:`ListInvoicesResponse <ListInvoicesResponse>`

        Usage:
        ::

            result = await api.list_invoices()
        """

        res = self._request(
            "GET",
            "/dedibox/v1/invoices",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListInvoicesResponse(res.json())

    async def list_invoices_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListInvoicesRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[InvoiceSummary]:
        """
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :return: :class:`List[InvoiceSummary] <List[InvoiceSummary]>`

        Usage:
        ::

            result = await api.list_invoices_all()
        """

        return await fetch_all_pages_async(
            type=ListInvoicesResponse,
            key="invoices",
            fetcher=self.list_invoices,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def get_invoice(
        self,
        *,
        invoice_id: int,
    ) -> Invoice:
        """
        :param invoice_id:
        :return: :class:`Invoice <Invoice>`

        Usage:
        ::

            result = await api.get_invoice(
                invoice_id=1,
            )
        """

        param_invoice_id = validate_path_param("invoice_id", invoice_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/invoices/{param_invoice_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Invoice(res.json())

    async def download_invoice(
        self,
        *,
        invoice_id: int,
    ) -> ScwFile:
        """
        :param invoice_id:
        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = await api.download_invoice(
                invoice_id=1,
            )
        """

        param_invoice_id = validate_path_param("invoice_id", invoice_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/invoices/{param_invoice_id}/download",
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())

    async def list_refunds(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRefundsRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListRefundsResponse:
        """
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :return: :class:`ListRefundsResponse <ListRefundsResponse>`

        Usage:
        ::

            result = await api.list_refunds()
        """

        res = self._request(
            "GET",
            "/dedibox/v1/refunds",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRefundsResponse(res.json())

    async def list_refunds_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRefundsRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[RefundSummary]:
        """
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :return: :class:`List[RefundSummary] <List[RefundSummary]>`

        Usage:
        ::

            result = await api.list_refunds_all()
        """

        return await fetch_all_pages_async(
            type=ListRefundsResponse,
            key="refunds",
            fetcher=self.list_refunds,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def get_refund(
        self,
        *,
        refund_id: int,
    ) -> Refund:
        """
        :param refund_id:
        :return: :class:`Refund <Refund>`

        Usage:
        ::

            result = await api.get_refund(
                refund_id=1,
            )
        """

        param_refund_id = validate_path_param("refund_id", refund_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/refunds/{param_refund_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Refund(res.json())

    async def download_refund(
        self,
        *,
        refund_id: int,
    ) -> ScwFile:
        """
        :param refund_id:
        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = await api.download_refund(
                refund_id=1,
            )
        """

        param_refund_id = validate_path_param("refund_id", refund_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/refunds/{param_refund_id}/download",
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())

    async def can_order(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> CanOrderResponse:
        """
        :param project_id:
        :return: :class:`CanOrderResponse <CanOrderResponse>`

        Usage:
        ::

            result = await api.can_order()
        """

        res = self._request(
            "GET",
            "/dedibox/v1/can-order",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_CanOrderResponse(res.json())


class DediboxV1IPv6BlockAPI(API):
    """
    Dedibox Phoenix IPv6 Block API.
    """

    async def get_i_pv6_block_quotas(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> GetIPv6BlockQuotasResponse:
        """
        Get IPv6 block quota.
        Get IPv6 block quota with the given project ID.
        /48 one per organization.
        /56 link to your number of server.
        /64 link to your number of failover IP.
        :param project_id: ID of the project.
        :return: :class:`GetIPv6BlockQuotasResponse <GetIPv6BlockQuotasResponse>`

        Usage:
        ::

            result = await api.get_i_pv6_block_quotas()
        """

        res = self._request(
            "GET",
            "/dedibox/v1/ipv6-block-quotas",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GetIPv6BlockQuotasResponse(res.json())

    async def create_i_pv6_block(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> IPv6Block:
        """
        Create IPv6 block for baremetal server.
        Create IPv6 block associated with the given project ID.
        :param project_id: ID of the project.
        :return: :class:`IPv6Block <IPv6Block>`

        Usage:
        ::

            result = await api.create_i_pv6_block()
        """

        res = self._request(
            "POST",
            "/dedibox/v1/ipv6-block",
            body=marshal_IPv6BlockApiCreateIPv6BlockRequest(
                IPv6BlockApiCreateIPv6BlockRequest(
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IPv6Block(res.json())

    async def get_i_pv6_block(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> IPv6Block:
        """
        Get a specific IPv6 block.
        Get the IPv6 block associated with the given ID.
        :param project_id: ID of the project.
        :return: :class:`IPv6Block <IPv6Block>`

        Usage:
        ::

            result = await api.get_i_pv6_block()
        """

        res = self._request(
            "GET",
            "/dedibox/v1/ipv6-block",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_IPv6Block(res.json())

    async def update_i_pv6_block(
        self,
        *,
        block_id: int,
        nameservers: Optional[List[str]] = None,
    ) -> IPv6Block:
        """
        Update IPv6 block.
        Update DNS associated to IPv6 block.
        If DNS is used, minimum of 2 is necessary and maximum of 5 (no duplicate).
        :param block_id: ID of the IPv6 block.
        :param nameservers: DNS to link to the IPv6.
        :return: :class:`IPv6Block <IPv6Block>`

        Usage:
        ::

            result = await api.update_i_pv6_block(
                block_id=1,
            )
        """

        param_block_id = validate_path_param("block_id", block_id)

        res = self._request(
            "PATCH",
            f"/dedibox/v1/ipv6-blocks/{param_block_id}",
            body=marshal_IPv6BlockApiUpdateIPv6BlockRequest(
                IPv6BlockApiUpdateIPv6BlockRequest(
                    block_id=block_id,
                    nameservers=nameservers,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IPv6Block(res.json())

    async def delete_i_pv6_block(
        self,
        *,
        block_id: int,
    ) -> None:
        """
        Delete IPv6 block.
        Delete IPv6 block subnet with the given ID.
        :param block_id: ID of the IPv6 block to delete.

        Usage:
        ::

            result = await api.delete_i_pv6_block(
                block_id=1,
            )
        """

        param_block_id = validate_path_param("block_id", block_id)

        res = self._request(
            "DELETE",
            f"/dedibox/v1/ipv6-blocks/{param_block_id}",
        )

        self._throw_on_error(res)

    async def create_i_pv6_block_subnet(
        self,
        *,
        block_id: int,
        address: str,
        cidr: int,
    ) -> IPv6Block:
        """
        Create IPv6 block subnet.
        Create IPv6 block subnet for the given IP ID.
        /48 could create subnet in /56 (quota link to your number of server).
        /56 could create subnet in /64 (quota link to your number of failover IP).
        :param block_id: ID of the IPv6 block.
        :param address: Address of the IPv6.
        :param cidr: Classless InterDomain Routing notation of the IPv6.
        :return: :class:`IPv6Block <IPv6Block>`

        Usage:
        ::

            result = await api.create_i_pv6_block_subnet(
                block_id=1,
                address="example",
                cidr=1,
            )
        """

        param_block_id = validate_path_param("block_id", block_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/ipv6-blocks/{param_block_id}/subnets",
            body=marshal_IPv6BlockApiCreateIPv6BlockSubnetRequest(
                IPv6BlockApiCreateIPv6BlockSubnetRequest(
                    block_id=block_id,
                    address=address,
                    cidr=cidr,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IPv6Block(res.json())

    async def list_i_pv6_block_subnets_available(
        self,
        *,
        block_id: int,
    ) -> ListIPv6BlockSubnetsAvailableResponse:
        """
        List available IPv6 block subnets.
        List all available IPv6 block subnets for given IP ID.
        :param block_id: ID of the IPv6 block.
        :return: :class:`ListIPv6BlockSubnetsAvailableResponse <ListIPv6BlockSubnetsAvailableResponse>`

        Usage:
        ::

            result = await api.list_i_pv6_block_subnets_available(
                block_id=1,
            )
        """

        param_block_id = validate_path_param("block_id", block_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/ipv6-blocks/{param_block_id}/subnets",
        )

        self._throw_on_error(res)
        return unmarshal_ListIPv6BlockSubnetsAvailableResponse(res.json())


class DediboxV1RpnAPI(API):
    """
    Dedibox Phoenix RPN API.
    """

    async def list_rpn_server_capabilities(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnServerCapabilitiesRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListRpnServerCapabilitiesResponse:
        """
        :param page: Page number.
        :param page_size: Number of servers per page.
        :param order_by: Order of the servers.
        :param project_id: Filter servers by project ID.
        :return: :class:`ListRpnServerCapabilitiesResponse <ListRpnServerCapabilitiesResponse>`

        Usage:
        ::

            result = await api.list_rpn_server_capabilities()
        """

        res = self._request(
            "GET",
            "/dedibox/v1/rpn/server-capabilities",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRpnServerCapabilitiesResponse(res.json())

    async def list_rpn_server_capabilities_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnServerCapabilitiesRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[RpnServerCapability]:
        """
        :param page: Page number.
        :param page_size: Number of servers per page.
        :param order_by: Order of the servers.
        :param project_id: Filter servers by project ID.
        :return: :class:`List[RpnServerCapability] <List[RpnServerCapability]>`

        Usage:
        ::

            result = await api.list_rpn_server_capabilities_all()
        """

        return await fetch_all_pages_async(
            type=ListRpnServerCapabilitiesResponse,
            key="servers",
            fetcher=self.list_rpn_server_capabilities,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def get_rpn_status(
        self,
        *,
        project_id: Optional[str] = None,
        rpnv1_group_id: Optional[int] = None,
        rpnv2_group_id: Optional[int] = None,
    ) -> GetRpnStatusResponse:
        """
        :param project_id: A project ID.
        :param rpnv1_group_id: An RPN v1 group ID.
        :param rpnv2_group_id: An RPN v2 group ID.
        :return: :class:`GetRpnStatusResponse <GetRpnStatusResponse>`

        Usage:
        ::

            result = await api.get_rpn_status()
        """

        res = self._request(
            "GET",
            "/dedibox/v1/rpn/status",
            params={
                "project_id": project_id or self.client.default_project_id,
                "rpnv1_group_id": rpnv1_group_id,
                "rpnv2_group_id": rpnv2_group_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GetRpnStatusResponse(res.json())


class DediboxV1RpnSanAPI(API):
    """
    Dedibox Phoenix RPN SAN API.
    """

    async def list_rpn_sans(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnSansRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListRpnSansResponse:
        """
        :param page: Page number.
        :param page_size: Number of RPN SANs per page.
        :param order_by: Order of the RPN SANs.
        :param project_id: Filter RPN SANs by project ID.
        :return: :class:`ListRpnSansResponse <ListRpnSansResponse>`

        Usage:
        ::

            result = await api.list_rpn_sans()
        """

        res = self._request(
            "GET",
            "/dedibox/v1/rpn-sans",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRpnSansResponse(res.json())

    async def list_rpn_sans_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnSansRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[RpnSanSummary]:
        """
        :param page: Page number.
        :param page_size: Number of RPN SANs per page.
        :param order_by: Order of the RPN SANs.
        :param project_id: Filter RPN SANs by project ID.
        :return: :class:`List[RpnSanSummary] <List[RpnSanSummary]>`

        Usage:
        ::

            result = await api.list_rpn_sans_all()
        """

        return await fetch_all_pages_async(
            type=ListRpnSansResponse,
            key="rpn_sans",
            fetcher=self.list_rpn_sans,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def get_rpn_san(
        self,
        *,
        rpn_san_id: int,
    ) -> RpnSan:
        """
        :param rpn_san_id: RPN SAN ID.
        :return: :class:`RpnSan <RpnSan>`

        Usage:
        ::

            result = await api.get_rpn_san(
                rpn_san_id=1,
            )
        """

        param_rpn_san_id = validate_path_param("rpn_san_id", rpn_san_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/rpn-sans/{param_rpn_san_id}",
        )

        self._throw_on_error(res)
        return unmarshal_RpnSan(res.json())

    async def wait_for_rpn_san(
        self,
        *,
        rpn_san_id: int,
        options: Optional[WaitForOptions[RpnSan, Union[bool, Awaitable[bool]]]] = None,
    ) -> RpnSan:
        """
        :param rpn_san_id: RPN SAN ID.
        :return: :class:`RpnSan <RpnSan>`

        Usage:
        ::

            result = await api.get_rpn_san(
                rpn_san_id=1,
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in RPN_SAN_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_rpn_san,
            options=options,
            args={
                "rpn_san_id": rpn_san_id,
            },
        )

    async def delete_rpn_san(
        self,
        *,
        rpn_san_id: int,
    ) -> None:
        """
        :param rpn_san_id: RPN SAN ID.

        Usage:
        ::

            result = await api.delete_rpn_san(
                rpn_san_id=1,
            )
        """

        param_rpn_san_id = validate_path_param("rpn_san_id", rpn_san_id)

        res = self._request(
            "DELETE",
            f"/dedibox/v1/rpn-sans/{param_rpn_san_id}",
        )

        self._throw_on_error(res)

    async def create_rpn_san(
        self,
        *,
        offer_id: int,
        project_id: Optional[str] = None,
    ) -> Service:
        """
        :param offer_id: Offer ID.
        :param project_id: Your project ID.
        :return: :class:`Service <Service>`

        Usage:
        ::

            result = await api.create_rpn_san(
                offer_id=1,
            )
        """

        res = self._request(
            "POST",
            "/dedibox/v1/rpn-sans",
            body=marshal_RpnSanApiCreateRpnSanRequest(
                RpnSanApiCreateRpnSanRequest(
                    offer_id=offer_id,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Service(res.json())

    async def list_ips(
        self,
        *,
        rpn_san_id: int,
        type_: Optional[RpnSanIpType] = None,
    ) -> ListIpsResponse:
        """
        :param rpn_san_id: RPN SAN ID.
        :param type_: Filter by IP type (server | rpnv2_subnet).
        :return: :class:`ListIpsResponse <ListIpsResponse>`

        Usage:
        ::

            result = await api.list_ips(
                rpn_san_id=1,
            )
        """

        param_rpn_san_id = validate_path_param("rpn_san_id", rpn_san_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/rpn-sans/{param_rpn_san_id}/ips",
            params={
                "type": type_,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListIpsResponse(res.json())

    async def add_ip(
        self,
        *,
        rpn_san_id: int,
        ip_ids: List[int],
    ) -> None:
        """
        :param rpn_san_id: RPN SAN ID.
        :param ip_ids: An array of IP ID.

        Usage:
        ::

            result = await api.add_ip(
                rpn_san_id=1,
                ip_ids=[],
            )
        """

        param_rpn_san_id = validate_path_param("rpn_san_id", rpn_san_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/rpn-sans/{param_rpn_san_id}/ips",
            body=marshal_RpnSanApiAddIpRequest(
                RpnSanApiAddIpRequest(
                    rpn_san_id=rpn_san_id,
                    ip_ids=ip_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def remove_ip(
        self,
        *,
        rpn_san_id: int,
        ip_ids: List[int],
    ) -> None:
        """
        :param rpn_san_id: RPN SAN ID.
        :param ip_ids: An array of IP ID.

        Usage:
        ::

            result = await api.remove_ip(
                rpn_san_id=1,
                ip_ids=[],
            )
        """

        param_rpn_san_id = validate_path_param("rpn_san_id", rpn_san_id)

        res = self._request(
            "DELETE",
            f"/dedibox/v1/rpn-sans/{param_rpn_san_id}/ips",
            body=marshal_RpnSanApiRemoveIpRequest(
                RpnSanApiRemoveIpRequest(
                    rpn_san_id=rpn_san_id,
                    ip_ids=ip_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def list_available_ips(
        self,
        *,
        rpn_san_id: int,
        type_: Optional[RpnSanIpType] = None,
    ) -> ListIpsResponse:
        """
        :param rpn_san_id: RPN SAN ID.
        :param type_: Filter by IP type (server | rpnv2_subnet).
        :return: :class:`ListIpsResponse <ListIpsResponse>`

        Usage:
        ::

            result = await api.list_available_ips(
                rpn_san_id=1,
            )
        """

        param_rpn_san_id = validate_path_param("rpn_san_id", rpn_san_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/rpn-sans/{param_rpn_san_id}/available-ips",
            params={
                "type": type_,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListIpsResponse(res.json())


class DediboxV1RpnV1API(API):
    """
    Dedibox Phoenix RPN v1 API.
    """

    async def list_rpn_groups(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnGroupsRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListRpnGroupsResponse:
        """
        :param page: Page number.
        :param page_size: Number of rpn v1 groups per page.
        :param order_by: Order of the rpn v1 groups.
        :param project_id: Filter rpn v1 groups by project ID.
        :return: :class:`ListRpnGroupsResponse <ListRpnGroupsResponse>`

        Usage:
        ::

            result = await api.list_rpn_groups()
        """

        res = self._request(
            "GET",
            "/dedibox/v1/rpnv1/groups",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRpnGroupsResponse(res.json())

    async def list_rpn_groups_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnGroupsRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[RpnGroup]:
        """
        :param page: Page number.
        :param page_size: Number of rpn v1 groups per page.
        :param order_by: Order of the rpn v1 groups.
        :param project_id: Filter rpn v1 groups by project ID.
        :return: :class:`List[RpnGroup] <List[RpnGroup]>`

        Usage:
        ::

            result = await api.list_rpn_groups_all()
        """

        return await fetch_all_pages_async(
            type=ListRpnGroupsResponse,
            key="rpn_groups",
            fetcher=self.list_rpn_groups,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def get_rpn_group(
        self,
        *,
        group_id: int,
    ) -> RpnGroup:
        """
        :param group_id: Rpn v1 group ID.
        :return: :class:`RpnGroup <RpnGroup>`

        Usage:
        ::

            result = await api.get_rpn_group(
                group_id=1,
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/rpnv1/groups/{param_group_id}",
        )

        self._throw_on_error(res)
        return unmarshal_RpnGroup(res.json())

    async def create_rpn_group(
        self,
        *,
        name: str,
        server_ids: Optional[List[int]] = None,
        san_server_ids: Optional[List[int]] = None,
        project_id: Optional[str] = None,
    ) -> RpnGroup:
        """
        :param name: Rpn v1 group name.
        :param server_ids: A collection of rpn v1 capable servers.
        :param san_server_ids: A collection of rpn v1 capable rpn sans servers.
        :param project_id: A project ID.
        :return: :class:`RpnGroup <RpnGroup>`

        Usage:
        ::

            result = await api.create_rpn_group(
                name="example",
            )
        """

        res = self._request(
            "POST",
            "/dedibox/v1/rpnv1/groups",
            body=marshal_RpnV1ApiCreateRpnGroupRequest(
                RpnV1ApiCreateRpnGroupRequest(
                    name=name,
                    server_ids=server_ids,
                    san_server_ids=san_server_ids,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RpnGroup(res.json())

    async def delete_rpn_group(
        self,
        *,
        group_id: int,
    ) -> None:
        """
        :param group_id: Rpn v1 group ID.

        Usage:
        ::

            result = await api.delete_rpn_group(
                group_id=1,
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "DELETE",
            f"/dedibox/v1/rpnv1/groups/{param_group_id}",
        )

        self._throw_on_error(res)

    async def update_rpn_group_name(
        self,
        *,
        group_id: int,
        name: Optional[str] = None,
    ) -> RpnGroup:
        """
        :param group_id: Rpn v1 group ID.
        :param name: New rpn v1 group name.
        :return: :class:`RpnGroup <RpnGroup>`

        Usage:
        ::

            result = await api.update_rpn_group_name(
                group_id=1,
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "PATCH",
            f"/dedibox/v1/rpnv1/groups/{param_group_id}",
            body=marshal_RpnV1ApiUpdateRpnGroupNameRequest(
                RpnV1ApiUpdateRpnGroupNameRequest(
                    group_id=group_id,
                    name=name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RpnGroup(res.json())

    async def list_rpn_group_members(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnGroupMembersRequestOrderBy] = None,
        group_id: int,
        project_id: Optional[str] = None,
    ) -> ListRpnGroupMembersResponse:
        """
        :param page: Page number.
        :param page_size: Number of rpn v1 group members per page.
        :param order_by: Order of the rpn v1 group members.
        :param group_id: Filter rpn v1 group members by group ID.
        :param project_id: A project ID.
        :return: :class:`ListRpnGroupMembersResponse <ListRpnGroupMembersResponse>`

        Usage:
        ::

            result = await api.list_rpn_group_members(
                group_id=1,
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/rpnv1/groups/{param_group_id}/members",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRpnGroupMembersResponse(res.json())

    async def list_rpn_group_members_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnGroupMembersRequestOrderBy] = None,
        group_id: int,
        project_id: Optional[str] = None,
    ) -> List[RpnGroupMember]:
        """
        :param page: Page number.
        :param page_size: Number of rpn v1 group members per page.
        :param order_by: Order of the rpn v1 group members.
        :param group_id: Filter rpn v1 group members by group ID.
        :param project_id: A project ID.
        :return: :class:`List[RpnGroupMember] <List[RpnGroupMember]>`

        Usage:
        ::

            result = await api.list_rpn_group_members_all(
                group_id=1,
            )
        """

        return await fetch_all_pages_async(
            type=ListRpnGroupMembersResponse,
            key="members",
            fetcher=self.list_rpn_group_members,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "group_id": group_id,
                "project_id": project_id,
            },
        )

    async def rpn_group_invite(
        self,
        *,
        group_id: int,
        server_ids: List[int],
        project_id: Optional[str] = None,
    ) -> None:
        """
        :param group_id: The RPN V1 group ID.
        :param server_ids: A collection of external server IDs.
        :param project_id: A project ID.

        Usage:
        ::

            result = await api.rpn_group_invite(
                group_id=1,
                server_ids=[],
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/rpnv1/groups/{param_group_id}/invite",
            body=marshal_RpnV1ApiRpnGroupInviteRequest(
                RpnV1ApiRpnGroupInviteRequest(
                    group_id=group_id,
                    server_ids=server_ids,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def leave_rpn_group(
        self,
        *,
        group_id: int,
        member_ids: List[int],
        project_id: Optional[str] = None,
    ) -> None:
        """
        :param group_id: The RPN V1 group ID.
        :param member_ids: A collection of rpn v1 group members IDs.
        :param project_id: A project ID.

        Usage:
        ::

            result = await api.leave_rpn_group(
                group_id=1,
                member_ids=[],
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/rpnv1/groups/{param_group_id}/leave",
            body=marshal_RpnV1ApiLeaveRpnGroupRequest(
                RpnV1ApiLeaveRpnGroupRequest(
                    group_id=group_id,
                    member_ids=member_ids,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def add_rpn_group_members(
        self,
        *,
        group_id: int,
        server_ids: Optional[List[int]] = None,
        san_server_ids: Optional[List[int]] = None,
    ) -> RpnGroup:
        """
        :param group_id: The rpn v1 group ID.
        :param server_ids: A collection of rpn v1 capable server IDs.
        :param san_server_ids: A collection of rpn v1 capable RPN SAN server IDs.
        :return: :class:`RpnGroup <RpnGroup>`

        Usage:
        ::

            result = await api.add_rpn_group_members(
                group_id=1,
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/rpnv1/groups/{param_group_id}/members",
            body=marshal_RpnV1ApiAddRpnGroupMembersRequest(
                RpnV1ApiAddRpnGroupMembersRequest(
                    group_id=group_id,
                    server_ids=server_ids,
                    san_server_ids=san_server_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RpnGroup(res.json())

    async def delete_rpn_group_members(
        self,
        *,
        group_id: int,
        member_ids: List[int],
    ) -> RpnGroup:
        """
        :param group_id: The rpn v1 group ID.
        :param member_ids: A collection of rpn v1 group members IDs.
        :return: :class:`RpnGroup <RpnGroup>`

        Usage:
        ::

            result = await api.delete_rpn_group_members(
                group_id=1,
                member_ids=[],
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "DELETE",
            f"/dedibox/v1/rpnv1/groups/{param_group_id}/members",
            body=marshal_RpnV1ApiDeleteRpnGroupMembersRequest(
                RpnV1ApiDeleteRpnGroupMembersRequest(
                    group_id=group_id,
                    member_ids=member_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RpnGroup(res.json())

    async def list_rpn_capable_servers(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnCapableServersRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListRpnCapableServersResponse:
        """
        :param page: Page number.
        :param page_size: Number of rpn capable resources per page.
        :param order_by: Order of the rpn capable resources.
        :param project_id: Filter rpn capable resources by project ID.
        :return: :class:`ListRpnCapableServersResponse <ListRpnCapableServersResponse>`

        Usage:
        ::

            result = await api.list_rpn_capable_servers()
        """

        res = self._request(
            "GET",
            "/dedibox/v1/rpnv1/capable-servers",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRpnCapableServersResponse(res.json())

    async def list_rpn_capable_servers_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnCapableServersRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[Server]:
        """
        :param page: Page number.
        :param page_size: Number of rpn capable resources per page.
        :param order_by: Order of the rpn capable resources.
        :param project_id: Filter rpn capable resources by project ID.
        :return: :class:`List[Server] <List[Server]>`

        Usage:
        ::

            result = await api.list_rpn_capable_servers_all()
        """

        return await fetch_all_pages_async(
            type=ListRpnCapableServersResponse,
            key="servers",
            fetcher=self.list_rpn_capable_servers,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def list_rpn_capable_san_servers(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnCapableSanServersRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListRpnCapableSanServersResponse:
        """
        :param page: Page number.
        :param page_size: Number of rpn capable resources per page.
        :param order_by: Order of the rpn capable resources.
        :param project_id: Filter rpn capable resources by project ID.
        :return: :class:`ListRpnCapableSanServersResponse <ListRpnCapableSanServersResponse>`

        Usage:
        ::

            result = await api.list_rpn_capable_san_servers()
        """

        res = self._request(
            "GET",
            "/dedibox/v1/rpnv1/capable-san-servers",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRpnCapableSanServersResponse(res.json())

    async def list_rpn_capable_san_servers_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnCapableSanServersRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[RpnSanServer]:
        """
        :param page: Page number.
        :param page_size: Number of rpn capable resources per page.
        :param order_by: Order of the rpn capable resources.
        :param project_id: Filter rpn capable resources by project ID.
        :return: :class:`List[RpnSanServer] <List[RpnSanServer]>`

        Usage:
        ::

            result = await api.list_rpn_capable_san_servers_all()
        """

        return await fetch_all_pages_async(
            type=ListRpnCapableSanServersResponse,
            key="san_servers",
            fetcher=self.list_rpn_capable_san_servers,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def list_rpn_invites(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnInvitesRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListRpnInvitesResponse:
        """
        :param page: Page number.
        :param page_size: Number of rpn capable resources per page.
        :param order_by: Order of the rpn capable resources.
        :param project_id: Filter rpn capable resources by project ID.
        :return: :class:`ListRpnInvitesResponse <ListRpnInvitesResponse>`

        Usage:
        ::

            result = await api.list_rpn_invites()
        """

        res = self._request(
            "GET",
            "/dedibox/v1/rpnv1/invites",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRpnInvitesResponse(res.json())

    async def list_rpn_invites_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnInvitesRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[RpnGroupMember]:
        """
        :param page: Page number.
        :param page_size: Number of rpn capable resources per page.
        :param order_by: Order of the rpn capable resources.
        :param project_id: Filter rpn capable resources by project ID.
        :return: :class:`List[RpnGroupMember] <List[RpnGroupMember]>`

        Usage:
        ::

            result = await api.list_rpn_invites_all()
        """

        return await fetch_all_pages_async(
            type=ListRpnInvitesResponse,
            key="members",
            fetcher=self.list_rpn_invites,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def accept_rpn_invite(
        self,
        *,
        member_id: int,
    ) -> None:
        """
        :param member_id: The member ID.

        Usage:
        ::

            result = await api.accept_rpn_invite(
                member_id=1,
            )
        """

        param_member_id = validate_path_param("member_id", member_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/rpnv1/invites/{param_member_id}/accept",
        )

        self._throw_on_error(res)

    async def refuse_rpn_invite(
        self,
        *,
        member_id: int,
    ) -> None:
        """
        :param member_id: The member ID.

        Usage:
        ::

            result = await api.refuse_rpn_invite(
                member_id=1,
            )
        """

        param_member_id = validate_path_param("member_id", member_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/rpnv1/invites/{param_member_id}/refuse",
        )

        self._throw_on_error(res)


class DediboxV1RpnV2API(API):
    """
    Dedibox Phoenix RPN v2 API.
    """

    async def list_rpn_v2_groups(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnV2GroupsRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListRpnV2GroupsResponse:
        """
        :param page: Page number.
        :param page_size: Number of rpn v2 groups per page.
        :param order_by: Order of the rpn v2 groups.
        :param project_id: Filter rpn v2 groups by project ID.
        :return: :class:`ListRpnV2GroupsResponse <ListRpnV2GroupsResponse>`

        Usage:
        ::

            result = await api.list_rpn_v2_groups()
        """

        res = self._request(
            "GET",
            "/dedibox/v1/rpnv2/groups",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRpnV2GroupsResponse(res.json())

    async def list_rpn_v2_groups_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnV2GroupsRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[RpnV2Group]:
        """
        :param page: Page number.
        :param page_size: Number of rpn v2 groups per page.
        :param order_by: Order of the rpn v2 groups.
        :param project_id: Filter rpn v2 groups by project ID.
        :return: :class:`List[RpnV2Group] <List[RpnV2Group]>`

        Usage:
        ::

            result = await api.list_rpn_v2_groups_all()
        """

        return await fetch_all_pages_async(
            type=ListRpnV2GroupsResponse,
            key="rpn_groups",
            fetcher=self.list_rpn_v2_groups,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def list_rpn_v2_members(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnV2MembersRequestOrderBy] = None,
        group_id: int,
        type_: Optional[ListRpnV2MembersRequestType] = None,
    ) -> ListRpnV2MembersResponse:
        """
        :param page: Page number.
        :param page_size: Number of rpn v2 group members per page.
        :param order_by: Order of the rpn v2 group members.
        :param group_id: RPN V2 group ID.
        :param type_: Filter members by type.
        :return: :class:`ListRpnV2MembersResponse <ListRpnV2MembersResponse>`

        Usage:
        ::

            result = await api.list_rpn_v2_members(
                group_id=1,
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/rpnv2/groups/{param_group_id}/members",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "type": type_,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRpnV2MembersResponse(res.json())

    async def list_rpn_v2_members_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnV2MembersRequestOrderBy] = None,
        group_id: int,
        type_: Optional[ListRpnV2MembersRequestType] = None,
    ) -> List[RpnV2Member]:
        """
        :param page: Page number.
        :param page_size: Number of rpn v2 group members per page.
        :param order_by: Order of the rpn v2 group members.
        :param group_id: RPN V2 group ID.
        :param type_: Filter members by type.
        :return: :class:`List[RpnV2Member] <List[RpnV2Member]>`

        Usage:
        ::

            result = await api.list_rpn_v2_members_all(
                group_id=1,
            )
        """

        return await fetch_all_pages_async(
            type=ListRpnV2MembersResponse,
            key="members",
            fetcher=self.list_rpn_v2_members,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "group_id": group_id,
                "type_": type_,
            },
        )

    async def get_rpn_v2_group(
        self,
        *,
        group_id: int,
    ) -> RpnV2Group:
        """
        :param group_id: RPN V2 group ID.
        :return: :class:`RpnV2Group <RpnV2Group>`

        Usage:
        ::

            result = await api.get_rpn_v2_group(
                group_id=1,
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/rpnv2/groups/{param_group_id}",
        )

        self._throw_on_error(res)
        return unmarshal_RpnV2Group(res.json())

    async def wait_for_rpn_v2_group(
        self,
        *,
        group_id: int,
        options: Optional[
            WaitForOptions[RpnV2Group, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> RpnV2Group:
        """
        :param group_id: RPN V2 group ID.
        :return: :class:`RpnV2Group <RpnV2Group>`

        Usage:
        ::

            result = await api.get_rpn_v2_group(
                group_id=1,
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in RPN_V2_GROUP_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_rpn_v2_group,
            options=options,
            args={
                "group_id": group_id,
            },
        )

    async def create_rpn_v2_group(
        self,
        *,
        name: str,
        servers: List[int],
        project_id: Optional[str] = None,
        type_: Optional[RpnV2GroupType] = None,
    ) -> RpnV2Group:
        """
        :param name: RPN V2 group name.
        :param servers: A collection of server IDs.
        :param project_id: Project ID of the RPN V2 group.
        :param type_: RPN V2 group type (qing / standard).
        :return: :class:`RpnV2Group <RpnV2Group>`

        Usage:
        ::

            result = await api.create_rpn_v2_group(
                name="example",
                servers=[],
            )
        """

        res = self._request(
            "POST",
            "/dedibox/v1/rpnv2/groups",
            body=marshal_RpnV2ApiCreateRpnV2GroupRequest(
                RpnV2ApiCreateRpnV2GroupRequest(
                    name=name,
                    servers=servers,
                    project_id=project_id,
                    type_=type_,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RpnV2Group(res.json())

    async def delete_rpn_v2_group(
        self,
        *,
        group_id: int,
    ) -> None:
        """
        :param group_id: RPN V2 group ID.

        Usage:
        ::

            result = await api.delete_rpn_v2_group(
                group_id=1,
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "DELETE",
            f"/dedibox/v1/rpnv2/groups/{param_group_id}",
        )

        self._throw_on_error(res)

    async def update_rpn_v2_group_name(
        self,
        *,
        group_id: int,
        name: Optional[str] = None,
    ) -> RpnV2Group:
        """
        :param group_id: RPN V2 group ID.
        :param name: RPN V2 group name.
        :return: :class:`RpnV2Group <RpnV2Group>`

        Usage:
        ::

            result = await api.update_rpn_v2_group_name(
                group_id=1,
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "PATCH",
            f"/dedibox/v1/rpnv2/groups/{param_group_id}",
            body=marshal_RpnV2ApiUpdateRpnV2GroupNameRequest(
                RpnV2ApiUpdateRpnV2GroupNameRequest(
                    group_id=group_id,
                    name=name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RpnV2Group(res.json())

    async def add_rpn_v2_members(
        self,
        *,
        group_id: int,
        servers: List[int],
    ) -> None:
        """
        :param group_id: RPN V2 group ID.
        :param servers: A collection of server IDs.

        Usage:
        ::

            result = await api.add_rpn_v2_members(
                group_id=1,
                servers=[],
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/rpnv2/groups/{param_group_id}/members",
            body=marshal_RpnV2ApiAddRpnV2MembersRequest(
                RpnV2ApiAddRpnV2MembersRequest(
                    group_id=group_id,
                    servers=servers,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def delete_rpn_v2_members(
        self,
        *,
        group_id: int,
        member_ids: List[int],
    ) -> None:
        """
        :param group_id: RPN V2 group ID.
        :param member_ids: A collection of member IDs.

        Usage:
        ::

            result = await api.delete_rpn_v2_members(
                group_id=1,
                member_ids=[],
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "DELETE",
            f"/dedibox/v1/rpnv2/groups/{param_group_id}/members",
            body=marshal_RpnV2ApiDeleteRpnV2MembersRequest(
                RpnV2ApiDeleteRpnV2MembersRequest(
                    group_id=group_id,
                    member_ids=member_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def list_rpn_v2_capable_resources(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnV2CapableResourcesRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListRpnV2CapableResourcesResponse:
        """
        :param page: Page number.
        :param page_size: Number of rpn v2 capable resources per page.
        :param order_by: Order of the rpn v2 capable resources.
        :param project_id: Filter rpn v2 capable resources by project ID.
        :return: :class:`ListRpnV2CapableResourcesResponse <ListRpnV2CapableResourcesResponse>`

        Usage:
        ::

            result = await api.list_rpn_v2_capable_resources()
        """

        res = self._request(
            "GET",
            "/dedibox/v1/rpnv2/groups/capable",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRpnV2CapableResourcesResponse(res.json())

    async def list_rpn_v2_capable_resources_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnV2CapableResourcesRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[Server]:
        """
        :param page: Page number.
        :param page_size: Number of rpn v2 capable resources per page.
        :param order_by: Order of the rpn v2 capable resources.
        :param project_id: Filter rpn v2 capable resources by project ID.
        :return: :class:`List[Server] <List[Server]>`

        Usage:
        ::

            result = await api.list_rpn_v2_capable_resources_all()
        """

        return await fetch_all_pages_async(
            type=ListRpnV2CapableResourcesResponse,
            key="servers",
            fetcher=self.list_rpn_v2_capable_resources,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def list_rpn_v2_group_logs(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnV2GroupLogsRequestOrderBy] = None,
        group_id: int,
    ) -> ListRpnV2GroupLogsResponse:
        """
        :param page: Page number.
        :param page_size: Number of rpn v2 group logs per page.
        :param order_by: Order of the rpn v2 group logs.
        :param group_id: RPN V2 group ID.
        :return: :class:`ListRpnV2GroupLogsResponse <ListRpnV2GroupLogsResponse>`

        Usage:
        ::

            result = await api.list_rpn_v2_group_logs(
                group_id=1,
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "GET",
            f"/dedibox/v1/rpnv2/groups/{param_group_id}/logs",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRpnV2GroupLogsResponse(res.json())

    async def list_rpn_v2_group_logs_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRpnV2GroupLogsRequestOrderBy] = None,
        group_id: int,
    ) -> List[Log]:
        """
        :param page: Page number.
        :param page_size: Number of rpn v2 group logs per page.
        :param order_by: Order of the rpn v2 group logs.
        :param group_id: RPN V2 group ID.
        :return: :class:`List[Log] <List[Log]>`

        Usage:
        ::

            result = await api.list_rpn_v2_group_logs_all(
                group_id=1,
            )
        """

        return await fetch_all_pages_async(
            type=ListRpnV2GroupLogsResponse,
            key="logs",
            fetcher=self.list_rpn_v2_group_logs,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "group_id": group_id,
            },
        )

    async def update_rpn_v2_vlan_for_members(
        self,
        *,
        group_id: int,
        member_ids: List[int],
        vlan: Optional[int] = None,
    ) -> None:
        """
        :param group_id: RPN V2 group ID.
        :param member_ids: RPN V2 member IDs.
        :param vlan: Min: 0.
        Max: 3967.

        Usage:
        ::

            result = await api.update_rpn_v2_vlan_for_members(
                group_id=1,
                member_ids=[],
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "PATCH",
            f"/dedibox/v1/rpnv2/groups/{param_group_id}/vlan",
            body=marshal_RpnV2ApiUpdateRpnV2VlanForMembersRequest(
                RpnV2ApiUpdateRpnV2VlanForMembersRequest(
                    group_id=group_id,
                    member_ids=member_ids,
                    vlan=vlan,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def enable_rpn_v2_group_compatibility(
        self,
        *,
        group_id: int,
        rpnv1_group_id: int,
    ) -> None:
        """
        :param group_id: RPN V2 group ID.
        :param rpnv1_group_id: RPN V1 group ID.

        Usage:
        ::

            result = await api.enable_rpn_v2_group_compatibility(
                group_id=1,
                rpnv1_group_id=1,
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/rpnv2/groups/{param_group_id}/enable-compatibility",
            body=marshal_RpnV2ApiEnableRpnV2GroupCompatibilityRequest(
                RpnV2ApiEnableRpnV2GroupCompatibilityRequest(
                    group_id=group_id,
                    rpnv1_group_id=rpnv1_group_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def disable_rpn_v2_group_compatibility(
        self,
        *,
        group_id: int,
    ) -> None:
        """
        :param group_id: RPN V2 group ID.

        Usage:
        ::

            result = await api.disable_rpn_v2_group_compatibility(
                group_id=1,
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "POST",
            f"/dedibox/v1/rpnv2/groups/{param_group_id}/disable-compatibility",
            body={},
        )

        self._throw_on_error(res)
