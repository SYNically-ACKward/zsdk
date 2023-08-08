from zsdk.api import Endpoint
from zsdk.utilities import snake_to_camel
from requests import Response
from typing import List, Optional


class dlp_dictionaries(Endpoint):
    def list(self, search: Optional[str] = None) -> List[dict]:
        """
        Retrieve a list of DLP Dictionaries based on search criteria.

        Parameters:
        - search (str): Search criteria to filter the results.

        Returns:
        - List[dict]: A list of dictionaries representing DLP Dictionaries.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/dlpDictionaries", params=params)

        return result.json()

    def get(self, dictionary_id: int) -> dict:
        """
        Retrieve details of a specific DLP Dictionary by its ID.

        Parameters:
        - dictionary_id (int): The ID of the DLP Dictionary to retrieve.

        Returns:
        - dict: A dictionary representing the details of the DLP Dictionary.
        """
        result = self._req(method="get", path=f"/dlpDictionaries/{dictionary_id}")

        return result.json()

    def list_lite(self) -> List[dict]:
        """
        Retrieve a lightweight list of all DLP Dictionaries.

        Returns:
        - List[dict]: A list of dictionaries, each containing basic info about a DLP Dictionaries.
        """
        result = self._req(method="get", path="/dlpDictionaries/lite")

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Create a new DLP (Data Loss Prevention) dictionary.

        Parameters:
        - payload (dict): A dictionary containing the details of the DLP dictionary to be created.
        The dictionary should have the following structure:
        {
            "name": str,               # Name of the dictionary.
            "description": str,        # Description of the dictionary.
            "confidenceThreshold": str, # Confidence threshold for the dictionary. E.g., "CONFIDENCE_LEVEL_LOW".
            "phrases": List[Dict],     # List of phrases. Each phrase has 'action' and 'phrase'.
            "customPhraseMatchType": str, # Custom phrase match type. E.g., "MATCH_ALL_CUSTOM_PHRASE_PATTERN_DICTIONARY".
            "patterns": List[Dict],    # List of patterns. Each pattern has 'action' and 'pattern'.
            "dictionaryType": str,     # Type of the dictionary. E.g., "PATTERNS_AND_PHRASES".
            "exactDataMatchDetails": List[Dict], # List of exact data match details.
            "idmProfileMatchAccuracy": List[Dict], # List of IDM profile match accuracies.
            "ignoreExactMatchIdmDict": bool, # Flag to determine if exact match IDM dictionary should be ignored.
            "includeBinNumbers": bool, # Flag to determine if BIN numbers should be included.
            "binNumbers": List[int],   # List of BIN numbers.
            "dictTemplateId": int,     # ID of the dictionary template.
            "proximity": int           # Proximity setting for the dictionary.
        }

        Returns:
        - Response: A Response object containing the server's response to the creation request.
        """
        result = self._req(method="post", path="/dlpDictionaries", json=payload)

        return result

    def update(self, dictionary_id: int, payload: dict) -> Response:
        """
        Updates an existing DLP (Data Loss Prevention) dictionary.

        Parameters:
        - dictionary_id (int): The ID of the dictionary to be updated
        - payload (dict): A dictionary containing the details of the DLP dictionary to be updated.
        The dictionary should have the following structure:
        {
            "name": str,               # Name of the dictionary.
            "description": str,        # Description of the dictionary.
            "confidenceThreshold": str, # Confidence threshold for the dictionary. E.g., "CONFIDENCE_LEVEL_LOW".
            "phrases": List[Dict],     # List of phrases. Each phrase has 'action' and 'phrase'.
            "customPhraseMatchType": str, # Custom phrase match type. E.g., "MATCH_ALL_CUSTOM_PHRASE_PATTERN_DICTIONARY".
            "patterns": List[Dict],    # List of patterns. Each pattern has 'action' and 'pattern'.
            "dictionaryType": str,     # Type of the dictionary. E.g., "PATTERNS_AND_PHRASES".
            "exactDataMatchDetails": List[Dict], # List of exact data match details.
            "idmProfileMatchAccuracy": List[Dict], # List of IDM profile match accuracies.
            "ignoreExactMatchIdmDict": bool, # Flag to determine if exact match IDM dictionary should be ignored.
            "includeBinNumbers": bool, # Flag to determine if BIN numbers should be included.
            "binNumbers": List[int],   # List of BIN numbers.
            "dictTemplateId": int,     # ID of the dictionary template.
            "proximity": int           # Proximity setting for the dictionary.
        }

        Returns:
        - Response: A Response object containing the server's response to the update request.
        """
        result = self._req(
            method="put", path=f"/dlpDictionaries/{dictionary_id}", json=payload
        )

        return result

    def delete(self, dictionary_id: int) -> Response:
        """
        Delete a specific DLP Dictionary by its ID.

        Parameters:
        - dictionary_id (int): The ID of the DLP Dictionary to delete.

        Returns:
        - Response: A Response object containing the server's response to the delete request.
        """
        result = self._req(method="delete", path=f"/dlpDictionaries/{dictionary_id}")

        return result

    def validate(self) -> Response:  # TODO: Investigate what to POST
        """
        Validates the pattern used by a Pattern and Phrases DLP dictionary type,
        and provides error information if the pattern is invalid.
        """
        pass


