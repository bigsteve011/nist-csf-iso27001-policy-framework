# Access Control Policy

| Field | Value |
| :--- | :--- |
| **Document ID** | POL-02 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Head of Identity and Access Management |
| **Approved by** | CISO |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

## 1. Purpose

To ensure that only authorised users, services and devices can access information and systems, with the minimum privileges they need.

## 2. Scope

This policy covers all user, privileged, service and third-party accounts on Meridian Payments' systems, including Microsoft Entra ID, AWS IAM, SaaS applications, databases and network devices. It also covers physical access to offices and equipment rooms.

## 3. Policy Statements

### 3.1 Identity Lifecycle
- Every user shall have a unique identity. Shared accounts are forbidden unless the CISO approves an exception.
- Access shall be granted, changed and removed through the [PRC-02 Joiner-Mover-Leaver Procedure](../procedures/PRC-02-joiner-mover-leaver-procedure.md).
- Leavers' access shall be disabled within **4 hours** of termination (immediately for involuntary terminations).
- Accounts that are inactive for **45 days** shall be disabled automatically.

### 3.2 Least Privilege and Segregation of Duties
- Access shall be role-based and limited to what each job requires.
- Incompatible duties shall be separated and enforced through the Segregation of Duties matrix. Examples are developing code and deploying it to production, and raising a payment and approving it.

### 3.3 Authentication
- Phishing-resistant multi-factor authentication (MFA) is mandatory for all remote access, cloud consoles, privileged access and email.
- Conditional Access policies shall block legacy authentication and require compliant devices to access sensitive data.
- Passwords shall be at least 14 characters long and checked against known-breached password lists. Periodic forced rotation is not required.

### 3.4 Privileged Access
- Administrative rights shall be granted just in time through Privileged Identity Management, for a maximum of 8 hours.
- Administrators shall use separate privileged accounts that have no mailbox or internet browsing access.
- Break-glass accounts shall be vaulted, monitored and tested every quarter.

### 3.5 Service Accounts and Secrets
- Each service account shall have a named owner. Where the platform supports it, workloads shall use managed identities instead of stored secrets.
- Secrets shall be stored in an approved vault (Azure Key Vault or AWS Secrets Manager) and must not be stored in source code.

### 3.6 Access Reviews
- User access shall be reviewed **quarterly** for privileged and in-scope PCI systems, and **semi-annually** for all other systems, following [PRC-01 User Access Review Procedure](../procedures/PRC-01-user-access-review-procedure.md).

### 3.7 Physical Access
- Offices and equipment rooms shall be protected by badge-controlled entry. Access to secure areas shall be logged and reviewed every quarter.
- Visitors shall be registered and escorted at all times.

## 4. Roles and Responsibilities

| Role | Responsibility |
| :--- | :--- |
| IAM Team | Operates identity platforms, PIM and access provisioning. |
| Line Managers | Request and approve access for their staff, and certify it during reviews. |
| System Owners | Define roles and approve access to their systems. |
| HR | Trigger joiner, mover and leaver events in the HR system. |
| Facilities | Manage physical access systems. |

## Compliance and Exceptions

Compliance with this policy is monitored through the controls listed in the Framework Mapping section, internal audit (ISO 27001 clause 9.2) and management review (clause 9.3). Breaches may lead to disciplinary action under the HR disciplinary process (Annex A 6.4).

Exceptions must be requested using the [Policy Exception Request](../templates/policy-exception-request.md), risk-assessed under [POL-10](POL-10-risk-management-policy.md), approved by the CISO and recorded in the risk register with an expiry date of no more than 12 months.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| PR.AA-01 | Identities and credentials for authorised users, services and hardware are managed | — | 5.16, 5.17 | Strong |
| PR.AA-03 | Users, services and hardware are authenticated | — | 8.5 | Strong |
| PR.AA-05 | Access permissions are defined, managed and reviewed using least privilege and separation of duties | — | 5.3, 5.15, 5.18, 8.2, 8.3 | Strong |
| PR.AA-06 | Physical access to assets is managed, monitored and enforced commensurate with risk | — | 7.1, 7.2, 7.3 | Partial |
<!-- mapping:end -->
