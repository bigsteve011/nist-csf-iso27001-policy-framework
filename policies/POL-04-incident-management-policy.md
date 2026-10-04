# Incident Management Policy

| Field | Value |
| :--- | :--- |
| **Document ID** | POL-04 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Head of Security Operations |
| **Approved by** | CISO |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

## 1. Purpose

To make sure information security incidents are detected, reported, handled and learned from consistently, so that their impact is limited and regulatory reporting obligations are met.

## 2. Scope

This policy covers all security events and incidents that affect Meridian Payments' information, systems, personnel or suppliers, including incidents at third parties that affect the company's services.

## 3. Definitions

- **Security event:** an observed occurrence that may indicate a breach of policy or a failure of a control.
- **Security incident:** one or more events that have compromised, or are likely to compromise, the confidentiality, integrity or availability of information or services.
- **Major ICT-related incident:** an incident that meets the DORA classification criteria (RTS on classification of ICT-related incidents).

## 4. Policy Statements

4.1 **Plan.** A documented incident response plan ([PRC-03](../procedures/PRC-03-incident-response-procedure.md)) shall be maintained, tested at least once a year through a tabletop exercise, and updated after every major incident.

4.2 **Reporting.** All personnel shall report suspected incidents immediately through the Service Desk, the `#security-incident` channel or `security@meridianpayments.example`. Nobody shall be penalised for reporting in good faith.

4.3 **Triage and declaration.** The Security Operations Centre (SOC) shall triage reported events and declare an incident when the criteria in the severity matrix are met.

| Severity | Criteria (examples) | Response Start | Escalation |
| :--- | :--- | :--- | :--- |
| **SEV-1 Critical** | Confirmed breach of Restricted data, ransomware, or outage of payment processing | 15 minutes | CISO, CEO, DPO; regulators assessed |
| **SEV-2 High** | Compromised privileged account, or malware spreading on multiple hosts | 1 hour | CISO, system owner |
| **SEV-3 Medium** | A single compromised user account, or malware that was contained | 4 hours | SOC lead |
| **SEV-4 Low** | Policy violation with no data exposure | 1 business day | SOC analyst |

4.4 **Response.** Incidents shall be contained, eradicated and recovered from following the response playbooks, in coordination with the relevant suppliers.

4.5 **Evidence.** Evidence shall be collected and preserved with a documented chain of custody, so that it can be used for legal or regulatory action.

4.6 **Notification.** Regulatory and customer notifications shall be made within the required deadlines:
- GDPR personal data breach: notify the supervisory authority within **72 hours**.
- DORA major ICT-related incident: initial notification within **4 hours** of classification (and no later than 24 hours after detection), an intermediate report within **72 hours**, and a final report within **1 month**.
- PCI DSS: notify the card brands and the acquirer as their rules require.

4.7 **Communication.** Only the Incident Commander and Corporate Communications may communicate about an incident externally.

4.8 **Lessons learned.** A post-incident review shall be held within **10 business days** of closing every SEV-1 and SEV-2 incident. Corrective actions shall be tracked to completion.

## 5. Roles and Responsibilities

| Role | Responsibility |
| :--- | :--- |
| Incident Commander (CISO or delegate) | Leads the response for SEV-1 and SEV-2 incidents and makes containment decisions. |
| SOC | Monitors, triages, investigates and coordinates technical response. |
| DPO | Assesses personal data breaches and handles GDPR notifications. |
| Compliance | Classifies incidents under DORA and submits regulatory reports. |
| Legal and Communications | Handle legal hold and external messaging. |

## Compliance and Exceptions

Compliance with this policy is monitored through the controls listed in the Framework Mapping section, internal audit (ISO 27001 clause 9.2) and management review (clause 9.3). Breaches may lead to disciplinary action under the HR disciplinary process (Annex A 6.4).

Exceptions must be requested using the [Policy Exception Request](../templates/policy-exception-request.md), risk-assessed under [POL-10](POL-10-risk-management-policy.md), approved by the CISO and recorded in the risk register with an expiry date of no more than 12 months.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| ID.IM-04 | Incident response and other cybersecurity plans are established, communicated and improved | — | 5.24, 5.27, 5.30 | Strong |
| DE.AE-08 | Incidents are declared when adverse events meet the defined incident criteria | — | 5.25 | Strong |
| RS.MA-01 | The incident response plan is executed in coordination with relevant third parties once an incident is declared | — | 5.26 | Strong |
| RS.MA-02 | Incident reports are triaged and validated | — | 5.25, 6.8 | Strong |
| RS.AN-03 | Analysis is performed to establish what took place during an incident and its root cause | — | 5.27 | Strong |
| RS.AN-06 | Actions performed during an investigation are recorded and the records' integrity is preserved | — | 5.28 | Strong |
| RS.CO-02 | Internal and external stakeholders are notified of incidents | — | 5.24, 5.26, 6.8 | Strong |
| RS.MI-01 | Incidents are contained | — | 5.26 | Strong |
| RS.MI-02 | Incidents are eradicated | — | 5.26 | Strong |
| RC.CO-03 | Recovery activities and progress in restoring operational capabilities are communicated to stakeholders | — | 5.26, 5.29 | Partial |
<!-- mapping:end -->
