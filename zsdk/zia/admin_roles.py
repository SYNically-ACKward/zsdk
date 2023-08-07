from zsdk.api import Endpoint


class admin_roles(Endpoint):
    def list(
        self,
        include_auditor_role: bool = False,
        include_partner_role: bool = False,
        include_api_role: bool = False,
    ) -> list:
        """
        Method to list the available Admin Roles

        :param includeAuditorRole: (bool, optional) Include Auditor roles in output. Defaults to False.
        :param includePartnerRole: (bool, optional) Include Partner roles in output. Defaults to False.
        :param includeApiRole: (bool, optional) Include API roles in output. Defaults to False.
        """
        parameters = {
            "includeAuditorRole": include_auditor_role,
            "includePartnerRole": include_partner_role,
            "includeApiRole": include_api_role,
        }
        result = self._req(method="get", path="/adminRoles/lite", params=parameters)
        return result.json()
