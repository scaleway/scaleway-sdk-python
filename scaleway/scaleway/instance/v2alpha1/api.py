# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone as ScwZone,
)
from scaleway_core.utils import (
    OneOfPossibility,
    WaitForOptions,
    resolve_one_of,
    validate_path_param,
    wait_for_resource,
)
from .types import (
    CreateVolumeRequestVolumeType,
    ListPlacementGroupsRequestOrderBy,
    ListPrivateNetworkInterfacesRequestOrderBy,
    ListSecurityGroupsRequestOrderBy,
    ListServersRequestOrderBy,
    ListSnapshotsRequestOrderBy,
    ListTemplatesRequestOrderBy,
    ListVolumesRequestOrderBy,
    PlacementGroupPolicyType,
    SecurityGroupAction,
    SecurityGroupRuleAction,
    SecurityGroupRuleDirection,
    SecurityGroupRuleProtocol,
    ServerVolumeVolumeType,
    SnapshotVolumeType,
    VolumeVolumeType,
    AddSecurityGroupRulesRequest,
    AddSecurityGroupRulesResponse,
    AttachServerFileSystemRequest,
    AttachServerIPRequest,
    AttachServerPrivateNetworkInterfaceRequest,
    AttachServerVolumeRequest,
    CreatePlacementGroupRequest,
    CreatePrivateNetworkInterfaceRequest,
    CreateSecurityGroupRequest,
    CreateServerFromTemplateRequest,
    CreateServerRequest,
    CreateServerRequestPublicNetworkInterface,
    CreateServerRequestServerVolume,
    CreateTemplateRequest,
    CreateTemplateRequestPrivateNetworkTemplate,
    CreateTemplateRequestVolumeTemplate,
    DeleteSecurityGroupRulesRequest,
    DetachServerFileSystemRequest,
    DetachServerIPRequest,
    DetachServerPrivateNetworkInterfaceRequest,
    DetachServerVolumeRequest,
    ListPlacementGroupsResponse,
    ListPrivateNetworkInterfacesResponse,
    ListSecurityGroupsResponse,
    ListServerTypesResponse,
    ListServersResponse,
    ListSnapshotsResponse,
    ListTemplateUserDataKeysResponse,
    ListTemplatesResponse,
    ListUserDataKeysResponse,
    ListVolumeTypesResponse,
    ListVolumesResponse,
    PlacementGroup,
    PrivateNetworkInterface,
    ResourceCounts,
    SecurityGroup,
    SecurityGroupRuleConfig,
    SecurityGroupRulePortRange,
    Server,
    SetSecurityGroupRulesRequest,
    SetServerCloudInitRequest,
    SetServerDefaultIPRequest,
    SetTemplateCloudInitRequest,
    SetTemplateUserDataRequest,
    SetUserDataRequest,
    Snapshot,
    StopAndDeleteServerRequest,
    Template,
    UpdatePlacementGroupRequest,
    UpdatePrivateNetworkInterfaceRequest,
    UpdateSecurityGroupRequest,
    UpdateSecurityGroupRuleRequest,
    UpdateServerRequest,
    UpdateServerRequestPublicNetworkInterface,
    UpdateTemplateRequest,
    UpdateTemplateRequestUpdatePrivateNetworks,
    UpdateTemplateRequestUpdateVolumes,
    UserData,
    Volume,
    VolumeApiCreateSnapshotRequest,
    VolumeApiCreateVolumeRequest,
    VolumeApiExportSnapshotToObjectStorageRequest,
    VolumeApiImportSnapshotFromObjectStorageRequest,
    VolumeApiUpdateSnapshotRequest,
    VolumeApiUpdateVolumeRequest,
)
from .content import (
    PRIVATE_NETWORK_INTERFACE_TRANSIENT_STATUSES,
    SERVER_TRANSIENT_STATUSES,
    SNAPSHOT_TRANSIENT_STATUSES,
    VOLUME_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_SecurityGroup,
    unmarshal_PlacementGroup,
    unmarshal_Snapshot,
    unmarshal_Volume,
    unmarshal_AddSecurityGroupRulesResponse,
    unmarshal_ListPlacementGroupsResponse,
    unmarshal_ListPrivateNetworkInterfacesResponse,
    unmarshal_ListSecurityGroupsResponse,
    unmarshal_ListServerTypesResponse,
    unmarshal_ListServersResponse,
    unmarshal_ListSnapshotsResponse,
    unmarshal_ListTemplateUserDataKeysResponse,
    unmarshal_ListTemplatesResponse,
    unmarshal_ListUserDataKeysResponse,
    unmarshal_ListVolumeTypesResponse,
    unmarshal_ListVolumesResponse,
    unmarshal_PrivateNetworkInterface,
    unmarshal_ResourceCounts,
    unmarshal_Server,
    unmarshal_Template,
    unmarshal_UserData,
    marshal_AddSecurityGroupRulesRequest,
    marshal_AttachServerFileSystemRequest,
    marshal_AttachServerIPRequest,
    marshal_AttachServerPrivateNetworkInterfaceRequest,
    marshal_AttachServerVolumeRequest,
    marshal_CreatePlacementGroupRequest,
    marshal_CreatePrivateNetworkInterfaceRequest,
    marshal_CreateSecurityGroupRequest,
    marshal_CreateServerFromTemplateRequest,
    marshal_CreateServerRequest,
    marshal_CreateTemplateRequest,
    marshal_DeleteSecurityGroupRulesRequest,
    marshal_DetachServerFileSystemRequest,
    marshal_DetachServerIPRequest,
    marshal_DetachServerPrivateNetworkInterfaceRequest,
    marshal_DetachServerVolumeRequest,
    marshal_SetSecurityGroupRulesRequest,
    marshal_SetServerCloudInitRequest,
    marshal_SetServerDefaultIPRequest,
    marshal_SetTemplateCloudInitRequest,
    marshal_SetTemplateUserDataRequest,
    marshal_SetUserDataRequest,
    marshal_StopAndDeleteServerRequest,
    marshal_UpdatePlacementGroupRequest,
    marshal_UpdatePrivateNetworkInterfaceRequest,
    marshal_UpdateSecurityGroupRequest,
    marshal_UpdateSecurityGroupRuleRequest,
    marshal_UpdateServerRequest,
    marshal_UpdateTemplateRequest,
    marshal_VolumeApiCreateSnapshotRequest,
    marshal_VolumeApiCreateVolumeRequest,
    marshal_VolumeApiExportSnapshotToObjectStorageRequest,
    marshal_VolumeApiImportSnapshotFromObjectStorageRequest,
    marshal_VolumeApiUpdateSnapshotRequest,
    marshal_VolumeApiUpdateVolumeRequest,
)


