# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Dict, List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    random_name,
    validate_path_param,
    fetch_all_pages_async,
)
from .types_private import (
    _SetImageResponse,
    _SetSecurityGroupRequest,
    _SetSecurityGroupResponse,
    _SetSecurityGroupRuleRequest,
    _SetSecurityGroupRuleResponse,
    _SetServerRequest,
    _SetServerResponse,
    _SetSnapshotRequest,
    _SetSnapshotResponse,
)
from .types import (
    Arch,
    AttachServerVolumeRequestVolumeType,
    BootType,
    ImageState,
    IpType,
    ListServersRequestOrder,
    PlacementGroupPolicyMode,
    PlacementGroupPolicyType,
    SecurityGroupPolicy,
    SecurityGroupRuleAction,
    SecurityGroupRuleDirection,
    SecurityGroupRuleProtocol,
    ServerAction,
    ServerState,
    SnapshotState,
    SnapshotVolumeType,
    VolumeVolumeType,
    ApplyBlockMigrationRequest,
    AttachServerVolumeRequest,
    AttachServerVolumeResponse,
    Bootscript,
    CreateImageRequest,
    CreateImageResponse,
    CreateIpRequest,
    CreateIpResponse,
    CreatePlacementGroupRequest,
    CreatePlacementGroupResponse,
    CreatePrivateNICRequest,
    CreatePrivateNICResponse,
    CreateSecurityGroupRequest,
    CreateSecurityGroupResponse,
    CreateSecurityGroupRuleRequest,
    CreateSecurityGroupRuleResponse,
    CreateServerRequest,
    CreateServerResponse,
    CreateSnapshotRequest,
    CreateSnapshotResponse,
    CreateVolumeRequest,
    CreateVolumeResponse,
    DetachServerVolumeRequest,
    DetachServerVolumeResponse,
    ExportSnapshotRequest,
    ExportSnapshotResponse,
    GetBootscriptResponse,
    GetDashboardResponse,
    GetImageResponse,
    GetIpResponse,
    GetPlacementGroupResponse,
    GetPlacementGroupServersResponse,
    GetPrivateNICResponse,
    GetSecurityGroupResponse,
    GetSecurityGroupRuleResponse,
    GetServerResponse,
    GetServerTypesAvailabilityResponse,
    GetSnapshotResponse,
    GetVolumeResponse,
    Image,
    Ip,
    ListBootscriptsResponse,
    ListImagesResponse,
    ListIpsResponse,
    ListPlacementGroupsResponse,
    ListPrivateNICsResponse,
    ListSecurityGroupRulesResponse,
    ListSecurityGroupsResponse,
    ListServerActionsResponse,
    ListServerUserDataResponse,
    ListServersResponse,
    ListServersTypesResponse,
    ListSnapshotsResponse,
    ListVolumesResponse,
    ListVolumesTypesResponse,
    MigrationPlan,
    PlacementGroup,
    PlanBlockMigrationRequest,
    PrivateNIC,
    SecurityGroup,
    SecurityGroupRule,
    SecurityGroupSummary,
    SecurityGroupTemplate,
    Server,
    ServerActionRequest,
    ServerActionRequestVolumeBackupTemplate,
    ServerActionResponse,
    ServerIp,
    ServerIpv6,
    ServerLocation,
    ServerMaintenance,
    ServerSummary,
    SetImageRequest,
    SetPlacementGroupRequest,
    SetPlacementGroupResponse,
    SetPlacementGroupServersRequest,
    SetPlacementGroupServersResponse,
    SetSecurityGroupRulesRequest,
    SetSecurityGroupRulesRequestRule,
    SetSecurityGroupRulesResponse,
    Snapshot,
    SnapshotBaseVolume,
    UpdateImageRequest,
    UpdateImageResponse,
    UpdateIpRequest,
    UpdateIpResponse,
    UpdatePlacementGroupRequest,
    UpdatePlacementGroupResponse,
    UpdatePlacementGroupServersRequest,
    UpdatePlacementGroupServersResponse,
    UpdatePrivateNICRequest,
    UpdateSecurityGroupRequest,
    UpdateSecurityGroupResponse,
    UpdateSecurityGroupRuleRequest,
    UpdateSecurityGroupRuleResponse,
    UpdateServerRequest,
    UpdateServerResponse,
    UpdateSnapshotRequest,
    UpdateSnapshotResponse,
    UpdateVolumeRequest,
    UpdateVolumeResponse,
    Volume,
    VolumeImageUpdateTemplate,
    VolumeServerTemplate,
    VolumeSummary,
    VolumeTemplate,
)
from .marshalling import (
    unmarshal_PrivateNIC,
    unmarshal_AttachServerVolumeResponse,
    unmarshal_CreateImageResponse,
    unmarshal_CreateIpResponse,
    unmarshal_CreatePlacementGroupResponse,
    unmarshal_CreatePrivateNICResponse,
    unmarshal_CreateSecurityGroupResponse,
    unmarshal_CreateSecurityGroupRuleResponse,
    unmarshal_CreateServerResponse,
    unmarshal_CreateSnapshotResponse,
    unmarshal_CreateVolumeResponse,
    unmarshal_DetachServerVolumeResponse,
    unmarshal_ExportSnapshotResponse,
    unmarshal_GetBootscriptResponse,
    unmarshal_GetDashboardResponse,
    unmarshal_GetImageResponse,
    unmarshal_GetIpResponse,
    unmarshal_GetPlacementGroupResponse,
    unmarshal_GetPlacementGroupServersResponse,
    unmarshal_GetPrivateNICResponse,
    unmarshal_GetSecurityGroupResponse,
    unmarshal_GetSecurityGroupRuleResponse,
    unmarshal_GetServerResponse,
    unmarshal_GetServerTypesAvailabilityResponse,
    unmarshal_GetSnapshotResponse,
    unmarshal_GetVolumeResponse,
    unmarshal_ListBootscriptsResponse,
    unmarshal_ListImagesResponse,
    unmarshal_ListIpsResponse,
    unmarshal_ListPlacementGroupsResponse,
    unmarshal_ListPrivateNICsResponse,
    unmarshal_ListSecurityGroupRulesResponse,
    unmarshal_ListSecurityGroupsResponse,
    unmarshal_ListServerActionsResponse,
    unmarshal_ListServerUserDataResponse,
    unmarshal_ListServersResponse,
    unmarshal_ListServersTypesResponse,
    unmarshal_ListSnapshotsResponse,
    unmarshal_ListVolumesResponse,
    unmarshal_ListVolumesTypesResponse,
    unmarshal_MigrationPlan,
    unmarshal_ServerActionResponse,
    unmarshal_SetPlacementGroupResponse,
    unmarshal_SetPlacementGroupServersResponse,
    unmarshal_SetSecurityGroupRulesResponse,
    unmarshal_UpdateImageResponse,
    unmarshal_UpdateIpResponse,
    unmarshal_UpdatePlacementGroupResponse,
    unmarshal_UpdatePlacementGroupServersResponse,
    unmarshal_UpdateSecurityGroupResponse,
    unmarshal_UpdateSecurityGroupRuleResponse,
    unmarshal_UpdateServerResponse,
    unmarshal_UpdateSnapshotResponse,
    unmarshal_UpdateVolumeResponse,
    unmarshal__SetImageResponse,
    unmarshal__SetSecurityGroupResponse,
    unmarshal__SetSecurityGroupRuleResponse,
    unmarshal__SetServerResponse,
    unmarshal__SetSnapshotResponse,
    marshal_ApplyBlockMigrationRequest,
    marshal_AttachServerVolumeRequest,
    marshal_CreateImageRequest,
    marshal_CreateIpRequest,
    marshal_CreatePlacementGroupRequest,
    marshal_CreatePrivateNICRequest,
    marshal_CreateSecurityGroupRequest,
    marshal_CreateSecurityGroupRuleRequest,
    marshal_CreateServerRequest,
    marshal_CreateSnapshotRequest,
    marshal_CreateVolumeRequest,
    marshal_DetachServerVolumeRequest,
    marshal_ExportSnapshotRequest,
    marshal_PlanBlockMigrationRequest,
    marshal_ServerActionRequest,
    marshal_SetImageRequest,
    marshal_SetPlacementGroupRequest,
    marshal_SetPlacementGroupServersRequest,
    marshal_SetSecurityGroupRulesRequest,
    marshal_UpdateImageRequest,
    marshal_UpdateIpRequest,
    marshal_UpdatePlacementGroupRequest,
    marshal_UpdatePlacementGroupServersRequest,
    marshal_UpdatePrivateNICRequest,
    marshal_UpdateSecurityGroupRequest,
    marshal_UpdateSecurityGroupRuleRequest,
    marshal_UpdateServerRequest,
    marshal_UpdateSnapshotRequest,
    marshal_UpdateVolumeRequest,
    marshal__SetSecurityGroupRequest,
    marshal__SetSecurityGroupRuleRequest,
    marshal__SetServerRequest,
    marshal__SetSnapshotRequest,
)


