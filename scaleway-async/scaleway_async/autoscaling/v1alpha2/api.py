# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Awaitable, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone as ScwZone,
)
from scaleway_core.utils import (
    OneOfPossibility,
    WaitForOptions,
    resolve_one_of,
    validate_path_param,
    wait_for_resource_async,
)
from .types import (
    ListGroupsRequestOrderBy,
    CreateGroupRequest,
    Group,
    ListAlertsResponse,
    ListGroupsResponse,
    ListLogsResponse,
    ListServersResponse,
    LoadBalancerConfigurationSpec,
    ScalingPolicySpec,
    UpdateGroupRequest,
)
from .content import (
    GROUP_GROUP_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Group,
    unmarshal_ListAlertsResponse,
    unmarshal_ListGroupsResponse,
    unmarshal_ListLogsResponse,
    unmarshal_ListServersResponse,
    marshal_CreateGroupRequest,
    marshal_UpdateGroupRequest,
)


class AutoscalingV1Alpha2API(API):
    """ """

    async def list_groups(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListGroupsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        project_id: Optional[str] = None,
        template_id: Optional[str] = None,
        load_balancer_id: Optional[str] = None,
    ) -> ListGroupsResponse:
        """
        List autoscaling groups.
        List all autoscaling groups in a project.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Order criteria for listing groups.
        :param page_size: Page size for pagination.
        :param page_token: Token for pagination.
        :param project_id: Project ID to filter groups.
        :param template_id: Template ID to filter groups.
        :param load_balancer_id: Load balancer ID to filter groups.
        :return: :class:`ListGroupsResponse <ListGroupsResponse>`

        Usage:
        ::

            result = await api.list_groups()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/autoscaling/v1alpha2/zones/{param_zone}/groups",
            params={
                "load_balancer_id": load_balancer_id,
                "order_by": order_by,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                "project_id": project_id or self.client.default_project_id,
                "template_id": template_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListGroupsResponse(res.json())

    async def get_group(
        self,
        *,
        group_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Group:
        """
        Get an autoscaling group.
        Get details of a specified autoscaling group including its
        configuration, current size, and status.
        :param group_id: ID of the group to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = await api.get_group(
                group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "GET",
            f"/autoscaling/v1alpha2/zones/{param_zone}/groups/{param_group_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Group(res.json())

    async def wait_for_group(
        self,
        *,
        group_id: str,
        zone: Optional[ScwZone] = None,
        options: Optional[WaitForOptions[Group, Union[bool, Awaitable[bool]]]] = None,
    ) -> Group:
        """
        Get an autoscaling group.
        Get details of a specified autoscaling group including its
        configuration, current size, and status.
        :param group_id: ID of the group to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = await api.get_group(
                group_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in GROUP_GROUP_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_group,
            options=options,
            args={
                "group_id": group_id,
                "zone": zone,
            },
        )

    async def create_group(
        self,
        *,
        name: str,
        template_id: str,
        zone: Optional[ScwZone] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        scaling_policy_spec: Optional[ScalingPolicySpec] = None,
        load_balancer_configuration_spec: Optional[
            LoadBalancerConfigurationSpec
        ] = None,
    ) -> Group:
        """
        Create an autoscaling group.
        Create a new autoscaling group with the specified configuration
        including template, scaling policy, and optional load balancer
        settings.
        :param name: Name of the autoscaling group.
        :param template_id: Template ID for instances in this group.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID to create the group in.
        :param tags: Tags associated with the group.
        :param scaling_policy_spec: Scaling policy configuration.
        :param load_balancer_configuration_spec: Optional load balancer configuration.
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = await api.create_group(
                name="example",
                template_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/autoscaling/v1alpha2/zones/{param_zone}/groups",
            body=marshal_CreateGroupRequest(
                CreateGroupRequest(
                    name=name,
                    template_id=template_id,
                    zone=zone,
                    project_id=project_id,
                    tags=tags,
                    scaling_policy_spec=scaling_policy_spec,
                    load_balancer_configuration_spec=load_balancer_configuration_spec,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Group(res.json())

    async def update_group(
        self,
        *,
        group_id: str,
        zone: Optional[ScwZone] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        template_id: Optional[str] = None,
        scaling_policy_spec: Optional[ScalingPolicySpec] = None,
        load_balancer_configuration_spec: Optional[
            LoadBalancerConfigurationSpec
        ] = None,
    ) -> Group:
        """
        Update an autoscaling group.
        Update the configuration of a specified autoscaling group including
        name, tags, template, scaling policy, and load balancer settings.
        :param group_id: ID of the group to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: New name for the group.
        :param tags: New tags for the group.
        :param template_id: New template ID for instances.
        :param scaling_policy_spec: New scaling policy configuration.
        :param load_balancer_configuration_spec: New load balancer configuration.
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = await api.update_group(
                group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "PATCH",
            f"/autoscaling/v1alpha2/zones/{param_zone}/groups/{param_group_id}",
            body=marshal_UpdateGroupRequest(
                UpdateGroupRequest(
                    group_id=group_id,
                    zone=zone,
                    name=name,
                    tags=tags,
                    template_id=template_id,
                    scaling_policy_spec=scaling_policy_spec,
                    load_balancer_configuration_spec=load_balancer_configuration_spec,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Group(res.json())

    async def delete_group(
        self,
        *,
        group_id: str,
        zone: Optional[ScwZone] = None,
    ) -> Group:
        """
        Delete an autoscaling group.
        Delete a specified autoscaling group and all its associated
        resources.
        :param group_id: ID of the group to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = await api.delete_group(
                group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "DELETE",
            f"/autoscaling/v1alpha2/zones/{param_zone}/groups/{param_group_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Group(res.json())

    async def list_logs(
        self,
        *,
        group_id: str,
        zone: Optional[ScwZone] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
    ) -> ListLogsResponse:
        """
        List autoscaling group logs.
        List logs for a specified autoscaling group to view scaling events
        and activities.
        :param group_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page_token:
        :param page_size:
        :param start_time:
        :param end_time:
        :return: :class:`ListLogsResponse <ListLogsResponse>`

        Usage:
        ::

            result = await api.list_logs(
                group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/autoscaling/v1alpha2/zones/{param_zone}/logs",
            params={
                "end_time": end_time,
                "group_id": group_id,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                "start_time": start_time,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLogsResponse(res.json())

    async def list_servers(
        self,
        *,
        group_id: str,
        zone: Optional[ScwZone] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> ListServersResponse:
        """
        List autoscaling group servers.
        List all Instances belonging to a specified autoscaling group.
        :param group_id:
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page_token:
        :param page_size:
        :return: :class:`ListServersResponse <ListServersResponse>`

        Usage:
        ::

            result = await api.list_servers(
                group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/autoscaling/v1alpha2/zones/{param_zone}/servers",
            params={
                "group_id": group_id,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServersResponse(res.json())

    async def list_alerts(
        self,
        *,
        zone: Optional[ScwZone] = None,
        group_id: Optional[str] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
    ) -> ListAlertsResponse:
        """
        List autoscaling group alerts.
        List active and historical alerts for a specified autoscaling group.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param group_id:
        One-Of ('scope'): at most one of 'group_id', 'project_id' could be set.
        :param page_token:
        :param page_size:
        :param project_id:
        One-Of ('scope'): at most one of 'group_id', 'project_id' could be set.
        :return: :class:`ListAlertsResponse <ListAlertsResponse>`

        Usage:
        ::

            result = await api.list_alerts()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/autoscaling/v1alpha2/zones/{param_zone}/alerts",
            params={
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                **resolve_one_of(
                    [
                        OneOfPossibility("group_id", group_id),
                        OneOfPossibility("project_id", project_id),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListAlertsResponse(res.json())
