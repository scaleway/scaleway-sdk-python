import os
import json
from pathlib import Path
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

import vcr
import inspect

PYTHON_UPDATE_CASSETTE = os.getenv("PYTHON_UPDATE_CASSETTE", "false").lower() in (
    "1",
    "true",
    "yes",
)

CI = os.getenv("CI", "false").lower() in (
    "1",
    "true",
    "yes",
)

REPLACE = "11111111-1111-1111-1111-111111111111"


def func_path(function):
    path = Path(Path(inspect.getfile(function)).parent, "cassettes")
    Path.mkdir(path, exist_ok=True)
    filename = function.__name__ + ".cassette.yaml"
    return Path(path, filename)


def scrub_data(data):
    if isinstance(data, dict):
        return {
            k: REPLACE
            if k in ("organization", "project", "organization_id", "project_id")
            else scrub_data(v)
            for k, v in data.items()
        }

    if isinstance(data, list):
        return [scrub_data(item) for item in data]

    return data


def scrub_string():
    def before_record_response(response):
        body_bytes = response["body"]["string"]

        if isinstance(body_bytes, bytes):
            body_str = body_bytes.decode("utf-8")
        else:
            body_str = str(body_bytes)

        body_str = body_str.strip()
        if not body_str or not (body_str.startswith("{") or body_str.startswith("[")):
            return response

        data = json.loads(body_str)

        data = scrub_data(data)

        response["body"]["string"] = json.dumps(data).encode("utf-8")

        return response

    return before_record_response


def scrub_uri():
    def before_record_request(request):
        request_bytes = request.body
        if isinstance(request_bytes, bytes):
            request_str = request_bytes.decode("utf-8")
        else:
            request_str = str(request_bytes)
        request_bytes = request_bytes.strip()
        if not request_bytes or not (
            request_str.startswith("{") or request_str.startswith("[")
        ):
            return request
        data = json.loads(request_str)
        data = scrub_data(data)
        request.body = json.dumps(data).encode("utf-8")
        index_orga_id = request.uri.rfind("?organization_id=")
        index_project_id = request.uri.rfind("&project_id=")
        index_orga = request.uri.rfind("?organization=")
        index_project = request.uri.rfind("&project=")
        uri = request.uri
        parsed = urlparse(uri)
        query = parse_qs(parsed.query)

        if index_orga_id != -1:
            query["organization_id"] = ["11111111-1111-1111-1111-111111111111"]

        if index_project_id != -1:
            query["project_id"] = ["11111111-1111-1111-1111-111111111111"]

        if index_orga != -1:
            query["organization"] = ["11111111-1111-1111-1111-111111111111"]

        if index_project != -1:
            query["project"] = ["11111111-1111-1111-1111-111111111111"]

        new_query = urlencode(query, doseq=True)
        uri = urlunparse(parsed._replace(query=new_query))

        request.uri = uri
        return request

    return before_record_request


scw_vcr = vcr.VCR(
    record_mode="all" if PYTHON_UPDATE_CASSETTE else "none",
    filter_headers=[
        "x-auth-token",
        "link",
        "Accept-Encoding",
        "Connection",
        "Content-Type",
        "accept",
    ],
    func_path_generator=func_path,
    before_record_response=scrub_string(),
    before_record_request=scrub_uri(),
)
