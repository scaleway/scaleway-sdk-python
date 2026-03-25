# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone as ScwZone,
)
from scaleway_core.utils import (
    WaitForOptions,
    random_name,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    GatewayNetworkStatus,
    GatewayStatus,
    ListGatewayNetworksRequestOrderBy,
    ListGatewaysRequestOrderBy,
    ListIPsRequestOrderBy,
    ListPatRulesRequestOrderBy,
    PatRuleProtocol,
    AddBastionAllowedIPsRequest,
    AddBastionAllowedIPsResponse,
    CreateGatewayNetworkRequest,
    CreateGatewayRequest,
    CreateIPRequest,
    CreatePatRuleRequest,
    Gateway,
    GatewayNetwork,
    IP,
    ListGatewayNetworksResponse,
    ListGatewayTypesResponse,
    ListGatewaysResponse,
    ListIPsResponse,
    ListPatRulesResponse,
    PatRule,
    SetBastionAllowedIPsRequest,
    SetBastionAllowedIPsResponse,
    SetPatRulesRequest,
    SetPatRulesRequestRule,
    SetPatRulesResponse,
    UpdateGatewayNetworkRequest,
    UpdateGatewayRequest,
    UpdateIPRequest,
    UpdatePatRuleRequest,
    UpgradeGatewayRequest,
)
from .content import (
    GATEWAY_NETWORK_TRANSIENT_STATUSES,
    GATEWAY_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_GatewayNetwork,
    unmarshal_IP,
    unmarshal_Gateway,
    unmarshal_PatRule,
    unmarshal_AddBastionAllowedIPsResponse,
    unmarshal_ListGatewayNetworksResponse,
    unmarshal_ListGatewayTypesResponse,
    unmarshal_ListGatewaysResponse,
    unmarshal_ListIPsResponse,
    unmarshal_ListPatRulesResponse,
    unmarshal_SetBastionAllowedIPsResponse,
    unmarshal_SetPatRulesResponse,
    marshal_AddBastionAllowedIPsRequest,
    marshal_CreateGatewayNetworkRequest,
    marshal_CreateGatewayRequest,
    marshal_CreateIPRequest,
    marshal_CreatePatRuleRequest,
    marshal_SetBastionAllowedIPsRequest,
    marshal_SetPatRulesRequest,
    marshal_UpdateGatewayNetworkRequest,
    marshal_UpdateGatewayRequest,
    marshal_UpdateIPRequest,
    marshal_UpdatePatRuleRequest,
    marshal_UpgradeGatewayRequest,
)


