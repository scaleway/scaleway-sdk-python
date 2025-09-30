# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    ProductCategory,
    ServiceCategory,
    Impact,
    SkuImpact,
    ZoneImpact,
    RegionImpact,
    ProjectImpact,
    ImpactDataResponse,
    ImpactReportAvailability,
    UserApiDownloadImpactReportRequest,
)


def unmarshal_Impact(data: Any) -> Impact:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Impact' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("kg_co2_equivalent", None)
    if field is not None:
        args["kg_co2_equivalent"] = field
    else:
        args["kg_co2_equivalent"] = 0.0

    field = data.get("m3_water_usage", None)
    if field is not None:
        args["m3_water_usage"] = field
    else:
        args["m3_water_usage"] = 0.0

    return Impact(**args)


def unmarshal_SkuImpact(data: Any) -> SkuImpact:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SkuImpact' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("sku", None)
    if field is not None:
        args["sku"] = field
    else:
        args["sku"] = None

    field = data.get("service_category", None)
    if field is not None:
        args["service_category"] = field
    else:
        args["service_category"] = ServiceCategory.UNKNOWN_SERVICE_CATEGORY

    field = data.get("product_category", None)
    if field is not None:
        args["product_category"] = field
    else:
        args["product_category"] = ProductCategory.UNKNOWN_PRODUCT_CATEGORY

    field = data.get("total_sku_impact", None)
    if field is not None:
        args["total_sku_impact"] = unmarshal_Impact(field)
    else:
        args["total_sku_impact"] = None

    return SkuImpact(**args)


def unmarshal_ZoneImpact(data: Any) -> ZoneImpact:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ZoneImpact' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("skus", None)
    if field is not None:
        args["skus"] = (
            [unmarshal_SkuImpact(v) for v in field] if field is not None else None
        )
    else:
        args["skus"] = []

    field = data.get("total_zone_impact", None)
    if field is not None:
        args["total_zone_impact"] = unmarshal_Impact(field)
    else:
        args["total_zone_impact"] = None

    return ZoneImpact(**args)


def unmarshal_RegionImpact(data: Any) -> RegionImpact:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RegionImpact' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("zones", None)
    if field is not None:
        args["zones"] = (
            [unmarshal_ZoneImpact(v) for v in field] if field is not None else None
        )
    else:
        args["zones"] = []

    field = data.get("total_region_impact", None)
    if field is not None:
        args["total_region_impact"] = unmarshal_Impact(field)
    else:
        args["total_region_impact"] = None

    return RegionImpact(**args)


def unmarshal_ProjectImpact(data: Any) -> ProjectImpact:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProjectImpact' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("regions", None)
    if field is not None:
        args["regions"] = (
            [unmarshal_RegionImpact(v) for v in field] if field is not None else None
        )
    else:
        args["regions"] = []

    field = data.get("total_project_impact", None)
    if field is not None:
        args["total_project_impact"] = unmarshal_Impact(field)
    else:
        args["total_project_impact"] = None

    return ProjectImpact(**args)


def unmarshal_ImpactDataResponse(data: Any) -> ImpactDataResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ImpactDataResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("projects", None)
    if field is not None:
        args["projects"] = (
            [unmarshal_ProjectImpact(v) for v in field] if field is not None else None
        )
    else:
        args["projects"] = []

    field = data.get("start_date", None)
    if field is not None:
        args["start_date"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["start_date"] = None

    field = data.get("end_date", None)
    if field is not None:
        args["end_date"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["end_date"] = None

    field = data.get("total_impact", None)
    if field is not None:
        args["total_impact"] = unmarshal_Impact(field)
    else:
        args["total_impact"] = None

    return ImpactDataResponse(**args)


def unmarshal_ImpactReportAvailability(data: Any) -> ImpactReportAvailability:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ImpactReportAvailability' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("month_summary_reports", None)
    if field is not None:
        args["month_summary_reports"] = field
    else:
        args["month_summary_reports"] = None

    return ImpactReportAvailability(**args)


def marshal_UserApiDownloadImpactReportRequest(
    request: UserApiDownloadImpactReportRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    if request.date is not None:
        output["date"] = request.date.isoformat()

    if request.type_ is not None:
        output["type"] = request.type_

    return output
