from zsdk.api import Endpoint
from zsdk.utilities import snake_to_camel
from requests import Response
from typing import List, Optional


class locations(Endpoint):
    def list(
        self,
        search: Optional[str] = None,
        xff_enabled: Optional[bool] = None,
        auth_required: Optional[bool] = None,
        bw_enfoced: Optional[bool] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[dict]:
        """
        Gets locations only, not sub-locations.
        When a location matches the given search parameter criteria only its parent
        location is included in the result set, not its sub-locations.

        Parameters:
        - search (str): The search string used to partially match against a location's name and port attributes
        - xff_enabled (bool): Filter based on whether the Enforce XFF Forwarding setting is enabled for a location
        - auth_required (bool): Filter based on whether the Enforce Authentication setting is enabled for a location
        - bw_enforced (bool): Filter based on whether Bandwith Control is being enforced for a location
        - page (int): Specifies the page offset
        - page_size (int): Specifies the page size. The default size is 100, but the maximum size is 1000
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/locations", params=params)

        return result.json()

    def list_lite(
        self,
        include_sub_locations: Optional[bool] = None,
        include_parent_locations: Optional[bool] = None,
        search: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ):
        """
        Gets a name and ID dictionary of locations.

        Parameters:
        - include_sub_locations (bool): If set to true sub-locations are included in the response
        - include_parent_locations (bool): If set to true locations with sub locations are included in the response,
            otherwise only locations without sub-locations are included
        - search (str): The search string used to partially match against a location's name and port attributes.
        - page (int): Specifies the page offset.
        - page_size (int): Specifies the page size. The default size is 100, but the maximum size is 1000.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/locations/lite", params=params)

        return result.json()

    def get(self, location_id: int) -> dict:
        """
        Gets the location information for the specified ID

        Parameters:
        - location_id (int): The unique identifier for the location
        """
        result = self._req(method="get", path=f"/locations/{location_id}")

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Creates a new location.

        :param payload: Dictionary containing details of the location to be created.
            - `name` (str): Name of the location.
            - `parentId` (int): ID of the parent location.
            - `upBandwidth` (int): Upload bandwidth.
            - `dnBandwidth` (int): Download bandwidth.
            - `country` (str): Country of the location. Default is "NONE".
            - `tz` (str): Timezone. Default is "NOT_SPECIFIED".
            - `ipAddresses` (List[str]): List of IP addresses.
            - `ports` (List[int]): List of ports.
            - `vpnCredentials` (List[dict]): List of VPN credentials. Each credential has:
                - `type` (str): Type of credential (e.g., "CN").
                - `fqdn` (str): Fully Qualified Domain Name.
                - `ipAddress` (str): IP address.
                - `preSharedKey` (str): Pre-shared key for the VPN.
                - `comments` (str): Additional comments.
            - `authRequired` (bool): If authentication is required. Default is False.
            - `sslScanEnabled` (bool): If SSL scanning is enabled. Default is False.
            - `zappSSLScanEnabled` (bool): If Zapp SSL scanning is enabled. Default is False.
            - `xffForwardEnabled` (bool): If XFF forwarding is enabled. Default is False.
            - `otherSubLocation` (bool): Indicates other sub-location. Default is True.
            - `other6SubLocation` (bool): Indicates another sub-location for IPv6. Default is True.
            - `surrogateIP` (bool): If surrogate IP is enabled. Default is False.
            - `idleTimeInMinutes` (int): Idle timeout in minutes.
            - `displayTimeUnit` (str): Unit for displaying time. Default is "MINUTE".
            - `surrogateIPEnforcedForKnownBrowsers` (bool): If surrogate IP is enforced for known browsers. Default is False.
            - `surrogateRefreshTimeInMinutes` (int): Surrogate refresh time in minutes.
            - `surrogateRefreshTimeUnit` (str): Unit for surrogate refresh time. Default is "MINUTE".
            - `ofwEnabled` (bool): If OFW is enabled. Default is False.
            - `ipsControl` (bool): If IPS control is enabled. Default is False.
            - `aupEnabled` (bool): If AUP is enabled. Default is False.
            - `cautionEnabled` (bool): If caution is enabled. Default is False.
            - `aupBlockInternetUntilAccepted` (bool): If AUP blocks internet until accepted. Default is False.
            - `aupForceSslInspection` (bool): If AUP forces SSL inspection. Default is False.
            - `ipv6Enabled` (bool): If IPv6 is enabled. Default is True.
            - `ipv6Dns64Prefix` (str): IPv6 DNS 64 Prefix. Default is "TBD".
            - `aupTimeoutInDays` (int): AUP timeout in days.
            - `profile` (str): Profile type. Default is "NONE".
            - `description` (str): Description of the location.

        :return: Response object indicating the result of the creation request.
        """
        result = self._req(method="post", path="/locations", json=payload)

        return result

    def update(self, location_id: int, payload: dict) -> Response:
        """
        Updates an existing location.

        :param payload: Dictionary containing details of the location to be updated.
            - `name` (str): Name of the location.
            - `parentId` (int): ID of the parent location.
            - `upBandwidth` (int): Upload bandwidth.
            - `dnBandwidth` (int): Download bandwidth.
            - `country` (str): Country of the location. Default is "NONE".
            - `tz` (str): Timezone. Default is "NOT_SPECIFIED".
            - `ipAddresses` (List[str]): List of IP addresses.
            - `ports` (List[int]): List of ports.
            - `vpnCredentials` (List[dict]): List of VPN credentials. Each credential has:
                - `type` (str): Type of credential (e.g., "CN").
                - `fqdn` (str): Fully Qualified Domain Name.
                - `ipAddress` (str): IP address.
                - `preSharedKey` (str): Pre-shared key for the VPN.
                - `comments` (str): Additional comments.
            - `authRequired` (bool): If authentication is required. Default is False.
            - `sslScanEnabled` (bool): If SSL scanning is enabled. Default is False.
            - `zappSSLScanEnabled` (bool): If Zapp SSL scanning is enabled. Default is False.
            - `xffForwardEnabled` (bool): If XFF forwarding is enabled. Default is False.
            - `otherSubLocation` (bool): Indicates other sub-location. Default is True.
            - `other6SubLocation` (bool): Indicates another sub-location for IPv6. Default is True.
            - `surrogateIP` (bool): If surrogate IP is enabled. Default is False.
            - `idleTimeInMinutes` (int): Idle timeout in minutes.
            - `displayTimeUnit` (str): Unit for displaying time. Default is "MINUTE".
            - `surrogateIPEnforcedForKnownBrowsers` (bool): If surrogate IP is enforced for known browsers. Default is False.
            - `surrogateRefreshTimeInMinutes` (int): Surrogate refresh time in minutes.
            - `surrogateRefreshTimeUnit` (str): Unit for surrogate refresh time. Default is "MINUTE".
            - `ofwEnabled` (bool): If OFW is enabled. Default is False.
            - `ipsControl` (bool): If IPS control is enabled. Default is False.
            - `aupEnabled` (bool): If AUP is enabled. Default is False.
            - `cautionEnabled` (bool): If caution is enabled. Default is False.
            - `aupBlockInternetUntilAccepted` (bool): If AUP blocks internet until accepted. Default is False.
            - `aupForceSslInspection` (bool): If AUP forces SSL inspection. Default is False.
            - `ipv6Enabled` (bool): If IPv6 is enabled. Default is True.
            - `ipv6Dns64Prefix` (str): IPv6 DNS 64 Prefix. Default is "TBD".
            - `aupTimeoutInDays` (int): AUP timeout in days.
            - `profile` (str): Profile type. Default is "NONE".
            - `description` (str): Description of the location.

        :return: Response object indicating the result of the update request.
        """
        result = self._req(method="put", path=f"/locations/{location_id}", json=payload)

        return result

    def delete(self, location_id: int) -> Response:
        """
        Deletes the location or sub-location for the specified ID

        Parameters:
        - location_id (int): The unique identifier for the location
        """
        result = self._req(method="delete", path=f"/locations/{location_id}")

        return result

    def bulk_delete(self, ids: List[int]) -> list:
        """
        Bulk delete locations up to a maximum of 100 users per request.
        The response returns the location IDs that were successfully deleted.

        Parameters:
        - ids (List[int]): A list of IDs to be deleted
        """
        payload = {"ids": ids}

        result = self._req(method="post", path="/locations/bulkDelete", json=payload)

        return result.json()


class sublocations(Endpoint):
    def list(
        self,
        location_id: int,
        search: Optional[str] = None,
        xff_enabled: Optional[bool] = None,
        auth_required: Optional[bool] = None,
        bw_enfoced: Optional[bool] = None,
        enforce_aup: Optional[bool] = None,
        enable_firewall: Optional[bool] = None,
    ) -> List[dict]:
        """
        Gets information on sublocations.

        Parameters:
        - location_id (int): The unique identifier for the location
        - search (str): The search string used to partially match against a sub-location's name and port attributes
        - xff_enabled (bool): Filter based on whether the Enforce XFF Forwarding setting is enabled for a sub-location
        - auth_required (bool): Filter based on whether the Enforce Authentication setting is enabled for a sub-location
        - bw_enforced (bool): Filter based on whether Bandwith Control is being enforced for a sub-location
        - enforce_aup (bool): Filter based on whether Enforce AUP setting is enabled for a sub-location
        - enable_firewall (bool): Filter based on whether Enable Firewall setting is enabled for a sub-location
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self" or "location_id"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path=f"/locations/{location_id}/sublocations")

        return result.json()


class location_groups(Endpoint):
    def list(
        self,
        name: Optional[str] = None,
        group_type: Optional[str] = None,
        comments: Optional[str] = None,
        location_id: Optional[int] = None,
        last_mod_user: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[dict]:
        """
        Gets information on location groups.

        Parameters:
        - name (str): The location group's name
        - group_type (str): The location group's type (i.e., Static or Dynamic)
        - comments (str): Additional comments or information about the location group
        - location_id (int): The unique identifier for a location within a location group
        - last_mod_user (str): The admin who modified the location group last
        - page (int): Specifies the page offset
        - page_size (int): Specifies the page size. The default size is 100, but the maximum size is 1000
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/locations/groups", params=params)

        return result.json()

    def list_lite(
        self, page: Optional[int] = None, page_size: Optional[int] = None
    ) -> List[dict]:
        """
        Gets the name and ID dictionary of location groups

        Parameters:
        - page (int): Specifies the page offset
        - page_size (int): Specifies the page size. The default size is 100, but the maximum size is 1000
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/locations/groups/lite", params=params)

        return result.json()

    def count(
        self,
        last_mod_user: Optional[str] = None,
        name: Optional[str] = None,
        group_type: Optional[str] = None,
        comments: Optional[str] = None,
        location_id: Optional[int] = None,
    ):
        """
        Gets the list of location groups for your organization

        Parameters:
        - last_mod_user (str): The admin who modified the location group last
        - name (str): The location group's name
        - group_type (str): The location group's type (i.e., Static or Dynamic)
        - comments (str): Additional comments or information about the location group
        - location_id (int): The unique identifier for a location within a location group
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/locations/groups/count", params=params)

        return result.json()

    def get(self, group_id: int) -> dict:
        """
        Gets the location group for the specified ID

        Parameters:
        - group_id (int): The unique identifier for the location group
        """
        result = self._req(method="get", path=f"/locations/groups/{group_id}")

        return result.json()

    def get_lite(self, group_id: int) -> dict:
        """
        Gets the name and ID dictionary for the specified location group ID.
        The response only provides id, name, and deleted information.

        Parameters:
        - location_id (int): The unique identifier for the location group.
        """
        result = self._req(method="get", path=f"/locations/groups/lite/{group_id}")

        return result.json()
