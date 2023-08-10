from zsdk.api import Endpoint
from zsdk.utilities import snake_to_camel
from requests import Response
from typing import List, Optional


class allowlist(Endpoint):
    def list(self):
        """
        Gets a list of URLs that are on the allowlist.
        """
        result = self._req(method="get", path="/security")

        return result.json()

    def update(self, url_list: List[str] = []) -> Response:
        """
        Updates the list of URLs on the allowlist.
        This will overwrite a previously-generated allowlist.
        If you need to completely erase the allowlist, submit an empty list.

        Parameters:
        - url_list (list): list of URLs for the allowlist
        """
        payload = {"whitelistUrls": url_list}

        result = self._req(method="put", path="/security", json=payload)

        return result


class denylist(Endpoint):
    def list(self):
        """
        Gets a list of URLs that are on the denylist
        """
        result = self._req(method="get", path="/security/advanced")

        return result.json()

    def update(self, url_list: List[str]) -> Response:
        """
        Updates the list of URLs on the denylist.
        This will overwrite a previously-generated denylist.
        If you need to completely erase the denylist, submit an empty list.

        Parameters:
        - url_list (list): list of URLs for the allowlist
        """
        payload = {"blacklistUrls": url_list}

        result = self._req(method="put", path="/security", json=payload)

        return result


class blacklist(Endpoint):
    def update(self, action: str = "ADD_TO_LIST", url_list: List[str] = []) -> Response:
        """
        Adds a URL to or removes a URL from the denylist.
        To add a URL to the denylist, set the action parameter to ADD_TO_LIST.
        To remove a URL, set action to REMOVE_FROM_LIST.

        Parameters:
        - action (str): Valid actions: "ADD_TO_LIST", "REMOVE_FROM_LIST". Default "ADD_TO_LIST"
        - url_list (list): list of URLs for the allowlist
        """
        payload = {"blacklistUrls": url_list}
        params = {"action": action}

        result = self._req(
            method="post",
            path="/security/advanced/blacklistUrls",
            params=params,
            json=payload,
        )

        return result
