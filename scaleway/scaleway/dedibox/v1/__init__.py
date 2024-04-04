# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from .types import AttachFailoverIPToMacAddressRequestMacType
from .types import BMCAccessStatus
from .content import BMC_ACCESS_TRANSIENT_STATUSES
from .types import BackupStatus
from .types import FailoverBlockVersion
from .types import FailoverIPInterfaceType
from .types import FailoverIPStatus
from .types import FailoverIPVersion
from .types import GetRpnStatusResponseStatus
from .types import IPSemantic
from .types import IPStatus
from .types import IPVersion
from .types import IPv6BlockDelegationStatus
from .content import I_PV6_BLOCK_DELEGATION_TRANSIENT_STATUSES
from .types import InvoicePaymentMethod
from .types import InvoiceStatus
from .types import ListFailoverIPsRequestOrderBy
from .types import ListInvoicesRequestOrderBy
from .types import ListOSRequestOrderBy
from .types import ListOffersRequestOrderBy
from .types import ListRefundsRequestOrderBy
from .types import ListRpnCapableSanServersRequestOrderBy
from .types import ListRpnCapableServersRequestOrderBy
from .types import ListRpnGroupMembersRequestOrderBy
from .types import ListRpnGroupsRequestOrderBy
from .types import ListRpnInvitesRequestOrderBy
from .types import ListRpnSansRequestOrderBy
from .types import ListRpnServerCapabilitiesRequestOrderBy
from .types import ListRpnV2CapableResourcesRequestOrderBy
from .types import ListRpnV2GroupLogsRequestOrderBy
from .types import ListRpnV2GroupsRequestOrderBy
from .types import ListRpnV2MembersRequestOrderBy
from .types import ListRpnV2MembersRequestType
from .types import ListServerDisksRequestOrderBy
from .types import ListServerEventsRequestOrderBy
from .types import ListServersRequestOrderBy
from .types import ListServicesRequestOrderBy
from .types import LogAction
from .types import LogStatus
from .types import MemoryType
from .types import NetworkInterfaceInterfaceType
from .types import OSArch
from .types import OSType
from .types import OfferAntiDosInfoType
from .types import OfferCatalog
from .types import OfferPaymentFrequency
from .types import OfferSANInfoType
from .types import OfferServerInfoStock
from .types import PartitionFileSystem
from .types import PartitionType
from .types import RaidArrayRaidLevel
from .types import RefundMethod
from .types import RefundStatus
from .types import RescueProtocol
from .types import RpnGroupMemberStatus
from .content import RPN_GROUP_MEMBER_TRANSIENT_STATUSES
from .types import RpnGroupType
from .types import RpnSanIpType
from .types import RpnSanStatus
from .content import RPN_SAN_TRANSIENT_STATUSES
from .types import RpnV2GroupStatus
from .content import RPN_V2_GROUP_TRANSIENT_STATUSES
from .types import RpnV2GroupType
from .types import RpnV2MemberStatus
from .content import RPN_V2_MEMBER_TRANSIENT_STATUSES
from .types import ServerDiskType
from .types import ServerInstallStatus
from .content import SERVER_INSTALL_TRANSIENT_STATUSES
from .types import ServerStatus
from .content import SERVER_TRANSIENT_STATUSES
from .types import ServiceLevelLevel
from .types import ServiceProvisioningStatus
from .content import SERVICE_PROVISIONING_TRANSIENT_STATUSES
from .types import ServiceType
from .types import OfferAntiDosInfo
from .types import OfferBackupInfo
from .types import OfferBandwidthInfo
from .types import OfferLicenseInfo
from .types import OfferRPNInfo
from .types import OfferSANInfo
from .types import OfferStorageInfo
from .types import IP
from .types import Offer
from .types import NetworkInterface
from .types import OS
from .types import ServerLocation
from .types import ServerOption
from .types import ServiceLevel
from .types import RpnSan
from .types import RpnGroup
from .types import RpnV2GroupSubnet
from .types import Server
from .types import FailoverBlock
from .types import RpnSanIpRpnV2Group
from .types import RpnSanIpServer
from .types import RpnSanServer
from .types import RpnV2Group
from .types import RpnV2Member
from .types import ServerDisk
from .types import Service
from .types import GetIPv6BlockQuotasResponseQuota
from .types import InstallPartition
from .types import FailoverIP
from .types import ListIPv6BlockSubnetsAvailableResponseSubnet
from .types import InvoiceSummary
from .types import RpnSanIp
from .types import RefundSummary
from .types import RpnGroupMember
from .types import RpnSanSummary
from .types import RpnServerCapability
from .types import Log
from .types import ServerEvent
from .types import ServerSummary
from .types import CPU
from .types import Disk
from .types import Memory
from .types import PersistentMemory
from .types import RaidController
from .types import RaidArray
from .types import Partition
from .types import UpdatableRaidArray
from .types import AttachFailoverIPToMacAddressRequest
from .types import AttachFailoverIPsRequest
from .types import BMCAccess
from .types import Backup
from .types import BillingApiCanOrderRequest
from .types import BillingApiDownloadInvoiceRequest
from .types import BillingApiDownloadRefundRequest
from .types import BillingApiGetInvoiceRequest
from .types import BillingApiGetRefundRequest
from .types import BillingApiListInvoicesRequest
from .types import BillingApiListRefundsRequest
from .types import CanOrderResponse
from .types import CancelServerInstallRequest
from .types import CreateFailoverIPsRequest
from .types import CreateFailoverIPsResponse
from .types import CreateServerRequest
from .types import DeleteFailoverIPRequest
from .types import DeleteServerRequest
from .types import DeleteServiceRequest
from .types import DetachFailoverIPFromMacAddressRequest
from .types import DetachFailoverIPsRequest
from .types import GetBMCAccessRequest
from .types import GetFailoverIPRequest
from .types import GetIPv6BlockQuotasResponse
from .types import GetOSRequest
from .types import GetOfferRequest
from .types import GetOrderedServiceRequest
from .types import GetRaidRequest
from .types import GetRemainingQuotaRequest
from .types import GetRemainingQuotaResponse
from .types import GetRescueRequest
from .types import GetRpnStatusResponse
from .types import GetServerBackupRequest
from .types import GetServerDefaultPartitioningRequest
from .types import GetServerInstallRequest
from .types import GetServerRequest
from .types import GetServiceRequest
from .types import IPv6Block
from .types import IPv6BlockApiCreateIPv6BlockRequest
from .types import IPv6BlockApiCreateIPv6BlockSubnetRequest
from .types import IPv6BlockApiDeleteIPv6BlockRequest
from .types import IPv6BlockApiGetIPv6BlockQuotasRequest
from .types import IPv6BlockApiGetIPv6BlockRequest
from .types import IPv6BlockApiListIPv6BlockSubnetsAvailableRequest
from .types import IPv6BlockApiUpdateIPv6BlockRequest
from .types import InstallServerRequest
from .types import Invoice
from .types import ListFailoverIPsRequest
from .types import ListFailoverIPsResponse
from .types import ListIPv6BlockSubnetsAvailableResponse
from .types import ListInvoicesResponse
from .types import ListIpsResponse
from .types import ListOSRequest
from .types import ListOSResponse
from .types import ListOffersRequest
from .types import ListOffersResponse
from .types import ListRefundsResponse
from .types import ListRpnCapableSanServersResponse
from .types import ListRpnCapableServersResponse
from .types import ListRpnGroupMembersResponse
from .types import ListRpnGroupsResponse
from .types import ListRpnInvitesResponse
from .types import ListRpnSansResponse
from .types import ListRpnServerCapabilitiesResponse
from .types import ListRpnV2CapableResourcesResponse
from .types import ListRpnV2GroupLogsResponse
from .types import ListRpnV2GroupsResponse
from .types import ListRpnV2MembersResponse
from .types import ListServerDisksRequest
from .types import ListServerDisksResponse
from .types import ListServerEventsRequest
from .types import ListServerEventsResponse
from .types import ListServersRequest
from .types import ListServersResponse
from .types import ListServicesRequest
from .types import ListServicesResponse
from .types import ListSubscribableServerOptionsRequest
from .types import ListSubscribableServerOptionsResponse
from .types import OfferFailoverBlockInfo
from .types import OfferFailoverIpInfo
from .types import OfferServerInfo
from .types import OfferServiceLevelInfo
from .types import Raid
from .types import RebootServerRequest
from .types import Refund
from .types import Rescue
from .types import RpnApiGetRpnStatusRequest
from .types import RpnApiListRpnServerCapabilitiesRequest
from .types import RpnSanApiAddIpRequest
from .types import RpnSanApiCreateRpnSanRequest
from .types import RpnSanApiDeleteRpnSanRequest
from .types import RpnSanApiGetRpnSanRequest
from .types import RpnSanApiListAvailableIpsRequest
from .types import RpnSanApiListIpsRequest
from .types import RpnSanApiListRpnSansRequest
from .types import RpnSanApiRemoveIpRequest
from .types import RpnV1ApiAcceptRpnInviteRequest
from .types import RpnV1ApiAddRpnGroupMembersRequest
from .types import RpnV1ApiCreateRpnGroupRequest
from .types import RpnV1ApiDeleteRpnGroupMembersRequest
from .types import RpnV1ApiDeleteRpnGroupRequest
from .types import RpnV1ApiGetRpnGroupRequest
from .types import RpnV1ApiLeaveRpnGroupRequest
from .types import RpnV1ApiListRpnCapableSanServersRequest
from .types import RpnV1ApiListRpnCapableServersRequest
from .types import RpnV1ApiListRpnGroupMembersRequest
from .types import RpnV1ApiListRpnGroupsRequest
from .types import RpnV1ApiListRpnInvitesRequest
from .types import RpnV1ApiRefuseRpnInviteRequest
from .types import RpnV1ApiRpnGroupInviteRequest
from .types import RpnV1ApiUpdateRpnGroupNameRequest
from .types import RpnV2ApiAddRpnV2MembersRequest
from .types import RpnV2ApiCreateRpnV2GroupRequest
from .types import RpnV2ApiDeleteRpnV2GroupRequest
from .types import RpnV2ApiDeleteRpnV2MembersRequest
from .types import RpnV2ApiDisableRpnV2GroupCompatibilityRequest
from .types import RpnV2ApiEnableRpnV2GroupCompatibilityRequest
from .types import RpnV2ApiGetRpnV2GroupRequest
from .types import RpnV2ApiListRpnV2CapableResourcesRequest
from .types import RpnV2ApiListRpnV2GroupLogsRequest
from .types import RpnV2ApiListRpnV2GroupsRequest
from .types import RpnV2ApiListRpnV2MembersRequest
from .types import RpnV2ApiUpdateRpnV2GroupNameRequest
from .types import RpnV2ApiUpdateRpnV2VlanForMembersRequest
from .types import ServerDefaultPartitioning
from .types import ServerInstall
from .types import StartBMCAccessRequest
from .types import StartRescueRequest
from .types import StartServerRequest
from .types import StopBMCAccessRequest
from .types import StopRescueRequest
from .types import StopServerRequest
from .types import SubscribeServerOptionRequest
from .types import SubscribeStorageOptionsRequest
from .types import SubscribeStorageOptionsResponse
from .types import UpdateRaidRequest
from .types import UpdateReverseRequest
from .types import UpdateServerBackupRequest
from .types import UpdateServerRequest
from .types import UpdateServerTagsRequest
from .api import DediboxV1API
from .api import DediboxV1BillingAPI
from .api import DediboxV1IPv6BlockAPI
from .api import DediboxV1RpnAPI
from .api import DediboxV1RpnSanAPI
from .api import DediboxV1RpnV1API
from .api import DediboxV1RpnV2API

