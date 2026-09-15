# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from .types import (
    AlertRuleStatus,
    CustomAlertRuleStatus,
    RunStatus,
)

ALERT_RULE_TRANSIENT_STATUSES: list[AlertRuleStatus] = [
    AlertRuleStatus.ENABLING,
    AlertRuleStatus.DISABLING,
]
"""
Lists transient statutes of the enum :class:`AlertRuleStatus <AlertRuleStatus>`.
"""
CUSTOM_ALERT_RULE_TRANSIENT_STATUSES: list[CustomAlertRuleStatus] = [
    CustomAlertRuleStatus.ENABLING,
    CustomAlertRuleStatus.DISABLING,
]
"""
Lists transient statutes of the enum :class:`CustomAlertRuleStatus <CustomAlertRuleStatus>`.
"""
RUN_TRANSIENT_STATUSES: list[RunStatus] = [
    RunStatus.INTERRUPTING,
    RunStatus.PAUSING,
]
"""
Lists transient statutes of the enum :class:`RunStatus <RunStatus>`.
"""
