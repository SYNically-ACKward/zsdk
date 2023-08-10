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


@pytest.mark.sandbox_report
@pytest.mark.sandbox_report_sandbox_report_quota
def test_sandbox_report_quota_get():
    pass


@pytest.mark.sandbox_report
@pytest.mark.sandbox_report_sandbox_report_file
def test_sandbox_report_file_get():
    pass
