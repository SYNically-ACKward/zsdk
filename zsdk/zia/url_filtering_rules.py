from zsdk.api import Endpoint
from requests import Response
from typing import List


class url_filtering_rules(Endpoint):
    def list(self) -> List[dict]:
        """
        Gets a list of all of URL Filtering Policy rules.
        """
        result = self._req(method="get", path="/urlFilteringRules")

        return result.json()

    def get(self, rule_id: int) -> dict:
        """
        Gets the URL Filtering Policy rule for the specified ID.

        Parameters:
        - rule_id (int): The unique identifier for the URL Filtering Policy rule.
        """
        result = self._req(method="get", path=f"/urlFilteringRules/{rule_id}")

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Adds a URL Filtering Policy rule.

        Parameters:
        - payload (dict): The URL filtering rule information.

        Example:
            payload = {
                "name": "string",
                "order": 0,
                "protocols": [
                    "string"
                ],
                "locations": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "groups": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "departments": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "users": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "urlCategories": [
                    "string"
                ],
                "state": "string",
                "timeWindows": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "rank": 0,
                "requestMethods": [
                    "string"
                ],
                "endUserNotificationUrl": "string",
                "overrideUsers": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "overrideGroups": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "blockOverride": bool,
                "timeQuota": 0,
                "sizeQuota": 0,
                "description": "string",
                "locationGroups": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "labels": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "validityStartTime": 0,
                "validityEndTime": 0,
                "validityTimeZoneId": "string",
                "lastModifiedTime": 0,
                "lastModifiedBy": {
                    "id": 0,
                    "extensions": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    }
                },
                "enforceTimeValidity": bool,
                "devices": [
                    {
                    "id": 0,
                    "extensions": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    }
                    }
                ],
                "deviceGroups": [
                    {
                    "id": 0,
                    "extensions": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    }
                    }
                ],
                "deviceTrustLevels": [
                    "string"
                ],
                "action": "string",
                "ciparule": bool
                }
        """
        result = self._req(method="post", path="/urlFilteringRules", json=payload)

        return result

    def update(self, rule_id: int, payload: dict) -> Response:
        """
        Adds a URL Filtering Policy rule.

        Parameters:
        - rule_id (int): The unique identifier of the URL Filtering Rule
        - payload (dict): The URL filtering rule information.

        Example:
            payload = {
                "name": "string",
                "order": 0,
                "protocols": [
                    "string"
                ],
                "locations": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "groups": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "departments": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "users": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "urlCategories": [
                    "string"
                ],
                "state": "string",
                "timeWindows": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "rank": 0,
                "requestMethods": [
                    "string"
                ],
                "endUserNotificationUrl": "string",
                "overrideUsers": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "overrideGroups": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "blockOverride": bool,
                "timeQuota": 0,
                "sizeQuota": 0,
                "description": "string",
                "locationGroups": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "labels": [
                    {
                        "id": 0,
                        "extensions": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        }
                    }
                ],
                "validityStartTime": 0,
                "validityEndTime": 0,
                "validityTimeZoneId": "string",
                "lastModifiedTime": 0,
                "lastModifiedBy": {
                    "id": 0,
                    "extensions": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    }
                },
                "enforceTimeValidity": bool,
                "devices": [
                    {
                    "id": 0,
                    "extensions": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    }
                    }
                ],
                "deviceGroups": [
                    {
                    "id": 0,
                    "extensions": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    }
                    }
                ],
                "deviceTrustLevels": [
                    "string"
                ],
                "action": "string",
                "ciparule": bool
                }
        """
        result = self._req(
            method="put", path=f"/urlFilteringRules/{rule_id}", json=payload
        )

        return result

    def delete(self, rule_id: int) -> Response:
        """
        Deletes the URL Filtering Policy rule for the specified ID.

        Parameters:
        - rule_id (int): The unique identifier of the URL Filtering Rule
        """
        result = self._req(
            method="delete",
            path=f"/urlFilteringRules/{rule_id}",
        )

        return result
