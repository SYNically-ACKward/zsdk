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


# For security_policy.allowlist
@pytest.mark.security_policy
@pytest.mark.security_policy_allowlist
def test_allowlist_list():
    pass


@pytest.mark.security_policy
@pytest.mark.security_policy_allowlist
def test_allowlist_update():
    pass


# For security_policy.denylist
@pytest.mark.security_policy
@pytest.mark.security_policy_denylist
def test_denylist_list():
    pass


@pytest.mark.security_policy
@pytest.mark.security_policy_denylist
def test_denylist_update():
    pass


# For security_policy.blacklist
@pytest.mark.security_policy
@pytest.mark.security_policy_blacklist
def test_blacklist_update():
    pass
