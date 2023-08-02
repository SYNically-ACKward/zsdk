import json

import requests
import requests.exceptions

from zsdk.utilities import _request


class Endpoint:
    def __init__(
        self,
        session: requests.Session,
        base_url: str,
        **kwargs,
    ):
        self._session = session
        self._base_url = base_url

    def _req(
        self,
        method: str,
        path: str = None,
        **kwargs,
    ) -> json or str:
        result = _request(
            session=self._session,
            method=method,
            url=f"{self._base_url}{path}",
            **kwargs,
        )
        try:
            return result.json()
        except requests.exceptions.JSONDecodeError:
            return result.text
