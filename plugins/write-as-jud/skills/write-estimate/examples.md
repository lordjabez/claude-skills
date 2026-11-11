# Estimate Examples

These examples are invented. The projects, task names, and numbers are made up,
and the figures are round numbers chosen so the arithmetic is easy to check.

## Small app estimate

```text
Permit Portal Estimate

TL;DR: $175,000. First release in 6 weeks, followed by 4 weeks of fixes, polish,
and handover.

Team of 2.5 (BE, FE, PM@50%)

Assumption: starting point is the city's existing form-builder library

Launch (560 hrs) - round up to 6 weeks x 2.5 people
Permit data model: 60 hours
Application form builder: 120 hours
Payment gateway integration: 80 hours
Reviewer queue: 120 hours
Email notifications: 40 hours
Automated test scenarios: 60 hours
Deployment and UAT: 60 hours
First-release docs: 20 hours

Improvements (380 hrs) - round up to 4 weeks x 2.5 people
Bug fixes and stabilization: 60 hours
Applicant feedback sessions: 40 hours
Reporting dashboard: 160 hours
Reviewer workflow tweaks: 80 hours
Handoff documentation: 40 hours

10 weeks x 2.5 people

Each team-week costs 40x$150 + 40x$100 + 20x$200 = $6,000 + $4,000 + $4,000 =
$14,000 / week = $140,000 x 1.25 contingency (standard assumptions) = $175,000
```

## Bid priced by task, with backing data

```text
The scope section and the price form disagree on the number of option years. I'm
going with the scope section.

Task 1 (Source System Audit): $60,000 in Base Period
Task 2 (Status Reports): $18,000 in Base Period, $9,000 in Options 1-3
Task 3 (Cutover and Validation): $86,000 in Base Period
Task 4 (Ongoing Support): $120,000 per Option Period, $60,000 in a 6 month extension
Task 5 (Data Quality Guarantee): $20,000 per Option Period

Shout if anything looks off. I'm on slack most afternoons.

Backing data (not to share):

Task 1: 4 weeks, 5 people at half time = 5 x 80 hours = 400 hours x $150 / hr
(blended rate, already includes overhead and contingency) = $60,000

Task 2: 5 hours per report x 2 people (PM drafts, engineer supplies metrics) x 12
per year = 120 hrs x $150 = $18,000. Option-period reports reuse the base template
(~50% discount) so $9,000.

Task 3: 3 hours of validation per batch x 2 people x 20 batches = 120 hours, plus
a parallel-run window (4 people x 2 weeks x 40 hours = 320 hours). (120 + 320) x
$150 = $66,000, plus two security scans at $10K each = $86,000.

Task 4: Support on our last migration ran $40K a year for business hours.
Round-the-clock coverage needs about three shifts, so $120K. Six months is half
of that, $60K.

Task 5: No clue what a data quality guarantee is worth. 10% of the $164,000 base
price is $16,400, so I'm rounding up to $20,000, but it's a coin flip.

What can be reduced:
- Reduce Data Quality Guarantee by $20,000
  - if the validation reports from Task 3 are enough to serve as the guarantee
- Reduce Ongoing Support by $40,000
  - if coverage can be business hours plus on-call instead of 24x7
Both reductions bring the Option Period cost to $89,000 annually.
```

## Scope definitions that protect a price

```text
Major issue - problems that block a core function, such as
- applicants cannot submit an application
- payments are charged but not recorded
Minor issue - problems that leave core functions working
- pages that load slowly but finish
- typos and misaligned labels
Feature enhancement - changes that satisfy every one of these
- leave the way an existing capability works fundamentally intact
- add no new screens to a user workflow
- need no new connections to or data from outside systems
New feature - changes that satisfy any of these
- add a capability the system never had
- add a new user workflow
- connect to an outside system
```

## Phased estimate with risks

```text
Roles
- Tech lead: 0.25 FTE
- Data engineer: 1 FTE
- Analyst: 0.5 FTE for the first 4 weeks

Assumptions
- The county provides a test copy of the database before week 2.
- The existing address-lookup service is reused as-is.

Risks
- The legacy nightly export running longer than the cutover window
- Reviewer sign-off taking more than three days per batch
```
