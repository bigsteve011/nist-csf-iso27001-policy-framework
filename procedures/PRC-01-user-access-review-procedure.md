# User Access Review Procedure

| Field | Value |
| :--- | :--- |
| **Document ID** | PRC-01 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Head of Identity and Access Management |
| **Approved by** | CISO |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

**Parent policy:** [POL-02 Access Control Policy](../policies/POL-02-access-control-policy.md)

## 1. Objective

To confirm on a regular basis that every user's access is still appropriate, and to remove access that is not.

## 2. Frequency

| System Category | Frequency |
| :--- | :--- |
| Privileged accounts (all systems), PCI cardholder data environment | Quarterly |
| Other Tier 0 and Tier 1 applications | Semi-annually |
| All other systems | Annually |

## 3. Steps

| # | Step | Owner | Output |
| :---: | :--- | :--- | :--- |
| 1 | Extract the user and entitlement lists from each in-scope system, such as Entra ID Access Reviews, AWS IAM Access Analyzer and application exports. Record the extraction date and the method used, so completeness can be shown. | IAM Team | Access listings |
| 2 | Reconcile the listings against the HR system. Flag leavers, people who changed role, orphaned accounts and accounts that have been dormant for more than 45 days. | IAM Team | Exceptions list |
| 3 | Send the access listings to reviewers: line managers review their staff, and system owners review privileged and service accounts. | IAM Team | Review campaign |
| 4 | Reviewers decide **Keep** or **Revoke** for every entitlement within **10 business days**. Each Keep needs a business justification. | Reviewers | Certified listings |
| 5 | Remove the revoked access within **5 business days**, then extract the listings again to confirm the removal. | IAM Team | Remediation evidence |
| 6 | Escalate reviews that are not completed to the CISO. If a review is still incomplete after 5 more days, the access is revoked by default. | IAM Team | Escalation log |
| 7 | Report the results: completion rate, revocation rate, and segregation-of-duties conflicts found. | IAM Team | Review report |

## 4. Quality Checks
- Reviewers must not certify their own access.
- A sample of 10% of Keep decisions for privileged access is checked again by Information Security.

## Records

Records produced by this procedure are kept for at least **3 years**, or longer where a regulation requires it, and must be available as audit evidence.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| PR.AA-05 | Access permissions are defined, managed and reviewed using least privilege and separation of duties | — | 5.3, 5.15, 5.18, 8.2, 8.3 | Strong |
<!-- mapping:end -->
