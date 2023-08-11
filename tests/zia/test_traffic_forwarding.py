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


# Tests for traffic_forwarding.gre_tunnels


@pytest.mark.traffic_forwarding
@pytest.mark.gre_tunnels
def test_gre_tunnels_list(tenant):
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.gre_tunnels
def test_gre_tunnels_get(tenant):
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.gre_tunnels
def test_gre_tunnels_create(tenant):
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.gre_tunnels
def test_gre_tunnels_update(tenant):
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.gre_tunnels
def test_gre_tunnels_delete(tenant):
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.gre_tunnels
def test_gre_tunnels_get_internal_ips(tenant):
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.gre_tunnels
def test_gre_tunnels_get_org_ips(tenant):
    pass


# Tests for traffic_forwarding.ipv6


@pytest.mark.traffic_forwarding
@pytest.mark.ipv6
def test_ipv6_get(tenant):
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.ipv6
def test_ipv6_get_nat64(tenant):
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.ipv6
def test_ipv6_get_dns64(tenant):
    pass


# Tests for traffic_forwarding.static_ips


@pytest.mark.traffic_forwarding
@pytest.mark.static_ips
def test_static_ips_list():
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.static_ips
def test_static_ips_get():
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.static_ips
def test_static_ips_create():
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.static_ips
def test_static_ips_update():
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.static_ips
def test_static_ips_delete():
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.static_ips
def test_static_ips_validate():
    pass


# Tests for traffic_forwarding.vips


@pytest.mark.traffic_forwarding
@pytest.mark.vips
def test_vips_list():
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.vips
def test_vips_list_by_dc():
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.vips
def test_vips_list_recommended():
    pass


# Tests for traffic_forwarding.vpn_credentials


@pytest.mark.traffic_forwarding
@pytest.mark.vpn_credentials
def test_vpn_credentials_list():
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.vpn_credentials
def test_vpn_credentials_get():
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.vpn_credentials
def test_vpn_credentials_create():
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.vpn_credentials
def test_vpn_credentials_update():
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.vpn_credentials
def test_vpn_credentials_delete():
    pass


@pytest.mark.traffic_forwarding
@pytest.mark.vpn_credentials
def test_vpn_credentials_bulk_delete():
    pass
