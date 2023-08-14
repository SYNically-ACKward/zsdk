<<<<<<< HEAD
## ZSDK v1.1.1 (In Progress) [@Ryan Ulrick](mailto:rulrick@zscaler.com)
- Update README.md with appropriate doc links. Iterate pyproject.toml to minor rev 1
=======
## ZSDK v1.1.1 (8-11-2023) [@Ryan Ulrick](mailto:rulrick@zscaler.com)
- Fix: zia.users.update() method fix
>>>>>>> main

## ZSDK v1.1.0 (8-11-2023) [@Ryan Ulrick]
- Updated logging handlers

## ZSDK v1.0.0 (8-11-2023) [@Ryan Ulrick](mailto:rulrick@zscaler.com)
- Feat: All ZIA methods
- Feat: Tests placeholders for all intermediate_ca_certs.intermediate_ca_certificates sub-methods
- Feat: Methods for intermediate_ca_certs.intermediate_ca_certificates: create, create_csr, create_key_pair, delete, finalize, get, get_attestation, get_csr, get_lite, get_public_key, get_ready_certs, list, list_lite, show_csr, show_signed_cert, update, update_default, upload_cert, upload_cert_chain, verify_key_attestation
- Feat: Tests placeholders fro app_total.app_total methods
- Feat: Methods for app_total.app_total: get, analyze
- Feat: Tests placeholders for user_authentication_settings sub-methods
- Feat: Methods for user_authentication_settings.user_authentication_settings: list, update
- Feat: Tests placeholders for url_filtering_rules.url_filtering_rules sub-methods
- Feat: Methods for url_filtering_rules.url_filtering_rules: list, get, create, update, delete
- Feat: Tests placeholders for url_categories.url_categories methods
- Feat: Methods for url_categories.url_categories: list, list_lite, get, create, update, delete, get_quota, lookup
- Feat: Tests placeholders for traffic_forwarding.vpn_credentials sub-methods
- Feat: Methods for traffic_forwarding.vpn_credentials: list, get, create, update, delete, bulk_delete
- Feat: Tests placeholders for traffic_forwarding.vips sub-methods
- Feat: Methods for traffic_forwarding.vips: list, list_by_dc, list_recommended
- Feat: Tests placeholders for traffic_forwarding.static_ips sub-methods
- Feat: Methods for traffic_forwarding.static_ips: list, get, create, update, delete, validate
- Feat: Tests placeholders for traffic_forwarding.ipv6 sub-methods
- Feat: Methods for traffic_forwarding.ipv6: get, get_nat64, get_dns64
- Feat: Tests placeholders for traffic_forwarding.gre_tunnels sub-methods
- Feat: Methods for traffic_forwarding.gre_tunnels: list, get, create, update, delete, get_internal_ips, get_org_ips
- Feat: Tests placeholders for all security_policy methods and sub-methods
- Feat: Methods for security_policy.allowlist: list, update
- Feat: Methods for security_policy.denylist: list, update
- Feat: Methods for security_policy.blacklist: update
- Feat: Tests placeholders for sandbox_submission methods and sub-methods
- Feat: Methods for sandbox_submission.sandbox_submission: submit
- Feat: Tests placeholders for all sandbox_settings methods and sub-methods
- Feat: Methods for sandbox_settings.sandbox_settings: get, update, count
- Feat: Tests placeholders for all sandbox_report methods and sub-methods
- Feat: Methods for sandbox_report.sandbox_report_quota: get
- Feat: Methods for sandbox_report.sandbox_report_file: get
- Feat: Tests placeholders for all rule_labels methods and sub-methods
- Feat: Methods for rule_labels.rule_labels: list, get, create, update, delete
- Feat: Tests placeholders for all locations methods and sub-methods
- Feat: Methods for locations.locations: list, list_lite, get, create, update, delete, bulk_delete
- Feat: Methods for locations.sublocations: list
- Feat: Methods for locations.location_groups: list, list_lite, count, get, get_lite
- Feat: Methods for event_logs.event_logs: status, create, delete, download
- Feat: Tests for all event_logs.event_logs methods and sub-methods
- Feat: Tests placeholders for all device_groups methods and sub-methods
- Feat: Methods for device_groups.device_groups: list
- Feat: Methods for device_groups.devices: list, list_lite
- Feat: Tests placeholders for all data_loss_prevention methods and sub-methods
- Feat: Methods for data_loss_prevention.web_dlp_rules: get, create, update, list, list_lite, delete
- Feat: Methods for data_loss_prevention.incident_receivers: get, list, list_lite
- Feat: Methods for data_loss_prevention.dlp_edm: list, list_lite
- Feat: Methods for data_loss_prevention.idm_profiles: get, list, list_lite
- Feat: Methods for data_loss_prevention.icap_servers: get, list, list_lite
- Feat: Methods for data_loss_prevention.dlp_notification_templates: get, create, update, list, delete
- Feat: Methods for data_loss_prevention.dlp_dictionaries: get, create, update, list, delete, list_lite, validate
- Feat: Methods for data_loss_prevention.dlp_engines: get, create, update, list, delete, list_lite, validate
- Feat: Methods for user_management.departments: list, get
- Feat: Tests for user_management.departments: list, get
- Feat: Methods for user_management.groups: list, get
- Feat: Methods for user_management.users: get, create, update, list, delete, bulk_delete
- Feat: Methods for user_management.auditors: list
- Feat: Tests placeholders for all user_management methods and sub-methods
- Feat: Methods for firewall_policies.firewall_filtering_rules: list, get, create, update, delete
- Feat: Methods for firewall_policies.ip_destination_groups: list, get, create, update, list_lite, delete
- Feat: Methods for firewall_policies.ip_source_groups: list, get, create, update, list_lite, delete
- Feat: Methods for firewall_policies.ipv6_destination_groups: list, list_lite
- Feat: Methods for firewall_policies.ipv6_source_groups: list, list_lite
- Feat: Methods for firewall_policies.network_application_groups: list, get, create, update, list_lite, delete
- Feat: Methods for firewall_policies.network_applications: get, list
- Feat: Methods for firewall_policies.network_service_groups: list, get, create, update, list_lite, delete
- Feat: Methods for firewall_policies.network_services: list, get, create, update, list_lite, delete
- Feat: Methods for firewall_policies.time_windows: list, lite_lite
- Feat: Tests placeholders created for all firewall_policies methods and sub-methods


## ZSDK v0.1.1 (8-7-2023) [@Ryan Ulrick](mailto:rulrick@zscaler.com)
- Feat: Methods for ZIA admin_users: create, update, delete, list
- Feat: Methods for ZIA admin_roles: list
- Feat: Tests for ZIA admin_users: create, update, delete, list
- Feat: Test for ZIA admin_roles: list
- Feat: Test for ZIA activate_changes
- Feat: Methods for admin_audit_logs: status, create, delete, download
- Feat: Tests for admin_audit_logs: status, create, delete, download