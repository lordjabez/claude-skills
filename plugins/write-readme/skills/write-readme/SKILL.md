---
name: write-readme
description: >-
  Writes or rewrites a README.md for one of Jud's own repositories in his
  house style: short, Prerequisites/Usage/To-Do/References structure, linked
  tools, backticked literals, flat caveats, no marketing. Use whenever he
  asks to create, draft, update, tighten, or "write up" a README, document
  how to install or use a script, package, Lambda, CDK construct, or Pi
  project, or add usage, configuration, or deployment instructions to a repo
  he owns, even if he just says "document this". Not for repos with an
  established house style of their own (an employer's or an open-source
  org's template), where that style wins.
---

# Write README

Derived from 12 READMEs across his public GitHub repositories, from short
scripts to published packages. The clean baseline is the solo-authored repos.
Org-template sections (Contributing, Security, Authors) and one recent
AI-assisted README were excluded.

The README reads like notes to a competent future self: what it is, what you
need, how to run it, what's unfinished. The median is about 240 words, and two
thirds of them are under 300.

## Structure

Use only the sections the repo needs, in this order:

```markdown
# Title Case Name

[badges, only for published packages: Tests, Linter, Security, Release]

{One to three sentences: what it is, then current scope or limitation.}


## Prerequisites

## {Task section: Installation | Configuration | Token Creation | Deployment | Testing}

## Usage

## To-Do

## References
```

- **Title**: Title Case with spaces, not the repo slug ("SQL To OData" for
  `sql-to-odata`).
- **No** table of contents, Features list, logo, screenshots, FAQ, Roadmap,
  Support, or Acknowledgments. Credit goes in prose or References.
- **License** only if a LICENSE file exists, as one fixed sentence: "This
  project is licensed under the MIT License. See the [LICENSE](LICENSE) file
  for details."
- Leave **two blank lines** before each `##` heading. It's a consistent habit
  across his repos, so keep it even though some linters flag it.

## Opening

Sentence one states the type and function plainly. Sentence two gives the
current scope, a limitation, or the origin.

- "This repository contains scripts for creating a root certificate authority
  (CA) as well as key pairs signed by said authority."
- "This Python package makes it easy to interact with Google Chrome local
  storage, either a locally-running browser or any remote browser that supports
  remote debugging."
- "An AWS Lambda function that collects data from my thermostats and
  corresponding outdoor temperatures."

Verbs: "contains", "provides", "makes it easy to". No adjectives selling it.

When the paragraph after the opening tells the backstory, write it the way he
describes his own projects: why he needed it, what it does, and an honest
status, with credit given where it's due.

- "I wanted a way for musicians to adjust their own levels without buying an
  entire Aviom setup. So I grabbed a Raspberry Pi and wrote an HTTP server that
  abstracted the details."
- "Given how browser tech evolves, I doubt this still works, and if I have to
  do it again, my first choice would be CloudWatch Synthetics Canaries
  instead."
- "I'm not the original author of this package... When I needed a few new
  features, I offered to write the PRs, and discovered the creator was looking
  for a new owner."
- "Kinda hacky, but it worked more reliably than the bargain basement light
  board and the inexperienced volunteers that ran it."

## Sections

- **Prerequisites**: bullets of tools, each linked to its official download or
  docs page, with an optional " - why it's needed" suffix. Put the install
  command right after: "Installation is via `pip`:" plus a code block.
- **Configuration**: one bullet per key, as `` `key`: Description `` with where
  the value comes from and its format ("Comma-separated lat/lon"). Never a
  table.
- **Deployment and setup steps**: numbered imperatives. Each step names the
  artifact to carry forward ("Copy the function URL in the output"), and
  placeholders are ALL CAPS ("replacing `SECRET` with the copied secret from
  step 2").
- **Usage**: "Basic usage is as follows:" then a code block with `#` comments
  explaining each call in a plain sentence. Follow with one paragraph on
  parameters. Optionally add "In a more complex example, ..." carrying the
  origin story.
- **To-Do**: always spelled "To-Do". Short, unpolished items, occasionally
  wry: "Create a test database that includes more variety of stuff".
- **References**: bare links titled with the page title, no descriptions.

## Line-level style

- Imperative and impersonal ("Install...", "Run..."), "you" occasionally, and
  "I/my" only for motivation in personal repos. Never "we".
- Assume competence. Don't explain Lambda, venv, or PATH. Do explain the
  fiddly thing, in a "because" clause right next to the instruction, not in a
  background section.
- State caveats flatly, with "Note that..." or "Currently...": "Note that the
  function URL endpoint itself is unauthenticated, but an HMAC signature check
  is performed." No warning blocks, admonitions, or bold.
- Backtick every command, file, flag, env var, key, and folder.
- Link every named tool on first mention, preferring official docs.
- Hard-wrap prose at about 90 columns.
- Tag code blocks with a language: `bash` most often, `python`, `javascript`,
  `typescript`.
- Zero emoji, exclamation points, bold, tables, or em dashes.
- Use `-` for bullets. Older repos used `*` followed by two spaces, but his
  current Markdown rules call for `-`.

A generic template and two invented exemplars: [examples.md](examples.md).
Open it when writing a README from scratch.

## Check the draft

1. Under 300 words, unless the tool genuinely has several setup paths?
2. Does sentence two state a limitation or the current scope?
3. Is every tool linked and every literal backticked?
4. Any section that a typical README has but his don't (Features, ToC,
   Contributing on a personal repo)? Cut it.
