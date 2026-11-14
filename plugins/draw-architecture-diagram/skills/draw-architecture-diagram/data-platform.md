# Data Platform Layout

For the data platform or secure enclave archetype: multi-account data lakes
and researcher enclaves. The edge, label, and file conventions in SKILL.md
still apply.

- An organization title at the top, then accounts as columns separated by
  heavy vertical and horizontal rules, each labeled in italics ("Management
  Account", "Data Sub-Account").
- An access note under the account name, in small bold caps: "ADMIN-ONLY
  ACCESS".
- Shared security services (SSO, org audit trail, security hub, directory) go
  in the management account at the top, flowing down into the sub-accounts.
- The pipeline that crosses accounts sits inside a dashed box with a bold
  title at the bottom right ("Data Integration Pipeline").
- Data is split by sensitivity into separate buckets
  ("Raw Data", "PII Data", "Non-PII Data", "De-identified Data").
- The researcher-facing tools appear as a callout of tool logos (BI tool, R,
  Python) above the virtual desktop icon.
