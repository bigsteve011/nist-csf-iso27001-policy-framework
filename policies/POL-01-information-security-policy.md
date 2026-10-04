# Information Security Policy

| Field | Value |
| :--- | :--- |
| **Document ID** | POL-01 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Chief Information Security Officer (CISO) |
| **Approved by** | Management Board |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

## 1. Purpose

This is the top-level policy of Meridian Payments' Information Security Management System (ISMS). It sets management's direction for protecting the confidentiality, integrity and availability of information, and it is the authority for all other policies in this framework.

## 2. Scope

This policy applies to all employees, contractors, and third parties who access Meridian Payments' information or systems. It covers all information assets, whether on-premises, in the cloud (Microsoft Azure, AWS) or held by suppliers.

## 3. Context and Requirements

3.1 Meridian Payments processes card payments and personal data for merchants in the EU. Information security is essential to its mission and its licence to operate.

3.2 The ISMS shall take into account the following external requirements, recorded and maintained in the Legal and Regulatory Register:
- EU Digital Operational Resilience Act (DORA)
- General Data Protection Regulation (GDPR)
- PCI DSS v4.0
- Contractual security obligations to merchants and banking partners

3.3 Interested parties and their security expectations shall be identified and reviewed annually as part of the ISMS context review.

## 4. Policy Statements

4.1 **Commitment.** The Management Board is accountable for information security risk. It shall provide the resources the ISMS needs and shall promote a risk-aware culture.

4.2 **Objectives.** Measurable information security objectives shall be set each year. They shall be consistent with this policy and tracked through the ISMS metrics dashboard.

4.3 **Risk-based approach.** Security controls shall be selected based on risk assessment, as described in [POL-10 Risk Management Policy](POL-10-risk-management-policy.md).

4.4 **Policy framework.** Topic-specific policies (POL-02 to POL-11) and their procedures shall support this policy. All policies shall be managed under [PRC-08 Policy Lifecycle Procedure](../procedures/PRC-08-policy-lifecycle-procedure.md).

4.5 **Review.** This policy and all topic-specific policies shall be reviewed at least once a year, and also after significant changes to the business, the threat landscape, technology or regulation.

4.6 **Performance evaluation.** ISMS effectiveness shall be measured through metrics, internal audit and an annual independent review. Management shall review the results at least once a year.

4.7 **Continual improvement.** Nonconformities and improvement opportunities from audits, incidents and reviews shall be recorded and corrected through a root-cause-based corrective action process.

## 5. Roles and Responsibilities

| Role | Responsibility |
| :--- | :--- |
| Management Board | Approves this policy and the risk appetite. Chairs the annual management review. |
| CISO | Owns the ISMS and the policy framework. Reports ISMS performance to the Board each quarter. |
| Information Security Steering Committee | Oversees risk treatment, policy exceptions and security programme priorities. |
| Asset and Process Owners | Implement controls for their assets and accept residual risk within their delegated authority. |
| Internal Audit | Provides independent assurance on the ISMS. |
| All personnel | Comply with security policies and report suspected incidents. |

Roles that conflict, such as requesting and approving one's own access, shall be segregated.

## Compliance and Exceptions

Compliance with this policy is monitored through the controls listed in the Framework Mapping section, internal audit (ISO 27001 clause 9.2) and management review (clause 9.3). Breaches may lead to disciplinary action under the HR disciplinary process (Annex A 6.4).

Exceptions must be requested using the [Policy Exception Request](../templates/policy-exception-request.md), risk-assessed under [POL-10](POL-10-risk-management-policy.md), approved by the CISO and recorded in the risk register with an expiry date of no more than 12 months.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| GV.OC-01 | The organisational mission is understood and informs cybersecurity risk management | 4.1, 4.2 | — | Partial |
| GV.OC-03 | Legal, regulatory and contractual cybersecurity requirements are understood and managed | 4.2 | 5.31, 5.34 | Strong |
| GV.RR-01 | Leadership is accountable for cybersecurity risk and fosters a risk-aware culture | 5.1, 5.3 | 5.4 | Strong |
| GV.RR-02 | Cybersecurity roles, responsibilities and authorities are established and communicated | 5.3 | 5.2, 5.3 | Strong |
| GV.PO-01 | Cybersecurity policy is established, communicated and enforced | 5.2, 7.5 | 5.1 | Strong |
| GV.PO-02 | Cybersecurity policy is reviewed and updated to reflect changes in requirements, threats and technology | 7.5, 9.3 | 5.1, 5.36 | Strong |
| GV.OV-01 | Strategy outcomes are reviewed to inform and adjust strategy and direction | 9.1, 9.3 | 5.35 | Strong |
| ID.IM-01 | Improvements are identified from evaluations, audits and reviews | 9.2, 10.1, 10.2 | — | Strong |
<!-- mapping:end -->
