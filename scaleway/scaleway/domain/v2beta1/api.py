# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    ScwFile,
    unmarshal_ScwFile,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages,
    validate_path_param,
    wait_for_resource,
)
from .types import (
    DomainRecordType,
    DomainStatus,
    LanguageCode,
    ListDNSZoneRecordsRequestOrderBy,
    ListDNSZonesRequestOrderBy,
    ListDomainsRequestOrderBy,
    ListRenewableDomainsRequestOrderBy,
    ListTasksRequestOrderBy,
    RawFormat,
    TaskStatus,
    TaskType,
    CheckContactsCompatibilityResponse,
    ClearDNSZoneRecordsResponse,
    Contact,
    ContactExtensionEU,
    ContactExtensionFR,
    ContactExtensionNL,
    ContactRoles,
    DNSZone,
    DNSZoneVersion,
    DSRecord,
    DeleteDNSZoneResponse,
    DeleteExternalDomainResponse,
    DeleteSSLCertificateResponse,
    Domain,
    DomainRecord,
    DomainSummary,
    GetDNSZoneTsigKeyResponse,
    GetDNSZoneVersionDiffResponse,
    GetDomainAuthCodeResponse,
    Host,
    ImportProviderDNSZoneRequestOnlineV1,
    ImportProviderDNSZoneResponse,
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
    Nameserver,
    NewContact,
    OrderResponse,
    RecordChange,
    RefreshDNSZoneResponse,
    RegisterExternalDomainResponse,
    RenewableDomain,
    RestoreDNSZoneVersionResponse,
    SSLCertificate,
    SearchAvailableDomainsResponse,
    Task,
    TransferInDomainRequestTransferRequest,
    UpdateContactRequestQuestion,
    UpdateDNSZoneNameserversResponse,
    UpdateDNSZoneRecordsResponse,
    CreateDNSZoneRequest,
    UpdateDNSZoneRequest,
    CloneDNSZoneRequest,
    UpdateDNSZoneRecordsRequest,
    UpdateDNSZoneNameserversRequest,
    ImportRawDNSZoneRequest,
    ImportProviderDNSZoneRequest,
    RefreshDNSZoneRequest,
    CreateSSLCertificateRequest,
    RegistrarApiBuyDomainsRequest,
    RegistrarApiRenewDomainsRequest,
    RegistrarApiTransferInDomainRequest,
    RegistrarApiTradeDomainRequest,
    RegistrarApiRegisterExternalDomainRequest,
    RegistrarApiCheckContactsCompatibilityRequest,
    RegistrarApiUpdateContactRequest,
    RegistrarApiUpdateDomainRequest,
    RegistrarApiEnableDomainDNSSECRequest,
    RegistrarApiCreateDomainHostRequest,
    RegistrarApiUpdateDomainHostRequest,
)
from .content import (
    DOMAIN_TRANSIENT_STATUSES,
    SSL_CERTIFICATE_TRANSIENT_STATUSES,
)
from .marshalling import (
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
    unmarshal_OrderResponse,
    unmarshal_RefreshDNSZoneResponse,
    unmarshal_RegisterExternalDomainResponse,
    unmarshal_RestoreDNSZoneVersionResponse,
    unmarshal_SearchAvailableDomainsResponse,
    unmarshal_UpdateDNSZoneNameserversResponse,
    unmarshal_UpdateDNSZoneRecordsResponse,
)


