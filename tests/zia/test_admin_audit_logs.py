import os
import pytest
import tomli
import time
from zsdk.zia import zia
from datetime import datetime

app_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(app_dir, "config.toml")

with open(config_path, "rb") as cf:
    config = tomli.load(cf)

current_timestamp = datetime.now().timestamp() * 1000
now_minus_ten = current_timestamp - (10 * 60 * 1000)


@pytest.fixture(scope="module")
def tenant():
    return zia(
        config["PARENT"]["username"],
        config["PARENT"]["password"],
        config["PARENT"]["api_key"],
        config["PARENT"]["cloudId"],
    )


def test_create(tenant):
    data = tenant.admin_audit_logs.create(now_minus_ten, current_timestamp)
    assert data.status_code in [204, 200]


def test_status(tenant):
    create_data = tenant.admin_audit_logs.create(now_minus_ten, current_timestamp)
    assert create_data.status_code in [204, 200]

    data = tenant.admin_audit_logs.status()
    assert type(data) is dict


def test_delete(tenant):
    create_data = tenant.admin_audit_logs.create(now_minus_ten, current_timestamp)
    assert create_data.status_code in [204, 200]

    data = tenant.admin_audit_logs.delete()
    assert data.status_code in [204, 200]


def test_download(tenant):
    create_data = tenant.admin_audit_logs.create(now_minus_ten, current_timestamp)
    assert create_data.status_code in [204, 200]

    while tenant.admin_audit_logs.status().get("status") != "COMPLETE":
        time.sleep(2)
    data = tenant.admin_audit_logs.download()
    assert type(data) is str
