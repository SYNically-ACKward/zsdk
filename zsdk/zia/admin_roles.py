from zsdk.api import Endpoint


class admin_roles(Endpoint):
    def list(
            self,
            include_auditor_role: bool = False,
            include_partner_role: bool = False,
            include_api_role: bool = False
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
        result = self._req(method="get", path="/adminRoles", params=parameters)
        return result

    def create(
               self,
               payload: dict,
               ) -> dict:
        """
        Method to create new Admin Roles

        :param payload: (dict) A dictionary containing the required attributes to create a new administrator role.

        Example:
            payload = {
                        "rank": 7,
                        "logsLimit": "UNRESTRICTED",
                        "name": "",
                        "policyAccess": "READ_WRITE",
                        "dashboardAccess": "READ_WRITE",
                        "reportAccess": "READ_WRITE",
                        "analysisAccess": "READ_ONLY",
                        "alertingAccess": "READ_WRITE",
                        "usernameAccess": "READ_ONLY",
                        "deviceInfoAccess": "READ_ONLY",
                        "adminAcctAccess": "READ_WRITE",
                        "isAuditor": False,
                        "permissions": [
                            "ADVANCED_SETTINGS",
                            "COMPLY",
                            "FIREWALL_DNS",
                            "NSS_CONFIGURATION",
                            "SECURE",
                            "SSL_POLICY",
                            "VZEN_CONFIGURATION",
                            "PARTNER_INTEGRATION",
                            "REMOTE_ASSISTANCE_MANAGEMENT",
                            "LOCATIONS",
                            "VPN_CREDENTIALS",
                            "HOSTED_PAC_FILES",
                            "EZ_AGENT_CONFIGURATIONS",
                            "SECURE_AGENT_NOTIFICATIONS",
                            "PROXY_GATEWAY",
                            "STATIC_IPS",
                            "GRE_TUNNELS",
                            "SUBCLOUDS",
                            "AUTHENTICATION_SETTINGS",
                            "USER_MANAGEMENT",
                            "IDENTITY_PROXY_SETTINGS",
                            "APIKEY_MANAGEMENT",
                            "POLICY_RESOURCE_MANAGEMENT",
                            "CLIENT_CONNECTOR_PORTAL",
                            "CUSTOM_URL_CAT",
                            "OVERRIDE_EXISTING_CAT",
                            "TENANT_PROFILE_MANAGEMENT"
                        ],
                        "isNonEditable": False
                        }
        Notes:
            - `rank` should be defined as an integer between 0 and 7
            - `permissions` should be passed as a list containing the applicable configuration area permissions for
                the admin role
            - `isNonEditable` and `isAuditor` should be set as boolean values
            - `name` should be passed as a string
            - All remaining parameters should be passed as a string containing either ["READ_WRITE", "READ_ONLY"]
        """
        result = self._req(method="post", path="/adminRoles", json=payload)
        return result

    def delete(
               self,
               role_id: int,
               ) -> str:
        """
        Method to delete a given Admin Role

        :param role_id: (int) Integer ID of the Admin Role to delete.
        """
        result = self._req(
            method="delete",
            path=f"/adminRoles/{role_id}",
        )
        return result
