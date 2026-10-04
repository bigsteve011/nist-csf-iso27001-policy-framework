# Third-Party Security Policy

| Field | Value |
| :--- | :--- |
| **Document ID** | POL-06 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Head of Third-Party Risk |
| **Approved by** | CISO |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

## 1. Purpose

To manage information security risks from suppliers, cloud service providers and other third parties throughout the relationship.

## 2. Scope

This policy covers all third parties that access, process, store or transmit Meridian Payments' information, or that provide ICT services the company depends on.

## 3. Policy Statements

### 3.1 Tiering
Each supplier shall be assigned a risk tier before onboarding. The tier is based on the data it accesses and how critical its service is:

| Tier | Criteria | Assessment | Reassessment |
| :--- | :--- | :--- | :--- |
| **Critical** | Supports a critical or important function (DORA), or processes Restricted data | Full questionnaire, review of SOC 2 Type II or ISO 27001 certificate, and an on-site visit or audit right | Annual |
| **High** | Processes Confidential data or has network access | Full questionnaire and certification review | Annual |
| **Medium** | Processes Internal data only | Light questionnaire | Every 2 years |
| **Low** | No data access | Due diligence only | When the contract is renewed |

### 3.2 Due Diligence
- Suppliers shall be assessed following [PRC-06](../procedures/PRC-06-supplier-security-assessment-procedure.md) before a contract is signed. Critical and High suppliers cannot be onboarded until the assessment is complete.

### 3.3 Contractual Requirements
Contracts with Critical and High suppliers shall include:
- security and confidentiality obligations
- the right to audit, including for regulators
- incident notification within **24 hours**
- the location of data processing and approval of sub-processors
- a GDPR data processing agreement (Art. 28) where personal data is involved
- exit and transition support (DORA Art. 30)
- business continuity commitments that match Meridian Payments' RTO

### 3.4 Cloud Services
- Cloud services shall follow the shared responsibility model. Meridian Payments' own responsibilities shall be documented and assigned controls.
- Each critical cloud service shall have a documented, tested exit strategy, and concentration risk across providers shall be assessed.

### 3.5 Monitoring and Offboarding
- Critical suppliers' security posture, SLA performance and incidents shall be monitored continuously.
- When a contract ends, access shall be revoked and data returned or destroyed, with written confirmation from the supplier.
- The Register of Information on ICT third-party arrangements (DORA) shall be kept up to date.

## 4. Roles and Responsibilities

| Role | Responsibility |
| :--- | :--- |
| Third-Party Risk Team | Tiering, assessments and the supplier register. |
| Business Owner | Justifies the need for the supplier, owns the relationship and accepts the risk. |
| Procurement and Legal | Make sure contracts contain the required clauses. |

## Compliance and Exceptions

Compliance with this policy is monitored through the controls listed in the Framework Mapping section, internal audit (ISO 27001 clause 9.2) and management review (clause 9.3). Breaches may lead to disciplinary action under the HR disciplinary process (Annex A 6.4).

Exceptions must be requested using the [Policy Exception Request](../templates/policy-exception-request.md), risk-assessed under [POL-10](POL-10-risk-management-policy.md), approved by the CISO and recorded in the risk register with an expiry date of no more than 12 months.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| GV.SC-01 | A supply chain risk management programme is established and agreed | 8.1 | 5.19, 5.21 | Strong |
| GV.SC-05 | Supply chain security requirements are included in contracts and agreements | — | 5.20, 5.23 | Strong |
| GV.SC-07 | Supplier risks are identified, recorded, prioritised and monitored over the relationship | — | 5.22 | Strong |
<!-- mapping:end -->
