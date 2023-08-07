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


def test_list(tenant):
    data = tenant.admin_users.list()
    assert type(data) is list
    assert len(data) != 0


def test_create(tenant):
    admin_data = {
        "loginName": "pytest@tng-lab.org",
        "userName": "Pytest",
        "password": "Zscaler!123",
        "role": {"id": 59804, "name": "Super Admin"},
        "email": "pytest@tng-lab.org",
        "adminScopeType": "ORGANIZATION",
        "passwordLoginPermitted": "Yes",
        "isPasswordLoginAllowed": True,
    }
    data = tenant.admin_users.create(admin_data)
    assert data.status_code == 200


def test_delete(tenant):
    id = tenant.admin_users.list(search="pytest@tng-lab.org")[0].get("id")
    data = tenant.admin_users.delete(id)
    assert data.status_code == 204


def test_activate(tenant):
    data = tenant.activate_changes()
    assert data.status_code == 200
