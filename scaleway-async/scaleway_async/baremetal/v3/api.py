# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone as ScwZone,
)
from scaleway_core.utils import (
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    ListServerPrivateNetworksRequestOrderBy,
    ListServerPrivateNetworksResponse,
    PrivateNetworkApiAddServerPrivateNetworkRequest,
    PrivateNetworkApiSetServerPrivateNetworksRequest,
    ServerPrivateNetwork,
    SetServerPrivateNetworksResponse,
)
from .marshalling import (
    unmarshal_ServerPrivateNetwork,
    unmarshal_ListServerPrivateNetworksResponse,
    unmarshal_SetServerPrivateNetworksResponse,
    marshal_PrivateNetworkApiAddServerPrivateNetworkRequest,
    marshal_PrivateNetworkApiSetServerPrivateNetworksRequest,
)


class BaremetalV3PrivateNetworkAPI(API):
    """
    Elastic Metal - Private Networks API.
    """

    async def add_server_private_network(
        self,
        *,
        server_id: str,
        private_network_id: str,
        zone: Optional[ScwZone] = None,
        ipam_ip_ids: Optional[list[str]] = None,
    ) -> ServerPrivateNetwork:
        """
        Add a server to a Private Network.
        Add an Elastic Metal server to a Private Network.
        :param server_id: UUID of the server.
        :param private_network_id: UUID of the Private Network.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param ipam_ip_ids: IPAM IDs of an IPs to attach to the server.
        :return: :class:`ServerPrivateNetwork <ServerPrivateNetwork>`

        Usage:
        ::

            result = await api.add_server_private_network(
                server_id="example",
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/baremetal/v3/zones/{param_zone}/servers/{param_server_id}/private-networks",
            body=marshal_PrivateNetworkApiAddServerPrivateNetworkRequest(
                PrivateNetworkApiAddServerPrivateNetworkRequest(
                    server_id=server_id,
                    private_network_id=private_network_id,
                    zone=zone,
                    ipam_ip_ids=ipam_ip_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ServerPrivateNetwork(res.json())

    async def set_server_private_networks(
        self,
        *,
        server_id: str,
        per_private_network_ipam_ip_ids: dict[str, list[str]],
        zone: Optional[ScwZone] = None,
    ) -> SetServerPrivateNetworksResponse:
        """
        Set multiple Private Networks on a server.
        Configure multiple Private Networks on an Elastic Metal server.
        :param server_id: UUID of the server.
        :param per_private_network_ipam_ip_ids: Object where the keys are the UUIDs of Private Networks and the values are arrays of IPAM IDs representing the IPs to assign to this Elastic Metal server on the Private Network. If the array supplied for a Private Network is empty, the next available IP from the Private Network's CIDR block will automatically be used for attachment.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`SetServerPrivateNetworksResponse <SetServerPrivateNetworksResponse>`

        Usage:
        ::

            result = await api.set_server_private_networks(
                server_id="example",
                per_private_network_ipam_ip_ids={},
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "PUT",
            f"/baremetal/v3/zones/{param_zone}/servers/{param_server_id}/private-networks",
            body=marshal_PrivateNetworkApiSetServerPrivateNetworksRequest(
                PrivateNetworkApiSetServerPrivateNetworksRequest(
                    server_id=server_id,
                    per_private_network_ipam_ip_ids=per_private_network_ipam_ip_ids,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetServerPrivateNetworksResponse(res.json())

    async def list_server_private_networks(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListServerPrivateNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        server_id: Optional[str] = None,
        private_network_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        ipam_ip_ids: Optional[list[str]] = None,
    ) -> ListServerPrivateNetworksResponse:
        """
        List the Private Networks of a server.
        List the Private Networks of an Elastic Metal server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order for the returned Private Networks.
        :param page: Page number for the returned Private Networks.
        :param page_size: Maximum number of Private Networks per page.
        :param server_id: Filter Private Networks by server UUID.
        :param private_network_id: Filter Private Networks by Private Network UUID.
        :param organization_id: Filter Private Networks by organization UUID.
        :param project_id: Filter Private Networks by project UUID.
        :param ipam_ip_ids: Filter Private Networks by IPAM IP UUIDs.
        :return: :class:`ListServerPrivateNetworksResponse <ListServerPrivateNetworksResponse>`

        Usage:
        ::

            result = await api.list_server_private_networks()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/baremetal/v3/zones/{param_zone}/server-private-networks",
            params={
                "ipam_ip_ids": ipam_ip_ids,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "private_network_id": private_network_id,
                "project_id": project_id or self.client.default_project_id,
                "server_id": server_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServerPrivateNetworksResponse(res.json())

    async def list_server_private_networks_all(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListServerPrivateNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        server_id: Optional[str] = None,
        private_network_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        ipam_ip_ids: Optional[list[str]] = None,
    ) -> list[ServerPrivateNetwork]:
        """
        List the Private Networks of a server.
        List the Private Networks of an Elastic Metal server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order for the returned Private Networks.
        :param page: Page number for the returned Private Networks.
        :param page_size: Maximum number of Private Networks per page.
        :param server_id: Filter Private Networks by server UUID.
        :param private_network_id: Filter Private Networks by Private Network UUID.
        :param organization_id: Filter Private Networks by organization UUID.
        :param project_id: Filter Private Networks by project UUID.
        :param ipam_ip_ids: Filter Private Networks by IPAM IP UUIDs.
        :return: :class:`list[ServerPrivateNetwork] <list[ServerPrivateNetwork]>`

        Usage:
        ::

            result = await api.list_server_private_networks_all()
        """

        return await fetch_all_pages_async(
            type=ListServerPrivateNetworksResponse,
            key="server_private_networks",
            fetcher=self.list_server_private_networks,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "server_id": server_id,
                "private_network_id": private_network_id,
                "organization_id": organization_id,
                "project_id": project_id,
                "ipam_ip_ids": ipam_ip_ids,
            },
        )

    async def delete_server_private_network(
        self,
        *,
        server_id: str,
        private_network_id: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete a Private Network.
        :param server_id: UUID of the server.
        :param private_network_id: UUID of the Private Network.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_server_private_network(
                server_id="example",
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "DELETE",
            f"/baremetal/v3/zones/{param_zone}/servers/{param_server_id}/private-networks/{param_private_network_id}",
        )

        self._throw_on_error(res)
