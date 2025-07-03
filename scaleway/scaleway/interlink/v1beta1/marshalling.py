# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    BgpStatus,
    DedicatedConnectionStatus,
    LinkKind,
    LinkStatus,
    ListDedicatedConnectionsRequestOrderBy,
    ListLinksRequestOrderBy,
    ListPartnersRequestOrderBy,
    ListPopsRequestOrderBy,
    ListRoutingPoliciesRequestOrderBy,
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
    UpdateLinkRequest,
    UpdateRoutingPolicyRequest,
)

def unmarshal_DedicatedConnection(data: Any) -> DedicatedConnection:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DedicatedConnection' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("status", getattr(DedicatedConnectionStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("pop_id", str())
    args["pop_id"] = field

    field = data.get("bandwidth_mbps", 0)
    args["bandwidth_mbps"] = field

    field = data.get("available_link_bandwidths", [])
    args["available_link_bandwidths"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("demarcation_info", None)
    args["demarcation_info"] = field

    return DedicatedConnection(**args)

def unmarshal_BgpConfig(data: Any) -> BgpConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BgpConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("asn", 0)
    args["asn"] = field

    field = data.get("ipv4", str())
    args["ipv4"] = field

    field = data.get("ipv6", str())
    args["ipv6"] = field

    return BgpConfig(**args)

def unmarshal_PartnerHost(data: Any) -> PartnerHost:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PartnerHost' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("partner_id", str())
    args["partner_id"] = field

    field = data.get("pairing_key", str())
    args["pairing_key"] = field

    field = data.get("disapproved_reason", None)
    args["disapproved_reason"] = field

    return PartnerHost(**args)

def unmarshal_SelfHost(data: Any) -> SelfHost:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SelfHost' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("connection_id", str())
    args["connection_id"] = field

    return SelfHost(**args)

def unmarshal_Link(data: Any) -> Link:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Link' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("pop_id", str())
    args["pop_id"] = field

    field = data.get("bandwidth_mbps", 0)
    args["bandwidth_mbps"] = field

    field = data.get("status", getattr(LinkStatus, "UNKNOWN_LINK_STATUS"))
    args["status"] = field

    field = data.get("bgp_v4_status", getattr(BgpStatus, "UNKNOWN_BGP_STATUS"))
    args["bgp_v4_status"] = field

    field = data.get("bgp_v6_status", getattr(BgpStatus, "UNKNOWN_BGP_STATUS"))
    args["bgp_v6_status"] = field

    field = data.get("enable_route_propagation", False)
    args["enable_route_propagation"] = field

    field = data.get("vlan", 0)
    args["vlan"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("vpc_id", None)
    args["vpc_id"] = field

    field = data.get("routing_policy_id", None)
    args["routing_policy_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("partner", None)
    args["partner"] = unmarshal_PartnerHost(field) if field is not None else None

    field = data.get("self", None)
    args["self_"] = unmarshal_SelfHost(field) if field is not None else None

    field = data.get("scw_bgp_config", None)
    args["scw_bgp_config"] = unmarshal_BgpConfig(field) if field is not None else None

    field = data.get("peer_bgp_config", None)
    args["peer_bgp_config"] = unmarshal_BgpConfig(field) if field is not None else None

    field = data.get("routing_policy_v4_id", None)
    args["routing_policy_v4_id"] = field

    field = data.get("routing_policy_v6_id", None)
    args["routing_policy_v6_id"] = field

    return Link(**args)

def unmarshal_Partner(data: Any) -> Partner:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Partner' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("contact_email", str())
    args["contact_email"] = field

    field = data.get("logo_url", str())
    args["logo_url"] = field

    field = data.get("portal_url", str())
    args["portal_url"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Partner(**args)

def unmarshal_Pop(data: Any) -> Pop:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Pop' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("hosting_provider_name", str())
    args["hosting_provider_name"] = field

    field = data.get("address", str())
    args["address"] = field

    field = data.get("city", str())
    args["city"] = field

    field = data.get("logo_url", str())
    args["logo_url"] = field

    field = data.get("available_link_bandwidths_mbps", [])
    args["available_link_bandwidths_mbps"] = field

    field = data.get("region", )
    args["region"] = field

    return Pop(**args)

def unmarshal_RoutingPolicy(data: Any) -> RoutingPolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RoutingPolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("prefix_filter_in", [])
    args["prefix_filter_in"] = field

    field = data.get("prefix_filter_out", [])
    args["prefix_filter_out"] = field

    field = data.get("is_ipv6", False)
    args["is_ipv6"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return RoutingPolicy(**args)

def unmarshal_ListDedicatedConnectionsResponse(data: Any) -> ListDedicatedConnectionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDedicatedConnectionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("connections", [])
    args["connections"] = [unmarshal_DedicatedConnection(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListDedicatedConnectionsResponse(**args)

def unmarshal_ListLinksResponse(data: Any) -> ListLinksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLinksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("links", [])
    args["links"] = [unmarshal_Link(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListLinksResponse(**args)

def unmarshal_ListPartnersResponse(data: Any) -> ListPartnersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPartnersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("partners", [])
    args["partners"] = [unmarshal_Partner(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListPartnersResponse(**args)

def unmarshal_ListPopsResponse(data: Any) -> ListPopsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPopsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pops", [])
    args["pops"] = [unmarshal_Pop(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListPopsResponse(**args)

def unmarshal_ListRoutingPoliciesResponse(data: Any) -> ListRoutingPoliciesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRoutingPoliciesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("routing_policies", str())
    args["routing_policies"] = [unmarshal_RoutingPolicy(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListRoutingPoliciesResponse(**args)

def marshal_AttachRoutingPolicyRequest(
    request: AttachRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.routing_policy_id is not None:
        output["routing_policy_id"] = request.routing_policy_id
    else:
        output["routing_policy_id"] = str()


    return output

def marshal_AttachVpcRequest(
    request: AttachVpcRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.vpc_id is not None:
        output["vpc_id"] = request.vpc_id
    else:
        output["vpc_id"] = str()


    return output

def marshal_CreateLinkRequest(
    request: CreateLinkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="connection_id", value=request.connection_id,marshal_func=None
            ),
            OneOfPossibility(param="partner_id", value=request.partner_id,marshal_func=None
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.pop_id is not None:
        output["pop_id"] = request.pop_id
    else:
        output["pop_id"] = str()

    if request.bandwidth_mbps is not None:
        output["bandwidth_mbps"] = request.bandwidth_mbps
    else:
        output["bandwidth_mbps"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.peer_asn is not None:
        output["peer_asn"] = request.peer_asn
    else:
        output["peer_asn"] = None

    if request.vlan is not None:
        output["vlan"] = request.vlan
    else:
        output["vlan"] = None


    return output

def marshal_CreateRoutingPolicyRequest(
    request: CreateRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6
    else:
        output["is_ipv6"] = False

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.prefix_filter_in is not None:
        output["prefix_filter_in"] = request.prefix_filter_in
    else:
        output["prefix_filter_in"] = None

    if request.prefix_filter_out is not None:
        output["prefix_filter_out"] = request.prefix_filter_out
    else:
        output["prefix_filter_out"] = None


    return output

def marshal_DetachRoutingPolicyRequest(
    request: DetachRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.routing_policy_id is not None:
        output["routing_policy_id"] = request.routing_policy_id
    else:
        output["routing_policy_id"] = str()


    return output

def marshal_UpdateLinkRequest(
    request: UpdateLinkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.peer_asn is not None:
        output["peer_asn"] = request.peer_asn
    else:
        output["peer_asn"] = None


    return output

def marshal_UpdateRoutingPolicyRequest(
    request: UpdateRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.prefix_filter_in is not None:
        output["prefix_filter_in"] = request.prefix_filter_in
    else:
        output["prefix_filter_in"] = None

    if request.prefix_filter_out is not None:
        output["prefix_filter_out"] = request.prefix_filter_out
    else:
        output["prefix_filter_out"] = None


    return output
