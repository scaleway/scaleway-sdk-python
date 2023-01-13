# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    fetch_all_pages,
    random_name,
    validate_path_param,
)
from .types import (
    ListPrivateNetworksRequestOrderBy,
    ListPrivateNetworksResponse,
    PrivateNetwork,
    CreatePrivateNetworkRequest,
    UpdatePrivateNetworkRequest,
)
from .marshalling import (
    marshal_CreatePrivateNetworkRequest,
    marshal_UpdatePrivateNetworkRequest,
    unmarshal_PrivateNetwork,
    unmarshal_ListPrivateNetworksResponse,
)


class VpcV1API(API):
    """
    VPC API.
    """

    def list_private_networks(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: ListPrivateNetworksRequestOrderBy = ListPrivateNetworksRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        private_network_ids: Optional[List[str]] = None,
    ) -> ListPrivateNetworksResponse:
        """
        List private networks
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: The sort order of the returned private networks
        :param page: The page number for the returned private networks
        :param page_size: The maximum number of private networks per page
        :param name: Filter private networks with names containing this string
        :param tags: Filter private networks with one or more matching tags
        :param organization_id: The organization ID on which to filter the returned private networks
        :param project_id: The project ID on which to filter the returned private networks
        :param private_network_ids: The PrivateNetwork IDs on which to filter the returned private networks
        :return: :class:`ListPrivateNetworksResponse <ListPrivateNetworksResponse>`

        Usage:
        ::

            result = api.list_private_networks()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/vpc/v1/zones/{param_zone}/private-networks",
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
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPrivateNetworksResponse(res.json())

    def list_private_networks_all(
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
    ) -> List[PrivateNetwork]:
        """
        List private networks
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: The sort order of the returned private networks
        :param page: The page number for the returned private networks
        :param page_size: The maximum number of private networks per page
        :param name: Filter private networks with names containing this string
        :param tags: Filter private networks with one or more matching tags
        :param organization_id: The organization ID on which to filter the returned private networks
        :param project_id: The project ID on which to filter the returned private networks
        :param private_network_ids: The PrivateNetwork IDs on which to filter the returned private networks
        :return: :class:`List[ListPrivateNetworksResponse] <List[ListPrivateNetworksResponse]>`

        Usage:
        ::

            result = api.list_private_networks_all()
        """

        return fetch_all_pages(
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
            },
        )

    def create_private_network(
        self,
        *,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        subnets: Optional[List[str]] = None,
    ) -> PrivateNetwork:
        """
        Create a private network
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param name: The name of the private network
        :param project_id: The project ID of the private network
        :param tags: The private networks tags
        :param subnets: Private network subnets CIDR
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = api.create_private_network()
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

    def get_private_network(
        self,
        *,
        private_network_id: str,
        zone: Optional[Zone] = None,
    ) -> PrivateNetwork:
        """
        Get a private network
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param private_network_id: The private network id
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = api.get_private_network(private_network_id="example")
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

    def update_private_network(
        self,
        *,
        private_network_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        subnets: Optional[List[str]] = None,
    ) -> PrivateNetwork:
        """
        Update private network
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param private_network_id: The private network ID
        :param name: The name of the private network
        :param tags: The private networks tags
        :param subnets: Private network subnets CIDR
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = api.update_private_network(private_network_id="example")
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

    def delete_private_network(
        self,
        *,
        private_network_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a private network
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param private_network_id: The private network ID

        Usage:
        ::

            result = api.delete_private_network(private_network_id="example")
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
        return None
