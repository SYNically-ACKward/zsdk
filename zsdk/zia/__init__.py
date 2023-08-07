import json
import time

import requests
from requests import Response

from zsdk.logger import setup_logger
from zsdk.utilities import call

from .admin_roles import admin_roles
from .admin_users import admin_users
from .admin_audit_logs import admin_audit_logs

logger = setup_logger(name=__name__)


def _obfuscate_api_key(seed: str) -> list:
    now = int(time.time() * 1000)
    n = str(now)[-6:]
    r = str(int(n) >> 1).zfill(6)
    key = "".join(seed[int(digit)] for digit in n)
    key += "".join(seed[int(digit) + 2] for digit in r)
    return str(now), str(key)


class zia:
    def __init__(
        self,
        username: str,
        password: str,
        api_key: str,
        cloud_name: str,
    ):
        self._session = requests.Session()
        self.username = username
        self.password = password
        self.api_key = api_key
        self.cloud_name = cloud_name
        self._base_url = f"https://zsapi.{self.cloud_name}/api/v1"
        self._authenticate()

    def _authenticate(
        self,
    ) -> Response:
        now, key = _obfuscate_api_key(self.api_key)
        result = call(
            session=self._session,
            method="post",
            url=f"{self._base_url}/authenticatedSession",
            json={
                "apiKey": key,
                "username": self.username,
                "password": self.password,
                "timestamp": now,
            },
        )
        logger.debug(result)
        return result

    def activate_changes(
        self,
    ) -> Response:
        result = call(
            session=self._session,
            method="post",
            url=f"{self._base_url}/status/activate",
        )

        return result

    @property
    def admin_roles(self) -> admin_roles:
        return admin_roles(
            session=self._session,
            base_url=self._base_url,
        )

    @property
    def admin_users(self) -> admin_users:
        return admin_users(
            session=self._session,
            base_url=self._base_url,
        )

    @property
    def admin_audit_logs(self) -> admin_audit_logs:
        return admin_audit_logs(
            session=self._session,
            base_url=self._base_url,
        )
