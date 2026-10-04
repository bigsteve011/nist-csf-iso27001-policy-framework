# Policy Lifecycle Procedure

| Field | Value |
| :--- | :--- |
| **Document ID** | PRC-08 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Chief Information Security Officer (CISO) |
| **Approved by** | Information Security Steering Committee |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

**Parent policy:** [POL-01 Information Security Policy](../policies/POL-01-information-security-policy.md)

## 1. Objective

To control how security policies and procedures are written, approved, published, reviewed and retired, as required by ISO 27001 clause 7.5 (documented information).

## 2. Document Hierarchy

| Level | Type | Approved By | Review Cycle |
| :--- | :--- | :--- | :--- |
| 1 | Information Security Policy (POL-01) | Management Board | Annual |
| 2 | Topic-specific policies (POL-02 to POL-11) | CISO, or the Board where indicated | Annual |
| 3 | Procedures (PRC-xx) | Document owner | Annual |
| 4 | Standards, playbooks, work instructions | Document owner | As needed, at least every 2 years |

## 3. Steps

| # | Step | Owner | Output |
| :---: | :--- | :--- | :--- |
| 1 | **Trigger:** the annual review date, or a change in regulation, an audit finding, an incident or a significant change in technology. | Document Owner | Change request |
| 2 | **Draft or revise** the document using the standard template. Update the framework mapping CSV if the scope of controls changes. | Document Owner | Draft (pull request) |
| 3 | **Consult** the affected stakeholders, Legal, the DPO and Compliance, for at least 10 business days. | Document Owner | Comment log |
| 4 | **Check quality:** CI confirms the framework mapping is valid and the generated sections are up to date. A peer reviews clarity, the use of "shall" and whether each statement is testable. | GRC Team | Approved PR review |
| 5 | **Approve** at the right level (see §2). Record the approval in the version history. | Approver | Approval record |
| 6 | **Publish** to the policy portal and notify the affected personnel. Collect attestations for Level 1–2 policies. | GRC Team | Attestation report |
| 7 | **Monitor compliance** through control testing and exceptions. | GRC Team | Compliance metrics |
| 8 | **Retire** documents that have been replaced. Archive them for 7 years. | GRC Team | Archive record |

## 4. Writing Standards
- Use **"shall"** for mandatory requirements, **"should"** for recommendations and **"may"** for things that are optional.
- Each policy statement must be testable: an auditor must be able to collect evidence that it is being met.
- Keep policies at the level of *what* is required, and procedures at the level of *how*.

## Records

Records produced by this procedure are kept for at least **3 years**, or longer where a regulation requires it, and must be available as audit evidence.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| GV.PO-01 | Cybersecurity policy is established, communicated and enforced | 5.2, 7.5 | 5.1 | Strong |
| GV.PO-02 | Cybersecurity policy is reviewed and updated to reflect changes in requirements, threats and technology | 7.5, 9.3 | 5.1, 5.36 | Strong |
<!-- mapping:end -->
