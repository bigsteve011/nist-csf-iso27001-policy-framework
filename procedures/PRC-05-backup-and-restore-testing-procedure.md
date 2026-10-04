# Backup and Restore Testing Procedure

| Field | Value |
| :--- | :--- |
| **Document ID** | PRC-05 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Head of Business Continuity |
| **Approved by** | CISO |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

**Parent policy:** [POL-05 Business Continuity and Backup Policy](../policies/POL-05-business-continuity-and-backup-policy.md)

## 1. Objective

To show that backups can be restored completely and correctly, within the RTO and RPO agreed in the BIA.

## 2. Steps

| # | Step | Owner | Output |
| :---: | :--- | :--- | :--- |
| 1 | Pick the systems to test from the test schedule. For Tier 0, pick one at random each quarter and test all of them within the year. | BC Manager | Test plan |
| 2 | Check the backup job history. Make sure the latest successful backup is within the RPO and that the immutable copy exists. | Infrastructure | Backup status evidence |
| 3 | Check backup integrity by comparing checksums and scanning the backup for malware before restoring it. | Infrastructure | Integrity report |
| 4 | Restore into an isolated recovery environment. Time the restore from start to finish. | Infrastructure | Restore log |
| 5 | The application owner checks that data is complete and the application works, using test cases and record counts. | Service Owner | Validation sign-off |
| 6 | Compare the measured recovery time with the RTO, and the age of the restored data with the RPO. | BC Manager | Test result |
| 7 | Record any shortfalls as risks in the risk register, with a treatment plan. | BC Manager | Risk entries |
| 8 | Tear down the test environment and archive the evidence. | Infrastructure | Evidence pack |

## 3. Production Restores
Steps 2 and 3 are mandatory before **any** restore into production, including during incident recovery.

## Records

Records produced by this procedure are kept for at least **3 years**, or longer where a regulation requires it, and must be available as audit evidence.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| PR.DS-11 | Backups of data are created, protected, maintained and tested | — | 8.13 | Strong |
| RC.RP-01 | The recovery portion of the incident response plan is executed once initiated | — | 5.26, 5.29, 5.30 | Strong |
| RC.RP-03 | The integrity of backups and other restoration assets is verified before using them for restoration | — | 8.13 | Strong |
<!-- mapping:end -->
