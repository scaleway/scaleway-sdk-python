# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    FlexibleIPStatus,
    ListFlexibleIPsRequestOrderBy,
    MACAddressType,
    AttachFlexibleIPRequest,
    AttachFlexibleIPsResponse,
    CreateFlexibleIPRequest,
    DetachFlexibleIPRequest,
    DetachFlexibleIPsResponse,
    DuplicateMACAddrRequest,
    FlexibleIP,
    GenerateMACAddrRequest,
    ListFlexibleIPsResponse,
    MoveMACAddrRequest,
    UpdateFlexibleIPRequest,
)
from .content import (
    FLEXIBLE_IP_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_FlexibleIP,
    unmarshal_AttachFlexibleIPsResponse,
    unmarshal_DetachFlexibleIPsResponse,
    unmarshal_ListFlexibleIPsResponse,
    marshal_AttachFlexibleIPRequest,
    marshal_CreateFlexibleIPRequest,
    marshal_DetachFlexibleIPRequest,
    marshal_DuplicateMACAddrRequest,
    marshal_GenerateMACAddrRequest,
    marshal_MoveMACAddrRequest,
    marshal_UpdateFlexibleIPRequest,
)


class FlexibleipV1Alpha1API(API):
    """
    This API allows you to manage your Elastic Metal servers' flexible public IP addresses.
    """

    def create_flexible_ip(
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
        Create a new flexible IP.
        Generate a new flexible IP within a given zone, specifying its configuration including Project ID and description.
        :param description: Flexible IP description (max. of 255 characters).
        :param is_ipv6: Defines whether the flexible IP has an IPv6 address.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: ID of the project to associate with the Flexible IP.
        :param tags: Tags to associate to the flexible IP.
        :param server_id: ID of the server to which the newly created flexible IP will be attached.
        :param reverse: Value of the reverse DNS.
        :return: :class:`FlexibleIP <FlexibleIP>`

        Usage:
        ::

            result = api.create_flexible_ip(
                description="example",
                is_ipv6=False,
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

    def get_flexible_ip(
        self,
        *,
        fip_id: str,
        zone: Optional[Zone] = None,
    ) -> FlexibleIP:
        """
        Get an existing flexible IP.
        Retrieve information about an existing flexible IP, specified by its ID and zone. Its full details, including Project ID, description and status, are returned in the response object.
        :param fip_id: ID of the flexible IP.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`FlexibleIP <FlexibleIP>`

        Usage:
        ::

            result = api.get_flexible_ip(
                fip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_fip_id = validate_path_param("fip_id", fip_id)

        res = self._request(
            "GET",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips/{param_fip_id}",
        )

        self._throw_on_error(res)
        return unmarshal_FlexibleIP(res.json())

    def wait_for_flexible_ip(
        self,
        *,
        fip_id: str,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[FlexibleIP, bool]] = None,
    ) -> FlexibleIP:
        """
        Get an existing flexible IP.
        Retrieve information about an existing flexible IP, specified by its ID and zone. Its full details, including Project ID, description and status, are returned in the response object.
        :param fip_id: ID of the flexible IP.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`FlexibleIP <FlexibleIP>`

        Usage:
        ::

            result = api.get_flexible_ip(
                fip_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in FLEXIBLE_IP_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_flexible_ip,
            options=options,
            args={
                "fip_id": fip_id,
                "zone": zone,
            },
        )

    def list_flexible_i_ps(
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
    ) -> ListFlexibleIPsResponse:
        """
        List flexible IPs.
        List all flexible IPs within a given zone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of the returned flexible IPs.
        :param page: Page number.
        :param page_size: Maximum number of flexible IPs per page.
        :param tags: Filter by tag, only flexible IPs with one or more matching tags will be returned.
        :param status: Filter by status, only flexible IPs with this status will be returned.
        :param server_ids: Filter by server IDs, only flexible IPs with these server IDs will be returned.
        :param organization_id: Filter by Organization ID, only flexible IPs from this Organization will be returned.
        :param project_id: Filter by Project ID, only flexible IPs from this Project will be returned.
        :return: :class:`ListFlexibleIPsResponse <ListFlexibleIPsResponse>`

        Usage:
        ::

            result = api.list_flexible_i_ps()
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

    def list_flexible_i_ps_all(
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
        List flexible IPs.
        List all flexible IPs within a given zone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of the returned flexible IPs.
        :param page: Page number.
        :param page_size: Maximum number of flexible IPs per page.
        :param tags: Filter by tag, only flexible IPs with one or more matching tags will be returned.
        :param status: Filter by status, only flexible IPs with this status will be returned.
        :param server_ids: Filter by server IDs, only flexible IPs with these server IDs will be returned.
        :param organization_id: Filter by Organization ID, only flexible IPs from this Organization will be returned.
        :param project_id: Filter by Project ID, only flexible IPs from this Project will be returned.
        :return: :class:`List[FlexibleIP] <List[FlexibleIP]>`

        Usage:
        ::

            result = api.list_flexible_i_ps_all()
        """

        return fetch_all_pages(
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

    def update_flexible_ip(
        self,
        *,
        fip_id: str,
        zone: Optional[Zone] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        reverse: Optional[str] = None,
    ) -> FlexibleIP:
        """
        Update an existing flexible IP.
        Update the parameters of an existing flexible IP, specified by its ID and zone. These parameters include tags and description.
        :param fip_id: ID of the flexible IP to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param description: Flexible IP description (max. 255 characters).
        :param tags: Tags associated with the flexible IP.
        :param reverse: Value of the reverse DNS.
        :return: :class:`FlexibleIP <FlexibleIP>`

        Usage:
        ::

            result = api.update_flexible_ip(
                fip_id="example",
            )
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

    def delete_flexible_ip(
        self,
        *,
        fip_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete an existing flexible IP.
        Delete an existing flexible IP, specified by its ID and zone. Note that deleting a flexible IP is permanent and cannot be undone.
        :param fip_id: ID of the flexible IP to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_flexible_ip(
                fip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_fip_id = validate_path_param("fip_id", fip_id)

        res = self._request(
            "DELETE",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips/{param_fip_id}",
        )

        self._throw_on_error(res)

    def attach_flexible_ip(
        self,
        *,
        fips_ids: List[str],
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> AttachFlexibleIPsResponse:
        """
        Attach an existing flexible IP to a server.
        Attach an existing flexible IP to a specified Elastic Metal server.
        :param fips_ids: Multiple IDs can be provided, but note that flexible IPs must belong to the same MAC group (see details about MAC groups).
        :param server_id: ID of the server on which to attach the flexible IPs.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`AttachFlexibleIPsResponse <AttachFlexibleIPsResponse>`

        Usage:
        ::

            result = api.attach_flexible_ip(
                fips_ids=[],
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

    def detach_flexible_ip(
        self,
        *,
        fips_ids: List[str],
        zone: Optional[Zone] = None,
    ) -> DetachFlexibleIPsResponse:
        """
        Detach an existing flexible IP from a server.
        Detach an existing flexible IP from a specified Elastic Metal server.
        :param fips_ids: List of flexible IP IDs to detach from a server. Multiple IDs can be provided. Note that flexible IPs must belong to the same MAC group.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`DetachFlexibleIPsResponse <DetachFlexibleIPsResponse>`

        Usage:
        ::

            result = api.detach_flexible_ip(
                fips_ids=[],
            )
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

    def generate_mac_addr(
        self,
        *,
        fip_id: str,
        mac_type: MACAddressType,
        zone: Optional[Zone] = None,
    ) -> FlexibleIP:
        """
        Generate a virtual MAC address on an existing flexible IP.
        Generate a virtual MAC (Media Access Control) address on an existing flexible IP.
        :param fip_id: ID of the flexible IP for which to generate a virtual MAC.
        :param mac_type: TODO.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`FlexibleIP <FlexibleIP>`

        Usage:
        ::

            result = api.generate_mac_addr(
                fip_id="example",
                mac_type=MACAddressType.unknown_type,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_fip_id = validate_path_param("fip_id", fip_id)

        res = self._request(
            "POST",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips/{param_fip_id}/mac",
            body=marshal_GenerateMACAddrRequest(
                GenerateMACAddrRequest(
                    fip_id=fip_id,
                    mac_type=mac_type,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_FlexibleIP(res.json())

    def duplicate_mac_addr(
        self,
        *,
        fip_id: str,
        duplicate_from_fip_id: str,
        zone: Optional[Zone] = None,
    ) -> FlexibleIP:
        """
        Duplicate a virtual MAC address to another flexible IP.
        Duplicate a virtual MAC address from a given flexible IP to another flexible IP attached to the same server.
        :param fip_id: Note that the flexible IPs need to be attached to the same server.
        :param duplicate_from_fip_id: Note that flexible IPs need to be attached to the same server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`FlexibleIP <FlexibleIP>`

        Usage:
        ::

            result = api.duplicate_mac_addr(
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

    def move_mac_addr(
        self,
        *,
        fip_id: str,
        dst_fip_id: str,
        zone: Optional[Zone] = None,
    ) -> FlexibleIP:
        """
        Relocate an existing virtual MAC address to a different flexible IP.
        Relocate a virtual MAC (Media Access Control) address from an existing flexible IP to a different flexible IP.
        :param fip_id:
        :param dst_fip_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`FlexibleIP <FlexibleIP>`

        Usage:
        ::

            result = api.move_mac_addr(
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

    def delete_mac_addr(
        self,
        *,
        fip_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Detach a given virtual MAC address from an existing flexible IP.
        Detach a given MAC (Media Access Control) address from an existing flexible IP.
        :param fip_id: If the flexible IP belongs to a MAC group, the MAC will be removed from both the MAC group and flexible IP.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_mac_addr(
                fip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_fip_id = validate_path_param("fip_id", fip_id)

        res = self._request(
            "DELETE",
            f"/flexible-ip/v1alpha1/zones/{param_zone}/fips/{param_fip_id}/mac",
        )

        self._throw_on_error(res)
