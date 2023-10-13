import os
import pytest
import tomli
import random
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
def test_locations_list(tenant):
    data = tenant.locations.list()
    assert type(data) is list
    assert len(data) != 0


@pytest.mark.locations
@pytest.mark.locations_locations
def test_locations_list_lite():
    data = tenant.locations.list_lite()
    assert type(data) is list
    assert len(data) != 0


@pytest.mark.locations
@pytest.mark.locations_locations
def test_locations_get():
    locs = tenant.locations.list()
    loc = random.choice([loc.get('id') for loc in locs])
    data = tenant.locations.get(loc)
    assert type(data) is dict


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
