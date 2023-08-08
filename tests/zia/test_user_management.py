import os
import pytest
import tomli
from zsdk.zia import zia
import random

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


# departments under user_management
@pytest.mark.departments
def test_get(tenant):
    depts = [dept.get("id") for dept in tenant.departments.list()]
    dept = tenant.departments.get(random.choice(depts))
    assert type(dept) is dict


@pytest.mark.departments
def test_list(tenant):
    data = tenant.departments.list()
    assert type(data) is list
    assert len(data) != 0


# groups under user_management
@pytest.mark.groups
def test_list_groups(tenant):
    pass


@pytest.mark.groups
def test_get_groups(tenant):
    pass


# users under user_management
@pytest.mark.users
def test_get_users(tenant):
    pass


@pytest.mark.users
def test_create_users(tenant):
    pass


@pytest.mark.users
def test_update_users(tenant):
    pass


@pytest.mark.users
def test_list_users(tenant):
    pass


@pytest.mark.users
def test_delete_users(tenant):
    pass


@pytest.mark.users
def test_bulk_delete_users(tenant):
    pass


# auditors under user_management
@pytest.mark.auditors
def test_list_auditors(tenant):
    pass
