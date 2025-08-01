import pytest


@pytest.fixture(scope="session")
def vcr_config():
    return {
        # Replace the Authorization request header with "DUMMY" in cassettes
        "filter_headers": ["x-auth-token"],
    }
