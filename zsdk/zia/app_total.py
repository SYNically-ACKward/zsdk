from zsdk.api import Endpoint
from requests import Response
from typing import Optional


class app_total(Endpoint):
    def get(self, app_id: str, verbose: Optional[bool] = False) -> dict:
        """
        Searches the AppTotal App Catalog by app ID. If the app exists in the catalog, the app's information is returned
            If not, the app is submitted for analysis. After analysis is complete, a subsequent GET request is required
            to fetch the app's information.

        Parameters:
        - app_id (required, str): The app identifier (e.g., OAuth client ID).
        - verbose (bool): Return a verbose report including potentially heavy artifacts. Default = False
        """
        params = {"app_id": app_id, "verbose": verbose}

        result = self._req(method="get", path="/apps/app", params=params)

        return result.json()

    def analyze(self, app_id: str) -> Response:
        """
        Submits an application for analysis in the AppTotal Sandbox.
            After analysis is complete, a subsequent GET request is required to fetch the app's information.

        Parameters:
        - app_id (required, str): A string representation of the app ID for submission
        """
        payload = {"appId": app_id}

        result = self._req(method="post", path="/apps/app", json=payload)

        return result
