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


@pytest.mark.rule_labels
@pytest.mark.rule_labels_rule_labels
def test_rule_labels_list():
    pass


@pytest.mark.rule_labels
@pytest.mark.rule_labels_rule_labels
def test_rule_labels_get():
    pass


@pytest.mark.rule_labels
@pytest.mark.rule_labels_rule_labels
def test_rule_labels_create():
    pass


@pytest.mark.rule_labels
@pytest.mark.rule_labels_rule_labels
def test_rule_labels_update():
    pass


@pytest.mark.rule_labels
@pytest.mark.rule_labels_rule_labels
def test_rule_labels_delete():
    pass
