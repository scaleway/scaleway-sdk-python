# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ProductCategory(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PRODUCT_CATEGORY = "unknown_product_category"
    APPLE_SILICON = "apple_silicon"
    BLOCK_STORAGE = "block_storage"
    DEDIBOX = "dedibox"
    ELASTIC_METAL = "elastic_metal"
    INSTANCES = "instances"
    OBJECT_STORAGE = "object_storage"
    LOAD_BALANCER = "load_balancer"
    KUBERNETES = "kubernetes"

    def __str__(self) -> str:
        return str(self.value)


class ReportType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_REPORT_TYPE = "unknown_report_type"
    MONTHLY = "monthly"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)


class ServiceCategory(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SERVICE_CATEGORY = "unknown_service_category"
    BAREMETAL = "baremetal"
    COMPUTE = "compute"
    STORAGE = "storage"
    NETWORK = "network"
    CONTAINERS = "containers"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Impact:
    kg_co2_equivalent: float
    """
    The estimated carbon emissions in kilograms of CO₂ equivalent (kgCO₂e).
    """

    m3_water_usage: float
    """
    The estimated water consumption in cubic meters (m³).
    """


@dataclass
class SkuImpact:
    sku: str
    """
    Unique ID of the combination of product, region and zone.
    """

    service_category: ServiceCategory
    """
    The service category associated with this SKU.
    """

    product_category: ProductCategory
    """
    The product category associated with this SKU.
    """

    total_sku_impact: Optional[Impact] = None
    """
    The total estimated impact for this SKU during the given period.
    """


@dataclass
class ZoneImpact:
    zone: ScwZone
    """
    ID of the zone.
    """

    skus: list[SkuImpact]
    """
    List of estimated impact values per SKU.
    """

    total_zone_impact: Optional[Impact] = None
    """
    The total estimated impact for this zone across all given service categories, and product categories during the given period.
    """


@dataclass
class RegionImpact:
    region: ScwRegion
    """
    ID of the region.
    """

    zones: list[ZoneImpact]
    """
    List of estimated impact values per zone.
    """

    total_region_impact: Optional[Impact] = None
    """
    The total estimated impact for this region across all given zones, service categories, and product categories during the given period.
    """


@dataclass
class ProjectImpact:
    project_id: str
    """
    ID of the project.
    """

    regions: list[RegionImpact]
    """
    List of estimated impact values per region.
    """

    total_project_impact: Optional[Impact] = None
    """
    The total estimated impact for this Project across all given regions, zones, service categories, and product categories during the given period.
    """


@dataclass
class ImpactDataResponse:
    projects: list[ProjectImpact]
    """
    List of estimated impact values per Project.
    """

    start_date: Optional[datetime] = None
    """
    Start date of the impact data period (inclusive).
    """

    end_date: Optional[datetime] = None
    """
    End date of the impact data period (exclusive).
    """

    total_impact: Optional[Impact] = None
    """
    The total estimated impact across all given Projects, regions, zones, service categories, and product categories during the given period.
    """


@dataclass
class ImpactReportAvailability:
    month_summary_reports: list[datetime]
    """
    The list of calendar months for which impact reports are available.
    """

    yearly_summary_reports: list[datetime]
    """
    The list of calendar years for which impact reports are available.
    """


@dataclass
class UserApiDownloadImpactReportRequest:
    organization_id: Optional[str] = None
    """
    The UUID of the Organization for which you want to download a report.
    """

    date: Optional[datetime] = None
    """
    The start date of the period for which you want to download a report (ISO 8601 format, e.g. 2025-05-01T00:00:00Z).
    """

    type_: Optional[ReportType] = ReportType.UNKNOWN_REPORT_TYPE
    """
    Type of report to download (e.g. `monthly`).
    """


@dataclass
class UserApiGetImpactDataRequest:
    organization_id: Optional[str] = None
    """
    The UUID of the Organization for which you want to download a report.
    """

    start_date: Optional[datetime] = None
    """
    Start date (inclusive) of the period for which you want to retrieve impact data (ISO 8601 format, e.g. 2025-05-01T00:00:00Z).
    """

    end_date: Optional[datetime] = None
    """
    End date (exclusive) of the period for which you want to retrieve impact data (ISO 8601 format, with time in UTC, `YYYY-MM-DDTHH:MM:SSZ`). Defaults to today's date.
    """

    regions: Optional[list[str]] = field(default_factory=list)
    """
    List of regions to filter by (e.g. `fr-par`). Defaults to all regions.
    """

    zones: Optional[list[str]] = field(default_factory=list)
    """
    List of zones to filter by (e.g. `fr-par-1`). Defaults to all zones.
    """

    project_ids: Optional[list[str]] = field(default_factory=list)
    """
    List of Project IDs to filter by. Defaults to all Projects in the Organization.
    """

    service_categories: Optional[list[ServiceCategory]] = field(default_factory=list)
    """
    List of service categories to filter by. Defaults to all service categories.
    """

    product_categories: Optional[list[ProductCategory]] = field(default_factory=list)
    """
    List of product categories to filter by. Defaults to all product categories.
    """


@dataclass
class UserApiGetImpactReportAvailabilityRequest:
    organization_id: Optional[str] = None
    """
    The UUID of the Organization for which you want to download a report.
    """

    start_date: Optional[datetime] = None
    """
    Start date of the search period (ISO 8601 format, with time in UTC, `YYYY-MM-DDTHH:MM:SSZ`). The date is inclusive.
    """

    end_date: Optional[datetime] = None
    """
    End date of the search period (ISO 8601 format, with time in UTC, `YYYY-MM-DDTHH:MM:SSZ`). The date is inclusive. Defaults to today's date.
    """
