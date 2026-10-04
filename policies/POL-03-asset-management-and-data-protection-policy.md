# Asset Management and Data Protection Policy

| Field | Value |
| :--- | :--- |
| **Document ID** | POL-03 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Head of IT Operations |
| **Approved by** | CISO |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

## 1. Purpose

To make sure information assets are identified, owned, classified and protected according to their value and sensitivity, from acquisition to disposal.

## 2. Scope

This policy covers hardware, software, cloud services, data and information in any form.

## 3. Policy Statements

### 3.1 Asset Inventory
- Hardware, software, cloud resources and SaaS services shall be recorded in the Configuration Management Database (CMDB). Cloud inventories shall be synchronised automatically, at least daily.
- Each asset shall have a named owner who is accountable for its protection.
- Assets that are not in the inventory shall be investigated within 5 business days.

### 3.2 Information Classification

| Level | Description | Examples | Minimum Handling |
| :--- | :--- | :--- | :--- |
| **Restricted** | Severe harm if disclosed | Cardholder data, encryption keys, credentials | Encrypted at rest and in transit; named access only; DLP enforced |
| **Confidential** | Significant harm if disclosed | Customer PII, contracts, audit reports | Encrypted at rest and in transit; role-based access |
| **Internal** | Limited harm if disclosed | Policies, internal procedures | Access limited to staff and approved contractors |
| **Public** | Approved for release | Marketing material | No restrictions |

- Information owners shall classify information when it is created. Documents and emails shall be labelled using Microsoft Purview sensitivity labels.
- Assets shall be prioritised for protection and recovery based on their classification and business criticality.

### 3.3 Cryptography
- Confidential and Restricted data shall be encrypted at rest using AES-256 or an equivalent algorithm.
- Data in transit over untrusted networks shall use TLS 1.2 or higher. TLS 1.3 is preferred.
- Cryptographic keys for Restricted data shall be held in a hardware security module (HSM) or a managed key service, and rotated at least once a year.

### 3.4 Information Transfer
- Restricted and Confidential information shall only be transferred through approved, encrypted channels. A data-sharing agreement is required when the recipient is outside the company.

### 3.5 Asset Lifecycle and Disposal
- Assets shall be returned when employment or a contract ends.
- Storage media shall be wiped to NIST SP 800-88 standards or physically destroyed before disposal or reuse. A certificate of destruction shall be kept.
- Data shall be deleted when it is no longer needed, in line with the data retention schedule.

## 4. Roles and Responsibilities

| Role | Responsibility |
| :--- | :--- |
| Asset Owners | Keep inventory records accurate, classify assets and approve access. |
| IT Operations | Maintain the CMDB and perform secure disposal. |
| Data Protection Officer | Advises on handling personal data and on retention. |

## Compliance and Exceptions

Compliance with this policy is monitored through the controls listed in the Framework Mapping section, internal audit (ISO 27001 clause 9.2) and management review (clause 9.3). Breaches may lead to disciplinary action under the HR disciplinary process (Annex A 6.4).

Exceptions must be requested using the [Policy Exception Request](../templates/policy-exception-request.md), risk-assessed under [POL-10](POL-10-risk-management-policy.md), approved by the CISO and recorded in the risk register with an expiry date of no more than 12 months.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| ID.AM-01 | Inventories of hardware managed by the organisation are maintained | — | 5.9 | Strong |
| ID.AM-02 | Inventories of software, services and systems are maintained | — | 5.9, 5.23 | Strong |
| ID.AM-05 | Assets are prioritised based on classification, criticality and business value | — | 5.12, 5.13 | Strong |
| ID.AM-08 | Assets are managed throughout their life cycle | — | 5.11, 7.14, 8.10 | Partial |
| PR.DS-01 | The confidentiality, integrity and availability of data at rest are protected | — | 5.12, 8.24 | Strong |
| PR.DS-02 | The confidentiality, integrity and availability of data in transit are protected | — | 5.14, 8.24 | Strong |
<!-- mapping:end -->