class DomainV2Beta1API(API):
    """
    DNS API.

    DNS API.
    Manage your DNS zones and records.
    """

    def list_dns_zones(
        self,
        *,
        domain: str,
        dns_zone: str,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        order_by: ListDNSZonesRequestOrderBy = ListDNSZonesRequestOrderBy.DOMAIN_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListDNSZonesResponse:
        """
        List DNS zones.
        Returns a list of manageable DNS zones.
        You can filter the DNS zones by domain name.
        :param organization_id: The organization ID on which to filter the returned DNS zones.
        :param project_id: The project ID on which to filter the returned DNS zones.
        :param order_by: The sort order of the returned DNS zones.
        :param page: The page number for the returned DNS zones.
        :param page_size: The maximum number of DNS zones per page.
        :param domain: The domain on which to filter the returned DNS zones.
        :param dns_zone: The DNS zone on which to filter the returned DNS zones.
        :return: :class:`ListDNSZonesResponse <ListDNSZonesResponse>`

        Usage:
        ::

            result = api.list_dns_zones(
                domain="example",
                dns_zone="example",
            )
        """

        res = self._request(
            "GET",
            f"/domain/v2beta1/dns-zones",
            params={
                "dns_zone": dns_zone,
                "domain": domain,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDNSZonesResponse(res.json())

    def list_dns_zones_all(
        self,
        *,
        domain: str,
        dns_zone: str,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        order_by: Optional[ListDNSZonesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DNSZone]:
        """
        List DNS zones.
        Returns a list of manageable DNS zones.
        You can filter the DNS zones by domain name.
        :param organization_id: The organization ID on which to filter the returned DNS zones.
        :param project_id: The project ID on which to filter the returned DNS zones.
        :param order_by: The sort order of the returned DNS zones.
        :param page: The page number for the returned DNS zones.
        :param page_size: The maximum number of DNS zones per page.
        :param domain: The domain on which to filter the returned DNS zones.
        :param dns_zone: The DNS zone on which to filter the returned DNS zones.
        :return: :class:`List[ListDNSZonesResponse] <List[ListDNSZonesResponse]>`

        Usage:
        ::

            result = api.list_dns_zones_all(
                domain="example",
                dns_zone="example",
            )
        """

        return fetch_all_pages(
            type=ListDNSZonesResponse,
            key="dns_zones",
            fetcher=self.list_dns_zones,
            args={
                "domain": domain,
                "dns_zone": dns_zone,
                "organization_id": organization_id,
                "project_id": project_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
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
        Create a new DNS zone.
        :param domain: The domain of the DNS zone to create.
        :param subdomain: The subdomain of the DNS zone to create.
        :param project_id: The project ID where the DNS zone will be created.
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
            f"/domain/v2beta1/dns-zones",
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
        new_dns_zone: str,
        project_id: Optional[str] = None,
    ) -> DNSZone:
        """
        Update a DNS zone.
        Update the name and/or the organizations for a DNS zone.
        :param dns_zone: The DNS zone to update.
        :param new_dns_zone: The new DNS zone.
        :param project_id: The project ID of the new DNS zone.
        :return: :class:`DNSZone <DNSZone>`

        Usage:
        ::

            result = api.update_dns_zone(
                dns_zone="example",
                new_dns_zone="example",
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
        Clone an existed DNS zone with all its records into a new one.
        :param dns_zone: The DNS zone to clone.
        :param dest_dns_zone: The destinaton DNS zone.
        :param overwrite: Whether or not the destination DNS zone will be overwritten.
        :param project_id: The project ID of the destination DNS zone.
        :return: :class:`DNSZone <DNSZone>`

        Usage:
        ::

            result = api.clone_dns_zone(
                dns_zone="example",
                dest_dns_zone="example",
                overwrite=True,
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
        Delete DNS zone.
        Delete a DNS zone and all it's records.
        :param dns_zone: The DNS zone to delete.
        :param project_id: The project ID of the DNS zone to delete.
        :return: :class:`DeleteDNSZoneResponse <DeleteDNSZoneResponse>`

        Usage:
        ::

            result = api.delete_dns_zone(dns_zone="example")
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
        dns_zone: str,
        name: str,
        project_id: Optional[str] = None,
        order_by: ListDNSZoneRecordsRequestOrderBy = ListDNSZoneRecordsRequestOrderBy.NAME_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        type_: DomainRecordType = DomainRecordType.UNKNOWN,
        id: Optional[str] = None,
    ) -> ListDNSZoneRecordsResponse:
        """
        List DNS zone records.
        Returns a list of DNS records of a DNS zone with default NS.
        You can filter the records by type and name.
        :param dns_zone: The DNS zone on which to filter the returned DNS zone records.
        :param project_id: The project ID on which to filter the returned DNS zone records.
        :param order_by: The sort order of the returned DNS zone records.
        :param page: The page number for the returned DNS zone records.
        :param page_size: The maximum number of DNS zone records per page.
        :param name: The name on which to filter the returned DNS zone records.
        :param type_: The record type on which to filter the returned DNS zone records.
        :param id: The record ID on which to filter the returned DNS zone records.
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
        dns_zone: str,
        name: str,
        project_id: Optional[str] = None,
        order_by: Optional[ListDNSZoneRecordsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        type_: Optional[DomainRecordType] = None,
        id: Optional[str] = None,
    ) -> List[DomainRecord]:
        """
        List DNS zone records.
        Returns a list of DNS records of a DNS zone with default NS.
        You can filter the records by type and name.
        :param dns_zone: The DNS zone on which to filter the returned DNS zone records.
        :param project_id: The project ID on which to filter the returned DNS zone records.
        :param order_by: The sort order of the returned DNS zone records.
        :param page: The page number for the returned DNS zone records.
        :param page_size: The maximum number of DNS zone records per page.
        :param name: The name on which to filter the returned DNS zone records.
        :param type_: The record type on which to filter the returned DNS zone records.
        :param id: The record ID on which to filter the returned DNS zone records.
        :return: :class:`List[ListDNSZoneRecordsResponse] <List[ListDNSZoneRecordsResponse]>`

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
                "dns_zone": dns_zone,
                "name": name,
                "project_id": project_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
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
        Update DNS zone records.
        Only available with default NS.<br/>
        Send a list of actions and records.

        Action can be:
         - add:
          - Add new record
          - Can be more specific and add a new IP to an existing A record for example
         - set:
          - Edit a record
          - Can be more specific and edit an IP from an existing A record for example
         - delete:
          - Delete a record
          - Can be more specific and delete an IP from an existing A record for example
         - clear:
          - Delete all records from a DNS zone

        All edits will be versioned.
        :param dns_zone: The DNS zone where the DNS zone records will be updated.
        :param changes: The changes made to the records.
        :param return_all_records: Whether or not to return all the records.
        :param disallow_new_zone_creation: Forbid the creation of the target zone if not existing (default action is yes).
        :param serial: Don't use the autoincremenent serial but the provided one (0 to keep the same).
        :return: :class:`UpdateDNSZoneRecordsResponse <UpdateDNSZoneRecordsResponse>`

        Usage:
        ::

            result = api.update_dns_zone_records(
                dns_zone="example",
                changes=[RecordChange(...)],
                disallow_new_zone_creation=True,
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
        dns_zone: str,
        project_id: Optional[str] = None,
    ) -> ListDNSZoneNameserversResponse:
        """
        List DNS zone nameservers.
        Returns a list of Nameservers and their optional glue records for a DNS zone.
        :param dns_zone: The DNS zone on which to filter the returned DNS zone nameservers.
        :param project_id: The project ID on which to filter the returned DNS zone nameservers.
        :return: :class:`ListDNSZoneNameserversResponse <ListDNSZoneNameserversResponse>`

        Usage:
        ::

            result = api.list_dns_zone_nameservers(dns_zone="example")
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
        Update DNS zone nameservers.
        Update DNS zone nameservers and set optional glue records.
        :param dns_zone: The DNS zone where the DNS zone nameservers will be updated.
        :param ns: The new DNS zone nameservers.
        :return: :class:`UpdateDNSZoneNameserversResponse <UpdateDNSZoneNameserversResponse>`

        Usage:
        ::

            result = api.update_dns_zone_nameservers(
                dns_zone="example",
                ns=[Nameserver(...)],
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
        Clear DNS zone records.
        Only available with default NS.<br/>
        Delete all the records from a DNS zone.
        All edits will be versioned.
        :param dns_zone: The DNS zone to clear.
        :return: :class:`ClearDNSZoneRecordsResponse <ClearDNSZoneRecordsResponse>`

        Usage:
        ::

            result = api.clear_dns_zone_records(dns_zone="example")
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
        format: RawFormat,
    ) -> Optional[ScwFile]:
        """
        Export raw DNS zone.
        Get a DNS zone in a given format with default NS.
        :param dns_zone: The DNS zone to export.
        :param format: Format for DNS zone.
        :return: :class:`Optional[ScwFile] <Optional[ScwFile]>`

        Usage:
        ::

            result = api.export_raw_dns_zone(
                dns_zone="example",
                format=unknown_raw_format,
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
        json = res.json()
        return unmarshal_ScwFile(json) if json is not None else None

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
        Import raw DNS zone.
        Import and replace records from a given provider format with default NS.
        :param dns_zone: The DNS zone to import.
        :param content:
        :param project_id:
        :param format:
        :param bind_source: Import a bind file format.

        One-of ('source'): at most one of 'bind_source', 'axfr_source' could be set.
        :param axfr_source: Import from the nameserver given with tsig use or not.

        One-of ('source'): at most one of 'bind_source', 'axfr_source' could be set.
        :return: :class:`ImportRawDNSZoneResponse <ImportRawDNSZoneResponse>`

        Usage:
        ::

            result = api.import_raw_dns_zone(dns_zone="example")
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
        Import provider DNS zone.
        Import and replace records from a given provider format with default NS.
        :param dns_zone:
        :param online_v1: One-of ('provider'): at most one of 'online_v1' could be set.
        :return: :class:`ImportProviderDNSZoneResponse <ImportProviderDNSZoneResponse>`

        Usage:
        ::

            result = api.import_provider_dns_zone(dns_zone="example")
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
        Refresh DNS zone.
        Refresh SOA DNS zone.
        You can recreate the given DNS zone and its sub DNS zone if needed.
        :param dns_zone: The DNS zone to refresh.
        :param recreate_dns_zone: Whether or not to recreate the DNS zone.
        :param recreate_sub_dns_zone: Whether or not to recreate the sub DNS zone.
        :return: :class:`RefreshDNSZoneResponse <RefreshDNSZoneResponse>`

        Usage:
        ::

            result = api.refresh_dns_zone(
                dns_zone="example",
                recreate_dns_zone=True,
                recreate_sub_dns_zone=True,
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
        dns_zone: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListDNSZoneVersionsResponse:
        """
        List DNS zone versions.
        Get a list of DNS zone versions.<br/>
        The maximum version count is 100.<br/>
        If the count reaches this limit, the oldest version will be deleted after each new modification.
        :param dns_zone:
        :param page: The page number for the returned DNS zones versions.
        :param page_size: The maximum number of DNS zones versions per page.
        :return: :class:`ListDNSZoneVersionsResponse <ListDNSZoneVersionsResponse>`

        Usage:
        ::

            result = api.list_dns_zone_versions(dns_zone="example")
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
        dns_zone: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DNSZoneVersion]:
        """
        List DNS zone versions.
        Get a list of DNS zone versions.<br/>
        The maximum version count is 100.<br/>
        If the count reaches this limit, the oldest version will be deleted after each new modification.
        :param dns_zone:
        :param page: The page number for the returned DNS zones versions.
        :param page_size: The maximum number of DNS zones versions per page.
        :return: :class:`List[ListDNSZoneVersionsResponse] <List[ListDNSZoneVersionsResponse]>`

        Usage:
        ::

            result = api.list_dns_zone_versions_all(dns_zone="example")
        """

        return fetch_all_pages(
            type=ListDNSZoneVersionsResponse,
            key="versions",
            fetcher=self.list_dns_zone_versions,
            args={
                "dns_zone": dns_zone,
                "page": page,
                "page_size": page_size,
            },
        )

    def list_dns_zone_version_records(
        self,
        *,
        dns_zone_version_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListDNSZoneVersionRecordsResponse:
        """
        List DNS zone version records.
        Get a list of records from a previous DNS zone version.
        :param dns_zone_version_id:
        :param page: The page number for the returned DNS zones versions records.
        :param page_size: The maximum number of DNS zones versions records per page.
        :return: :class:`ListDNSZoneVersionRecordsResponse <ListDNSZoneVersionRecordsResponse>`

        Usage:
        ::

            result = api.list_dns_zone_version_records(dns_zone_version_id="example")
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
        dns_zone_version_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DomainRecord]:
        """
        List DNS zone version records.
        Get a list of records from a previous DNS zone version.
        :param dns_zone_version_id:
        :param page: The page number for the returned DNS zones versions records.
        :param page_size: The maximum number of DNS zones versions records per page.
        :return: :class:`List[ListDNSZoneVersionRecordsResponse] <List[ListDNSZoneVersionRecordsResponse]>`

        Usage:
        ::

            result = api.list_dns_zone_version_records_all(dns_zone_version_id="example")
        """

        return fetch_all_pages(
            type=ListDNSZoneVersionRecordsResponse,
            key="records",
            fetcher=self.list_dns_zone_version_records,
            args={
                "dns_zone_version_id": dns_zone_version_id,
                "page": page,
                "page_size": page_size,
            },
        )

    def get_dns_zone_version_diff(
        self,
        *,
        dns_zone_version_id: str,
    ) -> GetDNSZoneVersionDiffResponse:
        """
        Get DNS zone version diff.
        Get all differences from a previous DNS zone version.
        :param dns_zone_version_id:
        :return: :class:`GetDNSZoneVersionDiffResponse <GetDNSZoneVersionDiffResponse>`

        Usage:
        ::

            result = api.get_dns_zone_version_diff(dns_zone_version_id="example")
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
        Restore DNS zone version.
        Restore and activate a previous DNS zone version.
        :param dns_zone_version_id:
        :return: :class:`RestoreDNSZoneVersionResponse <RestoreDNSZoneVersionResponse>`

        Usage:
        ::

            result = api.restore_dns_zone_version(dns_zone_version_id="example")
        """

        param_dns_zone_version_id = validate_path_param(
            "dns_zone_version_id", dns_zone_version_id
        )

        res = self._request(
            "POST",
            f"/domain/v2beta1/dns-zones/version/{param_dns_zone_version_id}/restore",
        )

        self._throw_on_error(res)
        return unmarshal_RestoreDNSZoneVersionResponse(res.json())

    def get_ssl_certificate(
        self,
        *,
        dns_zone: str,
    ) -> SSLCertificate:
        """
        Get the zone TLS certificate if it exists.
        :param dns_zone:
        :return: :class:`SSLCertificate <SSLCertificate>`

        Usage:
        ::

            result = api.get_ssl_certificate(dns_zone="example")
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
        Waits for :class:`SSLCertificate <SSLCertificate>` to be in a final state.
        :param dns_zone:
        :param options: The options for the waiter
        :return: :class:`SSLCertificate <SSLCertificate>`

        Usage:
        ::

            result = api.wait_for_ssl_certificate(dns_zone="example")
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
        Create or return the zone TLS certificate.
        :param dns_zone:
        :param alternative_dns_zones:
        :return: :class:`SSLCertificate <SSLCertificate>`

        Usage:
        ::

            result = api.create_ssl_certificate(dns_zone="example")
        """

        res = self._request(
            "POST",
            f"/domain/v2beta1/ssl-certificates",
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
        List all user TLS certificates.
        :param dns_zone:
        :param page:
        :param page_size:
        :param project_id:
        :return: :class:`ListSSLCertificatesResponse <ListSSLCertificatesResponse>`

        Usage:
        ::

            result = api.list_ssl_certificates(dns_zone="example")
        """

        res = self._request(
            "GET",
            f"/domain/v2beta1/ssl-certificates",
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
        List all user TLS certificates.
        :param dns_zone:
        :param page:
        :param page_size:
        :param project_id:
        :return: :class:`List[ListSSLCertificatesResponse] <List[ListSSLCertificatesResponse]>`

        Usage:
        ::

            result = api.list_ssl_certificates_all(dns_zone="example")
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
        Delete an TLS certificate.
        :param dns_zone:
        :return: :class:`DeleteSSLCertificateResponse <DeleteSSLCertificateResponse>`

        Usage:
        ::

            result = api.delete_ssl_certificate(dns_zone="example")
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
        Get the DNS zone TSIG Key.
        Get the DNS zone TSIG Key to allow AXFR request.
        :param dns_zone:
        :return: :class:`GetDNSZoneTsigKeyResponse <GetDNSZoneTsigKeyResponse>`

        Usage:
        ::

            result = api.get_dns_zone_tsig_key(dns_zone="example")
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
    ) -> Optional[None]:
        """
        Delete the DNS zone TSIG Key.
        :param dns_zone:

        Usage:
        ::

            result = api.delete_dns_zone_tsig_key(dns_zone="example")
        """

        param_dns_zone = validate_path_param("dns_zone", dns_zone)

        res = self._request(
            "DELETE",
            f"/domain/v2beta1/dns-zones/{param_dns_zone}/tsig-key",
        )

        self._throw_on_error(res)
        return None


class DomainRegistrarV2Beta1API(API):
    """
    Domains registrar API.

    Domains registrar API.
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
        order_by: ListTasksRequestOrderBy = ListTasksRequestOrderBy.DOMAIN_DESC,
    ) -> ListTasksResponse:
        """
        List tasks.
        List all account tasks.
        You can filter the list by domain name.
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
            f"/domain/v2beta1/tasks",
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
        List all account tasks.
        You can filter the list by domain name.
        :param page:
        :param page_size:
        :param project_id:
        :param organization_id:
        :param domain:
        :param types:
        :param statuses:
        :param order_by:
        :return: :class:`List[ListTasksResponse] <List[ListTasksResponse]>`

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
        Buy one or more domains.
        Request the registration of domain names.
        You can provide an already existing domain's contact or a new contact.
        :param domains:
        :param duration_in_years:
        :param project_id:
        :param owner_contact_id: One-of ('owner_contact_type'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param owner_contact: One-of ('owner_contact_type'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param administrative_contact_id: One-of ('administrative_contact_type'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :param administrative_contact: One-of ('administrative_contact_type'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :param technical_contact_id: One-of ('technical_contact_type'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :param technical_contact: One-of ('technical_contact_type'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :return: :class:`OrderResponse <OrderResponse>`

        Usage:
        ::

            result = api.buy_domains(
                domains=["example"],
                duration_in_years=1,
            )
        """

        res = self._request(
            "POST",
            f"/domain/v2beta1/buy-domains",
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
        Renew one or more domains.
        Request the renewal of domain names.
        :param domains:
        :param duration_in_years:
        :param force_late_renewal:
        :return: :class:`OrderResponse <OrderResponse>`

        Usage:
        ::

            result = api.renew_domains(
                domains=["example"],
                duration_in_years=1,
            )
        """

        res = self._request(
            "POST",
            f"/domain/v2beta1/renew-domains",
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
        Request the transfer from another registrar domain to Scaleway.
        :param domains:
        :param project_id:
        :param owner_contact_id: One-of ('owner_contact_type'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param owner_contact: One-of ('owner_contact_type'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param administrative_contact_id: One-of ('administrative_contact_type'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :param administrative_contact: One-of ('administrative_contact_type'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :param technical_contact_id: One-of ('technical_contact_type'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :param technical_contact: One-of ('technical_contact_type'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :return: :class:`OrderResponse <OrderResponse>`

        Usage:
        ::

            result = api.transfer_in_domain(domains=[TransferInDomainRequestTransferRequest(...)])
        """

        res = self._request(
            "POST",
            f"/domain/v2beta1/domains/transfer-domains",
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
        Trade a domain contact.
        Request a trade for the contact owner.<br/>
        If an `organization_id` is given, the change is from the current Scaleway account to another Scaleway account.<br/>
        If no contact is given, the first contact of the other Scaleway account is taken.<br/>
        If the other Scaleway account has no contact. An error occurs.
        :param domain:
        :param project_id:
        :param new_owner_contact_id: One-of ('new_owner_contact_type'): at most one of 'new_owner_contact_id', 'new_owner_contact' could be set.
        :param new_owner_contact: One-of ('new_owner_contact_type'): at most one of 'new_owner_contact_id', 'new_owner_contact' could be set.
        :return: :class:`OrderResponse <OrderResponse>`

        Usage:
        ::

            result = api.trade_domain(domain="example")
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

            result = api.register_external_domain(domain="example")
        """

        res = self._request(
            "POST",
            f"/domain/v2beta1/external-domains",
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

            result = api.delete_external_domain(domain="example")
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
        Check if contacts are compatible against a domain or a tld.
        Check if contacts are compatible against a domain or a tld.
        If not, it will return the information requiring a correction.
        :param domains:
        :param tlds:
        :param owner_contact_id: One-of ('owner_contact_type'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param owner_contact: One-of ('owner_contact_type'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param administrative_contact_id: One-of ('administrative_contact_type'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :param administrative_contact: One-of ('administrative_contact_type'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :param technical_contact_id: One-of ('technical_contact_type'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :param technical_contact: One-of ('technical_contact_type'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :return: :class:`CheckContactsCompatibilityResponse <CheckContactsCompatibilityResponse>`

        Usage:
        ::

            result = api.check_contacts_compatibility()
        """

        res = self._request(
            "POST",
            f"/domain/v2beta1/check-contacts-compatibility",
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
    ) -> ListContactsResponse:
        """
        List contacts.
        Return a list of contacts with their domains and roles.
        You can filter the list by domain name.
        :param page:
        :param page_size:
        :param domain:
        :param project_id:
        :param organization_id:
        :return: :class:`ListContactsResponse <ListContactsResponse>`

        Usage:
        ::

            result = api.list_contacts()
        """

        res = self._request(
            "GET",
            f"/domain/v2beta1/contacts",
            params={
                "domain": domain,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
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
    ) -> List[ContactRoles]:
        """
        List contacts.
        Return a list of contacts with their domains and roles.
        You can filter the list by domain name.
        :param page:
        :param page_size:
        :param domain:
        :param project_id:
        :param organization_id:
        :return: :class:`List[ListContactsResponse] <List[ListContactsResponse]>`

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
            },
        )

    def get_contact(
        self,
        *,
        contact_id: str,
    ) -> Contact:
        """
        Get a contact.
        Return a contact details retrieved from the registrar using a given contact ID.
        :param contact_id:
        :return: :class:`Contact <Contact>`

        Usage:
        ::

            result = api.get_contact(contact_id="example")
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
        lang: LanguageCode,
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
        You can edit the contact coordinates.
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
                lang=unknown_language_code,
            )
        """

        param_contact_id = validate_path_param("contact_id", contact_id)

        res = self._request(
            "PATCH",
            f"/domain/v2beta1/contacts/{param_contact_id}",
            body=marshal_RegistrarApiUpdateContactRequest(
                RegistrarApiUpdateContactRequest(
                    contact_id=contact_id,
                    lang=lang,
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
        order_by: ListDomainsRequestOrderBy = ListDomainsRequestOrderBy.DOMAIN_ASC,
        registrar: Optional[str] = None,
        status: DomainStatus = DomainStatus.STATUS_UNKNOWN,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        is_external: Optional[bool] = None,
        domain: Optional[str] = None,
    ) -> ListDomainsResponse:
        """
        List domains.
        Returns a list of domains owned by the user.
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
            f"/domain/v2beta1/domains",
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
        Returns a list of domains owned by the user.
        :param page:
        :param page_size:
        :param order_by:
        :param registrar:
        :param status:
        :param project_id:
        :param organization_id:
        :param is_external:
        :param domain:
        :return: :class:`List[ListDomainsResponse] <List[ListDomainsResponse]>`

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
        order_by: ListRenewableDomainsRequestOrderBy = ListRenewableDomainsRequestOrderBy.DOMAIN_ASC,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
    ) -> ListRenewableDomainsResponse:
        """
        List scaleway domains that can or not be renewed.
        Returns a list of domains owned by the user with a renew status and if renewable, the maximum renew duration in years.
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
            f"/domain/v2beta1/renewable-domains",
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
        List scaleway domains that can or not be renewed.
        Returns a list of domains owned by the user with a renew status and if renewable, the maximum renew duration in years.
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :param organization_id:
        :return: :class:`List[ListRenewableDomainsResponse] <List[ListRenewableDomainsResponse]>`

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
        Returns a the domain with more informations.
        :param domain:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.get_domain(domain="example")
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
        Waits for :class:`Domain <Domain>` to be in a final state.
        :param domain:
        :param options: The options for the waiter
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.wait_for_domain(domain="example")
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
        Update a domain.
        Update the domain contacts or create a new one.<br/>
        If you add the same contact for multiple roles. Only one ID will be created and used for all of them.
        :param domain:
        :param technical_contact_id: One-of ('technical_contact_info'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :param technical_contact: One-of ('technical_contact_info'): at most one of 'technical_contact_id', 'technical_contact' could be set.
        :param owner_contact_id: One-of ('owner_contact_info'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param owner_contact: One-of ('owner_contact_info'): at most one of 'owner_contact_id', 'owner_contact' could be set.
        :param administrative_contact_id: One-of ('administrative_contact_info'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :param administrative_contact: One-of ('administrative_contact_info'): at most one of 'administrative_contact_id', 'administrative_contact' could be set.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.update_domain(domain="example")
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
        Lock domain transfer.
        Lock domain transfer. A locked domain transfer can't be transferred and the auth code can't be requested.
        :param domain:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.lock_domain_transfer(domain="example")
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "POST",
            f"/domain/v2beta1/domains/{param_domain}/lock-transfer",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def unlock_domain_transfer(
        self,
        *,
        domain: str,
    ) -> Domain:
        """
        Unlock domain transfer.
        Unlock domain transfer. An unlocked domain can be transferred and the auth code can be requested for this.
        :param domain:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.unlock_domain_transfer(domain="example")
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "POST",
            f"/domain/v2beta1/domains/{param_domain}/unlock-transfer",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def enable_domain_auto_renew(
        self,
        *,
        domain: str,
    ) -> Domain:
        """
        Enable domain auto renew.
        :param domain:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.enable_domain_auto_renew(domain="example")
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "POST",
            f"/domain/v2beta1/domains/{param_domain}/enable-auto-renew",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def disable_domain_auto_renew(
        self,
        *,
        domain: str,
    ) -> Domain:
        """
        Disable domain auto renew.
        :param domain:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.disable_domain_auto_renew(domain="example")
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "POST",
            f"/domain/v2beta1/domains/{param_domain}/disable-auto-renew",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def get_domain_auth_code(
        self,
        *,
        domain: str,
    ) -> GetDomainAuthCodeResponse:
        """
        Return domain auth code.
        If possible, return the auth code for an unlocked domain transfer, or an error if the domain is locked.
        Some TLD may have a different procedure to retrieve the auth code, in that case, the information is given in the message field.
        :param domain:
        :return: :class:`GetDomainAuthCodeResponse <GetDomainAuthCodeResponse>`

        Usage:
        ::

            result = api.get_domain_auth_code(domain="example")
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
        If your domain has the default Scaleway NS and uses another registrar, you have to update the DS record manually.
        For the algorithm, here are the code numbers for each type:
          - 1: RSAMD5
          - 2: DIFFIE_HELLMAN
          - 3: DSA_SHA1
          - 5: RSA_SHA1
          - 6: DSA_NSEC3_SHA1
          - 7: RSASHA1_NSEC3_SHA1
          - 8: RSASHA256
          - 10: RSASHA512
          - 12: ECC_GOST
          - 13: ECDSAP256SHA256
          - 14: ECDSAP384SHA384

        And for the digest type:
          - 1: SHA_1
          - 2: SHA_256
          - 3: GOST_R_34_11_94
          - 4: SHA_384
        :param domain:
        :param ds_record:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.enable_domain_dnssec(domain="example")
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
        Disable domain DNSSEC.
        :param domain:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.disable_domain_dnssec(domain="example")
        """

        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "POST",
            f"/domain/v2beta1/domains/{param_domain}/disable-dnssec",
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
        Search a domain (or at maximum, 10 domains).

        If the TLD list is empty or not set the search returns the results from the most popular TLDs.
        :param domains: A list of domain to search, TLD is optional.
        :param tlds: Array of tlds to search on.
        :param strict_search: Search exact match.
        :return: :class:`SearchAvailableDomainsResponse <SearchAvailableDomainsResponse>`

        Usage:
        ::

            result = api.search_available_domains(
                domains=["example"],
                strict_search=True,
            )
        """

        res = self._request(
            "GET",
            f"/domain/v2beta1/search-domains",
            params={
                "domains": domains,
                "strict_search": strict_search,
                "tlds": tlds,
            },
        )

        self._throw_on_error(res)
        return unmarshal_SearchAvailableDomainsResponse(res.json())

    def create_domain_host(
        self,
        *,
        domain: str,
        name: str,
        ips: Optional[List[str]] = None,
    ) -> Host:
        """
        Create domain hostname with glue IPs.
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
        domain: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListDomainHostsResponse:
        """
        List domain hostnames with they glue IPs.
        :param domain:
        :param page:
        :param page_size:
        :return: :class:`ListDomainHostsResponse <ListDomainHostsResponse>`

        Usage:
        ::

            result = api.list_domain_hosts(domain="example")
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
        domain: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Host]:
        """
        List domain hostnames with they glue IPs.
        :param domain:
        :param page:
        :param page_size:
        :return: :class:`List[ListDomainHostsResponse] <List[ListDomainHostsResponse]>`

        Usage:
        ::

            result = api.list_domain_hosts_all(domain="example")
        """

        return fetch_all_pages(
            type=ListDomainHostsResponse,
            key="hosts",
            fetcher=self.list_domain_hosts,
            args={
                "domain": domain,
                "page": page,
                "page_size": page_size,
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
        Update domain hostname with glue IPs.
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
        Delete domain hostname.
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
