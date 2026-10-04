# Business Continuity and Backup Policy

| Field | Value |
| :--- | :--- |
| **Document ID** | POL-05 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Head of Business Continuity |
| **Approved by** | Management Board |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

## 1. Purpose

To make sure critical business services can continue or recover within agreed time frames after a disruption, and that data can be restored reliably.

## 2. Scope

This policy covers all critical and important business functions (as defined under DORA) and the ICT systems, data, people and suppliers they depend on.

## 3. Policy Statements

### 3.1 Business Impact Analysis
- A Business Impact Analysis (BIA) shall be carried out every year, and also when services change significantly. The BIA shall set the Maximum Tolerable Downtime (MTD), Recovery Time Objective (RTO) and Recovery Point Objective (RPO) for each critical service.

| Tier | Example Services | RTO | RPO |
| :--- | :--- | :--- | :--- |
| Tier 0 | Payment authorisation, settlement | 2 hours | 5 minutes |
| Tier 1 | Merchant portal, fraud screening | 8 hours | 1 hour |
| Tier 2 | Internal reporting, HR | 72 hours | 24 hours |

### 3.2 Resilience
- Tier 0 and Tier 1 systems shall be deployed across at least two availability zones. Tier 0 systems shall also be able to fail over to a secondary region.
- Single points of failure found in the BIA shall be recorded as risks and treated.

### 3.3 Backup
- Backups shall follow the **3-2-1-1-0** rule: 3 copies, on 2 different media, 1 off-site, 1 immutable or air-gapped, and 0 errors when restores are verified.
- Backups shall be encrypted and access-controlled separately from production. Backup administrator accounts shall not be domain-joined to production.
- Backup frequency shall meet the RPO for each tier.

### 3.4 Testing
- Restores shall be tested following [PRC-05](../procedures/PRC-05-backup-and-restore-testing-procedure.md). Tier 0 systems shall be tested **quarterly** and all other tiers **annually**.
- Backup integrity shall be checked before data is restored into production.
- DR failover for Tier 0 systems shall be tested at least once a year. The results shall be compared with the RTO and RPO, and any gaps shall be raised as risks.

### 3.5 Continuity Plans
- Each critical service shall have a documented continuity and recovery plan. The plan shall cover communication with staff, customers and regulators during recovery.

## 4. Roles and Responsibilities

| Role | Responsibility |
| :--- | :--- |
| Business Continuity Manager | Owns the BIA, plans and test schedule. |
| Service Owners | Maintain recovery plans and take part in tests. |
| Infrastructure Team | Operates backups and DR environments. |

## Compliance and Exceptions

Compliance with this policy is monitored through the controls listed in the Framework Mapping section, internal audit (ISO 27001 clause 9.2) and management review (clause 9.3). Breaches may lead to disciplinary action under the HR disciplinary process (Annex A 6.4).

Exceptions must be requested using the [Policy Exception Request](../templates/policy-exception-request.md), risk-assessed under [POL-10](POL-10-risk-management-policy.md), approved by the CISO and recorded in the risk register with an expiry date of no more than 12 months.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| PR.DS-11 | Backups of data are created, protected, maintained and tested | — | 8.13 | Strong |
| PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adverse situations | — | 5.30, 8.14 | Strong |
| RC.RP-01 | The recovery portion of the incident response plan is executed once initiated | — | 5.26, 5.29, 5.30 | Strong |
| RC.RP-03 | The integrity of backups and other restoration assets is verified before using them for restoration | — | 8.13 | Strong |
<!-- mapping:end -->
