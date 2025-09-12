# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone as ScwZone,
)
from scaleway_core.utils import (
    validate_path_param,
    fetch_all_pages,
)
from .types import (
    InstancePolicyAction,
    InstancePolicyType,
    ListInstanceGroupEventsRequestOrderBy,
    ListInstanceGroupsRequestOrderBy,
    ListInstancePoliciesRequestOrderBy,
    ListInstanceTemplatesRequestOrderBy,
    Capacity,
    CreateInstanceGroupRequest,
    CreateInstancePolicyRequest,
    CreateInstanceTemplateRequest,
    InstanceGroup,
    InstanceGroupEvent,
    InstancePolicy,
    InstanceTemplate,
    ListInstanceGroupEventsResponse,
    ListInstanceGroupsResponse,
    ListInstancePoliciesResponse,
    ListInstanceTemplatesResponse,
    Loadbalancer,
    Metric,
    UpdateInstanceGroupRequest,
    UpdateInstanceGroupRequestCapacity,
    UpdateInstanceGroupRequestLoadbalancer,
    UpdateInstancePolicyRequest,
    UpdateInstancePolicyRequestMetric,
    UpdateInstanceTemplateRequest,
    VolumeInstanceTemplate,
)
from .marshalling import (
    unmarshal_InstanceGroup,
    unmarshal_InstancePolicy,
    unmarshal_InstanceTemplate,
    unmarshal_ListInstanceGroupEventsResponse,
    unmarshal_ListInstanceGroupsResponse,
    unmarshal_ListInstancePoliciesResponse,
    unmarshal_ListInstanceTemplatesResponse,
    marshal_CreateInstanceGroupRequest,
    marshal_CreateInstancePolicyRequest,
    marshal_CreateInstanceTemplateRequest,
    marshal_UpdateInstanceGroupRequest,
    marshal_UpdateInstancePolicyRequest,
    marshal_UpdateInstanceTemplateRequest,
)


