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


@pytest.mark.locations
@pytest.mark.locations_locations
def test_locations_list():
    pass


@pytest.mark.locations
@pytest.mark.locations_locations
def test_locations_list_lite():
    pass


@pytest.mark.locations
@pytest.mark.locations_locations
def test_locations_get():
    pass


@pytest.mark.locations
@pytest.mark.locations_locations
def test_locations_create():
    pass


@pytest.mark.locations
@pytest.mark.locations_locations
def test_locations_update():
    pass


@pytest.mark.locations
@pytest.mark.locations_locations
def test_locations_delete():
    pass


@pytest.mark.locations
@pytest.mark.locations_locations
def test_locations_bulk_delete():
    pass


@pytest.mark.locations
@pytest.mark.locations_sublocations
def test_sublocations_list():
    pass


@pytest.mark.locations
@pytest.mark.locations_location_groups
def test_location_groups_list():
    pass


@pytest.mark.locations
@pytest.mark.locations_location_groups
def test_location_groups_list_lite():
    pass


@pytest.mark.locations
@pytest.mark.locations_location_groups
def test_location_groups_count():
    pass


@pytest.mark.locations
@pytest.mark.locations_location_groups
def test_location_groups_get():
    pass


@pytest.mark.locations
@pytest.mark.locations_location_groups
def test_location_groups_get_lite():
    pass
