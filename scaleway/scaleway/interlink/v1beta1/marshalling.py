# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    BgpStatus,
    DedicatedConnectionStatus,
    LinkStatus,
    DedicatedConnection,
    BgpConfig,
    PartnerHost,
    SelfHost,
    Link,
    Partner,
    Pop,
    RoutingPolicy,
    ListDedicatedConnectionsResponse,
    ListLinksResponse,
    ListPartnersResponse,
    ListPopsResponse,
    ListRoutingPoliciesResponse,
    AttachRoutingPolicyRequest,
    AttachVpcRequest,
    CreateLinkRequest,
    CreateRoutingPolicyRequest,
    DetachRoutingPolicyRequest,
    SetRoutingPolicyRequest,
    UpdateLinkRequest,
    UpdateRoutingPolicyRequest,
)


def unmarshal_DedicatedConnection(data: Any) -> DedicatedConnection:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DedicatedConnection' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DedicatedConnectionStatus.UNKNOWN_STATUS

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("pop_id", None)
    if field is not None:
        args["pop_id"] = field
    else:
        args["pop_id"] = None

    field = data.get("bandwidth_mbps", None)
    if field is not None:
        args["bandwidth_mbps"] = field
    else:
        args["bandwidth_mbps"] = 0

    field = data.get("available_link_bandwidths", None)
    if field is not None:
        args["available_link_bandwidths"] = field
    else:
        args["available_link_bandwidths"] = []

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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

    field = data.get("demarcation_info", None)
    if field is not None:
        args["demarcation_info"] = field
    else:
        args["demarcation_info"] = None

    return DedicatedConnection(**args)


def unmarshal_BgpConfig(data: Any) -> BgpConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BgpConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("asn", None)
    if field is not None:
        args["asn"] = field
    else:
        args["asn"] = 0

    field = data.get("ipv4", None)
    if field is not None:
        args["ipv4"] = field
    else:
        args["ipv4"] = None

    field = data.get("ipv6", None)
    if field is not None:
        args["ipv6"] = field
    else:
        args["ipv6"] = None

    return BgpConfig(**args)


def unmarshal_PartnerHost(data: Any) -> PartnerHost:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PartnerHost' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("partner_id", None)
    if field is not None:
        args["partner_id"] = field
    else:
        args["partner_id"] = None

    field = data.get("pairing_key", None)
    if field is not None:
        args["pairing_key"] = field
    else:
        args["pairing_key"] = None

    field = data.get("disapproved_reason", None)
    if field is not None:
        args["disapproved_reason"] = field
    else:
        args["disapproved_reason"] = None

    return PartnerHost(**args)


def unmarshal_SelfHost(data: Any) -> SelfHost:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SelfHost' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("connection_id", None)
    if field is not None:
        args["connection_id"] = field
    else:
        args["connection_id"] = None

    return SelfHost(**args)


def unmarshal_Link(data: Any) -> Link:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Link' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("pop_id", None)
    if field is not None:
        args["pop_id"] = field
    else:
        args["pop_id"] = None

    field = data.get("bandwidth_mbps", None)
    if field is not None:
        args["bandwidth_mbps"] = field
    else:
        args["bandwidth_mbps"] = 0

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = LinkStatus.UNKNOWN_LINK_STATUS

    field = data.get("bgp_v4_status", None)
    if field is not None:
        args["bgp_v4_status"] = field
    else:
        args["bgp_v4_status"] = BgpStatus.UNKNOWN_BGP_STATUS

    field = data.get("bgp_v6_status", None)
    if field is not None:
        args["bgp_v6_status"] = field
    else:
        args["bgp_v6_status"] = BgpStatus.UNKNOWN_BGP_STATUS

    field = data.get("enable_route_propagation", None)
    if field is not None:
        args["enable_route_propagation"] = field
    else:
        args["enable_route_propagation"] = False

    field = data.get("vlan", None)
    if field is not None:
        args["vlan"] = field
    else:
        args["vlan"] = 0

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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

    field = data.get("partner", None)
    if field is not None:
        args["partner"] = unmarshal_PartnerHost(field)
    else:
        args["partner"] = None

    field = data.get("self", None)
    if field is not None:
        args["self_"] = unmarshal_SelfHost(field)
    else:
        args["self_"] = None

    field = data.get("scw_bgp_config", None)
    if field is not None:
        args["scw_bgp_config"] = unmarshal_BgpConfig(field)
    else:
        args["scw_bgp_config"] = None

    field = data.get("peer_bgp_config", None)
    if field is not None:
        args["peer_bgp_config"] = unmarshal_BgpConfig(field)
    else:
        args["peer_bgp_config"] = None

    field = data.get("routing_policy_v4_id", None)
    if field is not None:
        args["routing_policy_v4_id"] = field
    else:
        args["routing_policy_v4_id"] = None

    field = data.get("routing_policy_v6_id", None)
    if field is not None:
        args["routing_policy_v6_id"] = field
    else:
        args["routing_policy_v6_id"] = None

    return Link(**args)


