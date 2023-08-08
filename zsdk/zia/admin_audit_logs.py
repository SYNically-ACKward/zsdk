from zsdk.api import Endpoint
from requests import Response
import csv

actions = [
    "ACTIVATE",
    "ALERT",
    "AUDIT_OPERATION",
    "AUTO_IR",
    "CHANGE_DEPLOYED_PAC_VERSION",
    "CONTAIN_DEVICE",
    "CREATE",
    "CREATE_NEW_PAC_VERSION",
    "DELETE",
    "DELETE_PAC",
    "DELETE_PAC_VERSION",
    "DOWNLOAD",
    "FORCED_ACTIVATE",
    "IMPORT",
    "ISOLATE",
    "KILL_CURRENT_EXECUTION",
    "PATCH",
    "QUARANTINE",
    "REMEDIATE",
    "REPORT",
    "SIGN_IN",
    "SIGN_OUT",
    "STAGE_PAC_VERSION",
    "UPDATE",
]


class admin_audit_logs(Endpoint):
    def status(self) -> dict:
        """
        Gets the status of a request for an audit log report.
        After sending a POST request to /auditlogEntryReport to generate a report, you can continue to call GET
        /auditlogEntryReport to check whether the report has finished generating.
        Once the status is COMPLETE, you can send another GET request to /auditlogEntryReport/download
        to download the report as a CSV file.
        """
        response = self._req(method="get", path="/auditlogEntryReport")
        return response.json()

    def create(
        self,
        start_time: int,
        end_time: int,
        action_types: list = actions,
        category: str = None,
        subcategories: list = None,
        action_result: str = None,
        action_interface: str = None,
        object_name: str = None,
        client_ip: str = None,
        admin_name: str = None,
    ) -> Response:
        """
        Creates an audit log report for the specified time period and saves it as a CSV file.
        The report includes audit information for every call made to the cloud service API during
        the specified time period.
        Creating a new audit log report will overwrite a previously-generated report.
        :param start_time: (int, required) The timestamp in epoch to start the audit log
        :param end_time: (int, required) The timestamp in epoch to end the audit log
        :param action_types: (list, optional) A list of action types to include in the audit log. Defaults to ALL
        :param category: (str, optional) A string containing the category of action to include in the audit log
        :param subcategories: (list, optional) A list of subcategories to include in the audit log
        :param action_result: (str, optional) A string of the action result type to include in the audit log
        :param action_interface: (str, optional) A string indicating the admin interface to include in the audit log
        :param object_name: (str, optional)
        :param client_ip: (str, optional) The source IP Address to include in the audit log
        :param admin_name: (str, optional) A string of the admin username to include in the audit log

        """
        data = {
            "startTime": start_time,
            "endTime": end_time,
            "actionTypes": action_types,
            "category": category,
            "subcategories": subcategories,
            "actionResult": action_result,
            "actionInterface": action_interface,
            "objectName": object_name,
            "clientIP": client_ip,
            "adminName": admin_name,
        }

        keys_to_remove = [k for k, v in data.items() if v is None]
        for k in keys_to_remove:
            del data[k]

        result = self._req(method="post", path="/auditlogEntryReport", json=data)

        return result

    def delete(self) -> Response:
        """
        Cancels the request to create an audit log report.
        """
        result = self._req(method="delete", path="/auditlogEntryReport")

        return result

    def download(self) -> csv:
        """
        Downloads the most recently created audit log report.
        After a call to GET /auditlogEntryReport indicates that the report (CSV file)
        was generated, you can send a GET request to /auditlogEntryReport/download to download the file.
        """
        result = self._req(method="get", path="/auditlogEntryReport/download")
        return result.content.decode("utf-8")
