from zsdk.api import Endpoint
from zsdk.utilities import snake_to_camel
from requests import Response
from typing import List, Optional


class firewall_filtering_rules(Endpoint):
    def list(
        self,
    ) -> list:
        """
        Method to list all currently configured Firewall Filtering Rules.
        """
        result = self._req(method="get", path="/firewallFilteringRules")

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Creates a new firewall filtering rule with the given payload.

        :param payload: A dictionary containing the details of the new rule.
                        The required fields are 'name', 'order' and 'action'.
                        See the API documentation for the full list of available fields.
        :type payload: dict

        :return: A Response object representing the API response.
        :rtype: Response
        """
        result = self._req(method="post", path="/firewallFilteringRules", json=payload)
        return result

    def get(self, rule_id: int):
        """
        Method to retrieve a single firewall filtering rule.

        :param rule_id: An integer representing the ID of the desired rule.
        :type rule_id: int

        :return: A dictionary representation of the firewall filtering rule.
        :rtype: dict
        """
        result = self._req(method="get", path=f"/firewallFilteringRules/{rule_id}")

        return result.json()

    def update(
        self, rule_id: int, payload: dict
    ) -> Response:  # TODO: ID Required payload keys
        """
        Method to update a single firewall filtering rule.

        :param payload: A dictionary containing the details of the updated rule.
                The required field is 'name'.
                See the API documentation for the full list of available fields.
        :type payload: dict

        :return: A Response object representing the API response.
        :rtype: Response
        """
        result = self._req(
            method="put", path=f"/firewallFilteringRules/{rule_id}", json=payload
        )

        return result

    def delete(self, rule_id: int) -> Response:
        """
        Method to delete a single firewall filtering rule.

        :param rule_id: An integer representing the ID of the desired rule.
        :type rule_id: int
        """
        result = self._req(method="delete", path=f"/firewallFilteringRules/{rule_id}")

        return result


class ip_destination_groups(Endpoint):
    def list(self, exclude_type: str = None) -> list:
        """
        Retrieve a list of configured IP Destination Groups.

        Parameters:
        - exclude_type (str, optional): A string identifying a destination group type to exclude.
        Possible values include: "DSTN_IP", "DSTN_FQDN", "DSTN_DOMAIN", "DSTN_OTHER".

        Returns:
        - Response: A Response object containing the list of IP Destination Groups.
        """
        if exclude_type is None:
            result = self._req(method="get", path="/ipDestinationGroups")
        else:
            parameters = {"excludeType": exclude_type}
            result = self._req(
                method="get", path="/ipDestinationGroups", params=parameters
            )

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Create a new IP Destination Group.

        Sends a POST request to create a new IP Destination Group based on the provided payload.

        Parameters:
        - payload (dict): A dictionary containing the details of the IP Destination Group to be created.
        The dictionary can contain the following keys:
            - name (str): Name of the IP Destination Group.
            - type (str): Type of IP Destination Group, expected to be "DSTN_IP".
            - addresses (list of str): List of IP addresses associated with the group.
            - description (str): Description of the IP Destination Group.
            - ipCategories (list of str): Categories of IP addresses (e.g., "ANY").
            - countries (list of str): Countries associated with the IP addresses.
            - isNonEditable (bool): Flag indicating if the IP Destination Group is editable.

        Returns:
        - Response: A Response object containing the server's response to the request.

        Example:
        ```python
        group_payload = {
            "name": "Test IP Group",
            "type": "DSTN_IP",
            "addresses": ["192.168.1.1"]
        }
        response = obj.create_ip_destination_group(group_payload)
        ```
        """
        result = self._req(method="post", path="/ipDestinationGroups", json=payload)

        return result

    def get(self, group_id: int) -> dict:
        """
        Retrieve details of an IP Destination Group based on its ID.

        Parameters:
        - group_id (int): The ID of the IP Destination Group to retrieve.

        Returns:
        - Response: A Response object containing the details of the IP Destination Group.
        """
        result = self._req(method="get", path=f"/ipDestinationGroups/{group_id}")

        return result.json()

    def update(self, group_id: int, payload: dict) -> Response:
        """
        Update an existing IP Destination Group.

        Sends a PUT request to update the details of an IP Destination Group based on the provided payload.

        Parameters:
        - group_id (int): The ID of the IP Destination Group to update.
        - payload (dict): A dictionary containing the updated details of the IP Destination Group.

        Returns:
        - Response: A Response object containing the server's response to the update request.
        """
        result = self._req(
            method="put", path=f"/ipDestinationGroups/{group_id}", json=payload
        )

        return result

    def delete(self, group_id: int) -> Response:
        """
        Delete an IP Destination Group based on its ID.

        Parameters:
        - group_id (int): The ID of the IP Destination Group to delete.

        Returns:
        - Response: A Response object containing the server's response to the delete request.
        """
        result = self._req(method="delete", path=f"/ipDestinationGroups/{group_id}")

        return result

    def list_lite(
        self, type: Optional[str] = None, exclude_type: Optional[str] = None
    ) -> List[dict]:
        """
        Retrieve a lightweight list of configured IP Destination Groups.

        This method fetches a simplified list containing only the name and ID for each group,
        rather than the full details of each group. Filters can be applied using the `type` and
        `exclude_type` parameters.

        Parameters:
        - type (str, optional): A string identifying a specific destination group type to include.
        Possible values include: "DSTN_IP", "DSTN_FQDN", "DSTN_DOMAIN", "DSTN_OTHER".
        - exclude_type (str, optional): A string identifying a destination group type to exclude.
        Possible values include: "DSTN_IP", "DSTN_FQDN", "DSTN_DOMAIN", "DSTN_OTHER".

        Returns:
        - List[dict]: A list of dictionaries, each containing the 'name' and 'id' of an IP Destination Group.

        Example:
        ```python
        groups = obj.list_lite(type="DSTN_IP", exclude_type="DSTN_FQDN")
        ```
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(
            method="get", path="/ipDestinationGroups/lite", params=params
        )

        return result.json()


class ipv6_destination_groups(Endpoint):
    def list(self, exclude_type: str) -> List[dict]:
        """
        Retrieve a list of configured IPv6 Destination Groups.

        Parameters:
        - exclude_type (str, optional): A string identifying a destination group type to exclude.
        Possible values include: "DSTN_IP", "DSTN_FQDN", "DSTN_DOMAIN", "DSTN_OTHER".

        Returns:
        - Response: A Response object containing the list of IP Destination Groups.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(
            method="get",
            path="/ipDestinationGroups/ipv6DestinationGroups",
            params=params,
        )

        return result.json()

    def list_lite(
        self, type: Optional[str] = None, exclude_type: Optional[str] = None
    ) -> List[dict]:
        """
        Retrieve a lightweight list of configured IPv6 Destination Groups.

        This method fetches a simplified list containing only the name and ID for each group,
        rather than the full details of each group. Filters can be applied using the `type` and
        `exclude_type` parameters.

        Parameters:
        - type (str, optional): A string identifying a specific destination group type to include.
        Possible values include: "DSTN_IP", "DSTN_FQDN", "DSTN_DOMAIN", "DSTN_OTHER".
        - exclude_type (str, optional): A string identifying a destination group type to exclude.
        Possible values include: "DSTN_IP", "DSTN_FQDN", "DSTN_DOMAIN", "DSTN_OTHER".

        Returns:
        - List[dict]: A list of dictionaries, each containing the 'name' and 'id' of an IPv6 Destination Group.

        Example:
        ```python
        groups = obj.list_lite(type="DSTN_IP", exclude_type="DSTN_FQDN")
        ```
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(
            method="get",
            path="/ipDestinationGroups/ipv6DestinationGroups/lite",
            params=params,
        )

        return result.json()


class ip_source_groups(Endpoint):
    def list(self, search: str) -> List[dict]:
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }

        result = self._req(method="get", path="/ipSourceGroups", params=params)

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Create a new IP Source Group.

        Sends a POST request to create a new IP Source Group based on the provided payload.
        """
        result = self._req(method="post", path="/ipSourceGroups", json=payload)

        return result

    def get(self, group_id: int) -> dict:
        """
        Retrieve details of an IP Source Group based on its ID.

        Parameters:
        - group_id (int): The ID of the IP Destination Source to retrieve.

        Returns:
        - Response: A Response object containing the details of the IP Source Group.
        """
        result = self._req(method="get", path=f"/ipSourceGroups/{group_id}")

        return result.json()

    def update(self, group_id: int, payload: dict) -> Response:
        """
        Update an existing IP Source Group.

        Sends a PUT request to update the details of an IP Source Group based on the provided payload.

        Parameters:
        - group_id (int): The ID of the IP Source Group to update.
        - payload (dict): A dictionary containing the updated details of the IP Source Group.

        Returns:
        - Response: A Response object containing the server's response to the update request.
        """
        result = self._req(
            method="put", path=f"/ipSourceGroups/{group_id}", json=payload
        )

        return result

    def delete(self, group_id: int) -> Response:
        """
        Delete an IP Source Group based on its ID.

        Parameters:
        - group_id (int): The ID of the IP Source Group to delete.

        Returns:
        - Response: A Response object containing the server's response to the delete request.
        """
        result = self._req(method="delete", path=f"/ipSourceGroups/{group_id}")

        return result

    def list_lite(self) -> List[dict]:
        """
        Retrieve a lightweight list of configured IP Source Groups.

        This method fetches a simplified list containing only the name and ID for each group,
        rather than the full details of each group.

        Returns:
        - List[dict]: A list of dictionaries, each containing the 'name' and 'id' of an IP Source Group.

        """

        result = self._req(method="get", path="/ipSourceGroups/lite")

        return result.json()


