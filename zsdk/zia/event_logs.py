from zsdk.api import Endpoint
from zsdk.utilities import snake_to_camel
from requests import Response
from typing import List, Optional
import csv


class event_logs(Endpoint):
    def status(self) -> dict:
        """
        Gets the status of the request to generate an event log report.
        """
        result = self._req(method="get", path="/eventlogEntryReport")

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Creates an event log report for the specified time period.

        Parameters: A dictionary containing the details of the event log to be created
        - payload (dict):
        The dictionary should have the following structure:
        {
            "startTime": int,           # The timestamp in epoch to start the event log (Required)
            "endTime": int,             # The timestamp in epoch to stop the event log (Required)
            "category": str,            # The category of event for which to output the event log (Required)
            "subcategories": List[str]  # Filters the list based on areas within a category
            "actionResult": str,        # Filters the list based on the outcome
            "message": str,             # The search string used to match against the event log message.
            "errorCode": str,           # The search string used to match against the error code in event log entries
            "statusCode": str           # The search string used to match against the status code in event log entries
        }
        """
        result = self._req(method="post", path="/eventlogEntryReport", json=payload)

        return result

    def delete(self) -> Response:
        """
        Cancels the request to generate an event log report.
        """
        result = self._req(method="delete", path="/eventlogEntryReport")

        return result

    def download(self) -> csv:
        """
        Downloads the most recently generated event log report.
        Calling this endpoint downloads the file only if the report generation status is COMPLETE.
        The report status can be retrieved using the STATUS method.
        """
        result = self._req(method="get", path="/eventlogEntryReport/download")

        return result.content.decode("utf-8")
