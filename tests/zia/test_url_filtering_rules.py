import os
import pytest
import random
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


@pytest.fixture
def filtering_rule_data(tenant):
    return {
        "name": "Pytest URLF Rule",
        "order": 1,
        "rank": 7,
        "state": "ENABLED",
        "urlCategories": ["OTHER_ADULT_MATERIAL"],
        "action": "ALLOW",
        "protocols": ["HTTPS_RULE"],
        "requestMethods": ["GET"],
    }


@pytest.mark.url_filtering_rules
def test_url_filtering_rules_list(tenant):
    result = tenant.url_filtering_rules.list()
    assert type(result) is list
    assert type(result[0]) is dict


@pytest.mark.url_filtering_rules
def test_url_filtering_rules_get(tenant):
    filtering_rule = random.choice(
        [rule.get("id") for rule in tenant.url_filtering_rules.list()]
    )

    result = tenant.url_filtering_rules.get(filtering_rule)
    assert type(result) is dict
    assert result.get("id") == filtering_rule


@pytest.mark.url_filtering_rules
def test_url_filtering_rules_create(tenant, filtering_rule_data):
    result = tenant.url_filtering_rules.create(filtering_rule_data)
    assert result.status_code == 200
    assert type(result.json()) is dict
    assert "Pytest URLF Rule" in result.json().get("name")


@pytest.mark.url_filtering_rules
def test_url_filtering_rules_update(tenant):
    rule = [
        rule
        for rule in tenant.url_filtering_rules.list()
        if rule.get("name") == "Pytest URLF Rule"
    ]

    update_data = rule[0]
    update_data["name"] = f"{update_data.get('name')} - Updated"

    result = tenant.url_filtering_rules.update(update_data.get("id"), update_data)

    assert result.status_code in [200, 204]


@pytest.mark.url_filtering_rules
def test_url_filtering_rules_delete(tenant):
    rule = [
        rule
        for rule in tenant.url_filtering_rules.list()
        if rule.get("name") == "Pytest URLF Rule - Updated"
    ]

    result = tenant.url_filtering_rules.delete(rule[0].get("id"))
    assert result.status_code == 204


def test_activate(tenant):
    tenant.activate_changes()
