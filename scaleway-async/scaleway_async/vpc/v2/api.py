# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    random_name,
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    Action,
    ListIngressRulesRequestOrderBy,
    ListPrivateNetworksRequestOrderBy,
    ListSubnetOverlapsRequestOrderBy,
    ListSubnetsRequestOrderBy,
    ListVPCConnectorsRequestOrderBy,
    ListVPCsRequestOrderBy,
    VPCConnectorStatus,
    AclRule,
    CreateIngressRuleRequest,
    CreatePrivateNetworkRequest,
    CreateRouteRequest,
    CreateVPCConnectorRequest,
    CreateVPCRequest,
    GetAclResponse,
    IngressRule,
    ListIngressRulesResponse,
    ListPrivateNetworksResponse,
    ListSubnetOverlapsResponse,
    ListSubnetOverlapsResponseSubnetOverlap,
    ListSubnetsResponse,
    ListVPCConnectorsResponse,
    ListVPCsResponse,
    PrivateNetwork,
    Route,
    SetAclRequest,
    SetAclResponse,
    Subnet,
    UpdateIngressRuleRequest,
    UpdatePrivateNetworkRequest,
    UpdateRouteRequest,
    UpdateVPCConnectorRequest,
    UpdateVPCRequest,
    VPC,
    VPCConnector,
)
from .marshalling import (
    unmarshal_PrivateNetwork,
    unmarshal_Route,
    unmarshal_IngressRule,
    unmarshal_VPCConnector,
    unmarshal_VPC,
    unmarshal_GetAclResponse,
    unmarshal_ListIngressRulesResponse,
    unmarshal_ListPrivateNetworksResponse,
    unmarshal_ListSubnetOverlapsResponse,
    unmarshal_ListSubnetsResponse,
    unmarshal_ListVPCConnectorsResponse,
    unmarshal_ListVPCsResponse,
    unmarshal_SetAclResponse,
    marshal_CreateIngressRuleRequest,
    marshal_CreatePrivateNetworkRequest,
    marshal_CreateRouteRequest,
    marshal_CreateVPCConnectorRequest,
    marshal_CreateVPCRequest,
    marshal_SetAclRequest,
    marshal_UpdateIngressRuleRequest,
    marshal_UpdatePrivateNetworkRequest,
    marshal_UpdateRouteRequest,
    marshal_UpdateVPCConnectorRequest,
    marshal_UpdateVPCRequest,
)


