import os
from typing import Coroutine, Generator, Any, Optional

import vcr
import inspect

from vcr.cassette import CassetteContextDecorator

PYTHON_UPDATE_CASSETTE = os.getenv("PYTHON_UPDATE_CASSETTE", "false").lower() in ("1", "true", "yes")

class ScwVCR(vcr.VCR):
    def use_cassette(self, path: Optional[str] = None, **kwargs):
        caller_file = inspect.stack()[1].filename
        cassette_dir = os.path.join(os.path.dirname(caller_file), "cassettes")
        os.makedirs(cassette_dir, exist_ok=True)

        if path is None:
            caller_name = os.path.splitext(os.path.basename(caller_file))[0]
            path = f"{caller_name}.yaml"

        full_path = os.path.join(cassette_dir, path)
        return super().use_cassette(full_path, **kwargs)


scw_vcr = ScwVCR(
    record_mode="all" if PYTHON_UPDATE_CASSETTE else "none",
    filter_headers=["x-auth-token"],
)