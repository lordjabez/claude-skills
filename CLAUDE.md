# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Claude Code plugin marketplace. Content is almost entirely Markdown skills; the only code is a small Python linter. There is no build step.

## Commands

```bash
claude plugin validate .        # the only CI check (.github/workflows/validate.yml, on every push)

# Advisory voice linter: warnings only, always exits 0, stdlib-only
plugins/write-as-jud/skills/write-as-jud/scripts/voice_lint.py --mode email draft.md
plugins/write-as-jud/skills/write-as-jud/scripts/voice_lint.py --mode blog -   # stdin
```

Modes: `email`, `blog`, `proposal`, `notes`, `estimate`, `feedback`. Phrase tells live in `scripts/tells.txt` (`phrase | suggestion`, one per line).

## Layout and conventions

- Each skill ships as its own plugin under `plugins/<name>/`, with `.claude-plugin/plugin.json` and `skills/<name>/SKILL.md`. One plugin per skill keeps install-time context cost down; bundle skills into one plugin only when they must be co-present (see README "Why one plugin per skill").
- `write-as-jud` is the exception: one plugin with a core voice skill plus companions (`write-proposal`, `write-estimate`, `write-feedback`, `write-notes`) that build on it. Companions reach the shared linter by relative path, `${CLAUDE_SKILL_DIR}/../write-as-jud/scripts/voice_lint.py`, both in their `allowed-tools` frontmatter and in their body. Moving or renaming the core skill or its `scripts/` breaks all of them.
- Skills follow progressive disclosure as described by `create-skill`: a small `SKILL.md` with a trigger-focused `description`, and detail pushed into sibling files (`reference.md`, `examples.md`, mode files like `email.md`/`blog.md`) that the SKILL.md tells Claude when to read.
- `style-of-the-faith` is a reference skill (`user-invocable: false`) with no workflow; other skills load it for palette and typography. `tokens.css` must stay in sync with `palette.md`.
- Style skills encode only the spec they were given. Don't infer conventions from older artifacts; ask when the source is silent.

## When adding or changing a plugin

Several things must stay in agreement, and `validate` won't catch drift in all of them:

- The plugin description is duplicated in `plugins/<name>/.claude-plugin/plugin.json` and its entry in `.claude-plugin/marketplace.json`. Keep them identical.
- Bump `version` in `plugin.json` when a plugin's content changes (installed copies update on version).
- New plugins need a marketplace entry, an install line in README "Installation", and a section in README "Available Skills".

## Writing rules for skill content

The voice skills deliberately avoid em dashes, "not X but Y" framing, and the filler phrases in `tells.txt`. Hold edits to those skills, and their examples, to the same rules. Examples in the voice skills are invented to match observed patterns, except blog quotes, which come from the public blog.
