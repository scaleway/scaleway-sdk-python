# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages_async,
    validate_path_param,
    wait_for_resource_async,
)
from .types import (
    FlexibleIPStatus,
    ListFlexibleIPsRequestOrderBy,
    MACAddressType,
    AttachFlexibleIPsResponse,
    DetachFlexibleIPsResponse,
    FlexibleIP,
    ListFlexibleIPsResponse,
    CreateFlexibleIPRequest,
    UpdateFlexibleIPRequest,
    AttachFlexibleIPRequest,
    DetachFlexibleIPRequest,
    GenerateMACAddrRequest,
    DuplicateMACAddrRequest,
    MoveMACAddrRequest,
)
from .content import (
    FLEXIBLE_IP_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_AttachFlexibleIPRequest,
    marshal_CreateFlexibleIPRequest,
    marshal_DetachFlexibleIPRequest,
    marshal_DuplicateMACAddrRequest,
    marshal_GenerateMACAddrRequest,
    marshal_MoveMACAddrRequest,
    marshal_UpdateFlexibleIPRequest,
    unmarshal_FlexibleIP,
    unmarshal_AttachFlexibleIPsResponse,
    unmarshal_DetachFlexibleIPsResponse,
    unmarshal_ListFlexibleIPsResponse,
)


class FlexibleipV1Alpha1API(API):
    """
    Flexible IP API.
    """

    async def create_flexible_ip(
        self,
        *,
        description: str,
        is_ipv6: bool,
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        server_id: Optional[str] = None,
        reverse: Optional[str] = None,
    ) -> FlexibleIP:
        """
        Create a Flexible IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param project_id: ID of the project to associate with the Flexible IP
        :param description: Description to associate with the Flexible IP, max 255 characters
        :param tags: Tags to associate to the Flexible IP
        :param server_id: Server ID on which to attach the created Flexible IP
        :param reverse: Reverse DNS value
        :param is_ipv6: If true, creates a Flexible IP with an ipv6 address
        :return: :class:`FlexibleIP <FlexibleIP>`

        Usage:
        ::

            result = await api.create_flexible_ip(
                description="example",
                is_ipv6=True,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips",
            body=marshal_CreateFlexibleIPRequest(
                CreateFlexibleIPRequest(
                    description=description,
                    is_ipv6=is_ipv6,
                    zone=zone,
                    project_id=project_id,
                    tags=tags,
                    server_id=server_id,
                    reverse=reverse,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_FlexibleIP(res.json())

    async def get_flexible_ip(
        self,
        *,
        fip_id: str,
        zone: Optional[Zone] = None,
    ) -> FlexibleIP:
        """
        Get a Flexible IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param fip_id: Flexible IP ID
        :return: :class:`FlexibleIP <FlexibleIP>`

        Usage:
        ::

            result = await api.get_flexible_ip(fip_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_fip_id = validate_path_param("fip_id", fip_id)

        res = self._request(
            "GET",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips/{param_fip_id}",
        )

        self._throw_on_error(res)
        return unmarshal_FlexibleIP(res.json())

    async def wait_for_flexible_ip(
        self,
        *,
        fip_id: str,
        zone: Optional[Zone] = None,
        options: Optional[
            WaitForOptions[FlexibleIP, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> FlexibleIP:
        """
        Waits for :class:`FlexibleIP <FlexibleIP>` to be in a final state.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param fip_id: Flexible IP ID
        :param options: The options for the waiter
        :return: :class:`FlexibleIP <FlexibleIP>`

        Usage:
        ::

            result = api.wait_for_flexible_ip(fip_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in FLEXIBLE_IP_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_flexible_ip,
            options=options,
            args={
                "fip_id": fip_id,
                "zone": zone,
            },
        )

    async def list_flexible_i_ps(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: ListFlexibleIPsRequestOrderBy = ListFlexibleIPsRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[List[str]] = None,
        status: Optional[List[FlexibleIPStatus]] = None,
        server_ids: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListFlexibleIPsResponse:
        """
        List Flexible IPs
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: The sort order of the returned Flexible IPs
        :param page: The page number for the returned Flexible IPs
        :param page_size: The maximum number of Flexible IPs per page
        :param tags: Filter Flexible IPs with one or more matching tags
        :param status: Filter Flexible IPs by status
        :param server_ids: Filter Flexible IPs by server IDs
        :param organization_id: Filter Flexible IPs by organization ID
        :param project_id: Filter Flexible IPs by project ID
        :return: :class:`ListFlexibleIPsResponse <ListFlexibleIPsResponse>`

        Usage:
        ::

            result = await api.list_flexible_i_ps()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "server_ids": server_ids,
                "status": status,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListFlexibleIPsResponse(res.json())

    async def list_flexible_i_ps_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListFlexibleIPsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[List[str]] = None,
        status: Optional[List[FlexibleIPStatus]] = None,
        server_ids: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[FlexibleIP]:
        """
        List Flexible IPs
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: The sort order of the returned Flexible IPs
        :param page: The page number for the returned Flexible IPs
        :param page_size: The maximum number of Flexible IPs per page
        :param tags: Filter Flexible IPs with one or more matching tags
        :param status: Filter Flexible IPs by status
        :param server_ids: Filter Flexible IPs by server IDs
        :param organization_id: Filter Flexible IPs by organization ID
        :param project_id: Filter Flexible IPs by project ID
        :return: :class:`List[ListFlexibleIPsResponse] <List[ListFlexibleIPsResponse]>`

        Usage:
        ::

            result = await api.list_flexible_i_ps_all()
        """

        return await fetch_all_pages_async(
            type=ListFlexibleIPsResponse,
            key="flexible_ips",
            fetcher=self.list_flexible_i_ps,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "tags": tags,
                "status": status,
                "server_ids": server_ids,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    async def update_flexible_ip(
        self,
        *,
        fip_id: str,
        zone: Optional[Zone] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        reverse: Optional[str] = None,
    ) -> FlexibleIP:
        """
        Update a Flexible IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param fip_id: ID of the Flexible IP to update
        :param description: Description to associate with the Flexible IP, max 255 characters
        :param tags: Tags to associate with the Flexible IP
        :param reverse: Reverse DNS value
        :return: :class:`FlexibleIP <FlexibleIP>`

        Usage:
        ::

            result = await api.update_flexible_ip(fip_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_fip_id = validate_path_param("fip_id", fip_id)

        res = self._request(
            "PATCH",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips/{param_fip_id}",
            body=marshal_UpdateFlexibleIPRequest(
                UpdateFlexibleIPRequest(
                    fip_id=fip_id,
                    zone=zone,
                    description=description,
                    tags=tags,
                    reverse=reverse,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_FlexibleIP(res.json())

    async def delete_flexible_ip(
        self,
        *,
        fip_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a Flexible IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param fip_id: ID of the Flexible IP to delete

        Usage:
        ::

            result = await api.delete_flexible_ip(fip_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_fip_id = validate_path_param("fip_id", fip_id)

        res = self._request(
            "DELETE",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips/{param_fip_id}",
        )

        self._throw_on_error(res)
        return None

    async def attach_flexible_ip(
        self,
        *,
        fips_ids: List[str],
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> AttachFlexibleIPsResponse:
        """
        Attach a Flexible IP to a server
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param fips_ids: Multiple IDs can be provided as long as Flexible IPs belong to the same MAC groups (see details about MAC groups).
        :param server_id: A server ID on which to attach the Flexible IPs
        :return: :class:`AttachFlexibleIPsResponse <AttachFlexibleIPsResponse>`

        Usage:
        ::

            result = await api.attach_flexible_ip(
                fips_ids=["example"],
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips/attach",
            body=marshal_AttachFlexibleIPRequest(
                AttachFlexibleIPRequest(
                    fips_ids=fips_ids,
                    server_id=server_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AttachFlexibleIPsResponse(res.json())

    async def detach_flexible_ip(
        self,
        *,
        fips_ids: List[str],
        zone: Optional[Zone] = None,
    ) -> DetachFlexibleIPsResponse:
        """
        Detach a Flexible IP from a server
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param fips_ids: Multiple IDs can be provided as long as Flexible IPs belong to the same MAC groups (see details about MAC groups).
        :return: :class:`DetachFlexibleIPsResponse <DetachFlexibleIPsResponse>`

        Usage:
        ::

            result = await api.detach_flexible_ip(fips_ids=["example"])
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips/detach",
            body=marshal_DetachFlexibleIPRequest(
                DetachFlexibleIPRequest(
                    fips_ids=fips_ids,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DetachFlexibleIPsResponse(res.json())

    async def generate_mac_addr(
        self,
        *,
        fip_id: str,
        zone: Optional[Zone] = None,
        mac_type: MACAddressType = MACAddressType.UNKNOWN_TYPE,
    ) -> FlexibleIP:
        """
        Generate a virtual MAC on a given Flexible IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param fip_id: Flexible IP ID on which to generate a Virtual MAC
        :param mac_type: TODO
        :return: :class:`FlexibleIP <FlexibleIP>`

        Usage:
        ::

            result = await api.generate_mac_addr(fip_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_fip_id = validate_path_param("fip_id", fip_id)

        res = self._request(
            "POST",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips/{param_fip_id}/mac",
            body=marshal_GenerateMACAddrRequest(
                GenerateMACAddrRequest(
                    fip_id=fip_id,
                    zone=zone,
                    mac_type=mac_type,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_FlexibleIP(res.json())

    async def duplicate_mac_addr(
        self,
        *,
        fip_id: str,
        duplicate_from_fip_id: str,
        zone: Optional[Zone] = None,
    ) -> FlexibleIP:
        """
        Duplicate a Virtual MAC from a given Flexible IP onto another attached on the same server.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param fip_id: Flexible IPs need to be attached to the same server.
        :param duplicate_from_fip_id: Flexible IPs need to be attached to the same server.
        :return: :class:`FlexibleIP <FlexibleIP>`

        Usage:
        ::

            result = await api.duplicate_mac_addr(
                fip_id="example",
                duplicate_from_fip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_fip_id = validate_path_param("fip_id", fip_id)

        res = self._request(
            "POST",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips/{param_fip_id}/mac/duplicate",
            body=marshal_DuplicateMACAddrRequest(
                DuplicateMACAddrRequest(
                    fip_id=fip_id,
                    duplicate_from_fip_id=duplicate_from_fip_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_FlexibleIP(res.json())

    async def move_mac_addr(
        self,
        *,
        fip_id: str,
        dst_fip_id: str,
        zone: Optional[Zone] = None,
    ) -> FlexibleIP:
        """

        Usage:
        ::

            result = await api.move_mac_addr(
                fip_id="example",
                dst_fip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_fip_id = validate_path_param("fip_id", fip_id)

        res = self._request(
            "POST",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips/{param_fip_id}/mac/move",
            body=marshal_MoveMACAddrRequest(
                MoveMACAddrRequest(
                    fip_id=fip_id,
                    dst_fip_id=dst_fip_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_FlexibleIP(res.json())

    async def delete_mac_addr(
        self,
        *,
        fip_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Remove a virtual MAC from a Flexible IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param fip_id: If the Flexible IP belongs to a MAC group, the MAC will be removed from the MAC group and from the Flexible IP.

        Usage:
        ::

            result = await api.delete_mac_addr(fip_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_fip_id = validate_path_param("fip_id", fip_id)

        res = self._request(
            "DELETE",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips/{param_fip_id}/mac",
        )

        self._throw_on_error(res)
        return None