def unmarshal_Partner(data: Any) -> Partner:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Partner' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("contact_email", None)
    if field is not None:
        args["contact_email"] = field
    else:
        args["contact_email"] = None

    field = data.get("logo_url", None)
    if field is not None:
        args["logo_url"] = field
    else:
        args["logo_url"] = None

    field = data.get("portal_url", None)
    if field is not None:
        args["portal_url"] = field
    else:
        args["portal_url"] = None

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

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("hosting_provider_name", None)
    if field is not None:
        args["hosting_provider_name"] = field
    else:
        args["hosting_provider_name"] = None

    field = data.get("address", None)
    if field is not None:
        args["address"] = field
    else:
        args["address"] = None

    field = data.get("city", None)
    if field is not None:
        args["city"] = field
    else:
        args["city"] = None

    field = data.get("logo_url", None)
    if field is not None:
        args["logo_url"] = field
    else:
        args["logo_url"] = None

    field = data.get("available_link_bandwidths_mbps", None)
    if field is not None:
        args["available_link_bandwidths_mbps"] = field
    else:
        args["available_link_bandwidths_mbps"] = []

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    return Pop(**args)


def unmarshal_RoutingPolicy(data: Any) -> RoutingPolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RoutingPolicy' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("prefix_filter_in", None)
    if field is not None:
        args["prefix_filter_in"] = field
    else:
        args["prefix_filter_in"] = []

    field = data.get("prefix_filter_out", None)
    if field is not None:
        args["prefix_filter_out"] = field
    else:
        args["prefix_filter_out"] = []

    field = data.get("is_ipv6", None)
    if field is not None:
        args["is_ipv6"] = field
    else:
        args["is_ipv6"] = False

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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


def unmarshal_ListDedicatedConnectionsResponse(
    data: Any,
) -> ListDedicatedConnectionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDedicatedConnectionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("connections", None)
    if field is not None:
        args["connections"] = (
            [unmarshal_DedicatedConnection(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["connections"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListDedicatedConnectionsResponse(**args)


def unmarshal_ListLinksResponse(data: Any) -> ListLinksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLinksResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("links", None)
    if field is not None:
        args["links"] = (
            [unmarshal_Link(v) for v in field] if field is not None else None
        )
    else:
        args["links"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListLinksResponse(**args)


def unmarshal_ListPartnersResponse(data: Any) -> ListPartnersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPartnersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("partners", None)
    if field is not None:
        args["partners"] = (
            [unmarshal_Partner(v) for v in field] if field is not None else None
        )
    else:
        args["partners"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListPartnersResponse(**args)


def unmarshal_ListPopsResponse(data: Any) -> ListPopsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPopsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("pops", None)
    if field is not None:
        args["pops"] = [unmarshal_Pop(v) for v in field] if field is not None else None
    else:
        args["pops"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListPopsResponse(**args)


def unmarshal_ListRoutingPoliciesResponse(data: Any) -> ListRoutingPoliciesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRoutingPoliciesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("routing_policies", None)
    if field is not None:
        args["routing_policies"] = (
            [unmarshal_RoutingPolicy(v) for v in field] if field is not None else None
        )
    else:
        args["routing_policies"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListRoutingPoliciesResponse(**args)


def marshal_AttachRoutingPolicyRequest(
    request: AttachRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.routing_policy_id is not None:
        output["routing_policy_id"] = request.routing_policy_id

    return output


def marshal_AttachVpcRequest(
    request: AttachVpcRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.vpc_id is not None:
        output["vpc_id"] = request.vpc_id

    return output


def marshal_CreateLinkRequest(
    request: CreateLinkRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="connection_id",
                    value=request.connection_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="partner_id", value=request.partner_id, marshal_func=None
                ),
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
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.peer_asn is not None:
        output["peer_asn"] = request.peer_asn

    if request.vlan is not None:
        output["vlan"] = request.vlan

    if request.routing_policy_v4_id is not None:
        output["routing_policy_v4_id"] = request.routing_policy_v4_id

    if request.routing_policy_v6_id is not None:
        output["routing_policy_v6_id"] = request.routing_policy_v6_id

    return output


def marshal_CreateRoutingPolicyRequest(
    request: CreateRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.prefix_filter_in is not None:
        output["prefix_filter_in"] = request.prefix_filter_in

    if request.prefix_filter_out is not None:
        output["prefix_filter_out"] = request.prefix_filter_out

    return output


def marshal_DetachRoutingPolicyRequest(
    request: DetachRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.routing_policy_id is not None:
        output["routing_policy_id"] = request.routing_policy_id

    return output


def marshal_SetRoutingPolicyRequest(
    request: SetRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.routing_policy_id is not None:
        output["routing_policy_id"] = request.routing_policy_id

    return output


def marshal_UpdateLinkRequest(
    request: UpdateLinkRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.peer_asn is not None:
        output["peer_asn"] = request.peer_asn

    return output


def marshal_UpdateRoutingPolicyRequest(
    request: UpdateRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.prefix_filter_in is not None:
        output["prefix_filter_in"] = request.prefix_filter_in

    if request.prefix_filter_out is not None:
        output["prefix_filter_out"] = request.prefix_filter_out

    return output