class VpcgwV2API(API):
    """
    This API allows you to manage your Public Gateways.
    """

    def list_gateways(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListGatewaysRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        types: Optional[list[str]] = None,
        status: Optional[list[GatewayStatus]] = None,
        private_network_ids: Optional[list[str]] = None,
        include_legacy: Optional[bool] = None,
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
        :param types: Filter for gateways of these types.
        :param status: Filter for gateways with these status. Use `unknown` to include all statuses.
        :param private_network_ids: Filter for gateways attached to these Private Networks.
        :param include_legacy: Include also legacy gateways.
        :return: :class:`ListGatewaysResponse <ListGatewaysResponse>`

        Usage:
        ::

            result = api.list_gateways()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/vpc-gw/v2/zones/{param_zone}/gateways",
            params={
                "include_legacy": include_legacy,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "private_network_ids": private_network_ids,
                "project_id": project_id or self.client.default_project_id,
                "status": status,
                "tags": tags,
                "types": types,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListGatewaysResponse(res.json())

    def list_gateways_all(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListGatewaysRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        types: Optional[list[str]] = None,
        status: Optional[list[GatewayStatus]] = None,
        private_network_ids: Optional[list[str]] = None,
        include_legacy: Optional[bool] = None,
    ) -> list[Gateway]:
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
        :param types: Filter for gateways of these types.
        :param status: Filter for gateways with these status. Use `unknown` to include all statuses.
        :param private_network_ids: Filter for gateways attached to these Private Networks.
        :param include_legacy: Include also legacy gateways.
        :return: :class:`list[Gateway] <list[Gateway]>`

        Usage:
        ::

            result = api.list_gateways_all()
        """

        return fetch_all_pages(
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
                "types": types,
                "status": status,
                "private_network_ids": private_network_ids,
                "include_legacy": include_legacy,
            },
        )

    def get_gateway(
        self,
        *,
        gateway_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Gateway:
        """
        Get a Public Gateway.
        Get details of a Public Gateway, specified by its gateway ID. The response object contains full details of the gateway, including its **name**, **type**, **status** and more.
        :param gateway_id: ID of the gateway to fetch.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = api.get_gateway(
                gateway_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "GET",
            f"/vpc-gw/v2/zones/{param_zone}/gateways/{param_gateway_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Gateway(res.json())

    def wait_for_gateway(
        self,
        *,
        gateway_id: str,
        zone: Optional[ScwZone] = None,
        options: Optional[WaitForOptions[Gateway, bool]] = None,
    ) -> Gateway:
        """
        Get a Public Gateway.
        Get details of a Public Gateway, specified by its gateway ID. The response object contains full details of the gateway, including its **name**, **type**, **status** and more.
        :param gateway_id: ID of the gateway to fetch.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = api.get_gateway(
                gateway_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in GATEWAY_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_gateway,
            options=options,
            args={
                "gateway_id": gateway_id,
                "zone": zone,
            },
        )

    def create_gateway(
        self,
        *,
        type_: str,
        enable_smtp: bool,
        enable_bastion: bool,
        zone: Optional[ScwZone] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
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
        :param ip_id: Existing IP address to attach to the gateway.
        :param bastion_port: Port of the SSH bastion.
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = api.create_gateway(
                type="example",
                enable_smtp=False,
                enable_bastion=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/vpc-gw/v2/zones/{param_zone}/gateways",
            body=marshal_CreateGatewayRequest(
                CreateGatewayRequest(
                    type_=type_,
                    enable_smtp=enable_smtp,
                    enable_bastion=enable_bastion,
                    zone=zone,
                    project_id=project_id,
                    name=name or random_name(prefix="gw"),
                    tags=tags,
                    ip_id=ip_id,
                    bastion_port=bastion_port,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Gateway(res.json())

    def update_gateway(
        self,
        *,
        gateway_id: str,
        zone: Optional[ScwZone] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
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
        :param enable_bastion: Defines whether SSH bastion should be enabled the gateway.
        :param bastion_port: Port of the SSH bastion.
        :param enable_smtp: Defines whether SMTP traffic should be allowed to pass through the gateway.
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = api.update_gateway(
                gateway_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "PATCH",
            f"/vpc-gw/v2/zones/{param_zone}/gateways/{param_gateway_id}",
            body=marshal_UpdateGatewayRequest(
                UpdateGatewayRequest(
                    gateway_id=gateway_id,
                    zone=zone,
                    name=name,
                    tags=tags,
                    enable_bastion=enable_bastion,
                    bastion_port=bastion_port,
                    enable_smtp=enable_smtp,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Gateway(res.json())

    def delete_gateway(
        self,
        *,
        gateway_id: str,
        delete_ip: bool,
        zone: Optional[ScwZone] = None,
    ) -> Gateway:
        """
        Delete a Public Gateway.
        Delete an existing Public Gateway, specified by its gateway ID. This action is irreversible.
        :param gateway_id: ID of the gateway to delete.
        :param delete_ip: Defines whether the PGW's IP should be deleted.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = api.delete_gateway(
                gateway_id="example",
                delete_ip=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "DELETE",
            f"/vpc-gw/v2/zones/{param_zone}/gateways/{param_gateway_id}",
            params={
                "delete_ip": delete_ip,
            },
        )

        self._throw_on_error(res)
        return unmarshal_Gateway(res.json())

    def upgrade_gateway(
        self,
        *,
        gateway_id: str,
        zone: Optional[ScwZone] = None,
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

            result = api.upgrade_gateway(
                gateway_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "POST",
            f"/vpc-gw/v2/zones/{param_zone}/gateways/{param_gateway_id}/upgrade",
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

    def list_gateway_networks(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListGatewayNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        status: Optional[list[GatewayNetworkStatus]] = None,
        gateway_ids: Optional[list[str]] = None,
        private_network_ids: Optional[list[str]] = None,
        masquerade_enabled: Optional[bool] = None,
    ) -> ListGatewayNetworksResponse:
        """
        List Public Gateway connections to Private Networks.
        List the connections between Public Gateways and Private Networks (a connection = a GatewayNetwork). You can choose to filter by `gateway-id` to list all Private Networks attached to the specified Public Gateway, or by `private_network_id` to list all Public Gateways attached to the specified Private Network. Other query parameters are also available. The result is an array of GatewayNetwork objects, each giving details of the connection between a given Public Gateway and a given Private Network.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: GatewayNetworks per page.
        :param status: Filter for GatewayNetworks with these status. Use `unknown` to include all statuses.
        :param gateway_ids: Filter for GatewayNetworks connected to these gateways.
        :param private_network_ids: Filter for GatewayNetworks connected to these Private Networks.
        :param masquerade_enabled: Filter for GatewayNetworks with this `enable_masquerade` setting.
        :return: :class:`ListGatewayNetworksResponse <ListGatewayNetworksResponse>`

        Usage:
        ::

            result = api.list_gateway_networks()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/vpc-gw/v2/zones/{param_zone}/gateway-networks",
            params={
                "gateway_ids": gateway_ids,
                "masquerade_enabled": masquerade_enabled,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "private_network_ids": private_network_ids,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListGatewayNetworksResponse(res.json())

    def list_gateway_networks_all(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListGatewayNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        status: Optional[list[GatewayNetworkStatus]] = None,
        gateway_ids: Optional[list[str]] = None,
        private_network_ids: Optional[list[str]] = None,
        masquerade_enabled: Optional[bool] = None,
    ) -> list[GatewayNetwork]:
        """
        List Public Gateway connections to Private Networks.
        List the connections between Public Gateways and Private Networks (a connection = a GatewayNetwork). You can choose to filter by `gateway-id` to list all Private Networks attached to the specified Public Gateway, or by `private_network_id` to list all Public Gateways attached to the specified Private Network. Other query parameters are also available. The result is an array of GatewayNetwork objects, each giving details of the connection between a given Public Gateway and a given Private Network.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: GatewayNetworks per page.
        :param status: Filter for GatewayNetworks with these status. Use `unknown` to include all statuses.
        :param gateway_ids: Filter for GatewayNetworks connected to these gateways.
        :param private_network_ids: Filter for GatewayNetworks connected to these Private Networks.
        :param masquerade_enabled: Filter for GatewayNetworks with this `enable_masquerade` setting.
        :return: :class:`list[GatewayNetwork] <list[GatewayNetwork]>`

        Usage:
        ::

            result = api.list_gateway_networks_all()
        """

        return fetch_all_pages(
            type=ListGatewayNetworksResponse,
            key="gateway_networks",
            fetcher=self.list_gateway_networks,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "status": status,
                "gateway_ids": gateway_ids,
                "private_network_ids": private_network_ids,
                "masquerade_enabled": masquerade_enabled,
            },
        )

    def get_gateway_network(
        self,
        *,
        gateway_network_id: str,
        zone: Optional[ScwZone] = None,
    ) -> GatewayNetwork:
        """
        Get a Public Gateway connection to a Private Network.
        Get details of a given connection between a Public Gateway and a Private Network (this connection = a GatewayNetwork), specified by its `gateway_network_id`. The response object contains details of the connection including the IDs of the Public Gateway and Private Network, the dates the connection was created/updated and its configuration settings.
        :param gateway_network_id: ID of the GatewayNetwork to fetch.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GatewayNetwork <GatewayNetwork>`

        Usage:
        ::

            result = api.get_gateway_network(
                gateway_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_network_id = validate_path_param(
            "gateway_network_id", gateway_network_id
        )

        res = self._request(
            "GET",
            f"/vpc-gw/v2/zones/{param_zone}/gateway-networks/{param_gateway_network_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GatewayNetwork(res.json())

    def wait_for_gateway_network(
        self,
        *,
        gateway_network_id: str,
        zone: Optional[ScwZone] = None,
        options: Optional[WaitForOptions[GatewayNetwork, bool]] = None,
    ) -> GatewayNetwork:
        """
        Get a Public Gateway connection to a Private Network.
        Get details of a given connection between a Public Gateway and a Private Network (this connection = a GatewayNetwork), specified by its `gateway_network_id`. The response object contains details of the connection including the IDs of the Public Gateway and Private Network, the dates the connection was created/updated and its configuration settings.
        :param gateway_network_id: ID of the GatewayNetwork to fetch.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GatewayNetwork <GatewayNetwork>`

        Usage:
        ::

            result = api.get_gateway_network(
                gateway_network_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: (
                res.status not in GATEWAY_NETWORK_TRANSIENT_STATUSES
            )

        return wait_for_resource(
            fetcher=self.get_gateway_network,
            options=options,
            args={
                "gateway_network_id": gateway_network_id,
                "zone": zone,
            },
        )

    def create_gateway_network(
        self,
        *,
        gateway_id: str,
        private_network_id: str,
        enable_masquerade: bool,
        push_default_route: bool,
        zone: Optional[ScwZone] = None,
        ipam_ip_id: Optional[str] = None,
    ) -> GatewayNetwork:
        """
        Attach a Public Gateway to a Private Network.
        Attach a specific Public Gateway to a specific Private Network (create a GatewayNetwork). You can configure parameters for the connection including whether to enable masquerade (dynamic NAT), and more.
        :param gateway_id: Public Gateway to connect.
        :param private_network_id: Private Network to connect.
        :param enable_masquerade: Defines whether to enable masquerade (dynamic NAT) on the GatewayNetwork.
        :param push_default_route: Enabling the default route also enables masquerading.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param ipam_ip_id: Use this IPAM-booked IP ID as the Gateway's IP in this Private Network.
        :return: :class:`GatewayNetwork <GatewayNetwork>`

        Usage:
        ::

            result = api.create_gateway_network(
                gateway_id="example",
                private_network_id="example",
                enable_masquerade=False,
                push_default_route=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/vpc-gw/v2/zones/{param_zone}/gateway-networks",
            body=marshal_CreateGatewayNetworkRequest(
                CreateGatewayNetworkRequest(
                    gateway_id=gateway_id,
                    private_network_id=private_network_id,
                    enable_masquerade=enable_masquerade,
                    push_default_route=push_default_route,
                    zone=zone,
                    ipam_ip_id=ipam_ip_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_GatewayNetwork(res.json())

    def update_gateway_network(
        self,
        *,
        gateway_network_id: str,
        zone: Optional[ScwZone] = None,
        enable_masquerade: Optional[bool] = None,
        push_default_route: Optional[bool] = None,
        ipam_ip_id: Optional[str] = None,
    ) -> GatewayNetwork:
        """
        Update a Public Gateway's connection to a Private Network.
        Update the configuration parameters of a connection between a given Public Gateway and Private Network (the connection = a GatewayNetwork). Updatable parameters include whether to enable traffic masquerade (dynamic NAT).
        :param gateway_network_id: ID of the GatewayNetwork to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param enable_masquerade: Defines whether to enable masquerade (dynamic NAT) on the GatewayNetwork.
        :param push_default_route: Enabling the default route also enables masquerading.
        :param ipam_ip_id: Use this IPAM-booked IP ID as the Gateway's IP in this Private Network.
        :return: :class:`GatewayNetwork <GatewayNetwork>`

        Usage:
        ::

            result = api.update_gateway_network(
                gateway_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_network_id = validate_path_param(
            "gateway_network_id", gateway_network_id
        )

        res = self._request(
            "PATCH",
            f"/vpc-gw/v2/zones/{param_zone}/gateway-networks/{param_gateway_network_id}",
            body=marshal_UpdateGatewayNetworkRequest(
                UpdateGatewayNetworkRequest(
                    gateway_network_id=gateway_network_id,
                    zone=zone,
                    enable_masquerade=enable_masquerade,
                    push_default_route=push_default_route,
                    ipam_ip_id=ipam_ip_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_GatewayNetwork(res.json())

    def delete_gateway_network(
        self,
        *,
        gateway_network_id: str,
        zone: Optional[ScwZone] = None,
    ) -> GatewayNetwork:
        """
        Detach a Public Gateway from a Private Network.
        Detach a given Public Gateway from a given Private Network, i.e. delete a GatewayNetwork specified by a gateway_network_id.
        :param gateway_network_id: ID of the GatewayNetwork to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GatewayNetwork <GatewayNetwork>`

        Usage:
        ::

            result = api.delete_gateway_network(
                gateway_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_network_id = validate_path_param(
            "gateway_network_id", gateway_network_id
        )

        res = self._request(
            "DELETE",
            f"/vpc-gw/v2/zones/{param_zone}/gateway-networks/{param_gateway_network_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GatewayNetwork(res.json())

    def list_pat_rules(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListPatRulesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        gateway_ids: Optional[list[str]] = None,
        private_ips: Optional[list[str]] = None,
        protocol: Optional[PatRuleProtocol] = None,
    ) -> ListPatRulesResponse:
        """
        List PAT rules.
        List PAT rules. You can filter by gateway ID to list all PAT rules for a particular gateway, or filter for PAT rules targeting a specific IP address or using a specific protocol.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: PAT rules per page.
        :param gateway_ids: Filter for PAT rules on these gateways.
        :param private_ips: Filter for PAT rules targeting these private ips.
        :param protocol: Filter for PAT rules with this protocol.
        :return: :class:`ListPatRulesResponse <ListPatRulesResponse>`

        Usage:
        ::

            result = api.list_pat_rules()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/vpc-gw/v2/zones/{param_zone}/pat-rules",
            params={
                "gateway_ids": gateway_ids,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "private_ips": private_ips,
                "protocol": protocol,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPatRulesResponse(res.json())

    def list_pat_rules_all(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListPatRulesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        gateway_ids: Optional[list[str]] = None,
        private_ips: Optional[list[str]] = None,
        protocol: Optional[PatRuleProtocol] = None,
    ) -> list[PatRule]:
        """
        List PAT rules.
        List PAT rules. You can filter by gateway ID to list all PAT rules for a particular gateway, or filter for PAT rules targeting a specific IP address or using a specific protocol.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: PAT rules per page.
        :param gateway_ids: Filter for PAT rules on these gateways.
        :param private_ips: Filter for PAT rules targeting these private ips.
        :param protocol: Filter for PAT rules with this protocol.
        :return: :class:`list[PatRule] <list[PatRule]>`

        Usage:
        ::

            result = api.list_pat_rules_all()
        """

        return fetch_all_pages(
            type=ListPatRulesResponse,
            key="pat_rules",
            fetcher=self.list_pat_rules,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "gateway_ids": gateway_ids,
                "private_ips": private_ips,
                "protocol": protocol,
            },
        )

    def get_pat_rule(
        self,
        *,
        pat_rule_id: str,
        zone: Optional[ScwZone] = None,
    ) -> PatRule:
        """
        Get a PAT rule.
        Get a PAT rule, specified by its PAT rule ID. The response object gives full details of the PAT rule, including the Public Gateway it belongs to and the configuration settings in terms of public / private ports, private IP and protocol.
        :param pat_rule_id: ID of the PAT rule to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`PatRule <PatRule>`

        Usage:
        ::

            result = api.get_pat_rule(
                pat_rule_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_pat_rule_id = validate_path_param("pat_rule_id", pat_rule_id)

        res = self._request(
            "GET",
            f"/vpc-gw/v2/zones/{param_zone}/pat-rules/{param_pat_rule_id}",
        )

        self._throw_on_error(res)
        return unmarshal_PatRule(res.json())

    def create_pat_rule(
        self,
        *,
        gateway_id: str,
        public_port: int,
        private_ip: str,
        private_port: int,
        zone: Optional[ScwZone] = None,
        protocol: Optional[PatRuleProtocol] = None,
    ) -> PatRule:
        """
        Create a PAT rule.
        Create a new PAT rule on a specified Public Gateway, defining the protocol to use, public port to listen on, and private port / IP address to map to.
        :param gateway_id: ID of the Gateway on which to create the rule.
        :param public_port: Public port to listen on.
        :param private_ip: Private IP to forward data to.
        :param private_port: Private port to translate to.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param protocol: Protocol the rule should apply to.
        :return: :class:`PatRule <PatRule>`

        Usage:
        ::

            result = api.create_pat_rule(
                gateway_id="example",
                public_port=1,
                private_ip="example",
                private_port=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/vpc-gw/v2/zones/{param_zone}/pat-rules",
            body=marshal_CreatePatRuleRequest(
                CreatePatRuleRequest(
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
        return unmarshal_PatRule(res.json())

    def update_pat_rule(
        self,
        *,
        pat_rule_id: str,
        zone: Optional[ScwZone] = None,
        public_port: Optional[int] = None,
        private_ip: Optional[str] = None,
        private_port: Optional[int] = None,
        protocol: Optional[PatRuleProtocol] = None,
    ) -> PatRule:
        """
        Update a PAT rule.
        Update a PAT rule, specified by its PAT rule ID. Configuration settings including private/public port, private IP address and protocol can all be updated.
        :param pat_rule_id: ID of the PAT rule to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param public_port: Public port to listen on.
        :param private_ip: Private IP to forward data to.
        :param private_port: Private port to translate to.
        :param protocol: Protocol the rule should apply to.
        :return: :class:`PatRule <PatRule>`

        Usage:
        ::

            result = api.update_pat_rule(
                pat_rule_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_pat_rule_id = validate_path_param("pat_rule_id", pat_rule_id)

        res = self._request(
            "PATCH",
            f"/vpc-gw/v2/zones/{param_zone}/pat-rules/{param_pat_rule_id}",
            body=marshal_UpdatePatRuleRequest(
                UpdatePatRuleRequest(
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
        return unmarshal_PatRule(res.json())

    def set_pat_rules(
        self,
        *,
        gateway_id: str,
        pat_rules: list[SetPatRulesRequestRule],
        zone: Optional[ScwZone] = None,
    ) -> SetPatRulesResponse:
        """
        Set all PAT rules.
        Set a definitive list of PAT rules attached to a Public Gateway. Each rule is identified by its public port and protocol. This will sync the current PAT rule list on the gateway with the new list, creating, updating or deleting PAT rules accordingly.
        :param gateway_id: ID of the gateway on which to set the PAT rules.
        :param pat_rules: New list of PAT rules.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`SetPatRulesResponse <SetPatRulesResponse>`

        Usage:
        ::

            result = api.set_pat_rules(
                gateway_id="example",
                pat_rules=[],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "PUT",
            f"/vpc-gw/v2/zones/{param_zone}/pat-rules",
            body=marshal_SetPatRulesRequest(
                SetPatRulesRequest(
                    gateway_id=gateway_id,
                    pat_rules=pat_rules,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetPatRulesResponse(res.json())

    def delete_pat_rule(
        self,
        *,
        pat_rule_id: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete a PAT rule.
        Delete a PAT rule, identified by its PAT rule ID. This action is irreversible.
        :param pat_rule_id: ID of the PAT rule to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_pat_rule(
                pat_rule_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_pat_rule_id = validate_path_param("pat_rule_id", pat_rule_id)

        res = self._request(
            "DELETE",
            f"/vpc-gw/v2/zones/{param_zone}/pat-rules/{param_pat_rule_id}",
        )

        self._throw_on_error(res)

    def list_gateway_types(
        self,
        *,
        zone: Optional[ScwZone] = None,
    ) -> ListGatewayTypesResponse:
        """
        List Public Gateway types.
        List the different Public Gateway commercial offer types available at Scaleway. The response is an array of objects describing the name and technical details of each available gateway type.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ListGatewayTypesResponse <ListGatewayTypesResponse>`

        Usage:
        ::

            result = api.list_gateway_types()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/vpc-gw/v2/zones/{param_zone}/gateway-types",
        )

        self._throw_on_error(res)
        return unmarshal_ListGatewayTypesResponse(res.json())

    def list_i_ps(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListIPsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
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
        :param organization_id: Include only gateways in this Organization.
        :param project_id: Filter for IP addresses in this Project.
        :param tags: Filter for IP addresses with these tags.
        :param reverse: Filter for IP addresses that have a reverse containing this string.
        :param is_free: Filter based on whether the IP is attached to a gateway or not.
        :return: :class:`ListIPsResponse <ListIPsResponse>`

        Usage:
        ::

            result = api.list_i_ps()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/vpc-gw/v2/zones/{param_zone}/ips",
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

    def list_i_ps_all(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListIPsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        reverse: Optional[str] = None,
        is_free: Optional[bool] = None,
    ) -> list[IP]:
        """
        List IPs.
        List Public Gateway flexible IP addresses. A number of filter options are available for limiting results in the response.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order in which to return results.
        :param page: Page number.
        :param page_size: IP addresses per page.
        :param organization_id: Include only gateways in this Organization.
        :param project_id: Filter for IP addresses in this Project.
        :param tags: Filter for IP addresses with these tags.
        :param reverse: Filter for IP addresses that have a reverse containing this string.
        :param is_free: Filter based on whether the IP is attached to a gateway or not.
        :return: :class:`list[IP] <list[IP]>`

        Usage:
        ::

            result = api.list_i_ps_all()
        """

        return fetch_all_pages(
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

    def get_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[ScwZone] = None,
    ) -> IP:
        """
        Get an IP.
        Get details of a Public Gateway flexible IP address, identified by its IP ID. The response object contains information including which (if any) Public Gateway using this IP address, the reverse and various other metadata.
        :param ip_id: ID of the IP address to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = api.get_ip(
                ip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "GET",
            f"/vpc-gw/v2/zones/{param_zone}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    def create_ip(
        self,
        *,
        zone: Optional[ScwZone] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
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

            result = api.create_ip()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/vpc-gw/v2/zones/{param_zone}/ips",
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

    def update_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[ScwZone] = None,
        tags: Optional[list[str]] = None,
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

            result = api.update_ip(
                ip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "PATCH",
            f"/vpc-gw/v2/zones/{param_zone}/ips/{param_ip_id}",
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

    def delete_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete an IP.
        Delete a flexible IP address from your account. This action is irreversible.
        :param ip_id: ID of the IP address to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_ip(
                ip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "DELETE",
            f"/vpc-gw/v2/zones/{param_zone}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)

    def refresh_ssh_keys(
        self,
        *,
        gateway_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Gateway:
        """
        Refresh a Public Gateway's SSH keys.
        Refresh the SSH keys of a given Public Gateway, specified by its gateway ID. This adds any new SSH keys in the gateway's Scaleway Project to the gateway itself.
        :param gateway_id: ID of the gateway to refresh SSH keys on.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Gateway <Gateway>`

        Usage:
        ::

            result = api.refresh_ssh_keys(
                gateway_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "POST",
            f"/vpc-gw/v2/zones/{param_zone}/gateways/{param_gateway_id}/refresh-ssh-keys",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Gateway(res.json())

    def add_bastion_allowed_i_ps(
        self,
        *,
        gateway_id: str,
        ip_range: str,
        zone: Optional[ScwZone] = None,
    ) -> AddBastionAllowedIPsResponse:
        """
        Add allowed IP range to SSH bastion.
        Add an IP range (in CIDR notation) to be allowed to connect to the SSH bastion.
        :param gateway_id: ID of the gateway to add the allowed IP range to.
        :param ip_range: IP range allowed to connect to the SSH bastion.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`AddBastionAllowedIPsResponse <AddBastionAllowedIPsResponse>`

        Usage:
        ::

            result = api.add_bastion_allowed_i_ps(
                gateway_id="example",
                ip_range="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "POST",
            f"/vpc-gw/v2/zones/{param_zone}/gateways/{param_gateway_id}/bastion-allowed-ips",
            body=marshal_AddBastionAllowedIPsRequest(
                AddBastionAllowedIPsRequest(
                    gateway_id=gateway_id,
                    ip_range=ip_range,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AddBastionAllowedIPsResponse(res.json())

    def set_bastion_allowed_i_ps(
        self,
        *,
        gateway_id: str,
        zone: Optional[ScwZone] = None,
        ip_ranges: Optional[list[str]] = None,
    ) -> SetBastionAllowedIPsResponse:
        """
        Set all IP ranges allowed for SSH bastion.
        Set a definitive list of IP ranges (in CIDR notation) allowed to connect to the SSH bastion.
        :param gateway_id: ID of the gateway on which to set the allowed IP range.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param ip_ranges: New list of IP ranges (each range in CIDR notation) allowed to connect to the SSH bastion.
        :return: :class:`SetBastionAllowedIPsResponse <SetBastionAllowedIPsResponse>`

        Usage:
        ::

            result = api.set_bastion_allowed_i_ps(
                gateway_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)

        res = self._request(
            "PUT",
            f"/vpc-gw/v2/zones/{param_zone}/gateways/{param_gateway_id}/bastion-allowed-ips",
            body=marshal_SetBastionAllowedIPsRequest(
                SetBastionAllowedIPsRequest(
                    gateway_id=gateway_id,
                    zone=zone,
                    ip_ranges=ip_ranges,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetBastionAllowedIPsResponse(res.json())

    def delete_bastion_allowed_i_ps(
        self,
        *,
        gateway_id: str,
        ip_range: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete allowed IP range from SSH bastion.
        Delete an IP range (defined in CIDR notation) from SSH bastion, so that it is no longer allowed to connect.
        :param gateway_id: ID of the gateway on which to delete the allowed IP range.
        :param ip_range: IP range to delete from SSH bastion's list of allowed IPs.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_bastion_allowed_i_ps(
                gateway_id="example",
                ip_range="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_gateway_id = validate_path_param("gateway_id", gateway_id)
        param_ip_range = validate_path_param("ip_range", ip_range)

        res = self._request(
            "DELETE",
            f"/vpc-gw/v2/zones/{param_zone}/gateways/{param_gateway_id}/bastion-allowed-ips/{param_ip_range}",
        )

        self._throw_on_error(res)
