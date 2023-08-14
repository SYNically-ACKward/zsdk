import os
import time
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


@pytest.mark.user_authentication_settings
def test_user_authentication_settings_list(tenant):
    result = tenant.user_authentication_settings.list()
    assert type(result) is dict
    assert type(result.get('urls')) is list


@pytest.mark.user_authentication_settings
def test_user_authentication_settings_update(tenant):
    update_urls = ["pytest.example.com"]
    result = tenant.user_authentication_settings.update(update_urls)
    assert type(result) is dict
    assert type(result.get('urls')) is list
    assert len(result.get('urls')) != 0

    reset_result = tenant.user_authentication_settings.update(update_urls, action="REMOVE_FROM_LIST")
    assert type(reset_result) is dict
    assert len(reset_result.get('urls')) != 0

    reset_settings = tenant.user_authentication_settings.list()
    assert type(reset_settings) is dict
    assert len(reset_settings.get('urls')) == 0


def test_activate(tenant):
    tenant.activate_changes()
