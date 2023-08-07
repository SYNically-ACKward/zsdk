import json

import requests
import requests.exceptions

from zsdk.utilities import call


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
        result = call(
            session=self._session,
            method=method,
            url=f"{self._base_url}{path}",
            **kwargs,
        )
        try:
            return result
        except requests.exceptions.JSONDecodeError:
            return result
