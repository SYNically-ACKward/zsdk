from zsdk.api import Endpoint
from zsdk.utilities import snake_to_camel
from requests import Response
from typing import List, Optional


class rule_labels(Endpoint):
    def list(
        self, page: Optional[int] = None, page_size: Optional[int] = None
    ) -> List[dict]:
        """
        Gets a list of rule labels.

        Parameters:
        - page (int): Specifies the page offset.
        - page_size (int): Specifies the page size. The default size is 100, but the maximum size is 1000
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/ruleLabels", params=params)

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Adds a rule label.

        Parameters:
        - payload (dict): A dictionary containing the information for the label to be created
        The dictionary should have the following structure:
        {
            "name": str,               # Name of the rule label.
            "description": str         # Description of the rule label.
        }
        """
        result = self._req(method="post", path="ruleLabels", json=payload)

        return result

    def get(self, label_id: int) -> dict:
        """
        Gets rule label information for the specified ID.

        Parameters:
        - label_id (int): The unique identifier for the rule label
        """
        result = self._req(method="get", path=f"/ruleLabels/{label_id}")

        return result

    def update(self, label_id: int, payload: dict) -> Response:
        """
        Updates rule label information for the specified ID.

        Parameters:
        - label_id (int): The unique identifier for the rule label
        - payload (dict): A dictionary containing the information for the label to be updated
        The dictionary should have the following structure:
        {
            "name": str,               # Name of the rule label.
            "description": str         # Description of the rule label.
        }
        """
        result = self._req(method="put", path=f"/ruleLabels/{label_id}", json=payload)

        return result

    def delete(self, label_id: int) -> Response:
        """
        Deletes the rule label for the specified ID
        Parameters:
        - label_id (int): The unique identifier for the rule label
        """
        result = self._req(method="delete", path=f"/ruleLabels/{label_id}")

        return result
