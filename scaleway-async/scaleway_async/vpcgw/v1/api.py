# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages_async,
    random_name,
    validate_path_param,
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
    SetDHCPEntriesRequestEntry,
    SetDHCPEntriesResponse,
    SetPATRulesRequestRule,
    SetPATRulesResponse,
    CreateGatewayRequest,
    UpdateGatewayRequest,
    CreateGatewayNetworkRequest,
    UpdateGatewayNetworkRequest,
    CreateDHCPRequest,
    UpdateDHCPRequest,
    CreateDHCPEntryRequest,
    UpdateDHCPEntryRequest,
    SetDHCPEntriesRequest,
    CreatePATRuleRequest,
    UpdatePATRuleRequest,
    SetPATRulesRequest,
    CreateIPRequest,
    UpdateIPRequest,
)
from .content import (
    GATEWAY_NETWORK_TRANSIENT_STATUSES,
    GATEWAY_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_CreateDHCPEntryRequest,
    marshal_CreateDHCPRequest,
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
)


class VpcgwV1API(API):
    """
    VPC Public Gateway API.
    """

    async def list_gateways(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: ListGatewaysRequestOrderBy = ListGatewaysRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        type_: Optional[str] = None,
        status: GatewayStatus = GatewayStatus.UNKNOWN,
        private_network_id: Optional[str] = None,
    ) -> ListGatewaysResponse:
        """
        List VPC Public Gateways
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Order in which to return results
        :param page: Page number
        :param page_size: Gateways per page
        :param organization_id: Include only gateways in this organization
        :param project_id: Include only gateways in this project
        :param name: Filter gateways including this name
        :param tags: Filter gateways with these tags
        :param type_: Filter gateways of this type
        :param status: Filter gateways in this status (unknown for any)
        :param private_network_id: Filter gateways attached to this private network
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
        List VPC Public Gateways
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Order in which to return results
        :param page: Page number
        :param page_size: Gateways per page
        :param organization_id: Include only gateways in this organization
        :param project_id: Include only gateways in this project
        :param name: Filter gateways including this name
        :param tags: Filter gateways with these tags
        :param type_: Filter gateways of this type
        :param status: Filter gateways in this status (unknown for any)
        :param private_network_id: Filter gateways attached to this private network
        :return: :class:`List[ListGatewaysResponse] <List[ListGatewaysResponse]>`

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
        Get a VPC Public Gateway
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param gateway_id: ID of the gateway to fetch
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = await api.get_gateway(gateway_id="example")
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
        Waits for :class:`Gateway <Gateway>` to be in a final state.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param gateway_id: ID of the gateway to fetch
        :param options: The options for the waiter
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = api.wait_for_gateway(gateway_id="example")
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
        Create a VPC Public Gateway
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param project_id: Project to create the gateway into
        :param name: Name of the gateway
        :param tags: Tags for the gateway
        :param type_: Gateway type
        :param upstream_dns_servers: Override the gateway's default recursive DNS servers, if DNS features are enabled
        :param ip_id: Attach an existing IP to the gateway
        :param enable_smtp: Allow SMTP traffic to pass through the gateway
        :param enable_bastion: Enable SSH bastion on the gateway
        :param bastion_port: Port of the SSH bastion
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = await api.create_gateway(
                type_="example",
                enable_smtp=True,
                enable_bastion=True,
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
        Update a VPC Public Gateway
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param gateway_id: ID of the gateway to update
        :param name: Name fo the gateway
        :param tags: Tags for the gateway
        :param upstream_dns_servers: Override the gateway's default recursive DNS servers, if DNS features are enabled
        :param enable_bastion: Enable SSH bastion on the gateway
        :param bastion_port: Port of the SSH bastion
        :param enable_smtp: Allow SMTP traffic to pass through the gateway
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = await api.update_gateway(gateway_id="example")
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
    ) -> Optional[None]:
        """
        Delete a VPC Public Gateway
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param gateway_id: ID of the gateway to delete
        :param cleanup_dhcp: Whether to cleanup attached DHCP configurations (if any, and if not attached to another Gateway Network).


        Usage:
        ::

            result = await api.delete_gateway(
                gateway_id="example",
                cleanup_dhcp=True,
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
        return None

    async def upgrade_gateway(
        self,
        *,
        gateway_id: str,
        zone: Optional[Zone] = None,
    ) -> Gateway:
        """
        Upgrade a VPC Public Gateway to the latest version
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param gateway_id: ID of the gateway to upgrade
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = await api.upgrade_gateway(gateway_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "POST",
            f"/vpc-gw/v1/zones/{param_zone}/gateways/{param_gateway_id}/upgrade",
        )

        self._throw_on_error(res)
        return unmarshal_Gateway(res.json())

    async def list_gateway_networks(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: ListGatewayNetworksRequestOrderBy = ListGatewayNetworksRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        gateway_id: Optional[str] = None,
        private_network_id: Optional[str] = None,
        enable_masquerade: Optional[bool] = None,
        dhcp_id: Optional[str] = None,
        status: GatewayNetworkStatus = GatewayNetworkStatus.UNKNOWN,
    ) -> ListGatewayNetworksResponse:
        """
        List gateway connections to Private Networks
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Order in which to return results
        :param page: Page number
        :param page_size: GatewayNetworks per page
        :param gateway_id: Filter by gateway
        :param private_network_id: Filter by private network
        :param enable_masquerade: Filter by masquerade enablement
        :param dhcp_id: Filter by DHCP configuration
        :param status: Filter GatewayNetworks by this status (unknown for any)
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
        List gateway connections to Private Networks
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Order in which to return results
        :param page: Page number
        :param page_size: GatewayNetworks per page
        :param gateway_id: Filter by gateway
        :param private_network_id: Filter by private network
        :param enable_masquerade: Filter by masquerade enablement
        :param dhcp_id: Filter by DHCP configuration
        :param status: Filter GatewayNetworks by this status (unknown for any)
        :return: :class:`List[ListGatewayNetworksResponse] <List[ListGatewayNetworksResponse]>`

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
        Get a gateway connection to a Private Network
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param gateway_network_id: ID of the GatewayNetwork to fetch
        :return: :class:`GatewayNetwork <GatewayNetwork>`

        Usage:
        ::

            result = await api.get_gateway_network(gateway_network_id="example")
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
        Waits for :class:`GatewayNetwork <GatewayNetwork>` to be in a final state.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param gateway_network_id: ID of the GatewayNetwork to fetch
        :param options: The options for the waiter
        :return: :class:`GatewayNetwork <GatewayNetwork>`

        Usage:
        ::

            result = api.wait_for_gateway_network(gateway_network_id="example")
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
        dhcp_id: Optional[str] = None,
        address: Optional[str] = None,
        enable_dhcp: Optional[bool] = None,
    ) -> GatewayNetwork:
        """
        Attach a gateway to a Private Network
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param gateway_id: Gateway to connect
        :param private_network_id: Private Network to connect
        :param enable_masquerade: Whether to enable masquerade on this network
        :param dhcp_id: Existing configuration.

        One-of ('ip_config'): at most one of 'dhcp_id', 'address' could be set.
        :param address: Static IP address in CIDR format to to use without DHCP.

        One-of ('ip_config'): at most one of 'dhcp_id', 'address' could be set.
        :param enable_dhcp: Whether to enable DHCP on this Private Network. Defaults to `true` if either `dhcp_id` or `dhcp` short: are present. If set to `true`, requires that either `dhcp_id` or `dhcp` to be present.

        :return: :class:`GatewayNetwork <GatewayNetwork>`

        Usage:
        ::

            result = await api.create_gateway_network(
                gateway_id="example",
                private_network_id="example",
                enable_masquerade=True,
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
                    dhcp_id=dhcp_id,
                    address=address,
                    enable_dhcp=enable_dhcp,
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
        dhcp_id: Optional[str] = None,
        enable_dhcp: Optional[bool] = None,
        address: Optional[str] = None,
    ) -> GatewayNetwork:
        """
        Update a gateway connection to a Private Network
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param gateway_network_id: ID of the GatewayNetwork to update
        :param enable_masquerade: New masquerade enablement
        :param dhcp_id: New DHCP configuration.

        One-of ('ip_config'): at most one of 'dhcp_id', 'address' could be set.
        :param enable_dhcp: Whether to enable DHCP on the connected Private Network
        :param address: New static IP address.

        One-of ('ip_config'): at most one of 'dhcp_id', 'address' could be set.
        :return: :class:`GatewayNetwork <GatewayNetwork>`

        Usage:
        ::

            result = await api.update_gateway_network(gateway_network_id="example")
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
                    dhcp_id=dhcp_id,
                    enable_dhcp=enable_dhcp,
                    address=address,
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
    ) -> Optional[None]:
        """
        Detach a gateway from a Private Network
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param gateway_network_id: GatewayNetwork to delete
        :param cleanup_dhcp: Whether to cleanup the attached DHCP configuration (if any, and if not attached to another gateway_network).


        Usage:
        ::

            result = await api.delete_gateway_network(
                gateway_network_id="example",
                cleanup_dhcp=True,
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
        return None

    async def list_dhc_ps(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: ListDHCPsRequestOrderBy = ListDHCPsRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        address: Optional[str] = None,
        has_address: Optional[str] = None,
    ) -> ListDHCPsResponse:
        """
        List DHCP configurations
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Order in which to return results
        :param page: Page number
        :param page_size: DHCP configurations per page
        :param organization_id: Include only DHCPs in this organization
        :param project_id: Include only DHCPs in this project
        :param address: Filter on gateway address
        :param has_address: Filter on subnets containing address
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
        List DHCP configurations
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Order in which to return results
        :param page: Page number
        :param page_size: DHCP configurations per page
        :param organization_id: Include only DHCPs in this organization
        :param project_id: Include only DHCPs in this project
        :param address: Filter on gateway address
        :param has_address: Filter on subnets containing address
        :return: :class:`List[ListDHCPsResponse] <List[ListDHCPsResponse]>`

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
        Get a DHCP configuration
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param dhcp_id: ID of the DHCP config to fetch
        :return: :class:`DHCP <DHCP>`

        Usage:
        ::

            result = await api.get_dhcp(dhcp_id="example")
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
        Create a DHCP configuration
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param project_id: Project to create the DHCP configuration in
        :param subnet: Subnet for the DHCP server
        :param address: Address of the DHCP server. This will be the gateway's address in the private network. Defaults to the first address of the subnet
        :param pool_low: Low IP (included) of the dynamic address pool. Defaults to the second address of the subnet.
        :param pool_high: High IP (included) of the dynamic address pool. Defaults to the last address of the subnet.
        :param enable_dynamic: Whether to enable dynamic pooling of IPs. By turning the dynamic pool off, only pre-existing DHCP reservations will be handed out. Defaults to true.

        :param valid_lifetime: For how long, in seconds, will DHCP entries will be valid. Defaults to 1h (3600s).
        :param renew_timer: After how long, in seconds, a renew will be attempted. Must be 30s lower than `rebind_timer`. Defaults to 50m (3000s).

        :param rebind_timer: After how long, in seconds, a DHCP client will query for a new lease if previous renews fail. Must be 30s lower than `valid_lifetime`. Defaults to 51m (3060s).

        :param push_default_route: Whether the gateway should push a default route to DHCP clients or only hand out IPs. Defaults to true
        :param push_dns_server: Whether the gateway should push custom DNS servers to clients. This allows for instance hostname -> IP resolution. Defaults to true.

        :param dns_servers_override: Override the DNS server list pushed to DHCP clients, instead of the gateway itself
        :param dns_search: Additional DNS search paths
        :param dns_local_name: TLD given to hostnames in the Private Network. Allowed characters are `a-z0-9-.`. Defaults to the slugified Private Network name if created along a GatewayNetwork, or else to `priv`.

        :return: :class:`DHCP <DHCP>`

        Usage:
        ::

            result = await api.create_dhcp(subnet="example")
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
        Update a DHCP configuration
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param dhcp_id: DHCP config to update
        :param subnet: Subnet for the DHCP server
        :param address: Address of the DHCP server. This will be the gateway's address in the private network
        :param pool_low: Low IP (included) of the dynamic address pool
        :param pool_high: High IP (included) of the dynamic address pool
        :param enable_dynamic: Whether to enable dynamic pooling of IPs. By turning the dynamic pool off, only pre-existing DHCP reservations will be handed out. Defaults to true.

        :param valid_lifetime: How long, in seconds, DHCP entries will be valid for
        :param renew_timer: After how long, in seconds, a renew will be attempted. Must be 30s lower than `rebind_timer`.
        :param rebind_timer: After how long, in seconds, a DHCP client will query for a new lease if previous renews fail. Must be 30s lower than `valid_lifetime`.

        :param push_default_route: Whether the gateway should push a default route to DHCP clients or only hand out IPs
        :param push_dns_server: Whether the gateway should push custom DNS servers to clients. This allows for instance hostname -> IP resolution.

        :param dns_servers_override: Override the DNS server list pushed to DHCP clients, instead of the gateway itself
        :param dns_search: Additional DNS search paths
        :param dns_local_name: TLD given to hostnames in the Private Network. Allowed characters are `a-z0-9-.`.
        :return: :class:`DHCP <DHCP>`

        Usage:
        ::

            result = await api.update_dhcp(dhcp_id="example")
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
    ) -> Optional[None]:
        """
        Delete a DHCP configuration
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param dhcp_id: DHCP config id to delete

        Usage:
        ::

            result = await api.delete_dhcp(dhcp_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_dhcp_id = validate_path_param("dhcp_id", dhcp_id)

        res = self._request(
            "DELETE",
            f"/vpc-gw/v1/zones/{param_zone}/dhcps/{param_dhcp_id}",
        )

        self._throw_on_error(res)
        return None

    async def list_dhcp_entries(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: ListDHCPEntriesRequestOrderBy = ListDHCPEntriesRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        gateway_network_id: Optional[str] = None,
        mac_address: Optional[str] = None,
        ip_address: Optional[str] = None,
        hostname: Optional[str] = None,
        type_: DHCPEntryType = DHCPEntryType.UNKNOWN,
    ) -> ListDHCPEntriesResponse:
        """
        List DHCP entries
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Order in which to return results
        :param page: Page number
        :param page_size: DHCP entries per page
        :param gateway_network_id: Filter entries based on the gateway network they are on
        :param mac_address: Filter entries on their MAC address
        :param ip_address: Filter entries on their IP address
        :param hostname: Filter entries on their hostname substring
        :param type_: Filter entries on their type
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
        List DHCP entries
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Order in which to return results
        :param page: Page number
        :param page_size: DHCP entries per page
        :param gateway_network_id: Filter entries based on the gateway network they are on
        :param mac_address: Filter entries on their MAC address
        :param ip_address: Filter entries on their IP address
        :param hostname: Filter entries on their hostname substring
        :param type_: Filter entries on their type
        :return: :class:`List[ListDHCPEntriesResponse] <List[ListDHCPEntriesResponse]>`

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
        Get DHCP entries
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param dhcp_entry_id: ID of the DHCP entry to fetch
        :return: :class:`DHCPEntry <DHCPEntry>`

        Usage:
        ::

            result = await api.get_dhcp_entry(dhcp_entry_id="example")
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
        Create a static DHCP reservation
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param gateway_network_id: GatewayNetwork on which to create a DHCP reservation
        :param mac_address: MAC address to give a static entry to
        :param ip_address: IP address to give to the machine
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
        Update a DHCP entry
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param dhcp_entry_id: DHCP entry ID to update
        :param ip_address: New IP address to give to the machine
        :return: :class:`DHCPEntry <DHCPEntry>`

        Usage:
        ::

            result = await api.update_dhcp_entry(dhcp_entry_id="example")
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
        Set the list of DHCP reservations attached to a Gateway Network. Reservations are identified by their MAC address, and will sync the current DHCP entry list to the given list, creating, updating or deleting DHCP entries.

        :param zone: Zone to target. If none is passed will use default zone from the config
        :param gateway_network_id: Gateway Network on which to set DHCP reservation list
        :param dhcp_entries: New list of DHCP reservations
        :return: :class:`SetDHCPEntriesResponse <SetDHCPEntriesResponse>`

        Usage:
        ::

            result = await api.set_dhcp_entries(gateway_network_id="example")
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
    ) -> Optional[None]:
        """
        Delete a DHCP reservation
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param dhcp_entry_id: DHCP entry ID to delete

        Usage:
        ::

            result = await api.delete_dhcp_entry(dhcp_entry_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_dhcp_entry_id = validate_path_param("dhcp_entry_id", dhcp_entry_id)

        res = self._request(
            "DELETE",
            f"/vpc-gw/v1/zones/{param_zone}/dhcp-entries/{param_dhcp_entry_id}",
        )

        self._throw_on_error(res)
        return None

    async def list_pat_rules(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: ListPATRulesRequestOrderBy = ListPATRulesRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        gateway_id: Optional[str] = None,
        private_ip: Optional[str] = None,
        protocol: PATRuleProtocol = PATRuleProtocol.UNKNOWN,
    ) -> ListPATRulesResponse:
        """
        List PAT rules
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Order in which to return results
        :param page: Page number
        :param page_size: PAT rules per page
        :param gateway_id: Fetch rules for this gateway
        :param private_ip: Fetch rules targeting this private ip
        :param protocol: Fetch rules for this protocol
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
        List PAT rules
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Order in which to return results
        :param page: Page number
        :param page_size: PAT rules per page
        :param gateway_id: Fetch rules for this gateway
        :param private_ip: Fetch rules targeting this private ip
        :param protocol: Fetch rules for this protocol
        :return: :class:`List[ListPATRulesResponse] <List[ListPATRulesResponse]>`

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
        Get a PAT rule
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param pat_rule_id: PAT rule to get
        :return: :class:`PATRule <PATRule>`

        Usage:
        ::

            result = await api.get_pat_rule(pat_rule_id="example")
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
        protocol: PATRuleProtocol,
        zone: Optional[Zone] = None,
    ) -> PATRule:
        """
        Create a PAT rule
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param gateway_id: Gateway on which to attach the rule to
        :param public_port: Public port to listen on
        :param private_ip: Private IP to forward data to
        :param private_port: Private port to translate to
        :param protocol: Protocol the rule should apply to
        :return: :class:`PATRule <PATRule>`

        Usage:
        ::

            result = await api.create_pat_rule(
                gateway_id="example",
                public_port=1,
                private_ip="example",
                private_port=1,
                protocol=unknown,
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
                    protocol=protocol,
                    zone=zone,
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
        protocol: PATRuleProtocol,
        zone: Optional[Zone] = None,
        public_port: Optional[int] = None,
        private_ip: Optional[str] = None,
        private_port: Optional[int] = None,
    ) -> PATRule:
        """
        Update a PAT rule
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param pat_rule_id: PAT rule to update
        :param public_port: Public port to listen on
        :param private_ip: Private IP to forward data to
        :param private_port: Private port to translate to
        :param protocol: Protocol the rule should apply to
        :return: :class:`PATRule <PATRule>`

        Usage:
        ::

            result = await api.update_pat_rule(
                pat_rule_id="example",
                protocol=unknown,
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
                    protocol=protocol,
                    zone=zone,
                    public_port=public_port,
                    private_ip=private_ip,
                    private_port=private_port,
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
        Set the list of PAT rules attached to a Gateway. Rules are identified by their public port and protocol. This will sync the current PAT rule list with the givent list, creating, updating or deleting PAT rules.

        :param zone: Zone to target. If none is passed will use default zone from the config
        :param gateway_id: Gateway on which to set the PAT rules
        :param pat_rules: New list of PAT rules
        :return: :class:`SetPATRulesResponse <SetPATRulesResponse>`

        Usage:
        ::

            result = await api.set_pat_rules(
                gateway_id="example",
                pat_rules=[SetPATRulesRequestRule(...)],
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
    ) -> Optional[None]:
        """
        Delete a PAT rule
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param pat_rule_id: PAT rule to delete

        Usage:
        ::

            result = await api.delete_pat_rule(pat_rule_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_pat_rule_id = validate_path_param("pat_rule_id", pat_rule_id)

        res = self._request(
            "DELETE",
            f"/vpc-gw/v1/zones/{param_zone}/pat-rules/{param_pat_rule_id}",
        )

        self._throw_on_error(res)
        return None

    async def list_gateway_types(
        self,
        *,
        zone: Optional[Zone] = None,
    ) -> ListGatewayTypesResponse:
        """
        List VPC Public Gateway types
        :param zone: Zone to target. If none is passed will use default zone from the config
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
        order_by: ListIPsRequestOrderBy = ListIPsRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        reverse: Optional[str] = None,
        is_free: Optional[bool] = None,
    ) -> ListIPsResponse:
        """
        List IPs
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Order in which to return results
        :param page: Page number
        :param page_size: IPs per page
        :param organization_id: Include only IPs in this organization
        :param project_id: Include only IPs in this project
        :param tags: Filter IPs with these tags
        :param reverse: Filter by reverse containing this string
        :param is_free: Filter whether the IP is attached to a gateway or not
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
        List IPs
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Order in which to return results
        :param page: Page number
        :param page_size: IPs per page
        :param organization_id: Include only IPs in this organization
        :param project_id: Include only IPs in this project
        :param tags: Filter IPs with these tags
        :param reverse: Filter by reverse containing this string
        :param is_free: Filter whether the IP is attached to a gateway or not
        :return: :class:`List[ListIPsResponse] <List[ListIPsResponse]>`

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
        Get an IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param ip_id: ID of the IP to get
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = await api.get_ip(ip_id="example")
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
        Reserve an IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param project_id: Project to create the IP into
        :param tags: Tags to give to the IP
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
        Update an IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param ip_id: ID of the IP to update
        :param tags: Tags to give to the IP
        :param reverse: Reverse to set on the IP. Empty string to unset
        :param gateway_id: Gateway to attach the IP to. Empty string to detach
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = await api.update_ip(ip_id="example")
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
    ) -> Optional[None]:
        """
        Delete an IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param ip_id: ID of the IP to delete

        Usage:
        ::

            result = await api.delete_ip(ip_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "DELETE",
            f"/vpc-gw/v1/zones/{param_zone}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)
        return None

    async def refresh_ssh_keys(
        self,
        *,
        gateway_id: str,
        zone: Optional[Zone] = None,
    ) -> Gateway:
        """

        Usage:
        ::

            result = await api.refresh_ssh_keys(gateway_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "POST",
            f"/vpc-gw/v1/zones/{param_zone}/gateways/{param_gateway_id}/refresh-ssh-keys",
        )

        self._throw_on_error(res)
        return unmarshal_Gateway(res.json())
