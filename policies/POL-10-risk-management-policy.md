# Risk Management Policy

| Field | Value |
| :--- | :--- |
| **Document ID** | POL-10 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Head of Information Security Risk |
| **Approved by** | Management Board |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

## 1. Purpose

To set out how information security risks are identified, analysed, evaluated, treated and monitored, in line with ISO/IEC 27001 clause 6.1 and ISO/IEC 27005.

## 2. Scope

This policy covers information security and ICT risks across all business processes, assets, projects and suppliers.

## 3. Policy Statements

### 3.1 Risk Appetite
The Management Board sets the risk appetite each year:

| Risk Area | Appetite | Statement |
| :--- | :--- | :--- |
| Cardholder and personal data | **Very low** | No risk with a residual rating of High or above is accepted for Restricted data. |
| Payment service availability | **Low** | Tier 0 services must meet their RTO and RPO. Any gap needs a funded treatment plan. |
| Regulatory compliance | **Very low** | Known non-compliance with DORA, GDPR or PCI DSS must have a remediation plan within 30 days. |
| Innovation and new technology | **Moderate** | New technology may be adopted once it has been risk-assessed and its residual risk accepted. |

### 3.2 Risk Assessment
- Risks shall be assessed following [PRC-07](../procedures/PRC-07-risk-assessment-procedure.md):
  - at least once a year
  - before significant changes
  - after major incidents
  - when new threats emerge
- Likelihood and impact shall each be rated on a 5×5 scale. Impact shall consider financial, regulatory, customer, operational and reputational effects. Material risks may also be quantified using FAIR.

| Score (L×I) | Rating | Treatment Decision | Acceptance Authority |
| :--- | :--- | :--- | :--- |
| 20–25 | **Critical** | Treat immediately | Management Board |
| 12–19 | **High** | Treatment plan within 30 days | CISO and Steering Committee |
| 6–11 | **Medium** | Treat or accept | Risk Owner and CISO |
| 1–5 | **Low** | Accept and monitor | Risk Owner |

### 3.3 Risk Treatment
- Each risk shall be treated in one of four ways: modify (apply controls), avoid, share (insurance or contract) or retain (accept).
- Controls shall be selected from ISO/IEC 27001 Annex A and recorded in the Statement of Applicability.
- Each treatment plan shall name an owner, actions and a due date. Progress shall be tracked in the risk register.

### 3.4 Monitoring and Reporting
- The risk register shall be reviewed every quarter by risk owners and the Steering Committee.
- Risks above the appetite and overdue treatment plans shall be reported to the Management Board every quarter.

## 4. Roles and Responsibilities

| Role | Responsibility |
| :--- | :--- |
| Management Board | Sets the risk appetite and accepts Critical risks. |
| Risk Owners | Own individual risks and their treatment. |
| Information Security Risk Team | Defines the methodology, facilitates assessments and maintains the risk register. |

## Compliance and Exceptions

Compliance with this policy is monitored through the controls listed in the Framework Mapping section, internal audit (ISO 27001 clause 9.2) and management review (clause 9.3). Breaches may lead to disciplinary action under the HR disciplinary process (Annex A 6.4).

Exceptions must be requested using the [Policy Exception Request](../templates/policy-exception-request.md), risk-assessed under [POL-10](POL-10-risk-management-policy.md), approved by the CISO and recorded in the risk register with an expiry date of no more than 12 months.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| GV.RM-01 | Risk management objectives are established and agreed by stakeholders | 6.1, 6.2 | — | Strong |
| GV.RM-02 | Risk appetite and risk tolerance statements are established and maintained | 6.1.2 | — | Partial |
| ID.RA-05 | Threats, vulnerabilities, likelihoods and impacts are used to understand inherent risk | 6.1.2, 8.2 | — | Strong |
| ID.RA-06 | Risk responses are chosen, prioritised, planned, tracked and communicated | 6.1.3, 8.3 | — | Strong |
<!-- mapping:end -->
