from zsdk.api import Endpoint
from zsdk.utilities import snake_to_camel
from requests import Response
from typing import List, Optional


class intermediate_ca_certificates(Endpoint):
    def list(
        self, page: Optional[int] = 1, page_size: Optional[int] = 100
    ) -> List[dict]:
        """
        Gets the list of intermediate CA certificates added for SSL inspection.

        Parameters:
        - page (optional, int): Specifies the page offset.
        - page_size (optional, int): Specifies the page size.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(
            method="get", path="/intermediateCaCertificate", params=params
        )

        return result.json()

    def create(self, payload: dict) -> Response:
        """
        Adds a custom intermediate CA certificate that can be used for SSL inspection.

        Parameters:
        - payload (dict): Intermediate CA certificate information.
        Example:
            payload = {
                        "name": "string", # Required
                        "type": "ZSCALER", # Required. Valid Values: "ZSCALER", "CUSTOM_SW", "CUSTOM_HSM"
                        "region": "GLOBAL", # Valid Values: "GLOBAL", "ASIA", "EUROPE", "US"
                        "status": "ENABLED", # Valid Values: "ENABLED", "DISABLED"
                        "defaultCertificate": bool,
                        "description": "string"
                        }
        """
        result = self._req(
            method="post", path="/intermediateCaCertificate", json=payload
        )

        return result

    def get_attestation(self, cert_id: int) -> Response:
        """
        Downloads the attestation bundle produced by the HSM solution for the specified intermediate CA certificate ID.
            The attestation bundle can be used to verify the HSM key attributes and the validity of the certificate.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        """
        result = self._req(
            method="get",
            path=f"/intermediateCaCertificate/downloadAttestation/{cert_id}",
        )

        return result

    def get_csr(self, cert_id: int) -> Response:
        """
        Downloads a Certificate Signing Request (CSR) for the specified ID.
            To perform this operation, a CSR must have already been generated.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        """
        result = self._req(
            method="get", path=f"/intermediateCaCertificate/downloadCsr/{cert_id}"
        )

        return result

    def get_public_key(self, cert_id: int) -> Response:
        """
        Downloads the public key in the HSM key pair for the intermediate CA certificate with the specified ID.
        To perform this operation, a HSM key pair must have already been generated.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        """
        result = self._req(
            method="get", path=f"/intermediateCaCertificate/downloadPublicKey/{cert_id}"
        )

        return result

    def finalize(self, cert_id: int) -> Response:
        """
        Finalizes the intermediate CA certificate with the specified ID.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        """
        result = self._req(
            method="post", path=f"/intermediateCaCertificate/finalizeCert/{cert_id}"
        )

        return result

    def create_csr(self, cert_id: int, payload: dict) -> Response:
        """
        Generates a Certificate Signing Request (CSR) for the custom intermediate CA certificate with the specified ID.
            You can send the generated CSR to your Certificate Authority (CA) to sign as a subordinate CA certificate or
            intermediate CA certificate. The subordinate CA can be an intermediate or an issuing CA.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        - payload (dict): Certificate Signing Request (CSR) information.

        Example:
        - payload = {
            "csrFileName": "string",
            "commName": "string",
            "orgName": "string",
            "deptName": "string",
            "city": "string",
            "state": "string",
            "country": "NONE",
            "signatureAlgorithm": "SHA256"
        }
        """
        result = self._req(
            method="post",
            path=f"/intermediateCaCertificate/generateCsr/{cert_id}",
            json=payload,
        )

        return result

    def create_key_pair(self, cert_id: int) -> Response:
        """
        Generates a HSM key pair for the custom intermediate CA certificate with the specified ID.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        """
        result = self._req(
            method="post", path=f"/intermediateCaCertificate/keyPair/{cert_id}"
        )

        return result

    def list_lite(
        self, page: Optional[int] = 1, page_size: Optional[int] = 100
    ) -> List[dict]:
        """
        Gets the list of intermediate CA certificates added for SSL inspection.

        Parameters:
        - page (optional, int): Specifies the page offset.
        - page_size (optional, int): Specifies the page size.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(
            method="get", path="/intermediateCaCertificate/lite", params=params
        )

        return result.json()

    def get_lite(self, cert_id: int) -> Response:
        """
        Gets information about the intermediate CA certificate with the specified ID.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        """
        result = self._req(
            method="post", path=f"/intermediateCaCertificate/lite/{cert_id}"
        )

        return result.json()

    def update_default(self, cert_id: int) -> Response:
        """
        Updates the intermediate CA certificate information for the specified ID to mark it
            as the default intermediate certificate. Only one intermediate certificate can be
            marked as the default certificate at a time.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        """
        result = self._req(
            method="put", path=f"/intermediateCaCertificate/makeDefault/{cert_id}"
        )

        return result

    def get_ready_certs(
        self, page: Optional[int] = 1, page_size: Optional[int] = 100
    ) -> List[dict]:
        """
        Gets the list of intermediate CA certificates that are ready to use for SSL inspection.

        Parameters:
        - page (optional, int): Specifies the page offset.
        - page_size (optional, int): Specifies the page size.
        """
        args = locals()
        params = {
            key: value
            for key, value in args.items()
            if value is not None and key != "self"
        }
        params = {snake_to_camel(key): value for key, value in params.items()}

        result = self._req(
            method="get", path="/intermediateCaCertificate/readyToUse", params=params
        )

        return result.json()

    def show_signed_cert(self, cert_id: int) -> List[dict]:
        """
        Shows information about the signed intermediate CA certificate with the specified ID.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        """

        result = self._req(
            method="get", path=f"/intermediateCaCertificate/showCert/{cert_id}"
        )

        return result.json()

    def show_csr(self, cert_id: int) -> List[dict]:
        """
        Shows information about the Certificate Signing Request (CSR) for the specified ID.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        """

        result = self._req(
            method="get", path=f"/intermediateCaCertificate/showCert/{cert_id}"
        )

        return result.json()

    def upload_cert(self, cert_id: int, cert_path: str) -> Response:
        """
        Uploads a custom intermediate CA certificate signed by your Certificate Authority (CA) for SSL inspection.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        - cert_path (str): Path to the certificate file
        """
        payload = {"Content-Type": "multipart/form-data"}

        files = [
            ("fileUpload", ("file", open(cert_path), "rb"), "application/octet-stream")
        ]
        result = self._req(
            method="post",
            path=f"/intermediateCaCertificate/uploadCert/{cert_id}",
            data=payload,
            files=files,
        )

        return result

    def upload_cert_chain(self, cert_id: int, cert_chain_path: str) -> Response:
        """
        Uploads a custom intermediate CA certificate signed by your Certificate Authority (CA) for SSL inspection.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        - cert_chain_path (str): Path to the certificate chain file (PEM)
        """
        payload = {"Content-Type": "multipart/form-data"}

        files = [
            (
                "fileUpload",
                ("file", open(cert_chain_path), "rb"),
                "application/octet-stream",
            )
        ]
        result = self._req(
            method="post",
            path=f"/intermediateCaCertificate/uploadCertChain/{cert_id}",
            data=payload,
            files=files,
        )

        return result

    def verify_key_attestation(self, cert_id: int) -> dict:
        """
        Verifies the attestation for the HSM keys generated for the specified ID.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        """
        result = self._req(
            method="post",
            path=f"/intermediateCaCertificate/verifyKeyAttestation/{cert_id}",
        )

        return result.json()

    def get(self, cert_id: int) -> dict:
        """
        Gets intermediate CA certificate information for the specified ID.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        """
        result = self._req(method="get", path=f"/intermediateCaCertificate/{cert_id}")

        return result.json()

    def update(self, cert_id: int, payload: dict) -> Response:
        """
        Updates a custom intermediate CA certificate that can be used for SSL inspection.

        Parameters:
        - payload (dict): Intermediate CA certificate information.
        Example:
            payload = {
                        "name": "string", # Required
                        "type": "ZSCALER", # Required. Valid Values: "ZSCALER", "CUSTOM_SW", "CUSTOM_HSM"
                        "region": "GLOBAL", # Valid Values: "GLOBAL", "ASIA", "EUROPE", "US"
                        "status": "ENABLED", # Valid Values: "ENABLED", "DISABLED"
                        "defaultCertificate": bool,
                        "description": "string"
                        }
        """
        result = self._req(
            method="put", path=f"/intermediateCaCertificate/{cert_id}", json=payload
        )

        return result

    def delete(self, cert_id: int) -> Response:
        """
        Deletes the intermediate CA certificate with the specified ID.
            The default intermediate certificate cannot be deleted.

        Parameters:
        - cert_id (int): The unique identifier for the intermediate CA certificate.
        """
        result = self._req(
            method="delete", path=f"/intermediateCaCertificate/{cert_id}"
        )

        return result
