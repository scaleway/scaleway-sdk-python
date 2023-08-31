from __future__ import annotations


from scaleway_core.profile import Profile
from scaleway_core.validations.string_validation import (
    is_access_key,
    is_organization_id,
    is_project_id,
    is_region,
    is_secret_key,
    is_url,
    is_zone,
)


class Client(Profile):
    _request_count: int = 1

    @staticmethod
    def from_profile(profile: Profile) -> Client:
        return Client(**profile.__dict__)

    def _increment_request_count(self) -> int:
        current = self._request_count
        self._request_count += 1
        return current

    def validate(self) -> bool:
        return self.validate_credentials() and self.validate_settings()

    def validate_credentials(self) -> bool:
        if not self.access_key or not self.secret_key:
            raise ValueError(
                "Invalid secrets, access_key & secret_key must be defined. See https://www.scaleway.com/docs/console/my-project/how-to/generate-api-key"
            )

        if not is_access_key(self.access_key):
            raise ValueError(
                f"Invalid access key format '{self.access_key}', expected SCWXXXXXXXXXXXXXXXXX format. See https://www.scaleway.com/docs/console/my-project/how-to/generate-api-key"
            )

        if not is_secret_key(self.secret_key):
            raise ValueError(
                f"Invalid secret key format '{self.secret_key}', expected a UUID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. See https://www.scaleway.com/docs/console/my-project/how-to/generate-api-key"
            )

        return True

    def validate_settings(self) -> bool:
        if self.default_organization_id is not None:
            if not self.default_organization_id:
                raise ValueError("Default organization ID cannot be empty")

            if not is_organization_id(self.default_organization_id):
                raise ValueError(
                    f"Invalid organization ID format '${self.default_organization_id}', expected a UUID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                )

        if self.default_project_id is not None:
            if not self.default_project_id:
                raise ValueError("Default project ID cannot be empty")

            if not is_project_id(self.default_project_id):
                raise ValueError(
                    f"Invalid project ID format '${self.default_project_id}', expected a UUID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                )

        if self.default_region is not None:
            if not self.default_region:
                raise ValueError("Default region cannot be empty")

            if not is_region(self.default_region):
                raise ValueError(
                    f"Invalid default region format '{self.default_region}'"
                )

        if self.default_zone is not None:
            if not self.default_zone:
                raise ValueError("Default zone cannot be empty")

            if not is_zone(self.default_zone):
                raise ValueError(f"Invalid default zone format '{self.default_zone}'")

        if not is_url(self.api_url):
            raise ValueError(f"Invalid URL '{self.api_url}'")

        if self.api_url[-1] == "/":
            raise ValueError(
                f"Invalid URL ${self.api_url}: it should not have a trailing slash"
            )

        if self.default_page_size is not None:
            if self.default_page_size < 1:
                raise ValueError(
                    f"Invalid defaultPageSize {self.default_page_size}: it should be a number above 0"
                )

        return True