class AutoscalingV1Alpha1API(API):
    """ """

    def get_instance_group(
        self,
        *,
        instance_group_id: str,
        zone: Optional[ScwZone] = None,
    ) -> InstanceGroup:
        """
        Get Instance group.
        Retrieve information about an existing Instance group, specified by its `instance_group_id`. Its full details, including errors, are returned in the response object.
        :param instance_group_id: ID of the requested Instance group.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`InstanceGroup <InstanceGroup>`

        Usage:
        ::

            result = api.get_instance_group(
                instance_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_instance_group_id = validate_path_param(
            "instance_group_id", instance_group_id
        )

        res = self._request(
            "GET",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-groups/{param_instance_group_id}",
        )

        self._throw_on_error(res)
        return unmarshal_InstanceGroup(res.json())

    def create_instance_group(
        self,
        *,
        name: str,
        template_id: str,
        capacity: Capacity,
        loadbalancer: Loadbalancer,
        zone: Optional[ScwZone] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> InstanceGroup:
        """
        Create Instance group.
        Create a new Instance group. You must specify a `template_id`, capacity and Load Balancer object.
        :param name: Name of Instance group.
        :param template_id: Template ID (ID of the Instance template to attach to the Instance group).
        :param capacity: Specification of the minimum and maximum replicas for the Instance group, and the cooldown interval between two scaling events.
        :param loadbalancer: Specification of the Load Balancer to link to the Instance group.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID to filter for, only Instance groups from this Project will be returned.
        :param tags: List of tags for the Instance group.
        :return: :class:`InstanceGroup <InstanceGroup>`

        Usage:
        ::

            result = api.create_instance_group(
                name="example",
                template_id="example",
                capacity=Capacity(),
                loadbalancer=Loadbalancer(),
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-groups",
            body=marshal_CreateInstanceGroupRequest(
                CreateInstanceGroupRequest(
                    name=name,
                    template_id=template_id,
                    capacity=capacity,
                    loadbalancer=loadbalancer,
                    zone=zone,
                    project_id=project_id,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_InstanceGroup(res.json())

    def list_instance_groups(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListInstanceGroupsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListInstanceGroupsResponse:
        """
        List Instance groups.
        List all Instance groups, for a Scaleway Organization or Scaleway Project. By default, the Instance groups returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of Instance groups in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of Instance groups to return per page.
        :return: :class:`ListInstanceGroupsResponse <ListInstanceGroupsResponse>`

        Usage:
        ::

            result = api.list_instance_groups()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-groups",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListInstanceGroupsResponse(res.json())

    def list_instance_groups_all(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListInstanceGroupsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[InstanceGroup]:
        """
        List Instance groups.
        List all Instance groups, for a Scaleway Organization or Scaleway Project. By default, the Instance groups returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of Instance groups in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of Instance groups to return per page.
        :return: :class:`list[InstanceGroup] <list[InstanceGroup]>`

        Usage:
        ::

            result = api.list_instance_groups_all()
        """

        return fetch_all_pages(
            type=ListInstanceGroupsResponse,
            key="instance_groups",
            fetcher=self.list_instance_groups,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    def update_instance_group(
        self,
        *,
        instance_group_id: str,
        zone: Optional[ScwZone] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        capacity: Optional[UpdateInstanceGroupRequestCapacity] = None,
        loadbalancer: Optional[UpdateInstanceGroupRequestLoadbalancer] = None,
    ) -> InstanceGroup:
        """
        Update Instance group.
        Update the parameters of an existing Instance group, specified by its `instance_group_id`.
        :param instance_group_id: Instance group ID to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of Instance group.
        :param tags: List of tags for the Load Balancer.
        :param capacity: Specification of the minimum and maximum replicas for the Instance group, and the cooldown interval between two scaling events.
        :param loadbalancer: Specification of the Load Balancer to link to the Instance group.
        :return: :class:`InstanceGroup <InstanceGroup>`

        Usage:
        ::

            result = api.update_instance_group(
                instance_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_instance_group_id = validate_path_param(
            "instance_group_id", instance_group_id
        )

        res = self._request(
            "PATCH",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-groups/{param_instance_group_id}",
            body=marshal_UpdateInstanceGroupRequest(
                UpdateInstanceGroupRequest(
                    instance_group_id=instance_group_id,
                    zone=zone,
                    name=name,
                    tags=tags,
                    capacity=capacity,
                    loadbalancer=loadbalancer,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_InstanceGroup(res.json())

    def delete_instance_group(
        self,
        *,
        instance_group_id: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete  Instance group.
        Delete an existing Instance group, specified by its `instance_group_id`. Deleting an Instance group is permanent, and cannot be undone.
        :param instance_group_id: ID of the Instance group to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_instance_group(
                instance_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_instance_group_id = validate_path_param(
            "instance_group_id", instance_group_id
        )

        res = self._request(
            "DELETE",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-groups/{param_instance_group_id}",
        )

        self._throw_on_error(res)

    def create_instance_template(
        self,
        *,
        zone: Optional[ScwZone] = None,
        commercial_type: str,
        volumes: dict[str, VolumeInstanceTemplate],
        image_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        security_group_id: Optional[str] = None,
        name: str,
        placement_group_id: Optional[str] = None,
        public_ips_v4_count: Optional[int] = None,
        public_ips_v6_count: Optional[int] = None,
        project_id: Optional[str] = None,
        private_network_ids: Optional[list[str]] = None,
        cloud_init: Optional[str] = None,
    ) -> InstanceTemplate:
        """
        Create Instance template.
        Create a new Instance template. This specifies the details of the Instance (commercial type, zone, image, volumes etc.) that will be in the Instance group.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param commercial_type: Name of Instance commercial type.
        :param volumes: Template of Instance volume.
        :param image_id: Instance image ID. Can be an ID of a marketplace or personal image. This image must be compatible with `volume` and `commercial_type` template.
        :param tags: List of tags for the Instance template.
        :param security_group_id: Instance security group ID (optional).
        :param name: Name of Instance template.
        :param placement_group_id: Instance placement group ID. This is optional, but it is highly recommended to set a preference for Instance location within Availability Zone.
        :param public_ips_v4_count: Number of flexible IPv4 addresses to attach to the new Instance.
        :param public_ips_v6_count: Number of flexible IPv6 addresses to attach to the new Instance.
        :param project_id: ID of the Project containing the Instance template resource.
        :param private_network_ids: Private Network IDs to attach to the new Instance.
        :param cloud_init: Cloud-config file must be passed in Base64 format. Cloud-config files are special scripts designed to be run by the cloud-init process. These are generally used for initial configuration on the very first boot of a server.
        :return: :class:`InstanceTemplate <InstanceTemplate>`

        Usage:
        ::

            result = api.create_instance_template(
                commercial_type="example",
                volumes={},
                name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-templates",
            body=marshal_CreateInstanceTemplateRequest(
                CreateInstanceTemplateRequest(
                    zone=zone,
                    commercial_type=commercial_type,
                    volumes=volumes,
                    image_id=image_id,
                    tags=tags,
                    security_group_id=security_group_id,
                    name=name,
                    placement_group_id=placement_group_id,
                    public_ips_v4_count=public_ips_v4_count,
                    public_ips_v6_count=public_ips_v6_count,
                    project_id=project_id,
                    private_network_ids=private_network_ids,
                    cloud_init=cloud_init,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_InstanceTemplate(res.json())

    def update_instance_template(
        self,
        *,
        template_id: str,
        zone: Optional[ScwZone] = None,
        commercial_type: Optional[str] = None,
        image_id: Optional[str] = None,
        volumes: Optional[dict[str, VolumeInstanceTemplate]] = None,
        tags: Optional[list[str]] = None,
        security_group_id: Optional[str] = None,
        placement_group_id: Optional[str] = None,
        public_ips_v4_count: Optional[int] = None,
        public_ips_v6_count: Optional[int] = None,
        name: Optional[str] = None,
        private_network_ids: Optional[list[str]] = None,
        cloud_init: Optional[str] = None,
    ) -> InstanceTemplate:
        """
        Update Instance template.
        Update an Instance template, such as its commercial offer type, image or volume template.
        :param template_id: Template ID of the resource.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param commercial_type: Name of Instance commercial type.
        :param image_id: Instance image ID. Can be an ID of a marketplace or personal image. This image must be compatible with `volume` and `commercial_type` template.
        :param volumes: Template of Instance volume.
        :param tags: List of tags for the Instance template.
        :param security_group_id: Instance security group ID (optional).
        :param placement_group_id: Instance placement group ID. This is optional, but it is highly recommended to set a preference for Instance location within Availability Zone.
        :param public_ips_v4_count: Number of flexible IPv4 addresses to attach to the new Instance.
        :param public_ips_v6_count: Number of flexible IPv6 addresses to attach to the new Instance.
        :param name: Name of Instance template.
        :param private_network_ids: Private Network IDs to attach to the new Instance.
        :param cloud_init: Cloud-config file must be passed in Base64 format. Cloud-config files are special scripts designed to be run by the cloud-init process. These are generally used for initial configuration on the very first boot of a server.
        :return: :class:`InstanceTemplate <InstanceTemplate>`

        Usage:
        ::

            result = api.update_instance_template(
                template_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_template_id = validate_path_param("template_id", template_id)

        res = self._request(
            "PATCH",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-templates/{param_template_id}",
            body=marshal_UpdateInstanceTemplateRequest(
                UpdateInstanceTemplateRequest(
                    template_id=template_id,
                    zone=zone,
                    commercial_type=commercial_type,
                    image_id=image_id,
                    volumes=volumes,
                    tags=tags,
                    security_group_id=security_group_id,
                    placement_group_id=placement_group_id,
                    public_ips_v4_count=public_ips_v4_count,
                    public_ips_v6_count=public_ips_v6_count,
                    name=name,
                    private_network_ids=private_network_ids,
                    cloud_init=cloud_init,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_InstanceTemplate(res.json())

    def get_instance_template(
        self,
        *,
        template_id: str,
        zone: Optional[ScwZone] = None,
    ) -> InstanceTemplate:
        """
        Get Instance template.
        Get an existing Instance template from its `template_id`.
        :param template_id: Template ID of the resource.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`InstanceTemplate <InstanceTemplate>`

        Usage:
        ::

            result = api.get_instance_template(
                template_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_template_id = validate_path_param("template_id", template_id)

        res = self._request(
            "GET",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-templates/{param_template_id}",
        )

        self._throw_on_error(res)
        return unmarshal_InstanceTemplate(res.json())

    def delete_instance_template(
        self,
        *,
        template_id: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete Instance template.
        Delete an existing Instance template. This action is permanent and cannot be undone.
        :param template_id: ID of the template to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_instance_template(
                template_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_template_id = validate_path_param("template_id", template_id)

        res = self._request(
            "DELETE",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-templates/{param_template_id}",
        )

        self._throw_on_error(res)

    def list_instance_templates(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListInstanceTemplatesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListInstanceTemplatesResponse:
        """
        List Instance templates.
        List all Instance templates, for a Scaleway Organization or Scaleway Project. By default, the Instance templates returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of Instance groups in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of Instance groups to return per page.
        :return: :class:`ListInstanceTemplatesResponse <ListInstanceTemplatesResponse>`

        Usage:
        ::

            result = api.list_instance_templates()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-templates",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListInstanceTemplatesResponse(res.json())

    def list_instance_templates_all(
        self,
        *,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListInstanceTemplatesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[InstanceTemplate]:
        """
        List Instance templates.
        List all Instance templates, for a Scaleway Organization or Scaleway Project. By default, the Instance templates returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of Instance groups in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of Instance groups to return per page.
        :return: :class:`list[InstanceTemplate] <list[InstanceTemplate]>`

        Usage:
        ::

            result = api.list_instance_templates_all()
        """

        return fetch_all_pages(
            type=ListInstanceTemplatesResponse,
            key="instance_templates",
            fetcher=self.list_instance_templates,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    def create_instance_policy(
        self,
        *,
        name: str,
        action: InstancePolicyAction,
        type_: InstancePolicyType,
        value: int,
        priority: int,
        instance_group_id: str,
        zone: Optional[ScwZone] = None,
        metric: Optional[Metric] = None,
    ) -> InstancePolicy:
        """
        Create scaling policy.
        Create a new scaling policy. You must specify a `policy_id`, capacity and Load Balancer object.
        :param name: Name of the policy.
        :param action: Action to execute when the metric-based condition is met.
        :param type_: How to use the number defined in `value` when determining by how many Instances to scale up/down.
        :param value: Value representing the magnitude of the scaling action to take for the Instance group. Depending on the `type` parameter, this number could represent a total number of Instances in the group, a number of Instances to add, or a percentage to scale the group by.
        :param priority: Priority of this policy compared to all other scaling policies. This determines the processing order. The lower the number, the higher the priority.
        :param instance_group_id: Instance group ID related to this policy.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param metric: Cockpit metric to use when determining whether to trigger a scale up/down action.
        One-Of ('trigger'): at most one of 'metric' could be set.
        :return: :class:`InstancePolicy <InstancePolicy>`

        Usage:
        ::

            result = api.create_instance_policy(
                name="example",
                action=InstancePolicyAction.unknown_action,
                type=InstancePolicyType.unknown_type,
                value=1,
                priority=1,
                instance_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-policies",
            body=marshal_CreateInstancePolicyRequest(
                CreateInstancePolicyRequest(
                    name=name,
                    action=action,
                    type_=type_,
                    value=value,
                    priority=priority,
                    instance_group_id=instance_group_id,
                    zone=zone,
                    metric=metric,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_InstancePolicy(res.json())

    def update_instance_policy(
        self,
        *,
        policy_id: str,
        zone: Optional[ScwZone] = None,
        name: Optional[str] = None,
        metric: Optional[UpdateInstancePolicyRequestMetric] = None,
        action: Optional[InstancePolicyAction] = None,
        type_: Optional[InstancePolicyType] = None,
        value: Optional[int] = None,
        priority: Optional[int] = None,
    ) -> InstancePolicy:
        """
        Update scaling policy.
        Update the parameters of an existing scaling policy, specified by its `policy_id`.
        :param policy_id: Policy ID to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Policy name to update.
        :param metric: Metric specification to update (Cockpit metric to use when determining whether to trigger a scale up/down action).
        One-Of ('trigger'): at most one of 'metric' could be set.
        :param action: Action to update (action to execute when the metric-based condition is met).
        :param type_: Type to update (how to use the number defined in `value` when determining by how many Instances to scale up/down).
        :param value: Value to update (number representing the magnitude of the scaling action to take for the Instance group).
        :param priority: Priority to update (priority of this policy compared to all other scaling policies. The lower the number, the higher the priority).
        :return: :class:`InstancePolicy <InstancePolicy>`

        Usage:
        ::

            result = api.update_instance_policy(
                policy_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_policy_id = validate_path_param("policy_id", policy_id)

        res = self._request(
            "PATCH",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-policies/{param_policy_id}",
            body=marshal_UpdateInstancePolicyRequest(
                UpdateInstancePolicyRequest(
                    policy_id=policy_id,
                    zone=zone,
                    name=name,
                    action=action,
                    type_=type_,
                    value=value,
                    priority=priority,
                    metric=metric,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_InstancePolicy(res.json())

    def list_instance_policies(
        self,
        *,
        instance_group_id: str,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListInstancePoliciesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListInstancePoliciesResponse:
        """
        List scaling policies.
        List all scaling policies, for a Scaleway Organization or Scaleway Project. By default, the policies returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param instance_group_id: Instance group ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of Instance groups in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of scaling policies to return per page.
        :return: :class:`ListInstancePoliciesResponse <ListInstancePoliciesResponse>`

        Usage:
        ::

            result = api.list_instance_policies(
                instance_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-policies",
            params={
                "instance_group_id": instance_group_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListInstancePoliciesResponse(res.json())

    def list_instance_policies_all(
        self,
        *,
        instance_group_id: str,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListInstancePoliciesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[InstancePolicy]:
        """
        List scaling policies.
        List all scaling policies, for a Scaleway Organization or Scaleway Project. By default, the policies returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param instance_group_id: Instance group ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of Instance groups in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of scaling policies to return per page.
        :return: :class:`list[InstancePolicy] <list[InstancePolicy]>`

        Usage:
        ::

            result = api.list_instance_policies_all(
                instance_group_id="example",
            )
        """

        return fetch_all_pages(
            type=ListInstancePoliciesResponse,
            key="policies",
            fetcher=self.list_instance_policies,
            args={
                "instance_group_id": instance_group_id,
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    def get_instance_policy(
        self,
        *,
        policy_id: str,
        zone: Optional[ScwZone] = None,
    ) -> InstancePolicy:
        """
        Get scaling policy.
        Retrieve information about an existing scaling policy, specified by its `policy_id`. Its full details are returned in the response object.
        :param policy_id: Policy ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`InstancePolicy <InstancePolicy>`

        Usage:
        ::

            result = api.get_instance_policy(
                policy_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_policy_id = validate_path_param("policy_id", policy_id)

        res = self._request(
            "GET",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-policies/{param_policy_id}",
        )

        self._throw_on_error(res)
        return unmarshal_InstancePolicy(res.json())

    def delete_instance_policy(
        self,
        *,
        policy_id: str,
        zone: Optional[ScwZone] = None,
    ) -> None:
        """
        Delete scaling policy.
        Delete an existing scaling policy, specified by its `policy_id`. Deleting a scaling policy is permanent, and cannot be undone.
        :param policy_id: ID of the policy to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_instance_policy(
                policy_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_policy_id = validate_path_param("policy_id", policy_id)

        res = self._request(
            "DELETE",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-policies/{param_policy_id}",
        )

        self._throw_on_error(res)

    def list_instance_group_events(
        self,
        *,
        instance_group_id: str,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListInstanceGroupEventsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListInstanceGroupEventsResponse:
        """
        List events.
        List all events for a given Instance group. By default, the events are ordered by creation date in descending order, though this can be modified via the `order_by` field.
        :param instance_group_id: List all event logs for the Instance group ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of Instance groups in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of Instance groups to return per page.
        :return: :class:`ListInstanceGroupEventsResponse <ListInstanceGroupEventsResponse>`

        Usage:
        ::

            result = api.list_instance_group_events(
                instance_group_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_instance_group_id = validate_path_param(
            "instance_group_id", instance_group_id
        )

        res = self._request(
            "GET",
            f"/autoscaling/v1alpha1/zones/{param_zone}/instance-groups/{param_instance_group_id}/events",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListInstanceGroupEventsResponse(res.json())

    def list_instance_group_events_all(
        self,
        *,
        instance_group_id: str,
        zone: Optional[ScwZone] = None,
        order_by: Optional[ListInstanceGroupEventsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[InstanceGroupEvent]:
        """
        List events.
        List all events for a given Instance group. By default, the events are ordered by creation date in descending order, though this can be modified via the `order_by` field.
        :param instance_group_id: List all event logs for the Instance group ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of Instance groups in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of Instance groups to return per page.
        :return: :class:`list[InstanceGroupEvent] <list[InstanceGroupEvent]>`

        Usage:
        ::

            result = api.list_instance_group_events_all(
                instance_group_id="example",
            )
        """

        return fetch_all_pages(
            type=ListInstanceGroupEventsResponse,
            key="instance_events",
            fetcher=self.list_instance_group_events,
            args={
                "instance_group_id": instance_group_id,
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )
