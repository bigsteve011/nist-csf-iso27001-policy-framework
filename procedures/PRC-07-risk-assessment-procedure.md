# Risk Assessment Procedure

| Field | Value |
| :--- | :--- |
| **Document ID** | PRC-07 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Head of Information Security Risk |
| **Approved by** | CISO |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

**Parent policy:** [POL-10 Risk Management Policy](../policies/POL-10-risk-management-policy.md)

## 1. Objective

To identify, analyse and evaluate information security risks in a way that gives consistent, comparable results, based on ISO/IEC 27005.

## 2. Scales

**Likelihood**

| Score | Level | Description |
| :---: | :--- | :--- |
| 1 | Rare | Less than once in 10 years |
| 2 | Unlikely | Once in 3–10 years |
| 3 | Possible | Once in 1–3 years |
| 4 | Likely | One or more times a year |
| 5 | Almost certain | Several times a year |

**Impact** (use the highest score across the categories)

| Score | Financial | Regulatory | Customer / Operational |
| :---: | :--- | :--- | :--- |
| 1 | < €10k | No reportable impact | Negligible |
| 2 | €10k–€100k | Minor finding | Minor service degradation |
| 3 | €100k–€1M | Formal regulatory inquiry | Tier 1 outage longer than its RTO |
| 4 | €1M–€10M | Fine or enforcement action | Tier 0 outage longer than its RTO; breach of Confidential data |
| 5 | > €10M | Licence at risk | Breach of Restricted data at scale |

## 3. Steps

| # | Step | Owner | Output |
| :---: | :--- | :--- | :--- |
| 1 | Define the scope: the process, system or change, and the assets and data involved. | Risk Team | Scope statement |
| 2 | Identify threats, using MITRE ATT&CK and threat intelligence, and the vulnerabilities they could exploit, using scan results, audit findings and control gaps. | Risk Team / SMEs | Threat–vulnerability pairs |
| 3 | Write each risk as a scenario: *"[Threat] exploits [vulnerability] causing [impact] to [asset]."* | Risk Team | Risk statements |
| 4 | Rate the inherent likelihood and impact, then rate the residual risk after existing controls. | Risk Owner | Scores |
| 5 | Compare each risk with the appetite. Risks above appetite need treatment. | Risk Team | Evaluation |
| 6 | Choose a treatment and map the controls to ISO 27001 Annex A. Set the target residual risk. | Risk Owner | Treatment plan |
| 7 | Record everything in the [risk register](../templates/risk-register.csv) and update the Statement of Applicability. | Risk Team | Updated register |
| 8 | Get residual risk accepted by the authority named in POL-10 §3.2. | Risk Owner | Acceptance record |
| 9 | Review progress every quarter. Reassess when something triggers it, such as an incident, a change or a new threat. | Risk Team | Review minutes |

## Records

Records produced by this procedure are kept for at least **3 years**, or longer where a regulation requires it, and must be available as audit evidence.

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
