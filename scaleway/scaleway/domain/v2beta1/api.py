# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    ScwFile,
    unmarshal_ScwFile,
)
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    ContactEmailStatus,
    DomainStatus,
    ListContactsRequestRole,
    ListDNSZoneRecordsRequestOrderBy,
    ListDNSZonesRequestOrderBy,
    ListDomainsRequestOrderBy,
    ListRenewableDomainsRequestOrderBy,
    ListTasksRequestOrderBy,
    ListTldsRequestOrderBy,
    RawFormat,
    RecordType,
    TaskStatus,
    TaskType,
    CheckContactsCompatibilityResponse,
    ClearDNSZoneRecordsResponse,
    CloneDNSZoneRequest,
    Contact,
    ContactExtensionEU,
    ContactExtensionFR,
    ContactExtensionNL,
    ContactRoles,
    CreateDNSZoneRequest,
    CreateSSLCertificateRequest,
    DNSZone,
    DNSZoneVersion,
    DSRecord,
    DeleteDNSZoneResponse,
    DeleteExternalDomainResponse,
    DeleteSSLCertificateResponse,
    Domain,
    DomainSummary,
    GetDNSZoneTsigKeyResponse,
    GetDNSZoneVersionDiffResponse,
    GetDomainAuthCodeResponse,
    Host,
    ImportProviderDNSZoneRequest,
    ImportProviderDNSZoneRequestOnlineV1,
    ImportProviderDNSZoneResponse,
    ImportRawDNSZoneRequest,
    ImportRawDNSZoneRequestAXFRSource,
    ImportRawDNSZoneRequestBindSource,
    ImportRawDNSZoneResponse,
    ListContactsResponse,
    ListDNSZoneNameserversResponse,
    ListDNSZoneRecordsResponse,
    ListDNSZoneVersionRecordsResponse,
    ListDNSZoneVersionsResponse,
    ListDNSZonesResponse,
    ListDomainHostsResponse,
    ListDomainsResponse,
    ListRenewableDomainsResponse,
    ListSSLCertificatesResponse,
    ListTasksResponse,
    ListTldsResponse,
    Nameserver,
    NewContact,
    OrderResponse,
    Record,
    RecordChange,
    RefreshDNSZoneRequest,
    RefreshDNSZoneResponse,
    RegisterExternalDomainResponse,
    RegistrarApiBuyDomainsRequest,
    RegistrarApiCheckContactsCompatibilityRequest,
    RegistrarApiCreateDomainHostRequest,
    RegistrarApiEnableDomainDNSSECRequest,
    RegistrarApiRegisterExternalDomainRequest,
    RegistrarApiRenewDomainsRequest,
    RegistrarApiTradeDomainRequest,
    RegistrarApiTransferInDomainRequest,
    RegistrarApiUpdateContactRequest,
    RegistrarApiUpdateDomainHostRequest,
    RegistrarApiUpdateDomainRequest,
    RenewableDomain,
    RestoreDNSZoneVersionResponse,
    SSLCertificate,
    SearchAvailableDomainsResponse,
    Task,
    Tld,
    TransferInDomainRequestTransferRequest,
    UpdateContactRequestQuestion,
    UpdateDNSZoneNameserversRequest,
    UpdateDNSZoneNameserversResponse,
    UpdateDNSZoneRecordsRequest,
    UpdateDNSZoneRecordsResponse,
    UpdateDNSZoneRequest,
)
from .content import (
    DOMAIN_TRANSIENT_STATUSES,
    SSL_CERTIFICATE_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Contact,
    unmarshal_DNSZone,
    unmarshal_Host,
    unmarshal_SSLCertificate,
    unmarshal_CheckContactsCompatibilityResponse,
    unmarshal_ClearDNSZoneRecordsResponse,
    unmarshal_DeleteDNSZoneResponse,
    unmarshal_DeleteExternalDomainResponse,
    unmarshal_DeleteSSLCertificateResponse,
    unmarshal_Domain,
    unmarshal_GetDNSZoneTsigKeyResponse,
    unmarshal_GetDNSZoneVersionDiffResponse,
    unmarshal_GetDomainAuthCodeResponse,
    unmarshal_ImportProviderDNSZoneResponse,
    unmarshal_ImportRawDNSZoneResponse,
    unmarshal_ListContactsResponse,
    unmarshal_ListDNSZoneNameserversResponse,
    unmarshal_ListDNSZoneRecordsResponse,
    unmarshal_ListDNSZoneVersionRecordsResponse,
    unmarshal_ListDNSZoneVersionsResponse,
    unmarshal_ListDNSZonesResponse,
    unmarshal_ListDomainHostsResponse,
    unmarshal_ListDomainsResponse,
    unmarshal_ListRenewableDomainsResponse,
    unmarshal_ListSSLCertificatesResponse,
    unmarshal_ListTasksResponse,
    unmarshal_ListTldsResponse,
    unmarshal_OrderResponse,
    unmarshal_RefreshDNSZoneResponse,
    unmarshal_RegisterExternalDomainResponse,
    unmarshal_RestoreDNSZoneVersionResponse,
    unmarshal_SearchAvailableDomainsResponse,
    unmarshal_UpdateDNSZoneNameserversResponse,
    unmarshal_UpdateDNSZoneRecordsResponse,
    marshal_CloneDNSZoneRequest,
    marshal_CreateDNSZoneRequest,
    marshal_CreateSSLCertificateRequest,
    marshal_ImportProviderDNSZoneRequest,
    marshal_ImportRawDNSZoneRequest,
    marshal_RefreshDNSZoneRequest,
    marshal_RegistrarApiBuyDomainsRequest,
    marshal_RegistrarApiCheckContactsCompatibilityRequest,
    marshal_RegistrarApiCreateDomainHostRequest,
    marshal_RegistrarApiEnableDomainDNSSECRequest,
    marshal_RegistrarApiRegisterExternalDomainRequest,
    marshal_RegistrarApiRenewDomainsRequest,
    marshal_RegistrarApiTradeDomainRequest,
    marshal_RegistrarApiTransferInDomainRequest,
    marshal_RegistrarApiUpdateContactRequest,
    marshal_RegistrarApiUpdateDomainHostRequest,
    marshal_RegistrarApiUpdateDomainRequest,
    marshal_UpdateDNSZoneNameserversRequest,
    marshal_UpdateDNSZoneRecordsRequest,
    marshal_UpdateDNSZoneRequest,
)
from ...std.types import (
    LanguageCode as StdLanguageCode,
)


