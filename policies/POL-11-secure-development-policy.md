# Secure Development Policy

| Field | Value |
| :--- | :--- |
| **Document ID** | POL-11 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Head of Engineering |
| **Approved by** | CISO |
| **Effective date** | 2026-01-15 |
| **Next review** | 2027-01-15 |

## 1. Purpose

To make sure software and infrastructure code are designed, built, tested and released securely.

## 2. Scope

This policy covers all applications, APIs, Infrastructure-as-Code and scripts that Meridian Payments develops, or that are developed for it, including outsourced development.

## 3. Policy Statements

### 3.1 Secure Design
- Security and privacy requirements shall be defined for every new system and for significant features.
- Threat modelling (STRIDE) shall be carried out for systems that handle Restricted or Confidential data.

### 3.2 Secure Coding
- Developers shall follow secure coding standards based on OWASP ASVS Level 2.
- Secrets must not be committed to source code. Secret scanning shall block commits that contain them.

### 3.3 Security Testing in CI/CD
Every pipeline shall include:

| Control | Tooling (example) | Gate |
| :--- | :--- | :--- |
| Static analysis (SAST) | CodeQL / Semgrep | Block on Critical or High findings |
| Dependency scanning (SCA) | Dependabot / Snyk | Block on Critical findings that have a fix available |
| Secret scanning | GitHub secret scanning / Gitleaks | Block |
| IaC scanning | Checkov / tfsec | Block on Critical findings |
| Container image scanning | Trivy / Defender for Containers | Block on Critical findings |
| Dynamic testing (DAST) | OWASP ZAP | Run before every major release |

### 3.4 Source Code and Pipeline Security
- Main branches shall be protected. Every merge requires at least one peer review, and the author cannot approve their own change.
- Pipelines shall authenticate to the cloud using short-lived OIDC federation, not long-lived keys.
- Production, test and development environments shall be kept separate. Production data must not be used in non-production environments unless it is masked.

### 3.5 Outsourced Development
- Contracts with external developers shall require them to follow this policy and allow Meridian Payments to review their code and test results.

## 4. Roles and Responsibilities

| Role | Responsibility |
| :--- | :--- |
| Engineering Leads | Make sure teams follow this policy and fix findings. |
| Application Security | Defines standards, sets up tooling and supports threat modelling. |
| Developers | Write secure code and address findings. |

## Compliance and Exceptions

Compliance with this policy is monitored through the controls listed in the Framework Mapping section, internal audit (ISO 27001 clause 9.2) and management review (clause 9.3). Breaches may lead to disciplinary action under the HR disciplinary process (Annex A 6.4).

Exceptions must be requested using the [Policy Exception Request](../templates/policy-exception-request.md), risk-assessed under [POL-10](POL-10-risk-management-policy.md), approved by the CISO and recorded in the risk register with an expiry date of no more than 12 months.

## Framework Mapping

<!-- mapping:start -->
_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv) by `scripts/build_mapping.py`. Do not edit by hand._

| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |
| :--- | :--- | :--- | :--- | :--- |
| PR.PS-06 | Secure software development practices are integrated and their performance is monitored | — | 8.25, 8.28, 8.29 | Strong |
<!-- mapping:end -->