class dlp_engines(Endpoint):
    def list(self, search: Optional[str] = None) -> List[dict]:
        """
        Retrieve a list of DLP Engines based on search criteria.

        Parameters:
        - search (str): Search criteria to filter the results.

        Returns:
        - List[dict]: A list of dictionaries representing DLP Engines.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(method="get", path="/dlpEngines", params=params)

        return result.json()

    def get(self, engine_id: int) -> dict:
        """
        Retrieve details of a specific DLP Engine by its ID.

        Parameters:
        - dict_id (int): The ID of the DLP Engine to retrieve.

        Returns:
        - dict: A dictionary representing the details of the DLP Engine.
        """
        result = self._req(method="get", path=f"/dlpEngines/{engine_id}")

        return result.json()

    def list_lite(self) -> List[dict]:
        """
        Retrieve a lightweight list of all DLP Engines.

        Returns:
        - List[dict]: A list of dictionaries, each containing basic info about a DLP Engines.
        """
        result = self._req(method="get", path="/dlpEngines/lite")

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Create a new DLP (Data Loss Prevention) Engine.

        Parameters:
        - payload (dict): A dictionary containing the details of the DLP Engine to be created.
        The dictionary should have the following structure:
        {
            "name": str,                # Name of the DLP Engine.
            "engineExpression": str,    # Expression associated with the DLP Engine.
            "customDlpEngine": bool,    # Flag indicating if the DLP Engine is custom.
            "description": str          # Description of the DLP Engine.
        }

        Returns:
        - Response: A Response object containing the server's response to the creation request.
        """
        result = self._req(method="post", path="/dlpEngines", json=payload)

        return result

    def update(self, engine_id: int, payload: dict) -> Response:
        """
        Updates an existing DLP (Data Loss Prevention) Engine.

        Parameters:
        - engine_id (int): The ID of the engine to be updated
        - payload (dict): A dictionary containing the details of the DLP Engine to be created.
        The dictionary should have the following structure:
        {
            "name": str,                # Name of the DLP Engine.
            "engineExpression": str,    # Expression associated with the DLP Engine.
            "customDlpEngine": bool,    # Flag indicating if the DLP Engine is custom.
            "description": str          # Description of the DLP Engine.
        }

        Returns:
        - Response: A Response object containing the server's response to the update request.
        """
        result = self._req(method="put", path=f"/dlpEngines/{engine_id}", json=payload)

        return result

    def delete(self, engine_id: int) -> Response:
        """
        Delete a specific DLP Engine by its ID.

        Parameters:
        - engine_id (int): The ID of the DLP Engine to delete.

        Returns:
        - Response: A Response object containing the server's response to the delete request.
        """
        result = self._req(method="delete", path=f"/dlpEngines/{engine_id}")

        return result

    def validate(self) -> Response:  # TODO: Investigate what to POST
        """
        Validates the logical expression within a DLP engine that is formed by combining DLP dictionaries
        and provides error information if the expression is invalid.
        """
        pass


