from zsdk.api import Endpoint
from typing import List, Optional


class user_authentication_settings(Endpoint):
    def list(self) -> dict:
        """
        Gets a list of URLs that were exempted from cookie authentication.
        """
        result = self._req(method="get", path="/authSettings/exemptedUrls")

        return result.json()

    def update(
        self, action: Optional[str] = "ADD_TO_LIST", urls: List[str] = []
    ) -> dict:
        """
        Adds a URL to or removes a URL from the cookie authentication exempt list.
            To add a URL to the list, set the action parameter to ADD_TO_LIST.
            To remove a URL, set action to REMOVE_FROM_LIST.

        Parameters:
        - action (str): Valid values: "ADD_TO_LIST", "REMOVE_FROM_LIST". Default = "ADD_TO_LIST"
        - urls (List[str]): A list of strings representing URLs. Default = []
        """
        payload = {"urls": urls}

        params = {"action": action}

        result = self._req(
            method="post",
            path="/authSettings/exemptedUrls",
            params=params,
            json=payload,
        )

        return result.json()
