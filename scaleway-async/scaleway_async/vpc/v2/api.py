# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    random_name,
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    ListPrivateNetworksRequestOrderBy,
    ListSubnetsRequestOrderBy,
    ListVPCsRequestOrderBy,
    AddSubnetsRequest,
    AddSubnetsResponse,
    CreatePrivateNetworkRequest,
    CreateRouteRequest,
    CreateVPCRequest,
    DeleteSubnetsRequest,
    DeleteSubnetsResponse,
    ListPrivateNetworksResponse,
    ListSubnetsResponse,
    ListVPCsResponse,
    MigrateZonalPrivateNetworksRequest,
    PrivateNetwork,
    Route,
    SetSubnetsRequest,
    SetSubnetsResponse,
    Subnet,
    UpdatePrivateNetworkRequest,
    UpdateRouteRequest,
    UpdateVPCRequest,
    VPC,
)
from .marshalling import (
    unmarshal_PrivateNetwork,
    unmarshal_Route,
    unmarshal_VPC,
    unmarshal_AddSubnetsResponse,
    unmarshal_DeleteSubnetsResponse,
    unmarshal_ListPrivateNetworksResponse,
    unmarshal_ListSubnetsResponse,
    unmarshal_ListVPCsResponse,
    unmarshal_SetSubnetsResponse,
    marshal_AddSubnetsRequest,
    marshal_CreatePrivateNetworkRequest,
    marshal_CreateRouteRequest,
    marshal_CreateVPCRequest,
    marshal_DeleteSubnetsRequest,
    marshal_MigrateZonalPrivateNetworksRequest,
    marshal_SetSubnetsRequest,
    marshal_UpdatePrivateNetworkRequest,
    marshal_UpdateRouteRequest,
    marshal_UpdateVPCRequest,
)