class dlp_edm(Endpoint):
    def list(self) -> list:
        """
        Method to retrieve a list of DLP (Data Loss Prevention) EDM (Exact Data Match) Schemas
        """
        result = self._req(method="get", path="/dlpExactDataMatchSchemas")

        return result.json()

    def list_lite(
        self,
        schema_name: Optional[str] = None,
        active_only: Optional[bool] = None,
        fetch_tokens: Optional[bool] = None,
    ) -> list:
        """
        Gets a list of active EDM templates (or EDM schemas) and their criteria (or token details), only.

        Parameters:
        - schema_name: (str) The EDM schema name.
        - active_only: (bool) If set to true, only active EDM templates (or schemas) are returned in the response.
        - fetch_tokens: (bool) If set to true, the criteria (i.e., token details) for
            the active templates are returned in the response.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(
            method="get", path="/dlpExactDataMatchSchemas/lite", params=params
        )

        return result.json()


class dlp_notification_templates(Endpoint):
    def list(self) -> List[dict]:
        """
        Retrieve a list of DLP Notification Templates based on search criteria.

        Returns:
        - List[dict]: A list of dictionaries representing DLP Notification Templates.
        """
        result = self._req(method="get", path="/dlpNotificationTemplates")

        return result.json()

    def get(self, template_id: int) -> dict:
        """
        Retrieve details of a specific DLP Notification Template by its ID.

        Parameters:
        - template_id (int): The ID of the DLP Notification Template to retrieve.

        Returns:
        - dict: A dictionary representing the details of the DLP Notification Template.
        """
        result = self._req(
            method="get", path=f"/dlpNotificationTemplates/{template_id}"
        )

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Create a new DLP Notification Template.

        Parameters:
        - payload (dict): A dictionary containing the details to be created.
        The dictionary should have the following structure:
        {
            "name": str,                # The DLP notification template name.
            "subject": str,             # The Subject line that is displayed within the DLP notification email.
            "attachContent": bool,      # If set to true, the content that is violation is attached to the DLP notification email.
            "plainTextMessage": str,    # The template for the plain text UTF-8 message body that must be displayed in the DLP notification email.
            "htmlMessage": str          # The template for the HTML message body that must be displayed in the DLP notification email.

        }

        Returns:
        - Response: A Response object containing the server's response to the creation request.
        """
        result = self._req(
            method="post", path="/dlpNotificationTemplates", json=payload
        )

        return result

    def update(self, template_id: int, payload: dict) -> Response:
        """
        Update an existing DLP Notification Template.

        Parameters:
        - template_id (int): The ID of the DLP Notification Template to update.
        - payload (dict): A dictionary containing the details to be created.
        The dictionary should have the following structure:
        {
            "name": str,                # The DLP notification template name.
            "subject": str,             # The Subject line that is displayed within the DLP notification email.
            "attachContent": bool,      # If set to true, the content that is violation is attached to the DLP notification email.
            "plainTextMessage": str,    # The template for the plain text UTF-8 message body that must be displayed in the DLP notification email.
            "htmlMessage": str          # The template for the HTML message body that must be displayed in the DLP notification email.

        }

        Returns:
        - Response: A Response object containing the server's response to the update request.
        """
        result = self._req(
            method="put", path=f"/dlpNotificationTemplates/{template_id}", json=payload
        )

        return result

    def delete(self, template_id: int) -> Response:
        """
        Delete a specific DLP Notification Template by its ID.

        Parameters:
        - template_id (int): The ID of the DLP Notification Template to delete.

        Returns:
        - Response: A Response object containing the server's response to the delete request.
        """
        result = self._req(
            method="delete", path=f"/dlpNotificationTemplates/{template_id}"
        )

        return result


class icap_servers(Endpoint):
    def list(self) -> List[dict]:
        """
        Retrieve a the list of DLP servers using ICAP

        Returns:
        - List[dict]: A list of dictionaries representing DLP Servers using ICAP.
        """
        result = self._req(method="get", path="/icapServers")

        return result.json()

    def get(
        self,
        icap_server_id: int,
    ) -> dict:
        """
        Get DLP server (i.e., for servers using ICAP) information for the specified ID.

        Parameters:
        - icap_server_id (int): The unique identifier for the DLP server using ICAP.

        Returns:
        - dict: A dictionary representing the details of the DLP server using ICAP
        """
        result = self._req(method="get", path=f"/icapServers/{icap_server_id}")

        return result.json()

    def list_lite(self) -> List[dict]:
        """
        Retrieve a name and ID dictionary for all DLP servers using ICAP.

        Returns:
        - List[dict]: A list of dictionaries, each containing basic info about a DLP server using ICAP.
        """
        result = self._req(method="get", path="/icapServers/lite")

        return result.json()


