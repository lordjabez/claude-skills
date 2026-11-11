---
name: draw-architecture-diagram
description: >-
  Produces cloud architecture and data-flow diagrams the way Jud draws them,
  as draw.io (.drawio) XML or as a specification for one: a single account or
  project boundary, layered users, then business logic, then data, then
  background jobs, with compute grouped in labeled panels and external
  systems as clouds around the edge. Use
  whenever he asks to draw, diagram, sketch, redraw, port (e.g. AWS to GCP),
  or visualize a system architecture, infrastructure, data platform, secure
  enclave, data pipeline, or multi-tenant deployment, or to add a diagram to
  a proposal or architecture doc, even if he doesn't say "draw.io". Not for
  charts of data, org charts, or slide decks.
---

# Draw Architecture Diagram

Derived from about 25 draw.io files and exports, which come down to roughly 12
distinct diagrams once page variants and cloud ports are collapsed. They span
2021-2025, AWS, GCP, and Azure, and serve both proposals and as-built docs.
Several were inherited or co-drawn, so these conventions come from patterns
that hold across many diagrams. Single diagrams that deviate are listed at the
end as options, not rules.

## Pick the archetype

| Archetype | When | Shape |
| --- | --- | --- |
| **Application infrastructure** | A web app or API platform. The most common archetype | One boundary box with layers in a fixed order (below) |
| **Data platform or secure enclave** | Multi-account data lakes and researcher enclaves | Account columns split by heavy rules, a dashed box around the pipeline that crosses them |
| **Pipeline or data flow** | Explaining how records move through jobs, for engineers | Numbered components, edges labeled with data, a Notes list |
| **Multi-tenant concept** | Exec or funder audience, showing how it scales | One tenant block repeated three times, feeding a shared component |

## Application infrastructure layout

This is the strongest pattern: about eight diagrams on both AWS and GCP follow
it almost identically.

**The layer order is the rule: users, then business logic, then data, then
background jobs.** The orientation is a choice:

- **Top to bottom for a document**, such as a proposal or architecture doc
  printed portrait. This is the default.
- **Left to right for a screen**, such as a slide or a shared display, where
  landscape space is plentiful.

If it's unclear where the diagram will be shown, ask. The steps below assume
top to bottom. For left to right, rotate the same sequence so users sit at the
left edge and background jobs at the right.

