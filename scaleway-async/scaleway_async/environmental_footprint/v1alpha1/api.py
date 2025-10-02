# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    ScwFile,
    unmarshal_ScwFile,
)
from .types import (
    ProductCategory,
    ReportType,
    ServiceCategory,
    ImpactDataResponse,
    ImpactReportAvailability,
    UserApiDownloadImpactReportRequest,
)
from .marshalling import (
    unmarshal_ImpactDataResponse,
    unmarshal_ImpactReportAvailability,
    marshal_UserApiDownloadImpactReportRequest,
)


class EnvironmentalFootprintV1Alpha1UserAPI(API):
    """
    Access and download impact reports and impact data for your Scaleway projects. Our API provides key metrics such as estimated carbon emissions and water usage to help monitor your environmental footprint.
    """

    async def get_impact_report_availability(
        self,
        *,
        organization_id: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> ImpactReportAvailability:
        """
        Get available impact reports.
        Returns a list of dates of available impact reports.
        :param organization_id: The UUID of the Organization for which you want to download a report.
        :param start_date: Start date of the search period (ISO 8601 format, with time in UTC, `YYYY-MM-DDTHH:MM:SSZ`). The date is inclusive.
        :param end_date: End date of the search period (ISO 8601 format, with time in UTC, `YYYY-MM-DDTHH:MM:SSZ`). The date is inclusive. Defaults to today's date.
        :return: :class:`ImpactReportAvailability <ImpactReportAvailability>`

        Usage:
        ::

            result = await api.get_impact_report_availability()
        """

        res = self._request(
            "GET",
            "/environmental-footprint/v1alpha1/reports/availability",
            params={
                "end_date": end_date,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "start_date": start_date,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ImpactReportAvailability(res.json())

    async def download_impact_report(
        self,
        *,
        organization_id: Optional[str] = None,
        date: Optional[datetime] = None,
        type_: Optional[ReportType] = None,
    ) -> ScwFile:
        """
        Download PDF impact report.
        Download a Scaleway impact PDF report with detailed impact data for your Scaleway projects.
        :param organization_id: The UUID of the Organization for which you want to download a report.
        :param date: The start date of the period for which you want to download a report (ISO 8601 format, e.g. 2025-05-01T00:00:00Z).
        :param type_: Type of report to download (e.g. `monthly`).
        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = await api.download_impact_report()
        """

        res = self._request(
            "POST",
            "/environmental-footprint/v1alpha1/reports/download",
            body=marshal_UserApiDownloadImpactReportRequest(
                UserApiDownloadImpactReportRequest(
                    organization_id=organization_id,
                    date=date,
                    type_=type_,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())

    async def get_impact_data(
        self,
        *,
        organization_id: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        regions: Optional[list[str]] = None,
        zones: Optional[list[str]] = None,
        project_ids: Optional[list[str]] = None,
        service_categories: Optional[list[ServiceCategory]] = None,
        product_categories: Optional[list[ProductCategory]] = None,
    ) -> ImpactDataResponse:
        """
        Retrieve detailed impact data.
        Retrieve detailed impact data for your Scaleway projects within a specified date range. Filter by project ID, region, zone, service category, and/or product category.
        :param organization_id: The UUID of the Organization for which you want to download a report.
        :param start_date: Start date (inclusive) of the period for which you want to retrieve impact data (ISO 8601 format, e.g. 2025-05-01T00:00:00Z).
        :param end_date: End date (exclusive) of the period for which you want to retrieve impact data (ISO 8601 format, with time in UTC, `YYYY-MM-DDTHH:MM:SSZ`). Defaults to today's date.
        :param regions: List of regions to filter by (e.g. `fr-par`). Defaults to all regions.
        :param zones: List of zones to filter by (e.g. `fr-par-1`). Defaults to all zones.
        :param project_ids: List of Project IDs to filter by. Defaults to all Projects in the Organization.
        :param service_categories: List of service categories to filter by. Defaults to all service categories.
        :param product_categories: List of product categories to filter by. Defaults to all product categories.
        :return: :class:`ImpactDataResponse <ImpactDataResponse>`

        Usage:
        ::

            result = await api.get_impact_data()
        """

        res = self._request(
            "GET",
            "/environmental-footprint/v1alpha1/data/query",
            params={
                "end_date": end_date,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "product_categories": product_categories,
                "project_ids": project_ids,
                "regions": regions,
                "service_categories": service_categories,
                "start_date": start_date,
                "zones": zones,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ImpactDataResponse(res.json())