class idm_profiles(Endpoint):
    def list(self) -> List[dict]:
        """
        Retrieve all of the IDM templates for all Index Tools used by the organization

        Returns:
        - List[dict]: A list of dictionaries representing IDM Templates
        """
        result = self._req(method="get", path="/idmprofile")

        return result.json()

    def get(
        self,
        idm_profile_id: int,
    ) -> dict:
        """
        Get IDM template information for the specified ID.

        Parameters:
        - idm_profile_id (int): The unique identifier for the IDM profile.

        Returns:
        - dict: A dictionary representing the details of the IDM profile
        """
        result = self._req(method="get", path=f"/icapServers/{idm_profile_id}")

        return result.json()

    def list_lite(self, active_only: Optional[bool] = False) -> List[dict]:
        """
        Retrieve a list of active IDM templates (or IDM profiles) and their criteria, only.

        Returns:
        - List[dict]: A list of dictionaries, each containing basic info about an IDM profile.
        """
        params = {"activeOnly": active_only}
        result = self._req(method="get", path="/idmprofile/lite", params=params)

        return result.json()


class incident_receivers(Endpoint):
    def list(self) -> List[dict]:
        """
        Retrieve a list of DLP Incident receivers

        Returns:
        - List[dict]: A list of dictionaries representing DLP Incident receivers
        """
        result = self._req(method="get", path="/incidentReceiverServers")

        return result.json()

    def get(
        self,
        receiver_id: int,
    ) -> dict:
        """
        Gets DLP Incident receiver information for the specified ID.

        Parameters:
        - reciever_id (int): The unique identifier for the receiver.

        Returns:
        - dict: A dictionary representing the details of the receiver
        """
        result = self._req(method="get", path=f"/incidentReceiverServers/{receiver_id}")

        return result.json()

    def list_lite(self) -> List[dict]:
        """
        Retrieve a name and ID dictionary for all DLP Incident Receivers.

        Returns:
        - List[dict]: A list of dictionaries, each containing basic info about a receiver server
        """
        result = self._req(method="get", path="/incidentReceiverServers/lite")

        return result.json()


