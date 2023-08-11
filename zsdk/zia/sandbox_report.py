from zsdk.api import Endpoint


class sandbox_report_quota(Endpoint):
    def get(self) -> dict:
        """
        The resource access quota for retrieving Sandbox Detail Reports is restricted to 1000 requests per day,
        with a rate limit of 2/sec and 1000/hour.
        Use this method to retrieve details regarding your organization's daily Sandbox API resource usage
        """
        result = self._req(method="get", path="/sandbox/report/quota")

        return result.json()


class sandbox_report_file(Endpoint):
    def get(self, md5_hash: str, details: str = "full") -> dict:
        """
        Gets a full (i.e., complete) or summary detail report for an MD5 hash of a file that was analyzed by Sandbox.

        Parameters:
        - md5_hash (str): MD5 hash of the file that was analyzed by Sandbox.
        - details (str): Type of report. Valid options are 'full' or 'summary'. Default is 'full'.
        """
        params = {"details": details}

        result = self._req(
            method="get", path=f"/sandbox/report/{md5_hash}", params=params
        )

        return result.json()
