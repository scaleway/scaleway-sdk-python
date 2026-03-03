# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    StrEnumMeta,
)

from ...std.types import (
    CountryCode as StdCountryCode,
)


class AlertRuleStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ENABLED = "enabled"
    DISABLED = "disabled"
    ENABLING = "enabling"
    DISABLING = "disabling"

    def __str__(self) -> str:
        return str(self.value)


class AuthenticationEventFailureReason(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_FAILURE_REASON = "unknown_failure_reason"
    INVALID_MFA = "invalid_mfa"
    INVALID_PASSWORD = "invalid_password"

    def __str__(self) -> str:
        return str(self.value)


class AuthenticationEventMFAType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_MFA_TYPE = "unknown_mfa_type"
    TOTP = "totp"

    def __str__(self) -> str:
        return str(self.value)


class AuthenticationEventMethod(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_METHOD = "unknown_method"
    PASSWORD = "password"
    AUTHENTICATION_CODE = "authentication_code"
    OAUTH2 = "oauth2"
    SAML = "saml"

    def __str__(self) -> str:
        return str(self.value)


class AuthenticationEventOrigin(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ORIGIN = "unknown_origin"
    PUBLIC_API = "public_api"
    ADMIN_API = "admin_api"

    def __str__(self) -> str:
        return str(self.value)


class AuthenticationEventResult(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_RESULT = "unknown_result"
    SUCCESS = "success"
    FAILURE = "failure"

    def __str__(self) -> str:
        return str(self.value)


class ExportJobStatusCode(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_CODE = "unknown_code"
    SUCCESS = "success"
    FAILURE = "failure"

    def __str__(self) -> str:
        return str(self.value)


class ListAuthenticationEventsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    RECORDED_AT_DESC = "recorded_at_desc"
    RECORDED_AT_ASC = "recorded_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListCombinedEventsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    RECORDED_AT_DESC = "recorded_at_desc"
    RECORDED_AT_ASC = "recorded_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListEventsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    RECORDED_AT_DESC = "recorded_at_desc"
    RECORDED_AT_ASC = "recorded_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListExportJobsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSystemEventsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    RECORDED_AT_DESC = "recorded_at_desc"
    RECORDED_AT_ASC = "recorded_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ResourceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    SECM_SECRET = "secm_secret"
    SECM_SECRET_VERSION = "secm_secret_version"
    KUBE_CLUSTER = "kube_cluster"
    KUBE_POOL = "kube_pool"
    KUBE_NODE = "kube_node"
    KUBE_ACL = "kube_acl"
    KEYM_KEY = "keym_key"
    IAM_USER = "iam_user"
    IAM_APPLICATION = "iam_application"
    IAM_GROUP = "iam_group"
    IAM_POLICY = "iam_policy"
    IAM_API_KEY = "iam_api_key"
    IAM_SSH_KEY = "iam_ssh_key"
    IAM_RULE = "iam_rule"
    IAM_SAML = "iam_saml"
    IAM_SAML_CERTIFICATE = "iam_saml_certificate"
    IAM_SCIM = "iam_scim"
    IAM_SCIM_TOKEN = "iam_scim_token"
    SECRET_MANAGER_SECRET = "secret_manager_secret"
    SECRET_MANAGER_VERSION = "secret_manager_version"
    KEY_MANAGER_KEY = "key_manager_key"
    ACCOUNT_USER = "account_user"
    ACCOUNT_ORGANIZATION = "account_organization"
    ACCOUNT_PROJECT = "account_project"
    ACCOUNT_CONTRACT_SIGNATURE = "account_contract_signature"
    INSTANCE_SERVER = "instance_server"
    INSTANCE_PLACEMENT_GROUP = "instance_placement_group"
    INSTANCE_SECURITY_GROUP = "instance_security_group"
    INSTANCE_VOLUME = "instance_volume"
    INSTANCE_SNAPSHOT = "instance_snapshot"
    INSTANCE_IMAGE = "instance_image"
    INSTANCE_TEMPLATE = "instance_template"
    APPLE_SILICON_SERVER = "apple_silicon_server"
    BAREMETAL_SERVER = "baremetal_server"
    BAREMETAL_SETTING = "baremetal_setting"
    IPAM_IP = "ipam_ip"
    SBS_VOLUME = "sbs_volume"
    SBS_SNAPSHOT = "sbs_snapshot"
    LOAD_BALANCER_LB = "load_balancer_lb"
    LOAD_BALANCER_IP = "load_balancer_ip"
    LOAD_BALANCER_FRONTEND = "load_balancer_frontend"
    LOAD_BALANCER_BACKEND = "load_balancer_backend"
    LOAD_BALANCER_ROUTE = "load_balancer_route"
    LOAD_BALANCER_ACL = "load_balancer_acl"
    LOAD_BALANCER_CERTIFICATE = "load_balancer_certificate"
    SFS_FILESYSTEM = "sfs_filesystem"
    VPC_PRIVATE_NETWORK = "vpc_private_network"
    VPC_VPC = "vpc_vpc"
    VPC_SUBNET = "vpc_subnet"
    VPC_ROUTE = "vpc_route"
    VPC_ACL = "vpc_acl"
    EDGE_SERVICES_PLAN = "edge_services_plan"
    EDGE_SERVICES_PIPELINE = "edge_services_pipeline"
    EDGE_SERVICES_DNS_STAGE = "edge_services_dns_stage"
    EDGE_SERVICES_TLS_STAGE = "edge_services_tls_stage"
    EDGE_SERVICES_CACHE_STAGE = "edge_services_cache_stage"
    EDGE_SERVICES_ROUTE_STAGE = "edge_services_route_stage"
    EDGE_SERVICES_ROUTE_RULES = "edge_services_route_rules"
    EDGE_SERVICES_WAF_STAGE = "edge_services_waf_stage"
    EDGE_SERVICES_BACKEND_STAGE = "edge_services_backend_stage"
    S2S_VPN_GATEWAY = "s2s_vpn_gateway"
    S2S_CUSTOMER_GATEWAY = "s2s_customer_gateway"
    S2S_ROUTING_POLICY = "s2s_routing_policy"
    S2S_CONNECTION = "s2s_connection"
    VPC_GW_GATEWAY = "vpc_gw_gateway"
    VPC_GW_GATEWAY_NETWORK = "vpc_gw_gateway_network"
    VPC_GW_DHCP = "vpc_gw_dhcp"
    VPC_GW_DHCP_ENTRY = "vpc_gw_dhcp_entry"
    VPC_GW_PAT_RULE = "vpc_gw_pat_rule"
    VPC_GW_IP = "vpc_gw_ip"
    AUDIT_TRAIL_EXPORT_JOB = "audit_trail_export_job"
    RDB_INSTANCE = "rdb_instance"
    RDB_INSTANCE_BACKUP = "rdb_instance_backup"
    RDB_INSTANCE_ENDPOINT = "rdb_instance_endpoint"
    RDB_INSTANCE_LOGS = "rdb_instance_logs"
    RDB_INSTANCE_READ_REPLICA = "rdb_instance_read_replica"
    RDB_INSTANCE_SNAPSHOT = "rdb_instance_snapshot"

    def __str__(self) -> str:
        return str(self.value)


class SystemEventKind(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_KIND = "unknown_kind"
    CRON = "cron"
    NOTIFICATION = "notification"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class AccountContractSignatureInfoAccountContractInfo:
    id: str
    type_: str
    name: str
    version: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class AccountContractSignatureInfo:
    signed_by_account_root_user_id: str
    signed_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    contract: Optional[AccountContractSignatureInfoAccountContractInfo] = None


@dataclass
class AccountOrganizationInfo:
    pass


@dataclass
class AccountProjectInfo:
    description: str


@dataclass
class AccountUserInfo:
    email: str
    phone_number: Optional[str] = None


@dataclass
class AppleSiliconServerInfo:
    id: str
    name: str


@dataclass
class AuditTrailExportJobInfo:
    pass


@dataclass
class BaremetalServerInfo:
    description: str
    tags: list[str]


@dataclass
class BaremetalSettingInfo:
    type_: str


@dataclass
class EdgeServicesBackendStageInfo:
    pipeline_id: Optional[str] = None


@dataclass
class EdgeServicesCacheStageInfo:
    pipeline_id: Optional[str] = None


@dataclass
class EdgeServicesDNSStageInfo:
    pipeline_id: Optional[str] = None


@dataclass
class EdgeServicesPipelineInfo:
    name: str


@dataclass
class EdgeServicesPlanInfo:
    pass


@dataclass
class EdgeServicesRouteRulesInfo:
    route_stage_id: str


@dataclass
class EdgeServicesRouteStageInfo:
    pipeline_id: Optional[str] = None


@dataclass
class EdgeServicesTLSStageInfo:
    pipeline_id: Optional[str] = None


@dataclass
class EdgeServicesWAFStageInfo:
    pipeline_id: Optional[str] = None


@dataclass
class InstanceServerInfo:
    name: str


@dataclass
class IpamIpInfo:
    address: str


@dataclass
class KeyManagerKeyInfo:
    pass


@dataclass
class KubernetesACLInfo:
    pass


@dataclass
class KubernetesClusterInfo:
    pass


@dataclass
class KubernetesNodeInfo:
    id: str
    name: str


@dataclass
class KubernetesPoolInfo:
    id: str
    name: str


@dataclass
class LoadBalancerAclInfo:
    frontend_id: str


@dataclass
class LoadBalancerBackendInfo:
    lb_id: str
    name: str


@dataclass
class LoadBalancerCertificateInfo:
    lb_id: str
    name: str


@dataclass
class LoadBalancerFrontendInfo:
    lb_id: str
    name: str


@dataclass
class LoadBalancerIpInfo:
    ip_address: str
    lb_id: Optional[str] = None


@dataclass
class LoadBalancerLbInfo:
    name: str


@dataclass
class LoadBalancerRouteInfo:
    frontend_id: str
    backend_id: str


@dataclass
class SecretManagerSecretInfo:
    path: str
    key_id: Optional[str] = None


@dataclass
class SecretManagerSecretVersionInfo:
    revision: int


@dataclass
class VpcGwGatewayInfo:
    gateway_type_id: str
    vpc_id: Optional[str] = None
    public_ip_id: Optional[str] = None


@dataclass
class VpcGwGatewayNetworkInfo:
    gateway_id: str
    pn_id: str
    address: Optional[str] = None


@dataclass
class VpcPrivateNetworkInfo:
    vpc_id: str
    push_default_route: bool


@dataclass
class VpcRouteInfo:
    vpc_id: str
    destination: str
    nexthop_resource_key: Optional[str] = None
    nexthop_private_network_key: Optional[str] = None


@dataclass
class VpcSubnetInfo:
    subnet_cidr: str
    vpc_id: str


@dataclass
class Resource:
    id: str
    type_: ResourceType
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    name: Optional[str] = None
    secm_secret_info: Optional[SecretManagerSecretInfo] = None

    secm_secret_version_info: Optional[SecretManagerSecretVersionInfo] = None

    kube_cluster_info: Optional[KubernetesClusterInfo] = None

    kube_pool_info: Optional[KubernetesPoolInfo] = None

    kube_node_info: Optional[KubernetesNodeInfo] = None

    kube_acl_info: Optional[KubernetesACLInfo] = None

    keym_key_info: Optional[KeyManagerKeyInfo] = None

    secret_manager_secret_info: Optional[SecretManagerSecretInfo] = None

    secret_manager_version_info: Optional[SecretManagerSecretVersionInfo] = None

    key_manager_key_info: Optional[KeyManagerKeyInfo] = None

    account_user_info: Optional[AccountUserInfo] = None

    account_organization_info: Optional[AccountOrganizationInfo] = None

    instance_server_info: Optional[InstanceServerInfo] = None

    apple_silicon_server_info: Optional[AppleSiliconServerInfo] = None

    account_project_info: Optional[AccountProjectInfo] = None

    baremetal_server_info: Optional[BaremetalServerInfo] = None

    baremetal_setting_info: Optional[BaremetalSettingInfo] = None

    ipam_ip_info: Optional[IpamIpInfo] = None

    load_balancer_lb_info: Optional[LoadBalancerLbInfo] = None

    load_balancer_ip_info: Optional[LoadBalancerIpInfo] = None

    load_balancer_frontend_info: Optional[LoadBalancerFrontendInfo] = None

    load_balancer_backend_info: Optional[LoadBalancerBackendInfo] = None

    load_balancer_route_info: Optional[LoadBalancerRouteInfo] = None

    load_balancer_acl_info: Optional[LoadBalancerAclInfo] = None

    load_balancer_certificate_info: Optional[LoadBalancerCertificateInfo] = None

    edge_services_plan_info: Optional[EdgeServicesPlanInfo] = None

    edge_services_pipeline_info: Optional[EdgeServicesPipelineInfo] = None

    edge_services_dns_stage_info: Optional[EdgeServicesDNSStageInfo] = None

    edge_services_tls_stage_info: Optional[EdgeServicesTLSStageInfo] = None

    edge_services_cache_stage_info: Optional[EdgeServicesCacheStageInfo] = None

    edge_services_route_stage_info: Optional[EdgeServicesRouteStageInfo] = None

    edge_services_route_rules_info: Optional[EdgeServicesRouteRulesInfo] = None

    edge_services_waf_stage_info: Optional[EdgeServicesWAFStageInfo] = None

    edge_services_backend_stage_info: Optional[EdgeServicesBackendStageInfo] = None

    account_contract_signature_info: Optional[AccountContractSignatureInfo] = None

    vpc_subnet_info: Optional[VpcSubnetInfo] = None

    vpc_route_info: Optional[VpcRouteInfo] = None

    vpc_private_network_info: Optional[VpcPrivateNetworkInfo] = None

    audit_trail_export_job_info: Optional[AuditTrailExportJobInfo] = None

    vpc_gw_gateway_info: Optional[VpcGwGatewayInfo] = None

    vpc_gw_gateway_network_info: Optional[VpcGwGatewayNetworkInfo] = None


@dataclass
class EventPrincipal:
    id: str


@dataclass
class AuthenticationEvent:
    id: str
    """
    ID of the event.
    """

    organization_id: str
    """
    Organization ID containing the event.
    """

    source_ip: str
    """
    IP address at the origin of the event.
    """

    resources: list[Resource]
    """
    Resources attached to the event.
    """

    result: AuthenticationEventResult
    """
    Result of the authentication attempt.
    """

    method: AuthenticationEventMethod
    """
    Authentication method used.
    """

    origin: AuthenticationEventOrigin
    """
    Origin of the authentication attempt.
    """

    recorded_at: Optional[datetime] = None
    """
    Timestamp of the event.
    """

    user_agent: Optional[str] = None
    """
    User Agent at the origin of the event.
    """

    failure_reason: Optional[AuthenticationEventFailureReason] = (
        AuthenticationEventFailureReason.UNKNOWN_FAILURE_REASON
    )
    """
    (Optional) Reason for authentication failure.
    """

    country_code: Optional[StdCountryCode] = StdCountryCode.UNKNOWN_COUNTRY_CODE
    """
    (Optional) ISO 3166-1 alpha-2 country code of the source IP.
    """

    mfa_type: Optional[AuthenticationEventMFAType] = (
        AuthenticationEventMFAType.UNKNOWN_MFA_TYPE
    )
    """
    (Optional) MFA type used for the authentication attempt.
    """


@dataclass
class Event:
    id: str
    """
    ID of the event.
    """

    locality: str
    """
    Locality of the resource attached to the event.
    """

    organization_id: str
    """
    Organization ID containing the event.
    """

    source_ip: str
    """
    IP address at the origin of the event.
    """

    product_name: str
    """
    Product name of the resource attached to the event.
    """

    service_name: str
    """
    API name called to trigger the event.
    """

    method_name: str
    """
    API method called to trigger the event.
    """

    resources: list[Resource]
    """
    Resources attached to the event.
    """

    request_id: str
    """
    Unique identifier of the request at the origin of the event.
    """

    status_code: int
    """
    HTTP status code resulting of the API call.
    """

    recorded_at: Optional[datetime] = None
    """
    Timestamp of the event.
    """

    project_id: Optional[str] = None
    """
    (Optional) Project of the resource attached to the event.
    """

    user_agent: Optional[str] = None
    """
    User Agent at the origin of the event.
    """

    request_body: Optional[dict[str, Any]] = field(default_factory=dict)
    """
    Request at the origin of the event.
    """

    principal: Optional[EventPrincipal] = None


@dataclass
class SystemEvent:
    id: str
    """
    ID of the system event.
    """

    locality: str
    """
    Locality of the system event.
    """

    organization_id: str
    """
    Organization ID containing the system event.
    """

    product_name: str
    """
    Name of the Scaleway product in a hyphenated format.
    """

    source: str
    """
    Source of the system event.
    """

    system_name: str
    """
    Name of the jobs, notification, etc.
    """

    resources: list[Resource]
    """
    Resources attached to the event.
    """

    kind: SystemEventKind
    """
    Source of the event (unknown, cron or notification).
    """

    recorded_at: Optional[datetime] = None
    """
    Timestamp of the system event.
    """

    project_id: Optional[str] = None
    """
    Project of the resource attached to the system event.
    """


@dataclass
class ExportJobS3:
    bucket: str
    region: ScwRegion
    """
    Region to target. If none is passed will use default region from the config.
    """

    prefix: Optional[str] = None
    project_id: Optional[str] = None


@dataclass
class ExportJobStatus:
    code: ExportJobStatusCode
    message: Optional[str] = None


@dataclass
class ProductService:
    name: str
    methods: list[str]


@dataclass
class AlertRule:
    id: str
    """
    ID of the alert rule.
    """

    name: str
    """
    Name of the alert rule.
    """

    description: str
    """
    Description of the alert rule.
    """

    status: AlertRuleStatus
    """
    Current status of the alert rule.
    """


@dataclass
class ListCombinedEventsResponseCombinedEvent:
    api: Optional[Event] = None

    auth: Optional[AuthenticationEvent] = None

    system: Optional[SystemEvent] = None


@dataclass
class ExportJob:
    id: str
    """
    ID of the export job.
    """

    organization_id: str
    """
    ID of the targeted Organization.
    """

    name: str
    """
    Name of the export job.
    """

    tags: list[str]
    """
    Tags of the export job.
    """

    created_at: Optional[datetime] = None
    """
    Export job creation date.
    """

    last_run_at: Optional[datetime] = None
    """
    Last run of export job.
    """

    last_status: Optional[ExportJobStatus] = None
    """
    Status of last export job.
    """

    s3: Optional[ExportJobS3] = None


@dataclass
class Product:
    title: str
    """
    Product title.
    """

    name: str
    """
    Product name.
    """

    services: list[ProductService]
    """
    Specifies the API versions of the products integrated with Audit Trail. Each version defines the methods logged by Audit Trail.
    """


@dataclass
class CreateExportJobRequest:
    name: str
    """
    Name of the export.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization to target.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the export.
    """

    s3: Optional[ExportJobS3] = None


@dataclass
class DeleteExportJobRequest:
    export_job_id: str
    """
    ID of the export job.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DisableAlertRulesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization to target.
    """

    alert_rule_ids: Optional[list[str]] = field(default_factory=list)
    """
    List of IDs of the rules to disable.
    """


@dataclass
class DisableAlertRulesResponse:
    alert_rules: list[AlertRule]
    """
    List of the rules that were disabled.
    """


@dataclass
class EnableAlertRulesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization to target.
    """

    alert_rule_ids: Optional[list[str]] = field(default_factory=list)
    """
    List of IDs of the rules to enable.
    """


@dataclass
class EnableAlertRulesResponse:
    alert_rules: list[AlertRule]
    """
    List of the rules that were enabled.
    """


@dataclass
class ListAlertRulesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization to target.
    """

    status: Optional[AlertRuleStatus] = AlertRuleStatus.UNKNOWN_STATUS
    """
    (Optional) Status of the alert rule.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0


@dataclass
class ListAlertRulesResponse:
    alert_rules: list[AlertRule]
    """
    Single page of alert rules matching the requested criteria.
    """

    total_count: int
    """
    Total count of alert rules matching the requested criteria.
    """


@dataclass
class ListAuthenticationEventsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str] = None
    recorded_after: Optional[datetime] = None
    recorded_before: Optional[datetime] = None
    order_by: Optional[ListAuthenticationEventsRequestOrderBy] = None
    page_size: Optional[int] = None
    page_token: Optional[str] = None


@dataclass
class ListAuthenticationEventsResponse:
    events: list[AuthenticationEvent]
    next_page_token: Optional[str] = None


@dataclass
class ListCombinedEventsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str] = None
    project_id: Optional[str] = None
    resource_type: Optional[ResourceType] = None
    recorded_after: Optional[datetime] = None
    recorded_before: Optional[datetime] = None
    order_by: Optional[ListCombinedEventsRequestOrderBy] = None
    page_size: Optional[int] = None
    page_token: Optional[str] = None


@dataclass
class ListCombinedEventsResponse:
    events: list[ListCombinedEventsResponseCombinedEvent]
    next_page_token: Optional[str] = None


@dataclass
class ListEventsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    (Optional) ID of the Project containing the Audit Trail events.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization containing the Audit Trail events.
    """

    resource_type: Optional[ResourceType] = ResourceType.UNKNOWN_TYPE
    """
    (Optional) Type of the Scaleway resource.
    """

    method_name: Optional[str] = None
    """
    (Optional) Name of the method of the API call performed.
    """

    status: Optional[int] = 0
    """
    (Optional) HTTP status code of the request. Returns either `200` if the request was successful or `403` if the permission was denied.
    """

    recorded_after: Optional[datetime] = None
    """
    (Optional) The `recorded_after` parameter defines the earliest timestamp from which Audit Trail events are retrieved. Returns `one hour ago` by default.
    """

    recorded_before: Optional[datetime] = None
    """
    (Optional) The `recorded_before` parameter defines the latest timestamp up to which Audit Trail events are retrieved. Returns `now` by default.
    """

    order_by: Optional[ListEventsRequestOrderBy] = (
        ListEventsRequestOrderBy.RECORDED_AT_DESC
    )
    page_size: Optional[int] = 0
    page_token: Optional[str] = None
    product_name: Optional[str] = None
    """
    (Optional) Name of the Scaleway product in a hyphenated format.
    """

    service_name: Optional[str] = None
    """
    (Optional) Name of the service of the API call performed.
    """

    resource_id: Optional[str] = None
    """
    (Optional) ID of the Scaleway resource.
    """

    principal_id: Optional[str] = None
    """
    (Optional) ID of the User or IAM application at the origin of the event.
    """

    source_ip: Optional[str] = None
    """
    (Optional) IP address at the origin of the event.
    """


@dataclass
class ListEventsResponse:
    events: list[Event]
    """
    Single page of events matching the requested criteria.
    """

    next_page_token: Optional[str] = None
    """
    Page token to use in following calls to keep listing.
    """


@dataclass
class ListExportJobsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str] = None
    """
    Filter by Organization ID.
    """

    name: Optional[str] = None
    """
    (Optional) Filter by export name.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    (Optional) List of tags to filter on.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0
    order_by: Optional[ListExportJobsRequestOrderBy] = (
        ListExportJobsRequestOrderBy.NAME_ASC
    )


@dataclass
class ListExportJobsResponse:
    export_jobs: list[ExportJob]
    """
    Single page of export jobs matching the requested criteria.
    """

    total_count: int
    """
    Total count of export jobs matching the requested criteria.
    """


@dataclass
class ListProductsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization containing the Audit Trail events.
    """


@dataclass
class ListProductsResponse:
    products: list[Product]
    """
    List of all products integrated with Audit Trail.
    """

    total_count: int
    """
    Number of integrated products.
    """


@dataclass
class ListSystemEventsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization containing the Audit Trail system events.
    """

    recorded_after: Optional[datetime] = None
    """
    (Optional) The `recorded_after` parameter defines the earliest timestamp from which Audit Trail system events are retrieved. Returns `one hour ago` by default.
    """

    recorded_before: Optional[datetime] = None
    """
    (Optional) The `recorded_before` parameter defines the latest timestamp up to which Audit Trail system events are retrieved. Returns `now` by default.
    """

    order_by: Optional[ListSystemEventsRequestOrderBy] = (
        ListSystemEventsRequestOrderBy.RECORDED_AT_DESC
    )
    page_size: Optional[int] = 0
    page_token: Optional[str] = None


@dataclass
class ListSystemEventsResponse:
    events: list[SystemEvent]
    """
    Single page of system events matching the requested criteria.
    """

    next_page_token: Optional[str] = None
    """
    Page token to use in following calls to keep listing.
    """


@dataclass
class SetEnabledAlertRulesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization to target.
    """

    enabled_alert_rule_ids: Optional[list[str]] = field(default_factory=list)
    """
    List of IDs of the rules that must be enabled after the update.
    """


@dataclass
class SetEnabledAlertRulesResponse:
    alert_rules: list[AlertRule]
    """
    List of the rules that were enabled.
    """
