# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    Link,
    Partner,
    Pop,
    RoutingPolicy,
    ListLinksResponse,
    ListPartnersResponse,
    ListPopsResponse,
    ListRoutingPoliciesResponse,
    AttachRoutingPolicyRequest,
    AttachVpcRequest,
    CreateLinkRequest,
    CreateRoutingPolicyRequest,
    UpdateLinkRequest,
    UpdateRoutingPolicyRequest,
)


def unmarshal_Link(data: Any) -> Link:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Link' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("pop_id", None)
    if field is not None:
        args["pop_id"] = field

    field = data.get("bandwidth_mbps", None)
    if field is not None:
        args["bandwidth_mbps"] = field

    field = data.get("partner_id", None)
    if field is not None:
        args["partner_id"] = field
    else:
        args["partner_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("bgp_v4_status", None)
    if field is not None:
        args["bgp_v4_status"] = field

    field = data.get("bgp_v6_status", None)
    if field is not None:
        args["bgp_v6_status"] = field

    field = data.get("enable_route_propagation", None)
    if field is not None:
        args["enable_route_propagation"] = field

    field = data.get("pairing_key", None)
    if field is not None:
        args["pairing_key"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("vpc_id", None)
    if field is not None:
        args["vpc_id"] = field
    else:
        args["vpc_id"] = None

    field = data.get("routing_policy_id", None)
    if field is not None:
        args["routing_policy_id"] = field
    else:
        args["routing_policy_id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return Link(**args)


def unmarshal_Partner(data: Any) -> Partner:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Partner' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("contact_email", None)
    if field is not None:
        args["contact_email"] = field

    field = data.get("logo_url", None)
    if field is not None:
        args["logo_url"] = field

    field = data.get("portal_url", None)
    if field is not None:
        args["portal_url"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return Partner(**args)


def unmarshal_Pop(data: Any) -> Pop:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Pop' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("hosting_provider_name", None)
    if field is not None:
        args["hosting_provider_name"] = field

    field = data.get("address", None)
    if field is not None:
        args["address"] = field

    field = data.get("city", None)
    if field is not None:
        args["city"] = field

    field = data.get("logo_url", None)
    if field is not None:
        args["logo_url"] = field

    field = data.get("available_link_bandwidths_mbps", None)
    if field is not None:
        args["available_link_bandwidths_mbps"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    return Pop(**args)


def unmarshal_RoutingPolicy(data: Any) -> RoutingPolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RoutingPolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("prefix_filter_in", None)
    if field is not None:
        args["prefix_filter_in"] = field

    field = data.get("prefix_filter_out", None)
    if field is not None:
        args["prefix_filter_out"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return RoutingPolicy(**args)


def unmarshal_ListLinksResponse(data: Any) -> ListLinksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLinksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("links", None)
    if field is not None:
        args["links"] = (
            [unmarshal_Link(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListLinksResponse(**args)


def unmarshal_ListPartnersResponse(data: Any) -> ListPartnersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPartnersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("partners", None)
    if field is not None:
        args["partners"] = (
            [unmarshal_Partner(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListPartnersResponse(**args)


def unmarshal_ListPopsResponse(data: Any) -> ListPopsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPopsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pops", None)
    if field is not None:
        args["pops"] = [unmarshal_Pop(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListPopsResponse(**args)


def unmarshal_ListRoutingPoliciesResponse(data: Any) -> ListRoutingPoliciesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRoutingPoliciesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("routing_policies", None)
    if field is not None:
        args["routing_policies"] = (
            [unmarshal_RoutingPolicy(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListRoutingPoliciesResponse(**args)


def marshal_AttachRoutingPolicyRequest(
    request: AttachRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.routing_policy_id is not None:
        output["routing_policy_id"] = request.routing_policy_id

    return output


def marshal_AttachVpcRequest(
    request: AttachVpcRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.vpc_id is not None:
        output["vpc_id"] = request.vpc_id

    return output


def marshal_CreateLinkRequest(
    request: CreateLinkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("dedicated", request.dedicated),
                OneOfPossibility("port_id", request.port_id),
                OneOfPossibility("partner_id", request.partner_id),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.pop_id is not None:
        output["pop_id"] = request.pop_id

    if request.bandwidth_mbps is not None:
        output["bandwidth_mbps"] = request.bandwidth_mbps

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateRoutingPolicyRequest(
    request: CreateRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.prefix_filter_in is not None:
        output["prefix_filter_in"] = request.prefix_filter_in

    if request.prefix_filter_out is not None:
        output["prefix_filter_out"] = request.prefix_filter_out

    return output


def marshal_UpdateLinkRequest(
    request: UpdateLinkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateRoutingPolicyRequest(
    request: UpdateRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.prefix_filter_in is not None:
        output["prefix_filter_in"] = request.prefix_filter_in

    if request.prefix_filter_out is not None:
        output["prefix_filter_out"] = request.prefix_filter_out

    return output
