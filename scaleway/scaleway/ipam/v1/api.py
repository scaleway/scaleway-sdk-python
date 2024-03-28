# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
    validate_path_param,
    fetch_all_pages,
)
from .types import (
    ListIPsRequestOrderBy,
    ResourceType,
    BookIPRequest,
    IP,
    ListIPsResponse,
    Reverse,
    Source,
    UpdateIPRequest,
)
from .marshalling import (
    unmarshal_IP,
    unmarshal_ListIPsResponse,
    marshal_BookIPRequest,
    marshal_UpdateIPRequest,
)


class IpamV1API(API):
    """
    This API allows you to manage IP addresses with Scaleway's IP Address Management tool.
    """

    def book_ip(
        self,
        *,
        source: Source,
        is_ipv6: bool,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        address: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> IP:
        """
        Book a new IP.
        Book a new IP from the specified source. Currently IPs can only be booked from a Private Network.
        :param source: Source in which to book the IP. Not all sources are available for booking.
        :param is_ipv6: Request an IPv6 instead of an IPv4.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: When creating an IP in a Private Network, the Project must match the Private Network's Project.
        :param address: Note that only the Private Network source allows you to pick a specific IP. If the requested IP is already booked, then the call will fail.
        :param tags: Tags for the IP.
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = api.book_ip(
                source=Source(),
                is_ipv6=False,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/ipam/v1/regions/{param_region}/ips",
            body=marshal_BookIPRequest(
                BookIPRequest(
                    source=source,
                    is_ipv6=is_ipv6,
                    region=region,
                    project_id=project_id,
                    address=address,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    def release_ip(
        self,
        *,
        ip_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Release an IP.
        Release an IP not currently attached to a resource, and returns it to the available IP pool.
        :param ip_id: IP ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.release_ip(
                ip_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "DELETE",
            f"/ipam/v1/regions/{param_region}/ips/{param_ip_id}",
            body={},
        )

        self._throw_on_error(res)

    def get_ip(
        self,
        *,
        ip_id: str,
        region: Optional[Region] = None,
    ) -> IP:
        """
        Get an IP.
        Retrieve details of an existing IP, specified by its IP ID.
        :param ip_id: IP ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = api.get_ip(
                ip_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "GET",
            f"/ipam/v1/regions/{param_region}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    def update_ip(
        self,
        *,
        ip_id: str,
        region: Optional[Region] = None,
        tags: Optional[List[str]] = None,
        reverses: Optional[List[Reverse]] = None,
    ) -> IP:
        """
        Update an IP.
        Update parameters including tags of the specified IP.
        :param ip_id: IP ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tags: Tags for the IP.
        :param reverses: Array of reverse domain names associated with an IP in the subnet of the current IP.
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = api.update_ip(
                ip_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "PATCH",
            f"/ipam/v1/regions/{param_region}/ips/{param_ip_id}",
            body=marshal_UpdateIPRequest(
                UpdateIPRequest(
                    ip_id=ip_id,
                    region=region,
                    tags=tags,
                    reverses=reverses,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    def list_i_ps(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListIPsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        zonal: Optional[str] = None,
        private_network_id: Optional[str] = None,
        attached: Optional[bool] = None,
        resource_id: Optional[str] = None,
        resource_type: Optional[ResourceType] = None,
        mac_address: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        is_ipv6: Optional[bool] = None,
        resource_name: Optional[str] = None,
    ) -> ListIPsResponse:
        """
        List existing IPs.
        List existing IPs in the specified region using various filters. For example, you can filter for IPs within a specified Private Network, or for public IPs within a specified Project. By default, the IPs returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned IPs.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of IPs to return per page.
        :param project_id: Project ID to filter for. Only IPs belonging to this Project will be returned.
        :param zonal: Zone to filter for. Only IPs that are zonal, and in this zone, will be returned.
        One-Of ('source'): at most one of 'zonal', 'private_network_id' could be set.
        :param private_network_id: Only IPs that are private, and in this Private Network, will be returned.
        One-Of ('source'): at most one of 'zonal', 'private_network_id' could be set.
        :param attached: Defines whether to filter only for IPs which are attached to a resource.
        :param resource_id: Resource ID to filter for. Only IPs attached to this resource will be returned.
        :param resource_type: Resource type to filter for. Only IPs attached to this type of resource will be returned.
        :param mac_address: MAC address to filter for. Only IPs attached to a resource with this MAC address will be returned.
        :param tags: Tags to filter for, only IPs with one or more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only IPs belonging to this Organization will be returned.
        :param is_ipv6: Defines whether to filter only for IPv4s or IPv6s.
        :param resource_name: Attached resource name to filter for, only IPs attached to a resource with this string within their name will be returned.
        :return: :class:`ListIPsResponse <ListIPsResponse>`

        Usage:
        ::

            result = api.list_i_ps()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/ipam/v1/regions/{param_region}/ips",
            params={
                "attached": attached,
                "is_ipv6": is_ipv6,
                "mac_address": mac_address,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "resource_id": resource_id,
                "resource_name": resource_name,
                "resource_type": resource_type,
                "tags": tags,
                **resolve_one_of(
                    [
                        OneOfPossibility("private_network_id", private_network_id),
                        OneOfPossibility("zonal", zonal),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListIPsResponse(res.json())

    def list_i_ps_all(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListIPsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        zonal: Optional[str] = None,
        private_network_id: Optional[str] = None,
        attached: Optional[bool] = None,
        resource_id: Optional[str] = None,
        resource_type: Optional[ResourceType] = None,
        mac_address: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        is_ipv6: Optional[bool] = None,
        resource_name: Optional[str] = None,
    ) -> List[IP]:
        """
        List existing IPs.
        List existing IPs in the specified region using various filters. For example, you can filter for IPs within a specified Private Network, or for public IPs within a specified Project. By default, the IPs returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of the returned IPs.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of IPs to return per page.
        :param project_id: Project ID to filter for. Only IPs belonging to this Project will be returned.
        :param zonal: Zone to filter for. Only IPs that are zonal, and in this zone, will be returned.
        One-Of ('source'): at most one of 'zonal', 'private_network_id' could be set.
        :param private_network_id: Only IPs that are private, and in this Private Network, will be returned.
        One-Of ('source'): at most one of 'zonal', 'private_network_id' could be set.
        :param attached: Defines whether to filter only for IPs which are attached to a resource.
        :param resource_id: Resource ID to filter for. Only IPs attached to this resource will be returned.
        :param resource_type: Resource type to filter for. Only IPs attached to this type of resource will be returned.
        :param mac_address: MAC address to filter for. Only IPs attached to a resource with this MAC address will be returned.
        :param tags: Tags to filter for, only IPs with one or more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only IPs belonging to this Organization will be returned.
        :param is_ipv6: Defines whether to filter only for IPv4s or IPv6s.
        :param resource_name: Attached resource name to filter for, only IPs attached to a resource with this string within their name will be returned.
        :return: :class:`List[IP] <List[IP]>`

        Usage:
        ::

            result = api.list_i_ps_all()
        """

        return fetch_all_pages(
            type=ListIPsResponse,
            key="ips",
            fetcher=self.list_i_ps,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
                "attached": attached,
                "resource_id": resource_id,
                "resource_type": resource_type,
                "mac_address": mac_address,
                "tags": tags,
                "organization_id": organization_id,
                "is_ipv6": is_ipv6,
                "resource_name": resource_name,
                "zonal": zonal,
                "private_network_id": private_network_id,
            },
        )
