# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    random_name,
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    ListPrivateNetworksRequestOrderBy,
    CreatePrivateNetworkRequest,
    ListPrivateNetworksResponse,
    PrivateNetwork,
    UpdatePrivateNetworkRequest,
)
from .marshalling import (
    unmarshal_PrivateNetwork,
    unmarshal_ListPrivateNetworksResponse,
    marshal_CreatePrivateNetworkRequest,
    marshal_UpdatePrivateNetworkRequest,
)


class VpcV1API(API):
    """
    This API allows you to manage your Virtual Private Clouds (VPCs) and Private Networks.
    """

    async def list_private_networks(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListPrivateNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        private_network_ids: Optional[List[str]] = None,
        include_regional: Optional[bool] = None,
    ) -> ListPrivateNetworksResponse:
        """
        List Private Networks.
        List existing Private Networks in a specified Availability Zone. By default, the Private Networks returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of the returned Private Networks.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of Private Networks to return per page.
        :param name: Name to filter for. Only Private Networks with names containing this string will be returned.
        :param tags: Tags to filter for. Only Private Networks with one or more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only Private Networks belonging to this Organization will be returned.
        :param project_id: Project ID to filter for. Only Private Networks belonging to this Project will be returned.
        :param private_network_ids: Private Network IDs to filter for. Only Private Networks with one of these IDs will be returned.
        :param include_regional: Defines whether to include regional Private Networks in the response.
        :return: :class:`ListPrivateNetworksResponse <ListPrivateNetworksResponse>`

        Usage:
        ::

            result = await api.list_private_networks()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/vpc/v1/zones/{param_zone}/private-networks",
            params={
                "include_regional": include_regional,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "private_network_ids": private_network_ids,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPrivateNetworksResponse(res.json())

    async def list_private_networks_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListPrivateNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        private_network_ids: Optional[List[str]] = None,
        include_regional: Optional[bool] = None,
    ) -> List[PrivateNetwork]:
        """
        List Private Networks.
        List existing Private Networks in a specified Availability Zone. By default, the Private Networks returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of the returned Private Networks.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of Private Networks to return per page.
        :param name: Name to filter for. Only Private Networks with names containing this string will be returned.
        :param tags: Tags to filter for. Only Private Networks with one or more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only Private Networks belonging to this Organization will be returned.
        :param project_id: Project ID to filter for. Only Private Networks belonging to this Project will be returned.
        :param private_network_ids: Private Network IDs to filter for. Only Private Networks with one of these IDs will be returned.
        :param include_regional: Defines whether to include regional Private Networks in the response.
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
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
                "tags": tags,
                "organization_id": organization_id,
                "project_id": project_id,
                "private_network_ids": private_network_ids,
                "include_regional": include_regional,
            },
        )

    async def create_private_network(
        self,
        *,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        subnets: Optional[List[str]] = None,
    ) -> PrivateNetwork:
        """
        Create a Private Network.
        Create a new Private Network. Once created, you can attach Scaleway resources in the same Availability Zone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name for the Private Network.
        :param project_id: Scaleway Project in which to create the Private Network.
        :param tags: Tags for the Private Network.
        :param subnets: Private Network subnets CIDR.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = await api.create_private_network()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/vpc/v1/zones/{param_zone}/private-networks",
            body=marshal_CreatePrivateNetworkRequest(
                CreatePrivateNetworkRequest(
                    zone=zone,
                    name=name or random_name(prefix="pn"),
                    project_id=project_id,
                    tags=tags,
                    subnets=subnets,
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
        zone: Optional[Zone] = None,
    ) -> PrivateNetwork:
        """
        Get a Private Network.
        Retrieve information about an existing Private Network, specified by its Private Network ID. Its full details are returned in the response object.
        :param private_network_id: Private Network ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = await api.get_private_network(
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "GET",
            f"/vpc/v1/zones/{param_zone}/private-networks/{param_private_network_id}",
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNetwork(res.json())

    async def update_private_network(
        self,
        *,
        private_network_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        subnets: Optional[List[str]] = None,
    ) -> PrivateNetwork:
        """
        Update Private Network.
        Update parameters (such as name or tags) of an existing Private Network, specified by its Private Network ID.
        :param private_network_id: Private Network ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the private network.
        :param tags: Tags for the Private Network.
        :param subnets: Private Network subnets CIDR (deprecated).
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = await api.update_private_network(
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "PATCH",
            f"/vpc/v1/zones/{param_zone}/private-networks/{param_private_network_id}",
            body=marshal_UpdatePrivateNetworkRequest(
                UpdatePrivateNetworkRequest(
                    private_network_id=private_network_id,
                    zone=zone,
                    name=name,
                    tags=tags,
                    subnets=subnets,
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
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a Private Network.
        Delete an existing Private Network. Note that you must first detach all resources from the network, in order to delete it.
        :param private_network_id: Private Network ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_private_network(
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "DELETE",
            f"/vpc/v1/zones/{param_zone}/private-networks/{param_private_network_id}",
        )

        self._throw_on_error(res)
