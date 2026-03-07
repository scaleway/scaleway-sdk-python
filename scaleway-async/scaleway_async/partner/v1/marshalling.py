# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    OrganizationLockedBy,
    OrganizationStatus,
    Organization,
    ListOrganizationsResponse,
    CreateOrganizationRequest,
    RequestAdminRoleRequest,
    UpdateOrganizationRequest,
)


def unmarshal_Organization(data: Any) -> Organization:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Organization' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("email", None)
    if field is not None:
        args["email"] = field
    else:
        args["email"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = OrganizationStatus.UNKNOWN_STATUS

    field = data.get("owner_firstname", None)
    if field is not None:
        args["owner_firstname"] = field
    else:
        args["owner_firstname"] = None

    field = data.get("owner_lastname", None)
    if field is not None:
        args["owner_lastname"] = field
    else:
        args["owner_lastname"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("phone_number", None)
    if field is not None:
        args["phone_number"] = field
    else:
        args["phone_number"] = None

    field = data.get("siren_number", None)
    if field is not None:
        args["siren_number"] = field
    else:
        args["siren_number"] = None

    field = data.get("customer_id", None)
    if field is not None:
        args["customer_id"] = field
    else:
        args["customer_id"] = None

    field = data.get("lock_reason_message", None)
    if field is not None:
        args["lock_reason_message"] = field
    else:
        args["lock_reason_message"] = None

    field = data.get("locked_by", None)
    if field is not None:
        args["locked_by"] = field
    else:
        args["locked_by"] = OrganizationLockedBy.UNKNOWN_LOCKED_BY

    field = data.get("comment", None)
    if field is not None:
        args["comment"] = field
    else:
        args["comment"] = None

    field = data.get("locked_at", None)
    if field is not None:
        args["locked_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["locked_at"] = None

    field = data.get("picture_link", None)
    if field is not None:
        args["picture_link"] = field
    else:
        args["picture_link"] = None

    return Organization(**args)


def unmarshal_ListOrganizationsResponse(data: Any) -> ListOrganizationsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOrganizationsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("organizations", None)
    if field is not None:
        args["organizations"] = (
            [unmarshal_Organization(v) for v in field] if field is not None else None
        )
    else:
        args["organizations"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListOrganizationsResponse(**args)


def marshal_CreateOrganizationRequest(
    request: CreateOrganizationRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.partner_id is not None:
        output["partner_id"] = request.partner_id

    if request.email is not None:
        output["email"] = request.email

    if request.organization_name is not None:
        output["organization_name"] = request.organization_name

    if request.owner_firstname is not None:
        output["owner_firstname"] = request.owner_firstname

    if request.owner_lastname is not None:
        output["owner_lastname"] = request.owner_lastname

    if request.customer_id is not None:
        output["customer_id"] = request.customer_id

    if request.phone_number is not None:
        output["phone_number"] = request.phone_number

    if request.siren_number is not None:
        output["siren_number"] = request.siren_number

    return output


def marshal_RequestAdminRoleRequest(
    request: RequestAdminRoleRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username

    if request.email is not None:
        output["email"] = request.email

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_UpdateOrganizationRequest(
    request: UpdateOrganizationRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email

    if request.name is not None:
        output["name"] = request.name

    if request.owner_firstname is not None:
        output["owner_firstname"] = request.owner_firstname

    if request.owner_lastname is not None:
        output["owner_lastname"] = request.owner_lastname

    if request.phone_number is not None:
        output["phone_number"] = request.phone_number

    if request.customer_id is not None:
        output["customer_id"] = request.customer_id

    if request.comment is not None:
        output["comment"] = request.comment

    return output
