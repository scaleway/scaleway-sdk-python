from typing import Dict, Optional


def project_or_organization_id(
    organization_id: Optional[str],
    project_id: Optional[str],
    default_project_id: Optional[str],
) -> Dict[str, str]:
    if project_id is not None:
        return {
            "project_id": project_id,
        }

    if organization_id is not None:
        return {
            "organization_id": organization_id,
        }

    if default_project_id is not None:
        return {
            "project_id": default_project_id,
        }

    raise ValueError("You must provide either a project_id or an organization_id")
