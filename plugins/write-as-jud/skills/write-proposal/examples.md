# Proposal Examples

These passages are invented for illustration. The subjects (a county library
system, a parks reservation app), requirement numbers, products, and figures
are fictional. Use them to calibrate structure and tone, not as source text.

## Architecture section opening

```text
The diagram below shows the major components of the proposed catalog and
lending platform. Each component will be built iteratively and kept modular,
with clearly defined interfaces between neighbors. Managed cloud services will
be used wherever they fit, which shortens delivery and reduces the load on
library IT staff. Custom code is reserved for cases where no managed service
exists, where local rules demand it, or where existing code is worth keeping.
Because the system already runs its public site on a Linux and PostgreSQL stack
(see 3.2.4), hosting on AWS with managed PostgreSQL is recommended.

This design will almost certainly change once discovery begins. It is offered
as a draft to react to, and the project team expects to refine it together
with library staff.
```

Notes: the first sentence points at the diagram, the build philosophy follows,
the platform choice is tied to something the buyer already runs with a
requirement number, and the caveat closes the opening in fresh words.

## Component list keyed to the diagram

```text
- Patron Access (green) - Sign-in, library card lookup, and permissions for the
  public site and the staff console. These services touch most other
  components, so individual arrows are left off the diagram (Section 4.1).
- Lending (purple) - Checkout, renewal, hold, and fine logic, plus the
  nightly jobs that expire holds (Section 4.3).
- Branch Systems & Patrons (gray) - External parties and devices: self-checkout
  kiosks and door counters on one side, patron browsers and apps on the other.
```

## Tradeoff paragraph

```text
A managed workflow service is recommended for overdue-notice scheduling, as
called for in 4.2.7. It is not the open-source scheduler named in that
requirement, but it removes the need for library staff to patch and monitor a
server, and we believe that is the better fit for a team of two administrators.
If the library would rather keep the named scheduler, discovery is the place to
compare both options side by side.
```

## ROI paragraph

```text
The proposed automated renewal line uses a toll-free number billed at $0.02 per
minute. 8,000 calls per month x 4 minutes per call x $0.02 per minute = $640
per month. Against the current answering-service cost of $2,000 per month, this
is a savings of $1,360 per month, or 68%.

These figures assume today's call volume. Neighboring systems report that more
than half of renewals happen online, while here about one quarter do. As
patrons move to the web, call volume and cost will fall further, so the
estimate above is conservative.
```

Arithmetic: 8,000 x 4 = 32,000 minutes; 32,000 x 0.02 = 640; 2,000 - 640 =
1,360; 1,360 / 2,000 = 0.68.

## Assumptions

```text
- 12 MB of circulation records produced per branch annually
- 1 staff console account per 5 volunteers
- Records retained for 7 years, then archived
- No payment card processing (could be added, but extra cost needed)
```

## Future opportunities

```text
The current scope delivers a working reservation flow for a single pilot park.
Several further opportunities could be explored with additional funding and
time. These could include:

- Conduct interviews with campground hosts to learn how walk-up and online
  bookings compete for the same sites
- Build an admin tool for bulk-editing site availability before peak season
- Add a Spanish-language booking flow and test it with community groups
- Send text reminders before arrival and before checkout
- Provide a template for onboarding additional parks, including the
  infrastructure code to stand up a new park's environment
```

## Questionnaire answers

```text
Q: Is source code reviewed or analyzed for vulnerabilities before release?
A: Every pull request runs static analysis and a dependency audit in the CI
pipeline, and a release is blocked on any high-severity finding. A second
engineer reviews each change before merge.

Q: How will you keep staff from using access gained on another contract?
A: We have not worked with this customer before, so there is no prior access
to restrict. Going forward, access will be kept separate as follows:
- Each project has its own repositories and its own access list
- Accounts and credentials for the customer's systems are issued by the
  customer and revoked when a person leaves the project
- Staff are assigned to one project at a time where possible
```

## Internal technical briefing deck

Slides for a partner or internal audience keep a little personality:

```text
Where the Sync Service Runs
- Hosted by us, one shared instance
  - Fastest to start (a week, give or take)
  - Tenants separated by API key
  - Every library shares one upgrade schedule (convenient until it isn't)
- Hosted in the library's own cloud account
  - Data never leaves their boundary
  - Setup takes longer, and someone has to own the bill
  - Mental model is "their copy" vs a shared service
```

## What it should not look like

Boilerplate like this pads an answer with adjectives and says nothing. Never
produce it:

```text
Yes, backups are performed regularly. The organization is committed to
protecting data through industry-standard practices and a holistic approach to
resilience. These measures form part of a comprehensive data protection
strategy, ensuring a robust and reliable environment at all times.
```

The rewrite: "Yes. Database snapshots every 6 hours, kept 30 days, copied to a
second region. Restores are tested each quarter."