class VpcV2API(API):
    """
    This API allows you to manage your Virtual Private Clouds (VPCs) and Private Networks.
    """

    async def list_vp_cs(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListVPCsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
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
        :param tags: Tags to filter for. Only VPCs with one more more matching tags will be returned.
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
        region: Optional[Region] = None,
        order_by: Optional[ListVPCsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        is_default: Optional[bool] = None,
        routing_enabled: Optional[bool] = None,
    ) -> List[VPC]:
        """
        List VPCs.
        List existing VPCs in the specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned VPCs.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of VPCs to return per page.
        :param name: Name to filter for. Only VPCs with names containing this string will be returned.
        :param tags: Tags to filter for. Only VPCs with one more more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only VPCs belonging to this Organization will be returned.
        :param project_id: Project ID to filter for. Only VPCs belonging to this Project will be returned.
        :param is_default: Defines whether to filter only for VPCs which are the default one for their Project.
        :param routing_enabled: Defines whether to filter only for VPCs which route traffic between their Private Networks.
        :return: :class:`List[VPC] <List[VPC]>`

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
        region: Optional[Region] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> VPC:
        """
        Create a VPC.
        Create a new VPC in the specified region.
        :param enable_routing: Enable routing between Private Networks in the VPC.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name for the VPC.
        :param project_id: Scaleway Project in which to create the VPC.
        :param tags: Tags for the VPC.
        :return: :class:`VPC <VPC>`

        Usage:
        ::

            result = await api.create_vpc(
                enable_routing=False,
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
        region: Optional[Region] = None,
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
        region: Optional[Region] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
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
        region: Optional[Region] = None,
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
        region: Optional[Region] = None,
        order_by: Optional[ListPrivateNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        private_network_ids: Optional[List[str]] = None,
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
        region: Optional[Region] = None,
        order_by: Optional[ListPrivateNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        private_network_ids: Optional[List[str]] = None,
        vpc_id: Optional[str] = None,
        dhcp_enabled: Optional[bool] = None,
    ) -> List[PrivateNetwork]:
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
        :return: :class:`List[PrivateNetwork] <List[PrivateNetwork]>`

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
        region: Optional[Region] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        subnets: Optional[List[str]] = None,
        vpc_id: Optional[str] = None,
    ) -> PrivateNetwork:
        """
        Create a Private Network.
        Create a new Private Network. Once created, you can attach Scaleway resources which are in the same region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name for the Private Network.
        :param project_id: Scaleway Project in which to create the Private Network.
        :param tags: Tags for the Private Network.
        :param subnets: Private Network subnets CIDR.
        :param vpc_id: VPC in which to create the Private Network.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = await api.create_private_network()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/vpc/v2/regions/{param_region}/private-networks",
            body=marshal_CreatePrivateNetworkRequest(
                CreatePrivateNetworkRequest(
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
        region: Optional[Region] = None,
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
        region: Optional[Region] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> PrivateNetwork:
        """
        Update Private Network.
        Update parameters (such as name or tags) of an existing Private Network, specified by its Private Network ID.
        :param private_network_id: Private Network ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name for the Private Network.
        :param tags: Tags for the Private Network.
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
        region: Optional[Region] = None,
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

    async def migrate_zonal_private_networks(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        private_network_ids: Optional[List[str]] = None,
    ) -> None:
        """
        Migrate Private Networks from zoned to regional.
        Transform multiple existing zoned Private Networks (scoped to a single Availability Zone) into regional Private Networks, scoped to an entire region. You can transform one or many Private Networks (specified by their Private Network IDs) within a single Scaleway Organization or Project, with the same call.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Organization ID to target. The specified zoned Private Networks within this Organization will be migrated to regional.
        One-Of ('scope'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Project to target. The specified zoned Private Networks within this Project will be migrated to regional.
        One-Of ('scope'): at most one of 'organization_id', 'project_id' could be set.
        :param private_network_ids: IDs of the Private Networks to migrate.

        Usage:
        ::

            result = await api.migrate_zonal_private_networks()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/vpc/v2/regions/{param_region}/private-networks/migrate-zonal",
            body=marshal_MigrateZonalPrivateNetworksRequest(
                MigrateZonalPrivateNetworksRequest(
                    region=region,
                    private_network_ids=private_network_ids,
                    organization_id=organization_id,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def enable_dhcp(
        self,
        *,
        private_network_id: str,
        region: Optional[Region] = None,
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
        region: Optional[Region] = None,
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

    async def list_subnets(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListSubnetsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        subnet_ids: Optional[List[str]] = None,
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
        region: Optional[Region] = None,
        order_by: Optional[ListSubnetsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        subnet_ids: Optional[List[str]] = None,
        vpc_id: Optional[str] = None,
    ) -> List[Subnet]:
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
        :return: :class:`List[Subnet] <List[Subnet]>`

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

    async def set_subnets(
        self,
        *,
        private_network_id: str,
        region: Optional[Region] = None,
        subnets: Optional[List[str]] = None,
    ) -> SetSubnetsResponse:
        """
        Set a Private Network's subnets.
        Set subnets for an existing Private Network. Note that the method is PUT and not PATCH. Any existing subnets will be removed in favor of the new specified set of subnets.
        :param private_network_id: Private Network ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param subnets: Private Network subnets CIDR.
        :return: :class:`SetSubnetsResponse <SetSubnetsResponse>`

        Usage:
        ::

            result = await api.set_subnets(
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
            "PUT",
            f"/vpc/v2/regions/{param_region}/private-networks/{param_private_network_id}/subnets",
            body=marshal_SetSubnetsRequest(
                SetSubnetsRequest(
                    private_network_id=private_network_id,
                    region=region,
                    subnets=subnets,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetSubnetsResponse(res.json())

    async def add_subnets(
        self,
        *,
        private_network_id: str,
        region: Optional[Region] = None,
        subnets: Optional[List[str]] = None,
    ) -> AddSubnetsResponse:
        """
        Add subnets to a Private Network.
        Add new subnets to an existing Private Network.
        :param private_network_id: Private Network ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param subnets: Private Network subnets CIDR.
        :return: :class:`AddSubnetsResponse <AddSubnetsResponse>`

        Usage:
        ::

            result = await api.add_subnets(
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
            f"/vpc/v2/regions/{param_region}/private-networks/{param_private_network_id}/subnets",
            body=marshal_AddSubnetsRequest(
                AddSubnetsRequest(
                    private_network_id=private_network_id,
                    region=region,
                    subnets=subnets,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AddSubnetsResponse(res.json())

    async def delete_subnets(
        self,
        *,
        private_network_id: str,
        region: Optional[Region] = None,
        subnets: Optional[List[str]] = None,
    ) -> DeleteSubnetsResponse:
        """
        Delete subnets from a Private Network.
        Delete the specified subnets from a Private Network.
        :param private_network_id: Private Network ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param subnets: Private Network subnets CIDR.
        :return: :class:`DeleteSubnetsResponse <DeleteSubnetsResponse>`

        Usage:
        ::

            result = await api.delete_subnets(
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
            f"/vpc/v2/regions/{param_region}/private-networks/{param_private_network_id}/subnets",
            body=marshal_DeleteSubnetsRequest(
                DeleteSubnetsRequest(
                    private_network_id=private_network_id,
                    region=region,
                    subnets=subnets,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DeleteSubnetsResponse(res.json())

    async def create_route(
        self,
        *,
        description: str,
        vpc_id: str,
        destination: str,
        region: Optional[Region] = None,
        tags: Optional[List[str]] = None,
        nexthop_resource_id: Optional[str] = None,
        nexthop_private_network_id: Optional[str] = None,
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
        region: Optional[Region] = None,
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
        region: Optional[Region] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        destination: Optional[str] = None,
        nexthop_resource_id: Optional[str] = None,
        nexthop_private_network_id: Optional[str] = None,
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
        region: Optional[Region] = None,
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
