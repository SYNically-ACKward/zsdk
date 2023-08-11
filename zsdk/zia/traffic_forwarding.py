from zsdk.api import Endpoint
from zsdk.utilities import snake_to_camel
from requests import Response
from typing import List, Optional


class gre_tunnels(Endpoint):
    def list(
        self, page: Optional[int] = 1, page_size: Optional[int] = 100
    ) -> List[dict]:
        """
        Gets all provisioned GRE tunnel information.

        Parameters:
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

        result = self._req(method="get", path="/greTunnels", params=params)

        return result.json()

    def get(self, tunnel_id: int) -> dict:
        """
        Gets the GRE tunnel information for the specified ID.

        Parameters:
        - tunnel_id (int): The unique identifier for the GRE tunnel.
        """
        result = self._req(method="get", path=f"/greTunnels/{tunnel_id}")

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Adds a GRE tunnel configuration.

        Parameters:
        - payload (dict): A dictionary containing the GRE tunnel details.
            {
                "sourceIp": (str) The source IP address,
                "primaryDestVip": {
                    "id": (int) The ID of the virtual IP,
                    "virtualIp": (str) The virtual IP address
                },
                "secondaryDestVip": {
                    "id": (int) The ID of the virtual IP,
                    "virtualIp": (str) The virtual IP address
                },
                "internalIpRange": (str) The internal IP range,
                "lastModificationTime": (int) The timestamp of the last modification,
                "lastModifiedBy": {
                    "id": (int) Identifier of the modifier,
                    "extensions": {
                        "additionalProp1": (str) Additional property,
                        "additionalProp2": (str) Additional property,
                        "additionalProp3": (str) Additional property
                    }
                },
                "withinCountry": (bool) Indicates if the GRE tunnel is within the country,
                "comment": (str) A comment regarding the GRE tunnel,
                "ipUnnumbered": (bool) Indicates if the IP is unnumbered,
                "subcloud": (str) The subcloud information
            }

        Returns:
        - Response object containing the result of the operation.
        """
        result = self._req(method="post", path="/greTunnels", json=payload)

        return result

    def update(self, tunnel_id: int, payload: dict) -> Response:
        """
        Updates a GRE tunnel configuration.

        Parameters:
        - tunnel_id (int): The unique identifier for the GRE tunnel.
        - payload (dict): A dictionary containing the GRE tunnel details.
            {
                "sourceIp": (str) The source IP address,
                "primaryDestVip": {
                    "id": (int) The ID of the virtual IP,
                    "virtualIp": (str) The virtual IP address
                },
                "secondaryDestVip": {
                    "id": (int) The ID of the virtual IP,
                    "virtualIp": (str) The virtual IP address
                },
                "internalIpRange": (str) The internal IP range,
                "lastModificationTime": (int) The timestamp of the last modification,
                "lastModifiedBy": {
                    "id": (int) Identifier of the modifier,
                    "extensions": {
                        "additionalProp1": (str) Additional property,
                        "additionalProp2": (str) Additional property,
                        "additionalProp3": (str) Additional property
                    }
                },
                "withinCountry": (bool) Indicates if the GRE tunnel is within the country,
                "comment": (str) A comment regarding the GRE tunnel,
                "ipUnnumbered": (bool) Indicates if the IP is unnumbered,
                "subcloud": (str) The subcloud information
            }

        Returns:
        - Response object containing the result of the operation.
        """
        result = self._req(method="put", path=f"/greTunnels/{tunnel_id}", json=payload)

        return result

    def delete(self, tunnel_id: int) -> Response:
        """
        Deletes the GRE tunnel information for the specified ID.

        Parameters:
        - tunnel_id (int): The unique identifier for the GRE tunnel.
        """
        result = self._req(method="delete", path=f"/greTunnels/{tunnel_id}")

        return result

    def get_internal_ips(
        self,
        internal_ip_range: Optional[str] = None,
        static_ip: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> dict:
        """
        Gets the next available GRE tunnel internal IP address ranges.

        Parameters:
        - internal_ip_range (str): Internal IP range information.
        - static_ip (str): Static IP information.
        - limit (int): The maximum number of GRE tunnel IP ranges that can be added.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(
            method="get", path="/greTunnels/availableInternalIpRanges", params=params
        )

        return result.json()

    def get_org_ips(self, ip_addresses: Optional[List[str]] = None) -> dict:
        """
        Gets a list of IP addresses with GRE tunnel details.

        Parameters:
        - ip_addresses (List[str]): Filter based on an IP address range.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(
            method="get", path="/orgProvisioning/ipGreTunnelInfo", params=params
        )

        return result.json()


class ipv6(Endpoint):
    def get_config(self) -> dict:
        """
        Gets the IPv6 configuration details for the organization.
        """
        result = self._req(method="get", path="/ipv6config")

        return result.json()

    def get_dns64(self, search: Optional[str] = None) -> dict:
        """
        Gets the list of NAT64 prefixes configured as the DNS64 prefix for the organization.

        Parameters:
        - search (str): Used to match against a DNS64 prefix name, description, or prefixMask attributes.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/ipv6config/dns64prefix", params=params)

        return result.json()

    def get_nat64(
        self,
        search: Optional[str] = None,
        page: Optional[int] = 1,
        page_size: Optional[int] = 100,
    ) -> dict:
        """
        Gets the list of NAT64 prefixes configured for the organization.
        The prefix which has the dnsPrefix field set to true is identified as the DNS64 prefix.

        Parameters:
        - search (str): Used to match against a NAT64 prefixs name, description, or prefixMask attributes.
        - page (int): Specifies the page offset.
        - page_size (int): Specifies the page size. The default size is 100 and the maximum size is 1000.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/ipv6config/nat64prefix", params=params)

        return result.json()


class static_ips(Endpoint):
    def list(
        self,
        available_for_gre_tunnel: Optional[bool] = None,
        ip_address: Optional[str] = None,
        page: Optional[int] = 1,
        page_size: Optional[int] = 100,
    ) -> dict:
        """
        Gets all provisioned static IP addresses.

        Parameters:
        - available_for_gre_tunnel (bool): True to get only the static IP addresses not yet associated to a GRE tunnel.
        - ip_address (str): Filter based on IP address
        - page (int): Specifies the page offset.
        page_size (int): Specifies the page size. The default size is 100, but the maximum size is 1000.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/staticIP", params=params)

        return result.json()

    def get(self, ip_id: int) -> dict:
        """
        Gets static IP address for the specified ID

        Parameters:
        - ip_id (int): The unique identifier for the static IP address
        """
        result = self._req(method="get", path=f"/staticIP/{ip_id}")

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Adds a static IP address.

        Parameters:
        - payload (dict): The dictionary containing data for the creation.
        Example dictionary:
        {
            "ipAddress": "string",  # The static IP address
            "geoOverride": true,  # If not set, geographic coordinates and city are automatically determined from the IP address
            "latitude": 0, # Required only if the geoOverride attribute is set. Latitude with 7 digit precision
            "longitude": 0, # Required only if the geoOverride attribute is set. Longitude with 7 digit precision
            "routableIP": true, # Indicates whether a non-RFC 1918 IP address is publicly routable
            "comment": "string"
        }

        Returns:
        - Response: The server's response object.
        """
        result = self._req(method="post", path="/staticIP", json=payload)

        return result

    def update(self, ip_id: int, payload: dict) -> Response:
        """
        Adds a static IP address.

        Parameters:
        - ip_id (int): The unique identifier for the static IP address
        - payload (dict): The dictionary containing data for the update.
        Example dictionary:
        {
            "ipAddress": "string",  # The static IP address
            "geoOverride": true,  # If not set, geographic coordinates and city are automatically determined from the IP address
            "latitude": 0, # Required only if the geoOverride attribute is set. Latitude with 7 digit precision
            "longitude": 0, # Required only if the geoOverride attribute is set. Longitude with 7 digit precision
            "routableIP": true, # Indicates whether a non-RFC 1918 IP address is publicly routable
            "comment": "string"
        }

        Returns:
        - Response: The server's response object.
        """
        result = self._req(method="put", path=f"/staticIP/{ip_id}", json=payload)

        return result

    def delete(self, ip_id: int) -> Response:
        """
        Deletes the static IP address for the specified ID.

        Parameters:
        - ip_id (int): The unique identifier for the provisioned static IP address.
        """
        result = self._req(method="delete", path=f"/staticIP/{ip_id}")

        return result

    def validate(self, payload: dict) -> Response:
        """
        Validates the static IP address.

        Parameters:
        - payload (dict): The dictionary containing data for the validation.
        Example dictionary:
        {
            "ipAddress": "string",  # The static IP address
            "geoOverride": true,  # If not set, geographic coordinates and city are automatically determined from the IP address
            "latitude": 0, # Required only if the geoOverride attribute is set. Latitude with 7 digit precision
            "longitude": 0, # Required only if the geoOverride attribute is set. Longitude with 7 digit precision
            "routableIP": true, # Indicates whether a non-RFC 1918 IP address is publicly routable
            "comment": "string"
        }
        """
        result = self._req(method="post", path="/staticIP/validate", json=payload)

        return result


class vips(Endpoint):
    def list(
        self,
        dc: Optional[str] = None,
        region: Optional[str] = None,
        page: Optional[int] = 1,
        page_size: Optional[int] = 100,
        include: Optional[str] = "all",
        subcloud: Optional[str] = None,
    ) -> List[dict]:
        """
        Gets a paginated list of the virtual IP addresses (VIPs)
        available in the Zscaler cloud, including region and data center information.

        Parameters:
        - dc (str): Filter based on data center.
        - region (str): Filter based on region.
        - page (int): Specifies the page offset.
        - page_size (int): Specifies the page size. The default size is 100, but the maximum size is 1000.
        - include (str): Include all, private, or public VIPs in the list.
            Valid values: "all", "private", "public". Default = "all"
        - subcloud (str): Filter based on the subcloud for the VIP.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/vips", params=params)

        return result.json()

    def list_by_dc(
        self,
        routable_ip: Optional[bool] = None,
        within_country_only: Optional[bool] = None,
        include_private_service_edge: [Optional] = None,
        include_current_vips: Optional[bool] = None,
        source_ip: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        subcloud: Optional[str] = None,
    ) -> List[dict]:
        """
        Gets a list of recommended GRE tunnel virtual IP addresses (VIPs),
        grouped by data center, based on source IP address or latitude/longitude coordinates.

        Parameters:
        - routable_ip (bool): The routable IP address.
        - within_country_only (bool): Search within country only.
        - include_private_service_edge (bool): Include ZIA Private Service Edge VIPs.
        - include_current_vips (bool): Include currently assigned VIPs.
        - source_ip (str): The source IP address.
        - latitude (float): The latitude coordinate of the GRE tunnel source.
        - longitude (float): The longitude coordinate of the GRE tunnel source.
        - subcloud (str): The subcloud for the VIP.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key not in ["self", "routable_ip"]
        }
        params = {snake_to_camel(key): value for key, value in params.items()}
        if routable_ip is not None:
            params["routableIP"] = routable_ip

        result = self._req(method="get", path="/vips/groupByDatacenter", params=params)

        return result.json()

    def list_recommended(
        self,
        routable_ip: Optional[bool] = None,
        within_country_only: Optional[bool] = None,
        include_private_service_edge: [Optional] = None,
        include_current_vips: Optional[bool] = None,
        source_ip: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        subcloud: Optional[str] = None,
    ) -> List[dict]:
        """
        Gets a list of recommended GRE tunnel virtual IP addresses (VIPs),
        based on source IP address or latitude/longitude coordinates.

        Parameters:
        - routable_ip (bool): The routable IP address.
        - within_country_only (bool): Search within country only.
        - include_private_service_edge (bool): Include ZIA Private Service Edge VIPs.
        - include_current_vips (bool): Include currently assigned VIPs.
        - source_ip (str): The source IP address.
        - latitude (float): The latitude coordinate of the GRE tunnel source.
        - longitude (float): The longitude coordinate of the GRE tunnel source.
        - subcloud (str): The subcloud for the VIP.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key not in ["self", "routable_ip"]
        }
        params = {snake_to_camel(key): value for key, value in params.items()}
        if routable_ip is not None:
            params["routableIP"] = routable_ip

        result = self._req(method="get", path="/vips/recommendedList", params=params)

        return result.json()


class vpn_credentials(Endpoint):
    def list(
        self,
        search: Optional[str] = None,
        type: Optional[str] = None,
        include_only_without_location: Optional[bool] = None,
        location_id: Optional[int] = None,
        managed_by: Optional[int] = None,
        page: Optional[int] = 1,
        page_size: Optional[int] = 100,
    ) -> List[dict]:
        """
        Gets VPN credentials that can be associated to locations.

        Parameters:
        - search (str): The search string used to match against a VPN credential's
            commonName, fqdn, ipAddress, comments, or locationName attributes.
        - type (str): Only gets VPN credentials for the specified type.
            Valid values: "CN", "IP", "UFQDN", "XAUTH"
        - include_only_without_location (bool): Include VPN credential only if not associated to any location.
        - location_id (int): Gets the VPN credentials for the specified location ID.
        - managed_by (int): Gets the VPN credentials that are managed by the given partner.
        - page (int): Specifies the page offset.
        - page_size (int): Specifies the page size. The default size is 100, but the maximum size is 1000.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key not in ["self"]
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/vpnCredentials", params=params)

        return result.json()

    def get(self, credential_id: int) -> dict:
        """
        Gets the VPN credentials for the specified ID.

        Parameters:
        - credential_id (int): The unique identifier for the VPN credential.
        """
        result = self._req(method="get", path=f"/vpnCredentials/{credential_id}")

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Adds VPN credentials that can be associated to locations.

        Parameters:
        - payload (dict): The dictionary containing data for the creation.
        Example dictionary:
        {
            "type": "string",  # Type of credentials. Valid values: "CN", "IP", "UFQDN", "XAUTH"
            "fqdn": "string",  # Fully Qualified Domain Name.
            "ipAddress": "string", # Static IP address for VPN that is self-provisioned or provisioned by Zscaler.
            "preSharedKey": "string", # Pre-shared key. This is a required field for UFQDN and IP auth type.
            "comments": "string"
        }
        """
        result = self._req(method="post", path="/vpnCredentials", json=payload)

        return result

    def update(self, credential_id: int, payload: dict) -> Response:
        """
        Updates VPN credentials that can be associated to locations.

        Parameters:
        - credential_id (int): The unique identifier for the VPN credential.
        - payload (dict): The dictionary containing data for the update.
        Example dictionary:
        {
            "type": "string",  # Type of credentials. Valid values: "CN", "IP", "UFQDN", "XAUTH"
            "fqdn": "string",  # Fully Qualified Domain Name.
            "ipAddress": "string", # Static IP address for VPN that is self-provisioned or provisioned by Zscaler.
            "preSharedKey": "string", # Pre-shared key. This is a required field for UFQDN and IP auth type.
            "comments": "string"
        }
        """
        result = self._req(
            method="put", path=f"/vpnCredentials/{credential_id}", json=payload
        )

        return result

    def delete(self, credential_id: int) -> Response:
        """
        Deletes the VPN credentials for the specified ID.

        Parameters:
        - credential_id (int): The unique identifier for the VPN credential.
        """
        result = self._req(method="delete", path=f"/vpnCredentials/{credential_id}")

        return result

    def bulk_delete(self, credentials_to_delete: List[int]) -> Response:
        """
        Bulk delete VPN credentials up to a maximum of 100 credentials per request.

        Parameters:
        - credentials_to_delete (List[int]): The VPN IDs to bulk delete
        """
        payload = {"ids": credentials_to_delete}

        result = self._req(
            method="post", path="/vpnCredentials/bulkDelete", json=payload
        )

        return result