class ipv6_source_groups(Endpoint):
    def list(self) -> List[dict]:
        """
        Retrieve a list of configured IPv6 Source Groups.

        Returns:
        - Response: A Response object containing the list of IP Source Groups.
        """
        result = self._req(method="get", path="/ipSourceGroups/ipv6SourceGroups")

        return result.json()

    def list_lite(self) -> List[dict]:
        """
        Retrieve a lightweight list of configured IPv6 Source Groups.

        This method fetches a simplified list containing only the name and ID for each group,
        rather than the full details of each group.

        Returns:
        - List[dict]: A list of dictionaries, each containing the 'name' and 'id' of an IPv6 Destination Group.
        """
        result = self._req(method="get", path="/ipSourceGroups/ipv6SourceGroups/lite")

        return result.json()


class network_application_groups(Endpoint):
    def list(self, search: str) -> List[dict]:
        """
        Retrieve a list of network application groups based on search criteria.

        Parameters:
        - search (str): Search criteria to filter the results.

        Returns:
        - List[dict]: A list of dictionaries representing network application groups.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(
            method="get", path="/networkApplicationGroups", params=params
        )

        return result.json()

    def get(self, group_id: int) -> dict:
        """
        Retrieve details of a specific network application group by its ID.

        Parameters:
        - group_id (int): The ID of the network application group to retrieve.

        Returns:
        - dict: A dictionary representing the details of the network application group.
        """
        result = self._req(method="get", path=f"/networkApplicationGroups/{group_id}")

        return result.json()

    def list_lite(self) -> List[dict]:
        """
        Retrieve a lightweight list of all network application groups.

        Returns:
        - List[dict]: A list of dictionaries, each containing basic info about a network application group.
        """
        result = self._req(method="get", path="/networkApplicationGroups/lite")

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Create a new network application group.

        Parameters:
        - payload (dict): A dictionary containing the details of the network application group to be created.
        The dictionary should have the following structure:
        {
            "name": str,                  # Name of the network application group.
            "description": str,           # Description of the group.
            "networkApplications": List[str]  # List of network applications associated with the group.
        }

        Returns:
        - Response: A Response object containing the server's response to the creation request.
        """
        result = self._req(
            method="post", path="/networkApplicationGroups", json=payload
        )

        return result

    def update(self, group_id: int, payload: dict) -> Response:
        """
        Update an existing network application group.

        Parameters:
        - group_id (int): The ID of the network application group to update.
        - payload (dict): A dictionary containing the details of the network application group to be created.
        The dictionary should have the following structure:
        {
            "name": str,                  # Name of the network application group.
            "description": str,           # Description of the group.
            "networkApplications": List[str]  # List of network applications associated with the group.
        }

        Returns:
        - Response: A Response object containing the server's response to the update request.
        """
        result = self._req(
            method="put", path=f"/networkApplicationGroups/{group_id}", json=payload
        )

        return result

    def delete(self, group_id: int) -> Response:
        """
        Delete a specific network application group by its ID.

        Parameters:
        - group_id (int): The ID of the network application group to delete.

        Returns:
        - Response: A Response object containing the server's response to the delete request.
        """
        result = self._req(
            method="delete", path=f"/networkApplicationGroups/{group_id}"
        )

        return result


