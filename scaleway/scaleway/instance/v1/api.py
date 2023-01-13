# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Dict, List, Optional

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
    Arch,
    BootType,
    ImageState,
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
    Bootscript,
    CreateImageResponse,
    CreateIpResponse,
    CreatePlacementGroupResponse,
    CreatePrivateNICResponse,
    CreateSecurityGroupResponse,
    CreateSecurityGroupRuleResponse,
    CreateServerResponse,
    CreateSnapshotResponse,
    CreateVolumeResponse,
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
    PlacementGroup,
    PrivateNIC,
    SecurityGroup,
    SecurityGroupRule,
    SecurityGroupSummary,
    SecurityGroupTemplate,
    Server,
    ServerActionRequestVolumeBackupTemplate,
    ServerActionResponse,
    ServerIp,
    ServerIpv6,
    ServerLocation,
    ServerMaintenance,
    ServerSummary,
    SetPlacementGroupResponse,
    SetPlacementGroupServersResponse,
    SetSecurityGroupRulesRequestRule,
    SetSecurityGroupRulesResponse,
    Snapshot,
    SnapshotBaseVolume,
    UpdateIpResponse,
    UpdatePlacementGroupResponse,
    UpdatePlacementGroupServersResponse,
    UpdateServerResponse,
    UpdateVolumeResponse,
    Volume,
    VolumeServerTemplate,
    VolumeSummary,
    VolumeTemplate,
    ServerActionRequest,
    CreateImageRequest,
    CreateSnapshotRequest,
    ExportSnapshotRequest,
    CreateVolumeRequest,
    UpdateVolumeRequest,
    CreateSecurityGroupRequest,
    CreateSecurityGroupRuleRequest,
    SetSecurityGroupRulesRequest,
    CreatePlacementGroupRequest,
    SetPlacementGroupRequest,
    UpdatePlacementGroupRequest,
    SetPlacementGroupServersRequest,
    UpdatePlacementGroupServersRequest,
    CreateIpRequest,
    UpdateIpRequest,
    CreatePrivateNICRequest,
)
from .types_private import (
    _SetImageResponse,
    _SetSecurityGroupResponse,
    _SetSecurityGroupRuleResponse,
    _SetServerResponse,
    _SetSnapshotResponse,
    _CreateServerRequest,
    _SetServerRequest,
    _UpdateServerRequest,
    _SetImageRequest,
    _SetSnapshotRequest,
    _SetSecurityGroupRequest,
    _SetSecurityGroupRuleRequest,
)
from .marshalling import (
    marshal_CreateImageRequest,
    marshal_CreateIpRequest,
    marshal_CreatePlacementGroupRequest,
    marshal_CreatePrivateNICRequest,
    marshal_CreateSecurityGroupRequest,
    marshal_CreateSecurityGroupRuleRequest,
    marshal_CreateSnapshotRequest,
    marshal_CreateVolumeRequest,
    marshal_ExportSnapshotRequest,
    marshal_ServerActionRequest,
    marshal_SetPlacementGroupRequest,
    marshal_SetPlacementGroupServersRequest,
    marshal_SetSecurityGroupRulesRequest,
    marshal_UpdateIpRequest,
    marshal_UpdatePlacementGroupRequest,
    marshal_UpdatePlacementGroupServersRequest,
    marshal_UpdateVolumeRequest,
    marshal__CreateServerRequest,
    marshal__SetImageRequest,
    marshal__SetSecurityGroupRequest,
    marshal__SetSecurityGroupRuleRequest,
    marshal__SetServerRequest,
    marshal__SetSnapshotRequest,
    marshal__UpdateServerRequest,
    unmarshal_CreateImageResponse,
    unmarshal_CreateIpResponse,
    unmarshal_CreatePlacementGroupResponse,
    unmarshal_CreatePrivateNICResponse,
    unmarshal_CreateSecurityGroupResponse,
    unmarshal_CreateSecurityGroupRuleResponse,
    unmarshal_CreateServerResponse,
    unmarshal_CreateSnapshotResponse,
    unmarshal_CreateVolumeResponse,
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
    unmarshal_ServerActionResponse,
    unmarshal_SetPlacementGroupResponse,
    unmarshal_SetPlacementGroupServersResponse,
    unmarshal_SetSecurityGroupRulesResponse,
    unmarshal_UpdateIpResponse,
    unmarshal_UpdatePlacementGroupResponse,
    unmarshal_UpdatePlacementGroupServersResponse,
    unmarshal_UpdateServerResponse,
    unmarshal_UpdateVolumeResponse,
    unmarshal__SetImageResponse,
    unmarshal__SetSecurityGroupResponse,
    unmarshal__SetSecurityGroupRuleResponse,
    unmarshal__SetServerResponse,
    unmarshal__SetSnapshotResponse,
)


