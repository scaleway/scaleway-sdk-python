import logging
import os
from typing import Optional

import vcr
import inspect

PYTHON_UPDATE_CASSETTE = os.getenv("PYTHON_UPDATE_CASSETTE", "false").lower() in ("1", "true", "yes")

def func_path(function):
    path = os.path.join(os.path.dirname(inspect.getfile(function)), "cassettes")
    os.makedirs(path, exist_ok=True)
    filename = function.__name__ + ".cassette.yaml"
    return os.path.join(path, filename)

scw_vcr = vcr.VCR(
    record_mode="all" if PYTHON_UPDATE_CASSETTE else "none",
    filter_headers=["x-auth-token"],
    func_path_generator=func_path
)