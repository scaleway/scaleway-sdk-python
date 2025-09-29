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
    ConnectionStatus,
    CreateConnectionRequestInitiationPolicy,
    ListConnectionsRequestOrderBy,
    ListCustomerGatewaysRequestOrderBy,
    ListRoutingPoliciesRequestOrderBy,
    ListVpnGatewaysRequestOrderBy,
    VpnGatewayStatus,
    Connection,
    ConnectionCipher,
    CreateConnectionRequest,
    CreateConnectionRequestBgpConfig,
    CreateConnectionResponse,
    CreateCustomerGatewayRequest,
    CreateRoutingPolicyRequest,
    CreateVpnGatewayRequest,
    CreateVpnGatewayRequestPublicConfig,
    CustomerGateway,
    DetachRoutingPolicyRequest,
    GatewayType,
    ListConnectionsResponse,
    ListCustomerGatewaysResponse,
    ListRoutingPoliciesResponse,
    ListVpnGatewayTypesResponse,
    ListVpnGatewaysResponse,
    RenewConnectionPskResponse,
    RoutingPolicy,
    SetRoutingPolicyRequest,
    UpdateConnectionRequest,
    UpdateCustomerGatewayRequest,
    UpdateRoutingPolicyRequest,
    UpdateVpnGatewayRequest,
    VpnGateway,
)
from .content import (
    VPN_GATEWAY_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Connection,
    unmarshal_CustomerGateway,
    unmarshal_RoutingPolicy,
    unmarshal_VpnGateway,
    unmarshal_CreateConnectionResponse,
    unmarshal_ListConnectionsResponse,
    unmarshal_ListCustomerGatewaysResponse,
    unmarshal_ListRoutingPoliciesResponse,
    unmarshal_ListVpnGatewayTypesResponse,
    unmarshal_ListVpnGatewaysResponse,
    unmarshal_RenewConnectionPskResponse,
    marshal_CreateConnectionRequest,
    marshal_CreateCustomerGatewayRequest,
    marshal_CreateRoutingPolicyRequest,
    marshal_CreateVpnGatewayRequest,
    marshal_DetachRoutingPolicyRequest,
    marshal_SetRoutingPolicyRequest,
    marshal_UpdateConnectionRequest,
    marshal_UpdateCustomerGatewayRequest,
    marshal_UpdateRoutingPolicyRequest,
    marshal_UpdateVpnGatewayRequest,
)