class InstanceV1API(API):
    """
    Instance API.
    """

    def get_server_types_availability(
        self,
        *,
        zone: Optional[Zone] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> GetServerTypesAvailabilityResponse:
        """
        Get availability for all server types.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param per_page:
        :param page:
        :return: :class:`GetServerTypesAvailabilityResponse <GetServerTypesAvailabilityResponse>`

        Usage:
        ::

            result = api.get_server_types_availability()
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

    def list_servers_types(
        self,
        *,
        zone: Optional[Zone] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListServersTypesResponse:
        """
        Get server types technical details.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param per_page:
        :param page:
        :return: :class:`ListServersTypesResponse <ListServersTypesResponse>`

        Usage:
        ::

            result = api.list_servers_types()
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

    def list_volumes_types(
        self,
        *,
        zone: Optional[Zone] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListVolumesTypesResponse:
        """
        Get volumes technical details.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param per_page:
        :param page:
        :return: :class:`ListVolumesTypesResponse <ListVolumesTypesResponse>`

        Usage:
        ::

            result = api.list_volumes_types()
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

    def list_servers(
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
        commercial_type: Optional[str] = None,
        state: ServerState = ServerState.RUNNING,
        tags: Optional[List[str]] = None,
        private_network: Optional[str] = None,
        order: ListServersRequestOrder = ListServersRequestOrder.CREATION_DATE_DESC,
    ) -> ListServersResponse:
        """
        List all servers
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return
        :param page: A positive integer to choose the page to return
        :param organization: List only servers of this organization ID
        :param project: List only servers of this project ID
        :param name: Filter servers by name (for eg. "server1" will return "server100" and "server1" but not "foo")
        :param private_ip: List servers by private_ip
        :param without_ip: List servers that are not attached to a public IP
        :param commercial_type: List servers of this commercial type
        :param state: List servers in this state
        :param tags: List servers with these exact tags (to filter with several tags, use commas to separate them)
        :param private_network: List servers in this Private Network
        :param order: Define the order of the returned servers
        :return: :class:`ListServersResponse <ListServersResponse>`

        Usage:
        ::

            result = api.list_servers()
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
                "project": project or self.client.default_project_id,
                "state": state,
                "tags": ",".join(tags) if tags and len(tags) > 0 else None,
                "without_ip": without_ip,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServersResponse(res.json())

    def list_servers_all(
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
        commercial_type: Optional[str] = None,
        state: Optional[ServerState] = None,
        tags: Optional[List[str]] = None,
        private_network: Optional[str] = None,
        order: Optional[ListServersRequestOrder] = None,
    ) -> List[Server]:
        """
        List all servers
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return
        :param page: A positive integer to choose the page to return
        :param organization: List only servers of this organization ID
        :param project: List only servers of this project ID
        :param name: Filter servers by name (for eg. "server1" will return "server100" and "server1" but not "foo")
        :param private_ip: List servers by private_ip
        :param without_ip: List servers that are not attached to a public IP
        :param commercial_type: List servers of this commercial type
        :param state: List servers in this state
        :param tags: List servers with these exact tags (to filter with several tags, use commas to separate them)
        :param private_network: List servers in this Private Network
        :param order: Define the order of the returned servers
        :return: :class:`List[ListServersResponse] <List[ListServersResponse]>`

        Usage:
        ::

            result = api.list_servers_all()
        """

        return fetch_all_pages(
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
                "commercial_type": commercial_type,
                "state": state,
                "tags": tags,
                "private_network": private_network,
                "order": order,
            },
        )

    def _create_server(
        self,
        *,
        commercial_type: str,
        image: str,
        enable_ipv6: bool,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        dynamic_ip_required: Optional[bool] = None,
        volumes: Optional[Dict[str, VolumeServerTemplate]] = None,
        public_ip: Optional[str] = None,
        boot_type: Optional[BootType] = None,
        bootscript: Optional[str] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        security_group: Optional[str] = None,
        placement_group: Optional[str] = None,
    ) -> CreateServerResponse:
        """
        The `volumes` key is a dictionary composed of the volume position as key and the volume parameters as value.
        Depending of the volume parameters, you can achieve different behaviours :

        Create a volume from a snapshot of an image :
        Optional : `volume_type`, `size`, `boot`.
        If the `size` parameter is not set, the size of the volume will equal the size of the corresponding snapshot of the image.

        Attach an existing volume :
        Required : `id`, `name`.
        Optional : `boot`.

        Create an empty volume :
        Required : `name`, `volume_type`, `size`.
        Optional : `organization`, `project`, `boot`.

        Create a volume from a snapshot :
        Required : `base_snapshot`, `name`, `volume_type`.
        Optional : `organization`, `project`, `boot`.

        :param zone: Zone to target. If none is passed will use default zone from the config
        :param name: The server name
        :param dynamic_ip_required: Define if a dynamic IP is required for the instance
        :param commercial_type: Define the server commercial type (i.e. GP1-S)
        :param image: The server image ID or label
        :param volumes: The volumes attached to the server
        :param enable_ipv6: True if IPv6 is enabled on the server
        :param public_ip: The ID of the reserved IP to attach to the server
        :param boot_type: The boot type to use
        :param bootscript: The bootscript ID to use when `boot_type` is set to `bootscript`
        :param organization: The server organization ID.

        One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
        :param project: The server project ID.

        One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
        :param tags: The server tags
        :param security_group: The security group ID
        :param placement_group: Placement group ID if server must be part of a placement group
        :return: :class:`CreateServerResponse <CreateServerResponse>`

        Usage:
        ::

            result = api._create_server(
                commercial_type="example",
                image="example",
                enable_ipv6=True,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/servers",
            body=marshal__CreateServerRequest(
                _CreateServerRequest(
                    commercial_type=commercial_type,
                    image=image,
                    enable_ipv6=enable_ipv6,
                    zone=zone,
                    name=name or random_name(prefix="srv"),
                    dynamic_ip_required=dynamic_ip_required,
                    volumes=volumes,
                    public_ip=public_ip,
                    boot_type=boot_type,
                    bootscript=bootscript,
                    organization=organization,
                    project=project,
                    tags=tags,
                    security_group=security_group,
                    placement_group=placement_group,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateServerResponse(res.json())

    def delete_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a server with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id:

        Usage:
        ::

            result = api.delete_server(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}",
        )

        self._throw_on_error(res)
        return None

    def get_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> GetServerResponse:
        """
        Get the details of a specified Server.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: UUID of the server you want to get
        :return: :class:`GetServerResponse <GetServerResponse>`

        Usage:
        ::

            result = api.get_server(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetServerResponse(res.json())

    def _set_server(
        self,
        *,
        id: str,
        name: str,
        commercial_type: str,
        dynamic_ip_required: bool,
        enable_ipv6: bool,
        hostname: str,
        protected: bool,
        state: ServerState,
        boot_type: BootType,
        state_detail: str,
        arch: Arch,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        allowed_actions: Optional[List[ServerAction]] = None,
        tags: Optional[List[str]] = None,
        creation_date: Optional[datetime] = None,
        image: Optional[Image] = None,
        private_ip: Optional[str] = None,
        public_ip: Optional[ServerIp] = None,
        modification_date: Optional[datetime] = None,
        location: Optional[ServerLocation] = None,
        ipv6: Optional[ServerIpv6] = None,
        bootscript: Optional[Bootscript] = None,
        volumes: Optional[Dict[str, Volume]] = None,
        security_group: Optional[SecurityGroupSummary] = None,
        maintenances: Optional[List[ServerMaintenance]] = None,
        placement_group: Optional[PlacementGroup] = None,
        private_nics: Optional[List[PrivateNIC]] = None,
    ) -> _SetServerResponse:
        """

        Usage:
        ::

            result = api._set_server(
                id="example",
                name="example",
                commercial_type="example",
                dynamic_ip_required=True,
                enable_ipv6=True,
                hostname="example",
                protected=True,
                state=running,
                boot_type=local,
                state_detail="example",
                arch=x86_64,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_id = validate_path_param("id", id)

        res = self._request(
            "PUT",
            f"/instance/v1/zones/{param_zone}/servers/{param_id}",
            body=marshal__SetServerRequest(
                _SetServerRequest(
                    id=id,
                    name=name,
                    commercial_type=commercial_type,
                    dynamic_ip_required=dynamic_ip_required,
                    enable_ipv6=enable_ipv6,
                    hostname=hostname,
                    protected=protected,
                    state=state,
                    boot_type=boot_type,
                    state_detail=state_detail,
                    arch=arch,
                    zone=zone,
                    organization=organization,
                    project=project,
                    allowed_actions=allowed_actions,
                    tags=tags,
                    creation_date=creation_date,
                    image=image,
                    private_ip=private_ip,
                    public_ip=public_ip,
                    modification_date=modification_date,
                    location=location,
                    ipv6=ipv6,
                    bootscript=bootscript,
                    volumes=volumes,
                    security_group=security_group,
                    maintenances=maintenances,
                    placement_group=placement_group,
                    private_nics=private_nics,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal__SetServerResponse(res.json())

    def _update_server(
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
        enable_ipv6: Optional[bool] = None,
        protected: Optional[bool] = None,
        security_group: Optional[SecurityGroupTemplate] = None,
        placement_group: Optional[str] = None,
        private_nics: Optional[List[PrivateNIC]] = None,
    ) -> UpdateServerResponse:
        """
        Update a server
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: UUID of the server
        :param name: Name of the server
        :param boot_type:
        :param tags: Tags of the server
        :param volumes:
        :param bootscript:
        :param dynamic_ip_required:
        :param enable_ipv6:
        :param protected:
        :param security_group:
        :param placement_group: Placement group ID if server must be part of a placement group
        :param private_nics: The server private NICs
        :return: :class:`UpdateServerResponse <UpdateServerResponse>`

        Usage:
        ::

            result = api._update_server(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "PATCH",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}",
            body=marshal__UpdateServerRequest(
                _UpdateServerRequest(
                    server_id=server_id,
                    zone=zone,
                    name=name,
                    boot_type=boot_type,
                    tags=tags,
                    volumes=volumes,
                    bootscript=bootscript,
                    dynamic_ip_required=dynamic_ip_required,
                    enable_ipv6=enable_ipv6,
                    protected=protected,
                    security_group=security_group,
                    placement_group=placement_group,
                    private_nics=private_nics,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_UpdateServerResponse(res.json())

    def list_server_actions(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> ListServerActionsResponse:
        """
        List all actions that can currently be performed on a server.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id:
        :return: :class:`ListServerActionsResponse <ListServerActionsResponse>`

        Usage:
        ::

            result = api.list_server_actions(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/action",
        )

        self._throw_on_error(res)
        return unmarshal_ListServerActionsResponse(res.json())

    def server_action(
        self,
        *,
        server_id: str,
        action: ServerAction,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        volumes: Optional[Dict[str, ServerActionRequestVolumeBackupTemplate]] = None,
    ) -> ServerActionResponse:
        """
        Perform power related actions on a server. Be wary that when terminating a server, all the attached volumes (local *and* block storage) are deleted. So, if you want to keep your local volumes, you must use the `archive` action instead of `terminate`. And if you want to keep block-storage volumes, **you must** detach it beforehand you issue the `terminate` call.  For more information, read the [Volumes](#volumes-7e8a39) documentation.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: UUID of the server
        :param action: The action to perform on the server
        :param name: The name of the backup you want to create.
        This field should only be specified when performing a backup action.

        :param volumes: For each volume UUID, the snapshot parameters of the volume.
        This field should only be specified when performing a backup action.

        :return: :class:`ServerActionResponse <ServerActionResponse>`

        Usage:
        ::

            result = api.server_action(
                server_id="example",
                action=poweron,
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
                    action=action,
                    zone=zone,
                    name=name,
                    volumes=volumes,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ServerActionResponse(res.json())

    def list_server_user_data(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> ListServerUserDataResponse:
        """
        List all user data keys registered on a given server.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: UUID of the server
        :return: :class:`ListServerUserDataResponse <ListServerUserDataResponse>`

        Usage:
        ::

            result = api.list_server_user_data(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/user_data",
        )

        self._throw_on_error(res)
        return unmarshal_ListServerUserDataResponse(res.json())

    def delete_server_user_data(
        self,
        *,
        server_id: str,
        key: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete the given key from a server user data.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: UUID of the server
        :param key: Key of the user data to delete

        Usage:
        ::

            result = api.delete_server_user_data(
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
        return None

    def list_images(
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
        List all images available in an account.
        :param zone: Zone to target. If none is passed will use default zone from the config
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

            result = api.list_images()
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

    def list_images_all(
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
        List all images available in an account.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param organization:
        :param per_page:
        :param page:
        :param name:
        :param public:
        :param arch:
        :param project:
        :param tags:
        :return: :class:`List[ListImagesResponse] <List[ListImagesResponse]>`

        Usage:
        ::

            result = api.list_images_all()
        """

        return fetch_all_pages(
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

    def get_image(
        self,
        *,
        image_id: str,
        zone: Optional[Zone] = None,
    ) -> GetImageResponse:
        """
        Get details of an image with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param image_id: UUID of the image you want to get
        :return: :class:`GetImageResponse <GetImageResponse>`

        Usage:
        ::

            result = api.get_image(image_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_image_id = validate_path_param("image_id", image_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/images/{param_image_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetImageResponse(res.json())

    def create_image(
        self,
        *,
        root_volume: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        arch: Arch = Arch.X86_64,
        default_bootscript: Optional[str] = None,
        extra_volumes: Optional[Dict[str, VolumeTemplate]] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        public: Optional[bool] = None,
    ) -> CreateImageResponse:
        """
        Create an instance image
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param name: Name of the image
        :param root_volume: UUID of the snapshot
        :param arch: Architecture of the image
        :param default_bootscript: Default bootscript of the image
        :param extra_volumes: Additional volumes of the image
        :param organization: Organization ID of the image.

        One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
        :param project: Project ID of the image.

        One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
        :param tags: The tags of the image
        :param public: True to create a public image
        :return: :class:`CreateImageResponse <CreateImageResponse>`

        Usage:
        ::

            result = api.create_image(root_volume="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/images",
            body=marshal_CreateImageRequest(
                CreateImageRequest(
                    root_volume=root_volume,
                    zone=zone,
                    name=name or random_name(prefix="img"),
                    arch=arch,
                    default_bootscript=default_bootscript,
                    extra_volumes=extra_volumes,
                    organization=organization,
                    project=project,
                    tags=tags,
                    public=public,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateImageResponse(res.json())

    def _set_image(
        self,
        *,
        id: str,
        name: str,
        arch: Arch,
        from_server: str,
        public: bool,
        state: ImageState,
        zone: Optional[Zone] = None,
        creation_date: Optional[datetime] = None,
        modification_date: Optional[datetime] = None,
        default_bootscript: Optional[Bootscript] = None,
        extra_volumes: Optional[Dict[str, Volume]] = None,
        organization: Optional[str] = None,
        root_volume: Optional[VolumeSummary] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> _SetImageResponse:
        """
        Replace all image properties with an image message.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param id:
        :param name:
        :param arch:
        :param creation_date:
        :param modification_date:
        :param default_bootscript:
        :param extra_volumes:
        :param from_server:
        :param organization:
        :param public:
        :param root_volume:
        :param state:
        :param project:
        :param tags:
        :return: :class:`_SetImageResponse <_SetImageResponse>`

        Usage:
        ::

            result = api._set_image(
                id="example",
                name="example",
                arch=x86_64,
                from_server="example",
                public=True,
                state=available,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_id = validate_path_param("id", id)

        res = self._request(
            "PUT",
            f"/instance/v1/zones/{param_zone}/images/{param_id}",
            body=marshal__SetImageRequest(
                _SetImageRequest(
                    id=id,
                    name=name,
                    arch=arch,
                    from_server=from_server,
                    public=public,
                    state=state,
                    zone=zone,
                    creation_date=creation_date,
                    modification_date=modification_date,
                    default_bootscript=default_bootscript,
                    extra_volumes=extra_volumes,
                    organization=organization,
                    root_volume=root_volume,
                    project=project,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal__SetImageResponse(res.json())

    def delete_image(
        self,
        *,
        image_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete the image with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param image_id: UUID of the image you want to delete

        Usage:
        ::

            result = api.delete_image(image_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_image_id = validate_path_param("image_id", image_id)

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/images/{param_image_id}",
        )

        self._throw_on_error(res)
        return None

    def list_snapshots(
        self,
        *,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        name: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[str] = None,
    ) -> ListSnapshotsResponse:
        """
        List snapshots
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param organization:
        :param per_page:
        :param page:
        :param name:
        :param project:
        :param tags:
        :return: :class:`ListSnapshotsResponse <ListSnapshotsResponse>`

        Usage:
        ::

            result = api.list_snapshots()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/snapshots",
            params={
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

    def list_snapshots_all(
        self,
        *,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        name: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[str] = None,
    ) -> List[Snapshot]:
        """
        List snapshots
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param organization:
        :param per_page:
        :param page:
        :param name:
        :param project:
        :param tags:
        :return: :class:`List[ListSnapshotsResponse] <List[ListSnapshotsResponse]>`

        Usage:
        ::

            result = api.list_snapshots_all()
        """

        return fetch_all_pages(
            type=ListSnapshotsResponse,
            key="snapshots",
            fetcher=self.list_snapshots,
            args={
                "zone": zone,
                "organization": organization,
                "per_page": per_page,
                "page": page,
                "name": name,
                "project": project,
                "tags": tags,
            },
        )

    def create_snapshot(
        self,
        *,
        volume_type: SnapshotVolumeType,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        volume_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        bucket: Optional[str] = None,
        key: Optional[str] = None,
        size: Optional[int] = None,
    ) -> CreateSnapshotResponse:
        """
        Create a snapshot from a given volume or from a QCOW2 file
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param name: Name of the snapshot
        :param volume_id: UUID of the volume
        :param tags: The tags of the snapshot
        :param organization: Organization ID of the snapshot.

        One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
        :param project: Project ID of the snapshot.

        One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
        :param volume_type: Overrides the volume_type of the snapshot.
        If omitted, the volume type of the original volume will be used.

        :param bucket: Bucket name for snapshot imports
        :param key: Object key for snapshot imports
        :param size: Imported snapshot size, must be a multiple of 512
        :return: :class:`CreateSnapshotResponse <CreateSnapshotResponse>`

        Usage:
        ::

            result = api.create_snapshot(volume_type=unknown_volume_type)
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/snapshots",
            body=marshal_CreateSnapshotRequest(
                CreateSnapshotRequest(
                    volume_type=volume_type,
                    zone=zone,
                    name=name or random_name(prefix="snp"),
                    volume_id=volume_id,
                    tags=tags,
                    organization=organization,
                    project=project,
                    bucket=bucket,
                    key=key,
                    size=size,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateSnapshotResponse(res.json())

    def get_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[Zone] = None,
    ) -> GetSnapshotResponse:
        """
        Get details of a snapshot with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param snapshot_id: UUID of the snapshot you want to get
        :return: :class:`GetSnapshotResponse <GetSnapshotResponse>`

        Usage:
        ::

            result = api.get_snapshot(snapshot_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/snapshots/{param_snapshot_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetSnapshotResponse(res.json())

    def _set_snapshot(
        self,
        *,
        snapshot_id: str,
        id: str,
        name: str,
        volume_type: VolumeVolumeType,
        size: int,
        state: SnapshotState,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        base_volume: Optional[SnapshotBaseVolume] = None,
        creation_date: Optional[datetime] = None,
        modification_date: Optional[datetime] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> _SetSnapshotResponse:
        """
        Replace all snapshot properties with a snapshot message.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param snapshot_id:
        :param id:
        :param name:
        :param organization:
        :param volume_type:
        :param size:
        :param state:
        :param base_volume:
        :param creation_date:
        :param modification_date:
        :param project:
        :param tags:
        :return: :class:`_SetSnapshotResponse <_SetSnapshotResponse>`

        Usage:
        ::

            result = api._set_snapshot(
                snapshot_id="example",
                id="example",
                name="example",
                volume_type=l_ssd,
                size=1,
                state=available,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "PUT",
            f"/instance/v1/zones/{param_zone}/snapshots/{param_snapshot_id}",
            body=marshal__SetSnapshotRequest(
                _SetSnapshotRequest(
                    snapshot_id=snapshot_id,
                    id=id,
                    name=name,
                    volume_type=volume_type,
                    size=size,
                    state=state,
                    zone=zone,
                    organization=organization,
                    base_volume=base_volume,
                    creation_date=creation_date,
                    modification_date=modification_date,
                    project=project,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal__SetSnapshotResponse(res.json())

    def delete_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete the snapshot with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param snapshot_id: UUID of the snapshot you want to delete

        Usage:
        ::

            result = api.delete_snapshot(snapshot_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/snapshots/{param_snapshot_id}",
        )

        self._throw_on_error(res)
        return None

    def export_snapshot(
        self,
        *,
        snapshot_id: str,
        bucket: str,
        key: str,
        zone: Optional[Zone] = None,
    ) -> ExportSnapshotResponse:
        """
        Export a snapshot to a given S3 bucket in the same region.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param snapshot_id: The snapshot ID
        :param bucket: S3 bucket name
        :param key: S3 object key
        :return: :class:`ExportSnapshotResponse <ExportSnapshotResponse>`

        Usage:
        ::

            result = api.export_snapshot(
                snapshot_id="example",
                bucket="example",
                key="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/snapshots/{param_snapshot_id}/export",
            body=marshal_ExportSnapshotRequest(
                ExportSnapshotRequest(
                    snapshot_id=snapshot_id,
                    bucket=bucket,
                    key=key,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ExportSnapshotResponse(res.json())

    def list_volumes(
        self,
        *,
        zone: Optional[Zone] = None,
        volume_type: VolumeVolumeType = VolumeVolumeType.L_SSD,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
    ) -> ListVolumesResponse:
        """
        List volumes
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param volume_type: Filter by volume type
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return
        :param page: A positive integer to choose the page to return
        :param organization: Filter volume by organization ID
        :param project: Filter volume by project ID
        :param tags: Filter volumes with these exact tags (to filter with several tags, use commas to separate them)
        :param name: Filter volume by name (for eg. "vol" will return "myvolume" but not "data")
        :return: :class:`ListVolumesResponse <ListVolumesResponse>`

        Usage:
        ::

            result = api.list_volumes()
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

    def list_volumes_all(
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
        List volumes
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param volume_type: Filter by volume type
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return
        :param page: A positive integer to choose the page to return
        :param organization: Filter volume by organization ID
        :param project: Filter volume by project ID
        :param tags: Filter volumes with these exact tags (to filter with several tags, use commas to separate them)
        :param name: Filter volume by name (for eg. "vol" will return "myvolume" but not "data")
        :return: :class:`List[ListVolumesResponse] <List[ListVolumesResponse]>`

        Usage:
        ::

            result = api.list_volumes_all()
        """

        return fetch_all_pages(
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

    def create_volume(
        self,
        *,
        volume_type: VolumeVolumeType,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        size: Optional[int] = None,
        base_volume: Optional[str] = None,
        base_snapshot: Optional[str] = None,
    ) -> CreateVolumeResponse:
        """
        Create a volume
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param name: The volume name
        :param organization: The volume organization ID.

        One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
        :param project: The volume project ID.

        One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
        :param tags: The volume tags
        :param volume_type: The volume type
        :param size: The volume disk size, must be a multiple of 512.

        One-of ('from_'): at most one of 'size', 'base_volume', 'base_snapshot' could be set.
        :param base_volume: The ID of the volume on which this volume will be based.

        One-of ('from_'): at most one of 'size', 'base_volume', 'base_snapshot' could be set.
        :param base_snapshot: The ID of the snapshot on which this volume will be based.

        One-of ('from_'): at most one of 'size', 'base_volume', 'base_snapshot' could be set.
        :return: :class:`CreateVolumeResponse <CreateVolumeResponse>`

        Usage:
        ::

            result = api.create_volume(volume_type=l_ssd)
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/volumes",
            body=marshal_CreateVolumeRequest(
                CreateVolumeRequest(
                    volume_type=volume_type,
                    zone=zone,
                    name=name or random_name(prefix="vol"),
                    organization=organization,
                    project=project,
                    tags=tags,
                    size=size,
                    base_volume=base_volume,
                    base_snapshot=base_snapshot,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateVolumeResponse(res.json())

    def get_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[Zone] = None,
    ) -> GetVolumeResponse:
        """
        Get details of a volume with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param volume_id: UUID of the volume you want to get
        :return: :class:`GetVolumeResponse <GetVolumeResponse>`

        Usage:
        ::

            result = api.get_volume(volume_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/volumes/{param_volume_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetVolumeResponse(res.json())

    def update_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        size: Optional[int] = None,
    ) -> UpdateVolumeResponse:
        """
        Replace name and/or size properties of given ID volume with the given value(s). Any volume name can be changed while, for now, only `b_ssd` volume growing is supported.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param volume_id: UUID of the volume
        :param name: The volume name
        :param tags: The tags of the volume
        :param size: The volume disk size, must be a multiple of 512
        :return: :class:`UpdateVolumeResponse <UpdateVolumeResponse>`

        Usage:
        ::

            result = api.update_volume(volume_id="example")
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

    def delete_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete the volume with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param volume_id: UUID of the volume you want to delete

        Usage:
        ::

            result = api.delete_volume(volume_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/volumes/{param_volume_id}",
        )

        self._throw_on_error(res)
        return None

    def list_security_groups(
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
        List all security groups available in an account.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param name: Name of the security group
        :param organization: The security group organization ID
        :param project: The security group project ID
        :param tags: List security groups with these exact tags (to filter with several tags, use commas to separate them)
        :param project_default: Filter security groups with this value for project_default
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return
        :param page: A positive integer to choose the page to return
        :return: :class:`ListSecurityGroupsResponse <ListSecurityGroupsResponse>`

        Usage:
        ::

            result = api.list_security_groups()
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

    def list_security_groups_all(
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
        List all security groups available in an account.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param name: Name of the security group
        :param organization: The security group organization ID
        :param project: The security group project ID
        :param tags: List security groups with these exact tags (to filter with several tags, use commas to separate them)
        :param project_default: Filter security groups with this value for project_default
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return
        :param page: A positive integer to choose the page to return
        :return: :class:`List[ListSecurityGroupsResponse] <List[ListSecurityGroupsResponse]>`

        Usage:
        ::

            result = api.list_security_groups_all()
        """

        return fetch_all_pages(
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

    def create_security_group(
        self,
        *,
        description: str,
        stateful: bool,
        inbound_default_policy: SecurityGroupPolicy,
        outbound_default_policy: SecurityGroupPolicy,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        organization_default: Optional[bool] = None,
        project_default: Optional[bool] = None,
        enable_default_security: Optional[bool] = None,
    ) -> CreateSecurityGroupResponse:
        """
        Create a security group
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param name: Name of the security group
        :param description: Description of the security group
        :param organization: Organization ID the security group belongs to.

        One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
        :param project: Project ID the security group belong to.

        One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
        :param tags: The tags of the security group
        :param organization_default: Whether this security group becomes the default security group for new instances.

        One-of ('default_identifier'): at most one of 'organization_default', 'project_default' could be set.
        :param project_default: Whether this security group becomes the default security group for new instances.

        One-of ('default_identifier'): at most one of 'organization_default', 'project_default' could be set.
        :param stateful: Whether the security group is stateful or not
        :param inbound_default_policy: Default policy for inbound rules
        :param outbound_default_policy: Default policy for outbound rules
        :param enable_default_security: True to block SMTP on IPv4 and IPv6
        :return: :class:`CreateSecurityGroupResponse <CreateSecurityGroupResponse>`

        Usage:
        ::

            result = api.create_security_group(
                description="example",
                stateful=True,
                inbound_default_policy=accept,
                outbound_default_policy=accept,
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
                    inbound_default_policy=inbound_default_policy,
                    outbound_default_policy=outbound_default_policy,
                    zone=zone,
                    name=name or random_name(prefix="sg"),
                    organization=organization,
                    project=project,
                    tags=tags,
                    organization_default=organization_default,
                    project_default=project_default,
                    enable_default_security=enable_default_security,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateSecurityGroupResponse(res.json())

    def get_security_group(
        self,
        *,
        security_group_id: str,
        zone: Optional[Zone] = None,
    ) -> GetSecurityGroupResponse:
        """
        Get the details of a Security Group with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param security_group_id: UUID of the security group you want to get
        :return: :class:`GetSecurityGroupResponse <GetSecurityGroupResponse>`

        Usage:
        ::

            result = api.get_security_group(security_group_id="example")
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

    def delete_security_group(
        self,
        *,
        security_group_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a security group
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param security_group_id: UUID of the security group you want to delete

        Usage:
        ::

            result = api.delete_security_group(security_group_id="example")
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
        return None

    def _set_security_group(
        self,
        *,
        id: str,
        name: str,
        description: str,
        enable_default_security: bool,
        inbound_default_policy: SecurityGroupPolicy,
        outbound_default_policy: SecurityGroupPolicy,
        project_default: bool,
        stateful: bool,
        zone: Optional[Zone] = None,
        tags: Optional[List[str]] = None,
        creation_date: Optional[datetime] = None,
        modification_date: Optional[datetime] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        organization_default: Optional[bool] = None,
        servers: Optional[List[ServerSummary]] = None,
    ) -> _SetSecurityGroupResponse:
        """
        Replace all security group properties with a security group message.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param id: The ID of the security group (will be ignored)
        :param name: The name of the security group
        :param tags: The tags of the security group
        :param creation_date: The creation date of the security group (will be ignored)
        :param modification_date: The modification date of the security group (will be ignored)
        :param description: The description of the security group
        :param enable_default_security: True to block SMTP on IPv4 and IPv6
        :param inbound_default_policy: The default inbound policy
        :param outbound_default_policy: The default outbound policy
        :param organization: The security groups organization ID
        :param project: The security group project ID
        :param organization_default: Please use project_default instead
        :param project_default: True use this security group for future instances created in this project
        :param servers: The servers attached to this security group
        :param stateful: True to set the security group as stateful
        :return: :class:`_SetSecurityGroupResponse <_SetSecurityGroupResponse>`

        Usage:
        ::

            result = api._set_security_group(
                id="example",
                name="example",
                description="example",
                enable_default_security=True,
                inbound_default_policy=accept,
                outbound_default_policy=accept,
                project_default=True,
                stateful=True,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_id = validate_path_param("id", id)

        res = self._request(
            "PUT",
            f"/instance/v1/zones/{param_zone}/security_groups/{param_id}",
            body=marshal__SetSecurityGroupRequest(
                _SetSecurityGroupRequest(
                    id=id,
                    name=name,
                    description=description,
                    enable_default_security=enable_default_security,
                    inbound_default_policy=inbound_default_policy,
                    outbound_default_policy=outbound_default_policy,
                    project_default=project_default,
                    stateful=stateful,
                    zone=zone,
                    tags=tags,
                    creation_date=creation_date,
                    modification_date=modification_date,
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

    def list_default_security_group_rules(
        self,
        *,
        zone: Optional[Zone] = None,
    ) -> ListSecurityGroupRulesResponse:
        """
        Lists the default rules applied to all the security groups.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :return: :class:`ListSecurityGroupRulesResponse <ListSecurityGroupRulesResponse>`

        Usage:
        ::

            result = api.list_default_security_group_rules()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/security_groups/default/rules",
        )

        self._throw_on_error(res)
        return unmarshal_ListSecurityGroupRulesResponse(res.json())

    def list_security_group_rules(
        self,
        *,
        security_group_id: str,
        zone: Optional[Zone] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListSecurityGroupRulesResponse:
        """
        List rules
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param security_group_id: UUID of the security group
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return
        :param page: A positive integer to choose the page to return
        :return: :class:`ListSecurityGroupRulesResponse <ListSecurityGroupRulesResponse>`

        Usage:
        ::

            result = api.list_security_group_rules(security_group_id="example")
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

    def list_security_group_rules_all(
        self,
        *,
        security_group_id: str,
        zone: Optional[Zone] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[SecurityGroupRule]:
        """
        List rules
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param security_group_id: UUID of the security group
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return
        :param page: A positive integer to choose the page to return
        :return: :class:`List[ListSecurityGroupRulesResponse] <List[ListSecurityGroupRulesResponse]>`

        Usage:
        ::

            result = api.list_security_group_rules_all(security_group_id="example")
        """

        return fetch_all_pages(
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

    def create_security_group_rule(
        self,
        *,
        security_group_id: str,
        ip_range: str,
        position: int,
        editable: bool,
        zone: Optional[Zone] = None,
        protocol: SecurityGroupRuleProtocol = SecurityGroupRuleProtocol.TCP,
        direction: SecurityGroupRuleDirection = SecurityGroupRuleDirection.INBOUND,
        action: SecurityGroupRuleAction = SecurityGroupRuleAction.ACCEPT,
        dest_port_from: Optional[int] = None,
        dest_port_to: Optional[int] = None,
    ) -> CreateSecurityGroupRuleResponse:
        """
        Create rule
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param security_group_id: UUID of the security group
        :param protocol:
        :param direction:
        :param action:
        :param ip_range:
        :param dest_port_from: The beginning of the range of ports to apply this rule to (inclusive)
        :param dest_port_to: The end of the range of ports to apply this rule to (inclusive)
        :param position: The position of this rule in the security group rules list
        :param editable: Indicates if this rule is editable (will be ignored)
        :return: :class:`CreateSecurityGroupRuleResponse <CreateSecurityGroupRuleResponse>`

        Usage:
        ::

            result = api.create_security_group_rule(
                security_group_id="example",
                ip_range="example",
                position=1,
                editable=True,
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
        return unmarshal_CreateSecurityGroupRuleResponse(res.json())

    def set_security_group_rules(
        self,
        *,
        security_group_id: str,
        zone: Optional[Zone] = None,
        rules: Optional[List[SetSecurityGroupRulesRequestRule]] = None,
    ) -> SetSecurityGroupRulesResponse:
        """
        Replaces the rules of the security group with the rules provided. This endpoint supports the update of existing rules, creation of new rules and deletion of existing rules when they are not passed in the request.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param security_group_id: UUID of the security group to update the rules on
        :param rules: List of rules to update in the security group
        :return: :class:`SetSecurityGroupRulesResponse <SetSecurityGroupRulesResponse>`

        Usage:
        ::

            result = api.set_security_group_rules(security_group_id="example")
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

    def delete_security_group_rule(
        self,
        *,
        security_group_id: str,
        security_group_rule_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a security group rule with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param security_group_id:
        :param security_group_rule_id:

        Usage:
        ::

            result = api.delete_security_group_rule(
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
        return None

    def get_security_group_rule(
        self,
        *,
        security_group_id: str,
        security_group_rule_id: str,
        zone: Optional[Zone] = None,
    ) -> GetSecurityGroupRuleResponse:
        """
        Get details of a security group rule with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param security_group_id:
        :param security_group_rule_id:
        :return: :class:`GetSecurityGroupRuleResponse <GetSecurityGroupRuleResponse>`

        Usage:
        ::

            result = api.get_security_group_rule(
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

    def _set_security_group_rule(
        self,
        *,
        security_group_id: str,
        security_group_rule_id: str,
        id: str,
        protocol: SecurityGroupRuleProtocol,
        direction: SecurityGroupRuleDirection,
        action: SecurityGroupRuleAction,
        ip_range: str,
        position: int,
        editable: bool,
        zone: Optional[Zone] = None,
        dest_port_from: Optional[int] = None,
        dest_port_to: Optional[int] = None,
    ) -> _SetSecurityGroupRuleResponse:
        """
        Update security group rule
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param security_group_id:
        :param security_group_rule_id:
        :param id:
        :param protocol:
        :param direction:
        :param action:
        :param ip_range:
        :param dest_port_from:
        :param dest_port_to:
        :param position:
        :param editable:
        :return: :class:`_SetSecurityGroupRuleResponse <_SetSecurityGroupRuleResponse>`

        Usage:
        ::

            result = api._set_security_group_rule(
                security_group_id="example",
                security_group_rule_id="example",
                id="example",
                protocol=TCP,
                direction=inbound,
                action=accept,
                ip_range="example",
                position=1,
                editable=True,
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
        return unmarshal__SetSecurityGroupRuleResponse(res.json())

    def list_placement_groups(
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
        List all placement groups.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return
        :param page: A positive integer to choose the page to return
        :param organization: List only placement groups of this organization ID
        :param project: List only placement groups of this project ID
        :param tags: List placement groups with these exact tags (to filter with several tags, use commas to separate them)
        :param name: Filter placement groups by name (for eg. "cluster1" will return "cluster100" and "cluster1" but not "foo")
        :return: :class:`ListPlacementGroupsResponse <ListPlacementGroupsResponse>`

        Usage:
        ::

            result = api.list_placement_groups()
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

    def list_placement_groups_all(
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
        List all placement groups.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return
        :param page: A positive integer to choose the page to return
        :param organization: List only placement groups of this organization ID
        :param project: List only placement groups of this project ID
        :param tags: List placement groups with these exact tags (to filter with several tags, use commas to separate them)
        :param name: Filter placement groups by name (for eg. "cluster1" will return "cluster100" and "cluster1" but not "foo")
        :return: :class:`List[ListPlacementGroupsResponse] <List[ListPlacementGroupsResponse]>`

        Usage:
        ::

            result = api.list_placement_groups_all()
        """

        return fetch_all_pages(
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

    def create_placement_group(
        self,
        *,
        policy_mode: PlacementGroupPolicyMode,
        policy_type: PlacementGroupPolicyType,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> CreatePlacementGroupResponse:
        """
        Create a new placement group.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param name: Name of the placement group
        :param organization: Organization ID of the placement group.

        One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
        :param project: Project ID of the placement group.

        One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
        :param tags: The tags of the placement group
        :param policy_mode: The operating mode of the placement group
        :param policy_type: The policy type of the placement group
        :return: :class:`CreatePlacementGroupResponse <CreatePlacementGroupResponse>`

        Usage:
        ::

            result = api.create_placement_group(
                policy_mode=optional,
                policy_type=max_availability,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/placement_groups",
            body=marshal_CreatePlacementGroupRequest(
                CreatePlacementGroupRequest(
                    policy_mode=policy_mode,
                    policy_type=policy_type,
                    zone=zone,
                    name=name or random_name(prefix="pg"),
                    organization=organization,
                    project=project,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreatePlacementGroupResponse(res.json())

    def get_placement_group(
        self,
        *,
        placement_group_id: str,
        zone: Optional[Zone] = None,
    ) -> GetPlacementGroupResponse:
        """
        Get the given placement group.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param placement_group_id: UUID of the placement group you want to get
        :return: :class:`GetPlacementGroupResponse <GetPlacementGroupResponse>`

        Usage:
        ::

            result = api.get_placement_group(placement_group_id="example")
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

    def set_placement_group(
        self,
        *,
        placement_group_id: str,
        name: str,
        policy_mode: PlacementGroupPolicyMode,
        policy_type: PlacementGroupPolicyType,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> SetPlacementGroupResponse:
        """
        Set all parameters of the given placement group.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param placement_group_id:
        :param name:
        :param organization:
        :param policy_mode:
        :param policy_type:
        :param project:
        :param tags:
        :return: :class:`SetPlacementGroupResponse <SetPlacementGroupResponse>`

        Usage:
        ::

            result = api.set_placement_group(
                placement_group_id="example",
                name="example",
                policy_mode=optional,
                policy_type=max_availability,
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
                    policy_mode=policy_mode,
                    policy_type=policy_type,
                    zone=zone,
                    organization=organization,
                    project=project,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetPlacementGroupResponse(res.json())

    def update_placement_group(
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
        Update one or more parameter of the given placement group.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param placement_group_id: UUID of the placement group
        :param name: Name of the placement group
        :param tags: The tags of the placement group
        :param policy_mode: The operating mode of the placement group
        :param policy_type: The policy type of the placement group
        :return: :class:`UpdatePlacementGroupResponse <UpdatePlacementGroupResponse>`

        Usage:
        ::

            result = api.update_placement_group(placement_group_id="example")
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

    def delete_placement_group(
        self,
        *,
        placement_group_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete the given placement group.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param placement_group_id: UUID of the placement group you want to delete

        Usage:
        ::

            result = api.delete_placement_group(placement_group_id="example")
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
        return None

    def get_placement_group_servers(
        self,
        *,
        placement_group_id: str,
        zone: Optional[Zone] = None,
    ) -> GetPlacementGroupServersResponse:
        """
        Get all servers belonging to the given placement group.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param placement_group_id:
        :return: :class:`GetPlacementGroupServersResponse <GetPlacementGroupServersResponse>`

        Usage:
        ::

            result = api.get_placement_group_servers(placement_group_id="example")
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

    def set_placement_group_servers(
        self,
        *,
        placement_group_id: str,
        zone: Optional[Zone] = None,
        servers: Optional[List[str]] = None,
    ) -> SetPlacementGroupServersResponse:
        """
        Set all servers belonging to the given placement group.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param placement_group_id:
        :param servers:
        :return: :class:`SetPlacementGroupServersResponse <SetPlacementGroupServersResponse>`

        Usage:
        ::

            result = api.set_placement_group_servers(placement_group_id="example")
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
                    zone=zone,
                    servers=servers,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetPlacementGroupServersResponse(res.json())

    def update_placement_group_servers(
        self,
        *,
        placement_group_id: str,
        servers: List[str],
        zone: Optional[Zone] = None,
    ) -> UpdatePlacementGroupServersResponse:
        """
        Update all servers belonging to the given placement group.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param placement_group_id: UUID of the placement group
        :param servers:
        :return: :class:`UpdatePlacementGroupServersResponse <UpdatePlacementGroupServersResponse>`

        Usage:
        ::

            result = api.update_placement_group_servers(
                placement_group_id="example",
                servers=["example"],
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

    def list_ips(
        self,
        *,
        zone: Optional[Zone] = None,
        project: Optional[str] = None,
        organization: Optional[str] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListIpsResponse:
        """
        List all flexible IPs
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param project: The project ID the IPs are reserved in
        :param organization: The organization ID the IPs are reserved in
        :param tags: Filter IPs with these exact tags (to filter with several tags, use commas to separate them)
        :param name: Filter on the IP address (Works as a LIKE operation on the IP address)
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return
        :param page: A positive integer to choose the page to return
        :return: :class:`ListIpsResponse <ListIpsResponse>`

        Usage:
        ::

            result = api.list_ips()
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
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListIpsResponse(res.json())

    def list_ips_all(
        self,
        *,
        zone: Optional[Zone] = None,
        project: Optional[str] = None,
        organization: Optional[str] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[Ip]:
        """
        List all flexible IPs
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param project: The project ID the IPs are reserved in
        :param organization: The organization ID the IPs are reserved in
        :param tags: Filter IPs with these exact tags (to filter with several tags, use commas to separate them)
        :param name: Filter on the IP address (Works as a LIKE operation on the IP address)
        :param per_page: A positive integer lower or equal to 100 to select the number of items to return
        :param page: A positive integer to choose the page to return
        :return: :class:`List[ListIpsResponse] <List[ListIpsResponse]>`

        Usage:
        ::

            result = api.list_ips_all()
        """

        return fetch_all_pages(
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
            },
        )

    def create_ip(
        self,
        *,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[List[str]] = None,
        server: Optional[str] = None,
    ) -> CreateIpResponse:
        """
        Reserve a flexible IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param organization: The organization ID the IP is reserved in.

        One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
        :param project: The project ID the IP is reserved in.

        One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
        :param tags: The tags of the IP
        :param server: UUID of the server you want to attach the IP to
        :return: :class:`CreateIpResponse <CreateIpResponse>`

        Usage:
        ::

            result = api.create_ip()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/ips",
            body=marshal_CreateIpRequest(
                CreateIpRequest(
                    zone=zone,
                    organization=organization,
                    project=project,
                    tags=tags,
                    server=server,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateIpResponse(res.json())

    def get_ip(
        self,
        *,
        ip: str,
        zone: Optional[Zone] = None,
    ) -> GetIpResponse:
        """
        Get details of an IP with the given ID or address.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param ip: The IP ID or address to get
        :return: :class:`GetIpResponse <GetIpResponse>`

        Usage:
        ::

            result = api.get_ip(ip="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip = validate_path_param("ip", ip)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/ips/{param_ip}",
        )

        self._throw_on_error(res)
        return unmarshal_GetIpResponse(res.json())

    def update_ip(
        self,
        *,
        ip: str,
        zone: Optional[Zone] = None,
        reverse: Optional[str] = None,
        tags: Optional[List[str]] = None,
        server: Optional[str] = None,
    ) -> UpdateIpResponse:
        """
        Update a flexible IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param ip: IP ID or IP address
        :param reverse: Reverse domain name
        :param tags: An array of keywords you want to tag this IP with
        :param server:
        :return: :class:`UpdateIpResponse <UpdateIpResponse>`

        Usage:
        ::

            result = api.update_ip(ip="example")
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
                    tags=tags,
                    server=server,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_UpdateIpResponse(res.json())

    def delete_ip(
        self,
        *,
        ip: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete the IP with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param ip: The ID or the address of the IP to delete

        Usage:
        ::

            result = api.delete_ip(ip="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip = validate_path_param("ip", ip)

        res = self._request(
            "DELETE",
            f"/instance/v1/zones/{param_zone}/ips/{param_ip}",
        )

        self._throw_on_error(res)
        return None

    def list_private_ni_cs(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> ListPrivateNICsResponse:
        """
        List all private NICs of a given server.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: The server the private NIC is attached to
        :return: :class:`ListPrivateNICsResponse <ListPrivateNICsResponse>`

        Usage:
        ::

            result = api.list_private_ni_cs(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/private_nics",
        )

        self._throw_on_error(res)
        return unmarshal_ListPrivateNICsResponse(res.json())

    def create_private_nic(
        self,
        *,
        server_id: str,
        private_network_id: str,
        zone: Optional[Zone] = None,
    ) -> CreatePrivateNICResponse:
        """
        Create a private NIC connecting a server to a private network.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: UUID of the server the private NIC will be attached to
        :param private_network_id: UUID of the private network where the private NIC will be attached
        :return: :class:`CreatePrivateNICResponse <CreatePrivateNICResponse>`

        Usage:
        ::

            result = api.create_private_nic(
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
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreatePrivateNICResponse(res.json())

    def get_private_nic(
        self,
        *,
        server_id: str,
        private_nic_id: str,
        zone: Optional[Zone] = None,
    ) -> GetPrivateNICResponse:
        """
        Get private NIC properties.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: The server the private NIC is attached to
        :param private_nic_id: The private NIC unique ID
        :return: :class:`GetPrivateNICResponse <GetPrivateNICResponse>`

        Usage:
        ::

            result = api.get_private_nic(
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

    def delete_private_nic(
        self,
        *,
        server_id: str,
        private_nic_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a private NIC.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: The server the private NIC is attached to
        :param private_nic_id: The private NIC unique ID

        Usage:
        ::

            result = api.delete_private_nic(
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
        return None

    def list_bootscripts(
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
        List bootscripts
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param arch:
        :param title:
        :param default:
        :param public:
        :param per_page:
        :param page:
        :return: :class:`ListBootscriptsResponse <ListBootscriptsResponse>`

        Usage:
        ::

            result = api.list_bootscripts()
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

    def list_bootscripts_all(
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
        List bootscripts
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param arch:
        :param title:
        :param default:
        :param public:
        :param per_page:
        :param page:
        :return: :class:`List[ListBootscriptsResponse] <List[ListBootscriptsResponse]>`

        Usage:
        ::

            result = api.list_bootscripts_all()
        """

        return fetch_all_pages(
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

    def get_bootscript(
        self,
        *,
        bootscript_id: str,
        zone: Optional[Zone] = None,
    ) -> GetBootscriptResponse:
        """
        Get details of a bootscript with the given ID.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param bootscript_id:
        :return: :class:`GetBootscriptResponse <GetBootscriptResponse>`

        Usage:
        ::

            result = api.get_bootscript(bootscript_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_bootscript_id = validate_path_param("bootscript_id", bootscript_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/bootscripts/{param_bootscript_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetBootscriptResponse(res.json())

    def get_dashboard(
        self,
        *,
        zone: Optional[Zone] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
    ) -> GetDashboardResponse:
        """

        Usage:
        ::

            result = api.get_dashboard()
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