class network_applications(Endpoint):
    def list(
        self, search: Optional[str] = None, locale: Optional[str] = "en-US"
    ) -> List[dict]:
        """
        Retrieve a list of network applications based on search criteria.

        Parameters:
        - search (str): Search criteria to filter the results.
        - locale (str): When set to one of the supported locales
        (i.e., en-US, de-DE, es-ES, fr-FR, ja-JP, zh-CN), the network application's
        description is localized into the requested language.

        Returns:
        - List[dict]: A list of dictionaries representing network applications.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/networkApplications", params=params)

        return result.json()

    def get(self, app_id: str, locale: Optional[str] = "en-US") -> dict:
        """
        Retrieve details of a specific network application by its ID.

        Parameters:
        - app_id (str): The ID of the network application to retrieve.
        - locale (str): When set to one of the supported locales
        (i.e., en-US, de-DE, es-ES, fr-FR, ja-JP, zh-CN), the network application's
        description is localized into the requested language.

        Returns:
        - dict: A dictionary representing the details of the network application group.
        """
        params = {"locale": locale}
        result = self._req(
            method="get", path=f"/networkApplications/{app_id}", params=params
        )

        return result.json()


class network_service_groups(Endpoint):
    def list(self, search: Optional[str] = None) -> List[dict]:
        """
        Retrieve a list of network service groups based on search criteria.

        Parameters:
        - search (str): Search criteria to filter the results.

        Returns:
        - List[dict]: A list of dictionaries representing network service groups.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/networkServiceGroups", params=params)

        return result.json()

    def get(self, group_id: int) -> dict:
        """
        Retrieve details of a specific network service group by its ID.

        Parameters:
        - group_id (int): The ID of the network service group to retrieve.

        Returns:
        - dict: A dictionary representing the details of the network service group.
        """
        result = self._req(method="get", path=f"/networkServiceGroups/{group_id}")

        return result.json()

    def list_lite(self) -> List[dict]:
        """
        Retrieve a lightweight list of all network service groups.

        Returns:
        - List[dict]: A list of dictionaries, each containing basic info about a network service group.
        """
        result = self._req(method="get", path="/networkServiceGroups/lite")

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Create a new network service group.

        Parameters:
        - payload (dict): A dictionary containing the details of the network service group to be created.
        - payload (dict): A dictionary containing the details of the network service group to be created.
        The dictionary should have the following structure:
        {
            "name": str,                  # Name of the network application group.
            "description": str,           # Description of the group.
            "services": List[dict]  # List of dictionaries containing network services to include
        }

        Returns:
        - Response: A Response object containing the server's response to the creation request.
        """
        result = self._req(method="post", path="/networkServiceGroups", json=payload)

        return result.json()

    def update(self, group_id: int, payload: dict) -> Response:
        """
        Update an existing network service group.

        Parameters:
        - group_id (int): The ID of the network service group to update.
        - payload (dict): A dictionary containing the details of the network service group to be created.
        The dictionary should have the following structure:
        {
            "name": str,                  # Name of the network application group.
            "description": str,           # Description of the group.
            "services": List[dict]  # List of dictionaries containing network services to include
        }

        Returns:
        - Response: A Response object containing the server's response to the update request.
        """
        result = self._req(
            method="put", path=f"/networkServiceGroups/{group_id}", json=payload
        )

        return result.json()

    def delete(self, group_id: int) -> Response:
        """
        Delete a specific network service group by its ID.

        Parameters:
        - group_id (int): The ID of the network service group to delete.

        Returns:
        - Response: A Response object containing the server's response to the delete request.
        """
        result = self._req(method="delete", path=f"/networkServiceGroups/{group_id}")

        return result


class network_services(Endpoint):
    def list(
        self,
        search: Optional[str] = None,
        protocol: Optional[List[str]] = None,
        locale: Optional[str] = "en-US",
    ) -> List[dict]:
        """
        Retrieve a list of network services based on search criteria.

        Parameters:
        - search (str): Search criteria to filter the results.
        - protocols (List[str]): List of strings representing protocols to search by. Valid values are:
            ["ICMP", "TCP", "UDP", "GRE", "ESP", "OTHER"]
        - locale (str): When set to one of the supported locales
        (i.e., en-US, de-DE, es-ES, fr-FR, ja-JP, zh-CN), the network application's
        description is localized into the requested language.

        Returns:
        - List[dict]: A list of dictionaries representing network services.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/networkServices", params=params)

        return result.json()

    def get(self, service_id: int, locale: Optional[str] = "en-US") -> dict:
        """
        Retrieve details of a specific network service by its ID.

        Parameters:
        - service_id (int): The ID of the network service to retrieve.
        - locale (str): When set to one of the supported locales
        (i.e., en-US, de-DE, es-ES, fr-FR, ja-JP, zh-CN), the network application's
        description is localized into the requested language.

        Returns:
        - dict: A dictionary representing the details of the network service.
        """
        params = {"locale": locale}

        result = self._req(
            method="get", path=f"/networkServices/{service_id}", params=params
        )

        return result.json()

    def list_lite(self, locale: Optional[str] = "en-US") -> List[dict]:
        """
        Retrieve a lightweight list of all network services.

        Returns:
        - List[dict]: A list of dictionaries, each containing basic info about a network services.
        """
        params = {"locale": locale}

        result = self._req(method="get", path="/networkServices/lite", params=params)

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Create a new network service.

        Parameters:
        - payload (dict): A dictionary containing the details of the network service to be created.
        The dictionary should have the following structure:
        {
            "name": str,                              # Name of the network service.
            "tag": str,                               # Tag associated with the service (e.g., "ICMP_ANY").
            "srcTcpPorts": List[Dict[str, int]],      # List of source TCP ports with start and end values.
            "destTcpPorts": List[Dict[str, int]],     # List of destination TCP ports with start and end values.
            "srcUdpPorts": List[Dict[str, int]],      # List of source UDP ports with start and end values.
            "destUdpPorts": List[Dict[str, int]],     # List of destination UDP ports with start and end values.
            "type": str,                              # Type of the network service (e.g., "STANDARD").
            "description": str                        # Description of the network service.
        }

        Returns:
        - Response: A Response object containing the server's response to the creation request.
        """
        result = self._req(method="post", path="/networkServices", json=payload)

        return result

    def update(self, service_id: int, payload: dict) -> Response:
        """
        Updates an exisiting network service

        Parameters:
        - service_id (int): The service ID of the network service to be updated
        - payload (dict): A dictionary containing the details of the network service to be created.
        The dictionary should have the following structure:
        {
            "name": str,                              # Name of the network service.
            "tag": str,                               # Tag associated with the service (e.g., "ICMP_ANY").
            "srcTcpPorts": List[Dict[str, int]],      # List of source TCP ports with start and end values.
            "destTcpPorts": List[Dict[str, int]],     # List of destination TCP ports with start and end values.
            "srcUdpPorts": List[Dict[str, int]],      # List of source UDP ports with start and end values.
            "destUdpPorts": List[Dict[str, int]],     # List of destination UDP ports with start and end values.
            "type": str,                              # Type of the network service (e.g., "STANDARD").
            "description": str                        # Description of the network service.
        }

        Returns:
        - Response: A Response object containing the server's response to the creation request.
        """
        result = self._req(
            method="put", path=f"/networkServices/{service_id}", json=payload
        )

        return result

    def delete(self, service_id: int) -> Response:
        """
        Delete a specific network service by its ID.

        Parameters:
        - service_id (int): The ID of the network service to delete.

        Returns:
        - Response: A Response object containing the server's response to the delete request.
        """
        result = self._req(method="delete", path=f"/networkServices/{service_id}")

        return result


class time_windows(Endpoint):
    def list(self) -> List[dict]:
        """
        Gets a list of time intervals used for by the Firewall policy or the URL Filtering policy.
        """
        result = self._req(method="get", path="/timeWindows")

        return result.json()

    def list_lite(self) -> List[dict]:
        """
        Gets a name and ID dictionary of time intervals used by the Firewall policy or the URL Filtering policy.
        """
        result = self._req(method="get", path="/timeWindows/lite")

        return result.json()
