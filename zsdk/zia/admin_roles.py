from zsdk.api import Endpoint
from zsdk.utilities import snake_to_camel
from requests import Response
from typing import List, Optional


class admin_roles(Endpoint):
    def list(
        self,
        include_auditor_role: bool = False,
        include_partner_role: bool = False,
        include_api_role: bool = False,
    ) -> list:
        """
        Method to list the available Admin Roles

        :param include_auditor_role: (bool, optional) Include Auditor roles in output. Defaults to False.
        :param include_partner_role: (bool, optional) Include Partner roles in output. Defaults to False.
        :param include_api_role: (bool, optional) Include API roles in output. Defaults to False.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}
        result = self._req(method="get", path="/adminRoles/lite", params=params)
        return result.json()
