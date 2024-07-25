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
    DHCPEntryType,
    GatewayNetworkStatus,
    GatewayStatus,
    ListDHCPEntriesRequestOrderBy,
    ListDHCPsRequestOrderBy,
    ListGatewayNetworksRequestOrderBy,
    ListGatewaysRequestOrderBy,
    ListIPsRequestOrderBy,
    ListPATRulesRequestOrderBy,
    PATRuleProtocol,
    CreateDHCPEntryRequest,
    CreateDHCPRequest,
    CreateGatewayNetworkRequest,
    CreateGatewayNetworkRequestIpamConfig,
    CreateGatewayRequest,
    CreateIPRequest,
    CreatePATRuleRequest,
    DHCP,
    DHCPEntry,
    Gateway,
    GatewayNetwork,
    IP,
    ListDHCPEntriesResponse,
    ListDHCPsResponse,
    ListGatewayNetworksResponse,
    ListGatewayTypesResponse,
    ListGatewaysResponse,
    ListIPsResponse,
    ListPATRulesResponse,
    PATRule,
    SetDHCPEntriesRequest,
    SetDHCPEntriesRequestEntry,
    SetDHCPEntriesResponse,
    SetPATRulesRequest,
    SetPATRulesRequestRule,
    SetPATRulesResponse,
    UpdateDHCPEntryRequest,
    UpdateDHCPRequest,
    UpdateGatewayNetworkRequest,
    UpdateGatewayNetworkRequestIpamConfig,
    UpdateGatewayRequest,
    UpdateIPRequest,
    UpdatePATRuleRequest,
    UpgradeGatewayRequest,
)
from .content import (
    GATEWAY_NETWORK_TRANSIENT_STATUSES,
    GATEWAY_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_DHCP,
    unmarshal_GatewayNetwork,
    unmarshal_IP,
    unmarshal_DHCPEntry,
    unmarshal_Gateway,
    unmarshal_PATRule,
    unmarshal_ListDHCPEntriesResponse,
    unmarshal_ListDHCPsResponse,
    unmarshal_ListGatewayNetworksResponse,
    unmarshal_ListGatewayTypesResponse,
    unmarshal_ListGatewaysResponse,
    unmarshal_ListIPsResponse,
    unmarshal_ListPATRulesResponse,
    unmarshal_SetDHCPEntriesResponse,
    unmarshal_SetPATRulesResponse,
    marshal_CreateDHCPRequest,
    marshal_CreateDHCPEntryRequest,
    marshal_CreateGatewayNetworkRequest,
    marshal_CreateGatewayRequest,
    marshal_CreateIPRequest,
    marshal_CreatePATRuleRequest,
    marshal_SetDHCPEntriesRequest,
    marshal_SetPATRulesRequest,
    marshal_UpdateDHCPEntryRequest,
    marshal_UpdateDHCPRequest,
    marshal_UpdateGatewayNetworkRequest,
    marshal_UpdateGatewayRequest,
    marshal_UpdateIPRequest,
    marshal_UpdatePATRuleRequest,
    marshal_UpgradeGatewayRequest,
)


