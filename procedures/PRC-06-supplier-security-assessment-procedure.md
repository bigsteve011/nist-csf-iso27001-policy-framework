# Supplier Security Assessment Procedure

| Field | Value |
| :--- | :--- |
| **Document ID** | PRC-06 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Head of Third-Party Risk |
| **Approved by** | CISO |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

**Parent policy:** [POL-06 Third-Party Security Policy](../policies/POL-06-third-party-security-policy.md)

## 1. Objective

To assess a supplier's security before onboarding, and to keep monitoring it for as long as the relationship lasts.

## 2. Steps

| # | Step | Owner | Output |
| :---: | :--- | :--- | :--- |
| 1 | The business owner submits an intake form describing the service, the data involved, how the supplier connects, and whether it supports a critical or important function. | Business Owner | Intake form |
| 2 | Assign the supplier tier using the criteria in POL-06. | Third-Party Risk | Tier |
| 3 | Send a questionnaire matched to the tier. Collect evidence such as the SOC 2 Type II report, ISO 27001 certificate and scope, penetration test summary, BC/DR test results and sub-processor list. | Third-Party Risk | Completed assessment |
| 4 | Review the evidence. Check the certification scope and the SOC 2 complementary user entity controls (CUECs). Record any gaps as findings. | Third-Party Risk | Findings |
| 5 | Rate the residual risk. Agree fixes with the supplier, or record the business owner's acceptance. | Third-Party Risk / Business Owner | Risk decision |
| 6 | Legal confirms the contract contains the clauses required by POL-06 §3.3. | Legal | Contract checklist |
| 7 | Add the supplier to the supplier register and the DORA Register of Information. | Third-Party Risk | Register entry |
| 8 | Monitor the supplier over time: reassess it on schedule, use external security ratings, track its incidents and SLAs, and re-trigger the assessment after material changes. | Third-Party Risk | Monitoring records |
| 9 | When the relationship ends: revoke access, get written confirmation that data was returned or destroyed, and update the registers. | Business Owner / IAM | Offboarding evidence |

## Records

Records produced by this procedure are kept for at least **3 years**, or longer where a regulation requires it, and must be available as audit evidence.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| GV.SC-01 | A supply chain risk management programme is established and agreed | 8.1 | 5.19, 5.21 | Strong |
| GV.SC-05 | Supply chain security requirements are included in contracts and agreements | — | 5.20, 5.23 | Strong |
| GV.SC-07 | Supplier risks are identified, recorded, prioritised and monitored over the relationship | — | 5.22 | Strong |
<!-- mapping:end -->
