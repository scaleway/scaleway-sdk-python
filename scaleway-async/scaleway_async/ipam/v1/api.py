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
    fetch_all_pages_async,
)
from .types import (
    ListIPsRequestOrderBy,
    ResourceType,
    AttachIPRequest,
    BookIPRequest,
    CustomResource,
    DetachIPRequest,
    IP,
    ListIPsResponse,
    MoveIPRequest,
    ReleaseIPSetRequest,
    Reverse,
    Source,
    UpdateIPRequest,
)
from .marshalling import (
    unmarshal_IP,
    unmarshal_ListIPsResponse,
    marshal_AttachIPRequest,
    marshal_BookIPRequest,
    marshal_DetachIPRequest,
    marshal_MoveIPRequest,
    marshal_ReleaseIPSetRequest,
    marshal_UpdateIPRequest,
)


class IpamV1API(API):
    """
    This API allows you to manage your Scaleway IP addresses with our IP Address Management tool.
    """

    async def book_ip(
        self,
        *,
        source: Source,
        is_ipv6: bool,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        address: Optional[str] = None,
        tags: Optional[List[str]] = None,
        resource: Optional[CustomResource] = None,
    ) -> IP:
        """
        Reserve a new IP.
        Reserve a new IP from the specified source. Currently IPs can only be reserved from a Private Network.
        :param source: Source in which to reserve the IP. Not all sources are available for reservation.
        :param is_ipv6: Request an IPv6 instead of an IPv4.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: When creating an IP in a Private Network, the Project must match the Private Network's Project.
        :param address: The requested address should not include the subnet mask (/suffix). Note that only the Private Network source allows you to pick a specific IP. If the requested IP is already reserved, then the call will fail.
        :param tags: Tags for the IP.
        :param resource: Custom resource to attach to the IP being reserved. An example of a custom resource is a virtual machine hosted on an Elastic Metal server. Do not use this for attaching IP addresses to standard Scaleway resources, as it will fail - instead, see the relevant product API for an equivalent method.
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = await api.book_ip(
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
                    resource=resource,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    async def release_ip(
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

            result = await api.release_ip(
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

    async def release_ip_set(
        self,
        *,
        region: Optional[Region] = None,
        ip_ids: Optional[List[str]] = None,
    ) -> None:
        """
        :param region: Region to target. If none is passed will use default region from the config.
        :param ip_ids:

        Usage:
        ::

            result = await api.release_ip_set()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/ipam/v1/regions/{param_region}/ip-sets/release",
            body=marshal_ReleaseIPSetRequest(
                ReleaseIPSetRequest(
                    region=region,
                    ip_ids=ip_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def get_ip(
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

            result = await api.get_ip(
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

    async def update_ip(
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

            result = await api.update_ip(
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

    async def list_i_ps(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListIPsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        zonal: Optional[str] = None,
        private_network_id: Optional[str] = None,
        subnet_id: Optional[str] = None,
        vpc_id: Optional[str] = None,
        attached: Optional[bool] = None,
        resource_id: Optional[str] = None,
        resource_type: Optional[ResourceType] = None,
        mac_address: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        is_ipv6: Optional[bool] = None,
        resource_name: Optional[str] = None,
        resource_types: Optional[List[ResourceType]] = None,
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
        One-Of ('source'): at most one of 'zonal', 'private_network_id', 'subnet_id' could be set.
        :param private_network_id: Only IPs that are private, and in this Private Network, will be returned.
        One-Of ('source'): at most one of 'zonal', 'private_network_id', 'subnet_id' could be set.
        :param subnet_id: Only IPs inside this exact subnet will be returned.
        One-Of ('source'): at most one of 'zonal', 'private_network_id', 'subnet_id' could be set.
        :param vpc_id: Only IPs owned by resources in this VPC will be returned.
        :param attached: Defines whether to filter only for IPs which are attached to a resource.
        :param resource_id: Resource ID to filter for. Only IPs attached to this resource will be returned.
        :param resource_type: Resource type to filter for. Only IPs attached to this type of resource will be returned.
        :param mac_address: MAC address to filter for. Only IPs attached to a resource with this MAC address will be returned.
        :param tags: Tags to filter for, only IPs with one or more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only IPs belonging to this Organization will be returned.
        :param is_ipv6: Defines whether to filter only for IPv4s or IPv6s.
        :param resource_name: Attached resource name to filter for, only IPs attached to a resource with this string within their name will be returned.
        :param resource_types: Resource types to filter for. Only IPs attached to these types of resources will be returned.
        :return: :class:`ListIPsResponse <ListIPsResponse>`

        Usage:
        ::

            result = await api.list_i_ps()
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
                "resource_types": resource_types,
                "tags": tags,
                "vpc_id": vpc_id,
                **resolve_one_of(
                    [
                        OneOfPossibility("private_network_id", private_network_id),
                        OneOfPossibility("subnet_id", subnet_id),
                        OneOfPossibility("zonal", zonal),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListIPsResponse(res.json())

    async def list_i_ps_all(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListIPsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        zonal: Optional[str] = None,
        private_network_id: Optional[str] = None,
        subnet_id: Optional[str] = None,
        vpc_id: Optional[str] = None,
        attached: Optional[bool] = None,
        resource_id: Optional[str] = None,
        resource_type: Optional[ResourceType] = None,
        mac_address: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        is_ipv6: Optional[bool] = None,
        resource_name: Optional[str] = None,
        resource_types: Optional[List[ResourceType]] = None,
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
        One-Of ('source'): at most one of 'zonal', 'private_network_id', 'subnet_id' could be set.
        :param private_network_id: Only IPs that are private, and in this Private Network, will be returned.
        One-Of ('source'): at most one of 'zonal', 'private_network_id', 'subnet_id' could be set.
        :param subnet_id: Only IPs inside this exact subnet will be returned.
        One-Of ('source'): at most one of 'zonal', 'private_network_id', 'subnet_id' could be set.
        :param vpc_id: Only IPs owned by resources in this VPC will be returned.
        :param attached: Defines whether to filter only for IPs which are attached to a resource.
        :param resource_id: Resource ID to filter for. Only IPs attached to this resource will be returned.
        :param resource_type: Resource type to filter for. Only IPs attached to this type of resource will be returned.
        :param mac_address: MAC address to filter for. Only IPs attached to a resource with this MAC address will be returned.
        :param tags: Tags to filter for, only IPs with one or more matching tags will be returned.
        :param organization_id: Organization ID to filter for. Only IPs belonging to this Organization will be returned.
        :param is_ipv6: Defines whether to filter only for IPv4s or IPv6s.
        :param resource_name: Attached resource name to filter for, only IPs attached to a resource with this string within their name will be returned.
        :param resource_types: Resource types to filter for. Only IPs attached to these types of resources will be returned.
        :return: :class:`List[IP] <List[IP]>`

        Usage:
        ::

            result = await api.list_i_ps_all()
        """

        return await fetch_all_pages_async(
            type=ListIPsResponse,
            key="ips",
            fetcher=self.list_i_ps,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
                "vpc_id": vpc_id,
                "attached": attached,
                "resource_id": resource_id,
                "resource_type": resource_type,
                "mac_address": mac_address,
                "tags": tags,
                "organization_id": organization_id,
                "is_ipv6": is_ipv6,
                "resource_name": resource_name,
                "resource_types": resource_types,
                "zonal": zonal,
                "private_network_id": private_network_id,
                "subnet_id": subnet_id,
            },
        )

    async def attach_ip(
        self,
        *,
        ip_id: str,
        resource: CustomResource,
        region: Optional[Region] = None,
    ) -> IP:
        """
        Attach IP to custom resource.
        Attach an existing reserved IP from a Private Network subnet to a custom, named resource via its MAC address. An example of a custom resource is a virtual machine hosted on an Elastic Metal server. Do not use this method for attaching IP addresses to standard Scaleway resources as it will fail - see the relevant product API for an equivalent method.
        :param ip_id: IP ID.
        :param resource: Custom resource to be attached to the IP.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = await api.attach_ip(
                ip_id="example",
                resource=CustomResource(),
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "POST",
            f"/ipam/v1/regions/{param_region}/ips/{param_ip_id}/attach",
            body=marshal_AttachIPRequest(
                AttachIPRequest(
                    ip_id=ip_id,
                    resource=resource,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    async def detach_ip(
        self,
        *,
        ip_id: str,
        resource: CustomResource,
        region: Optional[Region] = None,
    ) -> IP:
        """
        Detach IP from a custom resource.
        Detach a private IP from a custom resource. An example of a custom resource is a virtual machine hosted on an Elastic Metal server. Do not use this method for detaching IP addresses from standard Scaleway resources (e.g. Instances, Load Balancers) as it will fail - see the relevant product API for an equivalent method.
        :param ip_id: IP ID.
        :param resource: Custom resource currently attached to the IP.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = await api.detach_ip(
                ip_id="example",
                resource=CustomResource(),
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "POST",
            f"/ipam/v1/regions/{param_region}/ips/{param_ip_id}/detach",
            body=marshal_DetachIPRequest(
                DetachIPRequest(
                    ip_id=ip_id,
                    resource=resource,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    async def move_ip(
        self,
        *,
        ip_id: str,
        from_resource: CustomResource,
        region: Optional[Region] = None,
        to_resource: Optional[CustomResource] = None,
    ) -> IP:
        """
        Move IP to a custom resource.
        Move an existing reserved private IP from one custom resource (e.g. a virtual machine hosted on an Elastic Metal server) to another custom resource. This will detach it from the first resource, and attach it to the second. Do not use this method for moving IP addresses between standard Scaleway resources (e.g. Instances, Load Balancers) as it will fail - see the relevant product API for an equivalent method.
        :param ip_id: IP ID.
        :param from_resource: Custom resource currently attached to the IP.
        :param region: Region to target. If none is passed will use default region from the config.
        :param to_resource: Custom resource to be attached to the IP.
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = await api.move_ip(
                ip_id="example",
                from_resource=CustomResource(),
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "POST",
            f"/ipam/v1/regions/{param_region}/ips/{param_ip_id}/move",
            body=marshal_MoveIPRequest(
                MoveIPRequest(
                    ip_id=ip_id,
                    from_resource=from_resource,
                    region=region,
                    to_resource=to_resource,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())
