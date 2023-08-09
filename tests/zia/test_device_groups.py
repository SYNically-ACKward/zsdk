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


# device_groups
@pytest.mark.device_groups
def test_device_groups_list(tenant):
    pass


# devices
@pytest.mark.devices
def test_devices_list(tenant):
    pass


def test_devices_list_lite(tenant):
    pass
