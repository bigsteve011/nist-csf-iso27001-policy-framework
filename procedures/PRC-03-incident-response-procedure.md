# Incident Response Procedure

| Field | Value |
| :--- | :--- |
| **Document ID** | PRC-03 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Head of Security Operations |
| **Approved by** | CISO |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

**Parent policy:** [POL-04 Incident Management Policy](../policies/POL-04-incident-management-policy.md)

## 1. Objective

To give step-by-step instructions for handling security incidents from detection to closure, based on NIST SP 800-61 Rev. 3 and aligned with the NIST CSF 2.0 Respond and Recover functions.

## 2. Phases

### Phase 1: Detect and Triage
1. Receive the alert or report and open a ticket in the incident management tool.
2. Validate it: is it a true positive? Enrich it with asset criticality, data classification and threat intelligence.
3. Assign a severity using the POL-04 matrix. **Declare an incident** if the criteria are met.
4. For SEV-1 and SEV-2: page the Incident Commander, open a war-room bridge and start the incident log.

### Phase 2: Analyse
5. Determine the scope: which systems, accounts and data are affected, and the timeline of attacker activity.
6. Collect evidence before making any changes:
   - memory and disk images
   - cloud logs
   - EDR telemetry

   Hash every artefact and record it on the chain-of-custody form.
7. Compliance assesses whether the incident is a **DORA major incident**. The DPO assesses whether it is a **GDPR personal data breach**. Start the regulatory clocks.

### Phase 3: Contain
8. Short-term containment: isolate hosts through EDR, disable compromised accounts and revoke their sessions, and block indicators of compromise at the firewall, WAF and email gateway.
9. Long-term containment: apply temporary rule changes and segment the affected systems while eradication is prepared.

### Phase 4: Eradicate
10. Remove the malware or persistence, close the vulnerability that was exploited, and reset affected credentials and keys.
11. Confirm that no indicators of compromise remain by searching the whole environment.

### Phase 5: Recover
12. Restore systems from known-good backups, checking their integrity first (see [PRC-05](PRC-05-backup-and-restore-testing-procedure.md)), and rebuild compromised hosts.
13. Return the systems to production with closer monitoring for **30 days**.
14. Keep stakeholders updated on recovery progress at agreed intervals.

### Phase 6: Notify and Communicate

| Audience | Trigger | Deadline | Owner |
| :--- | :--- | :--- | :--- |
| Supervisory authority (GDPR) | Personal data breach with risk to individuals | 72 hours | DPO |
| Financial regulator (DORA) | Major ICT-related incident | Initial report 4 hours after classification; intermediate 72 hours; final 1 month | Compliance |
| Card brands / acquirer | Suspected cardholder data compromise | As their rules require | CISO |
| Affected individuals | High risk to individuals' rights | Without undue delay | DPO / Comms |
| Management Board | SEV-1 | 1 hour | Incident Commander |

### Phase 7: Post-Incident Review
15. Within **10 business days**, hold a blameless review covering what happened, the root cause, what went well and what to improve.
16. Record corrective actions with owners and due dates. Update playbooks, detection rules and the risk register.
17. Close the incident when all evidence is archived and the corrective actions are tracked.

## 3. Playbooks
Each incident type has its own playbook: ransomware, business email compromise, compromised cloud credentials, data exfiltration, DDoS and insider threat. The playbooks extend this procedure.

## Records

Records produced by this procedure are kept for at least **3 years**, or longer where a regulation requires it, and must be available as audit evidence.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| ID.IM-04 | Incident response and other cybersecurity plans are established, communicated and improved | — | 5.24, 5.27, 5.30 | Strong |
| DE.AE-02 | Potentially adverse events are analysed to better understand associated activities | — | 5.25, 8.16 | Strong |
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
