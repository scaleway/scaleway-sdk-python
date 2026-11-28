import unittest
from importlib.metadata import requires

from packaging.requirements import Requirement


class TestDependencies(unittest.TestCase):
    def test_python_dateutil_allows_2_x(self) -> None:
        # botocore (boto3) requires python-dateutil<3, scaleway-core must stay installable next to it
        dateutil = next(
            req
            for req in map(Requirement, requires("scaleway-core") or [])
            if req.name == "python-dateutil"
        )
        self.assertIn("2.9.0.post0", dateutil.specifier)
