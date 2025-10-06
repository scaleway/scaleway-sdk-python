# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    validate_path_param,
    fetch_all_pages,
)
from .types import (
    ListAuthenticationEventsRequestOrderBy,
    ListCombinedEventsRequestOrderBy,
    ListEventsRequestOrderBy,
    ListExportJobsRequestOrderBy,
    ResourceType,
    CreateExportJobRequest,
    ExportJob,
    ExportJobS3,
    ListAuthenticationEventsResponse,
    ListCombinedEventsResponse,
    ListEventsResponse,
    ListExportJobsResponse,
    ListProductsResponse,
)
from .marshalling import (
    unmarshal_ExportJob,
    unmarshal_ListAuthenticationEventsResponse,
    unmarshal_ListCombinedEventsResponse,
    unmarshal_ListEventsResponse,
    unmarshal_ListExportJobsResponse,
    unmarshal_ListProductsResponse,
    marshal_CreateExportJobRequest,
)


class AuditTrailV1Alpha1API(API):
    """
    This API allows you to ensure accountability and security by recording events and changes performed within your Scaleway Organization.
    """

    def list_events(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        resource_type: Optional[ResourceType] = None,
        method_name: Optional[str] = None,
        status: Optional[int] = None,
        recorded_after: Optional[datetime] = None,
        recorded_before: Optional[datetime] = None,
        order_by: Optional[ListEventsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        product_name: Optional[str] = None,
        service_name: Optional[str] = None,
        resource_id: Optional[str] = None,
        principal_id: Optional[str] = None,
        source_ip: Optional[str] = None,
    ) -> ListEventsResponse:
        """
        List events.
        Retrieve the list of Audit Trail events for a Scaleway Organization and/or Project. You must specify the `organization_id` and optionally, the `project_id`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: (Optional) ID of the Project containing the Audit Trail events.
        :param organization_id: ID of the Organization containing the Audit Trail events.
        :param resource_type: (Optional) Type of the Scaleway resource.
        :param method_name: (Optional) Name of the method of the API call performed.
        :param status: (Optional) HTTP status code of the request. Returns either `200` if the request was successful or `403` if the permission was denied.
        :param recorded_after: (Optional) The `recorded_after` parameter defines the earliest timestamp from which Audit Trail events are retrieved. Returns `one hour ago` by default.
        :param recorded_before: (Optional) The `recorded_before` parameter defines the latest timestamp up to which Audit Trail events are retrieved. Returns `now` by default.
        :param order_by:
        :param page_size:
        :param page_token:
        :param product_name: (Optional) Name of the Scaleway product in a hyphenated format.
        :param service_name: (Optional) Name of the service of the API call performed.
        :param resource_id: (Optional) ID of the Scaleway resource.
        :param principal_id: (Optional) ID of the User or IAM application at the origin of the event.
        :param source_ip: (Optional) IP address at the origin of the event.
        :return: :class:`ListEventsResponse <ListEventsResponse>`

        Usage:
        ::

            result = api.list_events()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/audit-trail/v1alpha1/regions/{param_region}/events",
            params={
                "method_name": method_name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                "principal_id": principal_id,
                "product_name": product_name,
                "project_id": project_id or self.client.default_project_id,
                "recorded_after": recorded_after,
                "recorded_before": recorded_before,
                "resource_id": resource_id,
                "resource_type": resource_type,
                "service_name": service_name,
                "source_ip": source_ip,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListEventsResponse(res.json())

    def list_authentication_events(
        self,
        *,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
        recorded_after: Optional[datetime] = None,
        recorded_before: Optional[datetime] = None,
        order_by: Optional[ListAuthenticationEventsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
    ) -> ListAuthenticationEventsResponse:
        """
        List authentication events.
        Retrieve the list of Audit Trail authentication events for a Scaleway Organization. You must specify the `organization_id`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id:
        :param recorded_after:
        :param recorded_before:
        :param order_by:
        :param page_size:
        :param page_token:
        :return: :class:`ListAuthenticationEventsResponse <ListAuthenticationEventsResponse>`

        Usage:
        ::

            result = api.list_authentication_events()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/audit-trail/v1alpha1/regions/{param_region}/authentication-events",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                "recorded_after": recorded_after,
                "recorded_before": recorded_before,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListAuthenticationEventsResponse(res.json())

    def list_combined_events(
        self,
        *,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        resource_type: Optional[ResourceType] = None,
        recorded_after: Optional[datetime] = None,
        recorded_before: Optional[datetime] = None,
        order_by: Optional[ListCombinedEventsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
    ) -> ListCombinedEventsResponse:
        """
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id:
        :param project_id:
        :param resource_type:
        :param recorded_after:
        :param recorded_before:
        :param order_by:
        :param page_size:
        :param page_token:
        :return: :class:`ListCombinedEventsResponse <ListCombinedEventsResponse>`

        Usage:
        ::

            result = api.list_combined_events()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/audit-trail/v1alpha1/regions/{param_region}/combined-events",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                "project_id": project_id or self.client.default_project_id,
                "recorded_after": recorded_after,
                "recorded_before": recorded_before,
                "resource_type": resource_type,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListCombinedEventsResponse(res.json())

    def list_products(
        self,
        *,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
    ) -> ListProductsResponse:
        """
        Retrieve the list of Scaleway resources for which you have Audit Trail events.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: ID of the Organization containing the Audit Trail events.
        :return: :class:`ListProductsResponse <ListProductsResponse>`

        Usage:
        ::

            result = api.list_products()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/audit-trail/v1alpha1/regions/{param_region}/products",
            params={
                "organization_id": organization_id
                or self.client.default_organization_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListProductsResponse(res.json())

    def create_export_job(
        self,
        *,
        name: str,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
        s3: Optional[ExportJobS3] = None,
        tags: Optional[dict[str, str]] = None,
    ) -> ExportJob:
        """
        Create an export job.
        Create an export job for a specified organization. This allows you to export audit trail events to a destination, such as an S3 bucket. The request requires the organization ID, a name for the export, and a destination configuration.
        :param name: Name of the export.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: ID of the Organization to target.
        :param s3: The configuration specifying the bucket where the audit trail events will be exported.
        One-Of ('destination'): at most one of 's3' could be set.
        :param tags: Tags of the export.
        :return: :class:`ExportJob <ExportJob>`

        Usage:
        ::

            result = api.create_export_job(
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/audit-trail/v1alpha1/regions/{param_region}/export-jobs",
            body=marshal_CreateExportJobRequest(
                CreateExportJobRequest(
                    name=name,
                    region=region,
                    organization_id=organization_id,
                    tags=tags,
                    s3=s3,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ExportJob(res.json())

    def delete_export_job(
        self,
        *,
        export_job_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete an export job.
        Deletes an export job for a specified id.
        :param export_job_id: ID of the export job.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_export_job(
                export_job_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_export_job_id = validate_path_param("export_job_id", export_job_id)

        res = self._request(
            "DELETE",
            f"/audit-trail/v1alpha1/regions/{param_region}/export-jobs/{param_export_job_id}",
        )

        self._throw_on_error(res)

    def list_export_jobs(
        self,
        *,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[dict[str, str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListExportJobsRequestOrderBy] = None,
    ) -> ListExportJobsResponse:
        """
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Filter by Organization ID.
        :param name: (Optional) Filter by export name.
        :param tags: (Optional) List of tags to filter on.
        :param page:
        :param page_size:
        :param order_by:
        :return: :class:`ListExportJobsResponse <ListExportJobsResponse>`

        Usage:
        ::

            result = api.list_export_jobs()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/audit-trail/v1alpha1/regions/{param_region}/export-jobs",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListExportJobsResponse(res.json())

    def list_export_jobs_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[dict[str, str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListExportJobsRequestOrderBy] = None,
    ) -> list[ExportJob]:
        """
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Filter by Organization ID.
        :param name: (Optional) Filter by export name.
        :param tags: (Optional) List of tags to filter on.
        :param page:
        :param page_size:
        :param order_by:
        :return: :class:`list[ExportJob] <list[ExportJob]>`

        Usage:
        ::

            result = api.list_export_jobs_all()
        """

        return fetch_all_pages(
            type=ListExportJobsResponse,
            key="export_jobs",
            fetcher=self.list_export_jobs,
            args={
                "region": region,
                "organization_id": organization_id,
                "name": name,
                "tags": tags,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )
