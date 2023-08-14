import logging
import time

import requests
from requests import Response

from zsdk.utilities import call

from .admin_roles import admin_roles
from .admin_users import admin_users
from .admin_audit_logs import admin_audit_logs
from .app_total import app_total
from .device_groups import device_groups, devices
from .event_logs import event_logs
from .locations import locations, location_groups, sublocations
from .rule_labels import rule_labels
from .sandbox_report import sandbox_report_file, sandbox_report_quota
from .sandbox_settings import sandbox_settings
from .sandbox_submission import sandbox_submission
from .security_policy_settings import allowlist, denylist, blacklist
from .traffic_forwarding import gre_tunnels, ipv6, static_ips, vips, vpn_credentials
from .url_categories import url_categories
from .url_filtering_rules import url_filtering_rules
from .user_authentication_settings import user_authentication_settings
from .user_management import departments, groups, users, auditors
from .firewall_policies import (
    firewall_filtering_rules,
    ip_destination_groups,
    ip_source_groups,
    ipv6_destination_groups,
    ipv6_source_groups,
    network_application_groups,
    network_applications,
    network_service_groups,
    network_services,
    time_windows,
)
from .intermediate_ca_certs import intermediate_ca_certificates
from .data_loss_prevention import (
    web_dlp_rules,
    incident_receivers,
    idm_profiles,
    icap_servers,
    dlp_notification_templates,
    dlp_dictionaries,
    dlp_engines,
    dlp_edm,
)

log = logging.getLogger(__name__)


def _obfuscate_api_key(seed: str) -> list:
    now = int(time.time() * 1000)
    n = str(now)[-6:]
    r = str(int(n) >> 1).zfill(6)
    key = "".join(seed[int(digit)] for digit in n)
    key += "".join(seed[int(digit) + 2] for digit in r)
    return str(now), str(key)


class zia:
    def __init__(
        self,
        username: str,
        password: str,
        api_key: str,
        cloud_name: str,
    ):
        self._session = requests.Session()
        self.username = username
        self.password = password
        self.api_key = api_key
        self.cloud_name = cloud_name
        self._base_url = f"https://zsapi.{self.cloud_name}/api/v1"
        self._authenticate()

    def _authenticate(
        self,
    ) -> Response:
        now, key = _obfuscate_api_key(self.api_key)
        result = call(
            session=self._session,
            method="post",
            url=f"{self._base_url}/authenticatedSession",
            json={
                "apiKey": key,
                "username": self.username,
                "password": self.password,
                "timestamp": now,
            },
        )
        log.debug(result)
        return result

    def activate_changes(
        self,
    ) -> Response:
        result = call(
            session=self._session,
            method="post",
            url=f"{self._base_url}/status/activate",
        )

        return result

    @property
    def admin_roles(self) -> admin_roles:
        return admin_roles(session=self._session, base_url=self._base_url)

    @property
    def admin_users(self) -> admin_users:
        return admin_users(session=self._session, base_url=self._base_url)

    @property
    def admin_audit_logs(self) -> admin_audit_logs:
        return admin_audit_logs(session=self._session, base_url=self._base_url)

    @property
    def departments(self) -> departments:
        return departments(session=self._session, base_url=self._base_url)

    @property
    def groups(self) -> groups:
        return groups(session=self._session, base_url=self._base_url)

    @property
    def users(self) -> users:
        return users(session=self._session, base_url=self._base_url)

    @property
    def auditors(self) -> auditors:
        return auditors(session=self._session, base_url=self._base_url)

    @property
    def firewall_filtering_rules(self) -> firewall_filtering_rules:
        return firewall_filtering_rules(session=self._session, base_url=self._base_url)

    @property
    def ip_destination_groups(self) -> ip_destination_groups:
        return ip_destination_groups(session=self._session, base_url=self._base_url)

    @property
    def ip_source_groups(self) -> ip_source_groups:
        return ip_source_groups(session=self._session, base_url=self._base_url)

    @property
    def ipv6_destination_groups(self) -> ipv6_destination_groups:
        return ipv6_destination_groups(session=self._session, base_url=self._base_url)

    @property
    def ipv6_source_groups(self) -> ipv6_source_groups:
        return ipv6_source_groups(session=self._session, base_url=self._base_url)

    @property
    def network_application_groups(self) -> network_application_groups:
        return network_application_groups(
            session=self._session, base_url=self._base_url
        )

    @property
    def network_applications(self) -> network_applications:
        return network_applications(session=self._session, base_url=self._base_url)

    @property
    def network_service_groups(self) -> network_service_groups:
        return network_service_groups(session=self._session, base_url=self._base_url)

    @property
    def network_services(self) -> network_services:
        return network_services(session=self._session, base_url=self._base_url)

    @property
    def time_windows(self) -> time_windows:
        return time_windows(session=self._session, base_url=self._base_url)

    @property
    def web_dlp_rules(self) -> web_dlp_rules:
        return web_dlp_rules(session=self._session, base_url=self._base_url)

    @property
    def incident_receivers(self) -> incident_receivers:
        return incident_receivers(session=self._session, base_url=self._base_url)

    @property
    def idm_profiles(self) -> idm_profiles:
        return idm_profiles(session=self._session, base_url=self._base_url)

    @property
    def icap_servers(self) -> icap_servers:
        return icap_servers(session=self._session, base_url=self._base_url)

    @property
    def dlp_notification_templates(self) -> dlp_notification_templates:
        return dlp_notification_templates(
            session=self._session, base_url=self._base_url
        )

    @property
    def dlp_dictionaries(self) -> dlp_dictionaries:
        return dlp_dictionaries(session=self._session, base_url=self._base_url)

    @property
    def dlp_engines(self) -> dlp_engines:
        return dlp_engines(session=self._session, base_url=self._base_url)

    @property
    def dlp_edm(self) -> dlp_edm:
        return dlp_edm(session=self._session, base_url=self._base_url)

    @property
    def device_groups(self) -> device_groups:
        return device_groups(session=self._session, base_url=self._base_url)

    @property
    def devices(self) -> devices:
        return devices(session=self._session, base_url=self._base_url)

    @property
    def event_logs(self) -> event_logs:
        return event_logs(session=self._session, base_url=self._base_url)

    @property
    def locations(self) -> locations:
        return locations(session=self._session, base_url=self._base_url)

    @property
    def location_groups(self) -> location_groups:
        return location_groups(session=self._session, base_url=self._base_url)

    @property
    def sublocations(self) -> sublocations:
        return sublocations(session=self._session, base_url=self._base_url)

    @property
    def rule_labels(self) -> rule_labels:
        return rule_labels(session=self._session, base_url=self._base_url)

    @property
    def sandbox_report_quota(self) -> sandbox_report_quota:
        return sandbox_report_quota(session=self._session, base_url=self._base_url)

    @property
    def sandbox_report_file(self) -> sandbox_report_file:
        return sandbox_report_file(session=self._session, base_url=self._base_url)

    @property
    def sandbox_settings(self) -> sandbox_settings:
        return sandbox_settings(session=self._session, base_url=self._base_url)

    @property
    def sandbox_submission(self) -> sandbox_submission:
        return sandbox_submission(session=self._session, base_url=self._base_url)

    @property
    def allowlist(self) -> allowlist:
        return allowlist(session=self._session, base_url=self._base_url)

    @property
    def denylist(self) -> denylist:
        return denylist(session=self._session, base_url=self._base_url)

    @property
    def blacklist(self) -> blacklist:
        return blacklist(session=self._session, base_url=self._base_url)

    @property
    def gre_tunnels(self) -> gre_tunnels:
        return gre_tunnels(session=self._session, base_url=self._base_url)

    @property
    def ipv6(self) -> ipv6:
        return ipv6(session=self._session, base_url=self._base_url)

    @property
    def static_ips(self) -> static_ips:
        return static_ips(session=self._session, base_url=self._base_url)

    @property
    def vips(self) -> vips:
        return vips(session=self._session, base_url=self._base_url)

    @property
    def vpn_credentials(self) -> vpn_credentials:
        return vpn_credentials(session=self._session, base_url=self._base_url)

    @property
    def url_categories(self) -> url_categories:
        return url_categories(session=self._session, base_url=self._base_url)

    @property
    def url_filtering_rules(self) -> url_filtering_rules:
        return url_filtering_rules(session=self._session, base_url=self._base_url)

    @property
    def user_authentication_settings(self) -> user_authentication_settings:
        return user_authentication_settings(
            session=self._session, base_url=self._base_url
        )

    @property
    def app_total(self) -> app_total:
        return app_total(session=self._session, base_url=self._base_url)

    @property
    def intermediate_ca_certificates(self) -> intermediate_ca_certificates:
        return intermediate_ca_certificates(
            session=self._session, base_url=self._base_url
        )
