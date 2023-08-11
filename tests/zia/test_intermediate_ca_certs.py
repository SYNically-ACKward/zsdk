import os
import pytest
import tomli
from zsdk.zia import zia

app_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(app_dir, "config.toml")

with open(config_path, "rb") as cf:
    config = tomli.load(cf)


@pytest.fixture(scope="module")
def tenant():
    return zia(
        config["PARENT"]["username"],
        config["PARENT"]["password"],
        config["PARENT"]["api_key"],
        config["PARENT"]["cloudId"],
    )


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_create(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_create_csr(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_create_key_pair(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_delete(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_finalize(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_get(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_get_attestation(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_get_csr(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_get_lite(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_get_public_key(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_get_ready_certs(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_list(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_list_lite(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_show_csr(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_show_signed_cert(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_update(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_update_default(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_upload_cert(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_upload_cert_chain(tenant):
    pass


@pytest.mark.intermediate_ca_certificates
def test_intermediate_ca_certificates_verify_key_attestation(tenant):
    pass