class VpcgwV1API(API):
    """
    This API allows you to manage your Public Gateways.
    """

    async def list_gateways(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListGatewaysRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        type_: Optional[str] = None,
        status: Optional[GatewayStatus] = None,
        private_network_id: Optional[str] = None,
    ) -> ListGatewaysResponse:
        """
        List Public Gateways.
        List Public Gateways in a given Scaleway Organization or Project. By default, results are displayed in ascending order of creation date.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number to return.
        :param page_size: Gateways per page.
        :param organization_id: Include only gateways in this Organization.
        :param project_id: Include only gateways in this Project.
        :param name: Filter for gateways which have this search term in their name.
        :param tags: Filter for gateways with these tags.
        :param type_: Filter for gateways of this type.
        :param status: Filter for gateways with this current status. Use `unknown` to include all statuses.
        :param private_network_id: Filter for gateways attached to this Private nNetwork.
        :return: :class:`ListGatewaysResponse <ListGatewaysResponse>`

        Usage:
        ::

            result = await api.list_gateways()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/vpc-gw/v1/zones/{param_zone}/gateways",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "private_network_id": private_network_id,
                "project_id": project_id or self.client.default_project_id,
                "status": status,
                "tags": tags,
                "type": type_,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListGatewaysResponse(res.json())

    async def list_gateways_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListGatewaysRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        type_: Optional[str] = None,
        status: Optional[GatewayStatus] = None,
        private_network_id: Optional[str] = None,
    ) -> List[Gateway]:
        """
        List Public Gateways.
        List Public Gateways in a given Scaleway Organization or Project. By default, results are displayed in ascending order of creation date.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number to return.
        :param page_size: Gateways per page.
        :param organization_id: Include only gateways in this Organization.
        :param project_id: Include only gateways in this Project.
        :param name: Filter for gateways which have this search term in their name.
        :param tags: Filter for gateways with these tags.
        :param type_: Filter for gateways of this type.
        :param status: Filter for gateways with this current status. Use `unknown` to include all statuses.
        :param private_network_id: Filter for gateways attached to this Private nNetwork.
        :return: :class:`List[Gateway] <List[Gateway]>`

        Usage:
        ::

            result = await api.list_gateways_all()
        """

        return await fetch_all_pages_async(
            type=ListGatewaysResponse,
            key="gateways",
            fetcher=self.list_gateways,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "project_id": project_id,
                "name": name,
                "tags": tags,
                "type_": type_,
                "status": status,
                "private_network_id": private_network_id,
            },
        )

    async def get_gateway(
        self,
        *,
        gateway_id: str,
        zone: Optional[Zone] = None,
    ) -> Gateway:
        """
        Get a Public Gateway.
        Get details of a Public Gateway, specified by its gateway ID. The response object contains full details of the gateway, including its **name**, **type**, **status** and more.
        :param gateway_id: ID of the gateway to fetch.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = await api.get_gateway(
                gateway_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "GET",
            f"/vpc-gw/v1/zones/{param_zone}/gateways/{param_gateway_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Gateway(res.json())

    async def wait_for_gateway(
        self,
        *,
        gateway_id: str,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[Gateway, Union[bool, Awaitable[bool]]]] = None,
    ) -> Gateway:
        """
        Get a Public Gateway.
        Get details of a Public Gateway, specified by its gateway ID. The response object contains full details of the gateway, including its **name**, **type**, **status** and more.
        :param gateway_id: ID of the gateway to fetch.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = await api.get_gateway(
                gateway_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in GATEWAY_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_gateway,
            options=options,
            args={
                "gateway_id": gateway_id,
                "zone": zone,
            },
        )

    async def create_gateway(
        self,
        *,
        type_: str,
        enable_smtp: bool,
        enable_bastion: bool,
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        upstream_dns_servers: Optional[List[str]] = None,
        ip_id: Optional[str] = None,
        bastion_port: Optional[int] = None,
    ) -> Gateway:
        """
        Create a Public Gateway.
        Create a new Public Gateway in the specified Scaleway Project, defining its **name**, **type** and other configuration details such as whether to enable SSH bastion.
        :param type_: Gateway type (commercial offer type).
        :param enable_smtp: Defines whether SMTP traffic should be allowed pass through the gateway.
        :param enable_bastion: Defines whether SSH bastion should be enabled the gateway.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Scaleway Project to create the gateway in.
        :param name: Name for the gateway.
        :param tags: Tags for the gateway.
        :param upstream_dns_servers: Array of DNS server IP addresses to override the gateway's default recursive DNS servers.
        :param ip_id: Existing IP address to attach to the gateway.
        :param bastion_port: Port of the SSH bastion.
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = await api.create_gateway(
                type="example",
                enable_smtp=False,
                enable_bastion=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/vpc-gw/v1/zones/{param_zone}/gateways",
            body=marshal_CreateGatewayRequest(
                CreateGatewayRequest(
                    type_=type_,
                    enable_smtp=enable_smtp,
                    enable_bastion=enable_bastion,
                    zone=zone,
                    project_id=project_id,
                    name=name or random_name(prefix="gw"),
                    tags=tags,
                    upstream_dns_servers=upstream_dns_servers,
                    ip_id=ip_id,
                    bastion_port=bastion_port,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Gateway(res.json())

    async def update_gateway(
        self,
        *,
        gateway_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        upstream_dns_servers: Optional[List[str]] = None,
        enable_bastion: Optional[bool] = None,
        bastion_port: Optional[int] = None,
        enable_smtp: Optional[bool] = None,
    ) -> Gateway:
        """
        Update a Public Gateway.
        Update the parameters of an existing Public Gateway, for example, its **name**, **tags**, **SSH bastion configuration**, and **DNS servers**.
        :param gateway_id: ID of the gateway to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name for the gateway.
        :param tags: Tags for the gateway.
        :param upstream_dns_servers: Array of DNS server IP addresses to override the gateway's default recursive DNS servers.
        :param enable_bastion: Defines whether SSH bastion should be enabled the gateway.
        :param bastion_port: Port of the SSH bastion.
        :param enable_smtp: Defines whether SMTP traffic should be allowed to pass through the gateway.
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = await api.update_gateway(
                gateway_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "PATCH",
            f"/vpc-gw/v1/zones/{param_zone}/gateways/{param_gateway_id}",
            body=marshal_UpdateGatewayRequest(
                UpdateGatewayRequest(
                    gateway_id=gateway_id,
                    zone=zone,
                    name=name,
                    tags=tags,
                    upstream_dns_servers=upstream_dns_servers,
                    enable_bastion=enable_bastion,
                    bastion_port=bastion_port,
                    enable_smtp=enable_smtp,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Gateway(res.json())

    async def delete_gateway(
        self,
        *,
        gateway_id: str,
        cleanup_dhcp: bool,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a Public Gateway.
        Delete an existing Public Gateway, specified by its gateway ID. This action is irreversible.
        :param gateway_id: ID of the gateway to delete.
        :param cleanup_dhcp: Defines whether to clean up attached DHCP configurations (if any, and if not attached to another Gateway Network).
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_gateway(
                gateway_id="example",
                cleanup_dhcp=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "DELETE",
            f"/vpc-gw/v1/zones/{param_zone}/gateways/{param_gateway_id}",
            params={
                "cleanup_dhcp": cleanup_dhcp,
            },
        )

        self._throw_on_error(res)

    async def upgrade_gateway(
        self,
        *,
        gateway_id: str,
        zone: Optional[Zone] = None,
        type_: Optional[str] = None,
    ) -> Gateway:
        """
        Upgrade a Public Gateway to the latest version and/or to a different commercial offer type.
        Upgrade a given Public Gateway to the newest software version or to a different commercial offer type. This applies the latest bugfixes and features to your Public Gateway. Note that gateway service will be interrupted during the update.
        :param gateway_id: ID of the gateway to upgrade.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param type_: Gateway type (commercial offer).
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = await api.upgrade_gateway(
                gateway_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "POST",
            f"/vpc-gw/v1/zones/{param_zone}/gateways/{param_gateway_id}/upgrade",
            body=marshal_UpgradeGatewayRequest(
                UpgradeGatewayRequest(
                    gateway_id=gateway_id,
                    zone=zone,
                    type_=type_,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Gateway(res.json())

    async def enable_ip_mobility(
        self,
        *,
        gateway_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Upgrade a Public Gateway to IP mobility.
        Upgrade a Public Gateway to IP mobility (move from NAT IP to routed IP). This is idempotent: repeated calls after the first will return no error but have no effect.
        :param gateway_id: ID of the gateway to upgrade to IP mobility.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.enable_ip_mobility(
                gateway_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "POST",
            f"/vpc-gw/v1/zones/{param_zone}/gateways/{param_gateway_id}/enable-ip-mobility",
            body={},
        )

        self._throw_on_error(res)

    async def list_gateway_networks(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListGatewayNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        gateway_id: Optional[str] = None,
        private_network_id: Optional[str] = None,
        enable_masquerade: Optional[bool] = None,
        dhcp_id: Optional[str] = None,
        status: Optional[GatewayNetworkStatus] = None,
    ) -> ListGatewayNetworksResponse:
        """
        List Public Gateway connections to Private Networks.
        List the connections between Public Gateways and Private Networks (a connection = a GatewayNetwork). You can choose to filter by `gateway-id` to list all Private Networks attached to the specified Public Gateway, or by `private_network_id` to list all Public Gateways attached to the specified Private Network. Other query parameters are also available. The result is an array of GatewayNetwork objects, each giving details of the connection between a given Public Gateway and a given Private Network.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: GatewayNetworks per page.
        :param gateway_id: Filter for GatewayNetworks connected to this gateway.
        :param private_network_id: Filter for GatewayNetworks connected to this Private Network.
        :param enable_masquerade: Filter for GatewayNetworks with this `enable_masquerade` setting.
        :param dhcp_id: Filter for GatewayNetworks using this DHCP configuration.
        :param status: Filter for GatewayNetworks with this current status this status. Use `unknown` to include all statuses.
        :return: :class:`ListGatewayNetworksResponse <ListGatewayNetworksResponse>`

        Usage:
        ::

            result = await api.list_gateway_networks()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/vpc-gw/v1/zones/{param_zone}/gateway-networks",
            params={
                "dhcp_id": dhcp_id,
                "enable_masquerade": enable_masquerade,
                "gateway_id": gateway_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "private_network_id": private_network_id,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListGatewayNetworksResponse(res.json())

    async def list_gateway_networks_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListGatewayNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        gateway_id: Optional[str] = None,
        private_network_id: Optional[str] = None,
        enable_masquerade: Optional[bool] = None,
        dhcp_id: Optional[str] = None,
        status: Optional[GatewayNetworkStatus] = None,
    ) -> List[GatewayNetwork]:
        """
        List Public Gateway connections to Private Networks.
        List the connections between Public Gateways and Private Networks (a connection = a GatewayNetwork). You can choose to filter by `gateway-id` to list all Private Networks attached to the specified Public Gateway, or by `private_network_id` to list all Public Gateways attached to the specified Private Network. Other query parameters are also available. The result is an array of GatewayNetwork objects, each giving details of the connection between a given Public Gateway and a given Private Network.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: GatewayNetworks per page.
        :param gateway_id: Filter for GatewayNetworks connected to this gateway.
        :param private_network_id: Filter for GatewayNetworks connected to this Private Network.
        :param enable_masquerade: Filter for GatewayNetworks with this `enable_masquerade` setting.
        :param dhcp_id: Filter for GatewayNetworks using this DHCP configuration.
        :param status: Filter for GatewayNetworks with this current status this status. Use `unknown` to include all statuses.
        :return: :class:`List[GatewayNetwork] <List[GatewayNetwork]>`

        Usage:
        ::

            result = await api.list_gateway_networks_all()
        """

        return await fetch_all_pages_async(
            type=ListGatewayNetworksResponse,
            key="gateway_networks",
            fetcher=self.list_gateway_networks,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "gateway_id": gateway_id,
                "private_network_id": private_network_id,
                "enable_masquerade": enable_masquerade,
                "dhcp_id": dhcp_id,
                "status": status,
            },
        )

    async def get_gateway_network(
        self,
        *,
        gateway_network_id: str,
        zone: Optional[Zone] = None,
    ) -> GatewayNetwork:
        """
        Get a Public Gateway connection to a Private Network.
        Get details of a given connection between a Public Gateway and a Private Network (this connection = a GatewayNetwork), specified by its `gateway_network_id`. The response object contains details of the connection including the IDs of the Public Gateway and Private Network, the dates the connection was created/updated and its configuration settings.
        :param gateway_network_id: ID of the GatewayNetwork to fetch.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GatewayNetwork <GatewayNetwork>`

        Usage:
        ::

            result = await api.get_gateway_network(
                gateway_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_network_id = validate_path_param(
            "gateway_network_id", gateway_network_id
        )

        res = self._request(
            "GET",
            f"/vpc-gw/v1/zones/{param_zone}/gateway-networks/{param_gateway_network_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GatewayNetwork(res.json())

    async def wait_for_gateway_network(
        self,
        *,
        gateway_network_id: str,
        zone: Optional[Zone] = None,
        options: Optional[
            WaitForOptions[GatewayNetwork, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> GatewayNetwork:
        """
        Get a Public Gateway connection to a Private Network.
        Get details of a given connection between a Public Gateway and a Private Network (this connection = a GatewayNetwork), specified by its `gateway_network_id`. The response object contains details of the connection including the IDs of the Public Gateway and Private Network, the dates the connection was created/updated and its configuration settings.
        :param gateway_network_id: ID of the GatewayNetwork to fetch.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GatewayNetwork <GatewayNetwork>`

        Usage:
        ::

            result = await api.get_gateway_network(
                gateway_network_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = (
                lambda res: res.status not in GATEWAY_NETWORK_TRANSIENT_STATUSES
            )

        return await wait_for_resource_async(
            fetcher=self.get_gateway_network,
            options=options,
            args={
                "gateway_network_id": gateway_network_id,
                "zone": zone,
            },
        )

    async def create_gateway_network(
        self,
        *,
        gateway_id: str,
        private_network_id: str,
        enable_masquerade: bool,
        zone: Optional[Zone] = None,
        enable_dhcp: Optional[bool] = None,
        dhcp_id: Optional[str] = None,
        dhcp: Optional[CreateDHCPRequest] = None,
        address: Optional[str] = None,
        ipam_config: Optional[CreateGatewayNetworkRequestIpamConfig] = None,
    ) -> GatewayNetwork:
        """
        Attach a Public Gateway to a Private Network.
        Attach a specific Public Gateway to a specific Private Network (create a GatewayNetwork). You can configure parameters for the connection including DHCP settings, whether to enable masquerade (dynamic NAT), and more.
        :param gateway_id: Public Gateway to connect.
        :param private_network_id: Private Network to connect.
        :param enable_masquerade: Note: this setting is ignored when passing `ipam_config`.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param enable_dhcp: Defaults to `true` if either `dhcp_id` or `dhcp` are present. If set to `true`, either `dhcp_id` or `dhcp` must be present.
        Note: this setting is ignored when passing `ipam_config`.
        :param dhcp_id: ID of an existing DHCP configuration object to use for this GatewayNetwork.
        One-Of ('ip_config'): at most one of 'dhcp_id', 'dhcp', 'address', 'ipam_config' could be set.
        :param dhcp: New DHCP configuration object to use for this GatewayNetwork.
        One-Of ('ip_config'): at most one of 'dhcp_id', 'dhcp', 'address', 'ipam_config' could be set.
        :param address: Static IP address in CIDR format to to use without DHCP.
        One-Of ('ip_config'): at most one of 'dhcp_id', 'dhcp', 'address', 'ipam_config' could be set.
        :param ipam_config: Note: all or none of the GatewayNetworks for a single gateway can use the IPAM. DHCP and IPAM configurations cannot be mixed. Some products may require that the Public Gateway uses the IPAM, to ensure correct functionality.
        One-Of ('ip_config'): at most one of 'dhcp_id', 'dhcp', 'address', 'ipam_config' could be set.
        :return: :class:`GatewayNetwork <GatewayNetwork>`

        Usage:
        ::

            result = await api.create_gateway_network(
                gateway_id="example",
                private_network_id="example",
                enable_masquerade=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/vpc-gw/v1/zones/{param_zone}/gateway-networks",
            body=marshal_CreateGatewayNetworkRequest(
                CreateGatewayNetworkRequest(
                    gateway_id=gateway_id,
                    private_network_id=private_network_id,
                    enable_masquerade=enable_masquerade,
                    zone=zone,
                    enable_dhcp=enable_dhcp,
                    dhcp_id=dhcp_id,
                    dhcp=dhcp,
                    address=address,
                    ipam_config=ipam_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_GatewayNetwork(res.json())

    async def update_gateway_network(
        self,
        *,
        gateway_network_id: str,
        zone: Optional[Zone] = None,
        enable_masquerade: Optional[bool] = None,
        enable_dhcp: Optional[bool] = None,
        dhcp_id: Optional[str] = None,
        address: Optional[str] = None,
        ipam_config: Optional[UpdateGatewayNetworkRequestIpamConfig] = None,
    ) -> GatewayNetwork:
        """
        Update a Public Gateway's connection to a Private Network.
        Update the configuration parameters of a connection between a given Public Gateway and Private Network (the connection = a GatewayNetwork). Updatable parameters include DHCP settings and whether to enable traffic masquerade (dynamic NAT).
        :param gateway_network_id: ID of the GatewayNetwork to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param enable_masquerade: Note: this setting is ignored when passing `ipam_config`.
        :param enable_dhcp: Defaults to `true` if `dhcp_id` is present. If set to `true`, `dhcp_id` must be present.
        Note: this setting is ignored when passing `ipam_config`.
        :param dhcp_id: ID of the new DHCP configuration object to use with this GatewayNetwork.
        One-Of ('ip_config'): at most one of 'dhcp_id', 'address', 'ipam_config' could be set.
        :param address: New static IP address.
        One-Of ('ip_config'): at most one of 'dhcp_id', 'address', 'ipam_config' could be set.
        :param ipam_config: Note: all or none of the GatewayNetworks for a single gateway can use the IPAM. DHCP and IPAM configurations cannot be mixed. Some products may require that the Public Gateway uses the IPAM, to ensure correct functionality.
        One-Of ('ip_config'): at most one of 'dhcp_id', 'address', 'ipam_config' could be set.
        :return: :class:`GatewayNetwork <GatewayNetwork>`

        Usage:
        ::

            result = await api.update_gateway_network(
                gateway_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_network_id = validate_path_param(
            "gateway_network_id", gateway_network_id
        )

        res = self._request(
            "PATCH",
            f"/vpc-gw/v1/zones/{param_zone}/gateway-networks/{param_gateway_network_id}",
            body=marshal_UpdateGatewayNetworkRequest(
                UpdateGatewayNetworkRequest(
                    gateway_network_id=gateway_network_id,
                    zone=zone,
                    enable_masquerade=enable_masquerade,
                    enable_dhcp=enable_dhcp,
                    dhcp_id=dhcp_id,
                    address=address,
                    ipam_config=ipam_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_GatewayNetwork(res.json())

    async def delete_gateway_network(
        self,
        *,
        gateway_network_id: str,
        cleanup_dhcp: bool,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Detach a Public Gateway from a Private Network.
        Detach a given Public Gateway from a given Private Network, i.e. delete a GatewayNetwork specified by a gateway_network_id.
        :param gateway_network_id: ID of the GatewayNetwork to delete.
        :param cleanup_dhcp: Defines whether to clean up attached DHCP configurations (if any, and if not attached to another Gateway Network).
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_gateway_network(
                gateway_network_id="example",
                cleanup_dhcp=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_network_id = validate_path_param(
            "gateway_network_id", gateway_network_id
        )

        res = self._request(
            "DELETE",
            f"/vpc-gw/v1/zones/{param_zone}/gateway-networks/{param_gateway_network_id}",
            params={
                "cleanup_dhcp": cleanup_dhcp,
            },
        )

        self._throw_on_error(res)

    async def list_dhc_ps(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListDHCPsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        address: Optional[str] = None,
        has_address: Optional[str] = None,
    ) -> ListDHCPsResponse:
        """
        List DHCP configurations.
        List DHCP configurations, optionally filtering by Organization, Project, Public Gateway IP address or more. The response is an array of DHCP configuration objects, each identified by a DHCP ID and containing configuration settings for the assignment of IP addresses to devices on a Private Network attached to a Public Gateway. Note that the response does not contain the IDs of any Private Network / Public Gateway the configuration is attached to. Use the `List Public Gateway connections to Private Networks` method for that purpose, filtering on DHCP ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: DHCP configurations per page.
        :param organization_id: Include only DHCP configuration objects in this Organization.
        :param project_id: Include only DHCP configuration objects in this Project.
        :param address: Filter for DHCP configuration objects with this DHCP server IP address (the gateway's address in the Private Network).
        :param has_address: Filter for DHCP configuration objects with subnets containing this IP address.
        :return: :class:`ListDHCPsResponse <ListDHCPsResponse>`

        Usage:
        ::

            result = await api.list_dhc_ps()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/vpc-gw/v1/zones/{param_zone}/dhcps",
            params={
                "address": address,
                "has_address": has_address,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDHCPsResponse(res.json())

    async def list_dhc_ps_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListDHCPsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        address: Optional[str] = None,
        has_address: Optional[str] = None,
    ) -> List[DHCP]:
        """
        List DHCP configurations.
        List DHCP configurations, optionally filtering by Organization, Project, Public Gateway IP address or more. The response is an array of DHCP configuration objects, each identified by a DHCP ID and containing configuration settings for the assignment of IP addresses to devices on a Private Network attached to a Public Gateway. Note that the response does not contain the IDs of any Private Network / Public Gateway the configuration is attached to. Use the `List Public Gateway connections to Private Networks` method for that purpose, filtering on DHCP ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: DHCP configurations per page.
        :param organization_id: Include only DHCP configuration objects in this Organization.
        :param project_id: Include only DHCP configuration objects in this Project.
        :param address: Filter for DHCP configuration objects with this DHCP server IP address (the gateway's address in the Private Network).
        :param has_address: Filter for DHCP configuration objects with subnets containing this IP address.
        :return: :class:`List[DHCP] <List[DHCP]>`

        Usage:
        ::

            result = await api.list_dhc_ps_all()
        """

        return await fetch_all_pages_async(
            type=ListDHCPsResponse,
            key="dhcps",
            fetcher=self.list_dhc_ps,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "project_id": project_id,
                "address": address,
                "has_address": has_address,
            },
        )

    async def get_dhcp(
        self,
        *,
        dhcp_id: str,
        zone: Optional[Zone] = None,
    ) -> DHCP:
        """
        Get a DHCP configuration.
        Get a DHCP configuration object, identified by its DHCP ID. The response object contains configuration settings for the assignment of IP addresses to devices on a Private Network attached to a Public Gateway. Note that the response does not contain the IDs of any Private Network / Public Gateway the configuration is attached to. Use the `List Public Gateway connections to Private Networks` method for that purpose, filtering on DHCP ID.
        :param dhcp_id: ID of the DHCP configuration to fetch.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`DHCP <DHCP>`

        Usage:
        ::

            result = await api.get_dhcp(
                dhcp_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_dhcp_id = validate_path_param("dhcp_id", dhcp_id)

        res = self._request(
            "GET",
            f"/vpc-gw/v1/zones/{param_zone}/dhcps/{param_dhcp_id}",
        )

        self._throw_on_error(res)
        return unmarshal_DHCP(res.json())

    async def create_dhcp(
        self,
        *,
        subnet: str,
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
        address: Optional[str] = None,
        pool_low: Optional[str] = None,
        pool_high: Optional[str] = None,
        enable_dynamic: Optional[bool] = None,
        valid_lifetime: Optional[str] = None,
        renew_timer: Optional[str] = None,
        rebind_timer: Optional[str] = None,
        push_default_route: Optional[bool] = None,
        push_dns_server: Optional[bool] = None,
        dns_servers_override: Optional[List[str]] = None,
        dns_search: Optional[List[str]] = None,
        dns_local_name: Optional[str] = None,
    ) -> DHCP:
        """
        Create a DHCP configuration.
        Create a new DHCP configuration object, containing settings for the assignment of IP addresses to devices on a Private Network attached to a Public Gateway. The response object includes the ID of the DHCP configuration object. You can use this ID as part of a call to `Create a Public Gateway connection to a Private Network` or `Update a Public Gateway connection to a Private Network` to directly apply this DHCP configuration.
        :param subnet: Subnet for the DHCP server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project to create the DHCP configuration in.
        :param address: IP address of the DHCP server. This will be the gateway's address in the Private Network. Defaults to the first address of the subnet.
        :param pool_low: Low IP (inclusive) of the dynamic address pool. Must be in the config's subnet. Defaults to the second address of the subnet.
        :param pool_high: High IP (inclusive) of the dynamic address pool. Must be in the config's subnet. Defaults to the last address of the subnet.
        :param enable_dynamic: Defines whether to enable dynamic pooling of IPs. When false, only pre-existing DHCP reservations will be handed out. Defaults to true.
        :param valid_lifetime: How long DHCP entries will be valid for. Defaults to 1h (3600s).
        :param renew_timer: After how long a renew will be attempted. Must be 30s lower than `rebind_timer`. Defaults to 50m (3000s).
        :param rebind_timer: After how long a DHCP client will query for a new lease if previous renews fail. Must be 30s lower than `valid_lifetime`. Defaults to 51m (3060s).
        :param push_default_route: Defines whether the gateway should push a default route to DHCP clients or only hand out IPs. Defaults to true.
        :param push_dns_server: Defines whether the gateway should push custom DNS servers to clients. This allows for Instance hostname -> IP resolution. Defaults to true.
        :param dns_servers_override: Array of DNS server IP addresses used to override the DNS server list pushed to DHCP clients, instead of the gateway itself.
        :param dns_search: Array of search paths in addition to the pushed DNS configuration.
        :param dns_local_name: TLD given to hostnames in the Private Network. Allowed characters are `a-z0-9-.`. Defaults to the slugified Private Network name if created along a GatewayNetwork, or else to `priv`.
        :return: :class:`DHCP <DHCP>`

        Usage:
        ::

            result = await api.create_dhcp(
                subnet="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/vpc-gw/v1/zones/{param_zone}/dhcps",
            body=marshal_CreateDHCPRequest(
                CreateDHCPRequest(
                    subnet=subnet,
                    zone=zone,
                    project_id=project_id,
                    address=address,
                    pool_low=pool_low,
                    pool_high=pool_high,
                    enable_dynamic=enable_dynamic,
                    valid_lifetime=valid_lifetime,
                    renew_timer=renew_timer,
                    rebind_timer=rebind_timer,
                    push_default_route=push_default_route,
                    push_dns_server=push_dns_server,
                    dns_servers_override=dns_servers_override,
                    dns_search=dns_search,
                    dns_local_name=dns_local_name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DHCP(res.json())

    async def update_dhcp(
        self,
        *,
        dhcp_id: str,
        zone: Optional[Zone] = None,
        subnet: Optional[str] = None,
        address: Optional[str] = None,
        pool_low: Optional[str] = None,
        pool_high: Optional[str] = None,
        enable_dynamic: Optional[bool] = None,
        valid_lifetime: Optional[str] = None,
        renew_timer: Optional[str] = None,
        rebind_timer: Optional[str] = None,
        push_default_route: Optional[bool] = None,
        push_dns_server: Optional[bool] = None,
        dns_servers_override: Optional[List[str]] = None,
        dns_search: Optional[List[str]] = None,
        dns_local_name: Optional[str] = None,
    ) -> DHCP:
        """
        Update a DHCP configuration.
        Update a DHCP configuration object, identified by its DHCP ID.
        :param dhcp_id: DHCP configuration to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param subnet: Subnet for the DHCP server.
        :param address: IP address of the DHCP server. This will be the Public Gateway's address in the Private Network. It must be part of config's subnet.
        :param pool_low: Low IP (inclusive) of the dynamic address pool. Must be in the config's subnet.
        :param pool_high: High IP (inclusive) of the dynamic address pool. Must be in the config's subnet.
        :param enable_dynamic: Defines whether to enable dynamic pooling of IPs. When false, only pre-existing DHCP reservations will be handed out. Defaults to true.
        :param valid_lifetime: How long DHCP entries will be valid for.
        :param renew_timer: After how long a renew will be attempted. Must be 30s lower than `rebind_timer`.
        :param rebind_timer: After how long a DHCP client will query for a new lease if previous renews fail. Must be 30s lower than `valid_lifetime`.
        :param push_default_route: Defines whether the gateway should push a default route to DHCP clients, or only hand out IPs.
        :param push_dns_server: Defines whether the gateway should push custom DNS servers to clients. This allows for instance hostname -> IP resolution.
        :param dns_servers_override: Array of DNS server IP addresses used to override the DNS server list pushed to DHCP clients, instead of the gateway itself.
        :param dns_search: Array of search paths in addition to the pushed DNS configuration.
        :param dns_local_name: TLD given to hostnames in the Private Networks. If an instance with hostname `foo` gets a lease, and this is set to `bar`, `foo.bar` will resolve. Allowed characters are `a-z0-9-.`.
        :return: :class:`DHCP <DHCP>`

        Usage:
        ::

            result = await api.update_dhcp(
                dhcp_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_dhcp_id = validate_path_param("dhcp_id", dhcp_id)

        res = self._request(
            "PATCH",
            f"/vpc-gw/v1/zones/{param_zone}/dhcps/{param_dhcp_id}",
            body=marshal_UpdateDHCPRequest(
                UpdateDHCPRequest(
                    dhcp_id=dhcp_id,
                    zone=zone,
                    subnet=subnet,
                    address=address,
                    pool_low=pool_low,
                    pool_high=pool_high,
                    enable_dynamic=enable_dynamic,
                    valid_lifetime=valid_lifetime,
                    renew_timer=renew_timer,
                    rebind_timer=rebind_timer,
                    push_default_route=push_default_route,
                    push_dns_server=push_dns_server,
                    dns_servers_override=dns_servers_override,
                    dns_search=dns_search,
                    dns_local_name=dns_local_name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DHCP(res.json())

    async def delete_dhcp(
        self,
        *,
        dhcp_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a DHCP configuration.
        Delete a DHCP configuration object, identified by its DHCP ID. Note that you cannot delete a DHCP configuration object that is currently being used by a Gateway Network.
        :param dhcp_id: DHCP configuration ID to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_dhcp(
                dhcp_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_dhcp_id = validate_path_param("dhcp_id", dhcp_id)

        res = self._request(
            "DELETE",
            f"/vpc-gw/v1/zones/{param_zone}/dhcps/{param_dhcp_id}",
        )

        self._throw_on_error(res)

    async def list_dhcp_entries(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListDHCPEntriesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        gateway_network_id: Optional[str] = None,
        mac_address: Optional[str] = None,
        ip_address: Optional[str] = None,
        hostname: Optional[str] = None,
        type_: Optional[DHCPEntryType] = None,
    ) -> ListDHCPEntriesResponse:
        """
        List DHCP entries.
        List DHCP entries, whether dynamically assigned and/or statically reserved. DHCP entries can be filtered by the Gateway Network they are on, their MAC address, IP address, type or hostname.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: DHCP entries per page.
        :param gateway_network_id: Filter for entries on this GatewayNetwork.
        :param mac_address: Filter for entries with this MAC address.
        :param ip_address: Filter for entries with this IP address.
        :param hostname: Filter for entries with this hostname substring.
        :param type_: Filter for entries of this type.
        :return: :class:`ListDHCPEntriesResponse <ListDHCPEntriesResponse>`

        Usage:
        ::

            result = await api.list_dhcp_entries()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/vpc-gw/v1/zones/{param_zone}/dhcp-entries",
            params={
                "gateway_network_id": gateway_network_id,
                "hostname": hostname,
                "ip_address": ip_address,
                "mac_address": mac_address,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "type": type_,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDHCPEntriesResponse(res.json())

    async def list_dhcp_entries_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListDHCPEntriesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        gateway_network_id: Optional[str] = None,
        mac_address: Optional[str] = None,
        ip_address: Optional[str] = None,
        hostname: Optional[str] = None,
        type_: Optional[DHCPEntryType] = None,
    ) -> List[DHCPEntry]:
        """
        List DHCP entries.
        List DHCP entries, whether dynamically assigned and/or statically reserved. DHCP entries can be filtered by the Gateway Network they are on, their MAC address, IP address, type or hostname.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: DHCP entries per page.
        :param gateway_network_id: Filter for entries on this GatewayNetwork.
        :param mac_address: Filter for entries with this MAC address.
        :param ip_address: Filter for entries with this IP address.
        :param hostname: Filter for entries with this hostname substring.
        :param type_: Filter for entries of this type.
        :return: :class:`List[DHCPEntry] <List[DHCPEntry]>`

        Usage:
        ::

            result = await api.list_dhcp_entries_all()
        """

        return await fetch_all_pages_async(
            type=ListDHCPEntriesResponse,
            key="dhcp_entries",
            fetcher=self.list_dhcp_entries,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "gateway_network_id": gateway_network_id,
                "mac_address": mac_address,
                "ip_address": ip_address,
                "hostname": hostname,
                "type_": type_,
            },
        )

    async def get_dhcp_entry(
        self,
        *,
        dhcp_entry_id: str,
        zone: Optional[Zone] = None,
    ) -> DHCPEntry:
        """
        Get a DHCP entry.
        Get a DHCP entry, specified by its DHCP entry ID.
        :param dhcp_entry_id: ID of the DHCP entry to fetch.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`DHCPEntry <DHCPEntry>`

        Usage:
        ::

            result = await api.get_dhcp_entry(
                dhcp_entry_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_dhcp_entry_id = validate_path_param("dhcp_entry_id", dhcp_entry_id)

        res = self._request(
            "GET",
            f"/vpc-gw/v1/zones/{param_zone}/dhcp-entries/{param_dhcp_entry_id}",
        )

        self._throw_on_error(res)
        return unmarshal_DHCPEntry(res.json())

    async def create_dhcp_entry(
        self,
        *,
        gateway_network_id: str,
        mac_address: str,
        ip_address: str,
        zone: Optional[Zone] = None,
    ) -> DHCPEntry:
        """
        Create a DHCP entry.
        Create a static DHCP reservation, specifying the Gateway Network for the reservation, the MAC address of the target device and the IP address to assign this device. The response is a DHCP entry object, confirming the ID and configuration details of the static DHCP reservation.
        :param gateway_network_id: GatewayNetwork on which to create a DHCP reservation.
        :param mac_address: MAC address to give a static entry to.
        :param ip_address: IP address to give to the device.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`DHCPEntry <DHCPEntry>`

        Usage:
        ::

            result = await api.create_dhcp_entry(
                gateway_network_id="example",
                mac_address="example",
                ip_address="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/vpc-gw/v1/zones/{param_zone}/dhcp-entries",
            body=marshal_CreateDHCPEntryRequest(
                CreateDHCPEntryRequest(
                    gateway_network_id=gateway_network_id,
                    mac_address=mac_address,
                    ip_address=ip_address,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DHCPEntry(res.json())

    async def update_dhcp_entry(
        self,
        *,
        dhcp_entry_id: str,
        zone: Optional[Zone] = None,
        ip_address: Optional[str] = None,
    ) -> DHCPEntry:
        """
        Update a DHCP entry.
        Update the IP address for a DHCP entry, specified by its DHCP entry ID. You can update an existing DHCP entry of any type (`reservation` (static), `lease` (dynamic) or `unknown`), but in manually updating the IP address the entry will necessarily be of type `reservation` after the update.
        :param dhcp_entry_id: ID of the DHCP entry to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param ip_address: New IP address to give to the device.
        :return: :class:`DHCPEntry <DHCPEntry>`

        Usage:
        ::

            result = await api.update_dhcp_entry(
                dhcp_entry_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_dhcp_entry_id = validate_path_param("dhcp_entry_id", dhcp_entry_id)

        res = self._request(
            "PATCH",
            f"/vpc-gw/v1/zones/{param_zone}/dhcp-entries/{param_dhcp_entry_id}",
            body=marshal_UpdateDHCPEntryRequest(
                UpdateDHCPEntryRequest(
                    dhcp_entry_id=dhcp_entry_id,
                    zone=zone,
                    ip_address=ip_address,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DHCPEntry(res.json())

    async def set_dhcp_entries(
        self,
        *,
        gateway_network_id: str,
        zone: Optional[Zone] = None,
        dhcp_entries: Optional[List[SetDHCPEntriesRequestEntry]] = None,
    ) -> SetDHCPEntriesResponse:
        """
        Set all DHCP reservations on a Gateway Network.
        Set the list of DHCP reservations attached to a Gateway Network. Reservations are identified by their MAC address, and will sync the current DHCP entry list to the given list, creating, updating or deleting DHCP entries accordingly.
        :param gateway_network_id: ID of the Gateway Network on which to set DHCP reservation list.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param dhcp_entries: New list of DHCP reservations.
        :return: :class:`SetDHCPEntriesResponse <SetDHCPEntriesResponse>`

        Usage:
        ::

            result = await api.set_dhcp_entries(
                gateway_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "PUT",
            f"/vpc-gw/v1/zones/{param_zone}/dhcp-entries",
            body=marshal_SetDHCPEntriesRequest(
                SetDHCPEntriesRequest(
                    gateway_network_id=gateway_network_id,
                    zone=zone,
                    dhcp_entries=dhcp_entries,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetDHCPEntriesResponse(res.json())

    async def delete_dhcp_entry(
        self,
        *,
        dhcp_entry_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a DHCP entry.
        Delete a static DHCP reservation, identified by its DHCP entry ID. Note that you cannot delete DHCP entries of type `lease`, these are deleted automatically when their time-to-live expires.
        :param dhcp_entry_id: ID of the DHCP entry to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_dhcp_entry(
                dhcp_entry_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_dhcp_entry_id = validate_path_param("dhcp_entry_id", dhcp_entry_id)

        res = self._request(
            "DELETE",
            f"/vpc-gw/v1/zones/{param_zone}/dhcp-entries/{param_dhcp_entry_id}",
        )

        self._throw_on_error(res)

    async def list_pat_rules(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListPATRulesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        gateway_id: Optional[str] = None,
        private_ip: Optional[str] = None,
        protocol: Optional[PATRuleProtocol] = None,
    ) -> ListPATRulesResponse:
        """
        List PAT rules.
        List PAT rules. You can filter by gateway ID to list all PAT rules for a particular gateway, or filter for PAT rules targeting a specific IP address or using a specific protocol.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: PAT rules per page.
        :param gateway_id: Filter for PAT rules on this Gateway.
        :param private_ip: Filter for PAT rules targeting this private ip.
        :param protocol: Filter for PAT rules with this protocol.
        :return: :class:`ListPATRulesResponse <ListPATRulesResponse>`

        Usage:
        ::

            result = await api.list_pat_rules()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/vpc-gw/v1/zones/{param_zone}/pat-rules",
            params={
                "gateway_id": gateway_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "private_ip": private_ip,
                "protocol": protocol,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPATRulesResponse(res.json())

    async def list_pat_rules_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListPATRulesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        gateway_id: Optional[str] = None,
        private_ip: Optional[str] = None,
        protocol: Optional[PATRuleProtocol] = None,
    ) -> List[PATRule]:
        """
        List PAT rules.
        List PAT rules. You can filter by gateway ID to list all PAT rules for a particular gateway, or filter for PAT rules targeting a specific IP address or using a specific protocol.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: PAT rules per page.
        :param gateway_id: Filter for PAT rules on this Gateway.
        :param private_ip: Filter for PAT rules targeting this private ip.
        :param protocol: Filter for PAT rules with this protocol.
        :return: :class:`List[PATRule] <List[PATRule]>`

        Usage:
        ::

            result = await api.list_pat_rules_all()
        """

        return await fetch_all_pages_async(
            type=ListPATRulesResponse,
            key="pat_rules",
            fetcher=self.list_pat_rules,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "gateway_id": gateway_id,
                "private_ip": private_ip,
                "protocol": protocol,
            },
        )

    async def get_pat_rule(
        self,
        *,
        pat_rule_id: str,
        zone: Optional[Zone] = None,
    ) -> PATRule:
        """
        Get a PAT rule.
        Get a PAT rule, specified by its PAT rule ID. The response object gives full details of the PAT rule, including the Public Gateway it belongs to and the configuration settings in terms of public / private ports, private IP and protocol.
        :param pat_rule_id: ID of the PAT rule to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`PATRule <PATRule>`

        Usage:
        ::

            result = await api.get_pat_rule(
                pat_rule_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_pat_rule_id = validate_path_param("pat_rule_id", pat_rule_id)

        res = self._request(
            "GET",
            f"/vpc-gw/v1/zones/{param_zone}/pat-rules/{param_pat_rule_id}",
        )

        self._throw_on_error(res)
        return unmarshal_PATRule(res.json())

    async def create_pat_rule(
        self,
        *,
        gateway_id: str,
        public_port: int,
        private_ip: str,
        private_port: int,
        zone: Optional[Zone] = None,
        protocol: Optional[PATRuleProtocol] = None,
    ) -> PATRule:
        """
        Create a PAT rule.
        Create a new PAT rule on a specified Public Gateway, defining the protocol to use, public port to listen on, and private port / IP address to map to.
        :param gateway_id: ID of the Gateway on which to create the rule.
        :param public_port: Public port to listen on.
        :param private_ip: Private IP to forward data to.
        :param private_port: Private port to translate to.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param protocol: Protocol the rule should apply to.
        :return: :class:`PATRule <PATRule>`

        Usage:
        ::

            result = await api.create_pat_rule(
                gateway_id="example",
                public_port=1,
                private_ip="example",
                private_port=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/vpc-gw/v1/zones/{param_zone}/pat-rules",
            body=marshal_CreatePATRuleRequest(
                CreatePATRuleRequest(
                    gateway_id=gateway_id,
                    public_port=public_port,
                    private_ip=private_ip,
                    private_port=private_port,
                    zone=zone,
                    protocol=protocol,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PATRule(res.json())

    async def update_pat_rule(
        self,
        *,
        pat_rule_id: str,
        zone: Optional[Zone] = None,
        public_port: Optional[int] = None,
        private_ip: Optional[str] = None,
        private_port: Optional[int] = None,
        protocol: Optional[PATRuleProtocol] = None,
    ) -> PATRule:
        """
        Update a PAT rule.
        Update a PAT rule, specified by its PAT rule ID. Configuration settings including private/public port, private IP address and protocol can all be updated.
        :param pat_rule_id: ID of the PAT rule to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param public_port: Public port to listen on.
        :param private_ip: Private IP to forward data to.
        :param private_port: Private port to translate to.
        :param protocol: Protocol the rule should apply to.
        :return: :class:`PATRule <PATRule>`

        Usage:
        ::

            result = await api.update_pat_rule(
                pat_rule_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_pat_rule_id = validate_path_param("pat_rule_id", pat_rule_id)

        res = self._request(
            "PATCH",
            f"/vpc-gw/v1/zones/{param_zone}/pat-rules/{param_pat_rule_id}",
            body=marshal_UpdatePATRuleRequest(
                UpdatePATRuleRequest(
                    pat_rule_id=pat_rule_id,
                    zone=zone,
                    public_port=public_port,
                    private_ip=private_ip,
                    private_port=private_port,
                    protocol=protocol,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PATRule(res.json())

    async def set_pat_rules(
        self,
        *,
        gateway_id: str,
        pat_rules: List[SetPATRulesRequestRule],
        zone: Optional[Zone] = None,
    ) -> SetPATRulesResponse:
        """
        Set all PAT rules.
        Set a definitive list of PAT rules attached to a Public Gateway. Each rule is identified by its public port and protocol. This will sync the current PAT rule list on the gateway with the new list, creating, updating or deleting PAT rules accordingly.
        :param gateway_id: ID of the gateway on which to set the PAT rules.
        :param pat_rules: New list of PAT rules.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`SetPATRulesResponse <SetPATRulesResponse>`

        Usage:
        ::

            result = await api.set_pat_rules(
                gateway_id="example",
                pat_rules=[],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "PUT",
            f"/vpc-gw/v1/zones/{param_zone}/pat-rules",
            body=marshal_SetPATRulesRequest(
                SetPATRulesRequest(
                    gateway_id=gateway_id,
                    pat_rules=pat_rules,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetPATRulesResponse(res.json())

    async def delete_pat_rule(
        self,
        *,
        pat_rule_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a PAT rule.
        Delete a PAT rule, identified by its PAT rule ID. This action is irreversible.
        :param pat_rule_id: ID of the PAT rule to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_pat_rule(
                pat_rule_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_pat_rule_id = validate_path_param("pat_rule_id", pat_rule_id)

        res = self._request(
            "DELETE",
            f"/vpc-gw/v1/zones/{param_zone}/pat-rules/{param_pat_rule_id}",
        )

        self._throw_on_error(res)

    async def list_gateway_types(
        self,
        *,
        zone: Optional[Zone] = None,
    ) -> ListGatewayTypesResponse:
        """
        List Public Gateway types.
        List the different Public Gateway commercial offer types available at Scaleway. The response is an array of objects describing the name and technical details of each available gateway type.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ListGatewayTypesResponse <ListGatewayTypesResponse>`

        Usage:
        ::

            result = await api.list_gateway_types()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/vpc-gw/v1/zones/{param_zone}/gateway-types",
        )

        self._throw_on_error(res)
        return unmarshal_ListGatewayTypesResponse(res.json())

    async def list_i_ps(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListIPsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        reverse: Optional[str] = None,
        is_free: Optional[bool] = None,
    ) -> ListIPsResponse:
        """
        List IPs.
        List Public Gateway flexible IP addresses. A number of filter options are available for limiting results in the response.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: IP addresses per page.
        :param organization_id: Filter for IP addresses in this Organization.
        :param project_id: Filter for IP addresses in this Project.
        :param tags: Filter for IP addresses with these tags.
        :param reverse: Filter for IP addresses that have a reverse containing this string.
        :param is_free: Filter based on whether the IP is attached to a gateway or not.
        :return: :class:`ListIPsResponse <ListIPsResponse>`

        Usage:
        ::

            result = await api.list_i_ps()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/vpc-gw/v1/zones/{param_zone}/ips",
            params={
                "is_free": is_free,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "reverse": reverse,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListIPsResponse(res.json())

    async def list_i_ps_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListIPsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        reverse: Optional[str] = None,
        is_free: Optional[bool] = None,
    ) -> List[IP]:
        """
        List IPs.
        List Public Gateway flexible IP addresses. A number of filter options are available for limiting results in the response.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: IP addresses per page.
        :param organization_id: Filter for IP addresses in this Organization.
        :param project_id: Filter for IP addresses in this Project.
        :param tags: Filter for IP addresses with these tags.
        :param reverse: Filter for IP addresses that have a reverse containing this string.
        :param is_free: Filter based on whether the IP is attached to a gateway or not.
        :return: :class:`List[IP] <List[IP]>`

        Usage:
        ::

            result = await api.list_i_ps_all()
        """

        return await fetch_all_pages_async(
            type=ListIPsResponse,
            key="ips",
            fetcher=self.list_i_ps,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "project_id": project_id,
                "tags": tags,
                "reverse": reverse,
                "is_free": is_free,
            },
        )

    async def get_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[Zone] = None,
    ) -> IP:
        """
        Get an IP.
        Get details of a Public Gateway flexible IP address, identified by its IP ID. The response object contains information including which (if any) Public Gateway using this IP address, the reverse and various other metadata.
        :param ip_id: ID of the IP address to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = await api.get_ip(
                ip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "GET",
            f"/vpc-gw/v1/zones/{param_zone}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    async def create_ip(
        self,
        *,
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> IP:
        """
        Reserve an IP.
        Create (reserve) a new flexible IP address that can be used for a Public Gateway in a specified Scaleway Project.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project to create the IP address in.
        :param tags: Tags to give to the IP address.
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = await api.create_ip()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/vpc-gw/v1/zones/{param_zone}/ips",
            body=marshal_CreateIPRequest(
                CreateIPRequest(
                    zone=zone,
                    project_id=project_id,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    async def update_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[Zone] = None,
        tags: Optional[List[str]] = None,
        reverse: Optional[str] = None,
        gateway_id: Optional[str] = None,
    ) -> IP:
        """
        Update an IP.
        Update details of an existing flexible IP address, including its tags, reverse and the Public Gateway it is assigned to.
        :param ip_id: ID of the IP address to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param tags: Tags to give to the IP address.
        :param reverse: Reverse to set on the address. Empty string to unset.
        :param gateway_id: Gateway to attach the IP address to. Empty string to detach.
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = await api.update_ip(
                ip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "PATCH",
            f"/vpc-gw/v1/zones/{param_zone}/ips/{param_ip_id}",
            body=marshal_UpdateIPRequest(
                UpdateIPRequest(
                    ip_id=ip_id,
                    zone=zone,
                    tags=tags,
                    reverse=reverse,
                    gateway_id=gateway_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    async def delete_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete an IP.
        Delete a flexible IP address from your account. This action is irreversible.
        :param ip_id: ID of the IP address to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_ip(
                ip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "DELETE",
            f"/vpc-gw/v1/zones/{param_zone}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)

    async def refresh_ssh_keys(
        self,
        *,
        gateway_id: str,
        zone: Optional[Zone] = None,
    ) -> Gateway:
        """
        Refresh a Public Gateway's SSH keys.
        Refresh the SSH keys of a given Public Gateway, specified by its gateway ID. This adds any new SSH keys in the gateway's Scaleway Project to the gateway itself.
        :param gateway_id: ID of the gateway to refresh SSH keys on.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = await api.refresh_ssh_keys(
                gateway_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "POST",
            f"/vpc-gw/v1/zones/{param_zone}/gateways/{param_gateway_id}/refresh-ssh-keys",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Gateway(res.json())