class InstanceV2Alpha1API(API):
    """
    This API allows you to manage your CPU and GPU Instances.
    """

    def get_resource_counts(
        self,
        *,
        zone: Optional[ScwZone] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ResourceCounts:
        """
        Get resource counts.
        Get counts of various resources (e.g. servers, volumes).
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param organization_id: Organization ID to filter resource counts.
        One-Of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Project ID to filter resource counts.
        One-Of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :return: :class:`ResourceCounts <ResourceCounts>`

        Usage:
        ::

            result = api.get_resource_counts()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/resource-counts",
            params={
                **resolve_one_of(
                    [
                        OneOfPossibility("organization_id", organization_id),
                        OneOfPossibility("project_id", project_id),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ResourceCounts(res.json())

    def list_servers(
        self,
        *,
        zone: Optional[ScwZone] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListServersRequestOrderBy] = None,
        project_id: Optional[str] = None,
        server_ids: Optional[list[str]] = None,
        name: Optional[str] = None,
        server_type: Optional[str] = None,
        tags: Optional[list[str]] = None,
        security_group_ids: Optional[list[str]] = None,
        placement_group_ids: Optional[list[str]] = None,
        private_network_ids: Optional[list[str]] = None,
        mac_addresses: Optional[list[str]] = None,
    ) -> ListServersResponse:
        """
        List all Instances.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page_token: Token for pagination.
        :param page_size: Number of servers to return per page.
        :param order_by: Order of the returned servers.
        :param project_id: Project ID to filter servers.
        :param server_ids: List of server IDs to filter.
        :param name: Name to filter servers.
        :param server_type: Server type to filter.
        :param tags: Tags to filter servers.
        :param security_group_ids: Security group IDs to filter servers.
        :param placement_group_ids: Placement group IDs to filter servers.
        :param private_network_ids: Private Network IDs to filter servers.
        :param mac_addresses: MAC addresses to filter servers.
        :return: :class:`ListServersResponse <ListServersResponse>`

        Usage:
        ::

            result = api.list_servers()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/servers",
            params={
                "mac_addresses": mac_addresses,
                "name": name,
                "order_by": order_by,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                "placement_group_ids": placement_group_ids,
                "private_network_ids": private_network_ids,
                "project_id": project_id or self.client.default_project_id,
                "security_group_ids": security_group_ids,
                "server_ids": server_ids,
                "server_type": server_type,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServersResponse(res.json())

    def create_server(
        self,
        *,
        name: str,
        server_type: str,
        zone: Optional[ScwZone] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        placement_group_id: Optional[str] = None,
        volumes: Optional[list[CreateServerRequestServerVolume]] = None,
        windows_rdp_ssh_key_id: Optional[str] = None,
        public_network_interface: Optional[
            CreateServerRequestPublicNetworkInterface
        ] = None,
    ) -> Server:
        """
        Create an Instance.
        Create a new Instance of a specified server_type.
        :param name: Name of the server.
        :param server_type: Type of the server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID for the server.
        :param tags: Tags to associate with the server.
        :param placement_group_id: ID of the placement group the server belongs to.
        :param volumes: Volumes to attach to the server.
        :param windows_rdp_ssh_key_id: IAM ID of the SSH key used to encrypt the Windows `Administrator` password for RDP use.
        :param public_network_interface: Public network interface configuration.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.create_server(
                name="example",
                server_type="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers",
            body=marshal_CreateServerRequest(
                CreateServerRequest(
                    name=name,
                    server_type=server_type,
                    zone=zone,
                    project_id=project_id,
                    tags=tags,
                    placement_group_id=placement_group_id,
                    volumes=volumes,
                    windows_rdp_ssh_key_id=windows_rdp_ssh_key_id,
                    public_network_interface=public_network_interface,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def get_server(
        self,
        *,
        server_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Server:
        """
        Get an Instance.
        Get the details of a specified Instance.
        :param server_id: ID of the server to retrieve.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.get_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def wait_for_server(
        self,
        *,
        server_id: str,
        zone: Optional[ScwZone] = None,
        options: Optional[WaitForOptions[Server, bool]] = None,
    ) -> Server:
        """
        Get an Instance.
        Get the details of a specified Instance.
        :param server_id: ID of the server to retrieve.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.get_server(
                server_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in SERVER_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_server,
            options=options,
            args={
                "server_id": server_id,
                "zone": zone,
            },
        )

    def update_server(
        self,
        *,
        server_id: str,
        zone: Optional[ScwZone] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        server_type: Optional[str] = None,
        placement_group_id: Optional[str] = None,
        rescue_mode: Optional[bool] = None,
        boot_volume_id: Optional[str] = None,
        windows_rdp_ssh_key_id: Optional[str] = None,
        protected: Optional[bool] = None,
        public_network_interface: Optional[
            UpdateServerRequestPublicNetworkInterface
        ] = None,
    ) -> Server:
        """
        Update an Instance.
        Update the properties of a specified Instance information, such as name, rescue_mode, or tags.
        :param server_id: ID of the server to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: New name for the server.
        :param tags: New tags for the server.
        :param server_type: New server type.
        :param placement_group_id: New placement group ID.
        :param rescue_mode: New rescue mode setting.
        :param boot_volume_id: New boot volume ID.
        :param windows_rdp_ssh_key_id: New IAM ID of the SSH key used to encrypt the Windows `Administrator` password for RDP use.
        :param protected: Protection status of the server.
        :param public_network_interface: New public network interface configuration.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.update_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "PATCH",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}",
            body=marshal_UpdateServerRequest(
                UpdateServerRequest(
                    server_id=server_id,
                    zone=zone,
                    name=name,
                    tags=tags,
                    server_type=server_type,
                    placement_group_id=placement_group_id,
                    rescue_mode=rescue_mode,
                    boot_volume_id=boot_volume_id,
                    windows_rdp_ssh_key_id=windows_rdp_ssh_key_id,
                    protected=protected,
                    public_network_interface=public_network_interface,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def delete_server(
        self,
        *,
        server_id: str,
        zone: Optional[ScwZone] = None,
        delete_all_ips: Optional[bool] = None,
        delete_ip_ids: Optional[list[str]] = None,
        delete_all_volumes: Optional[bool] = None,
        delete_volume_ids: Optional[list[str]] = None,
        keep_all_private_nics: Optional[bool] = None,
        delete_private_nic_ids: Optional[list[str]] = None,
    ) -> None:
        """
        Delete an Instance.
        Delete a specified Instance.
        :param server_id: ID of the server to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param delete_all_ips: Whether to delete all IPs attached to the server.
        One-Of ('ips'): at most one of 'delete_all_ips', 'delete_ip_ids' could be set.
        :param delete_ip_ids: List of IP IDs to delete.
        One-Of ('ips'): at most one of 'delete_all_ips', 'delete_ip_ids' could be set.
        :param delete_all_volumes: Whether to delete all volumes attached to the server.
        One-Of ('volumes'): at most one of 'delete_all_volumes', 'delete_volume_ids' could be set.
        :param delete_volume_ids: List of volume IDs to delete.
        One-Of ('volumes'): at most one of 'delete_all_volumes', 'delete_volume_ids' could be set.
        :param keep_all_private_nics: Whether to keep all private network interfaces.
        One-Of ('private_nics'): at most one of 'keep_all_private_nics', 'delete_private_nic_ids' could be set.
        :param delete_private_nic_ids: List of private network interface IDs to delete.
        One-Of ('private_nics'): at most one of 'keep_all_private_nics', 'delete_private_nic_ids' could be set.

        Usage:
        ::

            result = api.delete_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "DELETE",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}",
            params={
                **resolve_one_of(
                    [
                        OneOfPossibility("delete_all_ips", delete_all_ips),
                        OneOfPossibility("delete_ip_ids", delete_ip_ids),
                    ]
                ),
                **resolve_one_of(
                    [
                        OneOfPossibility("delete_all_volumes", delete_all_volumes),
                        OneOfPossibility("delete_volume_ids", delete_volume_ids),
                    ]
                ),
                **resolve_one_of(
                    [
                        OneOfPossibility(
                            "delete_private_nic_ids", delete_private_nic_ids
                        ),
                        OneOfPossibility(
                            "keep_all_private_nics", keep_all_private_nics
                        ),
                    ]
                ),
            },
        )

        self._throw_on_error(res)

    def list_server_types(
        self,
        *,
        zone: Optional[ScwZone] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> ListServerTypesResponse:
        """
        List Instance types.
        List available Instance types and their technical details.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page_token: Token for pagination.
        :param page_size: Number of server types to return per page.
        :return: :class:`ListServerTypesResponse <ListServerTypesResponse>`

        Usage:
        ::

            result = api.list_server_types()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/server-types",
            params={
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServerTypesResponse(res.json())

    def start_server(
        self,
        *,
        server_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Server:
        """
        Start an Instance.
        Start a stopped or paused Instance.
        :param server_id: ID of the server to start.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.start_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/start",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def reboot_server(
        self,
        *,
        server_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Server:
        """
        Reboot an Instance.
        Reboot a running or paused Instance.
        :param server_id: ID of the server to reboot.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.reboot_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/reboot",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def pause_server(
        self,
        *,
        server_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Server:
        """
        Pause an Instance.
        Pause a running Instance.
        :param server_id: ID of the server to pause.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.pause_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/pause",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def stop_server(
        self,
        *,
        server_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Server:
        """
        Stop an Instance.
        Stop a running or paused Instance.
        :param server_id: ID of the server to stop.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.stop_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/stop",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def stop_and_delete_server(
        self,
        *,
        server_id: str,
        zone: Optional[ScwZone] = None,
        delete_all_ips: Optional[bool] = None,
        delete_ip_ids: Optional[list[str]] = None,
        delete_all_volumes: Optional[bool] = None,
        delete_volume_ids: Optional[list[str]] = None,
        keep_all_private_nics: Optional[bool] = None,
        delete_private_nic_ids: Optional[list[str]] = None,
    ) -> Server:
        """
        Stop and delete an Instance.
        Stop and delete a running or paused Instance.
        :param server_id: ID of the server to stop and delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param delete_all_ips: Whether to delete all IPs attached to the server.
        One-Of ('ips'): at most one of 'delete_all_ips', 'delete_ip_ids' could be set.
        :param delete_ip_ids: List of IP IDs to delete.
        One-Of ('ips'): at most one of 'delete_all_ips', 'delete_ip_ids' could be set.
        :param delete_all_volumes: Whether to delete all volumes attached to the server.
        One-Of ('volumes'): at most one of 'delete_all_volumes', 'delete_volume_ids' could be set.
        :param delete_volume_ids: List of volume IDs to delete.
        One-Of ('volumes'): at most one of 'delete_all_volumes', 'delete_volume_ids' could be set.
        :param keep_all_private_nics: Whether to keep all private network interfaces.
        One-Of ('private_nics'): at most one of 'keep_all_private_nics', 'delete_private_nic_ids' could be set.
        :param delete_private_nic_ids: List of private network interface IDs to delete.
        One-Of ('private_nics'): at most one of 'keep_all_private_nics', 'delete_private_nic_ids' could be set.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.stop_and_delete_server(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/stop-and-delete",
            body=marshal_StopAndDeleteServerRequest(
                StopAndDeleteServerRequest(
                    server_id=server_id,
                    zone=zone,
                    delete_all_ips=delete_all_ips,
                    delete_ip_ids=delete_ip_ids,
                    delete_all_volumes=delete_all_volumes,
                    delete_volume_ids=delete_volume_ids,
                    keep_all_private_nics=keep_all_private_nics,
                    delete_private_nic_ids=delete_private_nic_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def attach_server_volume(
        self,
        *,
        server_id: str,
        volume_id: str,
        boot_volume: bool,
        zone: Optional[ScwZone] = None,
        volume_type: Optional[ServerVolumeVolumeType] = None,
    ) -> Server:
        """
        Attach a volume to an Instance.
        Attach a l_ssd or SBS volume to an Instance.
        :param server_id: ID of the server to attach the volume to.
        :param volume_id: ID of the volume to attach.
        :param boot_volume: Whether the volume should be used as the boot volume.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param volume_type: Type of the volume.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.attach_server_volume(
                server_id="example",
                volume_id="example",
                boot_volume=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/attach-volume",
            body=marshal_AttachServerVolumeRequest(
                AttachServerVolumeRequest(
                    server_id=server_id,
                    volume_id=volume_id,
                    boot_volume=boot_volume,
                    zone=zone,
                    volume_type=volume_type,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def detach_server_volume(
        self,
        *,
        server_id: str,
        volume_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Server:
        """
        Detach a volume from an Instance.
        :param server_id: ID of the server to detach the volume from.
        :param volume_id: ID of the volume to detach.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.detach_server_volume(
                server_id="example",
                volume_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/detach-volume",
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
        return unmarshal_Server(res.json())

    def attach_server_file_system(
        self,
        *,
        server_id: str,
        filesystem_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Server:
        """
        Attach a filesystem volume to an Instance.
        :param server_id: ID of the server to attach the filesystem to.
        :param filesystem_id: ID of the filesystem to attach.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.attach_server_file_system(
                server_id="example",
                filesystem_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/attach-filesystem",
            body=marshal_AttachServerFileSystemRequest(
                AttachServerFileSystemRequest(
                    server_id=server_id,
                    filesystem_id=filesystem_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def detach_server_file_system(
        self,
        *,
        server_id: str,
        filesystem_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Server:
        """
        Detach a filesystem volume from an Instance.
        :param server_id: ID of the server to detach the filesystem from.
        :param filesystem_id: ID of the filesystem to detach.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.detach_server_file_system(
                server_id="example",
                filesystem_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/detach-filesystem",
            body=marshal_DetachServerFileSystemRequest(
                DetachServerFileSystemRequest(
                    server_id=server_id,
                    filesystem_id=filesystem_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def attach_server_ip(
        self,
        *,
        server_id: str,
        ip_id: str,
        default: bool,
        move_allowed: bool,
        zone: Optional[ScwZone] = None,
    ) -> Server:
        """
        Attach an IP to an Instance.
        :param server_id: ID of the server to attach the IP to.
        :param ip_id: ID of the IP to attach.
        :param default: Whether the IP should be the default IP.
        :param move_allowed: Whether moving the IP is allowed.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.attach_server_ip(
                server_id="example",
                ip_id="example",
                default=False,
                move_allowed=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/attach-ip",
            body=marshal_AttachServerIPRequest(
                AttachServerIPRequest(
                    server_id=server_id,
                    ip_id=ip_id,
                    default=default,
                    move_allowed=move_allowed,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def detach_server_ip(
        self,
        *,
        server_id: str,
        ip_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Server:
        """
        Detach an IP from an Instance.
        :param server_id: ID of the server to detach the IP from.
        :param ip_id: ID of the IP to detach.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.detach_server_ip(
                server_id="example",
                ip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/detach-ip",
            body=marshal_DetachServerIPRequest(
                DetachServerIPRequest(
                    server_id=server_id,
                    ip_id=ip_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def set_server_default_ip(
        self,
        *,
        server_id: str,
        ip_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Server:
        """
        Set default IP for an Instance.
        Set the default IP for an Instance.
        :param server_id: ID of the server to set the default IP for.
        :param ip_id: ID of the IP to set as default.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.set_server_default_ip(
                server_id="example",
                ip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/set-default-ip",
            body=marshal_SetServerDefaultIPRequest(
                SetServerDefaultIPRequest(
                    server_id=server_id,
                    ip_id=ip_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def attach_server_private_network_interface(
        self,
        *,
        server_id: str,
        private_network_interface_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Server:
        """
        Attach a private network interface to an Instance.
        :param server_id: ID of the server to attach the private network interface to.
        :param private_network_interface_id: ID of the private network interface to attach.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.attach_server_private_network_interface(
                server_id="example",
                private_network_interface_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/attach-private-network-interface",
            body=marshal_AttachServerPrivateNetworkInterfaceRequest(
                AttachServerPrivateNetworkInterfaceRequest(
                    server_id=server_id,
                    private_network_interface_id=private_network_interface_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def detach_server_private_network_interface(
        self,
        *,
        server_id: str,
        private_network_interface_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Server:
        """
        Detach a private network interface from an Instance.
        :param server_id: ID of the server to detach the private network interface from.
        :param private_network_interface_id: ID of the private network interface to detach.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.detach_server_private_network_interface(
                server_id="example",
                private_network_interface_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/detach-private-network-interface",
            body=marshal_DetachServerPrivateNetworkInterfaceRequest(
                DetachServerPrivateNetworkInterfaceRequest(
                    server_id=server_id,
                    private_network_interface_id=private_network_interface_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    def list_private_network_interfaces(
        self,
        *,
        zone: Optional[ScwZone] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListPrivateNetworkInterfacesRequestOrderBy] = None,
        project_id: Optional[str] = None,
        server_ids: Optional[list[str]] = None,
        private_network_ids: Optional[list[str]] = None,
        tags: Optional[list[str]] = None,
    ) -> ListPrivateNetworkInterfacesResponse:
        """
        List private network interfaces.
        List all private network interfaces.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page_token: Token for pagination.
        :param page_size: Number of items to return per page.
        :param order_by: Field to order results by.
        :param project_id: Filter by Project ID.
        :param server_ids: Filter by server IDs.
        :param private_network_ids: Filter by Private Network IDs.
        :param tags: Filter by tags.
        :return: :class:`ListPrivateNetworkInterfacesResponse <ListPrivateNetworkInterfacesResponse>`

        Usage:
        ::

            result = api.list_private_network_interfaces()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/private-network-interfaces",
            params={
                "order_by": order_by,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                "private_network_ids": private_network_ids,
                "project_id": project_id or self.client.default_project_id,
                "server_ids": server_ids,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPrivateNetworkInterfacesResponse(res.json())

    def create_private_network_interface(
        self,
        *,
        private_network_id: str,
        zone: Optional[ScwZone] = None,
        project_id: Optional[str] = None,
        server_id: Optional[str] = None,
        ip_ids: Optional[list[str]] = None,
        tags: Optional[list[str]] = None,
    ) -> PrivateNetworkInterface:
        """
        Create a private network interface.
        Create a private network interface linked to a Private Network. It can be attached to an Instance.
        :param private_network_id: ID of the Private Network to attach to.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID for the private network interface.
        :param server_id: ID of the Instance to attach the interface to.
        :param ip_ids: List of IP IDs to attach to the interface.
        :param tags: Tags to assign to the private network interface.
        :return: :class:`PrivateNetworkInterface <PrivateNetworkInterface>`

        Usage:
        ::

            result = api.create_private_network_interface(
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/private-network-interfaces",
            body=marshal_CreatePrivateNetworkInterfaceRequest(
                CreatePrivateNetworkInterfaceRequest(
                    private_network_id=private_network_id,
                    zone=zone,
                    project_id=project_id,
                    server_id=server_id,
                    ip_ids=ip_ids,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNetworkInterface(res.json())

    def get_private_network_interface(
        self,
        *,
        private_network_interface_id: str,
        zone: Optional[ScwZone] = None,
    ) -> PrivateNetworkInterface:
        """
        Get a private network interface.
        Get details of a specified private network interface.
        :param private_network_interface_id: ID of the private network interface to retrieve.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`PrivateNetworkInterface <PrivateNetworkInterface>`

        Usage:
        ::

            result = api.get_private_network_interface(
                private_network_interface_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_private_network_interface_id = validate_path_param(
            "private_network_interface_id", private_network_interface_id
        )

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/private-network-interfaces/{param_private_network_interface_id}",
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNetworkInterface(res.json())

    def wait_for_private_network_interface(
        self,
        *,
        private_network_interface_id: str,
        zone: Optional[ScwZone] = None,
        options: Optional[WaitForOptions[PrivateNetworkInterface, bool]] = None,
    ) -> PrivateNetworkInterface:
        """
        Get a private network interface.
        Get details of a specified private network interface.
        :param private_network_interface_id: ID of the private network interface to retrieve.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`PrivateNetworkInterface <PrivateNetworkInterface>`

        Usage:
        ::

            result = api.get_private_network_interface(
                private_network_interface_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: (
                res.status not in PRIVATE_NETWORK_INTERFACE_TRANSIENT_STATUSES
            )

        return wait_for_resource(
            fetcher=self.get_private_network_interface,
            options=options,
            args={
                "private_network_interface_id": private_network_interface_id,
                "zone": zone,
            },
        )

    def update_private_network_interface(
        self,
        *,
        private_network_interface_id: str,
        zone: Optional[ScwZone] = None,
        tags: Optional[list[str]] = None,
    ) -> PrivateNetworkInterface:
        """
        Update a private network interface.
        Update the properties of a specified private network interface.
        :param private_network_interface_id: ID of the private network interface to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param tags: New tags to assign to the private network interface.
        :return: :class:`PrivateNetworkInterface <PrivateNetworkInterface>`

        Usage:
        ::

            result = api.update_private_network_interface(
                private_network_interface_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_private_network_interface_id = validate_path_param(
            "private_network_interface_id", private_network_interface_id
        )

        res = self._request(
            "PATCH",
            f"/instance/v2alpha1/zones/{param_zone}/private-network-interfaces/{param_private_network_interface_id}",
            body=marshal_UpdatePrivateNetworkInterfaceRequest(
                UpdatePrivateNetworkInterfaceRequest(
                    private_network_interface_id=private_network_interface_id,
                    zone=zone,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNetworkInterface(res.json())

    def delete_private_network_interface(
        self,
        *,
        private_network_interface_id: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete a private network interface.
        Delete a specified private network interface.
        :param private_network_interface_id: ID of the private network interface to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_private_network_interface(
                private_network_interface_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_private_network_interface_id = validate_path_param(
            "private_network_interface_id", private_network_interface_id
        )

        res = self._request(
            "DELETE",
            f"/instance/v2alpha1/zones/{param_zone}/private-network-interfaces/{param_private_network_interface_id}",
        )

        self._throw_on_error(res)

    def list_placement_groups(
        self,
        *,
        zone: Optional[ScwZone] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListPlacementGroupsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        placement_group_ids: Optional[list[str]] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> ListPlacementGroupsResponse:
        """
        List placement groups.
        List all placement groups.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page_token: The initial pagination token to start from.
        :param page_size: The maximum number of placement groups to return.
        :param order_by: The field by which to order the result list.
        :param project_id: List only placement groups of this Project ID.
        :param placement_group_ids: List only placement groups with these IDs.
        :param name: Filter placement groups by name.
        :param tags: List placement groups with these exact tags.
        :return: :class:`ListPlacementGroupsResponse <ListPlacementGroupsResponse>`

        Usage:
        ::

            result = api.list_placement_groups()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/placement-groups",
            params={
                "name": name,
                "order_by": order_by,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                "placement_group_ids": placement_group_ids,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPlacementGroupsResponse(res.json())

    def create_placement_group(
        self,
        *,
        name: str,
        zone: Optional[ScwZone] = None,
        project_id: Optional[str] = None,
        policy_type: Optional[PlacementGroupPolicyType] = None,
        tags: Optional[list[str]] = None,
    ) -> PlacementGroup:
        """
        Create a placement group.
        Create a new placement group.
        :param name: Name of the placement group.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID of the placement group.
        :param policy_type: Policy type of the placement group.
        :param tags: Tags of the placement group.
        :return: :class:`PlacementGroup <PlacementGroup>`

        Usage:
        ::

            result = api.create_placement_group(
                name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/placement-groups",
            body=marshal_CreatePlacementGroupRequest(
                CreatePlacementGroupRequest(
                    name=name,
                    zone=zone,
                    project_id=project_id,
                    policy_type=policy_type,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PlacementGroup(res.json())

    def get_placement_group(
        self,
        *,
        placement_group_id: str,
        zone: Optional[ScwZone] = None,
    ) -> PlacementGroup:
        """
        Get a placement group.
        Get a specified placement group.
        :param placement_group_id: UUID of the placement group you want to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`PlacementGroup <PlacementGroup>`

        Usage:
        ::

            result = api.get_placement_group(
                placement_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_placement_group_id = validate_path_param(
            "placement_group_id", placement_group_id
        )

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/placement-groups/{param_placement_group_id}",
        )

        self._throw_on_error(res)
        return unmarshal_PlacementGroup(res.json())

    def update_placement_group(
        self,
        *,
        placement_group_id: str,
        zone: Optional[ScwZone] = None,
        name: Optional[str] = None,
        policy_type: Optional[PlacementGroupPolicyType] = None,
        tags: Optional[list[str]] = None,
    ) -> PlacementGroup:
        """
        Update a placement group.
        Update the properties of a specified placement group.
        :param placement_group_id: UUID of the placement group.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the placement group.
        :param policy_type: Policy type of the placement group.
        :param tags: Tags of the placement group.
        :return: :class:`PlacementGroup <PlacementGroup>`

        Usage:
        ::

            result = api.update_placement_group(
                placement_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_placement_group_id = validate_path_param(
            "placement_group_id", placement_group_id
        )

        res = self._request(
            "PATCH",
            f"/instance/v2alpha1/zones/{param_zone}/placement-groups/{param_placement_group_id}",
            body=marshal_UpdatePlacementGroupRequest(
                UpdatePlacementGroupRequest(
                    placement_group_id=placement_group_id,
                    zone=zone,
                    name=name,
                    policy_type=policy_type,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PlacementGroup(res.json())

    def delete_placement_group(
        self,
        *,
        placement_group_id: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete a placement group.
        Delete a specified placement group.
        :param placement_group_id: UUID of the placement group you want to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_placement_group(
                placement_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_placement_group_id = validate_path_param(
            "placement_group_id", placement_group_id
        )

        res = self._request(
            "DELETE",
            f"/instance/v2alpha1/zones/{param_zone}/placement-groups/{param_placement_group_id}",
        )

        self._throw_on_error(res)

    def list_security_groups(
        self,
        *,
        zone: Optional[ScwZone] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSecurityGroupsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        security_group_ids: Optional[list[str]] = None,
    ) -> ListSecurityGroupsResponse:
        """
        List security groups.
        List all security groups.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page_token: Token for pagination.
        :param page_size: Number of items to return per page.
        :param order_by: Field and direction to sort by.
        :param project_id: Filter by Project ID.
        :param name: Filter by name.
        :param tags: Filter by tags.
        :param security_group_ids: Filter by specific security group IDs.
        :return: :class:`ListSecurityGroupsResponse <ListSecurityGroupsResponse>`

        Usage:
        ::

            result = api.list_security_groups()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/security-groups",
            params={
                "name": name,
                "order_by": order_by,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                "project_id": project_id or self.client.default_project_id,
                "security_group_ids": security_group_ids,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSecurityGroupsResponse(res.json())

    def create_security_group(
        self,
        *,
        name: str,
        description: str,
        disable_default_rules: bool,
        project_default: bool,
        stateless: bool,
        zone: Optional[ScwZone] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        inbound_default_action: Optional[SecurityGroupAction] = None,
        outbound_default_action: Optional[SecurityGroupAction] = None,
    ) -> SecurityGroup:
        """
        Create a security group.
        Create a security group with a specified name and description.
        :param name: Name of the security group.
        :param description: Description of the security group.
        :param disable_default_rules: Whether to disable default rules.
        :param project_default: Whether this should be the default security group for the project.
        :param stateless: Whether the security group should be stateless.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID the security group belongs to.
        :param tags: Tags for the security group.
        :param inbound_default_action: Default action for inbound rules.
        :param outbound_default_action: Default action for outbound rules.
        :return: :class:`SecurityGroup <SecurityGroup>`

        Usage:
        ::

            result = api.create_security_group(
                name="example",
                description="example",
                disable_default_rules=False,
                project_default=False,
                stateless=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/security-groups",
            body=marshal_CreateSecurityGroupRequest(
                CreateSecurityGroupRequest(
                    name=name,
                    description=description,
                    disable_default_rules=disable_default_rules,
                    project_default=project_default,
                    stateless=stateless,
                    zone=zone,
                    project_id=project_id,
                    tags=tags,
                    inbound_default_action=inbound_default_action,
                    outbound_default_action=outbound_default_action,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SecurityGroup(res.json())

    def get_security_group(
        self,
        *,
        security_group_id: str,
        zone: Optional[ScwZone] = None,
    ) -> SecurityGroup:
        """
        Get a security group.
        Get the details of a specified security group.
        :param security_group_id: ID of the security group to retrieve.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`SecurityGroup <SecurityGroup>`

        Usage:
        ::

            result = api.get_security_group(
                security_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_security_group_id = validate_path_param(
            "security_group_id", security_group_id
        )

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/security-groups/{param_security_group_id}",
        )

        self._throw_on_error(res)
        return unmarshal_SecurityGroup(res.json())

    def update_security_group(
        self,
        *,
        security_group_id: str,
        zone: Optional[ScwZone] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        disable_default_rules: Optional[bool] = None,
        tags: Optional[list[str]] = None,
        project_default: Optional[bool] = None,
        inbound_default_action: Optional[SecurityGroupAction] = None,
        outbound_default_action: Optional[SecurityGroupAction] = None,
        stateless: Optional[bool] = None,
    ) -> SecurityGroup:
        """
        Update a security group.
        Update the properties of a security group.
        :param security_group_id: ID of the security group to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: New name for the security group.
        :param description: New description for the security group.
        :param disable_default_rules: Whether to disable default rules.
        :param tags: New tags for the security group.
        :param project_default: Whether this should be the default security group for the project.
        :param inbound_default_action: New default action for inbound rules.
        :param outbound_default_action: New default action for outbound rules.
        :param stateless: Whether the security group should be stateless.
        :return: :class:`SecurityGroup <SecurityGroup>`

        Usage:
        ::

            result = api.update_security_group(
                security_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_security_group_id = validate_path_param(
            "security_group_id", security_group_id
        )

        res = self._request(
            "PATCH",
            f"/instance/v2alpha1/zones/{param_zone}/security-groups/{param_security_group_id}",
            body=marshal_UpdateSecurityGroupRequest(
                UpdateSecurityGroupRequest(
                    security_group_id=security_group_id,
                    zone=zone,
                    name=name,
                    description=description,
                    disable_default_rules=disable_default_rules,
                    tags=tags,
                    project_default=project_default,
                    inbound_default_action=inbound_default_action,
                    outbound_default_action=outbound_default_action,
                    stateless=stateless,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SecurityGroup(res.json())

    def delete_security_group(
        self,
        *,
        security_group_id: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete a security group.
        Delete a specified security group.
        :param security_group_id: ID of the security group to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_security_group(
                security_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_security_group_id = validate_path_param(
            "security_group_id", security_group_id
        )

        res = self._request(
            "DELETE",
            f"/instance/v2alpha1/zones/{param_zone}/security-groups/{param_security_group_id}",
        )

        self._throw_on_error(res)

    def add_security_group_rules(
        self,
        *,
        security_group_id: str,
        zone: Optional[ScwZone] = None,
        security_group_rules: Optional[list[SecurityGroupRuleConfig]] = None,
    ) -> AddSecurityGroupRulesResponse:
        """
        Add rules to a security group.
        Add one or more rules to a security group.
        :param security_group_id: ID of the security group to add rules to.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param security_group_rules: List of rules to add.
        :return: :class:`AddSecurityGroupRulesResponse <AddSecurityGroupRulesResponse>`

        Usage:
        ::

            result = api.add_security_group_rules(
                security_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/security-group-rules",
            body=marshal_AddSecurityGroupRulesRequest(
                AddSecurityGroupRulesRequest(
                    security_group_id=security_group_id,
                    zone=zone,
                    security_group_rules=security_group_rules,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AddSecurityGroupRulesResponse(res.json())

    def set_security_group_rules(
        self,
        *,
        security_group_id: str,
        zone: Optional[ScwZone] = None,
        security_group_rules: Optional[list[SecurityGroupRuleConfig]] = None,
    ) -> SecurityGroup:
        """
        Set all rules of a security group.
        Replace all rules of a specified security group with the provided rules.
        :param security_group_id: ID of the security group to set rules for.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param security_group_rules: List of rules to set.
        :return: :class:`SecurityGroup <SecurityGroup>`

        Usage:
        ::

            result = api.set_security_group_rules(
                security_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "PUT",
            f"/instance/v2alpha1/zones/{param_zone}/security-group-rules",
            body=marshal_SetSecurityGroupRulesRequest(
                SetSecurityGroupRulesRequest(
                    security_group_id=security_group_id,
                    zone=zone,
                    security_group_rules=security_group_rules,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SecurityGroup(res.json())

    def update_security_group_rule(
        self,
        *,
        security_group_rule_id: str,
        zone: Optional[ScwZone] = None,
        protocol: Optional[SecurityGroupRuleProtocol] = None,
        direction: Optional[SecurityGroupRuleDirection] = None,
        action: Optional[SecurityGroupRuleAction] = None,
        source_ip_range: Optional[str] = None,
        destination_ip_range: Optional[str] = None,
        source_ports: Optional[SecurityGroupRulePortRange] = None,
        destination_ports: Optional[SecurityGroupRulePortRange] = None,
        position: Optional[int] = None,
    ) -> SecurityGroup:
        """
        Update a security group rule.
        Update the properties of a rule from a specified security group.
        :param security_group_rule_id: ID of the rule to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param protocol: New protocol for the rule.
        :param direction: New direction for the rule.
        :param action: New action for the rule.
        :param source_ip_range: New source IP range for the rule.
        :param destination_ip_range: New destination IP range for the rule.
        :param source_ports: New source port range for the rule.
        :param destination_ports: New destination port range for the rule.
        :param position: New position for the rule.
        :return: :class:`SecurityGroup <SecurityGroup>`

        Usage:
        ::

            result = api.update_security_group_rule(
                security_group_rule_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_security_group_rule_id = validate_path_param(
            "security_group_rule_id", security_group_rule_id
        )

        res = self._request(
            "PATCH",
            f"/instance/v2alpha1/zones/{param_zone}/security-group-rules/{param_security_group_rule_id}",
            body=marshal_UpdateSecurityGroupRuleRequest(
                UpdateSecurityGroupRuleRequest(
                    security_group_rule_id=security_group_rule_id,
                    zone=zone,
                    protocol=protocol,
                    direction=direction,
                    action=action,
                    source_ip_range=source_ip_range,
                    destination_ip_range=destination_ip_range,
                    source_ports=source_ports,
                    destination_ports=destination_ports,
                    position=position,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SecurityGroup(res.json())

    def delete_security_group_rules(
        self,
        *,
        zone: Optional[ScwZone] = None,
        security_group_rule_ids: Optional[list[str]] = None,
    ) -> None:
        """
        Delete rules from a security group.
        Delete specified security groups.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param security_group_rule_ids: List of rule IDs to delete.

        Usage:
        ::

            result = api.delete_security_group_rules()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "DELETE",
            f"/instance/v2alpha1/zones/{param_zone}/security-group-rules",
            body=marshal_DeleteSecurityGroupRulesRequest(
                DeleteSecurityGroupRulesRequest(
                    zone=zone,
                    security_group_rule_ids=security_group_rule_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    def list_user_data_keys(
        self,
        *,
        server_id: str,
        zone: Optional[ScwZone] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> ListUserDataKeysResponse:
        """
        List user data keys.
        List all user data keys registered on a specified Instance.
        :param server_id: The ID of the server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page_token: Page token for pagination.
        :param page_size: Number of items to return per page.
        :return: :class:`ListUserDataKeysResponse <ListUserDataKeysResponse>`

        Usage:
        ::

            result = api.list_user_data_keys(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/user-data",
            params={
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListUserDataKeysResponse(res.json())

    def get_user_data(
        self,
        *,
        server_id: str,
        key: str,
        zone: Optional[ScwZone] = None,
    ) -> UserData:
        """
        Get user data.
        Get the content of a user data with a specified key on an Instance.
        :param server_id: The ID of the server.
        :param key: The key of the user data to retrieve.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`UserData <UserData>`

        Usage:
        ::

            result = api.get_user_data(
                server_id="example",
                key="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_key = validate_path_param("key", key)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/user-data/{param_key}",
        )

        self._throw_on_error(res)
        return unmarshal_UserData(res.json())

    def set_user_data(
        self,
        *,
        server_id: str,
        key: str,
        content: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Add/set user data.
        Add or update a user data with a specified key on an Instance.
        :param server_id: The ID of the server.
        :param key: The key of the user data to set.
        :param content: The content to set for the user data.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.set_user_data(
                server_id="example",
                key="example",
                content="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_key = validate_path_param("key", key)

        res = self._request(
            "PUT",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/user-data/{param_key}",
            body=marshal_SetUserDataRequest(
                SetUserDataRequest(
                    server_id=server_id,
                    key=key,
                    content=content,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    def delete_user_data(
        self,
        *,
        server_id: str,
        key: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete user data.
        Delete a specified key from an Instance's user data.
        :param server_id: The ID of the server.
        :param key: The key of the user data to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_user_data(
                server_id="example",
                key="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_key = validate_path_param("key", key)

        res = self._request(
            "DELETE",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/user-data/{param_key}",
        )

        self._throw_on_error(res)

    def get_server_cloud_init(
        self,
        *,
        server_id: str,
        zone: Optional[ScwZone] = None,
    ) -> UserData:
        """
        Get cloud-init user data.
        Get the cloud-init configuration of a specified Instance.
        :param server_id: The ID of the server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`UserData <UserData>`

        Usage:
        ::

            result = api.get_server_cloud_init(
                server_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/user-data/cloud-init",
        )

        self._throw_on_error(res)
        return unmarshal_UserData(res.json())

    def set_server_cloud_init(
        self,
        *,
        server_id: str,
        content: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Set cloud-init user data.
        Set the cloud-init configuration for a specified Instance.
        :param server_id: The ID of the server.
        :param content: The cloud-init configuration content.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.set_server_cloud_init(
                server_id="example",
                content="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "PUT",
            f"/instance/v2alpha1/zones/{param_zone}/servers/{param_server_id}/user-data/cloud-init",
            body=marshal_SetServerCloudInitRequest(
                SetServerCloudInitRequest(
                    server_id=server_id,
                    content=content,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    def list_templates(
        self,
        *,
        zone: Optional[ScwZone] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTemplatesRequestOrderBy] = None,
        project_id: Optional[str] = None,
        template_ids: Optional[list[str]] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        server_tags: Optional[list[str]] = None,
        security_group_ids: Optional[list[str]] = None,
        placement_group_ids: Optional[list[str]] = None,
    ) -> ListTemplatesResponse:
        """
        List templates.
        List all available templates.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page_token: Token for pagination.
        :param page_size: Number of items to return per page.
        :param order_by: Field to sort results by.
        :param project_id: Filter by Project ID.
        :param template_ids: Filter by specific template IDs.
        :param name: Filter by template name.
        :param tags: Filter by tags.
        :param server_tags: Filter by server tags.
        :param security_group_ids: Filter by security group IDs.
        :param placement_group_ids: Filter by placement group IDs.
        :return: :class:`ListTemplatesResponse <ListTemplatesResponse>`

        Usage:
        ::

            result = api.list_templates()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/templates",
            params={
                "name": name,
                "order_by": order_by,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                "placement_group_ids": placement_group_ids,
                "project_id": project_id or self.client.default_project_id,
                "security_group_ids": security_group_ids,
                "server_tags": server_tags,
                "tags": tags,
                "template_ids": template_ids,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTemplatesResponse(res.json())

    def create_template(
        self,
        *,
        zone: Optional[ScwZone] = None,
        name: str,
        server_type: str,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        server_tags: Optional[list[str]] = None,
        public_ip_v4_count: int,
        public_ip_v6_count: int,
        security_group_id: Optional[str] = None,
        placement_group_id: Optional[str] = None,
        volumes: Optional[list[CreateTemplateRequestVolumeTemplate]] = None,
        private_networks: Optional[
            list[CreateTemplateRequestPrivateNetworkTemplate]
        ] = None,
        filesystem_ids: Optional[list[str]] = None,
        windows_rdp_ssh_key_id: Optional[str] = None,
    ) -> Template:
        """
        Create a template.
        Create a new template from an Instance.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the template.
        :param server_type: Commercial type of the server defined by the template.
        :param project_id: Project ID for the template.
        :param tags: Tags to associate with the template.
        :param server_tags: Tags to associate with servers created from the template.
        :param public_ip_v4_count: Number of IPv4 public IPs to attach to servers created from this template.
        :param public_ip_v6_count: Number of IPv6 public IPs to attach to servers created from this template.
        :param security_group_id: Security group ID for the template.
        :param placement_group_id: Placement group ID for the template.
        :param volumes: List of volume templates to define volumes for servers.
        :param private_networks: List of private networks to associate with the template.
        :param filesystem_ids: List of filesystem IDs to associate with the template.
        :param windows_rdp_ssh_key_id: IAM ID of the SSH key used to encrypt the Windows `Administrator` password for RDP use.
        :return: :class:`Template <Template>`

        Usage:
        ::

            result = api.create_template(
                name="example",
                server_type="example",
                public_ip_v4_count=1,
                public_ip_v6_count=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/templates",
            body=marshal_CreateTemplateRequest(
                CreateTemplateRequest(
                    zone=zone,
                    name=name,
                    server_type=server_type,
                    project_id=project_id,
                    tags=tags,
                    server_tags=server_tags,
                    public_ip_v4_count=public_ip_v4_count,
                    public_ip_v6_count=public_ip_v6_count,
                    security_group_id=security_group_id,
                    placement_group_id=placement_group_id,
                    volumes=volumes,
                    private_networks=private_networks,
                    filesystem_ids=filesystem_ids,
                    windows_rdp_ssh_key_id=windows_rdp_ssh_key_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Template(res.json())

    def get_template(
        self,
        *,
        template_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Template:
        """
        Get a template.
        Get details of a specified template.
        :param template_id: Unique ID of the template to retrieve.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Template <Template>`

        Usage:
        ::

            result = api.get_template(
                template_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_template_id = validate_path_param("template_id", template_id)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/templates/{param_template_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Template(res.json())

    def update_template(
        self,
        *,
        template_id: str,
        zone: Optional[ScwZone] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        server_tags: Optional[list[str]] = None,
        server_type: Optional[str] = None,
        security_group_id: Optional[str] = None,
        placement_group_id: Optional[str] = None,
        update_volumes: Optional[UpdateTemplateRequestUpdateVolumes] = None,
        update_private_networks: Optional[
            UpdateTemplateRequestUpdatePrivateNetworks
        ] = None,
        filesystem_ids: Optional[list[str]] = None,
        public_ip_v4_count: Optional[int] = None,
        public_ip_v6_count: Optional[int] = None,
        windows_rdp_ssh_key_id: Optional[str] = None,
    ) -> Template:
        """
        Update a template.
        Update the properties of a template.
        :param template_id: Unique ID of the template to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: New name for the template.
        :param tags: New tags for the template.
        :param server_tags: New server tags for the template.
        :param server_type: New server type for the template.
        :param security_group_id: New security group ID for the template.
        :param placement_group_id: New placement group ID for the template.
        :param update_volumes: Updated volume templates for the template.
        :param update_private_networks: Updated private networks list for the template.
        :param filesystem_ids: New list of filesystem IDs for the template.
        :param public_ip_v4_count: New number of IPv4 public IPs to attach to servers.
        :param public_ip_v6_count: New number of IPv6 public IPs to attach to servers.
        :param windows_rdp_ssh_key_id: New IAM ID of the SSH key used to encrypt the Windows `Administrator` password for RDP use.
        :return: :class:`Template <Template>`

        Usage:
        ::

            result = api.update_template(
                template_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_template_id = validate_path_param("template_id", template_id)

        res = self._request(
            "PATCH",
            f"/instance/v2alpha1/zones/{param_zone}/templates/{param_template_id}",
            body=marshal_UpdateTemplateRequest(
                UpdateTemplateRequest(
                    template_id=template_id,
                    zone=zone,
                    name=name,
                    tags=tags,
                    server_tags=server_tags,
                    server_type=server_type,
                    security_group_id=security_group_id,
                    placement_group_id=placement_group_id,
                    update_volumes=update_volumes,
                    update_private_networks=update_private_networks,
                    filesystem_ids=filesystem_ids,
                    public_ip_v4_count=public_ip_v4_count,
                    public_ip_v6_count=public_ip_v6_count,
                    windows_rdp_ssh_key_id=windows_rdp_ssh_key_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Template(res.json())

    def delete_template(
        self,
        *,
        template_id: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete a template.
        Delete a specified template.
        :param template_id: Unique ID of the template to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_template(
                template_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_template_id = validate_path_param("template_id", template_id)

        res = self._request(
            "DELETE",
            f"/instance/v2alpha1/zones/{param_zone}/templates/{param_template_id}",
            body={},
        )

        self._throw_on_error(res)

    def list_template_user_data_keys(
        self,
        *,
        template_id: str,
        zone: Optional[ScwZone] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> ListTemplateUserDataKeysResponse:
        """
        List template user data keys.
        List all user data keys of a template.
        :param template_id: Unique ID of the template.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page_token: Token for pagination.
        :param page_size: Number of items to return per page.
        :return: :class:`ListTemplateUserDataKeysResponse <ListTemplateUserDataKeysResponse>`

        Usage:
        ::

            result = api.list_template_user_data_keys(
                template_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_template_id = validate_path_param("template_id", template_id)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/templates/{param_template_id}/user-data",
            params={
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTemplateUserDataKeysResponse(res.json())

    def get_template_user_data(
        self,
        *,
        template_id: str,
        key: str,
        zone: Optional[ScwZone] = None,
    ) -> UserData:
        """
        Get template user data.
        Get a specific user data key of a template.
        :param template_id: Unique ID of the template.
        :param key: Key of the user data to retrieve.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`UserData <UserData>`

        Usage:
        ::

            result = api.get_template_user_data(
                template_id="example",
                key="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_template_id = validate_path_param("template_id", template_id)
        param_key = validate_path_param("key", key)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/templates/{param_template_id}/user-data/{param_key}",
        )

        self._throw_on_error(res)
        return unmarshal_UserData(res.json())

    def set_template_user_data(
        self,
        *,
        template_id: str,
        key: str,
        content: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Set template user data.
        Set a user data key of a template.
        :param template_id: Unique ID of the template.
        :param key: Key of the user data to set.
        :param content: Content of the user data.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.set_template_user_data(
                template_id="example",
                key="example",
                content="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_template_id = validate_path_param("template_id", template_id)
        param_key = validate_path_param("key", key)

        res = self._request(
            "PUT",
            f"/instance/v2alpha1/zones/{param_zone}/templates/{param_template_id}/user-data/{param_key}",
            body=marshal_SetTemplateUserDataRequest(
                SetTemplateUserDataRequest(
                    template_id=template_id,
                    key=key,
                    content=content,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    def delete_template_user_data(
        self,
        *,
        template_id: str,
        key: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete template user data.
        Delete a specific user data key of a template.
        :param template_id: Unique ID of the template.
        :param key: Key of the user data to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_template_user_data(
                template_id="example",
                key="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_template_id = validate_path_param("template_id", template_id)
        param_key = validate_path_param("key", key)

        res = self._request(
            "DELETE",
            f"/instance/v2alpha1/zones/{param_zone}/templates/{param_template_id}/user-data/{param_key}",
        )

        self._throw_on_error(res)

    def get_template_cloud_init(
        self,
        *,
        template_id: str,
        zone: Optional[ScwZone] = None,
    ) -> UserData:
        """
        Get template cloud-init.
        Get the cloud-init configuration of a template.
        :param template_id: Unique ID of the template.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`UserData <UserData>`

        Usage:
        ::

            result = api.get_template_cloud_init(
                template_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_template_id = validate_path_param("template_id", template_id)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/templates/{param_template_id}/user-data/cloud-init",
        )

        self._throw_on_error(res)
        return unmarshal_UserData(res.json())

    def set_template_cloud_init(
        self,
        *,
        template_id: str,
        content: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Set template cloud-init.
        Set the cloud-init configuration of a template.
        :param template_id: Unique ID of the template.
        :param content: Cloud-init configuration content.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.set_template_cloud_init(
                template_id="example",
                content="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_template_id = validate_path_param("template_id", template_id)

        res = self._request(
            "PUT",
            f"/instance/v2alpha1/zones/{param_zone}/templates/{param_template_id}/user-data/cloud-init",
            body=marshal_SetTemplateCloudInitRequest(
                SetTemplateCloudInitRequest(
                    template_id=template_id,
                    content=content,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    def check_template(
        self,
        *,
        template_id: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Check a template.
        Validate that a template is usable.
        :param template_id: Unique ID of the template to check.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.check_template(
                template_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_template_id = validate_path_param("template_id", template_id)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/templates/{param_template_id}/check",
        )

        self._throw_on_error(res)

    def create_server_from_template(
        self,
        *,
        template_id: str,
        name: str,
        zone: Optional[ScwZone] = None,
    ) -> Server:
        """
        Create a server from a template.
        Create a new Instance using a specified template.
        :param template_id: Unique ID of the template to use.
        :param name: Name of the new server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.create_server_from_template(
                template_id="example",
                name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_template_id = validate_path_param("template_id", template_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/templates/{param_template_id}/create-server",
            body=marshal_CreateServerFromTemplateRequest(
                CreateServerFromTemplateRequest(
                    template_id=template_id,
                    name=name,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())


class InstanceV2Alpha1VolumeAPI(API):
    """
    This API allows you to manage Instance local and scratch volumes.
    """

    def list_volume_types(
        self,
        *,
        zone: Optional[ScwZone] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> ListVolumeTypesResponse:
        """
        List volume types.
        List all volume types and their technical details.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page_token: Token for pagination.
        :param page_size: Number of items to return per page.
        :return: :class:`ListVolumeTypesResponse <ListVolumeTypesResponse>`

        Usage:
        ::

            result = api.list_volume_types()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/volume-types",
            params={
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVolumeTypesResponse(res.json())

    def list_volumes(
        self,
        *,
        zone: Optional[ScwZone] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListVolumesRequestOrderBy] = None,
        project_id: Optional[str] = None,
        volume_ids: Optional[list[str]] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        volume_type: Optional[VolumeVolumeType] = None,
    ) -> ListVolumesResponse:
        """
        List volumes.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page_token: Token for pagination.
        :param page_size: Number of items to return per page.
        :param order_by: Field to order the results by.
        :param project_id: Filter by Project ID.
        :param volume_ids: Filter by specific volume IDs.
        :param name: Filter by volume name.
        :param tags: Filter by tags.
        :param volume_type: Filter by volume type.
        :return: :class:`ListVolumesResponse <ListVolumesResponse>`

        Usage:
        ::

            result = api.list_volumes()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/volumes",
            params={
                "name": name,
                "order_by": order_by,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
                "volume_ids": volume_ids,
                "volume_type": volume_type,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVolumesResponse(res.json())

    def create_volume(
        self,
        *,
        name: str,
        zone: Optional[ScwZone] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        size: Optional[int] = None,
        base_snapshot_id: Optional[str] = None,
        volume_type: Optional[CreateVolumeRequestVolumeType] = None,
    ) -> Volume:
        """
        Create a volume.
        Create a volume of a specified type.
        :param name: Volume name.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID to which the volume belongs.
        :param tags: Tags associated with the volume.
        :param size: Volume size in bytes.
        :param base_snapshot_id: ID of the base snapshot used for this volume.
        :param volume_type: Type of the volume.
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = api.create_volume(
                name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/volumes",
            body=marshal_VolumeApiCreateVolumeRequest(
                VolumeApiCreateVolumeRequest(
                    name=name,
                    zone=zone,
                    project_id=project_id,
                    tags=tags,
                    size=size,
                    base_snapshot_id=base_snapshot_id,
                    volume_type=volume_type,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Volume(res.json())

    def get_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Volume:
        """
        Get a volume.
        Get a specified volume.
        :param volume_id: ID of the volume to retrieve.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = api.get_volume(
                volume_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/volumes/{param_volume_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Volume(res.json())

    def wait_for_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[ScwZone] = None,
        options: Optional[WaitForOptions[Volume, bool]] = None,
    ) -> Volume:
        """
        Get a volume.
        Get a specified volume.
        :param volume_id: ID of the volume to retrieve.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = api.get_volume(
                volume_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in VOLUME_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_volume,
            options=options,
            args={
                "volume_id": volume_id,
                "zone": zone,
            },
        )

    def update_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[ScwZone] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        size: Optional[int] = None,
    ) -> Volume:
        """
        Update a volume.
        Update the properties of a specified volume.
        :param volume_id: ID of the volume to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: New name for the volume.
        :param tags: New tags for the volume.
        :param size: New size for the volume.
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = api.update_volume(
                volume_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "PATCH",
            f"/instance/v2alpha1/zones/{param_zone}/volumes/{param_volume_id}",
            body=marshal_VolumeApiUpdateVolumeRequest(
                VolumeApiUpdateVolumeRequest(
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
        return unmarshal_Volume(res.json())

    def delete_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete a volume.
        Delete a specified volume.
        :param volume_id: ID of the volume to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_volume(
                volume_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "DELETE",
            f"/instance/v2alpha1/zones/{param_zone}/volumes/{param_volume_id}",
        )

        self._throw_on_error(res)

    def list_snapshots(
        self,
        *,
        zone: Optional[ScwZone] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSnapshotsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        snapshot_ids: Optional[list[str]] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        base_volume_id: Optional[str] = None,
    ) -> ListSnapshotsResponse:
        """
        List snapshots.
        List all snapshots of an Organization.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page_token: Token for pagination.
        :param page_size: Number of snapshots to return per page.
        :param order_by: Field to sort by.
        :param project_id: Filter by Project ID.
        :param snapshot_ids: Filter by specific snapshot IDs.
        :param name: Filter by name.
        :param tags: Filter by tags.
        :param base_volume_id: Filter by base volume ID.
        :return: :class:`ListSnapshotsResponse <ListSnapshotsResponse>`

        Usage:
        ::

            result = api.list_snapshots()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/snapshots",
            params={
                "base_volume_id": base_volume_id,
                "name": name,
                "order_by": order_by,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                "project_id": project_id or self.client.default_project_id,
                "snapshot_ids": snapshot_ids,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSnapshotsResponse(res.json())

    def create_snapshot(
        self,
        *,
        name: str,
        base_volume_id: str,
        public: bool,
        zone: Optional[ScwZone] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> Snapshot:
        """
        Create a snapshot from a specified volume.
        Create a snapshot from a specified l_ssd volume.
        :param name: Name of the snapshot.
        :param base_volume_id: ID of the base volume.
        :param public: Whether the snapshot should be public.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID of the snapshot.
        :param tags: Tags associated with the snapshot.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.create_snapshot(
                name="example",
                base_volume_id="example",
                public=False,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/snapshots",
            body=marshal_VolumeApiCreateSnapshotRequest(
                VolumeApiCreateSnapshotRequest(
                    name=name,
                    base_volume_id=base_volume_id,
                    public=public,
                    zone=zone,
                    project_id=project_id,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    def get_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Snapshot:
        """
        Get a snapshot.
        Get details of a specified snapshot.
        :param snapshot_id: ID of the snapshot to retrieve.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.get_snapshot(
                snapshot_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "GET",
            f"/instance/v2alpha1/zones/{param_zone}/snapshots/{param_snapshot_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    def wait_for_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[ScwZone] = None,
        options: Optional[WaitForOptions[Snapshot, bool]] = None,
    ) -> Snapshot:
        """
        Get a snapshot.
        Get details of a specified snapshot.
        :param snapshot_id: ID of the snapshot to retrieve.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.get_snapshot(
                snapshot_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in SNAPSHOT_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_snapshot,
            options=options,
            args={
                "snapshot_id": snapshot_id,
                "zone": zone,
            },
        )

    def update_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[ScwZone] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        public: Optional[bool] = None,
    ) -> Snapshot:
        """
        Update a snapshot.
        Update the properties of a snapshot.
        :param snapshot_id: ID of the snapshot to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: New name for the snapshot.
        :param tags: New tags for the snapshot.
        :param public: Whether the snapshot should be public.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.update_snapshot(
                snapshot_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "PATCH",
            f"/instance/v2alpha1/zones/{param_zone}/snapshots/{param_snapshot_id}",
            body=marshal_VolumeApiUpdateSnapshotRequest(
                VolumeApiUpdateSnapshotRequest(
                    snapshot_id=snapshot_id,
                    zone=zone,
                    name=name,
                    tags=tags,
                    public=public,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    def delete_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete a snapshot.
        Delete a specified snapshot.
        :param snapshot_id: ID of the snapshot to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_snapshot(
                snapshot_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "DELETE",
            f"/instance/v2alpha1/zones/{param_zone}/snapshots/{param_snapshot_id}",
        )

        self._throw_on_error(res)

    def import_snapshot_from_object_storage(
        self,
        *,
        name: str,
        bucket: str,
        object_key: str,
        zone: Optional[ScwZone] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        size: Optional[int] = None,
        volume_type: Optional[SnapshotVolumeType] = None,
    ) -> Snapshot:
        """
        Import a snapshot from Object Storage.
        Import a snapshot from a QCOW2 file stored in Object Storage.
        :param name: Name of the snapshot.
        :param bucket: Object Storage bucket name.
        :param object_key: Object key.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID of the snapshot.
        :param tags: Tags associated with the snapshot.
        :param size: Size of the imported snapshot in bytes.
        :param volume_type: Volume type of the snapshot.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.import_snapshot_from_object_storage(
                name="example",
                bucket="example",
                object_key="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/snapshots/import-from-object-storage",
            body=marshal_VolumeApiImportSnapshotFromObjectStorageRequest(
                VolumeApiImportSnapshotFromObjectStorageRequest(
                    name=name,
                    bucket=bucket,
                    object_key=object_key,
                    zone=zone,
                    project_id=project_id,
                    tags=tags,
                    size=size,
                    volume_type=volume_type,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    def export_snapshot_to_object_storage(
        self,
        *,
        snapshot_id: str,
        bucket: str,
        object_key: str,
        zone: Optional[ScwZone] = None,
    ) -> Snapshot:
        """
        Export a snapshot to Object Storage.
        Export a snapshot to a specified Object Storage bucket in the same region.
        :param snapshot_id: ID of the snapshot to export.
        :param bucket: Object Storage bucket name.
        :param object_key: Object key.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.export_snapshot_to_object_storage(
                snapshot_id="example",
                bucket="example",
                object_key="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "POST",
            f"/instance/v2alpha1/zones/{param_zone}/snapshots/{param_snapshot_id}/export-to-object-storage",
            body=marshal_VolumeApiExportSnapshotToObjectStorageRequest(
                VolumeApiExportSnapshotToObjectStorageRequest(
                    snapshot_id=snapshot_id,
                    bucket=bucket,
                    object_key=object_key,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())
