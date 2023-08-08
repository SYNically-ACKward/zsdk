from zsdk.api import Endpoint
from zsdk.utilities import snake_to_camel
from requests import Response
from typing import List, Optional


class departments(Endpoint):
    def list(
        self,
        search: Optional[str] = None,
        limit_search: Optional[bool] = False,
        page: Optional[int] = 1,
        page_size: Optional[int] = 100,
    ) -> List[dict]:
        """
        Method to retrieve a list of all configured departments.

        :param search: (str, optional) A search string to query
        :param page: (int, optional)
        :param page_size: (int, optional)
        :param limit_search: (bool, optinal) Used in conjunction with search to limit search only to department name
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/departments", params=params)

        return result.json()

    def get(self, dept_id: int) -> dict:
        """
        Method to retrieve information about a single department

        :param dept_id: (required, int) ID of the department to retrieve
        """
        result = self._req(method="get", path=f"/departments/{str(dept_id)}")
        return result.json()


class groups(Endpoint):
    def list(
        self,
        search: Optional[str] = None,
        page: Optional[int] = 1,
        page_size: Optional[int] = 100,
    ) -> List[dict]:
        """
        Method to retrieve a list of all configured groups.

        :param search: (str, optional) A search string to query
        :param page: (int, optional)
        :param page_size: (int, optional)
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/groups", params=params)

        return result.json()

    def get(self, group_id: int) -> dict:
        """
        Method to retrieve information about a single group

        :param group_id: (required, int) ID of the group to retrieve
        """
        result = self._req(method="get", path=f"/groups/{group_id}")
        return result.json()


class users(Endpoint):
    def list(
        self,
        name: Optional[str] = None,
        dept: Optional[str] = None,
        group: Optional[str] = None,
        page: Optional[int] = 1,
        page_size: Optional[int] = 100,
    ) -> List[dict]:
        """
        Retrieve a list of users based on search criteria.

        Parameters:
        - name (str): Filter results by user name
        - dept (str): Filter results by department name
        - group (str): Filter results by group name
        - page (int):
        - page_size (int):

        Returns:
        - List[dict]: A list of dictionaries representing users.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/users", params=params)

        return result.json()

    def get(self, user_id: int) -> dict:
        """
        Retrieve details of a specific user by its ID.

        Parameters:
        - user_id (int): The ID of the user to retrieve.

        Returns:
        - dict: A dictionary representing the details of the user.
        """
        result = self._req(method="get", path=f"/users/{user_id}")
        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Create a new user.

        Parameters:
        - payload (dict): A dictionary containing the details of the user to be created.
        The dictionary should have the following structure:
        {
            "name": str,              # Name of the user. (Required)
            "email": str,             # Email address of the user. (Required)
            "groups": List[Dict],     # List of groups the user belongs to. Each group has 'id', 'name', 'idpId', and 'comments'. (Required)
            "department": {           # Department details the user is associated with. Contains 'id', 'name', 'idpId', 'comments', and 'deleted'. (Required)
                "id": int,
                "name": str,
                "comments": str
            },
            "comments": str,          # Additional comments about the user.
            "tempAuthEmail": str,     # Temporary authorization email for the user.
            "password": str           # Password for the user. (Required)
        }

        Returns:
        - Response: A Response object containing the server's response to the creation request.
        """
        result = self._req(method="post", path="/users", json=payload)

        return result

    def update(self) -> Response:
        """
        Update an existing user.

        Parameters:
        - user_id (int): The ID of the user to update.
        - payload (dict): A dictionary containing the details of the user to be updated.
        The dictionary should have the following structure:
        {
            "name": str,              # Name of the user. (Required)
            "email": str,             # Email address of the user. (Required)
            "groups": [{
            "id": int,
            "name": str,
            "comments": str
            }],     # List of groups the user belongs to. Each group has 'id', 'name', and 'comments'. (Required)
            "department": {           # Department details the user is associated with. Contains 'id', 'name', 'idpId', 'comments', and 'deleted'. (Required)
                "id": int,
                "name": str,
                "comments": str
            },
            "comments": str,          # Additional comments about the user.
            "tempAuthEmail": str,     # Temporary authorization email for the user.
            "password": str           # Password for the user. (Required)
        }

        Returns:
        - Response: A Response object containing the server's response to the update request.
        """
        pass

    def delete(self, user_id: int) -> Response:
        """
        Delete a specific user by its ID.

        Parameters:
        - user_id (int): The ID of the user to delete.

        Returns:
        - Response: A Response object containing the server's response to the delete request.
        """
        result = self._req(method="delete", path=f"/users/{user_id}")

        return result

    def bulk_delete(self, ids: List[int]) -> dict:
        """
        Bulk delete users up to a maximum of 500 users per request.
        The response returns the user IDs that were successfully deleted.

        Parameters:
        - ids (List[int]): A list of user IDs to delete

        Returns:
        - Response: A Response object containing the server's response to the delete request.
        """
        body = {"ids": ids}

        result = self._req(method="post", path="/users/bulkDelete", json=body)

        return result.json()


class auditors(Endpoint):
    def list(self) -> List[dict]:
        """
        Retrieve a list of auditors.

        Returns:
        - List[dict]: A list of dictionaries representing auditors.
        """
        result = self._req(method="get", path="/users/auditors")

        return result.json()
