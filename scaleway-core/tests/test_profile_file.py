import logging
import os
import sys
import tempfile
import unittest
import uuid

import utils

from scaleway_core.profile import Profile

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class TestProfileFile(unittest.TestCase):
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

        self.demo_profile_config = Profile(**self.profile_config.__dict__)
        self.demo_profile_config.access_key = utils.random_access_key()
        self.demo_profile_config.secret_key = str(uuid.uuid4())

        config = f"\
access_key: {self.profile_config.access_key}\n\
secret_key: {self.profile_config.secret_key}\n\
default_organization_id: {self.profile_config.default_organization_id}\n\
default_project_id: {self.profile_config.default_project_id}\n\
default_region: {self.profile_config.default_region}\n\
default_zone: {self.profile_config.default_zone}\n\
api_url: {self.profile_config.api_url}\n\
\n\
profiles:\n\
  demo:\n\
    access_key: {self.demo_profile_config.access_key}\n\
    secret_key: {self.demo_profile_config.secret_key}\n\
        ".strip()

        fp = tempfile.NamedTemporaryFile(
            delete=False,
            prefix="scaleway-sdk-python-profile-",
            suffix=".yaml",
        )
        self.profile_file_name = fp.name
        fp.write(config.encode())
        fp.close()

    def tearDown(self) -> None:
        os.unlink(self.profile_file_name)

    def test_load_profile_from_config_file(self) -> None:
        profile = Profile.from_config_file(self.profile_file_name)
        self.assertEqual(profile, self.profile_config)

    def test_load_profile_from_config_file_with_profile(self) -> None:
        profile = Profile.from_config_file(self.profile_file_name, "demo")
        self.assertEqual(profile, self.demo_profile_config)
