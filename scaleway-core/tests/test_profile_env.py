import logging
import os
import sys
import unittest
import uuid
from unittest import mock

import utils

from scaleway_core.profile import Profile

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class TestProfileEnv(unittest.TestCase):
    def setUp(self) -> None:
        self.profile_config = Profile(
            access_key=utils.random_access_key(),
            secret_key=str(uuid.uuid4()),
            default_organization_id=str(uuid.uuid4()),
            default_project_id=str(uuid.uuid4()),
            default_region="fr-par",
            default_zone="fr-par-1",
            api_url="https://example.com",
        )

    def test_load_profile_from_env(self) -> None:
        with mock.patch.dict(
            os.environ,
            {
                "SCW_ACCESS_KEY": self.profile_config.access_key,
                "SCW_SECRET_KEY": self.profile_config.secret_key,
                "SCW_DEFAULT_ORGANIZATION_ID": self.profile_config.default_organization_id,
                "SCW_DEFAULT_PROJECT_ID": self.profile_config.default_project_id,
                "SCW_DEFAULT_REGION": self.profile_config.default_region,
                "SCW_DEFAULT_ZONE": self.profile_config.default_zone,
                "SCW_API_URL": self.profile_config.api_url,
            },
        ):
            profile = Profile.from_env()
            self.assertEqual(profile, self.profile_config)