__all__ = [
    "AttachFailoverIPToMacAddressRequestMacType",
    "BMCAccessStatus",
    "BMC_ACCESS_TRANSIENT_STATUSES",
    "BackupStatus",
    "FailoverBlockVersion",
    "FailoverIPInterfaceType",
    "FailoverIPStatus",
    "FailoverIPVersion",
    "GetRpnStatusResponseStatus",
    "IPSemantic",
    "IPStatus",
    "IPVersion",
    "IPv6BlockDelegationStatus",
    "I_PV6_BLOCK_DELEGATION_TRANSIENT_STATUSES",
    "InvoicePaymentMethod",
    "InvoiceStatus",
    "ListFailoverIPsRequestOrderBy",
    "ListInvoicesRequestOrderBy",
    "ListOSRequestOrderBy",
    "ListOffersRequestOrderBy",
    "ListRefundsRequestOrderBy",
    "ListRpnCapableSanServersRequestOrderBy",
    "ListRpnCapableServersRequestOrderBy",
    "ListRpnGroupMembersRequestOrderBy",
    "ListRpnGroupsRequestOrderBy",
    "ListRpnInvitesRequestOrderBy",
    "ListRpnSansRequestOrderBy",
    "ListRpnServerCapabilitiesRequestOrderBy",
    "ListRpnV2CapableResourcesRequestOrderBy",
    "ListRpnV2GroupLogsRequestOrderBy",
    "ListRpnV2GroupsRequestOrderBy",
    "ListRpnV2MembersRequestOrderBy",
    "ListRpnV2MembersRequestType",
    "ListServerDisksRequestOrderBy",
    "ListServerEventsRequestOrderBy",
    "ListServersRequestOrderBy",
    "ListServicesRequestOrderBy",
    "LogAction",
    "LogStatus",
    "MemoryType",
    "NetworkInterfaceInterfaceType",
    "OSArch",
    "OSType",
    "OfferAntiDosInfoType",
    "OfferCatalog",
    "OfferPaymentFrequency",
    "OfferSANInfoType",
    "OfferServerInfoStock",
    "PartitionFileSystem",
    "PartitionType",
    "RaidArrayRaidLevel",
    "RefundMethod",
    "RefundStatus",
    "RescueProtocol",
    "RpnGroupMemberStatus",
    "RPN_GROUP_MEMBER_TRANSIENT_STATUSES",
    "RpnGroupType",
    "RpnSanIpType",
    "RpnSanStatus",
    "RPN_SAN_TRANSIENT_STATUSES",
    "RpnV2GroupStatus",
    "RPN_V2_GROUP_TRANSIENT_STATUSES",
    "RpnV2GroupType",
    "RpnV2MemberStatus",
    "RPN_V2_MEMBER_TRANSIENT_STATUSES",
    "ServerDiskType",
    "ServerInstallStatus",
    "SERVER_INSTALL_TRANSIENT_STATUSES",
    "ServerStatus",
    "SERVER_TRANSIENT_STATUSES",
    "ServiceLevelLevel",
    "ServiceProvisioningStatus",
    "SERVICE_PROVISIONING_TRANSIENT_STATUSES",
    "ServiceType",
    "OfferAntiDosInfo",
    "OfferBackupInfo",
    "OfferBandwidthInfo",
    "OfferLicenseInfo",
    "OfferRPNInfo",
    "OfferSANInfo",
    "OfferStorageInfo",
    "IP",
    "Offer",
    "NetworkInterface",
    "OS",
    "ServerLocation",
    "ServerOption",
    "ServiceLevel",
    "RpnSan",
    "RpnGroup",
    "RpnV2GroupSubnet",
    "Server",
    "FailoverBlock",
    "RpnSanIpRpnV2Group",
    "RpnSanIpServer",
    "RpnSanServer",
    "RpnV2Group",
    "RpnV2Member",
    "ServerDisk",
    "Service",
    "GetIPv6BlockQuotasResponseQuota",
    "InstallPartition",
    "FailoverIP",
    "ListIPv6BlockSubnetsAvailableResponseSubnet",
    "InvoiceSummary",
    "RpnSanIp",
    "RefundSummary",
    "RpnGroupMember",
    "RpnSanSummary",
    "RpnServerCapability",
    "Log",
    "ServerEvent",
    "ServerSummary",
    "CPU",
    "Disk",
    "Memory",
    "PersistentMemory",
    "RaidController",
    "RaidArray",
    "Partition",
    "UpdatableRaidArray",
    "AttachFailoverIPToMacAddressRequest",
    "AttachFailoverIPsRequest",
    "BMCAccess",
    "Backup",
    "BillingApiCanOrderRequest",
    "BillingApiDownloadInvoiceRequest",
    "BillingApiDownloadRefundRequest",
    "BillingApiGetInvoiceRequest",
    "BillingApiGetRefundRequest",
    "BillingApiListInvoicesRequest",
    "BillingApiListRefundsRequest",
    "CanOrderResponse",
    "CancelServerInstallRequest",
    "CreateFailoverIPsRequest",
    "CreateFailoverIPsResponse",
    "CreateServerRequest",
    "DeleteFailoverIPRequest",
    "DeleteServerRequest",
    "DeleteServiceRequest",
    "DetachFailoverIPFromMacAddressRequest",
    "DetachFailoverIPsRequest",
    "GetBMCAccessRequest",
    "GetFailoverIPRequest",
    "GetIPv6BlockQuotasResponse",
    "GetOSRequest",
    "GetOfferRequest",
    "GetOrderedServiceRequest",
    "GetRaidRequest",
    "GetRemainingQuotaRequest",
    "GetRemainingQuotaResponse",
    "GetRescueRequest",
    "GetRpnStatusResponse",
    "GetServerBackupRequest",
    "GetServerDefaultPartitioningRequest",
    "GetServerInstallRequest",
    "GetServerRequest",
    "GetServiceRequest",
    "IPv6Block",
    "IPv6BlockApiCreateIPv6BlockRequest",
    "IPv6BlockApiCreateIPv6BlockSubnetRequest",
    "IPv6BlockApiDeleteIPv6BlockRequest",
    "IPv6BlockApiGetIPv6BlockQuotasRequest",
    "IPv6BlockApiGetIPv6BlockRequest",
    "IPv6BlockApiListIPv6BlockSubnetsAvailableRequest",
    "IPv6BlockApiUpdateIPv6BlockRequest",
    "InstallServerRequest",
    "Invoice",
    "ListFailoverIPsRequest",
    "ListFailoverIPsResponse",
    "ListIPv6BlockSubnetsAvailableResponse",
    "ListInvoicesResponse",
    "ListIpsResponse",
    "ListOSRequest",
    "ListOSResponse",
    "ListOffersRequest",
    "ListOffersResponse",
    "ListRefundsResponse",
    "ListRpnCapableSanServersResponse",
    "ListRpnCapableServersResponse",
    "ListRpnGroupMembersResponse",
    "ListRpnGroupsResponse",
    "ListRpnInvitesResponse",
    "ListRpnSansResponse",
    "ListRpnServerCapabilitiesResponse",
    "ListRpnV2CapableResourcesResponse",
    "ListRpnV2GroupLogsResponse",
    "ListRpnV2GroupsResponse",
    "ListRpnV2MembersResponse",
    "ListServerDisksRequest",
    "ListServerDisksResponse",
    "ListServerEventsRequest",
    "ListServerEventsResponse",
    "ListServersRequest",
    "ListServersResponse",
    "ListServicesRequest",
    "ListServicesResponse",
    "ListSubscribableServerOptionsRequest",
    "ListSubscribableServerOptionsResponse",
    "OfferFailoverBlockInfo",
    "OfferFailoverIpInfo",
    "OfferServerInfo",
    "OfferServiceLevelInfo",
    "Raid",
    "RebootServerRequest",
    "Refund",
    "Rescue",
    "RpnApiGetRpnStatusRequest",
    "RpnApiListRpnServerCapabilitiesRequest",
    "RpnSanApiAddIpRequest",
    "RpnSanApiCreateRpnSanRequest",
    "RpnSanApiDeleteRpnSanRequest",
    "RpnSanApiGetRpnSanRequest",
    "RpnSanApiListAvailableIpsRequest",
    "RpnSanApiListIpsRequest",
    "RpnSanApiListRpnSansRequest",
    "RpnSanApiRemoveIpRequest",
    "RpnV1ApiAcceptRpnInviteRequest",
    "RpnV1ApiAddRpnGroupMembersRequest",
    "RpnV1ApiCreateRpnGroupRequest",
    "RpnV1ApiDeleteRpnGroupMembersRequest",
    "RpnV1ApiDeleteRpnGroupRequest",
    "RpnV1ApiGetRpnGroupRequest",
    "RpnV1ApiLeaveRpnGroupRequest",
    "RpnV1ApiListRpnCapableSanServersRequest",
    "RpnV1ApiListRpnCapableServersRequest",
    "RpnV1ApiListRpnGroupMembersRequest",
    "RpnV1ApiListRpnGroupsRequest",
    "RpnV1ApiListRpnInvitesRequest",
    "RpnV1ApiRefuseRpnInviteRequest",
    "RpnV1ApiRpnGroupInviteRequest",
    "RpnV1ApiUpdateRpnGroupNameRequest",
    "RpnV2ApiAddRpnV2MembersRequest",
    "RpnV2ApiCreateRpnV2GroupRequest",
    "RpnV2ApiDeleteRpnV2GroupRequest",
    "RpnV2ApiDeleteRpnV2MembersRequest",
    "RpnV2ApiDisableRpnV2GroupCompatibilityRequest",
    "RpnV2ApiEnableRpnV2GroupCompatibilityRequest",
    "RpnV2ApiGetRpnV2GroupRequest",
    "RpnV2ApiListRpnV2CapableResourcesRequest",
    "RpnV2ApiListRpnV2GroupLogsRequest",
    "RpnV2ApiListRpnV2GroupsRequest",
    "RpnV2ApiListRpnV2MembersRequest",
    "RpnV2ApiUpdateRpnV2GroupNameRequest",
    "RpnV2ApiUpdateRpnV2VlanForMembersRequest",
    "ServerDefaultPartitioning",
    "ServerInstall",
    "StartBMCAccessRequest",
    "StartRescueRequest",
    "StartServerRequest",
    "StopBMCAccessRequest",
    "StopRescueRequest",
    "StopServerRequest",
    "SubscribeServerOptionRequest",
    "SubscribeStorageOptionsRequest",
    "SubscribeStorageOptionsResponse",
    "UpdateRaidRequest",
    "UpdateReverseRequest",
    "UpdateServerBackupRequest",
    "UpdateServerRequest",
    "UpdateServerTagsRequest",
    "DediboxV1API",
    "DediboxV1BillingAPI",
    "DediboxV1IPv6BlockAPI",
    "DediboxV1RpnAPI",
    "DediboxV1RpnSanAPI",
    "DediboxV1RpnV1API",
    "DediboxV1RpnV2API",
]
