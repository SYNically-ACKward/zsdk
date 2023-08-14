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


@pytest.fixture(scope="module")
def test_user_data(tenant):
    return {
        "name": "pytest user",
        "email": "pytest@tng-lab.org",
        "groups": [
            random.choice(
                [
                    {"name": group["name"], "id": group["id"]}
                    for group in tenant.groups.list()
                ]
            )
        ],
        "department": random.choice(
            [
                {"name": dept["name"], "id": dept["id"]}
                for dept in tenant.departments.list()
            ]
        ),
        "password": "Zscaler!123",
    }


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
    data = tenant.groups.list()
    assert type(data) is list
    assert len(data) > 0


@pytest.mark.groups
def test_get_groups(tenant):
    groups = [group.get("id") for group in tenant.groups.list()]
    group = tenant.groups.get(random.choice(groups))
    assert type(group) is dict
    assert group.get("id") in groups


# users under user_management
@pytest.mark.users
def test_get_users(tenant):
    users = [user.get("id") for user in tenant.users.list()]
    user = tenant.users.get(random.choice(users))
    assert type(user) is dict
    assert user.get("id") in users


@pytest.mark.users
def test_create_users(tenant, test_user_data):
    data = tenant.users.create(test_user_data)
    assert data.status_code == 200
    assert "pytest@tng-lab.org" in data.json().get("email")


@pytest.mark.users
def test_update_users(tenant):
    user = next(
        (user for user in tenant.users.list() if user["email"] == "pytest@tng-lab.org"),
        None,
    )

    update_data = user

    update_data["name"] = f"{user.get('name')} Update"

    result = tenant.users.update(user.get("id"), update_data)

    assert result.status_code == 200
    assert "Update" in result.json().get("name")


@pytest.mark.users
def test_list_users(tenant):
    data = tenant.users.list()
    assert type(data) is list
    assert len(data) > 0


@pytest.mark.users
def test_delete_users(tenant):
    user = next(
        (user for user in tenant.users.list() if user["email"] == "pytest@tng-lab.org"),
        None,
    )

    result = tenant.users.delete(user.get("id"))

    assert result.status_code == 204


@pytest.mark.users
def test_bulk_delete_users(tenant):  # TODO
    pass


# auditors under user_management
@pytest.mark.auditors
def test_list_auditors(tenant):
    result = tenant.auditors.list()
    assert type(result) is list


def test_activate(tenant):
    tenant.activate_changes()
