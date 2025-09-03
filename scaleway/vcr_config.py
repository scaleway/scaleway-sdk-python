import os
import json
import inspect
from pathlib import Path
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

import vcr

# -------------------------------------------------------------------
# Environment flags
# -------------------------------------------------------------------
PYTHON_UPDATE_CASSETTE = os.getenv("PYTHON_UPDATE_CASSETTE", "false").lower() in (
    "1",
    "true",
    "yes",
)
REPLAY_CASSETTES = os.getenv("CI", "false").lower() in ("1", "true", "yes")

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
REPLACE = "11111111-1111-1111-1111-111111111111"
FILTER_HEADERS = {
    "x-auth-token",
    "link",
    "accept-encoding",
    "connection",
    "content-type",
    "accept",
    "content-security-policy",
    "x-content-type-options",
    "x-frame-options",
    "strict-transport-security",
}
SCRUB_KEYS = {"organization", "project", "organization_id", "project_id"}


def func_path(function) -> Path:
    path = Path(inspect.getfile(function)).parent / "cassettes"
    path.mkdir(exist_ok=True)
    return path / f"{function.__name__}.cassette.yaml"


def scrub_data(data):
    if isinstance(data, dict):
        return {
            k: REPLACE if k in SCRUB_KEYS else scrub_data(v) for k, v in data.items()
        }
    if isinstance(data, list):
        return [scrub_data(item) for item in data]
    return data


def scrub_json_string(raw: bytes | str) -> bytes | str:
    if isinstance(raw, bytes):
        raw = raw.decode("utf-8")

    raw = raw.strip()
    if not raw or not (raw.startswith("{") or raw.startswith("[")):
        return raw

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return raw

    return json.dumps(scrub_data(data))


def scrub_response_body(response):
    body = response["body"]["string"]
    response["body"]["string"] = scrub_json_string(body).encode("utf-8")
    return response


def scrub_response_headers(response):
    response["headers"] = {
        k: v for k, v in response["headers"].items() if k.lower() not in FILTER_HEADERS
    }
    return response


def scrub_request(request):
    body = request.body
    if body:
        scrubbed = scrub_json_string(body)
        if isinstance(scrubbed, str):
            scrubbed = scrubbed.encode("utf-8")
        request.body = scrubbed

    parsed = urlparse(request.uri)
    query = parse_qs(parsed.query)

    for key in SCRUB_KEYS:
        if key in query:
            query[key] = [REPLACE]

    request.uri = urlunparse(parsed._replace(query=urlencode(query, doseq=True)))
    return request


def scrub_response(response):
    response = scrub_response_body(response)
    return scrub_response_headers(response)


scw_vcr = vcr.VCR(
    record_mode="all" if PYTHON_UPDATE_CASSETTE else "none",
    filter_headers=list(FILTER_HEADERS),
    func_path_generator=func_path,
    before_record_request=scrub_request,
    before_record_response=scrub_response,
)
