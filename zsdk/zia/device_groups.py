from zsdk.api import Endpoint
from zsdk.utilities import snake_to_camel
from requests import Response
from typing import List, Optional


class device_groups(Endpoint):
    def list(
        self,
        include_device_info: Optional[bool] = None,
        include_pseudo_groups: Optional[bool] = None,
    ) -> List[dict]:
        """
        Gets a list of device groups.

        Parameters:
        - include_device_info (bool): Include or exclude device information.
        - include_pseudo_groups (bool): Include or exclude Zscaler Client Connector and Cloud Browser Isolation-related device groups.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/deviceGroups", params=params)

        return result.json()


class devices(Endpoint):
    def list(
        self,
        name: Optional[str] = None,
        model: Optional[str] = None,
        owner: Optional[str] = None,
        os_type: Optional[str] = None,
        os_version: Optional[str] = None,
        device_group_id: Optional[int] = None,
        user_ids: Optional[List[int]] = None,
        search_all: Optional[str] = None,
        include_all: Optional[bool] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[dict]:
        """
        Gets a list of devices. Any given search parameters are applied during device search.
        Search parameters are based on device name, model, owner, OS type, and OS version.
        The devices listed can also be restricted to return information only for ones belonging to specific users.

        Parameters:
        - name (str): The device group name.
        - model (str): The device models.
        - owner (str): The device owners.
        - os_type (str): The device's operating system.
            Valid values: ["ANY", "OTHER_OS", "IOS", "ANDROID_OS", "WINDOWS_OS", "MAC_OS", "LINUX"]
        - os_version (str): The device's operating system version.
        - device_group_id (int): The unique identifier for the device group.
        - user_ids (List[int]): Used to list devices for specific users.
        - search_all (str): Used to match against all device attribute information
        - include_all (bool): Used to include or exclude Cloud Browser Isolation devices.
        - page (int): Specifies the page offset.
        - page_size (int): Specifies the page size. The default size is 100, but the maximum size is 1000.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {
            snake_to_camel(key): value
            for key, value in params.items()
            if key != "search_all"
        }

        result = self._req(method="get", path="/deviceGroups/devices", params=params)

        return result.json()

    def list_lite(
        self,
        name: Optional[str] = None,
        user_ids: Optional[List[int]] = None,
        include_all: Optional[bool] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[dict]:
        """
        Gets a list of devices that includes device ID, name, and owner name.
        Any given search parameters are applied during device search.
        Search parameters are based on device or user name and owner.
        The devices listed can also be restricted to return information only for ones belonging to specific users.

        Parameters:
        - name (str): The device group name.
        - user_ids (List[int]): Used to list devices for specific users.
        - include_all (bool): Used to include or exclude Cloud Browser Isolation devices.
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

        result = self._req(
            method="get", path="/deviceGroups/devices/lite", params=params
        )

        return result.json()
