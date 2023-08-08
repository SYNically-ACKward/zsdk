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


# firewall_filtering_rules
@pytest.mark.firewall_filtering_rules
def test_list_firewall_filtering_rules(tenant):
    pass


@pytest.mark.firewall_filtering_rules
def test_get_firewall_filtering_rules(tenant):
    pass


@pytest.mark.firewall_filtering_rules
def test_create_firewall_filtering_rules(tenant):
    pass


@pytest.mark.firewall_filtering_rules
def test_update_firewall_filtering_rules(tenant):
    pass


@pytest.mark.firewall_filtering_rules
def test_delete_firewall_filtering_rules(tenant):
    pass


# ip_destination_groups
@pytest.mark.ip_destination_groups
def test_list_ip_destination_groups(tenant):
    pass


@pytest.mark.ip_destination_groups
def test_get_ip_destination_groups(tenant):
    pass


@pytest.mark.ip_destination_groups
def test_create_ip_destination_groups(tenant):
    pass


@pytest.mark.ip_destination_groups
def test_update_ip_destination_groups(tenant):
    pass


@pytest.mark.ip_destination_groups
def test_list_lite_ip_destination_groups(tenant):
    pass


@pytest.mark.ip_destination_groups
def test_delete_ip_destination_groups(tenant):
    pass


# ip_source_groups
@pytest.mark.ip_source_groups
def test_list_ip_source_groups(tenant):
    pass


@pytest.mark.ip_source_groups
def test_get_ip_source_groups(tenant):
    pass


@pytest.mark.ip_source_groups
def test_create_ip_source_groups(tenant):
    pass


@pytest.mark.ip_source_groups
def test_update_ip_source_groups(tenant):
    pass


@pytest.mark.ip_source_groups
def test_list_lite_ip_source_groups(tenant):
    pass


@pytest.mark.ip_source_groups
def test_delete_ip_source_groups(tenant):
    pass


# ipv6_destination_groups
@pytest.mark.ipv6_destination_groups
def test_list_ipv6_destination_groups(tenant):
    pass


@pytest.mark.ipv6_destination_groups
def test_list_lite_ipv6_destination_groups(tenant):
    pass


# ipv6_source_groups
@pytest.mark.ipv6_source_groups
def test_list_ipv6_source_groups(tenant):
    pass


@pytest.mark.ipv6_source_groups
def test_list_lite_ipv6_source_groups(tenant):
    pass


# network_application_groups
@pytest.mark.network_application_groups
def test_list_network_application_groups(tenant):
    pass


@pytest.mark.network_application_groups
def test_get_network_application_groups(tenant):
    pass


@pytest.mark.network_application_groups
def test_create_network_application_groups(tenant):
    pass


@pytest.mark.network_application_groups
def test_update_network_application_groups(tenant):
    pass


@pytest.mark.network_application_groups
def test_list_lite_network_application_groups(tenant):
    pass


@pytest.mark.network_application_groups
def test_delete_network_application_groups(tenant):
    pass


# network_applications
@pytest.mark.network_applications
def test_get_network_applications(tenant):
    pass


@pytest.mark.network_applications
def test_list_network_applications(tenant):
    pass


# network_service_groups
@pytest.mark.network_service_groups
def test_list_network_service_groups(tenant):
    pass


@pytest.mark.network_service_groups
def test_get_network_service_groups(tenant):
    pass


@pytest.mark.network_service_groups
def test_create_network_service_groups(tenant):
    pass


@pytest.mark.network_service_groups
def test_update_network_service_groups(tenant):
    pass


@pytest.mark.network_service_groups
def test_list_lite_network_service_groups(tenant):
    pass


@pytest.mark.network_service_groups
def test_delete_network_service_groups(tenant):
    pass


# network_services
@pytest.mark.network_services
def test_list_network_services(tenant):
    pass


@pytest.mark.network_services
def test_get_network_services(tenant):
    pass


@pytest.mark.network_services
def test_create_network_services(tenant):
    pass


@pytest.mark.network_services
def test_update_network_services(tenant):
    pass


@pytest.mark.network_services
def test_list_lite_network_services(tenant):
    pass


@pytest.mark.network_services
def test_delete_network_services(tenant):
    pass


# time_windows
@pytest.mark.time_windows
def test_list_time_windows(tenant):
    pass


@pytest.mark.time_windows
def test_list_lite_time_windows(tenant):
    pass
