from zsdk.api import Endpoint
from zsdk.logger import StructuredLogger as logger
from requests import Response


class sandbox_submission(Endpoint):  # TODO: COMPLETE
    def submit(self, file_path: str, api_token: str, force: str = "0") -> Response:
        """
        Submit a file to the Zscaler Sandbox

        Parameters:
        - file_path (str): Path to the file for submission
        - api_token (str): The Sandbox Submission API token generated by the API Key Management page ZIA Admin Portal.
        - force (str): Submit file to sandbox even if found malicious during AV scan and a verdict already exists.
            Available values "0", "1" as strings
        """
        params = {"api_token": api_token, "force": force}
        with open(file_path, "rb") as file:
            files = {"file": (file_path.split("/")[-1], file)}

        result = self._req(
            method="post", path="/zscsb/submit", params=params, files=files
        )

        return result