class InstanceV1API(API):
    """
    This API allows you to manage your Instances.
    """

    async def get_server_types_availability(
        self,
        *,
        zone: Optional[Zone] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> GetServerTypesAvailabilityResponse:
        """
        Get availability.
        Get availability for all Instance types.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :return: :class:`GetServerTypesAvailabilityResponse <GetServerTypesAvailabilityResponse>`

        Usage:
        ::

            result = await api.get_server_types_availability()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/products/servers/availability",
            params={
                "page": page,
                "per_page": per_page or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GetServerTypesAvailabilityResponse(res.json())

    async def list_servers_types(
        self,
        *,
        zone: Optional[Zone] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListServersTypesResponse:
        """
        List Instance types.
        List available Instance types and their technical details.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param per_page:
        :param page:
        :return: :class:`ListServersTypesResponse <ListServersTypesResponse>`

        Usage:
        ::

            result = await api.list_servers_types()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/products/servers",
            params={
                "page": page,
                "per_page": per_page or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServersTypesResponse(res.json())

    async def list_volumes_types(
        self,
        *,
        zone: Optional[Zone] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListVolumesTypesResponse:
        """
        List volume types.
        List all volume types and their technical details.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param per_page:
        :param page:
        :return: :class:`ListVolumesTypesResponse <ListVolumesTypesResponse>`

        Usage:
        ::

            result = await api.list_volumes_types()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/products/volumes",
            params={
                "page": page,
                "per_page": per_page or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVolumesTypesResponse(res.json())

    async def list_servers(
        self,
        *,
        zone: Optional[Zone] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        name: Optional[str] = None,
        private_ip: Optional[str] = None,
        without_ip: Optional[bool] = None,
        with_ip: Optional[str] = None,
        commercial_type: Optional[str] = None,
        state: Optional[ServerState] = None,
        tags: Optional[List[str]] = None,
        private_network: Optional[str] = None,
        order: Optional[ListServersRequestOrder] = None,
        private_networks: Optional[List[str]] = None,
        private_nic_mac_address: Optional[str] = None,
        servers: Optional[List[str]] = None,
    ) -> ListServersResponse:
        """
        List all Instances.
        List all Instances in a specified Availability Zone, e.g. `fr-par-1`.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :param organization: List only Instances of this Organization ID.
        :param project: List only Instances of this Project ID.
        :param name: Filter Instances by name (eg. "server1" will return "server100" and "server1" but not "foo").
        :param private_ip: List Instances by private_ip.
        :param without_ip: List Instances that are not attached to a public IP.
        :param with_ip: List Instances by IP (both private_ip and public_ip are supported).
        :param commercial_type: List Instances of this commercial type.
        :param state: List Instances in this state.
        :param tags: List Instances with these exact tags (to filter with several tags, use commas to separate them).
        :param private_network: List Instances in this Private Network.
        :param order: Define the order of the returned servers.
        :param private_networks: List Instances from the given Private Networks (use commas to separate them).
        :param private_nic_mac_address: List Instances associated with the given private NIC MAC address.
        :param servers: List Instances from these server ids (use commas to separate them).
        :return: :class:`ListServersResponse <ListServersResponse>`

        Usage:
        ::

            result = await api.list_servers()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/servers",
            params={
                "commercial_type": commercial_type,
                "name": name,
                "order": order,
                "organization": organization or self.client.default_organization_id,
                "page": page,
                "per_page": per_page or self.client.default_page_size,
                "private_ip": private_ip,
                "private_network": private_network,
                "private_networks": ",".join(private_networks)
                if private_networks and len(private_networks) > 0
                else None,
                "private_nic_mac_address": private_nic_mac_address,
                "project": project or self.client.default_project_id,
                "servers": ",".join(servers) if servers and len(servers) > 0 else None,
                "state": state,
                "tags": ",".join(tags) if tags and len(tags) > 0 else None,
                "with_ip": with_ip,
                "without_ip": without_ip,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServersResponse(res.json())

    async def list_servers_all(
        self,
        *,
        zone: Optional[Zone] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        name: Optional[str] = None,
        private_ip: Optional[str] = None,
        without_ip: Optional[bool] = None,
        with_ip: Optional[str] = None,
        commercial_type: Optional[str] = None,
        state: Optional[ServerState] = None,
        tags: Optional[List[str]] = None,
        private_network: Optional[str] = None,
        order: Optional[ListServersRequestOrder] = None,
        private_networks: Optional[List[str]] = None,
        private_nic_mac_address: Optional[str] = None,
        servers: Optional[List[str]] = None,
    ) -> List[Server]:
        """
        List all Instances.
        List all Instances in a specified Availability Zone, e.g. `fr-par-1`.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :param organization: List only Instances of this Organization ID.
        :param project: List only Instances of this Project ID.
        :param name: Filter Instances by name (eg. "server1" will return "server100" and "server1" but not "foo").
        :param private_ip: List Instances by private_ip.
        :param without_ip: List Instances that are not attached to a public IP.
        :param with_ip: List Instances by IP (both private_ip and public_ip are supported).
        :param commercial_type: List Instances of this commercial type.
        :param state: List Instances in this state.
        :param tags: List Instances with these exact tags (to filter with several tags, use commas to separate them).
        :param private_network: List Instances in this Private Network.
        :param order: Define the order of the returned servers.
        :param private_networks: List Instances from the given Private Networks (use commas to separate them).
        :param private_nic_mac_address: List Instances associated with the given private NIC MAC address.
        :param servers: List Instances from these server ids (use commas to separate them).
        :return: :class:`List[Server] <List[Server]>`

        Usage:
        ::

            result = await api.list_servers_all()
        """

        return await fetch_all_pages_async(
            type=ListServersResponse,
            key="servers",
            fetcher=self.list_servers,
            args={
                "zone": zone,
                "per_page": per_page,
                "page": page,
                "organization": organization,
                "project": project,
                "name": name,
                "private_ip": private_ip,
                "without_ip": without_ip,
                "with_ip": with_ip,
                "commercial_type": commercial_type,
                "state": state,
                "tags": tags,
                "private_network": private_network,
                "order": order,
                "private_networks": private_networks,
                "private_nic_mac_address": private_nic_mac_address,
                "servers": servers,
            },
        )

    async def _create_server(
        self,
        *,
        commercial_type: str,
        image: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        dynamic_ip_required: Optional[bool] = None,
        routed_ip_enabled: Optional[bool] = None,
        volumes: Optional[Dict[str, VolumeServerTemplate]] = None,
        enable_ipv6: Optional[bool] = None,
        public_ip: Optional[str] = None,
        public_ips: Optional[List[str]] = None,
        boot_type: Optional[BootType] = None,
        bootscript: Optional[str] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        security_group: Optional[str] = None,
        placement_group: Optional[str] = None,
        admin_password_encryption_ssh_key_id: Optional[str] = None,
    ) -> CreateServerResponse:
        """
        Create an Instance.
        Create a new Instance of the specified commercial type in the specified zone. Pay attention to the volumes parameter, which takes an object which can be used in different ways to achieve different behaviors.
        Get more information in the [Technical Information](#technical-information) section of the introduction.
        :param commercial_type: Define the Instance commercial type (i.e. GP1-S).
        :param image: Instance image ID or label.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Instance name.
        :param dynamic_ip_required: Define if a dynamic IPv4 is required for the Instance.
        :param routed_ip_enabled: If true, configure the Instance so it uses the new routed IP mode.
        :param volumes: Volumes attached to the server.
        :param enable_ipv6: True if IPv6 is enabled on the server (deprecated and always `False` when `routed_ip_enabled` is `True`).
        :param public_ip: ID of the reserved IP to attach to the Instance.
        :param public_ips: A list of reserved IP IDs to attach to the Instance.
        :param boot_type: Boot type to use.
        :param bootscript: Bootscript ID to use when `boot_type` is set to `bootscript`.
        :param organization: Instance Organization ID.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param project: Instance Project ID.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param tags: Instance tags.
        :param security_group: Security group ID.
        :param placement_group: Placement group ID if Instance must be part of a placement group.
        :param admin_password_encryption_ssh_key_id: The public_key value of this key is used to encrypt the admin password.
        :return: :class:`CreateServerResponse <CreateServerResponse>`

        Usage:
        ::

            result = await api._create_server(
                commercial_type="example",
                image="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/servers",
            body=marshal_CreateServerRequest(
                CreateServerRequest(
                    commercial_type=commercial_type,
                    image=image,
                    zone=zone,
                    name=name or random_name(prefix="srv"),
                    dynamic_ip_required=dynamic_ip_required,
                    routed_ip_enabled=routed_ip_enabled,
                    volumes=volumes,
                    enable_ipv6=enable_ipv6,
                    public_ip=public_ip,
                    public_ips=public_ips,
                    boot_type=boot_type,
                    bootscript=bootscript,
                    tags=tags,
                    security_group=security_group,
                    placement_group=placement_group,
                    admin_password_encryption_ssh_key_id=admin_password_encryption_ssh_key_id,
                    project=project,
                    organization=organization,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateServerResponse(res.json())

    async def delete_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete an Instance.
        Delete the Instance with the specified ID.
        :param server_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}",
        )

        self._throw_on_error(res)

    async def get_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> GetServerResponse:
        """
        Get an Instance.
        Get the details of a specified Instance.
        :param server_id: UUID of the Instance you want to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GetServerResponse <GetServerResponse>`

        Usage:
        ::

            result = await api.get_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetServerResponse(res.json())

    async def _set_server(
        self,
        *,
        zone: Optional[Zone] = None,
        id: str,
        name: str,
        commercial_type: str,
        organization: Optional[str] = None,
        dynamic_ip_required: bool,
        hostname: str,
        protected: bool,
        state_detail: str,
        project: Optional[str] = None,
        allowed_actions: Optional[List[ServerAction]] = None,
        tags: Optional[List[str]] = None,
        creation_date: Optional[datetime] = None,
        routed_ip_enabled: Optional[bool] = None,
        enable_ipv6: Optional[bool] = None,
        image: Optional[Image] = None,
        private_ip: Optional[str] = None,
        public_ip: Optional[ServerIp] = None,
        public_ips: Optional[List[ServerIp]] = None,
        modification_date: Optional[datetime] = None,
        state: Optional[ServerState] = None,
        location: Optional[ServerLocation] = None,
        ipv6: Optional[ServerIpv6] = None,
        bootscript: Optional[Bootscript] = None,
        boot_type: Optional[BootType] = None,
        volumes: Optional[Dict[str, Volume]] = None,
        security_group: Optional[SecurityGroupSummary] = None,
        maintenances: Optional[List[ServerMaintenance]] = None,
        arch: Optional[Arch] = None,
        placement_group: Optional[PlacementGroup] = None,
        private_nics: Optional[List[PrivateNIC]] = None,
        admin_password_encryption_ssh_key_id: Optional[str] = None,
    ) -> _SetServerResponse:
        """
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param id: Instance unique ID.
        :param name: Instance name.
        :param commercial_type: Instance commercial type (eg. GP1-M).
        :param organization: Instance Organization ID.
        :param dynamic_ip_required: True if a dynamic IPv4 is required.
        :param hostname: Instance host name.
        :param protected: Instance protection option is activated.
        :param state_detail: Instance state_detail.
        :param project: Instance Project ID.
        :param allowed_actions: Provide a list of allowed actions on the server.
        :param tags: Tags associated with the Instance.
        :param creation_date: Instance creation date.
        :param routed_ip_enabled: True to configure the instance so it uses the new routed IP mode (once this is set to True you cannot set it back to False).
        :param enable_ipv6: True if IPv6 is enabled (deprecated and always `False` when `routed_ip_enabled` is `True`).
        :param image: Provide information on the Instance image.
        :param private_ip: Instance private IP address (deprecated and always `null` when `routed_ip_enabled` is `True`).
        :param public_ip: Information about the public IP (deprecated in favor of `public_ips`).
        :param public_ips: Information about all the public IPs attached to the server.
        :param modification_date: Instance modification date.
        :param state: Instance state.
        :param location: Instance location.
        :param ipv6: Instance IPv6 address (deprecated when `routed_ip_enabled` is `True`).
        :param bootscript: Instance bootscript.
        :param boot_type: Instance boot type.
        :param volumes: Instance volumes.
        :param security_group: Instance security group.
        :param maintenances: Instance planned maintenances.
        :param arch: Instance architecture (refers to the CPU architecture used for the Instance, e.g. x86_64, arm64).
        :param placement_group: Instance placement group.
        :param private_nics: Instance private NICs.
        :param admin_password_encryption_ssh_key_id: The public_key value of this key is used to encrypt the admin password. When set to an empty string, reset this value and admin_password_encrypted_value to an empty string so a new password may be generated.
        :return: :class:`_SetServerResponse <_SetServerResponse>`

        Usage:
        ::

            result = await api._set_server(
                id="example",
                name="example",
                commercial_type="example",
                dynamic_ip_required=False,
                hostname="example",
                protected=False,
                state_detail="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_id = validate_path_param("id", id)

        res = self._request(
            "PUT",
            f"/instance/v1/zones/{param_zone}/servers/{param_id}",
            body=marshal__SetServerRequest(
                _SetServerRequest(
                    zone=zone,
                    id=id,
                    name=name,
                    commercial_type=commercial_type,
                    organization=organization,
                    dynamic_ip_required=dynamic_ip_required,
                    hostname=hostname,
                    protected=protected,
                    state_detail=state_detail,
                    project=project,
                    allowed_actions=allowed_actions,
                    tags=tags,
                    creation_date=creation_date,
                    routed_ip_enabled=routed_ip_enabled,
                    enable_ipv6=enable_ipv6,
                    image=image,
                    private_ip=private_ip,
                    public_ip=public_ip,
                    public_ips=public_ips,
                    modification_date=modification_date,
                    state=state,
                    location=location,
                    ipv6=ipv6,
                    bootscript=bootscript,
                    boot_type=boot_type,
                    volumes=volumes,
                    security_group=security_group,
                    maintenances=maintenances,
                    arch=arch,
                    placement_group=placement_group,
                    private_nics=private_nics,
                    admin_password_encryption_ssh_key_id=admin_password_encryption_ssh_key_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal__SetServerResponse(res.json())

    async def _update_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        boot_type: Optional[BootType] = None,
        tags: Optional[List[str]] = None,
        volumes: Optional[Dict[str, VolumeServerTemplate]] = None,
        bootscript: Optional[str] = None,
        dynamic_ip_required: Optional[bool] = None,
        routed_ip_enabled: Optional[bool] = None,
        public_ips: Optional[List[str]] = None,
        enable_ipv6: Optional[bool] = None,
        protected: Optional[bool] = None,
        security_group: Optional[SecurityGroupTemplate] = None,
        placement_group: Optional[str] = None,
        private_nics: Optional[List[str]] = None,
        commercial_type: Optional[str] = None,
        admin_password_encryption_ssh_key_id: Optional[str] = None,
    ) -> UpdateServerResponse:
        """
        Update an Instance.
        Update the Instance information, such as name, boot mode, or tags.
        :param server_id: UUID of the Instance.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the Instance.
        :param boot_type:
        :param tags: Tags of the Instance.
        :param volumes:
        :param bootscript:
        :param dynamic_ip_required:
        :param routed_ip_enabled: True to configure the instance so it uses the new routed IP mode (once this is set to True you cannot set it back to False).
        :param public_ips: A list of reserved IP IDs to attach to the Instance.
        :param enable_ipv6:
        :param protected:
        :param security_group:
        :param placement_group: Placement group ID if Instance must be part of a placement group.
        :param private_nics: Instance private NICs.
        :param commercial_type: Warning: This field has some restrictions:
        - Cannot be changed if the Instance is not in `stopped` state.
        - Cannot be changed if the Instance is in a placement group.
        - Cannot be changed from/to a Windows offer to/from a Linux offer.
        - Local storage requirements of the target commercial_types must be fulfilled (i.e. if an Instance has 80GB of local storage, it can be changed into a GP1-XS, which has a maximum of 150GB, but it cannot be changed into a DEV1-S, which has only 20GB).
        :param admin_password_encryption_ssh_key_id: The public_key value of this key is used to encrypt the admin password. When set to an empty string, reset this value and admin_password_encrypted_value to an empty string so a new password may be generated.
        :return: :class:`UpdateServerResponse <UpdateServerResponse>`

        Usage:
        ::

            result = await api._update_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "PATCH",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}",
            body=marshal_UpdateServerRequest(
                UpdateServerRequest(
                    server_id=server_id,
                    zone=zone,
                    name=name,
                    boot_type=boot_type,
                    tags=tags,
                    volumes=volumes,
                    bootscript=bootscript,
                    dynamic_ip_required=dynamic_ip_required,
                    routed_ip_enabled=routed_ip_enabled,
                    public_ips=public_ips,
                    enable_ipv6=enable_ipv6,
                    protected=protected,
                    security_group=security_group,
                    placement_group=placement_group,
                    private_nics=private_nics,
                    commercial_type=commercial_type,
                    admin_password_encryption_ssh_key_id=admin_password_encryption_ssh_key_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_UpdateServerResponse(res.json())

    async def list_server_actions(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> ListServerActionsResponse:
        """
        List Instance actions.
        List all actions (e.g. power on, power off, reboot) that can currently be performed on an Instance.
        :param server_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ListServerActionsResponse <ListServerActionsResponse>`

        Usage:
        ::

            result = await api.list_server_actions(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/action",
        )

        self._throw_on_error(res)
        return unmarshal_ListServerActionsResponse(res.json())

    async def server_action(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        action: Optional[ServerAction] = None,
        name: Optional[str] = None,
        volumes: Optional[Dict[str, ServerActionRequestVolumeBackupTemplate]] = None,
    ) -> ServerActionResponse:
        """
        Perform action.
        Perform an action on an Instance.
        Available actions are:
        * `poweron`: Start a stopped Instance.
        * `poweroff`: Fully stop the Instance and release the hypervisor slot.
        * `stop_in_place`: Stop the Instance, but keep the slot on the hypervisor.
        * `reboot`: Stop the instance and restart it.
        * `backup`:  Create an image with all the volumes of an Instance.
        * `terminate`: Delete the Instance along with all attached volumes.
        * `enable_routed_ip`: Migrate the Instance to the new network stack.

        Keep in mind that terminating an Instance will result in the deletion of all attached volumes, including local and block storage.
        If you want to preserve your local volumes, you should use the `archive` action instead of `terminate`. Similarly, if you want to keep your block storage volumes, you must first detach them before issuing the `terminate` command.
        For more information, read the [Volumes](#path-volumes-list-volumes) documentation.
        :param server_id: UUID of the Instance.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param action: Action to perform on the Instance.
        :param name: Name of the backup you want to create.
        This field should only be specified when performing a backup action.
        :param volumes: For each volume UUID, the snapshot parameters of the volume.
        This field should only be specified when performing a backup action.
        :return: :class:`ServerActionResponse <ServerActionResponse>`

        Usage:
        ::

            result = await api.server_action(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/action",
            body=marshal_ServerActionRequest(
                ServerActionRequest(
                    server_id=server_id,
                    zone=zone,
                    action=action,
                    name=name,
                    volumes=volumes,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ServerActionResponse(res.json())

    async def list_server_user_data(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> ListServerUserDataResponse:
        """
        List user data.
        List all user data keys registered on a specified Instance.
        :param server_id: UUID of the Instance.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ListServerUserDataResponse <ListServerUserDataResponse>`

        Usage:
        ::

            result = await api.list_server_user_data(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/user_data",
        )

        self._throw_on_error(res)
        return unmarshal_ListServerUserDataResponse(res.json())

    async def delete_server_user_data(
        self,
        *,
        server_id: str,
        key: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete user data.
        Delete the specified key from an Instance's user data.
        :param server_id: UUID of the Instance.
        :param key: Key of the user data to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_server_user_data(
                server_id="example",
                key="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_key = validate_path_param("key", key)

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/user_data/{param_key}",
        )

        self._throw_on_error(res)

    async def attach_server_volume(
        self,
        *,
        server_id: str,
        volume_id: str,
        zone: Optional[Zone] = None,
        volume_type: Optional[AttachServerVolumeRequestVolumeType] = None,
        boot: Optional[bool] = None,
    ) -> AttachServerVolumeResponse:
        """
        :param server_id:
        :param volume_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param volume_type:
        :param boot:
        :return: :class:`AttachServerVolumeResponse <AttachServerVolumeResponse>`

        Usage:
        ::

            result = await api.attach_server_volume(
                server_id="example",
                volume_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/attach-volume",
            body=marshal_AttachServerVolumeRequest(
                AttachServerVolumeRequest(
                    server_id=server_id,
                    volume_id=volume_id,
                    zone=zone,
                    volume_type=volume_type,
                    boot=boot,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AttachServerVolumeResponse(res.json())

    async def detach_server_volume(
        self,
        *,
        server_id: str,
        volume_id: str,
        zone: Optional[Zone] = None,
    ) -> DetachServerVolumeResponse:
        """
        :param server_id:
        :param volume_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`DetachServerVolumeResponse <DetachServerVolumeResponse>`

        Usage:
        ::

            result = await api.detach_server_volume(
                server_id="example",
                volume_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/detach-volume",
            body=marshal_DetachServerVolumeRequest(
                DetachServerVolumeRequest(
                    server_id=server_id,
                    volume_id=volume_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DetachServerVolumeResponse(res.json())

    async def list_images(
        self,
        *,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        name: Optional[str] = None,
        public: Optional[bool] = None,
        arch: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[str] = None,
    ) -> ListImagesResponse:
        """
        List Instance images.
        List all existing Instance images.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param organization:
        :param per_page:
        :param page:
        :param name:
        :param public:
        :param arch:
        :param project:
        :param tags:
        :return: :class:`ListImagesResponse <ListImagesResponse>`

        Usage:
        ::

            result = await api.list_images()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/images",
            params={
                "arch": arch,
                "name": name,
                "organization": organization or self.client.default_organization_id,
                "page": page,
                "per_page": per_page or self.client.default_page_size,
                "project": project or self.client.default_project_id,
                "public": public,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListImagesResponse(res.json())

    async def list_images_all(
        self,
        *,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        name: Optional[str] = None,
        public: Optional[bool] = None,
        arch: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[str] = None,
    ) -> List[Image]:
        """
        List Instance images.
        List all existing Instance images.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param organization:
        :param per_page:
        :param page:
        :param name:
        :param public:
        :param arch:
        :param project:
        :param tags:
        :return: :class:`List[Image] <List[Image]>`

        Usage:
        ::

            result = await api.list_images_all()
        """

        return await fetch_all_pages_async(
            type=ListImagesResponse,
            key="images",
            fetcher=self.list_images,
            args={
                "zone": zone,
                "organization": organization,
                "per_page": per_page,
                "page": page,
                "name": name,
                "public": public,
                "arch": arch,
                "project": project,
                "tags": tags,
            },
        )

    async def get_image(
        self,
        *,
        image_id: str,
        zone: Optional[Zone] = None,
    ) -> GetImageResponse:
        """
        Get an Instance image.
        Get details of an image with the specified ID.
        :param image_id: UUID of the image you want to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GetImageResponse <GetImageResponse>`

        Usage:
        ::

            result = await api.get_image(
                image_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_image_id = validate_path_param("image_id", image_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/images/{param_image_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetImageResponse(res.json())

    async def create_image(
        self,
        *,
        root_volume: str,
        arch: Arch,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        default_bootscript: Optional[str] = None,
        extra_volumes: Optional[Dict[str, VolumeTemplate]] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        public: Optional[bool] = None,
    ) -> CreateImageResponse:
        """
        Create an Instance image.
        Create an Instance image from the specified snapshot ID.
        :param root_volume: UUID of the snapshot.
        :param arch: Architecture of the image.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the image.
        :param default_bootscript: Default bootscript of the image.
        :param extra_volumes: Additional volumes of the image.
        :param organization: Organization ID of the image.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param project: Project ID of the image.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param tags: Tags of the image.
        :param public: True to create a public image.
        :return: :class:`CreateImageResponse <CreateImageResponse>`

        Usage:
        ::

            result = await api.create_image(
                root_volume="example",
                arch=Arch.unknown_arch,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/images",
            body=marshal_CreateImageRequest(
                CreateImageRequest(
                    root_volume=root_volume,
                    arch=arch,
                    zone=zone,
                    name=name or random_name(prefix="img"),
                    default_bootscript=default_bootscript,
                    extra_volumes=extra_volumes,
                    tags=tags,
                    public=public,
                    project=project,
                    organization=organization,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateImageResponse(res.json())

    async def _set_image(
        self,
        *,
        zone: Optional[Zone] = None,
        id: str,
        name: str,
        arch: Optional[Arch] = None,
        creation_date: Optional[datetime] = None,
        modification_date: Optional[datetime] = None,
        from_server: str,
        public: bool,
        default_bootscript: Optional[Bootscript] = None,
        extra_volumes: Optional[Dict[str, Volume]] = None,
        organization: Optional[str] = None,
        root_volume: Optional[VolumeSummary] = None,
        state: Optional[ImageState] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> _SetImageResponse:
        """
        Update image.
        Replace all image properties with an image message.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param id:
        :param name:
        :param arch:
        :param creation_date:
        :param modification_date:
        :param from_server:
        :param public:
        :param default_bootscript:
        :param extra_volumes:
        :param organization:
        :param root_volume:
        :param state:
        :param project:
        :param tags:
        :return: :class:`_SetImageResponse <_SetImageResponse>`

        Usage:
        ::

            result = await api._set_image(
                id="example",
                name="example",
                from_server="example",
                public=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_id = validate_path_param("id", id)

        res = self._request(
            "PUT",
            f"/instance/v1/zones/{param_zone}/images/{param_id}",
            body=marshal_SetImageRequest(
                SetImageRequest(
                    zone=zone,
                    id=id,
                    name=name,
                    arch=arch,
                    creation_date=creation_date,
                    modification_date=modification_date,
                    from_server=from_server,
                    public=public,
                    default_bootscript=default_bootscript,
                    extra_volumes=extra_volumes,
                    organization=organization,
                    root_volume=root_volume,
                    state=state,
                    project=project,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal__SetImageResponse(res.json())

    async def update_image(
        self,
        *,
        image_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        arch: Optional[Arch] = None,
        extra_volumes: Optional[Dict[str, VolumeImageUpdateTemplate]] = None,
        tags: Optional[List[str]] = None,
        public: Optional[bool] = None,
    ) -> UpdateImageResponse:
        """
        Update image.
        Update the properties of an image.
        :param image_id: UUID of the image.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the image.
        :param arch: Architecture of the image.
        :param extra_volumes: Additional snapshots of the image, with extra_volumeKey being the position of the snapshot in the image.
        :param tags: Tags of the image.
        :param public: True to set the image as public.
        :return: :class:`UpdateImageResponse <UpdateImageResponse>`

        Usage:
        ::

            result = await api.update_image(
                image_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_image_id = validate_path_param("image_id", image_id)

        res = self._request(
            "PATCH",
            f"/instance/v1/zones/{param_zone}/images/{param_image_id}",
            body=marshal_UpdateImageRequest(
                UpdateImageRequest(
                    image_id=image_id,
                    zone=zone,
                    name=name,
                    arch=arch,
                    extra_volumes=extra_volumes,
                    tags=tags,
                    public=public,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_UpdateImageResponse(res.json())

    async def delete_image(
        self,
        *,
        image_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete an Instance image.
        Delete the image with the specified ID.
        :param image_id: UUID of the image you want to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_image(
                image_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_image_id = validate_path_param("image_id", image_id)

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/images/{param_image_id}",
        )

        self._throw_on_error(res)

    async def list_snapshots(
        self,
        *,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[str] = None,
        base_volume_id: Optional[str] = None,
    ) -> ListSnapshotsResponse:
        """
        List snapshots.
        List all snapshots of an Organization in a specified Availability Zone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param organization: List snapshots only for this Organization ID.
        :param project: List snapshots only for this Project ID.
        :param per_page: Number of snapshots returned per page (positive integer lower or equal to 100).
        :param page: Page to be returned.
        :param name: List snapshots of the requested name.
        :param tags: List snapshots that have the requested tag.
        :param base_volume_id: List snapshots originating only from this volume.
        :return: :class:`ListSnapshotsResponse <ListSnapshotsResponse>`

        Usage:
        ::

            result = await api.list_snapshots()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/snapshots",
            params={
                "base_volume_id": base_volume_id,
                "name": name,
                "organization": organization or self.client.default_organization_id,
                "page": page,
                "per_page": per_page or self.client.default_page_size,
                "project": project or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSnapshotsResponse(res.json())

    async def list_snapshots_all(
        self,
        *,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        name: Optional[str] = None,
        tags: Optional[str] = None,
        base_volume_id: Optional[str] = None,
    ) -> List[Snapshot]:
        """
        List snapshots.
        List all snapshots of an Organization in a specified Availability Zone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param organization: List snapshots only for this Organization ID.
        :param project: List snapshots only for this Project ID.
        :param per_page: Number of snapshots returned per page (positive integer lower or equal to 100).
        :param page: Page to be returned.
        :param name: List snapshots of the requested name.
        :param tags: List snapshots that have the requested tag.
        :param base_volume_id: List snapshots originating only from this volume.
        :return: :class:`List[Snapshot] <List[Snapshot]>`

        Usage:
        ::

            result = await api.list_snapshots_all()
        """

        return await fetch_all_pages_async(
            type=ListSnapshotsResponse,
            key="snapshots",
            fetcher=self.list_snapshots,
            args={
                "zone": zone,
                "organization": organization,
                "project": project,
                "per_page": per_page,
                "page": page,
                "name": name,
                "tags": tags,
                "base_volume_id": base_volume_id,
            },
        )

    async def create_snapshot(
        self,
        *,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        volume_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        volume_type: Optional[SnapshotVolumeType] = None,
        bucket: Optional[str] = None,
        key: Optional[str] = None,
        size: Optional[int] = None,
    ) -> CreateSnapshotResponse:
        """
        Create a snapshot from a specified volume or from a QCOW2 file.
        Create a snapshot from a specified volume or from a QCOW2 file in a specified Availability Zone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the snapshot.
        :param volume_id: UUID of the volume.
        :param tags: Tags of the snapshot.
        :param organization: Organization ID of the snapshot.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param project: Project ID of the snapshot.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param volume_type: Overrides the volume_type of the snapshot.
        If omitted, the volume type of the original volume will be used.
        :param bucket: Bucket name for snapshot imports.
        :param key: Object key for snapshot imports.
        :param size: Imported snapshot size, must be a multiple of 512.
        :return: :class:`CreateSnapshotResponse <CreateSnapshotResponse>`

        Usage:
        ::

            result = await api.create_snapshot()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/snapshots",
            body=marshal_CreateSnapshotRequest(
                CreateSnapshotRequest(
                    zone=zone,
                    name=name or random_name(prefix="snp"),
                    volume_id=volume_id,
                    tags=tags,
                    volume_type=volume_type,
                    bucket=bucket,
                    key=key,
                    size=size,
                    project=project,
                    organization=organization,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateSnapshotResponse(res.json())

    async def get_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[Zone] = None,
    ) -> GetSnapshotResponse:
        """
        Get a snapshot.
        Get details of a snapshot with the specified ID.
        :param snapshot_id: UUID of the snapshot you want to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GetSnapshotResponse <GetSnapshotResponse>`

        Usage:
        ::

            result = await api.get_snapshot(
                snapshot_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/snapshots/{param_snapshot_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetSnapshotResponse(res.json())

    async def _set_snapshot(
        self,
        *,
        id: str,
        name: str,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        volume_type: Optional[VolumeVolumeType] = None,
        size: int,
        state: Optional[SnapshotState] = None,
        base_volume: Optional[SnapshotBaseVolume] = None,
        creation_date: Optional[datetime] = None,
        modification_date: Optional[datetime] = None,
        project: Optional[str] = None,
        snapshot_id: str,
        tags: Optional[List[str]] = None,
    ) -> _SetSnapshotResponse:
        """
        Set snapshot.
        Replace all the properties of a snapshot.
        :param id:
        :param name:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param organization:
        :param volume_type:
        :param size:
        :param state:
        :param base_volume:
        :param creation_date:
        :param modification_date:
        :param project:
        :param snapshot_id:
        :param tags:
        :return: :class:`_SetSnapshotResponse <_SetSnapshotResponse>`

        Usage:
        ::

            result = await api._set_snapshot(
                id="example",
                name="example",
                size=1,
                snapshot_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "PUT",
            f"/instance/v1/zones/{param_zone}/snapshots/{param_snapshot_id}",
            body=marshal__SetSnapshotRequest(
                _SetSnapshotRequest(
                    id=id,
                    name=name,
                    zone=zone,
                    organization=organization,
                    volume_type=volume_type,
                    size=size,
                    state=state,
                    base_volume=base_volume,
                    creation_date=creation_date,
                    modification_date=modification_date,
                    project=project,
                    snapshot_id=snapshot_id,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal__SetSnapshotResponse(res.json())

    async def update_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> UpdateSnapshotResponse:
        """
        Update a snapshot.
        Update the properties of a snapshot.
        :param snapshot_id: UUID of the snapshot.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the snapshot.
        :param tags: Tags of the snapshot.
        :return: :class:`UpdateSnapshotResponse <UpdateSnapshotResponse>`

        Usage:
        ::

            result = await api.update_snapshot(
                snapshot_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "PATCH",
            f"/instance/v1/zones/{param_zone}/snapshots/{param_snapshot_id}",
            body=marshal_UpdateSnapshotRequest(
                UpdateSnapshotRequest(
                    snapshot_id=snapshot_id,
                    zone=zone,
                    name=name,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_UpdateSnapshotResponse(res.json())

    async def delete_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a snapshot.
        Delete the snapshot with the specified ID.
        :param snapshot_id: UUID of the snapshot you want to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_snapshot(
                snapshot_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/snapshots/{param_snapshot_id}",
        )

        self._throw_on_error(res)

    async def export_snapshot(
        self,
        *,
        bucket: str,
        key: str,
        snapshot_id: str,
        zone: Optional[Zone] = None,
    ) -> ExportSnapshotResponse:
        """
        Export a snapshot.
        Export a snapshot to a specified S3 bucket in the same region.
        :param bucket: S3 bucket name.
        :param key: S3 object key.
        :param snapshot_id: Snapshot ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ExportSnapshotResponse <ExportSnapshotResponse>`

        Usage:
        ::

            result = await api.export_snapshot(
                bucket="example",
                key="example",
                snapshot_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/snapshots/{param_snapshot_id}/export",
            body=marshal_ExportSnapshotRequest(
                ExportSnapshotRequest(
                    bucket=bucket,
                    key=key,
                    snapshot_id=snapshot_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ExportSnapshotResponse(res.json())

    async def list_volumes(
        self,
        *,
        zone: Optional[Zone] = None,
        volume_type: Optional[VolumeVolumeType] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
    ) -> ListVolumesResponse:
        """
        List volumes.
        List volumes in the specified Availability Zone. You can filter the output by volume type.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param volume_type: Filter by volume type.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :param organization: Filter volume by Organization ID.
        :param project: Filter volume by Project ID.
        :param tags: Filter volumes with these exact tags (to filter with several tags, use commas to separate them).
        :param name: Filter volume by name (for eg. "vol" will return "myvolume" but not "data").
        :return: :class:`ListVolumesResponse <ListVolumesResponse>`

        Usage:
        ::

            result = await api.list_volumes()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/volumes",
            params={
                "name": name,
                "organization": organization or self.client.default_organization_id,
                "page": page,
                "per_page": per_page or self.client.default_page_size,
                "project": project or self.client.default_project_id,
                "tags": ",".join(tags) if tags and len(tags) > 0 else None,
                "volume_type": volume_type,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVolumesResponse(res.json())

    async def list_volumes_all(
        self,
        *,
        zone: Optional[Zone] = None,
        volume_type: Optional[VolumeVolumeType] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
    ) -> List[Volume]:
        """
        List volumes.
        List volumes in the specified Availability Zone. You can filter the output by volume type.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param volume_type: Filter by volume type.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :param organization: Filter volume by Organization ID.
        :param project: Filter volume by Project ID.
        :param tags: Filter volumes with these exact tags (to filter with several tags, use commas to separate them).
        :param name: Filter volume by name (for eg. "vol" will return "myvolume" but not "data").
        :return: :class:`List[Volume] <List[Volume]>`

        Usage:
        ::

            result = await api.list_volumes_all()
        """

        return await fetch_all_pages_async(
            type=ListVolumesResponse,
            key="volumes",
            fetcher=self.list_volumes,
            args={
                "zone": zone,
                "volume_type": volume_type,
                "per_page": per_page,
                "page": page,
                "organization": organization,
                "project": project,
                "tags": tags,
                "name": name,
            },
        )

    async def create_volume(
        self,
        *,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        volume_type: Optional[VolumeVolumeType] = None,
        size: Optional[int] = None,
        base_snapshot: Optional[str] = None,
    ) -> CreateVolumeResponse:
        """
        Create a volume.
        Create a volume of a specified type in an Availability Zone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Volume name.
        :param organization: Volume Organization ID.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param project: Volume Project ID.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param tags: Volume tags.
        :param volume_type: Volume type.
        :param size: Volume disk size, must be a multiple of 512.
        One-Of ('from'): at most one of 'size', 'base_snapshot' could be set.
        :param base_snapshot: ID of the snapshot on which this volume will be based.
        One-Of ('from'): at most one of 'size', 'base_snapshot' could be set.
        :return: :class:`CreateVolumeResponse <CreateVolumeResponse>`

        Usage:
        ::

            result = await api.create_volume()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/volumes",
            body=marshal_CreateVolumeRequest(
                CreateVolumeRequest(
                    zone=zone,
                    name=name or random_name(prefix="vol"),
                    tags=tags,
                    volume_type=volume_type,
                    project=project,
                    organization=organization,
                    size=size,
                    base_snapshot=base_snapshot,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateVolumeResponse(res.json())

    async def get_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[Zone] = None,
    ) -> GetVolumeResponse:
        """
        Get a volume.
        Get details of a volume with the specified ID.
        :param volume_id: UUID of the volume you want to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GetVolumeResponse <GetVolumeResponse>`

        Usage:
        ::

            result = await api.get_volume(
                volume_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/volumes/{param_volume_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetVolumeResponse(res.json())

    async def update_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        size: Optional[int] = None,
    ) -> UpdateVolumeResponse:
        """
        Update a volume.
        Replace the name and/or size properties of a volume specified by its ID, with the specified value(s). Any volume name can be changed, however only `b_ssd` volumes can currently be increased in size.
        :param volume_id: UUID of the volume.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Volume name.
        :param tags: Tags of the volume.
        :param size: Volume disk size, must be a multiple of 512.
        :return: :class:`UpdateVolumeResponse <UpdateVolumeResponse>`

        Usage:
        ::

            result = await api.update_volume(
                volume_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "PATCH",
            f"/instance/v1/zones/{param_zone}/volumes/{param_volume_id}",
            body=marshal_UpdateVolumeRequest(
                UpdateVolumeRequest(
                    volume_id=volume_id,
                    zone=zone,
                    name=name,
                    tags=tags,
                    size=size,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_UpdateVolumeResponse(res.json())

    async def delete_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a volume.
        Delete the volume with the specified ID.
        :param volume_id: UUID of the volume you want to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_volume(
                volume_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/volumes/{param_volume_id}",
        )

        self._throw_on_error(res)

    async def list_security_groups(
        self,
        *,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        project_default: Optional[bool] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListSecurityGroupsResponse:
        """
        List security groups.
        List all existing security groups.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the security group.
        :param organization: Security group Organization ID.
        :param project: Security group Project ID.
        :param tags: List security groups with these exact tags (to filter with several tags, use commas to separate them).
        :param project_default: Filter security groups with this value for project_default.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :return: :class:`ListSecurityGroupsResponse <ListSecurityGroupsResponse>`

        Usage:
        ::

            result = await api.list_security_groups()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/security_groups",
            params={
                "name": name,
                "organization": organization or self.client.default_organization_id,
                "page": page,
                "per_page": per_page or self.client.default_page_size,
                "project": project or self.client.default_project_id,
                "project_default": project_default,
                "tags": ",".join(tags) if tags and len(tags) > 0 else None,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSecurityGroupsResponse(res.json())

    async def list_security_groups_all(
        self,
        *,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        project_default: Optional[bool] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[SecurityGroup]:
        """
        List security groups.
        List all existing security groups.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the security group.
        :param organization: Security group Organization ID.
        :param project: Security group Project ID.
        :param tags: List security groups with these exact tags (to filter with several tags, use commas to separate them).
        :param project_default: Filter security groups with this value for project_default.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :return: :class:`List[SecurityGroup] <List[SecurityGroup]>`

        Usage:
        ::

            result = await api.list_security_groups_all()
        """

        return await fetch_all_pages_async(
            type=ListSecurityGroupsResponse,
            key="security_groups",
            fetcher=self.list_security_groups,
            args={
                "zone": zone,
                "name": name,
                "organization": organization,
                "project": project,
                "tags": tags,
                "project_default": project_default,
                "per_page": per_page,
                "page": page,
            },
        )

    async def create_security_group(
        self,
        *,
        description: str,
        stateful: bool,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization_default: Optional[bool] = None,
        project_default: Optional[bool] = None,
        inbound_default_policy: Optional[SecurityGroupPolicy] = None,
        outbound_default_policy: Optional[SecurityGroupPolicy] = None,
        enable_default_security: Optional[bool] = None,
    ) -> CreateSecurityGroupResponse:
        """
        Create a security group.
        Create a security group with a specified name and description.
        :param description: Description of the security group.
        :param stateful: Whether the security group is stateful or not.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the security group.
        :param organization: Organization ID the security group belongs to.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param project: Project ID the security group belong to.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param tags: Tags of the security group.
        :param organization_default: Defines whether this security group becomes the default security group for new Instances.
        One-Of ('default_identifier'): at most one of 'organization_default', 'project_default' could be set.
        :param project_default: Whether this security group becomes the default security group for new Instances.
        One-Of ('default_identifier'): at most one of 'organization_default', 'project_default' could be set.
        :param inbound_default_policy: Default policy for inbound rules.
        :param outbound_default_policy: Default policy for outbound rules.
        :param enable_default_security: True to block SMTP on IPv4 and IPv6. This feature is read only, please open a support ticket if you need to make it configurable.
        :return: :class:`CreateSecurityGroupResponse <CreateSecurityGroupResponse>`

        Usage:
        ::

            result = await api.create_security_group(
                description="example",
                stateful=false,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/security_groups",
            body=marshal_CreateSecurityGroupRequest(
                CreateSecurityGroupRequest(
                    description=description,
                    stateful=stateful,
                    zone=zone,
                    name=name or random_name(prefix="sg"),
                    tags=tags,
                    inbound_default_policy=inbound_default_policy,
                    outbound_default_policy=outbound_default_policy,
                    enable_default_security=enable_default_security,
                    project=project,
                    organization=organization,
                    organization_default=organization_default,
                    project_default=project_default,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateSecurityGroupResponse(res.json())

    async def get_security_group(
        self,
        *,
        security_group_id: str,
        zone: Optional[Zone] = None,
    ) -> GetSecurityGroupResponse:
        """
        Get a security group.
        Get the details of a security group with the specified ID.
        :param security_group_id: UUID of the security group you want to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GetSecurityGroupResponse <GetSecurityGroupResponse>`

        Usage:
        ::

            result = await api.get_security_group(
                security_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_security_group_id = validate_path_param(
            "security_group_id", security_group_id
        )

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/security_groups/{param_security_group_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetSecurityGroupResponse(res.json())

    async def delete_security_group(
        self,
        *,
        security_group_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a security group.
        Delete a security group with the specified ID.
        :param security_group_id: UUID of the security group you want to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_security_group(
                security_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_security_group_id = validate_path_param(
            "security_group_id", security_group_id
        )

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/security_groups/{param_security_group_id}",
        )

        self._throw_on_error(res)

    async def _set_security_group(
        self,
        *,
        zone: Optional[Zone] = None,
        id: str,
        name: str,
        description: str,
        enable_default_security: bool,
        tags: Optional[List[str]] = None,
        creation_date: Optional[datetime] = None,
        modification_date: Optional[datetime] = None,
        project_default: bool,
        stateful: bool,
        inbound_default_policy: Optional[SecurityGroupPolicy] = None,
        outbound_default_policy: Optional[SecurityGroupPolicy] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        organization_default: Optional[bool] = None,
        servers: Optional[List[ServerSummary]] = None,
    ) -> _SetSecurityGroupResponse:
        """
        Update a security group.
        Replace all security group properties with a security group message.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param id: UUID of the security group.
        :param name: Name of the security group.
        :param description: Description of the security group.
        :param enable_default_security: True to block SMTP on IPv4 and IPv6. This feature is read only, please open a support ticket if you need to make it configurable.
        :param tags: Tags of the security group.
        :param creation_date: Creation date of the security group (will be ignored).
        :param modification_date: Modification date of the security group (will be ignored).
        :param project_default: True use this security group for future Instances created in this project.
        :param stateful: True to set the security group as stateful.
        :param inbound_default_policy: Default inbound policy.
        :param outbound_default_policy: Default outbound policy.
        :param organization: Security groups Organization ID.
        :param project: Security group Project ID.
        :param organization_default: Please use project_default instead.
        :param servers: Instances attached to this security group.
        :return: :class:`_SetSecurityGroupResponse <_SetSecurityGroupResponse>`

        Usage:
        ::

            result = await api._set_security_group(
                id="example",
                name="example",
                description="example",
                enable_default_security=False,
                project_default=False,
                stateful=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_id = validate_path_param("id", id)

        res = self._request(
            "PUT",
            f"/instance/v1/zones/{param_zone}/security_groups/{param_id}",
            body=marshal__SetSecurityGroupRequest(
                _SetSecurityGroupRequest(
                    zone=zone,
                    id=id,
                    name=name,
                    description=description,
                    enable_default_security=enable_default_security,
                    tags=tags,
                    creation_date=creation_date,
                    modification_date=modification_date,
                    project_default=project_default,
                    stateful=stateful,
                    inbound_default_policy=inbound_default_policy,
                    outbound_default_policy=outbound_default_policy,
                    organization=organization,
                    project=project,
                    organization_default=organization_default,
                    servers=servers,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal__SetSecurityGroupResponse(res.json())

    async def update_security_group(
        self,
        *,
        security_group_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        enable_default_security: Optional[bool] = None,
        inbound_default_policy: Optional[SecurityGroupPolicy] = None,
        tags: Optional[List[str]] = None,
        organization_default: Optional[bool] = None,
        project_default: Optional[bool] = None,
        outbound_default_policy: Optional[SecurityGroupPolicy] = None,
        stateful: Optional[bool] = None,
    ) -> UpdateSecurityGroupResponse:
        """
        Update a security group.
        Update the properties of security group.
        :param security_group_id: UUID of the security group.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the security group.
        :param description: Description of the security group.
        :param enable_default_security: True to block SMTP on IPv4 and IPv6. This feature is read only, please open a support ticket if you need to make it configurable.
        :param inbound_default_policy: Default inbound policy.
        :param tags: Tags of the security group.
        :param organization_default: Please use project_default instead.
        :param project_default: True use this security group for future Instances created in this project.
        :param outbound_default_policy: Default outbound policy.
        :param stateful: True to set the security group as stateful.
        :return: :class:`UpdateSecurityGroupResponse <UpdateSecurityGroupResponse>`

        Usage:
        ::

            result = await api.update_security_group(
                security_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_security_group_id = validate_path_param(
            "security_group_id", security_group_id
        )

        res = self._request(
            "PATCH",
            f"/instance/v1/zones/{param_zone}/security_groups/{param_security_group_id}",
            body=marshal_UpdateSecurityGroupRequest(
                UpdateSecurityGroupRequest(
                    security_group_id=security_group_id,
                    zone=zone,
                    name=name,
                    description=description,
                    enable_default_security=enable_default_security,
                    inbound_default_policy=inbound_default_policy,
                    tags=tags,
                    organization_default=organization_default,
                    project_default=project_default,
                    outbound_default_policy=outbound_default_policy,
                    stateful=stateful,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_UpdateSecurityGroupResponse(res.json())

    async def list_default_security_group_rules(
        self,
        *,
        zone: Optional[Zone] = None,
    ) -> ListSecurityGroupRulesResponse:
        """
        Get default rules.
        Lists the default rules applied to all the security groups.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ListSecurityGroupRulesResponse <ListSecurityGroupRulesResponse>`

        Usage:
        ::

            result = await api.list_default_security_group_rules()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/security_groups/default/rules",
        )

        self._throw_on_error(res)
        return unmarshal_ListSecurityGroupRulesResponse(res.json())

    async def list_security_group_rules(
        self,
        *,
        security_group_id: str,
        zone: Optional[Zone] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListSecurityGroupRulesResponse:
        """
        List rules.
        List the rules of the a specified security group ID.
        :param security_group_id: UUID of the security group.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :return: :class:`ListSecurityGroupRulesResponse <ListSecurityGroupRulesResponse>`

        Usage:
        ::

            result = await api.list_security_group_rules(
                security_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_security_group_id = validate_path_param(
            "security_group_id", security_group_id
        )

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/security_groups/{param_security_group_id}/rules",
            params={
                "page": page,
                "per_page": per_page or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSecurityGroupRulesResponse(res.json())

    async def list_security_group_rules_all(
        self,
        *,
        security_group_id: str,
        zone: Optional[Zone] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[SecurityGroupRule]:
        """
        List rules.
        List the rules of the a specified security group ID.
        :param security_group_id: UUID of the security group.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :return: :class:`List[SecurityGroupRule] <List[SecurityGroupRule]>`

        Usage:
        ::

            result = await api.list_security_group_rules_all(
                security_group_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListSecurityGroupRulesResponse,
            key="rules",
            fetcher=self.list_security_group_rules,
            args={
                "security_group_id": security_group_id,
                "zone": zone,
                "per_page": per_page,
                "page": page,
            },
        )

    async def create_security_group_rule(
        self,
        *,
        security_group_id: str,
        protocol: SecurityGroupRuleProtocol,
        direction: SecurityGroupRuleDirection,
        action: SecurityGroupRuleAction,
        ip_range: str,
        position: int,
        editable: bool,
        zone: Optional[Zone] = None,
        dest_port_from: Optional[int] = None,
        dest_port_to: Optional[int] = None,
    ) -> CreateSecurityGroupRuleResponse:
        """
        Create rule.
        Create a rule in the specified security group ID.
        :param security_group_id: UUID of the security group.
        :param protocol:
        :param direction:
        :param action:
        :param ip_range:
        :param position: Position of this rule in the security group rules list.
        :param editable: Indicates if this rule is editable (will be ignored).
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param dest_port_from: Beginning of the range of ports to apply this rule to (inclusive).
        :param dest_port_to: End of the range of ports to apply this rule to (inclusive).
        :return: :class:`CreateSecurityGroupRuleResponse <CreateSecurityGroupRuleResponse>`

        Usage:
        ::

            result = await api.create_security_group_rule(
                security_group_id="example",
                protocol=SecurityGroupRuleProtocol.unknown_protocol,
                direction=SecurityGroupRuleDirection.unknown_direction,
                action=SecurityGroupRuleAction.unknown_action,
                ip_range="example",
                position=1,
                editable=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_security_group_id = validate_path_param(
            "security_group_id", security_group_id
        )

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/security_groups/{param_security_group_id}/rules",
            body=marshal_CreateSecurityGroupRuleRequest(
                CreateSecurityGroupRuleRequest(
                    security_group_id=security_group_id,
                    protocol=protocol,
                    direction=direction,
                    action=action,
                    ip_range=ip_range,
                    position=position,
                    editable=editable,
                    zone=zone,
                    dest_port_from=dest_port_from,
                    dest_port_to=dest_port_to,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateSecurityGroupRuleResponse(res.json())

    async def set_security_group_rules(
        self,
        *,
        security_group_id: str,
        zone: Optional[Zone] = None,
        rules: Optional[List[SetSecurityGroupRulesRequestRule]] = None,
    ) -> SetSecurityGroupRulesResponse:
        """
        Update all the rules of a security group.
        Replaces the existing rules of the security group with the rules provided. This endpoint supports the update of existing rules, creation of new rules and deletion of existing rules when they are not passed in the request.
        :param security_group_id: UUID of the security group to update the rules on.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param rules: List of rules to update in the security group.
        :return: :class:`SetSecurityGroupRulesResponse <SetSecurityGroupRulesResponse>`

        Usage:
        ::

            result = await api.set_security_group_rules(
                security_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_security_group_id = validate_path_param(
            "security_group_id", security_group_id
        )

        res = self._request(
            "PUT",
            f"/instance/v1/zones/{param_zone}/security_groups/{param_security_group_id}/rules",
            body=marshal_SetSecurityGroupRulesRequest(
                SetSecurityGroupRulesRequest(
                    security_group_id=security_group_id,
                    zone=zone,
                    rules=rules,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetSecurityGroupRulesResponse(res.json())

    async def delete_security_group_rule(
        self,
        *,
        security_group_id: str,
        security_group_rule_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete rule.
        Delete a security group rule with the specified ID.
        :param security_group_id:
        :param security_group_rule_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_security_group_rule(
                security_group_id="example",
                security_group_rule_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_security_group_id = validate_path_param(
            "security_group_id", security_group_id
        )
        param_security_group_rule_id = validate_path_param(
            "security_group_rule_id", security_group_rule_id
        )

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/security_groups/{param_security_group_id}/rules/{param_security_group_rule_id}",
        )

        self._throw_on_error(res)

    async def get_security_group_rule(
        self,
        *,
        security_group_id: str,
        security_group_rule_id: str,
        zone: Optional[Zone] = None,
    ) -> GetSecurityGroupRuleResponse:
        """
        Get rule.
        Get details of a security group rule with the specified ID.
        :param security_group_id:
        :param security_group_rule_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GetSecurityGroupRuleResponse <GetSecurityGroupRuleResponse>`

        Usage:
        ::

            result = await api.get_security_group_rule(
                security_group_id="example",
                security_group_rule_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_security_group_id = validate_path_param(
            "security_group_id", security_group_id
        )
        param_security_group_rule_id = validate_path_param(
            "security_group_rule_id", security_group_rule_id
        )

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/security_groups/{param_security_group_id}/rules/{param_security_group_rule_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetSecurityGroupRuleResponse(res.json())

    async def _set_security_group_rule(
        self,
        *,
        security_group_id: str,
        security_group_rule_id: str,
        id: str,
        ip_range: str,
        position: int,
        editable: bool,
        zone: Optional[Zone] = None,
        protocol: Optional[SecurityGroupRuleProtocol] = None,
        direction: Optional[SecurityGroupRuleDirection] = None,
        action: Optional[SecurityGroupRuleAction] = None,
        dest_port_from: Optional[int] = None,
        dest_port_to: Optional[int] = None,
    ) -> _SetSecurityGroupRuleResponse:
        """
        Set security group rule.
        Replace all the properties of a rule from a specified security group.
        :param security_group_id:
        :param security_group_rule_id:
        :param id:
        :param ip_range:
        :param position:
        :param editable:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param protocol:
        :param direction:
        :param action:
        :param dest_port_from:
        :param dest_port_to:
        :return: :class:`_SetSecurityGroupRuleResponse <_SetSecurityGroupRuleResponse>`

        Usage:
        ::

            result = await api._set_security_group_rule(
                security_group_id="example",
                security_group_rule_id="example",
                id="example",
                ip_range="example",
                position=1,
                editable=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_security_group_id = validate_path_param(
            "security_group_id", security_group_id
        )
        param_security_group_rule_id = validate_path_param(
            "security_group_rule_id", security_group_rule_id
        )

        res = self._request(
            "PUT",
            f"/instance/v1/zones/{param_zone}/security_groups/{param_security_group_id}/rules/{param_security_group_rule_id}",
            body=marshal__SetSecurityGroupRuleRequest(
                _SetSecurityGroupRuleRequest(
                    security_group_id=security_group_id,
                    security_group_rule_id=security_group_rule_id,
                    id=id,
                    ip_range=ip_range,
                    position=position,
                    editable=editable,
                    zone=zone,
                    protocol=protocol,
                    direction=direction,
                    action=action,
                    dest_port_from=dest_port_from,
                    dest_port_to=dest_port_to,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal__SetSecurityGroupRuleResponse(res.json())

    async def update_security_group_rule(
        self,
        *,
        security_group_id: str,
        security_group_rule_id: str,
        zone: Optional[Zone] = None,
        protocol: Optional[SecurityGroupRuleProtocol] = None,
        direction: Optional[SecurityGroupRuleDirection] = None,
        action: Optional[SecurityGroupRuleAction] = None,
        ip_range: Optional[str] = None,
        dest_port_from: Optional[int] = None,
        dest_port_to: Optional[int] = None,
        position: Optional[int] = None,
    ) -> UpdateSecurityGroupRuleResponse:
        """
        Update security group rule.
        Update the properties of a rule from a specified security group.
        :param security_group_id: UUID of the security group.
        :param security_group_rule_id: UUID of the rule.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param protocol: Protocol family this rule applies to.
        :param direction: Direction the rule applies to.
        :param action: Action to apply when the rule matches a packet.
        :param ip_range: Range of IP addresses these rules apply to.
        :param dest_port_from: Beginning of the range of ports this rule applies to (inclusive). If 0 is provided, unset the parameter.
        :param dest_port_to: End of the range of ports this rule applies to (inclusive). If 0 is provided, unset the parameter.
        :param position: Position of this rule in the security group rules list.
        :return: :class:`UpdateSecurityGroupRuleResponse <UpdateSecurityGroupRuleResponse>`

        Usage:
        ::

            result = await api.update_security_group_rule(
                security_group_id="example",
                security_group_rule_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_security_group_id = validate_path_param(
            "security_group_id", security_group_id
        )
        param_security_group_rule_id = validate_path_param(
            "security_group_rule_id", security_group_rule_id
        )

        res = self._request(
            "PATCH",
            f"/instance/v1/zones/{param_zone}/security_groups/{param_security_group_id}/rules/{param_security_group_rule_id}",
            body=marshal_UpdateSecurityGroupRuleRequest(
                UpdateSecurityGroupRuleRequest(
                    security_group_id=security_group_id,
                    security_group_rule_id=security_group_rule_id,
                    zone=zone,
                    protocol=protocol,
                    direction=direction,
                    action=action,
                    ip_range=ip_range,
                    dest_port_from=dest_port_from,
                    dest_port_to=dest_port_to,
                    position=position,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_UpdateSecurityGroupRuleResponse(res.json())

    async def list_placement_groups(
        self,
        *,
        zone: Optional[Zone] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
    ) -> ListPlacementGroupsResponse:
        """
        List placement groups.
        List all placement groups in a specified Availability Zone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :param organization: List only placement groups of this Organization ID.
        :param project: List only placement groups of this Project ID.
        :param tags: List placement groups with these exact tags (to filter with several tags, use commas to separate them).
        :param name: Filter placement groups by name (for eg. "cluster1" will return "cluster100" and "cluster1" but not "foo").
        :return: :class:`ListPlacementGroupsResponse <ListPlacementGroupsResponse>`

        Usage:
        ::

            result = await api.list_placement_groups()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/placement_groups",
            params={
                "name": name,
                "organization": organization or self.client.default_organization_id,
                "page": page,
                "per_page": per_page or self.client.default_page_size,
                "project": project or self.client.default_project_id,
                "tags": ",".join(tags) if tags and len(tags) > 0 else None,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPlacementGroupsResponse(res.json())

    async def list_placement_groups_all(
        self,
        *,
        zone: Optional[Zone] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
    ) -> List[PlacementGroup]:
        """
        List placement groups.
        List all placement groups in a specified Availability Zone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :param organization: List only placement groups of this Organization ID.
        :param project: List only placement groups of this Project ID.
        :param tags: List placement groups with these exact tags (to filter with several tags, use commas to separate them).
        :param name: Filter placement groups by name (for eg. "cluster1" will return "cluster100" and "cluster1" but not "foo").
        :return: :class:`List[PlacementGroup] <List[PlacementGroup]>`

        Usage:
        ::

            result = await api.list_placement_groups_all()
        """

        return await fetch_all_pages_async(
            type=ListPlacementGroupsResponse,
            key="placement_groups",
            fetcher=self.list_placement_groups,
            args={
                "zone": zone,
                "per_page": per_page,
                "page": page,
                "organization": organization,
                "project": project,
                "tags": tags,
                "name": name,
            },
        )

    async def create_placement_group(
        self,
        *,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        policy_mode: Optional[PlacementGroupPolicyMode] = None,
        policy_type: Optional[PlacementGroupPolicyType] = None,
    ) -> CreatePlacementGroupResponse:
        """
        Create a placement group.
        Create a new placement group in a specified Availability Zone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the placement group.
        :param organization: Organization ID of the placement group.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param project: Project ID of the placement group.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param tags: Tags of the placement group.
        :param policy_mode: Operating mode of the placement group.
        :param policy_type: Policy type of the placement group.
        :return: :class:`CreatePlacementGroupResponse <CreatePlacementGroupResponse>`

        Usage:
        ::

            result = await api.create_placement_group()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/placement_groups",
            body=marshal_CreatePlacementGroupRequest(
                CreatePlacementGroupRequest(
                    zone=zone,
                    name=name or random_name(prefix="pg"),
                    tags=tags,
                    policy_mode=policy_mode,
                    policy_type=policy_type,
                    project=project,
                    organization=organization,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreatePlacementGroupResponse(res.json())

    async def get_placement_group(
        self,
        *,
        placement_group_id: str,
        zone: Optional[Zone] = None,
    ) -> GetPlacementGroupResponse:
        """
        Get a placement group.
        Get the specified placement group.
        :param placement_group_id: UUID of the placement group you want to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GetPlacementGroupResponse <GetPlacementGroupResponse>`

        Usage:
        ::

            result = await api.get_placement_group(
                placement_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_placement_group_id = validate_path_param(
            "placement_group_id", placement_group_id
        )

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/placement_groups/{param_placement_group_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetPlacementGroupResponse(res.json())

    async def set_placement_group(
        self,
        *,
        placement_group_id: str,
        name: str,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        policy_mode: Optional[PlacementGroupPolicyMode] = None,
        policy_type: Optional[PlacementGroupPolicyType] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> SetPlacementGroupResponse:
        """
        Set placement group.
        Set all parameters of the specified placement group.
        :param placement_group_id:
        :param name:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param organization:
        :param policy_mode:
        :param policy_type:
        :param project:
        :param tags:
        :return: :class:`SetPlacementGroupResponse <SetPlacementGroupResponse>`

        Usage:
        ::

            result = await api.set_placement_group(
                placement_group_id="example",
                name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_placement_group_id = validate_path_param(
            "placement_group_id", placement_group_id
        )

        res = self._request(
            "PUT",
            f"/instance/v1/zones/{param_zone}/placement_groups/{param_placement_group_id}",
            body=marshal_SetPlacementGroupRequest(
                SetPlacementGroupRequest(
                    placement_group_id=placement_group_id,
                    name=name,
                    zone=zone,
                    organization=organization,
                    policy_mode=policy_mode,
                    policy_type=policy_type,
                    project=project,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetPlacementGroupResponse(res.json())

    async def update_placement_group(
        self,
        *,
        placement_group_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        policy_mode: Optional[PlacementGroupPolicyMode] = None,
        policy_type: Optional[PlacementGroupPolicyType] = None,
    ) -> UpdatePlacementGroupResponse:
        """
        Update a placement group.
        Update one or more parameter of the specified placement group.
        :param placement_group_id: UUID of the placement group.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the placement group.
        :param tags: Tags of the placement group.
        :param policy_mode: Operating mode of the placement group.
        :param policy_type: Policy type of the placement group.
        :return: :class:`UpdatePlacementGroupResponse <UpdatePlacementGroupResponse>`

        Usage:
        ::

            result = await api.update_placement_group(
                placement_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_placement_group_id = validate_path_param(
            "placement_group_id", placement_group_id
        )

        res = self._request(
            "PATCH",
            f"/instance/v1/zones/{param_zone}/placement_groups/{param_placement_group_id}",
            body=marshal_UpdatePlacementGroupRequest(
                UpdatePlacementGroupRequest(
                    placement_group_id=placement_group_id,
                    zone=zone,
                    name=name,
                    tags=tags,
                    policy_mode=policy_mode,
                    policy_type=policy_type,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_UpdatePlacementGroupResponse(res.json())

    async def delete_placement_group(
        self,
        *,
        placement_group_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete the specified placement group.
        :param placement_group_id: UUID of the placement group you want to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_placement_group(
                placement_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_placement_group_id = validate_path_param(
            "placement_group_id", placement_group_id
        )

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/placement_groups/{param_placement_group_id}",
        )

        self._throw_on_error(res)

    async def get_placement_group_servers(
        self,
        *,
        placement_group_id: str,
        zone: Optional[Zone] = None,
    ) -> GetPlacementGroupServersResponse:
        """
        Get placement group servers.
        Get all Instances belonging to the specified placement group.
        :param placement_group_id: UUID of the placement group you want to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GetPlacementGroupServersResponse <GetPlacementGroupServersResponse>`

        Usage:
        ::

            result = await api.get_placement_group_servers(
                placement_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_placement_group_id = validate_path_param(
            "placement_group_id", placement_group_id
        )

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/placement_groups/{param_placement_group_id}/servers",
        )

        self._throw_on_error(res)
        return unmarshal_GetPlacementGroupServersResponse(res.json())

    async def set_placement_group_servers(
        self,
        *,
        placement_group_id: str,
        servers: List[str],
        zone: Optional[Zone] = None,
    ) -> SetPlacementGroupServersResponse:
        """
        Set placement group servers.
        Set all Instances belonging to the specified placement group.
        :param placement_group_id: UUID of the placement group you want to set.
        :param servers: An array of the Instances' UUIDs you want to configure.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`SetPlacementGroupServersResponse <SetPlacementGroupServersResponse>`

        Usage:
        ::

            result = await api.set_placement_group_servers(
                placement_group_id="example",
                servers=[],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_placement_group_id = validate_path_param(
            "placement_group_id", placement_group_id
        )

        res = self._request(
            "PUT",
            f"/instance/v1/zones/{param_zone}/placement_groups/{param_placement_group_id}/servers",
            body=marshal_SetPlacementGroupServersRequest(
                SetPlacementGroupServersRequest(
                    placement_group_id=placement_group_id,
                    servers=servers,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetPlacementGroupServersResponse(res.json())

    async def update_placement_group_servers(
        self,
        *,
        placement_group_id: str,
        servers: List[str],
        zone: Optional[Zone] = None,
    ) -> UpdatePlacementGroupServersResponse:
        """
        Update placement group servers.
        Update all Instances belonging to the specified placement group.
        :param placement_group_id: UUID of the placement group you want to update.
        :param servers: An array of the Instances' UUIDs you want to configure.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`UpdatePlacementGroupServersResponse <UpdatePlacementGroupServersResponse>`

        Usage:
        ::

            result = await api.update_placement_group_servers(
                placement_group_id="example",
                servers=[],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_placement_group_id = validate_path_param(
            "placement_group_id", placement_group_id
        )

        res = self._request(
            "PATCH",
            f"/instance/v1/zones/{param_zone}/placement_groups/{param_placement_group_id}/servers",
            body=marshal_UpdatePlacementGroupServersRequest(
                UpdatePlacementGroupServersRequest(
                    placement_group_id=placement_group_id,
                    servers=servers,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_UpdatePlacementGroupServersResponse(res.json())

    async def list_ips(
        self,
        *,
        zone: Optional[Zone] = None,
        project: Optional[str] = None,
        organization: Optional[str] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        type_: Optional[str] = None,
    ) -> ListIpsResponse:
        """
        List all flexible IPs.
        List all flexible IPs in a specified zone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project: Project ID in which the IPs are reserved.
        :param organization: Organization ID in which the IPs are reserved.
        :param tags: Filter IPs with these exact tags (to filter with several tags, use commas to separate them).
        :param name: Filter on the IP address (Works as a LIKE operation on the IP address).
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :param type_: Filter on the IP Mobility IP type (whose value should be either 'routed_ipv4', 'routed_ipv6' or 'nat').
        :return: :class:`ListIpsResponse <ListIpsResponse>`

        Usage:
        ::

            result = await api.list_ips()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/ips",
            params={
                "name": name,
                "organization": organization or self.client.default_organization_id,
                "page": page,
                "per_page": per_page or self.client.default_page_size,
                "project": project or self.client.default_project_id,
                "tags": ",".join(tags) if tags and len(tags) > 0 else None,
                "type": type_,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListIpsResponse(res.json())

    async def list_ips_all(
        self,
        *,
        zone: Optional[Zone] = None,
        project: Optional[str] = None,
        organization: Optional[str] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        type_: Optional[str] = None,
    ) -> List[Ip]:
        """
        List all flexible IPs.
        List all flexible IPs in a specified zone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project: Project ID in which the IPs are reserved.
        :param organization: Organization ID in which the IPs are reserved.
        :param tags: Filter IPs with these exact tags (to filter with several tags, use commas to separate them).
        :param name: Filter on the IP address (Works as a LIKE operation on the IP address).
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :param type_: Filter on the IP Mobility IP type (whose value should be either 'routed_ipv4', 'routed_ipv6' or 'nat').
        :return: :class:`List[Ip] <List[Ip]>`

        Usage:
        ::

            result = await api.list_ips_all()
        """

        return await fetch_all_pages_async(
            type=ListIpsResponse,
            key="ips",
            fetcher=self.list_ips,
            args={
                "zone": zone,
                "project": project,
                "organization": organization,
                "tags": tags,
                "name": name,
                "per_page": per_page,
                "page": page,
                "type_": type_,
            },
        )

    async def create_ip(
        self,
        *,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        server: Optional[str] = None,
        type_: Optional[IpType] = None,
    ) -> CreateIpResponse:
        """
        Reserve a flexible IP.
        Reserve a flexible IP and attach it to the specified Instance.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param organization: Organization ID in which the IP is reserved.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param project: Project ID in which the IP is reserved.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param tags: Tags of the IP.
        :param server: UUID of the Instance you want to attach the IP to.
        :param type_: IP type to reserve (either 'routed_ipv4' or 'routed_ipv6', use of 'nat' is deprecated).
        :return: :class:`CreateIpResponse <CreateIpResponse>`

        Usage:
        ::

            result = await api.create_ip()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/ips",
            body=marshal_CreateIpRequest(
                CreateIpRequest(
                    zone=zone,
                    tags=tags,
                    server=server,
                    type_=type_,
                    project=project,
                    organization=organization,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateIpResponse(res.json())

    async def get_ip(
        self,
        *,
        ip: str,
        zone: Optional[Zone] = None,
    ) -> GetIpResponse:
        """
        Get a flexible IP.
        Get details of an IP with the specified ID or address.
        :param ip: IP ID or address to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GetIpResponse <GetIpResponse>`

        Usage:
        ::

            result = await api.get_ip(
                ip="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip = validate_path_param("ip", ip)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/ips/{param_ip}",
        )

        self._throw_on_error(res)
        return unmarshal_GetIpResponse(res.json())

    async def update_ip(
        self,
        *,
        ip: str,
        zone: Optional[Zone] = None,
        reverse: Optional[str] = None,
        type_: Optional[IpType] = None,
        tags: Optional[List[str]] = None,
        server: Optional[str] = None,
    ) -> UpdateIpResponse:
        """
        Update a flexible IP.
        Update a flexible IP in the specified zone with the specified ID.
        :param ip: IP ID or IP address.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param reverse: Reverse domain name.
        :param type_: Convert a 'nat' IP to a 'routed_ipv4'.
        :param tags: An array of keywords you want to tag this IP with.
        :param server:
        :return: :class:`UpdateIpResponse <UpdateIpResponse>`

        Usage:
        ::

            result = await api.update_ip(
                ip="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip = validate_path_param("ip", ip)

        res = self._request(
            "PATCH",
            f"/instance/v1/zones/{param_zone}/ips/{param_ip}",
            body=marshal_UpdateIpRequest(
                UpdateIpRequest(
                    ip=ip,
                    zone=zone,
                    reverse=reverse,
                    type_=type_,
                    tags=tags,
                    server=server,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_UpdateIpResponse(res.json())

    async def delete_ip(
        self,
        *,
        ip: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a flexible IP.
        Delete the IP with the specified ID.
        :param ip: ID or address of the IP to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_ip(
                ip="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip = validate_path_param("ip", ip)

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/ips/{param_ip}",
        )

        self._throw_on_error(res)

    async def list_private_ni_cs(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        tags: Optional[List[str]] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListPrivateNICsResponse:
        """
        List all private NICs.
        List all private NICs of a specified Instance.
        :param server_id: Instance to which the private NIC is attached.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param tags: Private NIC tags.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :return: :class:`ListPrivateNICsResponse <ListPrivateNICsResponse>`

        Usage:
        ::

            result = await api.list_private_ni_cs(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/private_nics",
            params={
                "page": page,
                "per_page": per_page or self.client.default_page_size,
                "tags": ",".join(tags) if tags and len(tags) > 0 else None,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPrivateNICsResponse(res.json())

    async def list_private_ni_cs_all(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        tags: Optional[List[str]] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[PrivateNIC]:
        """
        List all private NICs.
        List all private NICs of a specified Instance.
        :param server_id: Instance to which the private NIC is attached.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param tags: Private NIC tags.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return.
        :param page: A positive integer to choose the page to return.
        :return: :class:`List[PrivateNIC] <List[PrivateNIC]>`

        Usage:
        ::

            result = await api.list_private_ni_cs_all(
                server_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListPrivateNICsResponse,
            key="private_nics",
            fetcher=self.list_private_ni_cs,
            args={
                "server_id": server_id,
                "zone": zone,
                "tags": tags,
                "per_page": per_page,
                "page": page,
            },
        )

    async def create_private_nic(
        self,
        *,
        server_id: str,
        private_network_id: str,
        zone: Optional[Zone] = None,
        tags: Optional[List[str]] = None,
        ip_ids: Optional[List[str]] = None,
        ipam_ip_ids: Optional[List[str]] = None,
    ) -> CreatePrivateNICResponse:
        """
        Create a private NIC connecting an Instance to a Private Network.
        :param server_id: UUID of the Instance the private NIC will be attached to.
        :param private_network_id: UUID of the private network where the private NIC will be attached.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param tags: Private NIC tags.
        :param ip_ids: Ip_ids defined from IPAM.
        :param ipam_ip_ids: UUID of IPAM ips, to be attached to the instance in the requested private network.
        :return: :class:`CreatePrivateNICResponse <CreatePrivateNICResponse>`

        Usage:
        ::

            result = await api.create_private_nic(
                server_id="example",
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/private_nics",
            body=marshal_CreatePrivateNICRequest(
                CreatePrivateNICRequest(
                    server_id=server_id,
                    private_network_id=private_network_id,
                    zone=zone,
                    tags=tags,
                    ip_ids=ip_ids,
                    ipam_ip_ids=ipam_ip_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreatePrivateNICResponse(res.json())

    async def get_private_nic(
        self,
        *,
        server_id: str,
        private_nic_id: str,
        zone: Optional[Zone] = None,
    ) -> GetPrivateNICResponse:
        """
        Get a private NIC.
        Get private NIC properties.
        :param server_id: Instance to which the private NIC is attached.
        :param private_nic_id: Private NIC unique ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GetPrivateNICResponse <GetPrivateNICResponse>`

        Usage:
        ::

            result = await api.get_private_nic(
                server_id="example",
                private_nic_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_private_nic_id = validate_path_param("private_nic_id", private_nic_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/private_nics/{param_private_nic_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetPrivateNICResponse(res.json())

    async def update_private_nic(
        self,
        *,
        server_id: str,
        private_nic_id: str,
        zone: Optional[Zone] = None,
        tags: Optional[List[str]] = None,
    ) -> PrivateNIC:
        """
        Update a private NIC.
        Update one or more parameter(s) of a specified private NIC.
        :param server_id: UUID of the Instance the private NIC will be attached to.
        :param private_nic_id: Private NIC unique ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param tags: Tags used to select private NIC/s.
        :return: :class:`PrivateNIC <PrivateNIC>`

        Usage:
        ::

            result = await api.update_private_nic(
                server_id="example",
                private_nic_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_private_nic_id = validate_path_param("private_nic_id", private_nic_id)

        res = self._request(
            "PATCH",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/private_nics/{param_private_nic_id}",
            body=marshal_UpdatePrivateNICRequest(
                UpdatePrivateNICRequest(
                    server_id=server_id,
                    private_nic_id=private_nic_id,
                    zone=zone,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNIC(res.json())

    async def delete_private_nic(
        self,
        *,
        server_id: str,
        private_nic_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a private NIC.
        :param server_id: Instance to which the private NIC is attached.
        :param private_nic_id: Private NIC unique ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = await api.delete_private_nic(
                server_id="example",
                private_nic_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_private_nic_id = validate_path_param("private_nic_id", private_nic_id)

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/private_nics/{param_private_nic_id}",
        )

        self._throw_on_error(res)

    async def list_bootscripts(
        self,
        *,
        zone: Optional[Zone] = None,
        arch: Optional[str] = None,
        title: Optional[str] = None,
        default: Optional[bool] = None,
        public: Optional[bool] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListBootscriptsResponse:
        """
        List bootscripts.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param arch:
        :param title:
        :param default:
        :param public:
        :param per_page:
        :param page:
        :return: :class:`ListBootscriptsResponse <ListBootscriptsResponse>`
        :deprecated

        Usage:
        ::

            result = await api.list_bootscripts()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/bootscripts",
            params={
                "arch": arch,
                "default": default,
                "page": page,
                "per_page": per_page or self.client.default_page_size,
                "public": public,
                "title": title,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBootscriptsResponse(res.json())

    async def list_bootscripts_all(
        self,
        *,
        zone: Optional[Zone] = None,
        arch: Optional[str] = None,
        title: Optional[str] = None,
        default: Optional[bool] = None,
        public: Optional[bool] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[Bootscript]:
        """
        List bootscripts.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param arch:
        :param title:
        :param default:
        :param public:
        :param per_page:
        :param page:
        :return: :class:`List[Bootscript] <List[Bootscript]>`
        :deprecated

        Usage:
        ::

            result = await api.list_bootscripts_all()
        """

        return await fetch_all_pages_async(
            type=ListBootscriptsResponse,
            key="bootscripts",
            fetcher=self.list_bootscripts,
            args={
                "zone": zone,
                "arch": arch,
                "title": title,
                "default": default,
                "public": public,
                "per_page": per_page,
                "page": page,
            },
        )

    async def get_bootscript(
        self,
        *,
        bootscript_id: str,
        zone: Optional[Zone] = None,
    ) -> GetBootscriptResponse:
        """
        Get bootscripts.
        Get details of a bootscript with the specified ID.
        :param bootscript_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GetBootscriptResponse <GetBootscriptResponse>`
        :deprecated

        Usage:
        ::

            result = await api.get_bootscript(
                bootscript_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_bootscript_id = validate_path_param("bootscript_id", bootscript_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/bootscripts/{param_bootscript_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetBootscriptResponse(res.json())

    async def get_dashboard(
        self,
        *,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
    ) -> GetDashboardResponse:
        """
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param organization:
        :param project:
        :return: :class:`GetDashboardResponse <GetDashboardResponse>`

        Usage:
        ::

            result = await api.get_dashboard()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/dashboard",
            params={
                "organization": organization or self.client.default_organization_id,
                "project": project or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GetDashboardResponse(res.json())

    async def plan_block_migration(
        self,
        *,
        zone: Optional[Zone] = None,
        volume_id: Optional[str] = None,
        snapshot_id: Optional[str] = None,
    ) -> MigrationPlan:
        """
        Get a volume or snapshot's migration plan.
        Given a volume or snapshot, returns the migration plan for a call to the "Apply a migration plan" endpoint. This plan will include zero or one volume, and zero or more snapshots, which will need to be migrated together. This endpoint does not perform the actual migration itself, the "Apply a migration plan" endpoint must be used. The validation_key value returned by this endpoint must be provided to the call to the "Apply a migration plan" endpoint to confirm that all resources listed in the plan should be migrated.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param volume_id: The volume for which the migration plan will be generated.
        One-Of ('resource'): at most one of 'volume_id', 'snapshot_id' could be set.
        :param snapshot_id: The snapshot for which the migration plan will be generated.
        One-Of ('resource'): at most one of 'volume_id', 'snapshot_id' could be set.
        :return: :class:`MigrationPlan <MigrationPlan>`

        Usage:
        ::

            result = await api.plan_block_migration()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/block-migration/plan",
            body=marshal_PlanBlockMigrationRequest(
                PlanBlockMigrationRequest(
                    zone=zone,
                    volume_id=volume_id,
                    snapshot_id=snapshot_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_MigrationPlan(res.json())

    async def apply_block_migration(
        self,
        *,
        validation_key: str,
        zone: Optional[Zone] = None,
        volume_id: Optional[str] = None,
        snapshot_id: Optional[str] = None,
    ) -> None:
        """
        Migrate a volume and/or snapshots to SBS (Scaleway Block Storage).
        To be used, the call to this endpoint must be preceded by a call to the "Plan a migration" endpoint. To migrate all resources mentioned in the migration plan, the validation_key returned in the plan must be provided.
        :param validation_key: A value to be retrieved from a call to the "Plan a migration" endpoint, to confirm that the volume and/or snapshots specified in said plan should be migrated.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param volume_id: The volume to migrate, along with potentially other resources, according to the migration plan generated with a call to the "Plan a migration" endpoint.
        One-Of ('resource'): at most one of 'volume_id', 'snapshot_id' could be set.
        :param snapshot_id: The snapshot to migrate, along with potentially other resources, according to the migration plan generated with a call to the "Plan a migration" endpoint.
        One-Of ('resource'): at most one of 'volume_id', 'snapshot_id' could be set.

        Usage:
        ::

            result = await api.apply_block_migration(
                validation_key="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/block-migration/apply",
            body=marshal_ApplyBlockMigrationRequest(
                ApplyBlockMigrationRequest(
                    validation_key=validation_key,
                    zone=zone,
                    volume_id=volume_id,
                    snapshot_id=snapshot_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
