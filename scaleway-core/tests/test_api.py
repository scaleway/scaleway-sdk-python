import unittest
import uuid
from unittest import mock

from requests.models import Response

from scaleway_core.api import API, ScalewayException, ValidationError
from scaleway_core.client import Client


def _response(status_code: int, body: bytes) -> Response:
    response = Response()
    response.status_code = status_code
    response._content = body
    return response


def _api() -> API:
    client = Client(
        access_key="SCW" + "A" * 17,
        secret_key=str(uuid.uuid4()),
    )
    return API(client)


class TestThrowOnError(unittest.TestCase):
    def test_non_json_error_raises_scaleway_exception_with_raw_body(self):
        response = _response(502, b"<html>Bad Gateway</html>")

        with self.assertRaises(ScalewayException) as context:
            _api()._throw_on_error(response)

        self.assertEqual(context.exception.status_code, 502)
        self.assertIn("<html>Bad Gateway</html>", str(context.exception))

    def test_json_error_raises_scaleway_exception(self):
        response = _response(500, b'{"message": "boom"}')

        with self.assertRaises(ScalewayException):
            _api()._throw_on_error(response)

    def test_validation_error_raises_validation_error(self):
        response = _response(
            400,
            b'{"message": "Validation Error", "fields": {"name": "required"}}',
        )

        with self.assertRaises(ValidationError) as context:
            _api()._throw_on_error(response)

        self.assertEqual(context.exception.errors, {"name": "required"})


class TestRequest(unittest.TestCase):
    def test_total_count_header_is_injected_as_int(self):
        response = _response(200, b'{"servers": []}')
        response.headers["X-Total-Count"] = "3"

        with mock.patch("scaleway_core.api.requests.request", return_value=response):
            res = _api()._request("GET", "/instance/v1/zones/fr-par-1/servers")

        self.assertEqual(res.json(), {"servers": [], "total_count": 3})
