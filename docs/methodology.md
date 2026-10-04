# Mapping Methodology

## Approach

1. **Start from outcomes.** NIST CSF 2.0 describes *outcomes* (what good looks like). ISO/IEC 27001:2022 describes *requirements*: the ISMS clauses 4–10 and the Annex A reference controls. Each CSF subcategory was mapped to the ISO requirements that would produce that outcome if they were implemented.
2. **Separate clauses from controls.** GOVERN outcomes mostly map to ISMS clauses, such as 5.1 Leadership and 6.1 risk assessment. PROTECT, DETECT, RESPOND and RECOVER outcomes mostly map to Annex A controls.
3. **Rate the fit.**
   - **Strong:** implementing the mapped ISO requirements as written would meet the CSF outcome.
   - **Partial:** the ISO requirements address the outcome, but only partly. Extra controls or evidence are needed. These are listed in [COVERAGE.md](../mapping/COVERAGE.md#partial-mappings-review-candidates).
4. **Assign ownership.** Each subcategory is assigned to exactly one policy (the *what*) and, where one exists, one procedure (the *how*). This gives auditors one place to look for each outcome.
5. **Cross-check against official references.** The mappings were checked against the NIST OLIR informative reference for ISO/IEC 27001:2022 and the CSF 2.0 Reference Tool. Where this repository's view differs, it is because the mapping takes a stricter, outcome-based view.

## Sources

- NIST Cybersecurity Framework 2.0 (NIST CSWP 29, February 2024)
- ISO/IEC 27001:2022 Information security management systems: Requirements
- ISO/IEC 27002:2022 Information security controls
- ISO/IEC 27005:2022 Guidance on managing information security risks
- NIST SP 800-61 Rev. 3 Incident Response Recommendations
- Regulation (EU) 2022/2554 (DORA), GDPR, PCI DSS v4.0

## Limitations

- This is a **selection of 53 high-value CSF subcategories**, not all 106. They were chosen to cover every CSF category that matters most to a regulated payments company.
- The ISO standards are copyrighted. This repository refers to control **numbers** only and paraphrases outcomes; it does not reproduce the standards' text.
- Meridian Payments is a **fictional** organisation. The policies are templates to be adapted to a real organisation's context, risk appetite and legal advice.
