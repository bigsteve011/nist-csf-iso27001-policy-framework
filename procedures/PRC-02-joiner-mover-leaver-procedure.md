# Joiner-Mover-Leaver Procedure

| Field | Value |
| :--- | :--- |
| **Document ID** | PRC-02 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Head of Identity and Access Management |
| **Approved by** | CISO |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

**Parent policies:** [POL-02 Access Control](../policies/POL-02-access-control-policy.md) · [POL-09 Acceptable Use and Security Awareness](../policies/POL-09-acceptable-use-and-security-awareness-policy.md)

## 1. Objective

To grant, change and remove access in step with changes to employment, using the HR system as the source of truth.

## 2. Joiner

| # | Step | Owner | SLA |
| :---: | :--- | :--- | :--- |
| 1 | Confirm that screening is complete and the contract (with security clauses) is signed, then create the worker record in the HR system. | HR | Before the start date |
| 2 | The HR system automatically creates the identity in Entra ID with the role-based "birthright" access for the job. | IAM (automated) | Start date minus 1 day |
| 3 | The line manager requests any extra access through the IAM portal, and the system owner approves it. | Line Manager | — |
| 4 | Register MFA when the user first signs in. Issue a managed device. | User / IT | Day 1 |
| 5 | Assign security awareness training. | Security Awareness | Complete within 30 days |

## 3. Mover

| # | Step | Owner | SLA |
| :---: | :--- | :--- | :--- |
| 1 | HR records the role change. | HR | Effective date |
| 2 | Update birthright access for the new role. Remove access from the previous role after a **14-day** overlap, unless the new manager justifies keeping it. | IAM | 14 days |
| 3 | The new manager confirms the access needed for the new role. | Line Manager | 5 business days |

## 4. Leaver

| # | Step | Owner | SLA |
| :---: | :--- | :--- | :--- |
| 1 | HR records the termination date. For involuntary leavers, HR notifies IAM immediately. | HR | — |
| 2 | Disable the identity, revoke sessions and tokens, and remove MFA methods. | IAM (automated) | Within 4 hours (immediately if involuntary) |
| 3 | Rotate any shared or service credentials the leaver knew. | System Owners | 24 hours |
| 4 | Collect devices and badges. Remind the leaver of their continuing confidentiality obligations. | Line Manager / HR | Last day |
| 5 | Delete the account or convert the mailbox, in line with the retention schedule. | IAM | 30 days |

## 5. Monitoring
- Each week, reconcile active accounts against the HR system. Any active account belonging to a leaver is treated as a security event.

## Records

Records produced by this procedure are kept for at least **3 years**, or longer where a regulation requires it, and must be available as audit evidence.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| GV.RR-04 | Cybersecurity is included in human resources practices | 7.2 | 6.1, 6.2, 6.4, 6.5 | Strong |
| PR.AA-01 | Identities and credentials for authorised users, services and hardware are managed | — | 5.16, 5.17 | Strong |
<!-- mapping:end -->
