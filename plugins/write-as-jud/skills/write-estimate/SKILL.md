---
name: write-estimate
description: >-
  Writes level-of-effort estimates, cost and pricing rationale, and
  hours-and-budget tracking in Jud's voice: project estimates, price-by-task
  breakdowns for bids, work order outlines, staffing and rate math, reduction
  options, contingency, and burn-down of hours against budget. Use whenever he
  asks to estimate, price, size, scope, cost out, "put numbers on", or "show
  the math" for a project or bid, or to explain how a price was reached to a
  colleague or partner, even if the word "estimate" never appears. For a
  formal staffing-plan workbook use a spreadsheet skill instead; for the
  buyer-facing cost narrative in a proposal use write-proposal.
allowed-tools: Bash(${CLAUDE_SKILL_DIR}/../write-as-jud/scripts/voice_lint.py *)
---

# Write Estimate

This builds on the core voice in the `write-as-jud` skill
([../write-as-jud/SKILL.md](../write-as-jud/SKILL.md)). Read that first if it
isn't already loaded. This file covers only what changes, and wins where the
two differ.

Derived from about eight estimates and pricing write-ups: app and system
estimates, a bid priced by task with backing data, a work order sent to a
partner, and a project hours log.

The defining trait is that **the math is always visible**. A number with no
derivation next to it isn't in his voice.

## Shape

1. **Bottom line first.** "TL;DR: \$175,000. First release in 6 weeks, followed
   by 4 weeks of fixes, polish, and handover." Total, timeline, and
   phases in one or two lines.
2. **Reconcile the sources** before any numbers when the inputs disagree: "The
   scope section and the price form disagree on the number of option years. I'm
   going with the scope section."
3. **Team** on one line, with fractional allocation: "Team of 2.5 (BE, FE,
   PM@50%)".
4. **Assumptions**, starting with the biggest lever: "Assumption: starting
   point is the city's existing form-builder library".
5. **Phases, then tasks with hours.** Phase header with its total and how it
   was rounded ("Launch (560 hrs) - round up to 6 weeks x 2.5 people"), then
   `Task: N hours` lines. Use round numbers (20, 40, 80, 120).
6. **The arithmetic on one line**, ending in contingency:

   ```text
   Each team-week costs 40x$150 + 40x$100 + 20x$200 = $14,000 / week
   = $140,000 x 1.25 contingency = $175,000
   ```

   Pick the multiplier from the tiers in
   [Uncertainty multiplier](#uncertainty-multiplier).

7. **Close** with a short hand-off line if it's going to a colleague: "Shout if
   anything looks off. I'm on slack most afternoons."

## Pricing by task (bids)

- List the prices first, one line per task across every period: "Task 4
  (Ongoing Support): \$120,000 per Option Period, \$60,000 in a 6 month
  extension".
- Put the derivation under a separate heading that says who it's for:
  "Backing data (not to share):". One paragraph per task, in the form people x
  hours x rate = total, with each discount explained ("Option-period reports
  reuse the base template (~50% discount)").
- Anchor to precedent when there's no basis to compute from: "Support on our
  last migration ran \$40K a year for business hours. Round-the-clock coverage
  needs about three shifts, so I'm using \$120K."
- **Say what's a guess.** This is a strong habit and a trust builder:
  "guesstimating a team of 4 for 6 months", "Pure gut feel based on how
  messy the source data looks", "No clue what a data quality guarantee is
  worth. 10% of the \$164,000 base price is \$16,400, so I'm rounding up to
  \$20,000, but it's a coin flip". Keep the candor in internal versions and
  drop it from buyer-facing ones.
- **Offer a menu of reductions** with the condition each one depends on:

  ```text
  What can be reduced:
  - Reduce Data Quality Guarantee by $20,000
    - if the validation reports from Task 3 are enough to serve as the guarantee
  - Reduce Ongoing Support by $40,000
    - if coverage can be business hours plus on-call instead of 24x7
  Both reductions bring the Option Period cost to $89,000 annually.
  ```

- **Bound the scope with definitions** wherever price depends on
  interpretation: major vs minor issue, feature enhancement vs new feature. An
  enhancement must meet *all* of the criteria. A new feature meets *one or
  more*.

## Work order outlines (to partners)

Open conversationally with the split stated: "Hi [name], draft of a 4 week
kickoff work order below. I split the hours 60/40 so your side carries a bit
less of the build." Then:

- Roles by party, as `Role: N hours (\$rate / hr)`, with a subtotal and "(but
  double-check my math)"
- Tasks and deliverables nested by phase with week ranges: "Mapping (Weeks
  1-2)"
- A final deliverable stated concretely: "The last deliverable is a working
  import of one sample dataset in the test environment"
- A "Not in this work order, but coming next" section listing what follows

## Hours tracking

```text
- Mar: 16 hours - Joined weekly calls, reviewed the draft spec and sent comments
- May: 32 hours - Built a sample ingest pipeline locally, fixed encoding bugs, switched parsing libraries midway
- Jul: 8 hours (so far) - Started the sample report. Estimated 24 more required.

Expended hours: 56
Remaining hours (estimated): 24
Remaining hours (budget): 44
```

## Style rules

- Shorthand is fine: "hrs", "x" for multiplication, "\$K" and "\$M", "PM@50%",
  "~50%".
- Write money as "\$14,000 / week", with spaces around the slash.
- Never round a total without saying so ("round up to 6 weeks").
- Always add contingency explicitly, using the tiered multiplier below, rather
  than burying it in rates. If a blended rate already includes it, say so: "\$150 / hr
  (blended rate, already includes overhead and contingency)".
- Keep the shareable output and the internal rationale in separate sections,
  never mixed.

## Uncertainty multiplier

Contingency is a multiplier on the summed task estimates, and its size comes
from the list of assumptions and unknowns:

| Tier | Multiplier | When |
| --- | --- | --- |
| Low | x1.1 | Short or simple assumption list, well-understood work |
| Standard | x1.25 | "Standard" assumptions, the usual case and the default starting point |
| High | x1.5 | Large unknowns or significant anticipated complexity |

Name the tier next to the number so the reader sees why: "x1.25 contingency
(standard assumptions)". There's no hard rule between tiers; it's professional
judgment.

**If there's real doubt about which tier fits, ask Jud before finishing.**
Show him the assumptions and unknowns that drive the doubt, and the total under
each candidate tier, so he can pick with the tradeoff in front of him. Don't
silently default to the middle.

Worked examples, all invented: [examples.md](examples.md). Open them when
producing a full estimate from scratch.

## Check the draft

Run the linter on the draft first, and fix the findings that are real
tells:

```bash
${CLAUDE_SKILL_DIR}/../write-as-jud/scripts/voice_lint.py --mode estimate FILE
```

Then:

1. Does every number have its derivation next to it?
2. Is contingency explicit, with its tier named?
3. Is every guess labeled as one?
4. Are the shareable output and the internal rationale in separate sections?
