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


@pytest.mark.url_categories
def test_url_categories_list(tenant):
    pass


@pytest.mark.url_categories
def test_url_categories_list_lite(tenant):
    pass


@pytest.mark.url_categories
def test_url_categories_get(tenant):
    pass


@pytest.mark.url_categories
def test_url_categories_create(tenant):
    pass


@pytest.mark.url_categories
def test_url_categories_update(tenant):
    pass


@pytest.mark.url_categories
def test_url_categories_delete(tenant):
    pass


@pytest.mark.url_categories
def test_url_categories_get_quota(tenant):
    pass


@pytest.mark.url_categories
def test_url_categories_lookup(tenant):
    pass
