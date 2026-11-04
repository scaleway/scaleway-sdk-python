# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    BMCAccessStatus,
    IPv6BlockDelegationStatus,
    RpnGroupMemberStatus,
    RpnSanStatus,
    RpnV2GroupStatus,
    RpnV2MemberStatus,
    ServerInstallStatus,
    ServerStatus,
    ServiceProvisioningStatus,
)

BMC_ACCESS_TRANSIENT_STATUSES: list[BMCAccessStatus] = [
    BMCAccessStatus.CREATING,
    BMCAccessStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`BMCAccessStatus <BMCAccessStatus>`.
"""
I_PV6_BLOCK_DELEGATION_TRANSIENT_STATUSES: list[IPv6BlockDelegationStatus] = [
    IPv6BlockDelegationStatus.UPDATING,
]
"""
Lists transient statutes of the enum :class:`IPv6BlockDelegationStatus <IPv6BlockDelegationStatus>`.
"""
RPN_GROUP_MEMBER_TRANSIENT_STATUSES: list[RpnGroupMemberStatus] = [
    RpnGroupMemberStatus.CREATING,
    RpnGroupMemberStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`RpnGroupMemberStatus <RpnGroupMemberStatus>`.
"""
RPN_SAN_TRANSIENT_STATUSES: list[RpnSanStatus] = [
    RpnSanStatus.CREATING,
    RpnSanStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`RpnSanStatus <RpnSanStatus>`.
"""
RPN_V2_GROUP_TRANSIENT_STATUSES: list[RpnV2GroupStatus] = [
    RpnV2GroupStatus.CREATING,
    RpnV2GroupStatus.UPDATING,
    RpnV2GroupStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`RpnV2GroupStatus <RpnV2GroupStatus>`.
"""
RPN_V2_MEMBER_TRANSIENT_STATUSES: list[RpnV2MemberStatus] = [
    RpnV2MemberStatus.CREATING,
    RpnV2MemberStatus.UPDATING,
    RpnV2MemberStatus.DELETING,
]
"""
Lists transient statutes of the enum :class:`RpnV2MemberStatus <RpnV2MemberStatus>`.
"""
SERVER_INSTALL_TRANSIENT_STATUSES: list[ServerInstallStatus] = [
    ServerInstallStatus.BOOTING,
    ServerInstallStatus.SETTING_UP_RAID,
    ServerInstallStatus.PARTITIONING,
    ServerInstallStatus.FORMATTING,
    ServerInstallStatus.INSTALLING,
    ServerInstallStatus.CONFIGURING,
    ServerInstallStatus.CONFIGURING_BOOTLOADER,
    ServerInstallStatus.REBOOTING,
]
"""
Lists transient statutes of the enum :class:`ServerInstallStatus <ServerInstallStatus>`.
"""
SERVER_TRANSIENT_STATUSES: list[ServerStatus] = [
    ServerStatus.DELIVERING,
    ServerStatus.INSTALLING,
]
"""
Lists transient statutes of the enum :class:`ServerStatus <ServerStatus>`.
"""
SERVICE_PROVISIONING_TRANSIENT_STATUSES: list[ServiceProvisioningStatus] = [
    ServiceProvisioningStatus.DELIVERING,
    ServiceProvisioningStatus.EXPIRING,
]
"""
Lists transient statutes of the enum :class:`ServiceProvisioningStatus <ServiceProvisioningStatus>`.
"""
