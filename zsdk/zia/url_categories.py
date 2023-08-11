from zsdk.api import Endpoint
from zsdk.utilities import snake_to_camel
from requests import Response
from typing import List, Optional


class url_categories(Endpoint):
    def list(
        self,
        custom_only: Optional[bool] = None,
        include_only_url_keyword_counts: Optional[bool] = False,
    ) -> List[dict]:
        """
        Gets information about all or custom URL categories. By default, the response includes keywords.

        Parameters:
        - custom_only (bool): If set to true, gets information on custom URL categories only.
        - include_only_url_keyword_counts (bool): By default this parameter is set to false,
            so the response includes URLs and keywords for custom URL categories only.
            If set to true, the response only includes URL and keyword counts.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/urlCategories", params=params)

        return result.json()

    def list_lite(self) -> List[dict]:
        """
        Gets a lightweight key-value list of all or custom URL categories.
        """
        result = self._req(method="get", path="/urlCategories/lite")

        return result.json()

    def get(self, category_id: str) -> dict:
        """
        Gets the URL category information for the specified ID.

        Parameters:
        - category_id (str): The unique identifier for the URL category.
        """
        result = self._req(method="get", path=f"/urlCategories/{category_id}")

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Adds a new custom URL category. If keywords are included within the request, they are added to the new category.

        Parameters:
        - payload (dict): The details for the custom URL category.
            {
                "configuredName": "str",
                "superCategory": "str",
                "keywords": ["str", ...],
                "keywordsRetainingParentCategory": ["str", ...],
                "urls": ["str", ...],
                "dbCategorizedUrls": ["str", ...],
                "ipRanges": ["str", ...],
                "ipRangesRetainingParentCategory": ["str", ...],
                "customCategory": bool,
                "scopes": [
                    {
                        "scopeGroupMemberEntities": [
                            {
                                "id": int,
                                "extensions": {
                                    "additionalProp1": "str",
                                    "additionalProp2": "str",
                                    "additionalProp3": "str"
                                }
                            },
                            ...
                        ],
                        "Type": "str",
                        "ScopeEntities": [
                            {
                                "id": int,
                                "extensions": {
                                    "additionalProp1": "str",
                                    "additionalProp2": "str",
                                    "additionalProp3": "str"
                                }
                            },
                            ...
                        ]
                    },
                    ...
                ],
                "editable": bool,
                "description": "str",
                "type": "str",
                "urlKeywordCounts": {
                    "totalUrlCount": int,
                    "retainParentUrlCount": int,
                    "totalKeywordCount": int,
                    "retainParentKeywordCount": int
                },
                "customUrlsCount": int,
                "urlsRetainingParentCategoryCount": int,
                "customIpRangesCount": int,
                "ipRangesRetainingParentCategoryCount": int
            }
        """
        result = self._req(method="post", path="/urlCategories", json=payload)

        return result

    def update(self, category_id: str, payload: dict) -> Response:
        """
        Updates a URL category. If keywords are included within the request, they are added to the new category.

        Parameters:
        - payload (dict): The details for the custom URL category.
            {
                "configuredName": "str",
                "superCategory": "str",
                "keywords": ["str", ...],
                "keywordsRetainingParentCategory": ["str", ...],
                "urls": ["str", ...],
                "dbCategorizedUrls": ["str", ...],
                "ipRanges": ["str", ...],
                "ipRangesRetainingParentCategory": ["str", ...],
                "customCategory": bool,
                "scopes": [
                    {
                        "scopeGroupMemberEntities": [
                            {
                                "id": int,
                                "extensions": {
                                    "additionalProp1": "str",
                                    "additionalProp2": "str",
                                    "additionalProp3": "str"
                                }
                            },
                            ...
                        ],
                        "Type": "str",
                        "ScopeEntities": [
                            {
                                "id": int,
                                "extensions": {
                                    "additionalProp1": "str",
                                    "additionalProp2": "str",
                                    "additionalProp3": "str"
                                }
                            },
                            ...
                        ]
                    },
                    ...
                ],
                "editable": bool,
                "description": "str",
                "type": "str",
                "urlKeywordCounts": {
                    "totalUrlCount": int,
                    "retainParentUrlCount": int,
                    "totalKeywordCount": int,
                    "retainParentKeywordCount": int
                },
                "customUrlsCount": int,
                "urlsRetainingParentCategoryCount": int,
                "customIpRangesCount": int,
                "ipRangesRetainingParentCategoryCount": int
            }
        """
        result = self._req(
            method="post", path=f"/urlCategories/{category_id}", json=payload
        )

        return result

    def delete(self, category_id: str) -> Response:
        """
        Deletes the custom URL category for the specified ID.

        Parameters:
        - category_id (str): The unique identifer for the custom URL category.
        """
        result = self._req(method="delete", path=f"/urlCategories/{category_id}")

        return result

    def get_quota(self) -> dict:
        """
        Gets information on the number of unique URLs that are currently provisioned
            for your organization as well as how many URLs you can add before reaching that number.
        """
        result = self._req(method="get", path="/urlCategories/urlQuota")

        return result.json()

    def lookup(self, lookup_list: List[str]) -> List[dict]:
        """
        Look up the categorization of the given set of URLs, e.g., ['abc.com', 'xyz.com'].
            Up to 100 URLs can be looked up per request, and a URL cannot exceed 1024 characters.
        """
        result = self._req(method="post", path="/urlLookup", json=lookup_list)

        return result.json()
