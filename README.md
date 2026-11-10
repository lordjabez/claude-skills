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
/plugin install update-documentation@claude-skills
/plugin install write-as-jud@claude-skills
```

## Available Skills

### create-skill

Builds a new skill, or restructures an existing one, using progressive
disclosure so `SKILL.md` stays small and detail loads only when needed.

Covers naming (verb-first for skills that act, noun phrases for skills that are
reference), writing a description that actually triggers, the four disclosure
levels and what belongs at each, the full frontmatter field reference, and
verification by trigger test, near-miss test, and baseline comparison. Bundles a
copyable template and checklist.

### update-documentation

Reviews `README.md`, `CLAUDE.md`, and other documentation across a repo for
stale, missing, or contradictory content. Runs in a subagent so the review does
not consume the main session's context.

### write-as-jud

Writes prose in my voice: emails, blog posts, social posts, and anything else
going out under my name. Built from an analysis of about 350 long-form pieces
and 850 sent emails, with a shared core voice plus separate modes for email,
blog, and formal technical writing.

Nobody else needs to sound like me, so this one is mostly a worked example. Fork
it, run the same kind of analysis on your own writing, and swap in the results.
The email examples are invented, written to match the observed patterns.

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
