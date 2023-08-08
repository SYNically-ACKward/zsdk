from zsdk.api import Endpoint


class admin_users(Endpoint):
    def list(
        self,
        search: str = "",
        include_auditor_users: bool = False,
        include_admin_users: bool = True,
        page: int = 1,
        page_size: int = 100,
    ) -> list:
        """
        Method to list the currently configured Admin Users

        :param search: (str, optional) The search string used to partially match against an admin/auditor user's Login ID or Name.
        :param include_auditor_users: (bool, optional) Include or exclude auditor user information in the list.
        :param include_admin_users: (bool, optional) Include or exclude admin user information in the list.
        :param page: (int, optional) Specifies the page offset.
        :param page_size (int, optional) Specifies the page size. The default size is 100, but the maximum size is 1000.
        """
        parameters = {
            "includeAuditorUsers": include_auditor_users,
            "includeAdminUsers": include_admin_users,
            "search": search,
            "page": page,
            "pageSize": page_size,
        }
        result = self._req(
            method="get",
            path="/adminUsers",
            params=parameters,
        )
        return result.json()

    def create(
        self,
        payload: dict,
    ) -> dict:
        """
        Method to create a new Admin User

        :param payload: (dict) A dictionary containing the required attributes to create a new administrator.

        Example:
            payload = {
                        "loginName": "",
                        "userName": "",
                        "role": {
                            "id": 00000,
                            "name": "Super Admin"
                        },
                        "email": "",
                        "adminScopeType": "ORGANIZATION",
                        "isDefaultAdmin": False,
                        "isAuditor": False,
                        "password": "Zscaler!123",
                        "isPasswordLoginAllowed": True,
                        "isPasswordExpired": False,
                        "newLocationCreateAllowed": False,
                        "disabled": False,
                        "passwordLoginPermitted": "Yes"
                        }
        Notes:
            - At minimum the values for loginName, userName, email, adminScopeType and role:{"id":""} must be present
            - `loginName` should be a string containing the login ID of the administrator with FQDN such
                as `user@example.com`
            - `userName` should be a string containing the given name of the user such as `John Doe`
            - `role` should be a dictionary containing the keys `id` and `name` with the values appropriate
                to the organization
            - `email` should be a string containing the email address of the new administator
            - `adminScopeType` should be a string. Valid values are:
                - `ORGANIZATION`
                - `DEPARTMENT`
                - `LOCATION`
                - `LOCATION_GROUP`
            - `isDefaultAdmin` should be a boolean value set to False
            - `password` should be a plaintext string containing the password of the new administrator
            - `passwordLoginPermitted` should be a string with value `Yes` or `No`. This value should only be set
                to `No` if SAML Login is configured.
            - All remaining parameters are boolean values
        """
        result = self._req(
            method="post",
            path="/adminUsers",
            json=payload,
        )
        return result

    def update(
        self,
        payload: dict,
        user_id: int,
    ) -> dict:
        """
        Method to update an exisiting Admin User

        :param user_id: (int) User ID in form of integer. Can be retrieved via zia.admin_user.list
        :param payload: (dict) A dictionary containing the required attributes to create a new administrator.

        Example:
            payload = {
                        "loginName": "",
                        "userName": "",
                        "role": {
                            "id": 00000,
                            "name": "Super Admin"
                        },
                        "email": "",
                        "adminScopeType": "ORGANIZATION",
                        "isDefaultAdmin": False,
                        "isAuditor": False,
                        "password": "Zscaler!123",
                        "isPasswordLoginAllowed": True,
                        "isPasswordExpired": False,
                        "newLocationCreateAllowed": False,
                        "disabled": False,
                        "passwordLoginPermitted": "Yes"
                        }
        Notes:
            - At minimum the values for loginName, userName, email and role:{"id":""} must be present
            - `loginName` should be a string containing the login ID of the administrator with FQDN such
                as `user@example.com`
            - `userName` should be a string containing the given name of the user such as `John Doe`
            - `role` should be a dictionary containing the keys `id` and `name` with the values appropriate
                to the organization
            - `email` should be a string containing the email address of the new administator
            - `adminScopeType` should be a string. Valid values are:
                - `ORGANIZATION`
                - `DEPARTMENT`
                - `LOCATION`
                - `LOCATION_GROUP`
            - `isDefaultAdmin` should be a boolean value set to False
            - `password` should be a plaintext string containing the password of the new administrator
            - `passwordLoginPermitted` should be a string with value `Yes` or `No`. This value should only be set
                to `No` if SAML Login is configured.
            - All remaining parameters are boolean values
        """
        result = self._req(method="put", path=f"/adminUsers/{user_id}", json=payload)
        return result

    def delete(self, user_id: int) -> str:
        """
        Method to delete an Admin User

        :param user_id: (int) User ID in form of integer. Can be retrieved via zia.admin_user.list
        """
        result = self._req(method="delete", path=f"/adminUsers/{user_id}")
        return result