class VpcV2API(API):
    """
    This API allows you to manage your Virtual Private Clouds (VPCs) and Private Networks.
    """

    async def list_vp_cs(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListVPCsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        is_default: Optional[bool] = None,
        routing_enabled: Optional[bool] = None,
    ) -> ListVPCsResponse:
        """
        List VPCs.
        List existing VPCs in the specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned VPCs.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of VPCs to return per page.
        :param name: Name to filter for. Only VPCs with names containing this string will be returned.
        :param tags: Tags to filter for. Only VPCs with one or more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only VPCs belonging to this Organization will be returned.
        :param project_id: Project ID to filter for. Only VPCs belonging to this Project will be returned.
        :param is_default: Defines whether to filter only for VPCs which are the default one for their Project.
        :param routing_enabled: Defines whether to filter only for VPCs which route traffic between their Private Networks.
        :return: :class:`ListVPCsResponse <ListVPCsResponse>`

        Usage:
        ::

            result = await api.list_vp_cs()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/vpc/v2/regions/{param_region}/vpcs",
            params={
                "is_default": is_default,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "routing_enabled": routing_enabled,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVPCsResponse(res.json())

    async def list_vp_cs_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListVPCsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        is_default: Optional[bool] = None,
        routing_enabled: Optional[bool] = None,
    ) -> list[VPC]:
        """
        List VPCs.
        List existing VPCs in the specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned VPCs.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of VPCs to return per page.
        :param name: Name to filter for. Only VPCs with names containing this string will be returned.
        :param tags: Tags to filter for. Only VPCs with one or more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only VPCs belonging to this Organization will be returned.
        :param project_id: Project ID to filter for. Only VPCs belonging to this Project will be returned.
        :param is_default: Defines whether to filter only for VPCs which are the default one for their Project.
        :param routing_enabled: Defines whether to filter only for VPCs which route traffic between their Private Networks.
        :return: :class:`list[VPC] <list[VPC]>`

        Usage:
        ::

            result = await api.list_vp_cs_all()
        """

        return await fetch_all_pages_async(
            type=ListVPCsResponse,
            key="vpcs",
            fetcher=self.list_vp_cs,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
                "tags": tags,
                "organization_id": organization_id,
                "project_id": project_id,
                "is_default": is_default,
                "routing_enabled": routing_enabled,
            },
        )

    async def create_vpc(
        self,
        *,
        enable_routing: bool,
        enable_transitivity: bool,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> VPC:
        """
        Create a VPC.
        Create a new VPC in the specified region.
        :param enable_routing: Enable routing between Private Networks in the VPC.
        :param enable_transitivity: Enable packets from peered VPCs to transit through this VPC.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name for the VPC.
        :param project_id: Scaleway Project in which to create the VPC.
        :param tags: Tags for the VPC.
        :return: :class:`VPC <VPC>`

        Usage:
        ::

            result = await api.create_vpc(
                enable_routing=False,
                enable_transitivity=False,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/vpc/v2/regions/{param_region}/vpcs",
            body=marshal_CreateVPCRequest(
                CreateVPCRequest(
                    enable_routing=enable_routing,
                    enable_transitivity=enable_transitivity,
                    region=region,
                    name=name or random_name(prefix="vpc"),
                    project_id=project_id,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_VPC(res.json())

    async def get_vpc(
        self,
        *,
        vpc_id: str,
        region: Optional[ScwRegion] = None,
    ) -> VPC:
        """
        Get a VPC.
        Retrieve details of an existing VPC, specified by its VPC ID.
        :param vpc_id: VPC ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`VPC <VPC>`

        Usage:
        ::

            result = await api.get_vpc(
                vpc_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_vpc_id = validate_path_param("vpc_id", vpc_id)

        res = self._request(
            "GET",
            f"/vpc/v2/regions/{param_region}/vpcs/{param_vpc_id}",
        )

        self._throw_on_error(res)
        return unmarshal_VPC(res.json())

    async def update_vpc(
        self,
        *,
        vpc_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> VPC:
        """
        Update VPC.
        Update parameters including name and tags of the specified VPC.
        :param vpc_id: VPC ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name for the VPC.
        :param tags: Tags for the VPC.
        :return: :class:`VPC <VPC>`

        Usage:
        ::

            result = await api.update_vpc(
                vpc_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_vpc_id = validate_path_param("vpc_id", vpc_id)

        res = self._request(
            "PATCH",
            f"/vpc/v2/regions/{param_region}/vpcs/{param_vpc_id}",
            body=marshal_UpdateVPCRequest(
                UpdateVPCRequest(
                    vpc_id=vpc_id,
                    region=region,
                    name=name,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_VPC(res.json())

    async def delete_vpc(
        self,
        *,
        vpc_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a VPC.
        Delete a VPC specified by its VPC ID.
        :param vpc_id: VPC ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_vpc(
                vpc_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_vpc_id = validate_path_param("vpc_id", vpc_id)

        res = self._request(
            "DELETE",
            f"/vpc/v2/regions/{param_region}/vpcs/{param_vpc_id}",
        )

        self._throw_on_error(res)

    async def list_private_networks(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListPrivateNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        private_network_ids: Optional[list[str]] = None,
        vpc_id: Optional[str] = None,
        dhcp_enabled: Optional[bool] = None,
    ) -> ListPrivateNetworksResponse:
        """
        List Private Networks.
        List existing Private Networks in the specified region. By default, the Private Networks returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned Private Networks.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of Private Networks to return per page.
        :param name: Name to filter for. Only Private Networks with names containing this string will be returned.
        :param tags: Tags to filter for. Only Private Networks with one or more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only Private Networks belonging to this Organization will be returned.
        :param project_id: Project ID to filter for. Only Private Networks belonging to this Project will be returned.
        :param private_network_ids: Private Network IDs to filter for. Only Private Networks with one of these IDs will be returned.
        :param vpc_id: VPC ID to filter for. Only Private Networks belonging to this VPC will be returned.
        :param dhcp_enabled: DHCP status to filter for. When true, only Private Networks with managed DHCP enabled will be returned.
        :return: :class:`ListPrivateNetworksResponse <ListPrivateNetworksResponse>`

        Usage:
        ::

            result = await api.list_private_networks()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/vpc/v2/regions/{param_region}/private-networks",
            params={
                "dhcp_enabled": dhcp_enabled,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "private_network_ids": private_network_ids,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
                "vpc_id": vpc_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPrivateNetworksResponse(res.json())

    async def list_private_networks_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListPrivateNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        private_network_ids: Optional[list[str]] = None,
        vpc_id: Optional[str] = None,
        dhcp_enabled: Optional[bool] = None,
    ) -> list[PrivateNetwork]:
        """
        List Private Networks.
        List existing Private Networks in the specified region. By default, the Private Networks returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned Private Networks.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of Private Networks to return per page.
        :param name: Name to filter for. Only Private Networks with names containing this string will be returned.
        :param tags: Tags to filter for. Only Private Networks with one or more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only Private Networks belonging to this Organization will be returned.
        :param project_id: Project ID to filter for. Only Private Networks belonging to this Project will be returned.
        :param private_network_ids: Private Network IDs to filter for. Only Private Networks with one of these IDs will be returned.
        :param vpc_id: VPC ID to filter for. Only Private Networks belonging to this VPC will be returned.
        :param dhcp_enabled: DHCP status to filter for. When true, only Private Networks with managed DHCP enabled will be returned.
        :return: :class:`list[PrivateNetwork] <list[PrivateNetwork]>`

        Usage:
        ::

            result = await api.list_private_networks_all()
        """

        return await fetch_all_pages_async(
            type=ListPrivateNetworksResponse,
            key="private_networks",
            fetcher=self.list_private_networks,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
                "tags": tags,
                "organization_id": organization_id,
                "project_id": project_id,
                "private_network_ids": private_network_ids,
                "vpc_id": vpc_id,
                "dhcp_enabled": dhcp_enabled,
            },
        )

    async def create_private_network(
        self,
        *,
        default_route_propagation_enabled: bool,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        subnets: Optional[list[str]] = None,
        vpc_id: Optional[str] = None,
    ) -> PrivateNetwork:
        """
        Create a Private Network.
        Create a new Private Network. Once created, you can attach Scaleway resources which are in the same region.
        :param default_route_propagation_enabled: Defines whether default v4 and v6 routes are propagated for this Private Network.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name for the Private Network.
        :param project_id: Scaleway Project in which to create the Private Network.
        :param tags: Tags for the Private Network.
        :param subnets: Private Network subnets CIDR.
        :param vpc_id: VPC in which to create the Private Network.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = await api.create_private_network(
                default_route_propagation_enabled=False,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/vpc/v2/regions/{param_region}/private-networks",
            body=marshal_CreatePrivateNetworkRequest(
                CreatePrivateNetworkRequest(
                    default_route_propagation_enabled=default_route_propagation_enabled,
                    region=region,
                    name=name or random_name(prefix="pn"),
                    project_id=project_id,
                    tags=tags,
                    subnets=subnets,
                    vpc_id=vpc_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNetwork(res.json())

    async def get_private_network(
        self,
        *,
        private_network_id: str,
        region: Optional[ScwRegion] = None,
    ) -> PrivateNetwork:
        """
        Get a Private Network.
        Retrieve information about an existing Private Network, specified by its Private Network ID. Its full details are returned in the response object.
        :param private_network_id: Private Network ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = await api.get_private_network(
                private_network_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "GET",
            f"/vpc/v2/regions/{param_region}/private-networks/{param_private_network_id}",
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNetwork(res.json())

    async def update_private_network(
        self,
        *,
        private_network_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        default_route_propagation_enabled: Optional[bool] = None,
    ) -> PrivateNetwork:
        """
        Update Private Network.
        Update parameters (such as name or tags) of an existing Private Network, specified by its Private Network ID.
        :param private_network_id: Private Network ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name for the Private Network.
        :param tags: Tags for the Private Network.
        :param default_route_propagation_enabled: Defines whether default v4 and v6 routes are propagated for this Private Network.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = await api.update_private_network(
                private_network_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "PATCH",
            f"/vpc/v2/regions/{param_region}/private-networks/{param_private_network_id}",
            body=marshal_UpdatePrivateNetworkRequest(
                UpdatePrivateNetworkRequest(
                    private_network_id=private_network_id,
                    region=region,
                    name=name,
                    tags=tags,
                    default_route_propagation_enabled=default_route_propagation_enabled,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNetwork(res.json())

    async def delete_private_network(
        self,
        *,
        private_network_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a Private Network.
        Delete an existing Private Network. Note that you must first detach all resources from the network, in order to delete it.
        :param private_network_id: Private Network ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_private_network(
                private_network_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "DELETE",
            f"/vpc/v2/regions/{param_region}/private-networks/{param_private_network_id}",
        )

        self._throw_on_error(res)

    async def enable_dhcp(
        self,
        *,
        private_network_id: str,
        region: Optional[ScwRegion] = None,
    ) -> PrivateNetwork:
        """
        Enable DHCP on a Private Network.
        Enable DHCP managed on an existing Private Network. Note that you will not be able to deactivate it afterwards.
        :param private_network_id: Private Network ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = await api.enable_dhcp(
                private_network_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "POST",
            f"/vpc/v2/regions/{param_region}/private-networks/{param_private_network_id}/enable-dhcp",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNetwork(res.json())

    async def enable_routing(
        self,
        *,
        vpc_id: str,
        region: Optional[ScwRegion] = None,
    ) -> VPC:
        """
        Enable routing on a VPC.
        Enable routing on an existing VPC. Note that you will not be able to deactivate it afterwards.
        :param vpc_id: VPC ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`VPC <VPC>`

        Usage:
        ::

            result = await api.enable_routing(
                vpc_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_vpc_id = validate_path_param("vpc_id", vpc_id)

        res = self._request(
            "POST",
            f"/vpc/v2/regions/{param_region}/vpcs/{param_vpc_id}/enable-routing",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_VPC(res.json())

    async def enable_custom_routes_propagation(
        self,
        *,
        vpc_id: str,
        region: Optional[ScwRegion] = None,
    ) -> VPC:
        """
        Enable custom routes propagation on a VPC.
        Enable custom routes propagation on an existing VPC. Note that you will not be able to deactivate it afterwards.
        :param vpc_id: VPC ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`VPC <VPC>`

        Usage:
        ::

            result = await api.enable_custom_routes_propagation(
                vpc_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_vpc_id = validate_path_param("vpc_id", vpc_id)

        res = self._request(
            "POST",
            f"/vpc/v2/regions/{param_region}/vpcs/{param_vpc_id}/enable-custom-routes-propagation",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_VPC(res.json())

    async def list_subnets(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListSubnetsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        subnet_ids: Optional[list[str]] = None,
        vpc_id: Optional[str] = None,
    ) -> ListSubnetsResponse:
        """
        List subnets.
        List any Private Network's subnets. See ListPrivateNetworks to list a specific Private Network's subnets.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned subnets.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of Private Networks to return per page.
        :param organization_id: Organization ID to filter for. Only subnets belonging to this Organization will be returned.
        :param project_id: Project ID to filter for. Only subnets belonging to this Project will be returned.
        :param subnet_ids: Subnet IDs to filter for. Only subnets matching the specified IDs will be returned.
        :param vpc_id: VPC ID to filter for. Only subnets belonging to this VPC will be returned.
        :return: :class:`ListSubnetsResponse <ListSubnetsResponse>`

        Usage:
        ::

            result = await api.list_subnets()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/vpc/v2/regions/{param_region}/subnets",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "subnet_ids": subnet_ids,
                "vpc_id": vpc_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSubnetsResponse(res.json())

    async def list_subnets_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListSubnetsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        subnet_ids: Optional[list[str]] = None,
        vpc_id: Optional[str] = None,
    ) -> list[Subnet]:
        """
        List subnets.
        List any Private Network's subnets. See ListPrivateNetworks to list a specific Private Network's subnets.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned subnets.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of Private Networks to return per page.
        :param organization_id: Organization ID to filter for. Only subnets belonging to this Organization will be returned.
        :param project_id: Project ID to filter for. Only subnets belonging to this Project will be returned.
        :param subnet_ids: Subnet IDs to filter for. Only subnets matching the specified IDs will be returned.
        :param vpc_id: VPC ID to filter for. Only subnets belonging to this VPC will be returned.
        :return: :class:`list[Subnet] <list[Subnet]>`

        Usage:
        ::

            result = await api.list_subnets_all()
        """

        return await fetch_all_pages_async(
            type=ListSubnetsResponse,
            key="subnets",
            fetcher=self.list_subnets,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "project_id": project_id,
                "subnet_ids": subnet_ids,
                "vpc_id": vpc_id,
            },
        )

    async def create_route(
        self,
        *,
        description: str,
        vpc_id: str,
        destination: str,
        region: Optional[ScwRegion] = None,
        tags: Optional[list[str]] = None,
        nexthop_resource_id: Optional[str] = None,
        nexthop_private_network_id: Optional[str] = None,
        nexthop_vpc_connector_id: Optional[str] = None,
    ) -> Route:
        """
        Create a Route.
        Create a new custom Route.
        :param description: Route description.
        :param vpc_id: VPC the Route belongs to.
        :param destination: Destination of the Route.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tags: Tags of the Route.
        :param nexthop_resource_id: ID of the nexthop resource.
        :param nexthop_private_network_id: ID of the nexthop private network.
        :param nexthop_vpc_connector_id: ID of the nexthop VPC Connector.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = await api.create_route(
                description="example",
                vpc_id="example",
                destination="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/vpc/v2/regions/{param_region}/routes",
            body=marshal_CreateRouteRequest(
                CreateRouteRequest(
                    description=description,
                    vpc_id=vpc_id,
                    destination=destination,
                    region=region,
                    tags=tags,
                    nexthop_resource_id=nexthop_resource_id,
                    nexthop_private_network_id=nexthop_private_network_id,
                    nexthop_vpc_connector_id=nexthop_vpc_connector_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    async def get_route(
        self,
        *,
        route_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Route:
        """
        Get a Route.
        Retrieve details of an existing Route, specified by its Route ID.
        :param route_id: Route ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = await api.get_route(
                route_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "GET",
            f"/vpc/v2/regions/{param_region}/routes/{param_route_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    async def update_route(
        self,
        *,
        route_id: str,
        region: Optional[ScwRegion] = None,
        description: Optional[str] = None,
        tags: Optional[list[str]] = None,
        destination: Optional[str] = None,
        nexthop_resource_id: Optional[str] = None,
        nexthop_private_network_id: Optional[str] = None,
        nexthop_vpc_connector_id: Optional[str] = None,
    ) -> Route:
        """
        Update Route.
        Update parameters of the specified Route.
        :param route_id: Route ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param description: Route description.
        :param tags: Tags of the Route.
        :param destination: Destination of the Route.
        :param nexthop_resource_id: ID of the nexthop resource.
        :param nexthop_private_network_id: ID of the nexthop private network.
        :param nexthop_vpc_connector_id: ID of the nexthop VPC connector.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = await api.update_route(
                route_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "PATCH",
            f"/vpc/v2/regions/{param_region}/routes/{param_route_id}",
            body=marshal_UpdateRouteRequest(
                UpdateRouteRequest(
                    route_id=route_id,
                    region=region,
                    description=description,
                    tags=tags,
                    destination=destination,
                    nexthop_resource_id=nexthop_resource_id,
                    nexthop_private_network_id=nexthop_private_network_id,
                    nexthop_vpc_connector_id=nexthop_vpc_connector_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    async def delete_route(
        self,
        *,
        route_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a Route.
        Delete a Route specified by its Route ID.
        :param route_id: Route ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_route(
                route_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "DELETE",
            f"/vpc/v2/regions/{param_region}/routes/{param_route_id}",
        )

        self._throw_on_error(res)

    async def get_acl(
        self,
        *,
        vpc_id: str,
        is_ipv6: bool,
        region: Optional[ScwRegion] = None,
    ) -> GetAclResponse:
        """
        Get ACL Rules for VPC.
        Retrieve a list of ACL rules for a VPC, specified by its VPC ID.
        :param vpc_id: ID of the Network ACL's VPC.
        :param is_ipv6: Defines whether this set of ACL rules is for IPv6 (false = IPv4). Each Network ACL can have rules for only one IP type.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`GetAclResponse <GetAclResponse>`

        Usage:
        ::

            result = await api.get_acl(
                vpc_id="example",
                is_ipv6=False,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_vpc_id = validate_path_param("vpc_id", vpc_id)

        res = self._request(
            "GET",
            f"/vpc/v2/regions/{param_region}/vpcs/{param_vpc_id}/acl-rules",
            params={
                "is_ipv6": is_ipv6,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GetAclResponse(res.json())

    async def set_acl(
        self,
        *,
        vpc_id: str,
        rules: list[AclRule],
        is_ipv6: bool,
        default_policy: Action,
        region: Optional[ScwRegion] = None,
    ) -> SetAclResponse:
        """
        Set VPC ACL rules.
        Set the list of ACL rules and the default routing policy for a VPC.
        :param vpc_id: ID of the Network ACL's VPC.
        :param rules: List of Network ACL rules.
        :param is_ipv6: Defines whether this set of ACL rules is for IPv6 (false = IPv4). Each Network ACL can have rules for only one IP type.
        :param default_policy: Action to take for packets which do not match any rules.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`SetAclResponse <SetAclResponse>`

        Usage:
        ::

            result = await api.set_acl(
                vpc_id="example",
                rules=[],
                is_ipv6=False,
                default_policy=Action.unknown_action,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_vpc_id = validate_path_param("vpc_id", vpc_id)

        res = self._request(
            "PUT",
            f"/vpc/v2/regions/{param_region}/vpcs/{param_vpc_id}/acl-rules",
            body=marshal_SetAclRequest(
                SetAclRequest(
                    vpc_id=vpc_id,
                    rules=rules,
                    is_ipv6=is_ipv6,
                    default_policy=default_policy,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetAclResponse(res.json())

    async def list_vpc_connectors(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListVPCConnectorsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        vpc_id: Optional[str] = None,
        target_vpc_id: Optional[str] = None,
        status: Optional[VPCConnectorStatus] = None,
    ) -> ListVPCConnectorsResponse:
        """
        List VPC connectors.
        List existing VPC connectors in the specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned VPC connectors.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of VPC connectors to return per page.
        :param name: Name to filter for. Only connectors with names containing this string will be returned.
        :param tags: Tags to filter for. Only connectors with one or more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only connectors belonging to this Organization will be returned.
        :param project_id: Project ID to filter for. Only connectors belonging to this Project will be returned.
        :param vpc_id: VPC ID to filter for. Only connectors belonging to this VPC will be returned.
        :param target_vpc_id: Target VPC ID to filter for. Only connectors belonging to this target VPC will be returned.
        :param status: Status of the VPC connector.
        :return: :class:`ListVPCConnectorsResponse <ListVPCConnectorsResponse>`

        Usage:
        ::

            result = await api.list_vpc_connectors()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/vpc/v2/regions/{param_region}/vpc-connectors",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "status": status,
                "tags": tags,
                "target_vpc_id": target_vpc_id,
                "vpc_id": vpc_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVPCConnectorsResponse(res.json())

    async def list_vpc_connectors_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListVPCConnectorsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        vpc_id: Optional[str] = None,
        target_vpc_id: Optional[str] = None,
        status: Optional[VPCConnectorStatus] = None,
    ) -> list[VPCConnector]:
        """
        List VPC connectors.
        List existing VPC connectors in the specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned VPC connectors.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of VPC connectors to return per page.
        :param name: Name to filter for. Only connectors with names containing this string will be returned.
        :param tags: Tags to filter for. Only connectors with one or more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only connectors belonging to this Organization will be returned.
        :param project_id: Project ID to filter for. Only connectors belonging to this Project will be returned.
        :param vpc_id: VPC ID to filter for. Only connectors belonging to this VPC will be returned.
        :param target_vpc_id: Target VPC ID to filter for. Only connectors belonging to this target VPC will be returned.
        :param status: Status of the VPC connector.
        :return: :class:`list[VPCConnector] <list[VPCConnector]>`

        Usage:
        ::

            result = await api.list_vpc_connectors_all()
        """

        return await fetch_all_pages_async(
            type=ListVPCConnectorsResponse,
            key="vpc_connectors",
            fetcher=self.list_vpc_connectors,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
                "tags": tags,
                "organization_id": organization_id,
                "project_id": project_id,
                "vpc_id": vpc_id,
                "target_vpc_id": target_vpc_id,
                "status": status,
            },
        )

    async def create_vpc_connector(
        self,
        *,
        vpc_id: str,
        target_vpc_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> VPCConnector:
        """
        Create a VPC connector.
        Create a new VPC connector in the specified region.
        :param vpc_id: VPC ID to filter for. Only connectors belonging to this VPC will be returned.
        :param target_vpc_id: Target VPC ID to filter for. Only connectors belonging to this target VPC will be returned.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name for the VPC connector.
        :param tags: Tags for the VPC connector.
        :return: :class:`VPCConnector <VPCConnector>`

        Usage:
        ::

            result = await api.create_vpc_connector(
                vpc_id="example",
                target_vpc_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/vpc/v2/regions/{param_region}/vpc-connectors",
            body=marshal_CreateVPCConnectorRequest(
                CreateVPCConnectorRequest(
                    vpc_id=vpc_id,
                    target_vpc_id=target_vpc_id,
                    region=region,
                    name=name or random_name(prefix="VPCConnector"),
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_VPCConnector(res.json())

    async def get_vpc_connector(
        self,
        *,
        vpc_connector_id: str,
        region: Optional[ScwRegion] = None,
    ) -> VPCConnector:
        """
        Get a VPC connector.
        Retrieve details of an existing VPC connector, specified by its VPC connector ID.
        :param vpc_connector_id: VPC connector ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`VPCConnector <VPCConnector>`

        Usage:
        ::

            result = await api.get_vpc_connector(
                vpc_connector_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_vpc_connector_id = validate_path_param(
            "vpc_connector_id", vpc_connector_id
        )

        res = self._request(
            "GET",
            f"/vpc/v2/regions/{param_region}/vpc-connectors/{param_vpc_connector_id}",
        )

        self._throw_on_error(res)
        return unmarshal_VPCConnector(res.json())

    async def update_vpc_connector(
        self,
        *,
        vpc_connector_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> VPCConnector:
        """
        Update VPC connector.
        Update parameters including name and tags of the specified VPC connector.
        :param vpc_connector_id: VPC connector ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name for the VPC connector.
        :param tags: Tags for the VPC connector.
        :return: :class:`VPCConnector <VPCConnector>`

        Usage:
        ::

            result = await api.update_vpc_connector(
                vpc_connector_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_vpc_connector_id = validate_path_param(
            "vpc_connector_id", vpc_connector_id
        )

        res = self._request(
            "PATCH",
            f"/vpc/v2/regions/{param_region}/vpc-connectors/{param_vpc_connector_id}",
            body=marshal_UpdateVPCConnectorRequest(
                UpdateVPCConnectorRequest(
                    vpc_connector_id=vpc_connector_id,
                    region=region,
                    name=name,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_VPCConnector(res.json())

    async def delete_vpc_connector(
        self,
        *,
        vpc_connector_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a VPC connector.
        Delete a VPC connector specified by its VPC connector ID.
        :param vpc_connector_id: VPC connector ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_vpc_connector(
                vpc_connector_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_vpc_connector_id = validate_path_param(
            "vpc_connector_id", vpc_connector_id
        )

        res = self._request(
            "DELETE",
            f"/vpc/v2/regions/{param_region}/vpc-connectors/{param_vpc_connector_id}",
        )

        self._throw_on_error(res)

    async def list_subnet_overlaps(
        self,
        *,
        vpc_connector_id: str,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListSubnetOverlapsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListSubnetOverlapsResponse:
        """
        List subnet overlaps.
        List subnet overlaps between the VPCs on both sides of a connector, or for a specific subnet if specified.
        :param vpc_connector_id: VPC Peering connector ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned Subnet overlaps.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of Subnet overlaps to return per page.
        :return: :class:`ListSubnetOverlapsResponse <ListSubnetOverlapsResponse>`

        Usage:
        ::

            result = await api.list_subnet_overlaps(
                vpc_connector_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_vpc_connector_id = validate_path_param(
            "vpc_connector_id", vpc_connector_id
        )

        res = self._request(
            "GET",
            f"/vpc/v2/regions/{param_region}/vpc-connectors/{param_vpc_connector_id}/subnet-overlaps",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSubnetOverlapsResponse(res.json())

    async def list_subnet_overlaps_all(
        self,
        *,
        vpc_connector_id: str,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListSubnetOverlapsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[ListSubnetOverlapsResponseSubnetOverlap]:
        """
        List subnet overlaps.
        List subnet overlaps between the VPCs on both sides of a connector, or for a specific subnet if specified.
        :param vpc_connector_id: VPC Peering connector ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned Subnet overlaps.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of Subnet overlaps to return per page.
        :return: :class:`list[ListSubnetOverlapsResponseSubnetOverlap] <list[ListSubnetOverlapsResponseSubnetOverlap]>`

        Usage:
        ::

            result = await api.list_subnet_overlaps_all(
                vpc_connector_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListSubnetOverlapsResponse,
            key="subnet_overlaps",
            fetcher=self.list_subnet_overlaps,
            args={
                "vpc_connector_id": vpc_connector_id,
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    async def list_ingress_rules(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListIngressRulesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        vpc_id: Optional[str] = None,
        nexthop_resource_ip: Optional[str] = None,
        nexthop_private_network_id: Optional[str] = None,
        is_ipv6: Optional[bool] = None,
        tags: Optional[list[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListIngressRulesResponse:
        """
        List ingress rules.
        List existing ingress rules in the specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned ingress rules.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of ingress rules to return per page.
        :param vpc_id: ID of the VPC to filter for.
        :param nexthop_resource_ip: Next hop IP to filter for.
        :param nexthop_private_network_id: Next hop Private Network ID to filter for. Only ingress rules with this Private Network as next hop will be returned.
        :param is_ipv6: Whether to return only IPv4 or IPv6 ingress rules.
        :param tags: Tags to filter for. Only ingress rules with one or more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only ingress rules belonging to this Organization will be returned.
        :param project_id: Project ID to filter for. Only ingress rules belonging to this Project will be returned.
        :return: :class:`ListIngressRulesResponse <ListIngressRulesResponse>`

        Usage:
        ::

            result = await api.list_ingress_rules()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/vpc/v2/regions/{param_region}/ingress-rules",
            params={
                "is_ipv6": is_ipv6,
                "nexthop_private_network_id": nexthop_private_network_id,
                "nexthop_resource_ip": nexthop_resource_ip,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
                "vpc_id": vpc_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListIngressRulesResponse(res.json())

    async def list_ingress_rules_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListIngressRulesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        vpc_id: Optional[str] = None,
        nexthop_resource_ip: Optional[str] = None,
        nexthop_private_network_id: Optional[str] = None,
        is_ipv6: Optional[bool] = None,
        tags: Optional[list[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> list[IngressRule]:
        """
        List ingress rules.
        List existing ingress rules in the specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned ingress rules.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of ingress rules to return per page.
        :param vpc_id: ID of the VPC to filter for.
        :param nexthop_resource_ip: Next hop IP to filter for.
        :param nexthop_private_network_id: Next hop Private Network ID to filter for. Only ingress rules with this Private Network as next hop will be returned.
        :param is_ipv6: Whether to return only IPv4 or IPv6 ingress rules.
        :param tags: Tags to filter for. Only ingress rules with one or more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only ingress rules belonging to this Organization will be returned.
        :param project_id: Project ID to filter for. Only ingress rules belonging to this Project will be returned.
        :return: :class:`list[IngressRule] <list[IngressRule]>`

        Usage:
        ::

            result = await api.list_ingress_rules_all()
        """

        return await fetch_all_pages_async(
            type=ListIngressRulesResponse,
            key="rules",
            fetcher=self.list_ingress_rules,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "vpc_id": vpc_id,
                "nexthop_resource_ip": nexthop_resource_ip,
                "nexthop_private_network_id": nexthop_private_network_id,
                "is_ipv6": is_ipv6,
                "tags": tags,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    async def create_ingress_rule(
        self,
        *,
        vpc_id: str,
        source: str,
        nexthop_resource_ip: str,
        nexthop_private_network_id: str,
        region: Optional[ScwRegion] = None,
        description: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> IngressRule:
        """
        Create an ingress rule.
        Create an ingress rule in the specified region.
        :param vpc_id: ID of the VPC this rule will belong to.
        :param source: Source network to match ingress traffic on. Can be IPv6 or IPv4.
        :param nexthop_resource_ip: IP of the local resource to redirect ingress traffic to. IP version must be consistent with the source network.
        :param nexthop_private_network_id: ID of the Private Network the destination resource is in.
        :param region: Region to target. If none is passed will use default region from the config.
        :param description: Description for this ingress rule.
        :param tags: Tags for this ingress rule.
        :return: :class:`IngressRule <IngressRule>`

        Usage:
        ::

            result = await api.create_ingress_rule(
                vpc_id="example",
                source="example",
                nexthop_resource_ip="example",
                nexthop_private_network_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/vpc/v2/regions/{param_region}/ingress-rules",
            body=marshal_CreateIngressRuleRequest(
                CreateIngressRuleRequest(
                    vpc_id=vpc_id,
                    source=source,
                    nexthop_resource_ip=nexthop_resource_ip,
                    nexthop_private_network_id=nexthop_private_network_id,
                    region=region,
                    description=description,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IngressRule(res.json())

    async def get_ingress_rule(
        self,
        *,
        rule_id: str,
        region: Optional[ScwRegion] = None,
    ) -> IngressRule:
        """
        Get an ingress rule.
        Retrieve details of an existing ingress rule, specified by its ingress rule ID.
        :param rule_id: ID of the ingress rule to return.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`IngressRule <IngressRule>`

        Usage:
        ::

            result = await api.get_ingress_rule(
                rule_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_rule_id = validate_path_param("rule_id", rule_id)

        res = self._request(
            "GET",
            f"/vpc/v2/regions/{param_region}/ingress-rules/{param_rule_id}",
        )

        self._throw_on_error(res)
        return unmarshal_IngressRule(res.json())

    async def update_ingress_rule(
        self,
        *,
        rule_id: str,
        region: Optional[ScwRegion] = None,
        source: Optional[str] = None,
        nexthop_resource_ip: Optional[str] = None,
        nexthop_private_network_id: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> IngressRule:
        """
        Update an ingress rule.
        Update an ingress rule specified by its ingress rule ID.
        :param rule_id: ID of the ingress rule to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param source: Source network to match ingress traffic on. Can be IPv4 or IPv6.
        :param nexthop_resource_ip: IP of the local resource to redirect ingress traffic to. IP version must be consistent with the source network.
        :param nexthop_private_network_id: ID of the Private Network the destination resource is in.
        :param description: Description to set for this ingress rule.
        :param tags: Tags to set for this ingress rule.
        :return: :class:`IngressRule <IngressRule>`

        Usage:
        ::

            result = await api.update_ingress_rule(
                rule_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_rule_id = validate_path_param("rule_id", rule_id)

        res = self._request(
            "PATCH",
            f"/vpc/v2/regions/{param_region}/ingress-rules/{param_rule_id}",
            body=marshal_UpdateIngressRuleRequest(
                UpdateIngressRuleRequest(
                    rule_id=rule_id,
                    region=region,
                    source=source,
                    nexthop_resource_ip=nexthop_resource_ip,
                    nexthop_private_network_id=nexthop_private_network_id,
                    description=description,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IngressRule(res.json())

    async def delete_ingress_rule(
        self,
        *,
        rule_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete an ingress rule.
        Delete an ingress rule specified by its ingress rule ID.
        :param rule_id: ID of the ingress rule to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_ingress_rule(
                rule_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_rule_id = validate_path_param("rule_id", rule_id)

        res = self._request(
            "DELETE",
            f"/vpc/v2/regions/{param_region}/ingress-rules/{param_rule_id}",
        )

        self._throw_on_error(res)