class S2SVpnV1Alpha1API(API):
    """
    This API allows you to manage your Site-to-Site VPN.
    """

    async def list_vpn_gateway_types(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListVpnGatewayTypesResponse:
        """
        List VPN gateway types.
        List the different VPN gateway commercial offer types available at Scaleway. The response is an array of objects describing the name and technical details of each available VPN gateway type.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of VPN gateway types to return per page.
        :return: :class:`ListVpnGatewayTypesResponse <ListVpnGatewayTypesResponse>`

        Usage:
        ::

            result = await api.list_vpn_gateway_types()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/vpn-gateway-types",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVpnGatewayTypesResponse(res.json())

    async def list_vpn_gateway_types_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[GatewayType]:
        """
        List VPN gateway types.
        List the different VPN gateway commercial offer types available at Scaleway. The response is an array of objects describing the name and technical details of each available VPN gateway type.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of VPN gateway types to return per page.
        :return: :class:`list[GatewayType] <list[GatewayType]>`

        Usage:
        ::

            result = await api.list_vpn_gateway_types_all()
        """

        return await fetch_all_pages_async(
            type=ListVpnGatewayTypesResponse,
            key="gateway_types",
            fetcher=self.list_vpn_gateway_types,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
            },
        )

    async def list_vpn_gateways(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListVpnGatewaysRequestOrderBy] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        statuses: Optional[list[VpnGatewayStatus]] = None,
        gateway_types: Optional[list[str]] = None,
        private_network_ids: Optional[list[str]] = None,
    ) -> ListVpnGatewaysResponse:
        """
        List VPN gateways.
        List all your VPN gateways. A number of filters are available, including Project ID, name, tags and status.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of VPN gateways to return per page.
        :param order_by: Order in which to return results.
        :param project_id: Project ID to filter for.
        :param name: VPN gateway name to filter for.
        :param tags: Tags to filter for.
        :param statuses: VPN gateway statuses to filter for.
        :param gateway_types: Filter for VPN gateways of these types.
        :param private_network_ids: Filter for VPN gateways attached to these private networks.
        :return: :class:`ListVpnGatewaysResponse <ListVpnGatewaysResponse>`

        Usage:
        ::

            result = await api.list_vpn_gateways()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/vpn-gateways",
            params={
                "gateway_types": gateway_types,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "private_network_ids": private_network_ids,
                "project_id": project_id or self.client.default_project_id,
                "statuses": statuses,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVpnGatewaysResponse(res.json())

    async def list_vpn_gateways_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListVpnGatewaysRequestOrderBy] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        statuses: Optional[list[VpnGatewayStatus]] = None,
        gateway_types: Optional[list[str]] = None,
        private_network_ids: Optional[list[str]] = None,
    ) -> list[VpnGateway]:
        """
        List VPN gateways.
        List all your VPN gateways. A number of filters are available, including Project ID, name, tags and status.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of VPN gateways to return per page.
        :param order_by: Order in which to return results.
        :param project_id: Project ID to filter for.
        :param name: VPN gateway name to filter for.
        :param tags: Tags to filter for.
        :param statuses: VPN gateway statuses to filter for.
        :param gateway_types: Filter for VPN gateways of these types.
        :param private_network_ids: Filter for VPN gateways attached to these private networks.
        :return: :class:`list[VpnGateway] <list[VpnGateway]>`

        Usage:
        ::

            result = await api.list_vpn_gateways_all()
        """

        return await fetch_all_pages_async(
            type=ListVpnGatewaysResponse,
            key="gateways",
            fetcher=self.list_vpn_gateways,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
                "name": name,
                "tags": tags,
                "statuses": statuses,
                "gateway_types": gateway_types,
                "private_network_ids": private_network_ids,
            },
        )

    async def get_vpn_gateway(
        self,
        *,
        gateway_id: str,
        region: Optional[ScwRegion] = None,
    ) -> VpnGateway:
        """
        Get a VPN gateway.
        Get a VPN gateway for the given VPN gateway ID.
        :param gateway_id: ID of the requested VPN gateway.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`VpnGateway <VpnGateway>`

        Usage:
        ::

            result = await api.get_vpn_gateway(
                gateway_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "GET",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/vpn-gateways/{param_gateway_id}",
        )

        self._throw_on_error(res)
        return unmarshal_VpnGateway(res.json())

    async def wait_for_vpn_gateway(
        self,
        *,
        gateway_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[
            WaitForOptions[VpnGateway, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> VpnGateway:
        """
        Get a VPN gateway.
        Get a VPN gateway for the given VPN gateway ID.
        :param gateway_id: ID of the requested VPN gateway.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`VpnGateway <VpnGateway>`

        Usage:
        ::

            result = await api.get_vpn_gateway(
                gateway_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in VPN_GATEWAY_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_vpn_gateway,
            options=options,
            args={
                "gateway_id": gateway_id,
                "region": region,
            },
        )

    async def create_vpn_gateway(
        self,
        *,
        name: str,
        gateway_type: str,
        private_network_id: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        public_config: Optional[CreateVpnGatewayRequestPublicConfig] = None,
        ipam_private_ipv4_id: Optional[str] = None,
        ipam_private_ipv6_id: Optional[str] = None,
        zone: Optional[ScwZone] = None,
    ) -> VpnGateway:
        """
        Create VPN gateway.
        :param name: Name of the VPN gateway.
        :param gateway_type: VPN gateway type (commercial offer type).
        :param private_network_id: ID of the Private Network to attach to the VPN gateway.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to create the VPN gateway in.
        :param tags: List of tags to apply to the VPN gateway.
        :param public_config: Public endpoint configuration of the VPN gateway.
        One-Of ('endpoint'): at most one of 'public_config' could be set.
        :param ipam_private_ipv4_id: ID of the IPAM private IPv4 address to attach to the VPN gateway.
        :param ipam_private_ipv6_id: ID of the IPAM private IPv6 address to attach to the VPN gateway.
        :param zone: Availability Zone where the VPN gateway should be provisioned. If no zone is specified, the VPN gateway will be automatically placed.
        :return: :class:`VpnGateway <VpnGateway>`

        Usage:
        ::

            result = await api.create_vpn_gateway(
                name="example",
                gateway_type="example",
                private_network_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/vpn-gateways",
            body=marshal_CreateVpnGatewayRequest(
                CreateVpnGatewayRequest(
                    name=name,
                    gateway_type=gateway_type,
                    private_network_id=private_network_id,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                    ipam_private_ipv4_id=ipam_private_ipv4_id,
                    ipam_private_ipv6_id=ipam_private_ipv6_id,
                    zone=zone,
                    public_config=public_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_VpnGateway(res.json())

    async def update_vpn_gateway(
        self,
        *,
        gateway_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> VpnGateway:
        """
        Update a VPN gateway.
        Update an existing VPN gateway, specified by its VPN gateway ID. Only its name and tags can be updated.
        :param gateway_id: ID of the VPN gateway to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the VPN gateway.
        :param tags: List of tags to apply to the VPN Gateway.
        :return: :class:`VpnGateway <VpnGateway>`

        Usage:
        ::

            result = await api.update_vpn_gateway(
                gateway_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "PATCH",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/vpn-gateways/{param_gateway_id}",
            body=marshal_UpdateVpnGatewayRequest(
                UpdateVpnGatewayRequest(
                    gateway_id=gateway_id,
                    region=region,
                    name=name,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_VpnGateway(res.json())

    async def delete_vpn_gateway(
        self,
        *,
        gateway_id: str,
        region: Optional[ScwRegion] = None,
    ) -> VpnGateway:
        """
        Delete a VPN gateway.
        Delete an existing VPN gateway, specified by its VPN gateway ID.
        :param gateway_id: ID of the VPN gateway to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`VpnGateway <VpnGateway>`

        Usage:
        ::

            result = await api.delete_vpn_gateway(
                gateway_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "DELETE",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/vpn-gateways/{param_gateway_id}",
        )

        self._throw_on_error(res)
        return unmarshal_VpnGateway(res.json())

    async def list_connections(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListConnectionsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        statuses: Optional[list[ConnectionStatus]] = None,
        is_ipv6: Optional[bool] = None,
        routing_policy_ids: Optional[list[str]] = None,
        route_propagation_enabled: Optional[bool] = None,
        vpn_gateway_ids: Optional[list[str]] = None,
        customer_gateway_ids: Optional[list[str]] = None,
    ) -> ListConnectionsResponse:
        """
        List connections.
        List all your connections. A number of filters are available, including Project ID, name, tags and status.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of connections to return per page.
        :param order_by: Order in which to return results.
        :param project_id: Project ID to filter for.
        :param name: Connection name to filter for.
        :param tags: Tags to filter for.
        :param statuses: Connection statuses to filter for.
        :param is_ipv6: Filter connections with IP version of IPSec tunnel.
        :param routing_policy_ids: Filter for connections using these routing policies.
        :param route_propagation_enabled: Filter for connections with route propagation enabled.
        :param vpn_gateway_ids: Filter for connections attached to these VPN gateways.
        :param customer_gateway_ids: Filter for connections attached to these customer gateways.
        :return: :class:`ListConnectionsResponse <ListConnectionsResponse>`

        Usage:
        ::

            result = await api.list_connections()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/connections",
            params={
                "customer_gateway_ids": customer_gateway_ids,
                "is_ipv6": is_ipv6,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "route_propagation_enabled": route_propagation_enabled,
                "routing_policy_ids": routing_policy_ids,
                "statuses": statuses,
                "tags": tags,
                "vpn_gateway_ids": vpn_gateway_ids,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListConnectionsResponse(res.json())

    async def list_connections_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListConnectionsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        statuses: Optional[list[ConnectionStatus]] = None,
        is_ipv6: Optional[bool] = None,
        routing_policy_ids: Optional[list[str]] = None,
        route_propagation_enabled: Optional[bool] = None,
        vpn_gateway_ids: Optional[list[str]] = None,
        customer_gateway_ids: Optional[list[str]] = None,
    ) -> list[Connection]:
        """
        List connections.
        List all your connections. A number of filters are available, including Project ID, name, tags and status.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of connections to return per page.
        :param order_by: Order in which to return results.
        :param project_id: Project ID to filter for.
        :param name: Connection name to filter for.
        :param tags: Tags to filter for.
        :param statuses: Connection statuses to filter for.
        :param is_ipv6: Filter connections with IP version of IPSec tunnel.
        :param routing_policy_ids: Filter for connections using these routing policies.
        :param route_propagation_enabled: Filter for connections with route propagation enabled.
        :param vpn_gateway_ids: Filter for connections attached to these VPN gateways.
        :param customer_gateway_ids: Filter for connections attached to these customer gateways.
        :return: :class:`list[Connection] <list[Connection]>`

        Usage:
        ::

            result = await api.list_connections_all()
        """

        return await fetch_all_pages_async(
            type=ListConnectionsResponse,
            key="connections",
            fetcher=self.list_connections,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
                "name": name,
                "tags": tags,
                "statuses": statuses,
                "is_ipv6": is_ipv6,
                "routing_policy_ids": routing_policy_ids,
                "route_propagation_enabled": route_propagation_enabled,
                "vpn_gateway_ids": vpn_gateway_ids,
                "customer_gateway_ids": customer_gateway_ids,
            },
        )

    async def get_connection(
        self,
        *,
        connection_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Connection:
        """
        Get a connection.
        Get a connection for the given connection ID. The response object includes information about the connection's various configuration details.
        :param connection_id: ID of the requested connection.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Connection <Connection>`

        Usage:
        ::

            result = await api.get_connection(
                connection_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_connection_id = validate_path_param("connection_id", connection_id)

        res = self._request(
            "GET",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/connections/{param_connection_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Connection(res.json())

    async def create_connection(
        self,
        *,
        name: str,
        is_ipv6: bool,
        initiation_policy: CreateConnectionRequestInitiationPolicy,
        ikev2_ciphers: list[ConnectionCipher],
        esp_ciphers: list[ConnectionCipher],
        enable_route_propagation: bool,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        vpn_gateway_id: str,
        customer_gateway_id: str,
        bgp_config_ipv4: Optional[CreateConnectionRequestBgpConfig] = None,
        bgp_config_ipv6: Optional[CreateConnectionRequestBgpConfig] = None,
    ) -> CreateConnectionResponse:
        """
        Create a connection.
        :param name: Name of the connection.
        :param is_ipv6: Defines IP version of the IPSec Tunnel.
        :param initiation_policy: Who initiates the IPsec tunnel.
        :param ikev2_ciphers: List of IKE v2 ciphers proposed for the IPsec tunnel.
        :param esp_ciphers: List of ESP ciphers proposed for the IPsec tunnel.
        :param enable_route_propagation: Defines whether route propagation is enabled or not.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to create the connection in.
        :param tags: List of tags to apply to the connection.
        :param vpn_gateway_id: ID of the VPN gateway to attach to the connection.
        :param customer_gateway_id: ID of the customer gateway to attach to the connection.
        :param bgp_config_ipv4: BGP config of IPv4 session, including interco private IPv4 subnet (first IP assigned to the VPN Gateway, second IP to the Customer Gateway) and attached routing policy.
        :param bgp_config_ipv6: BGP config of IPv6 session, including interco private IPv6 subnet (first IP assigned to the VPN Gateway, second IP to the Customer Gateway) and attached routing policy.
        :return: :class:`CreateConnectionResponse <CreateConnectionResponse>`

        Usage:
        ::

            result = await api.create_connection(
                name="example",
                is_ipv6=False,
                initiation_policy=CreateConnectionRequestInitiationPolicy.unknown_initiation_policy,
                ikev2_ciphers=[],
                esp_ciphers=[],
                enable_route_propagation=False,
                vpn_gateway_id="example",
                customer_gateway_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/connections",
            body=marshal_CreateConnectionRequest(
                CreateConnectionRequest(
                    name=name,
                    is_ipv6=is_ipv6,
                    initiation_policy=initiation_policy,
                    ikev2_ciphers=ikev2_ciphers,
                    esp_ciphers=esp_ciphers,
                    enable_route_propagation=enable_route_propagation,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                    vpn_gateway_id=vpn_gateway_id,
                    customer_gateway_id=customer_gateway_id,
                    bgp_config_ipv4=bgp_config_ipv4,
                    bgp_config_ipv6=bgp_config_ipv6,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateConnectionResponse(res.json())

    async def update_connection(
        self,
        *,
        connection_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        initiation_policy: Optional[CreateConnectionRequestInitiationPolicy] = None,
        ikev2_ciphers: Optional[list[ConnectionCipher]] = None,
        esp_ciphers: Optional[list[ConnectionCipher]] = None,
    ) -> Connection:
        """
        Update a connection.
        Update an existing connection, specified by its connection ID.
        :param connection_id: ID of the connection to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the connection.
        :param tags: List of tags to apply to the connection.
        :param initiation_policy: Who initiates the IPsec tunnel.
        :param ikev2_ciphers: List of IKE v2 ciphers proposed for the IPsec tunnel.
        :param esp_ciphers: List of ESP ciphers proposed for the IPsec tunnel.
        :return: :class:`Connection <Connection>`

        Usage:
        ::

            result = await api.update_connection(
                connection_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_connection_id = validate_path_param("connection_id", connection_id)

        res = self._request(
            "PATCH",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/connections/{param_connection_id}",
            body=marshal_UpdateConnectionRequest(
                UpdateConnectionRequest(
                    connection_id=connection_id,
                    region=region,
                    name=name,
                    tags=tags,
                    initiation_policy=initiation_policy,
                    ikev2_ciphers=ikev2_ciphers,
                    esp_ciphers=esp_ciphers,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Connection(res.json())

    async def delete_connection(
        self,
        *,
        connection_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a connection.
        Delete an existing connection, specified by its connection ID.
        :param connection_id: ID of the connection to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_connection(
                connection_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_connection_id = validate_path_param("connection_id", connection_id)

        res = self._request(
            "DELETE",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/connections/{param_connection_id}",
        )

        self._throw_on_error(res)

    async def renew_connection_psk(
        self,
        *,
        connection_id: str,
        region: Optional[ScwRegion] = None,
    ) -> RenewConnectionPskResponse:
        """
        Renew pre-shared key.
        Renew pre-shared key for a given connection.
        :param connection_id: ID of the connection to renew the PSK.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`RenewConnectionPskResponse <RenewConnectionPskResponse>`

        Usage:
        ::

            result = await api.renew_connection_psk(
                connection_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_connection_id = validate_path_param("connection_id", connection_id)

        res = self._request(
            "POST",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/connections/{param_connection_id}/renew-psk",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_RenewConnectionPskResponse(res.json())

    async def set_routing_policy(
        self,
        *,
        connection_id: str,
        region: Optional[ScwRegion] = None,
        routing_policy_v4: Optional[str] = None,
        routing_policy_v6: Optional[str] = None,
    ) -> Connection:
        """
        Set a new routing policy.
        Set a new routing policy on a connection, overriding the existing one if present, specified by its connection ID.
        :param connection_id: ID of the connection whose routing policy is being updated.
        :param region: Region to target. If none is passed will use default region from the config.
        :param routing_policy_v4: ID of the routing policy to set for the BGP IPv4 session.
        One-Of ('routing_policy'): at most one of 'routing_policy_v4', 'routing_policy_v6' could be set.
        :param routing_policy_v6: ID of the routing policy to set for the BGP IPv6 session.
        One-Of ('routing_policy'): at most one of 'routing_policy_v4', 'routing_policy_v6' could be set.
        :return: :class:`Connection <Connection>`

        Usage:
        ::

            result = await api.set_routing_policy(
                connection_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_connection_id = validate_path_param("connection_id", connection_id)

        res = self._request(
            "POST",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/connections/{param_connection_id}/set-routing-policy",
            body=marshal_SetRoutingPolicyRequest(
                SetRoutingPolicyRequest(
                    connection_id=connection_id,
                    region=region,
                    routing_policy_v4=routing_policy_v4,
                    routing_policy_v6=routing_policy_v6,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Connection(res.json())

    async def detach_routing_policy(
        self,
        *,
        connection_id: str,
        region: Optional[ScwRegion] = None,
        routing_policy_v4: Optional[str] = None,
        routing_policy_v6: Optional[str] = None,
    ) -> Connection:
        """
        Detach a routing policy.
        Detach an existing routing policy from a connection, specified by its connection ID.
        :param connection_id: ID of the connection from which routing policy is being detached.
        :param region: Region to target. If none is passed will use default region from the config.
        :param routing_policy_v4: ID of the routing policy to detach from the BGP IPv4 session.
        One-Of ('routing_policy'): at most one of 'routing_policy_v4', 'routing_policy_v6' could be set.
        :param routing_policy_v6: ID of the routing policy to detach from the BGP IPv6 session.
        One-Of ('routing_policy'): at most one of 'routing_policy_v4', 'routing_policy_v6' could be set.
        :return: :class:`Connection <Connection>`

        Usage:
        ::

            result = await api.detach_routing_policy(
                connection_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_connection_id = validate_path_param("connection_id", connection_id)

        res = self._request(
            "POST",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/connections/{param_connection_id}/detach-routing-policy",
            body=marshal_DetachRoutingPolicyRequest(
                DetachRoutingPolicyRequest(
                    connection_id=connection_id,
                    region=region,
                    routing_policy_v4=routing_policy_v4,
                    routing_policy_v6=routing_policy_v6,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Connection(res.json())

    async def enable_route_propagation(
        self,
        *,
        connection_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Connection:
        """
        Enable route propagation.
        Enable all allowed prefixes (defined in a routing policy) to be announced in the BGP session. This allows traffic to flow between the attached VPC and the on-premises infrastructure along the announced routes. Note that by default, even when route propagation is enabled, all routes are blocked. It is essential to attach a routing policy to define the ranges of routes to announce.
        :param connection_id: ID of the connection on which to enable route propagation.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Connection <Connection>`

        Usage:
        ::

            result = await api.enable_route_propagation(
                connection_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_connection_id = validate_path_param("connection_id", connection_id)

        res = self._request(
            "POST",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/connections/{param_connection_id}/enable-route-propagation",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Connection(res.json())

    async def disable_route_propagation(
        self,
        *,
        connection_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Connection:
        """
        Disable route propagation.
        Prevent any prefixes from being announced in the BGP session. Traffic will not be able to flow over the VPN Gateway until route propagation is re-enabled.
        :param connection_id: ID of the connection on which to disable route propagation.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Connection <Connection>`

        Usage:
        ::

            result = await api.disable_route_propagation(
                connection_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_connection_id = validate_path_param("connection_id", connection_id)

        res = self._request(
            "POST",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/connections/{param_connection_id}/disable-route-propagation",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Connection(res.json())

    async def list_customer_gateways(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListCustomerGatewaysRequestOrderBy] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> ListCustomerGatewaysResponse:
        """
        List customer gateways.
        List all your customer gateways. A number of filters are available, including Project ID, name, and tags.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of customer gateways to return per page.
        :param order_by: Order in which to return results.
        :param project_id: Project ID to filter for.
        :param name: Customer gateway name to filter for.
        :param tags: Tags to filter for.
        :return: :class:`ListCustomerGatewaysResponse <ListCustomerGatewaysResponse>`

        Usage:
        ::

            result = await api.list_customer_gateways()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/customer-gateways",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListCustomerGatewaysResponse(res.json())

    async def list_customer_gateways_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListCustomerGatewaysRequestOrderBy] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> list[CustomerGateway]:
        """
        List customer gateways.
        List all your customer gateways. A number of filters are available, including Project ID, name, and tags.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of customer gateways to return per page.
        :param order_by: Order in which to return results.
        :param project_id: Project ID to filter for.
        :param name: Customer gateway name to filter for.
        :param tags: Tags to filter for.
        :return: :class:`list[CustomerGateway] <list[CustomerGateway]>`

        Usage:
        ::

            result = await api.list_customer_gateways_all()
        """

        return await fetch_all_pages_async(
            type=ListCustomerGatewaysResponse,
            key="gateways",
            fetcher=self.list_customer_gateways,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
                "name": name,
                "tags": tags,
            },
        )

    async def get_customer_gateway(
        self,
        *,
        gateway_id: str,
        region: Optional[ScwRegion] = None,
    ) -> CustomerGateway:
        """
        Get a customer gateway.
        Get a customer gateway for the given customer gateway ID.
        :param gateway_id: ID of the requested customer gateway.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`CustomerGateway <CustomerGateway>`

        Usage:
        ::

            result = await api.get_customer_gateway(
                gateway_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "GET",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/customer-gateways/{param_gateway_id}",
        )

        self._throw_on_error(res)
        return unmarshal_CustomerGateway(res.json())

    async def create_customer_gateway(
        self,
        *,
        name: str,
        asn: int,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        ipv4_public: Optional[str] = None,
        ipv6_public: Optional[str] = None,
    ) -> CustomerGateway:
        """
        Create a customer gateway.
        :param name: Name of the customer gateway.
        :param asn: AS Number of the customer gateway.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to create the customer gateway in.
        :param tags: List of tags to apply to the customer gateway.
        :param ipv4_public: Public IPv4 address of the customer gateway.
        :param ipv6_public: Public IPv6 address of the customer gateway.
        :return: :class:`CustomerGateway <CustomerGateway>`

        Usage:
        ::

            result = await api.create_customer_gateway(
                name="example",
                asn=1,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/customer-gateways",
            body=marshal_CreateCustomerGatewayRequest(
                CreateCustomerGatewayRequest(
                    name=name,
                    asn=asn,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                    ipv4_public=ipv4_public,
                    ipv6_public=ipv6_public,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CustomerGateway(res.json())

    async def update_customer_gateway(
        self,
        *,
        gateway_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        ipv4_public: Optional[str] = None,
        ipv6_public: Optional[str] = None,
        asn: Optional[int] = None,
    ) -> CustomerGateway:
        """
        Update a customer gateway.
        Update an existing customer gateway, specified by its customer gateway ID. You can update its name, tags, public IPv4 & IPv6 address and AS Number.
        :param gateway_id: ID of the customer gateway to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the customer gateway.
        :param tags: List of tags to apply to the customer gateway.
        :param ipv4_public: Public IPv4 address of the customer gateway.
        :param ipv6_public: Public IPv6 address of the customer gateway.
        :param asn: AS Number of the customer gateway.
        :return: :class:`CustomerGateway <CustomerGateway>`

        Usage:
        ::

            result = await api.update_customer_gateway(
                gateway_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "PATCH",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/customer-gateways/{param_gateway_id}",
            body=marshal_UpdateCustomerGatewayRequest(
                UpdateCustomerGatewayRequest(
                    gateway_id=gateway_id,
                    region=region,
                    name=name,
                    tags=tags,
                    ipv4_public=ipv4_public,
                    ipv6_public=ipv6_public,
                    asn=asn,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CustomerGateway(res.json())

    async def delete_customer_gateway(
        self,
        *,
        gateway_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a customer gateway.
        Delete an existing customer gateway, specified by its customer gateway ID.
        :param gateway_id: ID of the customer gateway to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_customer_gateway(
                gateway_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "DELETE",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/customer-gateways/{param_gateway_id}",
        )

        self._throw_on_error(res)

    async def list_routing_policies(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRoutingPoliciesRequestOrderBy] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        ipv6: Optional[bool] = None,
    ) -> ListRoutingPoliciesResponse:
        """
        List routing policies.
        List all routing policies in a given region. A routing policy can be attached to one or multiple connections (S2S VPN connections).
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of routing policies to return per page.
        :param order_by: Order in which to return results.
        :param project_id: Project ID to filter for.
        :param name: Routing policy name to filter for.
        :param tags: Tags to filter for.
        :param ipv6: Filter for the routing policies based on IP prefixes version.
        :return: :class:`ListRoutingPoliciesResponse <ListRoutingPoliciesResponse>`

        Usage:
        ::

            result = await api.list_routing_policies()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/routing-policies",
            params={
                "ipv6": ipv6,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRoutingPoliciesResponse(res.json())

    async def list_routing_policies_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRoutingPoliciesRequestOrderBy] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        ipv6: Optional[bool] = None,
    ) -> list[RoutingPolicy]:
        """
        List routing policies.
        List all routing policies in a given region. A routing policy can be attached to one or multiple connections (S2S VPN connections).
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of routing policies to return per page.
        :param order_by: Order in which to return results.
        :param project_id: Project ID to filter for.
        :param name: Routing policy name to filter for.
        :param tags: Tags to filter for.
        :param ipv6: Filter for the routing policies based on IP prefixes version.
        :return: :class:`list[RoutingPolicy] <list[RoutingPolicy]>`

        Usage:
        ::

            result = await api.list_routing_policies_all()
        """

        return await fetch_all_pages_async(
            type=ListRoutingPoliciesResponse,
            key="routing_policies",
            fetcher=self.list_routing_policies,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
                "name": name,
                "tags": tags,
                "ipv6": ipv6,
            },
        )

    async def get_routing_policy(
        self,
        *,
        routing_policy_id: str,
        region: Optional[ScwRegion] = None,
    ) -> RoutingPolicy:
        """
        Get routing policy.
        Get a routing policy for the given routing policy ID. The response object gives information including the policy's name, tags and prefix filters.
        :param routing_policy_id: ID of the routing policy to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`RoutingPolicy <RoutingPolicy>`

        Usage:
        ::

            result = await api.get_routing_policy(
                routing_policy_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_routing_policy_id = validate_path_param(
            "routing_policy_id", routing_policy_id
        )

        res = self._request(
            "GET",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/routing-policies/{param_routing_policy_id}",
        )

        self._throw_on_error(res)
        return unmarshal_RoutingPolicy(res.json())

    async def create_routing_policy(
        self,
        *,
        name: str,
        is_ipv6: bool,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        prefix_filter_in: Optional[list[str]] = None,
        prefix_filter_out: Optional[list[str]] = None,
    ) -> RoutingPolicy:
        """
        Create a routing policy.
        Create a routing policy. Routing policies allow you to set IP prefix filters to define the incoming route announcements to accept from the customer gateway, and the outgoing routes to announce to the customer gateway.
        :param name: Name of the routing policy.
        :param is_ipv6: IP prefixes version of the routing policy.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to create the routing policy in.
        :param tags: List of tags to apply to the routing policy.
        :param prefix_filter_in: IP prefixes to accept from the peer (ranges of route announcements to accept).
        :param prefix_filter_out: IP prefix filters to advertise to the peer (ranges of routes to advertise).
        :return: :class:`RoutingPolicy <RoutingPolicy>`

        Usage:
        ::

            result = await api.create_routing_policy(
                name="example",
                is_ipv6=False,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/routing-policies",
            body=marshal_CreateRoutingPolicyRequest(
                CreateRoutingPolicyRequest(
                    name=name,
                    is_ipv6=is_ipv6,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                    prefix_filter_in=prefix_filter_in,
                    prefix_filter_out=prefix_filter_out,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RoutingPolicy(res.json())

    async def update_routing_policy(
        self,
        *,
        routing_policy_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        prefix_filter_in: Optional[list[str]] = None,
        prefix_filter_out: Optional[list[str]] = None,
    ) -> RoutingPolicy:
        """
        Update a routing policy.
        Update an existing routing policy, specified by its routing policy ID. Its name, tags and incoming/outgoing prefix filters can be updated.
        :param routing_policy_id: ID of the routing policy to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the routing policy.
        :param tags: List of tags to apply to the routing policy.
        :param prefix_filter_in: IP prefixes to accept from the peer (ranges of route announcements to accept).
        :param prefix_filter_out: IP prefix filters for routes to advertise to the peer (ranges of routes to advertise).
        :return: :class:`RoutingPolicy <RoutingPolicy>`

        Usage:
        ::

            result = await api.update_routing_policy(
                routing_policy_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_routing_policy_id = validate_path_param(
            "routing_policy_id", routing_policy_id
        )

        res = self._request(
            "PATCH",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/routing-policies/{param_routing_policy_id}",
            body=marshal_UpdateRoutingPolicyRequest(
                UpdateRoutingPolicyRequest(
                    routing_policy_id=routing_policy_id,
                    region=region,
                    name=name,
                    tags=tags,
                    prefix_filter_in=prefix_filter_in,
                    prefix_filter_out=prefix_filter_out,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RoutingPolicy(res.json())

    async def delete_routing_policy(
        self,
        *,
        routing_policy_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a routing policy.
        Delete an existing routing policy, specified by its routing policy ID.
        :param routing_policy_id: ID of the routing policy to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_routing_policy(
                routing_policy_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_routing_policy_id = validate_path_param(
            "routing_policy_id", routing_policy_id
        )

        res = self._request(
            "DELETE",
            f"/s2s-vpn/v1alpha1/regions/{param_region}/routing-policies/{param_routing_policy_id}",
        )

        self._throw_on_error(res)
