# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    fetch_all_pages_async,
    random_name,
    validate_path_param,
)
from .types import (
    ListPrivateNetworksRequestOrderBy,
    ListVPCsRequestOrderBy,
    AddSubnetsResponse,
    DeleteSubnetsResponse,
    ListPrivateNetworksResponse,
    ListVPCsResponse,
    PrivateNetwork,
    SetSubnetsResponse,
    VPC,
    CreateVPCRequest,
    UpdateVPCRequest,
    CreatePrivateNetworkRequest,
    UpdatePrivateNetworkRequest,
    MigrateZonalPrivateNetworksRequest,
    SetSubnetsRequest,
    AddSubnetsRequest,
    DeleteSubnetsRequest,
)
from .marshalling import (
    marshal_AddSubnetsRequest,
    marshal_CreatePrivateNetworkRequest,
    marshal_CreateVPCRequest,
    marshal_DeleteSubnetsRequest,
    marshal_MigrateZonalPrivateNetworksRequest,
    marshal_SetSubnetsRequest,
    marshal_UpdatePrivateNetworkRequest,
    marshal_UpdateVPCRequest,
    unmarshal_PrivateNetwork,
    unmarshal_VPC,
    unmarshal_AddSubnetsResponse,
    unmarshal_DeleteSubnetsResponse,
    unmarshal_ListPrivateNetworksResponse,
    unmarshal_ListVPCsResponse,
    unmarshal_SetSubnetsResponse,
)


class VpcV2API(API):
    """
    VPC API.

    VPC API.
    """

    async def list_vp_cs(
        self,
        *,
        region: Optional[Region] = None,
        order_by: ListVPCsRequestOrderBy = ListVPCsRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        is_default: Optional[bool] = None,
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
        :return: :class:`List[ListVPCsResponse] <List[ListVPCsResponse]>`

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
            },
        )

    async def create_vpc(
        self,
        *,
        default_private_network_name: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> VPC:
        """
        Create a VPC.
        Create a new VPC in the specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name for the VPC.
        :param default_private_network_name: Name for the VPC's associated default Private Network.
        :param project_id: Scaleway Project in which to create the VPC.
        :param tags: Tags for the VPC.
        :return: :class:`VPC <VPC>`

        Usage:
        ::

            result = await api.create_vpc(default_private_network_name="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/vpc/v2/regions/{param_region}/vpcs",
            body=marshal_CreateVPCRequest(
                CreateVPCRequest(
                    default_private_network_name=default_private_network_name,
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
        :param region: Region to target. If none is passed will use default region from the config.
        :param vpc_id: VPC ID.
        :return: :class:`VPC <VPC>`

        Usage:
        ::

            result = await api.get_vpc(vpc_id="example")
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
        :param region: Region to target. If none is passed will use default region from the config.
        :param vpc_id: VPC ID.
        :param name: Name for the VPC.
        :param tags: Tags for the VPC.
        :return: :class:`VPC <VPC>`

        Usage:
        ::

            result = await api.update_vpc(vpc_id="example")
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
    ) -> Optional[None]:
        """
        Delete a VPC.
        Delete a VPC specified by its VPC ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param vpc_id: VPC ID.

        Usage:
        ::

            result = await api.delete_vpc(vpc_id="example")
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
        return None

    async def list_private_networks(
        self,
        *,
        region: Optional[Region] = None,
        order_by: ListPrivateNetworksRequestOrderBy = ListPrivateNetworksRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        private_network_ids: Optional[List[str]] = None,
        vpc_id: Optional[str] = None,
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
        :return: :class:`List[ListPrivateNetworksResponse] <List[ListPrivateNetworksResponse]>`

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
        :param region: Region to target. If none is passed will use default region from the config.
        :param private_network_id: Private Network ID.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = await api.get_private_network(private_network_id="example")
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
        :param region: Region to target. If none is passed will use default region from the config.
        :param private_network_id: Private Network ID.
        :param name: Name for the Private Network.
        :param tags: Tags for the Private Network.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = await api.update_private_network(private_network_id="example")
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
    ) -> Optional[None]:
        """
        Delete a Private Network.
        Delete an existing Private Network. Note that you must first detach all resources from the network, in order to delete it.
        :param region: Region to target. If none is passed will use default region from the config.
        :param private_network_id: Private Network ID.

        Usage:
        ::

            result = await api.delete_private_network(private_network_id="example")
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
        return None

    async def migrate_zonal_private_networks(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        private_network_ids: Optional[List[str]] = None,
    ) -> Optional[None]:
        """
        Migrate Private Networks from zoned to regional.
        Transform multiple existing zoned Private Networks (scoped to a single Availability Zone) into regional Private Networks, scoped to an entire region. You can transform one or many Private Networks (specified by their Private Network IDs) within a single Scaleway Organization or Project, with the same call.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Organization ID to target. The specified zoned Private Networks within this Organization will be migrated to regional.

        One-of ('scope'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Project to target. The specified zoned Private Networks within this Project will be migrated to regional.

        One-of ('scope'): at most one of 'organization_id', 'project_id' could be set.
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
                    organization_id=organization_id,
                    project_id=project_id,
                    private_network_ids=private_network_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return None

    async def set_subnets(
        self,
        *,
        private_network_id: str,
        region: Optional[Region] = None,
        subnets: Optional[List[str]] = None,
    ) -> SetSubnetsResponse:
        """
        Set the subnets of a Private Network.
        Set subnets for an existing Private Network. Note that the method is PUT and not PATCH. Any existing subnets will be removed in favor of the new specified set of subnets.
        :param region: Region to target. If none is passed will use default region from the config.
        :param private_network_id: Private Network ID.
        :param subnets: Private Network subnets CIDR.
        :return: :class:`SetSubnetsResponse <SetSubnetsResponse>`

        Usage:
        ::

            result = await api.set_subnets(private_network_id="example")
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
        :param region: Region to target. If none is passed will use default region from the config.
        :param private_network_id: Private Network ID.
        :param subnets: Private Network subnets CIDR.
        :return: :class:`AddSubnetsResponse <AddSubnetsResponse>`

        Usage:
        ::

            result = await api.add_subnets(private_network_id="example")
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
        :param region: Region to target. If none is passed will use default region from the config.
        :param private_network_id: Private Network ID.
        :param subnets: Private Network subnets CIDR.
        :return: :class:`DeleteSubnetsResponse <DeleteSubnetsResponse>`

        Usage:
        ::

            result = await api.delete_subnets(private_network_id="example")
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