1. **Outside the boundary, at the top**: a user group icon centered and labeled
   above ("Users", or split as "Authenticated Users" / "Unauthenticated
   Users"). Identity sits to its left: the identity provider as a lock icon,
   with upstream IdPs as cloud shapes ("State IdP", "3P IdP").
2. **The boundary**: one large plain rectangle (or the vendor's account group)
   labeled at the top in bold: "GCP Project", "AWS Account". The diagram title
   goes in large plain text just above the boundary, top right ("Case Management
   Application").
3. **The top row inside**: cross-cutting platform services in a line, with no
   edges (DNS, IAM, logging, monitoring, trace, WAF), then the entry point: a
   CDN, load balancer, or API gateway.
4. **API compute**: a labeled white or light-gray panel named by role ("REST
   API", "API Lambdas", "API Functions") holding the function or service icons.
   Label the icons with a short functional name ("Resume Upload", "Candidate
   Matching"). Use a row of identical unlabeled icons when the point is "many
   functions".
5. **The data row**: databases, object storage, search indexes, and queues,
   each labeled by role. Don't add encryption key icons beside the stores.
   They appear in some inherited diagrams, but he doesn't want them. If
   encryption at rest matters to the reader, say so in the accompanying text.
6. **Background compute**: a second panel ("Backend Lambdas", "Background /
   Admin Jobs", "Microservices") with a scheduler or queue next to it.
7. **External systems** go outside the boundary at the bottom or edges, as
   cloud shapes with plain names ("Jobs API", "Email Service"). Put a small
   note beside one when sourcing matters ("from GCP Marketplace").
8. **CI/CD**, if shown, is a small separate panel down the right side:
   repository, then build, then registry, stacked vertically.

When one account holds two subsystems, give each a light-gray (`#F5F5F5`)
panel with a large title ("Recommendation Engine"). When the customer's
network wraps the account, nest the boundaries (customer network around our
account and VPC) and show the customer's firewalls, WAF, and load balancers
explicitly, with ports on the edges.

## Data platform layout

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

## Edges

- **Orthogonal routing** for internal connections.
- **Dotted lines for traffic over the public internet** (user to CDN, user to
  IdP), labeled with the protocol: "HTTPS", "OAuth", "SAML". Use solid lines
  inside the boundary.
- **Bidirectional arrows** between compute and storage for read/write, and
  single arrows for one-way feeds.
- **Labels are sparse.** Give infrastructure diagrams protocol labels (and
  ports at network boundaries: "Port 443 / HTTPS"). Give pipeline diagrams data
  labels ("Raw job postings", "Cleaned and de-duplicated jobs"). Put a role
  that grants access in italics on the edge ("Pipeline Service Role", "SSO
  Permission Sets"). Most edges carry no label.

## Labels and text

- Helvetica 12 for labels, 14 for panel titles, and 18-24 for the diagram
  title and subsystem titles.
- A component label is either the service name ("Cloud SQL (Postgres)") or a
  role name. Name the role when there are several of the same service ("Case
  Database", "Front End S3").
- As-built versions add the real identifiers: account numbers, CIDR ranges,
  gateway attachment IDs, and hostnames. Proposal versions leave them out.
  Strip them entirely from any generic or template version.
- Unknowns or not-yet-designed parts are plain labeled rectangles, which is
  fine in a working draft.

## Files and pages

- One file per system, with pages for alternatives: "AWS" / "GCP" / "GCP RE
  Only", "As-Built" / "Analytics Extension".
- **Porting between clouds keeps the layout identical** and swaps the icons
  and service names. Readers should be able to diff the two pages by eye.
- Keep open questions on a page of their own, named "Questions", as short
  bullets ("Managed search? Elasticsearch on Compute Engine or alternative?").
- Name files `<System>_<Cloud>_Infrastructure_<YYYYMMDD>` when versioning by
  date.
- When a diagram is reused across customers, keep a sanitized "Generic" copy
  with customer names and identifiers stripped.

Exact draw.io style strings for the recurring elements are in
[reference.md](reference.md). Open it when writing `.drawio` XML by hand.

## Producing the file

1. Write `.drawio` XML using the styles in [reference.md](reference.md). Mixing
   icon generations (`aws3` and `aws4`) is normal in his files, so don't spend
   effort on icon-set purity.
2. Render to check the layout:

   ```bash
   /Applications/draw.io.app/Contents/MacOS/draw.io -x -f png -s 1 -o out.png diagram.drawio
   ```

3. Look at the render, then fix overlapping labels and any edge that crosses a
   boundary it shouldn't.
4. Clean up the PNG unless it was asked for.

## Options seen once (don't default to these)

- Right-to-left flow, from data sources on the right to a public site on the
  left (one executive concept diagram). Left to right, with users on the left,
  is the normal landscape choice.
- Encryption key icons beside every data store (inherited diagrams). He
  doesn't want these, so leave them out even when porting one of those
  diagrams.
- Numbered components keyed to a Notes list giving trigger, schedule, and
  source link (one operational pipeline diagram). Use it when the audience is
  on-call engineers.
- GCP "card" style boxes with drop shadows (two related enclave diagrams). His
  usual GCP style is flat icons.
- Thick colored block arrows, rounded colored zones, and a title with an
  "Updated YYYY-MM-DD" line in the top left (one early Azure draft).
- Marketing-style capability groupings with no real data flow (one
  pre-existing overview).

## Check the diagram

1. Can someone trace a request from the user to the data store and back?
2. Do the layers run users, then business logic, then data, then background
   jobs, in the orientation that suits where it will be shown?
3. Is internet traffic dotted and labeled with a protocol?
4. Is every component inside the boundary of whoever owns it?
5. For a port to another cloud: does the layout match the original page?
