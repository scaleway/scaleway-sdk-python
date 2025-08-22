import os
from pathlib import Path

import vcr
import inspect

PYTHON_UPDATE_CASSETTE = os.getenv("PYTHON_UPDATE_CASSETTE", "false").lower() in ("1", "true", "yes")

def func_path(function):
    path = Path(Path(inspect.getfile(function)).parent, "cassettes")
    Path.mkdir(path, exist_ok=True)
    filename = function.__name__ + ".cassette.yaml"
    return Path(path, filename)

scw_vcr = vcr.VCR(
    record_mode="all" if PYTHON_UPDATE_CASSETTE else "none",
    filter_headers=["x-auth-token"],
    func_path_generator=func_path
)