from zsdk.api import Endpoint
from requests import Response


class sandbox_settings(Endpoint):
    def list(self) -> list:
        """
        Gets the custom list of MD5 file hashes that are blocked by Sandbox
        """
        result = self._req(method="get", path="/behavioralAnalysisAdvancedSettings")

        return result.json()

    def update(self, hashes_to_block: list) -> Response:
        """
        Updates the custom list of MD5 file hashes that are blocked by Sandbox.
        This overwrites a previously generated blocklist.
        If you need to completely erase the blocklist, submit an empty list.

        Parameters:
        - hashes_to_block (List[str]): A list of strings of MD5 file hashes to block
        """
        payload = {"fileHashesToBeBlocked": hashes_to_block}

        result = self._req(
            method="put", path="/behavioralAnalysisAdvancedSettings", json=payload
        )

        return result

    def count(self) -> dict:
        """
        Gets the used and unused quota for blocking MD5 file hashes with Sandbox
        """
        result = self._req(
            method="get", path="/behavioralAnalysisAdvancedSettings/fileHashCount"
        )

        return result.json()
