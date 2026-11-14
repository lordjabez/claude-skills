# Claude Skills

Agent Skills for [Claude Code](https://code.claude.com), published as a plugin
marketplace. Each skill is its own plugin, so you install only the ones you
want and only pay context for those.

## Installation

Add the marketplace once:

```bash
/plugin marketplace add lordjabez/claude-skills
```

Then install whichever skills you want:

```bash
/plugin install create-skill@claude-skills
/plugin install draw-architecture-diagram@claude-skills
/plugin install style-of-the-faith@claude-skills
/plugin install update-documentation@claude-skills
/plugin install write-as-jud@claude-skills
/plugin install write-readme@claude-skills
```

## Available Skills

### create-skill

Builds a new skill, or restructures an existing one, using progressive
disclosure so `SKILL.md` stays small and detail loads only when needed.

Covers naming (verb-first for skills that act, noun phrases for skills that are
reference), writing a description that actually triggers, the four disclosure
levels and what belongs at each (including per-form files behind a routing
table, and bundled scripts and starter assets), the full frontmatter field
reference, and verification by trigger test, near-miss test, and baseline
comparison. Bundles a copyable template and checklist.

### draw-architecture-diagram

Draws cloud architecture and data-flow diagrams as draw.io XML, laid out the
way I draw them: one account or project boundary, layers running from users to
business logic to data to background jobs, and external systems as clouds
around the edge. Covers four archetypes (application, data platform, pipeline,
multi-tenant concept), edge and label conventions, porting between clouds, and
the exact draw.io style strings for the recurring elements. Ships a sanitized
`template.drawio` as the starting point for application diagrams.

### style-of-the-faith

The visual identity of the Church of the Incandescent Filaments: a named
palette of 43 swatches, Libre Franklin and EB Garamond typography, semantic
color roles, and contrast guidance. Holds no workflow of its own. Skills that
build decks, documents, and artifacts load it so colors and fonts live in one
place. Ships a `tokens.css` for HTML and WeasyPrint output.

### update-documentation

Reviews `README.md`, `CLAUDE.md`, and other documentation across a repo for
stale, missing, or contradictory content. Runs in a subagent so the review does
not consume the main session's context.

### write-as-jud

Writes prose in my voice: emails, blog posts, social posts, and anything else
going out under my name. Built from an analysis of about 350 long-form pieces
and 850 sent emails, with a shared core voice plus modes for email and blog.

Four companion skills build on the core voice for other genres, each derived
from its own set of samples:

- `write-proposal`: proposals, RFP and RFI responses, SOWs, architecture
  narratives, and security questionnaire answers
- `write-estimate`: level-of-effort estimates, pricing rationale, work orders,
  and hours tracking, with the math always visible
- `write-feedback`: feedback letters, recommendations, reviews,
  self-assessments, resumes, bios, and talk tracks for hard conversations
- `write-agenda`: interview guides, screening agendas, 1-on-1 agendas, and
  question banks

They ship in one plugin because they share the core voice and its linter.
`scripts/voice_lint.py` is a small, dependency-free, warnings-only check for
mechanical tells (em dashes, filler and hype phrases, "not X but Y" framing,
spelled-out contractions, length), with the phrase list in `scripts/tells.txt`.
It's a floor, not a judge of voice.

Nobody else needs to sound like me, so this one is mostly a worked example. Fork
it, run the same kind of analysis on your own writing, and swap in the results.
Quotes in the blog mode come from my public blog. Every other example is
invented, written to match the observed patterns.

### write-readme

Writes READMEs for my own repositories in my house style: short, with
Prerequisites, Usage, To-Do, and References sections, every tool linked, every
literal backticked, and no marketing. Derived from a dozen of my public
READMEs. Like `write-as-jud`, it's a worked example to fork.

## Why one plugin per skill

Every installed skill's description sits in Claude's context in every session,
whether or not the skill fires. Bundling unrelated skills charges that cost to
people who wanted one of them. Skills here ship separately unless they are a
system that has to be co-present, in which case they would ship as a single
plugin.

## Contributing

Issues and pull requests are welcome. New skills should follow the structure
that `create-skill` describes, and `claude plugin validate .` should pass before
opening a PR.

## License

MIT