class web_dlp_rules(Endpoint):
    def list(self) -> List[dict]:
        """
        Retrieve a list of Web DLP Rules

        Parameters:
        - search (str): Search criteria to filter the results.

        Returns:
        - List[dict]: A list of dictionaries representing Web DLP Rules.
        """
        result = self._req(method="get", path="/webDlpRules")

        return result.json()

    def get(self, rule_id: int) -> dict:
        """
        Retrieve details of a specific Web DLP Rule by its ID.

        Parameters:
        - rule_id (int): The ID of the Web DLP Rule to retrieve.

        Returns:
        - dict: A dictionary representing the details of the Web DLP Rule.
        """
        result = self._req(method="get", path=f"/webDlpRules/{rule_id}")

        return result.json()

    def list_lite(self) -> List[dict]:
        """
        Retrieve a lightweight list of all Web DLP Rules.

        Returns:
        - List[dict]: A list of dictionaries, each containing basic info about a Web DLP Rule.
        """
        result = self._req(method="get", path="/webDlpRules/lite")

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Create a new Web DLP Rule.

        Parameters:
        - payload (dict): A dictionary containing the details to be created.
        The dictionary should have the following structure:
        {
            "order": int,                               # Order value.
            "protocols": List[str],                      # List of protocols.
            "rank": int,                                # Rank value.
            "description": str,                         # Description.
            "locations": List[Dict],                    # List of location details.
            "locationGroups": List[Dict],               # List of location group details.
            "groups": List[Dict],                       # List of groups.
            "departments": List[Dict],                  # List of departments.
            "users": List[Dict],                        # List of users.
            "urlCategories": List[Dict],                # List of URL categories.
            "dlpEngines": List[Dict],                   # List of DLP engines.
            "fileTypes": List[str],                     # List of file types.
            "cloudApplications": List[str],             # List of cloud applications.
            "minSize": int,                             # Minimum size.
            "action": str,                              # Action value.
            "state": str,                               # State value, e.g., "DISABLED".
            "timeWindows": List[Dict],                  # List of time windows.
            "auditor": Dict,                            # Auditor details.
            "externalAuditorEmail": str,                # External auditor's email.
            "notificationTemplate": Dict,               # Notification template details.
            "matchOnly": bool,                          # Match only flag.
            "lastModifiedTime": int,                    # Last modified time.
            "lastModifiedBy": Dict,                     # Details of the last modifier.
            "icapServer": Dict,                         # ICAP server details.
            "withoutContentInspection": bool,           # Flag for content inspection.
            "name": str,                                # Name.
            "labels": List[Dict],                       # List of labels.
            "ocrEnabled": bool,                         # OCR enabled flag.
            "excludedGroups": List[Dict],               # List of excluded groups.
            "excludedDepartments": List[Dict],          # List of excluded departments.
            "excludedUsers": List[Dict],                # List of excluded users.
            "dlpDownloadScanEnabled": bool,             # DLP download scan enabled flag.
            "zscalerIncidentReceiver": bool,            # Zscaler incident receiver flag.
            "zccNotificationsEnabled": bool             # ZCC notifications enabled flag.
        }


        Returns:
        - Response: A Response object containing the server's response to the creation request.
        """
        result = self._req(method="post", path="/webDlpRules", json=payload)

        return result

    def update(self, rule_id: int, payload: dict) -> Response:
        """
        Update an existing Web DLP Rule.

        Parameters:
        - rule_id (int): The ID of the Web DLP Rule to update.
        - payload (dict): A dictionary containing the details to be updated.
        The dictionary should have the following structure:
        {
            "order": int,                               # Order value.
            "protocols": List[str],                      # List of protocols.
            "rank": int,                                # Rank value.
            "description": str,                         # Description.
            "locations": List[Dict],                    # List of location details.
            "locationGroups": List[Dict],               # List of location group details.
            "groups": List[Dict],                       # List of groups.
            "departments": List[Dict],                  # List of departments.
            "users": List[Dict],                        # List of users.
            "urlCategories": List[Dict],                # List of URL categories.
            "dlpEngines": List[Dict],                   # List of DLP engines.
            "fileTypes": List[str],                     # List of file types.
            "cloudApplications": List[str],             # List of cloud applications.
            "minSize": int,                             # Minimum size.
            "action": str,                              # Action value.
            "state": str,                               # State value, e.g., "DISABLED".
            "timeWindows": List[Dict],                  # List of time windows.
            "auditor": Dict,                            # Auditor details.
            "externalAuditorEmail": str,                # External auditor's email.
            "notificationTemplate": Dict,               # Notification template details.
            "matchOnly": bool,                          # Match only flag.
            "lastModifiedTime": int,                    # Last modified time.
            "lastModifiedBy": Dict,                     # Details of the last modifier.
            "icapServer": Dict,                         # ICAP server details.
            "withoutContentInspection": bool,           # Flag for content inspection.
            "name": str,                                # Name.
            "labels": List[Dict],                       # List of labels.
            "ocrEnabled": bool,                         # OCR enabled flag.
            "excludedGroups": List[Dict],               # List of excluded groups.
            "excludedDepartments": List[Dict],          # List of excluded departments.
            "excludedUsers": List[Dict],                # List of excluded users.
            "dlpDownloadScanEnabled": bool,             # DLP download scan enabled flag.
            "zscalerIncidentReceiver": bool,            # Zscaler incident receiver flag.
            "zccNotificationsEnabled": bool             # ZCC notifications enabled flag.
        }

        Returns:
        - Response: A Response object containing the server's response to the update request.
        """
        result = self._req(method="put", path=f"/webDlpRules/{rule_id}", json=payload)

        return result

    def delete(self, rule_id: int) -> Response:
        """
        Delete a specific Web DLP Rule by its ID.

        Parameters:
        - rule_id (int): The ID of the Web DLP Rule to delete.

        Returns:
        - Response: A Response object containing the server's response to the delete request.
        """
        result = self._req(method="delete", path=f"/webDlpRules/{rule_id}")

        return result