class DomainV2Beta1API(API):
    """
    This API allows you to manage your domains, DNS zones and records.
    """

    def list_dns_zones(
        self,
        *,
        domain: str,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        order_by: Optional[ListDNSZonesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        dns_zone: Optional[str] = None,
        dns_zones: Optional[List[str]] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        updated_after: Optional[datetime] = None,
        updated_before: Optional[datetime] = None,
    ) -> ListDNSZonesResponse:
        """
        List DNS zones.
        Retrieve the list of DNS zones you can manage and filter DNS zones associated with specific domain names.
        :param domain: Domain on which to filter the returned DNS zones.
        :param organization_id: Organization ID on which to filter the returned DNS zones.
        :param project_id: Project ID on which to filter the returned DNS zones.
        :param order_by: Sort order of the returned DNS zones.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of DNS zones to return per page.
        :param dns_zone: DNS zone on which to filter the returned DNS zones.
        :param dns_zones: DNS zones on which to filter the returned DNS zones.
        :param created_after: Only list DNS zones created after this date.
        :param created_before: Only list DNS zones created before this date.
        :param updated_after: Only list DNS zones updated after this date.
        :param updated_before: Only list DNS zones updated before this date.
        :return: :class:`ListDNSZonesResponse <ListDNSZonesResponse>`

        Usage:
        ::

            result = api.list_dns_zones(
                domain="example",
            )
        """

        res = self._request(
            "GET",
            "/domain/v2beta1/dns-zones",
            params={
                "created_after": created_after,
                "created_before": created_before,
                "dns_zone": dns_zone,
                "dns_zones": dns_zones,
                "domain": domain,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "updated_after": updated_after,
                "updated_before": updated_before,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDNSZonesResponse(res.json())

    def list_dns_zones_all(
        self,
        *,
        domain: str,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        order_by: Optional[ListDNSZonesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        dns_zone: Optional[str] = None,
        dns_zones: Optional[List[str]] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        updated_after: Optional[datetime] = None,
        updated_before: Optional[datetime] = None,
    ) -> List[DNSZone]:
        """
        List DNS zones.
        Retrieve the list of DNS zones you can manage and filter DNS zones associated with specific domain names.
        :param domain: Domain on which to filter the returned DNS zones.
        :param organization_id: Organization ID on which to filter the returned DNS zones.
        :param project_id: Project ID on which to filter the returned DNS zones.
        :param order_by: Sort order of the returned DNS zones.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of DNS zones to return per page.
        :param dns_zone: DNS zone on which to filter the returned DNS zones.
        :param dns_zones: DNS zones on which to filter the returned DNS zones.
        :param created_after: Only list DNS zones created after this date.
        :param created_before: Only list DNS zones created before this date.
        :param updated_after: Only list DNS zones updated after this date.
        :param updated_before: Only list DNS zones updated before this date.
        :return: :class:`List[DNSZone] <List[DNSZone]>`

        Usage:
        ::

            result = api.list_dns_zones_all(
                domain="example",
            )
        """

        return fetch_all_pages(
            type=ListDNSZonesResponse,
            key="dns_zones",
            fetcher=self.list_dns_zones,
            args={
                "domain": domain,
                "organization_id": organization_id,
                "project_id": project_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "dns_zone": dns_zone,
                "dns_zones": dns_zones,
                "created_after": created_after,
                "created_before": created_before,
                "updated_after": updated_after,
                "updated_before": updated_before,
            },
        )

    def create_dns_zone(
        self,
        *,
        domain: str,
        subdomain: str,
        project_id: Optional[str] = None,
    ) -> DNSZone:
        """
        Create a DNS zone.
        Create a new DNS zone specified by the domain name, the subdomain and the Project ID.
        :param domain: Domain in which to crreate the DNS zone.
        :param subdomain: Subdomain of the DNS zone to create.
        :param project_id: Project ID in which to create the DNS zone.
        :return: :class:`DNSZone <DNSZone>`

        Usage:
        ::

            result = api.create_dns_zone(
                domain="example",
                subdomain="example",
            )
        """

        res = self._request(
            "POST",
            "/domain/v2beta1/dns-zones",
            body=marshal_CreateDNSZoneRequest(
                CreateDNSZoneRequest(
                    domain=domain,
                    subdomain=subdomain,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DNSZone(res.json())

    def update_dns_zone(
        self,
        *,
        dns_zone: str,
        new_dns_zone: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> DNSZone:
        """
        Update a DNS zone.
        Update the name and/or the Organizations for a DNS zone.
        :param dns_zone: DNS zone to update.
        :param new_dns_zone: Name of the new DNS zone to create.
        :param project_id: Project ID in which to create the new DNS zone.
        :return: :class:`DNSZone <DNSZone>`

        Usage:
        ::

            result = api.update_dns_zone(
                dns_zone="example",
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "PATCH",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}",
            body=marshal_UpdateDNSZoneRequest(
                UpdateDNSZoneRequest(
                    dns_zone=dns_zone,
                    new_dns_zone=new_dns_zone,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DNSZone(res.json())

    def clone_dns_zone(
        self,
        *,
        dns_zone: str,
        dest_dns_zone: str,
        overwrite: bool,
        project_id: Optional[str] = None,
    ) -> DNSZone:
        """
        Clone a DNS zone.
        Clone an existing DNS zone with all its records into a new DNS zone.
        :param dns_zone: DNS zone to clone.
        :param dest_dns_zone: Destination DNS zone in which to clone the chosen DNS zone.
        :param overwrite: Specifies whether or not the destination DNS zone will be overwritten.
        :param project_id: Project ID of the destination DNS zone.
        :return: :class:`DNSZone <DNSZone>`

        Usage:
        ::

            result = api.clone_dns_zone(
                dns_zone="example",
                dest_dns_zone="example",
                overwrite=False,
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "POST",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}/clone",
            body=marshal_CloneDNSZoneRequest(
                CloneDNSZoneRequest(
                    dns_zone=dns_zone,
                    dest_dns_zone=dest_dns_zone,
                    overwrite=overwrite,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DNSZone(res.json())

    def delete_dns_zone(
        self,
        *,
        dns_zone: str,
        project_id: Optional[str] = None,
    ) -> DeleteDNSZoneResponse:
        """
        Delete a DNS zone.
        Delete a DNS zone and all its records.
        :param dns_zone: DNS zone to delete.
        :param project_id: Project ID of the DNS zone to delete.
        :return: :class:`DeleteDNSZoneResponse <DeleteDNSZoneResponse>`

        Usage:
        ::

            result = api.delete_dns_zone(
                dns_zone="example",
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "DELETE",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_DeleteDNSZoneResponse(res.json())

    def list_dns_zone_records(
        self,
        *,
        project_id: Optional[str] = None,
        order_by: Optional[ListDNSZoneRecordsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        dns_zone: str,
        name: str,
        type_: Optional[RecordType] = None,
        id: Optional[str] = None,
    ) -> ListDNSZoneRecordsResponse:
        """
        List records within a DNS zone.
        Retrieve a list of DNS records within a DNS zone that has default name servers.
        You can filter records by type and name.
        :param project_id: Project ID on which to filter the returned DNS zone records.
        :param order_by: Sort order of the returned DNS zone records.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of DNS zone records per page.
        :param dns_zone: DNS zone on which to filter the returned DNS zone records.
        :param name: Name on which to filter the returned DNS zone records.
        :param type_: Record type on which to filter the returned DNS zone records.
        :param id: Record ID on which to filter the returned DNS zone records.
        :return: :class:`ListDNSZoneRecordsResponse <ListDNSZoneRecordsResponse>`

        Usage:
        ::

            result = api.list_dns_zone_records(
                dns_zone="example",
                name="example",
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "GET",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}/records",
            params={
                "id": id,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "type": type_,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDNSZoneRecordsResponse(res.json())

    def list_dns_zone_records_all(
        self,
        *,
        project_id: Optional[str] = None,
        order_by: Optional[ListDNSZoneRecordsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        dns_zone: str,
        name: str,
        type_: Optional[RecordType] = None,
        id: Optional[str] = None,
    ) -> List[Record]:
        """
        List records within a DNS zone.
        Retrieve a list of DNS records within a DNS zone that has default name servers.
        You can filter records by type and name.
        :param project_id: Project ID on which to filter the returned DNS zone records.
        :param order_by: Sort order of the returned DNS zone records.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of DNS zone records per page.
        :param dns_zone: DNS zone on which to filter the returned DNS zone records.
        :param name: Name on which to filter the returned DNS zone records.
        :param type_: Record type on which to filter the returned DNS zone records.
        :param id: Record ID on which to filter the returned DNS zone records.
        :return: :class:`List[Record] <List[Record]>`

        Usage:
        ::

            result = api.list_dns_zone_records_all(
                dns_zone="example",
                name="example",
            )
        """

        return fetch_all_pages(
            type=ListDNSZoneRecordsResponse,
            key="records",
            fetcher=self.list_dns_zone_records,
            args={
                "project_id": project_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "dns_zone": dns_zone,
                "name": name,
                "type_": type_,
                "id": id,
            },
        )

    def update_dns_zone_records(
        self,
        *,
        dns_zone: str,
        changes: List[RecordChange],
        disallow_new_zone_creation: bool,
        return_all_records: Optional[bool] = None,
        serial: Optional[int] = None,
    ) -> UpdateDNSZoneRecordsResponse:
        """
        Update records within a DNS zone.
        Update records within a DNS zone that has default name servers and perform several actions on your records.

        Actions include:
         - add: allows you to add a new record or add a new IP to an existing A record, for example
         - set: allows you to edit a record or edit an IP from an existing A record, for example
         - delete: allows you to delete a record or delete an IP from an existing A record, for example
         - clear: allows you to delete all records from a DNS zone

        All edits will be versioned.
        :param dns_zone: DNS zone in which to update the DNS zone records.
        :param changes: Changes made to the records.
        :param disallow_new_zone_creation: Disable the creation of the target zone if it does not exist. Target zone creation is disabled by default.
        :param return_all_records: Specifies whether or not to return all the records.
        :param serial: Use the provided serial (0) instead of the auto-increment serial.
        :return: :class:`UpdateDNSZoneRecordsResponse <UpdateDNSZoneRecordsResponse>`

        Usage:
        ::

            result = api.update_dns_zone_records(
                dns_zone="example",
                changes=[],
                disallow_new_zone_creation=False,
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "PATCH",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}/records",
            body=marshal_UpdateDNSZoneRecordsRequest(
                UpdateDNSZoneRecordsRequest(
                    dns_zone=dns_zone,
                    changes=changes,
                    disallow_new_zone_creation=disallow_new_zone_creation,
                    return_all_records=return_all_records,
                    serial=serial,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_UpdateDNSZoneRecordsResponse(res.json())

    def list_dns_zone_nameservers(
        self,
        *,
        project_id: Optional[str] = None,
        dns_zone: str,
    ) -> ListDNSZoneNameserversResponse:
        """
        List name servers within a DNS zone.
        Retrieve a list of name servers within a DNS zone and their optional glue records.
        :param project_id: Project ID on which to filter the returned DNS zone name servers.
        :param dns_zone: DNS zone on which to filter the returned DNS zone name servers.
        :return: :class:`ListDNSZoneNameserversResponse <ListDNSZoneNameserversResponse>`

        Usage:
        ::

            result = api.list_dns_zone_nameservers(
                dns_zone="example",
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "GET",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}/nameservers",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDNSZoneNameserversResponse(res.json())

    def update_dns_zone_nameservers(
        self,
        *,
        dns_zone: str,
        ns: List[Nameserver],
    ) -> UpdateDNSZoneNameserversResponse:
        """
        Update name servers within a DNS zone.
        Update name servers within a DNS zone and set optional glue records.
        :param dns_zone: DNS zone in which to update the DNS zone name servers.
        :param ns: New DNS zone name servers.
        :return: :class:`UpdateDNSZoneNameserversResponse <UpdateDNSZoneNameserversResponse>`

        Usage:
        ::

            result = api.update_dns_zone_nameservers(
                dns_zone="example",
                ns=[],
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "PUT",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}/nameservers",
            body=marshal_UpdateDNSZoneNameserversRequest(
                UpdateDNSZoneNameserversRequest(
                    dns_zone=dns_zone,
                    ns=ns,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_UpdateDNSZoneNameserversResponse(res.json())

    def clear_dns_zone_records(
        self,
        *,
        dns_zone: str,
    ) -> ClearDNSZoneRecordsResponse:
        """
        Clear records within a DNS zone.
        Delete all records within a DNS zone that has default name servers.<br/>
        All edits will be versioned.
        :param dns_zone: DNS zone to clear.
        :return: :class:`ClearDNSZoneRecordsResponse <ClearDNSZoneRecordsResponse>`

        Usage:
        ::

            result = api.clear_dns_zone_records(
                dns_zone="example",
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "DELETE",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}/records",
        )

        self._throw_on_error(res)
        return unmarshal_ClearDNSZoneRecordsResponse(res.json())

    def export_raw_dns_zone(
        self,
        *,
        dns_zone: str,
        format: Optional[RawFormat] = None,
    ) -> ScwFile:
        """
        Export a raw DNS zone.
        Export a DNS zone with default name servers, in a specific format.
        :param dns_zone: DNS zone to export.
        :param format: DNS zone format.
        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = api.export_raw_dns_zone(
                dns_zone="example",
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "GET",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}/raw",
            params={
                "format": format,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())

    def import_raw_dns_zone(
        self,
        *,
        dns_zone: str,
        content: Optional[str] = None,
        project_id: Optional[str] = None,
        format: Optional[RawFormat] = None,
        bind_source: Optional[ImportRawDNSZoneRequestBindSource] = None,
        axfr_source: Optional[ImportRawDNSZoneRequestAXFRSource] = None,
    ) -> ImportRawDNSZoneResponse:
        """
        Import a raw DNS zone.
        Import and replace the format of records from a given provider, with default name servers.
        :param dns_zone: DNS zone to import.
        :param content:
        :param project_id:
        :param format:
        :param bind_source: Import a bind file format.
        One-Of ('source'): at most one of 'bind_source', 'axfr_source' could be set.
        :param axfr_source: Import from the name server given with TSIG, to use or not.
        One-Of ('source'): at most one of 'bind_source', 'axfr_source' could be set.
        :return: :class:`ImportRawDNSZoneResponse <ImportRawDNSZoneResponse>`

        Usage:
        ::

            result = api.import_raw_dns_zone(
                dns_zone="example",
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "POST",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}/raw",
            body=marshal_ImportRawDNSZoneRequest(
                ImportRawDNSZoneRequest(
                    dns_zone=dns_zone,
                    content=content,
                    project_id=project_id,
                    format=format,
                    bind_source=bind_source,
                    axfr_source=axfr_source,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ImportRawDNSZoneResponse(res.json())

    def import_provider_dns_zone(
        self,
        *,
        dns_zone: str,
        online_v1: Optional[ImportProviderDNSZoneRequestOnlineV1] = None,
    ) -> ImportProviderDNSZoneResponse:
        """
        Import a DNS zone from another provider.
        Import and replace the format of records from a given provider, with default name servers.
        :param dns_zone:
        :param online_v1:
        One-Of ('provider'): at most one of 'online_v1' could be set.
        :return: :class:`ImportProviderDNSZoneResponse <ImportProviderDNSZoneResponse>`

        Usage:
        ::

            result = api.import_provider_dns_zone(
                dns_zone="example",
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "POST",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}/import-provider",
            body=marshal_ImportProviderDNSZoneRequest(
                ImportProviderDNSZoneRequest(
                    dns_zone=dns_zone,
                    online_v1=online_v1,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ImportProviderDNSZoneResponse(res.json())

    def refresh_dns_zone(
        self,
        *,
        dns_zone: str,
        recreate_dns_zone: bool,
        recreate_sub_dns_zone: bool,
    ) -> RefreshDNSZoneResponse:
        """
        Refresh a DNS zone.
        Refresh an SOA DNS zone to reload the records in the DNS zone and update the SOA serial.
        You can recreate the given DNS zone and its sub DNS zone if needed.
        :param dns_zone: DNS zone to refresh.
        :param recreate_dns_zone: Specifies whether or not to recreate the DNS zone.
        :param recreate_sub_dns_zone: Specifies whether or not to recreate the sub DNS zone.
        :return: :class:`RefreshDNSZoneResponse <RefreshDNSZoneResponse>`

        Usage:
        ::

            result = api.refresh_dns_zone(
                dns_zone="example",
                recreate_dns_zone=False,
                recreate_sub_dns_zone=False,
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "POST",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}/refresh",
            body=marshal_RefreshDNSZoneRequest(
                RefreshDNSZoneRequest(
                    dns_zone=dns_zone,
                    recreate_dns_zone=recreate_dns_zone,
                    recreate_sub_dns_zone=recreate_sub_dns_zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RefreshDNSZoneResponse(res.json())

    def list_dns_zone_versions(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        dns_zone: str,
    ) -> ListDNSZoneVersionsResponse:
        """
        List versions of a DNS zone.
        Retrieve a list of a DNS zone's versions.<br/>
        The maximum version count is 100. If the count reaches this limit, the oldest version will be deleted after each new modification.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of DNS zones versions per page.
        :param dns_zone:
        :return: :class:`ListDNSZoneVersionsResponse <ListDNSZoneVersionsResponse>`

        Usage:
        ::

            result = api.list_dns_zone_versions(
                dns_zone="example",
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "GET",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}/versions",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDNSZoneVersionsResponse(res.json())

    def list_dns_zone_versions_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        dns_zone: str,
    ) -> List[DNSZoneVersion]:
        """
        List versions of a DNS zone.
        Retrieve a list of a DNS zone's versions.<br/>
        The maximum version count is 100. If the count reaches this limit, the oldest version will be deleted after each new modification.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of DNS zones versions per page.
        :param dns_zone:
        :return: :class:`List[DNSZoneVersion] <List[DNSZoneVersion]>`

        Usage:
        ::

            result = api.list_dns_zone_versions_all(
                dns_zone="example",
            )
        """

        return fetch_all_pages(
            type=ListDNSZoneVersionsResponse,
            key="versions",
            fetcher=self.list_dns_zone_versions,
            args={
                "page": page,
                "page_size": page_size,
                "dns_zone": dns_zone,
            },
        )

    def list_dns_zone_version_records(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        dns_zone_version_id: str,
    ) -> ListDNSZoneVersionRecordsResponse:
        """
        List records from a given version of a specific DNS zone.
        Retrieve a list of records from a specific DNS zone version.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of DNS zones versions records per page.
        :param dns_zone_version_id:
        :return: :class:`ListDNSZoneVersionRecordsResponse <ListDNSZoneVersionRecordsResponse>`

        Usage:
        ::

            result = api.list_dns_zone_version_records(
                dns_zone_version_id="example",
            )
        """

        param_dns_zone_version_id = validate_path_param(
            "dns_zone_version_id", dns_zone_version_id
        )

        res = self._request(
            "GET",
            f"/domain/v2beta1/dns-zones/version/{param_dns_zone_version_id}",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDNSZoneVersionRecordsResponse(res.json())

    def list_dns_zone_version_records_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        dns_zone_version_id: str,
    ) -> List[Record]:
        """
        List records from a given version of a specific DNS zone.
        Retrieve a list of records from a specific DNS zone version.
        :param page: Page number to return, from the paginated results.
        :param page_size: Maximum number of DNS zones versions records per page.
        :param dns_zone_version_id:
        :return: :class:`List[Record] <List[Record]>`

        Usage:
        ::

            result = api.list_dns_zone_version_records_all(
                dns_zone_version_id="example",
            )
        """

        return fetch_all_pages(
            type=ListDNSZoneVersionRecordsResponse,
            key="records",
            fetcher=self.list_dns_zone_version_records,
            args={
                "page": page,
                "page_size": page_size,
                "dns_zone_version_id": dns_zone_version_id,
            },
        )

    def get_dns_zone_version_diff(
        self,
        *,
        dns_zone_version_id: str,
    ) -> GetDNSZoneVersionDiffResponse:
        """
        Access differences from a specific DNS zone version.
        Access a previous DNS zone version to see the differences from another specific version.
        :param dns_zone_version_id:
        :return: :class:`GetDNSZoneVersionDiffResponse <GetDNSZoneVersionDiffResponse>`

        Usage:
        ::

            result = api.get_dns_zone_version_diff(
                dns_zone_version_id="example",
            )
        """

        param_dns_zone_version_id = validate_path_param(
            "dns_zone_version_id", dns_zone_version_id
        )

        res = self._request(
            "GET",
            f"/domain/v2beta1/dns-zones/version/{param_dns_zone_version_id}/diff",
        )

        self._throw_on_error(res)
        return unmarshal_GetDNSZoneVersionDiffResponse(res.json())

    def restore_dns_zone_version(
        self,
        *,
        dns_zone_version_id: str,
    ) -> RestoreDNSZoneVersionResponse:
        """
        Restore a DNS zone version.
        Restore and activate a version of a specific DNS zone.
        :param dns_zone_version_id:
        :return: :class:`RestoreDNSZoneVersionResponse <RestoreDNSZoneVersionResponse>`

        Usage:
        ::

            result = api.restore_dns_zone_version(
                dns_zone_version_id="example",
            )
        """

        param_dns_zone_version_id = validate_path_param(
            "dns_zone_version_id", dns_zone_version_id
        )

        res = self._request(
            "POST",
            f"/domain/v2beta1/dns-zones/version/{param_dns_zone_version_id}/restore",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_RestoreDNSZoneVersionResponse(res.json())

    def get_ssl_certificate(
        self,
        *,
        dns_zone: str,
    ) -> SSLCertificate:
        """
        Get a DNS zone's TLS certificate.
        Get the DNS zone's TLS certificate. If you do not have a certificate, the ouptut returns `no certificate found`.
        :param dns_zone:
        :return: :class:`SSLCertificate <SSLCertificate>`

        Usage:
        ::

            result = api.get_ssl_certificate(
                dns_zone="example",
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "GET",
            f"/domain/v2beta1/ssl-certificates/{param_dns_zone}",
        )

        self._throw_on_error(res)
        return unmarshal_SSLCertificate(res.json())

    def wait_for_ssl_certificate(
        self,
        *,
        dns_zone: str,
        options: Optional[WaitForOptions[SSLCertificate, bool]] = None,
    ) -> SSLCertificate:
        """
        Get a DNS zone's TLS certificate.
        Get the DNS zone's TLS certificate. If you do not have a certificate, the ouptut returns `no certificate found`.
        :param dns_zone:
        :return: :class:`SSLCertificate <SSLCertificate>`

        Usage:
        ::

            result = api.get_ssl_certificate(
                dns_zone="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = (
                lambda res: res.status not in SSL_CERTIFICATE_TRANSIENT_STATUSES
            )

        return wait_for_resource(
            fetcher=self.get_ssl_certificate,
            options=options,
            args={
                "dns_zone": dns_zone,
            },
        )

    def create_ssl_certificate(
        self,
        *,
        dns_zone: str,
        alternative_dns_zones: Optional[List[str]] = None,
    ) -> SSLCertificate:
        """
        Create or get the DNS zone's TLS certificate.
        Create a new TLS certificate or retrieve information about an existing TLS certificate.
        :param dns_zone:
        :param alternative_dns_zones:
        :return: :class:`SSLCertificate <SSLCertificate>`

        Usage:
        ::

            result = api.create_ssl_certificate(
                dns_zone="example",
            )
        """

        res = self._request(
            "POST",
            "/domain/v2beta1/ssl-certificates",
            body=marshal_CreateSSLCertificateRequest(
                CreateSSLCertificateRequest(
                    dns_zone=dns_zone,
                    alternative_dns_zones=alternative_dns_zones,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SSLCertificate(res.json())

    def list_ssl_certificates(
        self,
        *,
        dns_zone: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
    ) -> ListSSLCertificatesResponse:
        """
        List a user's TLS certificates.
        List all the TLS certificates a user has created, specified by the user's Project ID and the DNS zone.
        :param dns_zone:
        :param page:
        :param page_size:
        :param project_id:
        :return: :class:`ListSSLCertificatesResponse <ListSSLCertificatesResponse>`

        Usage:
        ::

            result = api.list_ssl_certificates(
                dns_zone="example",
            )
        """

        res = self._request(
            "GET",
            "/domain/v2beta1/ssl-certificates",
            params={
                "dns_zone": dns_zone,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSSLCertificatesResponse(res.json())

    def list_ssl_certificates_all(
        self,
        *,
        dns_zone: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
    ) -> List[SSLCertificate]:
        """
        List a user's TLS certificates.
        List all the TLS certificates a user has created, specified by the user's Project ID and the DNS zone.
        :param dns_zone:
        :param page:
        :param page_size:
        :param project_id:
        :return: :class:`List[SSLCertificate] <List[SSLCertificate]>`

        Usage:
        ::

            result = api.list_ssl_certificates_all(
                dns_zone="example",
            )
        """

        return fetch_all_pages(
            type=ListSSLCertificatesResponse,
            key="certificates",
            fetcher=self.list_ssl_certificates,
            args={
                "dns_zone": dns_zone,
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
            },
        )

    def delete_ssl_certificate(
        self,
        *,
        dns_zone: str,
    ) -> DeleteSSLCertificateResponse:
        """
        Delete a TLS certificate.
        Delete an existing TLS certificate specified by its DNS zone. Deleting a TLS certificate is permanent and cannot be undone.
        :param dns_zone:
        :return: :class:`DeleteSSLCertificateResponse <DeleteSSLCertificateResponse>`

        Usage:
        ::

            result = api.delete_ssl_certificate(
                dns_zone="example",
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "DELETE",
            f"/domain/v2beta1/ssl-certificates/{param_dns_zone}",
        )

        self._throw_on_error(res)
        return unmarshal_DeleteSSLCertificateResponse(res.json())

    def get_dns_zone_tsig_key(
        self,
        *,
        dns_zone: str,
    ) -> GetDNSZoneTsigKeyResponse:
        """
        Get the DNS zone's TSIG key.
        Retrieve information about the TSIG key of a given DNS zone to allow AXFR requests.
        :param dns_zone:
        :return: :class:`GetDNSZoneTsigKeyResponse <GetDNSZoneTsigKeyResponse>`

        Usage:
        ::

            result = api.get_dns_zone_tsig_key(
                dns_zone="example",
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "GET",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}/tsig-key",
        )

        self._throw_on_error(res)
        return unmarshal_GetDNSZoneTsigKeyResponse(res.json())

    def delete_dns_zone_tsig_key(
        self,
        *,
        dns_zone: str,
    ) -> None:
        """
        Delete the DNS zone's TSIG key.
        Delete an existing TSIG key specified by its DNS zone. Deleting a TSIG key is permanent and cannot be undone.
        :param dns_zone:

        Usage:
        ::

            result = api.delete_dns_zone_tsig_key(
                dns_zone="example",
            )
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "DELETE",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}/tsig-key",
        )

        self._throw_on_error(res)


class DomainV2Beta1RegistrarAPI(API):
    """
    Manage your domains and contacts.
    """

    def list_tasks(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        domain: Optional[str] = None,
        types: Optional[List[TaskType]] = None,
        statuses: Optional[List[TaskStatus]] = None,
        order_by: Optional[ListTasksRequestOrderBy] = None,
    ) -> ListTasksResponse:
        """
        List tasks.
        List all operations performed on the account.
        You can filter the list of tasks by domain name.
        :param page:
        :param page_size:
        :param project_id:
        :param organization_id:
        :param domain:
        :param types:
        :param statuses:
        :param order_by:
        :return: :class:`ListTasksResponse <ListTasksResponse>`

        Usage:
        ::

            result = api.list_tasks()
        """

        res = self._request(
            "GET",
            "/domain/v2beta1/tasks",
            params={
                "domain": domain,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "statuses": statuses,
                "types": types,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTasksResponse(res.json())

    def list_tasks_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        domain: Optional[str] = None,
        types: Optional[List[TaskType]] = None,
        statuses: Optional[List[TaskStatus]] = None,
        order_by: Optional[ListTasksRequestOrderBy] = None,
    ) -> List[Task]:
        """
        List tasks.
        List all operations performed on the account.
        You can filter the list of tasks by domain name.
        :param page:
        :param page_size:
        :param project_id:
        :param organization_id:
        :param domain:
        :param types:
        :param statuses:
        :param order_by:
        :return: :class:`List[Task] <List[Task]>`

        Usage:
        ::

            result = api.list_tasks_all()
        """

        return fetch_all_pages(
            type=ListTasksResponse,
            key="tasks",
            fetcher=self.list_tasks,
            args={
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
                "organization_id": organization_id,
                "domain": domain,
                "types": types,
                "statuses": statuses,
                "order_by": order_by,
            },
        )

    def buy_domains(
        self,
        *,
        domains: List[str],
        duration_in_years: int,
        project_id: Optional[str] = None,
        owner_contact_id: Optional[str] = None,
        owner_contact: Optional[NewContact] = None,
        administrative_contact_id: Optional[str] = None,
        administrative_contact: Optional[NewContact] = None,
        technical_contact_id: Optional[str] = None,
        technical_contact: Optional[NewContact] = None,
    ) -> OrderResponse:
        """
        Purchase domains.
        Request the registration of domain names.
        You can provide a domain's already existing contact or a new contact.
        :param domains:
        :param duration_in_years:
        :param project_id:
        :param owner_contact_id:
        One-Of ('owner_contact_type'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param owner_contact:
        One-Of ('owner_contact_type'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param administrative_contact_id:
        One-Of ('administrative_contact_type'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :param administrative_contact:
        One-Of ('administrative_contact_type'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :param technical_contact_id:
        One-Of ('technical_contact_type'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :param technical_contact:
        One-Of ('technical_contact_type'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :return: :class:`OrderResponse <OrderResponse>`

        Usage:
        ::

            result = api.buy_domains(
                domains=[],
                duration_in_years=1,
            )
        """

        res = self._request(
            "POST",
            "/domain/v2beta1/buy-domains",
            body=marshal_RegistrarApiBuyDomainsRequest(
                RegistrarApiBuyDomainsRequest(
                    domains=domains,
                    duration_in_years=duration_in_years,
                    project_id=project_id,
                    owner_contact_id=owner_contact_id,
                    owner_contact=owner_contact,
                    administrative_contact_id=administrative_contact_id,
                    administrative_contact=administrative_contact,
                    technical_contact_id=technical_contact_id,
                    technical_contact=technical_contact,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_OrderResponse(res.json())

    def renew_domains(
        self,
        *,
        domains: List[str],
        duration_in_years: int,
        force_late_renewal: Optional[bool] = None,
    ) -> OrderResponse:
        """
        Renew domains.
        Request the renewal of one or more domain names.
        :param domains:
        :param duration_in_years:
        :param force_late_renewal:
        :return: :class:`OrderResponse <OrderResponse>`

        Usage:
        ::

            result = api.renew_domains(
                domains=[],
                duration_in_years=1,
            )
        """

        res = self._request(
            "POST",
            "/domain/v2beta1/renew-domains",
            body=marshal_RegistrarApiRenewDomainsRequest(
                RegistrarApiRenewDomainsRequest(
                    domains=domains,
                    duration_in_years=duration_in_years,
                    force_late_renewal=force_late_renewal,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_OrderResponse(res.json())

    def transfer_in_domain(
        self,
        *,
        domains: List[TransferInDomainRequestTransferRequest],
        project_id: Optional[str] = None,
        owner_contact_id: Optional[str] = None,
        owner_contact: Optional[NewContact] = None,
        administrative_contact_id: Optional[str] = None,
        administrative_contact: Optional[NewContact] = None,
        technical_contact_id: Optional[str] = None,
        technical_contact: Optional[NewContact] = None,
    ) -> OrderResponse:
        """
        Transfer a domain.
        Request the transfer of a domain from another registrar to Scaleway Domains and DNS.
        :param domains:
        :param project_id:
        :param owner_contact_id:
        One-Of ('owner_contact_type'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param owner_contact:
        One-Of ('owner_contact_type'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param administrative_contact_id:
        One-Of ('administrative_contact_type'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :param administrative_contact:
        One-Of ('administrative_contact_type'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :param technical_contact_id:
        One-Of ('technical_contact_type'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :param technical_contact:
        One-Of ('technical_contact_type'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :return: :class:`OrderResponse <OrderResponse>`

        Usage:
        ::

            result = api.transfer_in_domain(
                domains=[],
            )
        """

        res = self._request(
            "POST",
            "/domain/v2beta1/domains/transfer-domains",
            body=marshal_RegistrarApiTransferInDomainRequest(
                RegistrarApiTransferInDomainRequest(
                    domains=domains,
                    project_id=project_id,
                    owner_contact_id=owner_contact_id,
                    owner_contact=owner_contact,
                    administrative_contact_id=administrative_contact_id,
                    administrative_contact=administrative_contact,
                    technical_contact_id=technical_contact_id,
                    technical_contact=technical_contact,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_OrderResponse(res.json())

    def trade_domain(
        self,
        *,
        domain: str,
        project_id: Optional[str] = None,
        new_owner_contact_id: Optional[str] = None,
        new_owner_contact: Optional[NewContact] = None,
    ) -> OrderResponse:
        """
        Trade a domain's contact.
        Request to change a domain's contact owner.<br/>
        If you specify the `organization_id` of the domain's new owner, the contact will change from the current owner's Scaleway account to the new owner's Scaleway account.<br/>
        If the new owner's current contact information is not available, the first ever contact they have created for previous domains is taken into account to operate the change.<br/>
        If the new owner has never created a contact to register domains before, an error message displays.
        :param domain:
        :param project_id:
        :param new_owner_contact_id:
        One-Of ('new_owner_contact_type'): at most one of 'new_owner_contact_id', 'new_owner_contact' could be set.
        :param new_owner_contact:
        One-Of ('new_owner_contact_type'): at most one of 'new_owner_contact_id', 'new_owner_contact' could be set.
        :return: :class:`OrderResponse <OrderResponse>`

        Usage:
        ::

            result = api.trade_domain(
                domain="example",
            )
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "POST",
            f"/domain/v2beta1/domains/{param_domain}/trade",
            body=marshal_RegistrarApiTradeDomainRequest(
                RegistrarApiTradeDomainRequest(
                    domain=domain,
                    project_id=project_id,
                    new_owner_contact_id=new_owner_contact_id,
                    new_owner_contact=new_owner_contact,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_OrderResponse(res.json())

    def register_external_domain(
        self,
        *,
        domain: str,
        project_id: Optional[str] = None,
    ) -> RegisterExternalDomainResponse:
        """
        Register an external domain.
        Request the registration of an external domain name.
        :param domain:
        :param project_id:
        :return: :class:`RegisterExternalDomainResponse <RegisterExternalDomainResponse>`

        Usage:
        ::

            result = api.register_external_domain(
                domain="example",
            )
        """

        res = self._request(
            "POST",
            "/domain/v2beta1/external-domains",
            body=marshal_RegistrarApiRegisterExternalDomainRequest(
                RegistrarApiRegisterExternalDomainRequest(
                    domain=domain,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RegisterExternalDomainResponse(res.json())

    def delete_external_domain(
        self,
        *,
        domain: str,
    ) -> DeleteExternalDomainResponse:
        """
        Delete an external domain.
        Delete an external domain name.
        :param domain:
        :return: :class:`DeleteExternalDomainResponse <DeleteExternalDomainResponse>`

        Usage:
        ::

            result = api.delete_external_domain(
                domain="example",
            )
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "DELETE",
            f"/domain/v2beta1/external-domains/{param_domain}",
        )

        self._throw_on_error(res)
        return unmarshal_DeleteExternalDomainResponse(res.json())

    def check_contacts_compatibility(
        self,
        *,
        domains: Optional[List[str]] = None,
        tlds: Optional[List[str]] = None,
        owner_contact_id: Optional[str] = None,
        owner_contact: Optional[NewContact] = None,
        administrative_contact_id: Optional[str] = None,
        administrative_contact: Optional[NewContact] = None,
        technical_contact_id: Optional[str] = None,
        technical_contact: Optional[NewContact] = None,
    ) -> CheckContactsCompatibilityResponse:
        """
        Check if contacts are compatible with a domain or a TLD.
        Check whether contacts are compatible with a domain or a TLD.
        If contacts are not compatible with either the domain or the TLD, the information that needs to be corrected is returned.
        :param domains:
        :param tlds:
        :param owner_contact_id:
        One-Of ('owner_contact_type'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param owner_contact:
        One-Of ('owner_contact_type'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param administrative_contact_id:
        One-Of ('administrative_contact_type'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :param administrative_contact:
        One-Of ('administrative_contact_type'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :param technical_contact_id:
        One-Of ('technical_contact_type'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :param technical_contact:
        One-Of ('technical_contact_type'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :return: :class:`CheckContactsCompatibilityResponse <CheckContactsCompatibilityResponse>`

        Usage:
        ::

            result = api.check_contacts_compatibility()
        """

        res = self._request(
            "POST",
            "/domain/v2beta1/check-contacts-compatibility",
            body=marshal_RegistrarApiCheckContactsCompatibilityRequest(
                RegistrarApiCheckContactsCompatibilityRequest(
                    domains=domains,
                    tlds=tlds,
                    owner_contact_id=owner_contact_id,
                    owner_contact=owner_contact,
                    administrative_contact_id=administrative_contact_id,
                    administrative_contact=administrative_contact,
                    technical_contact_id=technical_contact_id,
                    technical_contact=technical_contact,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CheckContactsCompatibilityResponse(res.json())

    def list_contacts(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        domain: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        role: Optional[ListContactsRequestRole] = None,
        email_status: Optional[ContactEmailStatus] = None,
    ) -> ListContactsResponse:
        """
        List contacts.
        Retrieve the list of contacts and their associated domains and roles.
        You can filter the list by domain name.
        :param page:
        :param page_size:
        :param domain:
        :param project_id:
        :param organization_id:
        :param role:
        :param email_status:
        :return: :class:`ListContactsResponse <ListContactsResponse>`

        Usage:
        ::

            result = api.list_contacts()
        """

        res = self._request(
            "GET",
            "/domain/v2beta1/contacts",
            params={
                "domain": domain,
                "email_status": email_status,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "role": role,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListContactsResponse(res.json())

    def list_contacts_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        domain: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        role: Optional[ListContactsRequestRole] = None,
        email_status: Optional[ContactEmailStatus] = None,
    ) -> List[ContactRoles]:
        """
        List contacts.
        Retrieve the list of contacts and their associated domains and roles.
        You can filter the list by domain name.
        :param page:
        :param page_size:
        :param domain:
        :param project_id:
        :param organization_id:
        :param role:
        :param email_status:
        :return: :class:`List[ContactRoles] <List[ContactRoles]>`

        Usage:
        ::

            result = api.list_contacts_all()
        """

        return fetch_all_pages(
            type=ListContactsResponse,
            key="contacts",
            fetcher=self.list_contacts,
            args={
                "page": page,
                "page_size": page_size,
                "domain": domain,
                "project_id": project_id,
                "organization_id": organization_id,
                "role": role,
                "email_status": email_status,
            },
        )

    def get_contact(
        self,
        *,
        contact_id: str,
    ) -> Contact:
        """
        Get a contact.
        Retrieve a contact's details from the registrar using the given contact's ID.
        :param contact_id:
        :return: :class:`Contact <Contact>`

        Usage:
        ::

            result = api.get_contact(
                contact_id="example",
            )
        """

        param_contact_id = validate_path_param("contact_id", contact_id)

        res = self._request(
            "GET",
            f"/domain/v2beta1/contacts/{param_contact_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Contact(res.json())

    def update_contact(
        self,
        *,
        contact_id: str,
        email: Optional[str] = None,
        email_alt: Optional[str] = None,
        phone_number: Optional[str] = None,
        fax_number: Optional[str] = None,
        address_line_1: Optional[str] = None,
        address_line_2: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        country: Optional[str] = None,
        vat_identification_code: Optional[str] = None,
        company_identification_code: Optional[str] = None,
        lang: Optional[StdLanguageCode] = None,
        resale: Optional[bool] = None,
        questions: Optional[List[UpdateContactRequestQuestion]] = None,
        extension_fr: Optional[ContactExtensionFR] = None,
        extension_eu: Optional[ContactExtensionEU] = None,
        whois_opt_in: Optional[bool] = None,
        state: Optional[str] = None,
        extension_nl: Optional[ContactExtensionNL] = None,
    ) -> Contact:
        """
        Update contact.
        Edit the contact's information.
        :param contact_id:
        :param email:
        :param email_alt:
        :param phone_number:
        :param fax_number:
        :param address_line_1:
        :param address_line_2:
        :param zip:
        :param city:
        :param country:
        :param vat_identification_code:
        :param company_identification_code:
        :param lang:
        :param resale:
        :param questions:
        :param extension_fr:
        :param extension_eu:
        :param whois_opt_in:
        :param state:
        :param extension_nl:
        :return: :class:`Contact <Contact>`

        Usage:
        ::

            result = api.update_contact(
                contact_id="example",
            )
        """

        param_contact_id = validate_path_param("contact_id", contact_id)

        res = self._request(
            "PATCH",
            f"/domain/v2beta1/contacts/{param_contact_id}",
            body=marshal_RegistrarApiUpdateContactRequest(
                RegistrarApiUpdateContactRequest(
                    contact_id=contact_id,
                    email=email,
                    email_alt=email_alt,
                    phone_number=phone_number,
                    fax_number=fax_number,
                    address_line_1=address_line_1,
                    address_line_2=address_line_2,
                    zip=zip,
                    city=city,
                    country=country,
                    vat_identification_code=vat_identification_code,
                    company_identification_code=company_identification_code,
                    lang=lang,
                    resale=resale,
                    questions=questions,
                    extension_fr=extension_fr,
                    extension_eu=extension_eu,
                    whois_opt_in=whois_opt_in,
                    state=state,
                    extension_nl=extension_nl,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Contact(res.json())

    def list_domains(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDomainsRequestOrderBy] = None,
        registrar: Optional[str] = None,
        status: Optional[DomainStatus] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        is_external: Optional[bool] = None,
        domain: Optional[str] = None,
    ) -> ListDomainsResponse:
        """
        List domains.
        Retrieve the list of domains you own.
        :param page:
        :param page_size:
        :param order_by:
        :param registrar:
        :param status:
        :param project_id:
        :param organization_id:
        :param is_external:
        :param domain:
        :return: :class:`ListDomainsResponse <ListDomainsResponse>`

        Usage:
        ::

            result = api.list_domains()
        """

        res = self._request(
            "GET",
            "/domain/v2beta1/domains",
            params={
                "domain": domain,
                "is_external": is_external,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "registrar": registrar,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDomainsResponse(res.json())

    def list_domains_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDomainsRequestOrderBy] = None,
        registrar: Optional[str] = None,
        status: Optional[DomainStatus] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        is_external: Optional[bool] = None,
        domain: Optional[str] = None,
    ) -> List[DomainSummary]:
        """
        List domains.
        Retrieve the list of domains you own.
        :param page:
        :param page_size:
        :param order_by:
        :param registrar:
        :param status:
        :param project_id:
        :param organization_id:
        :param is_external:
        :param domain:
        :return: :class:`List[DomainSummary] <List[DomainSummary]>`

        Usage:
        ::

            result = api.list_domains_all()
        """

        return fetch_all_pages(
            type=ListDomainsResponse,
            key="domains",
            fetcher=self.list_domains,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "registrar": registrar,
                "status": status,
                "project_id": project_id,
                "organization_id": organization_id,
                "is_external": is_external,
                "domain": domain,
            },
        )

    def list_renewable_domains(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRenewableDomainsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
    ) -> ListRenewableDomainsResponse:
        """
        List domains that can be renewed.
        Retrieve the list of domains you own that can be renewed. You can also see the maximum renewal duration in years for your domains that are renewable.
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :param organization_id:
        :return: :class:`ListRenewableDomainsResponse <ListRenewableDomainsResponse>`

        Usage:
        ::

            result = api.list_renewable_domains()
        """

        res = self._request(
            "GET",
            "/domain/v2beta1/renewable-domains",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRenewableDomainsResponse(res.json())

    def list_renewable_domains_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRenewableDomainsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
    ) -> List[RenewableDomain]:
        """
        List domains that can be renewed.
        Retrieve the list of domains you own that can be renewed. You can also see the maximum renewal duration in years for your domains that are renewable.
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :param organization_id:
        :return: :class:`List[RenewableDomain] <List[RenewableDomain]>`

        Usage:
        ::

            result = api.list_renewable_domains_all()
        """

        return fetch_all_pages(
            type=ListRenewableDomainsResponse,
            key="domains",
            fetcher=self.list_renewable_domains,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
                "organization_id": organization_id,
            },
        )

    def get_domain(
        self,
        *,
        domain: str,
    ) -> Domain:
        """
        Get domain.
        Retrieve a specific domain and display the domain's information.
        :param domain:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.get_domain(
                domain="example",
            )
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "GET",
            f"/domain/v2beta1/domains/{param_domain}",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def wait_for_domain(
        self,
        *,
        domain: str,
        options: Optional[WaitForOptions[Domain, bool]] = None,
    ) -> Domain:
        """
        Get domain.
        Retrieve a specific domain and display the domain's information.
        :param domain:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.get_domain(
                domain="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in DOMAIN_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_domain,
            options=options,
            args={
                "domain": domain,
            },
        )

    def update_domain(
        self,
        *,
        domain: str,
        technical_contact_id: Optional[str] = None,
        technical_contact: Optional[NewContact] = None,
        owner_contact_id: Optional[str] = None,
        owner_contact: Optional[NewContact] = None,
        administrative_contact_id: Optional[str] = None,
        administrative_contact: Optional[NewContact] = None,
    ) -> Domain:
        """
        Update a domain's contacts.
        Update contacts for a specific domain or create a new contact.<br/>
        If you add the same contact for multiple roles (owner, administrative, technical), only one ID will be created and used for all of the roles.
        :param domain:
        :param technical_contact_id:
        One-Of ('technical_contact_info'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :param technical_contact:
        One-Of ('technical_contact_info'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :param owner_contact_id:
        One-Of ('owner_contact_info'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param owner_contact:
        One-Of ('owner_contact_info'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param administrative_contact_id:
        One-Of ('administrative_contact_info'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :param administrative_contact:
        One-Of ('administrative_contact_info'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.update_domain(
                domain="example",
            )
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "PATCH",
            f"/domain/v2beta1/domains/{param_domain}",
            body=marshal_RegistrarApiUpdateDomainRequest(
                RegistrarApiUpdateDomainRequest(
                    domain=domain,
                    technical_contact_id=technical_contact_id,
                    technical_contact=technical_contact,
                    owner_contact_id=owner_contact_id,
                    owner_contact=owner_contact,
                    administrative_contact_id=administrative_contact_id,
                    administrative_contact=administrative_contact,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def lock_domain_transfer(
        self,
        *,
        domain: str,
    ) -> Domain:
        """
        Lock the transfer of a domain.
        Lock the transfer of a domain. This means that the domain cannot be transferred and the authorization code cannot be requested to your current registrar.
        :param domain:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.lock_domain_transfer(
                domain="example",
            )
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "POST",
            f"/domain/v2beta1/domains/{param_domain}/lock-transfer",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def unlock_domain_transfer(
        self,
        *,
        domain: str,
    ) -> Domain:
        """
        Unlock the transfer of a domain.
        Unlock the transfer of a domain. This means that the domain can be transferred and the authorization code can be requested to your current registrar.
        :param domain:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.unlock_domain_transfer(
                domain="example",
            )
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "POST",
            f"/domain/v2beta1/domains/{param_domain}/unlock-transfer",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def enable_domain_auto_renew(
        self,
        *,
        domain: str,
    ) -> Domain:
        """
        Enable auto renew.
        Enable the `auto renew` feature for a domain. This means the domain will be automatically renewed before its expiry date.
        :param domain:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.enable_domain_auto_renew(
                domain="example",
            )
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "POST",
            f"/domain/v2beta1/domains/{param_domain}/enable-auto-renew",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def disable_domain_auto_renew(
        self,
        *,
        domain: str,
    ) -> Domain:
        """
        Disable auto renew.
        Disable the `auto renew` feature for a domain. This means the domain will not be renewed before its expiry date.
        :param domain:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.disable_domain_auto_renew(
                domain="example",
            )
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "POST",
            f"/domain/v2beta1/domains/{param_domain}/disable-auto-renew",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def get_domain_auth_code(
        self,
        *,
        domain: str,
    ) -> GetDomainAuthCodeResponse:
        """
        Get a domain's authorization code.
        Retrieve the authorization code to tranfer an unlocked domain. The output returns an error if the domain is locked.
        Some TLDs may have a different procedure to retrieve the authorization code. In that case, the information displays in the message field.
        :param domain:
        :return: :class:`GetDomainAuthCodeResponse <GetDomainAuthCodeResponse>`

        Usage:
        ::

            result = api.get_domain_auth_code(
                domain="example",
            )
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "GET",
            f"/domain/v2beta1/domains/{param_domain}/auth-code",
        )

        self._throw_on_error(res)
        return unmarshal_GetDomainAuthCodeResponse(res.json())

    def enable_domain_dnssec(
        self,
        *,
        domain: str,
        ds_record: Optional[DSRecord] = None,
    ) -> Domain:
        """
        Update domain DNSSEC.
        If your domain uses another registrar and has the default Scaleway NS, you have to **update the DS record at your registrar**.
        :param domain:
        :param ds_record:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.enable_domain_dnssec(
                domain="example",
            )
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "POST",
            f"/domain/v2beta1/domains/{param_domain}/enable-dnssec",
            body=marshal_RegistrarApiEnableDomainDNSSECRequest(
                RegistrarApiEnableDomainDNSSECRequest(
                    domain=domain,
                    ds_record=ds_record,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def disable_domain_dnssec(
        self,
        *,
        domain: str,
    ) -> Domain:
        """
        Disable a domain's DNSSEC.
        Disable DNSSEC for a domain.
        :param domain:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.disable_domain_dnssec(
                domain="example",
            )
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "POST",
            f"/domain/v2beta1/domains/{param_domain}/disable-dnssec",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def search_available_domains(
        self,
        *,
        domains: List[str],
        strict_search: bool,
        tlds: Optional[List[str]] = None,
    ) -> SearchAvailableDomainsResponse:
        """
        Search available domains.
        Search a domain or a maximum of 10 domains that are available.

        If the TLD list is empty or not set, the search returns the results from the most popular TLDs.
        :param domains: A list of domain to search, TLD is optional.
        :param strict_search: Search exact match.
        :param tlds: Array of tlds to search on.
        :return: :class:`SearchAvailableDomainsResponse <SearchAvailableDomainsResponse>`

        Usage:
        ::

            result = api.search_available_domains(
                domains=[],
                strict_search=False,
            )
        """

        res = self._request(
            "GET",
            "/domain/v2beta1/search-domains",
            params={
                "domains": domains,
                "strict_search": strict_search,
                "tlds": tlds,
            },
        )

        self._throw_on_error(res)
        return unmarshal_SearchAvailableDomainsResponse(res.json())

    def list_tlds(
        self,
        *,
        tlds: Optional[List[str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTldsRequestOrderBy] = None,
    ) -> ListTldsResponse:
        """
        List TLD offers.
        Retrieve the list of TLDs and offers associated with them.
        :param tlds: Array of TLDs to return.
        :param page: Page number for the returned Projects.
        :param page_size: Maximum number of Project per page.
        :param order_by: Sort order of the returned TLDs.
        :return: :class:`ListTldsResponse <ListTldsResponse>`

        Usage:
        ::

            result = api.list_tlds()
        """

        res = self._request(
            "GET",
            "/domain/v2beta1/tlds",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "tlds": tlds,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTldsResponse(res.json())

    def list_tlds_all(
        self,
        *,
        tlds: Optional[List[str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTldsRequestOrderBy] = None,
    ) -> List[Tld]:
        """
        List TLD offers.
        Retrieve the list of TLDs and offers associated with them.
        :param tlds: Array of TLDs to return.
        :param page: Page number for the returned Projects.
        :param page_size: Maximum number of Project per page.
        :param order_by: Sort order of the returned TLDs.
        :return: :class:`List[Tld] <List[Tld]>`

        Usage:
        ::

            result = api.list_tlds_all()
        """

        return fetch_all_pages(
            type=ListTldsResponse,
            key="tlds",
            fetcher=self.list_tlds,
            args={
                "tlds": tlds,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    def create_domain_host(
        self,
        *,
        domain: str,
        name: str,
        ips: Optional[List[str]] = None,
    ) -> Host:
        """
        Create a hostname for a domain.
        Create a hostname for a domain with glue IPs.
        :param domain:
        :param name:
        :param ips:
        :return: :class:`Host <Host>`

        Usage:
        ::

            result = api.create_domain_host(
                domain="example",
                name="example",
            )
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "POST",
            f"/domain/v2beta1/domains/{param_domain}/hosts",
            body=marshal_RegistrarApiCreateDomainHostRequest(
                RegistrarApiCreateDomainHostRequest(
                    domain=domain,
                    name=name,
                    ips=ips,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Host(res.json())

    def list_domain_hosts(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        domain: str,
    ) -> ListDomainHostsResponse:
        """
        List a domain's hostnames.
        List a domain's hostnames using their glue IPs.
        :param page:
        :param page_size:
        :param domain:
        :return: :class:`ListDomainHostsResponse <ListDomainHostsResponse>`

        Usage:
        ::

            result = api.list_domain_hosts(
                domain="example",
            )
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "GET",
            f"/domain/v2beta1/domains/{param_domain}/hosts",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDomainHostsResponse(res.json())

    def list_domain_hosts_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        domain: str,
    ) -> List[Host]:
        """
        List a domain's hostnames.
        List a domain's hostnames using their glue IPs.
        :param page:
        :param page_size:
        :param domain:
        :return: :class:`List[Host] <List[Host]>`

        Usage:
        ::

            result = api.list_domain_hosts_all(
                domain="example",
            )
        """

        return fetch_all_pages(
            type=ListDomainHostsResponse,
            key="hosts",
            fetcher=self.list_domain_hosts,
            args={
                "page": page,
                "page_size": page_size,
                "domain": domain,
            },
        )

    def update_domain_host(
        self,
        *,
        domain: str,
        name: str,
        ips: Optional[List[str]] = None,
    ) -> Host:
        """
        Update a domain's hostname.
        Update a domain's hostname with glue IPs.
        :param domain:
        :param name:
        :param ips:
        :return: :class:`Host <Host>`

        Usage:
        ::

            result = api.update_domain_host(
                domain="example",
                name="example",
            )
        """

        param_domain = validate_path_param("domain", domain)
        param_name = validate_path_param("name", name)

        res = self._request(
            "PATCH",
            f"/domain/v2beta1/domains/{param_domain}/hosts/{param_name}",
            body=marshal_RegistrarApiUpdateDomainHostRequest(
                RegistrarApiUpdateDomainHostRequest(
                    domain=domain,
                    name=name,
                    ips=ips,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Host(res.json())

    def delete_domain_host(
        self,
        *,
        domain: str,
        name: str,
    ) -> Host:
        """
        Delete a domain's hostname.
        :param domain:
        :param name:
        :return: :class:`Host <Host>`

        Usage:
        ::

            result = api.delete_domain_host(
                domain="example",
                name="example",
            )
        """

        param_domain = validate_path_param("domain", domain)
        param_name = validate_path_param("name", name)

        res = self._request(
            "DELETE",
            f"/domain/v2beta1/domains/{param_domain}/hosts/{param_name}",
        )

        self._throw_on_error(res)
        return unmarshal_Host(res.json())
