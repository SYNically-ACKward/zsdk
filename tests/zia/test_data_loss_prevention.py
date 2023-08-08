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


# For data_loss_prevention.web_dlp_rules
@pytest.mark.web_dlp_rules
def test_web_dlp_rules_get(tenant):
    pass


@pytest.mark.web_dlp_rules
def test_web_dlp_rules_create(tenant):
    pass


@pytest.mark.web_dlp_rules
def test_web_dlp_rules_update(tenant):
    pass


@pytest.mark.web_dlp_rules
def test_web_dlp_rules_list(tenant):
    pass


@pytest.mark.web_dlp_rules
def test_web_dlp_rules_list_lite(tenant):
    pass


@pytest.mark.web_dlp_rules
def test_web_dlp_rules_delete(tenant):
    pass


# For data_loss_prevention.incident_receivers
@pytest.mark.incident_receivers
def test_incident_receivers_get(tenant):
    pass


@pytest.mark.incident_receivers
def test_incident_receivers_list(tenant):
    pass


@pytest.mark.incident_receivers
def test_incident_receivers_list_lite(tenant):
    pass


# For data_loss_prevention.idm_profiles
@pytest.mark.idm_profiles
def test_idm_profiles_get(tenant):
    pass


@pytest.mark.idm_profiles
def test_idm_profiles_list(tenant):
    pass


@pytest.mark.idm_profiles
def test_idm_profiles_list_lite(tenant):
    pass


# For data_loss_prevention.icap_servers
@pytest.mark.icap_servers
def test_icap_servers_get(tenant):
    pass


@pytest.mark.icap_servers
def test_icap_servers_list(tenant):
    pass


@pytest.mark.icap_servers
def test_icap_servers_list_lite(tenant):
    pass


# For data_loss_prevention.dlp_notification_templates
@pytest.mark.dlp_notification_templates
def test_dlp_notification_templates_get(tenant):
    pass


@pytest.mark.dlp_notification_templates
def test_dlp_notification_templates_create(tenant):
    pass


@pytest.mark.dlp_notification_templates
def test_dlp_notification_templates_update(tenant):
    pass


@pytest.mark.dlp_notification_templates
def test_dlp_notification_templates_list(tenant):
    pass


@pytest.mark.dlp_notification_templates
def test_dlp_notification_templates_delete(tenant):
    pass


# For data_loss_prevention.dlp_dictionaries
@pytest.mark.dlp_dictionaries
def test_dlp_dictionaries_get(tenant):
    pass


@pytest.mark.dlp_dictionaries
def test_dlp_dictionaries_create(tenant):
    pass


@pytest.mark.dlp_dictionaries
def test_dlp_dictionaries_update(tenant):
    pass


@pytest.mark.dlp_dictionaries
def test_dlp_dictionaries_list(tenant):
    pass


@pytest.mark.dlp_dictionaries
def test_dlp_dictionaries_delete(tenant):
    pass


@pytest.mark.dlp_dictionaries
def test_dlp_dictionaries_list_lite(tenant):
    pass


@pytest.mark.dlp_dictionaries
def test_dlp_dictionaries_validate(tenant):
    pass


# For data_loss_prevention.dlp_engines
@pytest.mark.dlp_engines
def test_dlp_engines_get(tenant):
    pass


@pytest.mark.dlp_engines
def test_dlp_engines_create(tenant):
    pass


@pytest.mark.dlp_engines
def test_dlp_engines_update(tenant):
    pass


@pytest.mark.dlp_engines
def test_dlp_engines_list(tenant):
    pass


@pytest.mark.dlp_engines
def test_dlp_engines_delete(tenant):
    pass


@pytest.mark.dlp_engines
def test_dlp_engines_list_lite(tenant):
    pass


@pytest.mark.dlp_engines
def test_dlp_engines_validate(tenant):
    pass


@pytest.mark.dlp_edm
def test_dlp_edm_list(tenant):
    pass


@pytest.mark.dlp_edm
def test_dlp_edm_list_lite(tenant):
    pass
