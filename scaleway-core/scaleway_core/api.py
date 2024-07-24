import json
import logging
from dataclasses import dataclass
from typing import IO, Any, Dict, Iterable, List, Mapping, Optional, Tuple, Union

import requests
from requests import Response

from .client import Client

Body = Union[
    str, bytes, Mapping[str, Any], Iterable[Tuple[str, Optional[str]]], IO[Any]
]

Params = Mapping[str, Any]


@dataclass
class APILogger:
    logger: logging.Logger

    identifier: int

    def log_request(
        self,
        method: str,
        url: str,
        params: List[Tuple[str, Any]],
        headers: Dict[str, str],
        body: Optional[str],
    ) -> None:
        if not self.logger.isEnabledFor(logging.DEBUG):
            return

        raw_params = "&".join([f"{k}={v}" for (k, v) in params])

        debug_headers = {
            **headers,
            "x-auth-token": "*****",
        }

        title = (
            f"--------------- Scaleway SDK REQUEST {self.identifier} ---------------\n"
        )

        log = f"{title}\n"
        log += f"{method} {url}?{raw_params}\n"

        for k, v in debug_headers.items():
            log += f"{k}: {v}\n"

        if body is not None:
            log += "\n"
            log += body
            log += "\n"

        log += "-" * len(title)

        self.logger.debug(log)

    def log_response(
        self,
        response: requests.Response,
    ) -> None:
        if not self.logger.isEnabledFor(logging.DEBUG):
            return

        title = (
            f"--------------- Scaleway SDK RESPONSE {self.identifier} ---------------"
        )
        ok = "OK" if response.ok else "NOK"

        log = f"{title}\n"
        log += f"HTTP {response.status_code} {ok}\n"

        for k, v in response.headers.items():
            log += f"{k}: {v}\n"

        if response.text:
            log += f"\n{response.text}\n"

        log += "-" * len(title)

        self.logger.debug(log)


@dataclass
class ScalewayException(Exception):
    response: Response

    @property
    def status_code(self) -> int:
        return self.response.status_code

    def __str__(self) -> str:
        return self.response.text


@dataclass
class ValidationError(ScalewayException):
    errors: Dict[str, str]


class API:
    def __init__(self, client: Client, *, bypass_validation: bool = False):
        if not bypass_validation:
            client.validate()

        self.client = client
        self._log = logging.getLogger("scaleway")

    def _request(
        self,
        method: str,
        path: str,
        params: Params = {},
        headers: Dict[str, str] = {},
        body: Optional[Body] = None,
    ) -> requests.Response:
        additional_headers: Dict[str, str] = {}
        method = method.upper()
        if method == "POST" or method == "PUT" or method == "PATCH":
            additional_headers["Content-Type"] = "application/json; charset=utf-8"

            if body is None:
                body = {}

        raw_body = json.dumps(body) if body is not None else None

        request_params: List[Tuple[str, Any]] = []
        for k, v in params.items():
            if v is None:
                continue

            if isinstance(v, list):
                for item in v:
                    request_params.append((k, item))
            else:
                request_params.append((k, v))

        headers = {
            "accept": "application/json",
            "user-agent": self.client.user_agent,
            **additional_headers,
            **headers,
        }
        if self.client.secret_key is not None:
            headers["x-auth-token"] = self.client.secret_key
        url = f"{self.client.api_url}{path}"

        logger = APILogger(self._log, self.client._increment_request_count())

        logger.log_request(
            method=method,
            url=url,
            params=request_params,
            headers=headers,
            body=raw_body,
        )

        response = requests.request(
            method=method,
            url=url,
            params=request_params,
            headers=headers,
            data=raw_body,
            verify=not self.client.api_allow_insecure,
        )

        if response.headers.get("x-total-count"):
            b = response.json()
            b["total_count"] = response.headers.get("x-total-count")
            b = json.dumps(b)
            response._content = bytes(b, "utf-8")

        logger.log_response(
            response=response,
        )

        return response

    def _throw_on_error(self, res: requests.Response) -> None:
        if res.status_code >= 400:
            data = res.json()

            if data:
                if "message" in data:
                    message = data["message"]

                    if message == "Validation Error":
                        raise ValidationError(res, data["fields"])

                    raise ScalewayException(res)

                raise ScalewayException(res)

            raise ScalewayException(res)
