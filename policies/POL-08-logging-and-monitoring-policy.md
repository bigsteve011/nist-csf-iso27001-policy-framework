# Logging and Monitoring Policy

| Field | Value |
| :--- | :--- |
| **Document ID** | POL-08 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Head of Security Operations |
| **Approved by** | CISO |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

## 1. Purpose

To make sure security-relevant events are recorded, protected and monitored, so that threats can be detected quickly and investigated.

## 2. Scope

This policy covers all production systems, identity platforms, cloud control planes, network devices, endpoints and security tools.

## 3. Policy Statements

### 3.1 Log Generation
The following events shall be logged at minimum:
- authentication successes and failures
- privileged actions and changes to access rights
- configuration changes and cloud control-plane activity (Azure Activity Log, AWS CloudTrail, GCP Audit Logs)
- access to Restricted data
- security tool alerts (EDR, WAF, IDS)

Logs shall include the timestamp, source, user or identity, action and outcome. All systems shall synchronise their clocks with approved NTP sources.

### 3.2 Log Protection and Retention
- Logs shall be sent to the central SIEM (Microsoft Sentinel) and protected from tampering. Access to logs shall be limited to read-only roles.
- Logs shall be kept for **12 months**, with at least **90 days** immediately available for search.

### 3.3 Monitoring and Detection
- The SOC shall monitor security alerts 24/7.
- Detection rules shall be mapped to MITRE ATT&CK and reviewed every quarter for coverage and false-positive rates.
- Endpoint detection and response (EDR) shall be deployed on every supported endpoint and server. Endpoints with unhealthy or missing agents shall be reported every week.
- The SOC shall be alerted within **24 hours** when a log source stops sending data.

### 3.4 Analysis
- Alerts shall be triaged and enriched with threat intelligence and asset context. Alerts that meet the incident criteria shall be escalated under [POL-04](POL-04-incident-management-policy.md).

### 3.5 Privacy
- User activity shall only be monitored for security purposes, in line with GDPR and employment law. Staff shall be told about monitoring through this policy and the Acceptable Use Policy.

## 4. Roles and Responsibilities

| Role | Responsibility |
| :--- | :--- |
| SOC | Monitors, triages and develops detection rules. |
| Platform Owners | Make sure their systems send the required logs. |
| SIEM Engineering | Onboards log sources, monitors their health and manages retention. |

## Compliance and Exceptions

Compliance with this policy is monitored through the controls listed in the Framework Mapping section, internal audit (ISO 27001 clause 9.2) and management review (clause 9.3). Breaches may lead to disciplinary action under the HR disciplinary process (Annex A 6.4).

Exceptions must be requested using the [Policy Exception Request](../templates/policy-exception-request.md), risk-assessed under [POL-10](POL-10-risk-management-policy.md), approved by the CISO and recorded in the risk register with an expiry date of no more than 12 months.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| PR.PS-04 | Log records are generated and made available for continuous monitoring | — | 8.15, 8.17 | Strong |
| DE.CM-01 | Networks and network services are monitored to find potentially adverse events | — | 8.16, 8.20 | Strong |
| DE.CM-03 | Personnel activity and technology usage are monitored to find potentially adverse events | — | 8.16 | Strong |
| DE.CM-09 | Computing hardware, software, runtime environments and their data are monitored | — | 8.7, 8.16 | Strong |
| DE.AE-02 | Potentially adverse events are analysed to better understand associated activities | — | 5.25, 8.16 | Strong |
<!-- mapping:end -->
