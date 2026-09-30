# Skill Reference

Open this when writing frontmatter, deciding where a skill lives, or bundling
scripts. The workflow itself is in [SKILL.md](SKILL.md).

## Frontmatter fields

All fields are optional, but `name` and `description` should always be present.
Boolean fields accept `true`, `false`, `yes`, `no`, `on`, `off`, `1`, and `0` in
any case.

| Field | Purpose |
| --- | --- |
| `name` | Display label. For plugin skills it also sets the final command segment. |
| `description` | What the skill does and when to use it. Always in context. |
| `when_to_use` | Optional split of the trigger half of the description. Combined with `description`, capped at 1,536 characters. |
| `allowed-tools` | Tools Claude may use without a permission prompt during the turn the skill is invoked, e.g. `Read Grep` or `Bash(${CLAUDE_SKILL_DIR}/scripts/render.sh *)`. |
| `disable-model-invocation` | `true` restricts the skill to manual `/name` invocation and blocks preloading into subagents and scheduled tasks. Use for anything with side effects, such as a deploy. |
| `user-invocable` | `false` hides the skill from the slash menu so only Claude can invoke it. |
| `arguments` / `argument-hint` | Positional parameter substitution and the hint shown in the slash menu. |
| `paths` | Glob patterns that limit automatic activation to matching files, e.g. `"**/*.md"`. |
| `shell` | `bash` (default) or `powershell` for inline skill commands. |
| `metadata` | Arbitrary key-value YAML map for your own use. |
| `license`, `compatibility` | Accepted for Agent Skills spec compliance; Claude Code stores but does not act on them. |

Unknown keys are a hard error when packaging or uploading a skill. The spec's
allowed set is narrower than what Claude Code accepts locally:
`allowed-tools`, `compatibility`, `description`, `license`, `metadata`, `name`.
A skill meant to be shared or uploaded should stay inside that set.

## Where skills live

| Location | Scope |
| --- | --- |
| `~/.claude/skills/<name>/SKILL.md` | Personal, every project. |
| `.claude/skills/<name>/SKILL.md` | This project only. |
| `<plugin>/skills/<name>/SKILL.md` | Wherever the plugin is enabled, namespaced as `plugin-name:skill-name`. |
| Enterprise-managed directory | All users in the organization. |

On a name conflict, enterprise wins over personal, and personal wins over
project. Skills take precedence over slash commands of the same name.

Command naming differs by scope. In personal and project skills the directory or
file name defines the command and `name:` is only the display label, with nested
paths appended to break ties. In plugin skills `name:` defines the command
segment, prefixed by the plugin name.

## Directory layout

```text
my-skill/
├── SKILL.md        # required: workflow plus a map of what to open next
├── reference.md    # lookup material, read on demand
├── examples.md     # worked examples, read on demand
└── scripts/
    └── helper.py   # executed, never loaded into context
```

The skill directory path is prepended to SKILL.md at load time, so relative
filenames in the body resolve correctly.

## Bundled scripts

Use `${CLAUDE_SKILL_DIR}` in both `allowed-tools` and the body so the script runs
without a permission prompt and without a hardcoded absolute path:

```yaml
---
name: render-chart
description: Renders a chart from a CSV file
allowed-tools: Bash(${CLAUDE_SKILL_DIR}/scripts/render.sh *)
---

Run `${CLAUDE_SKILL_DIR}/scripts/render.sh <csv-file>` to render the chart.
```

Prefer a script over prose whenever the work is deterministic. A script costs no
context to run, and its output is the same every time.

## Measuring a skill

The trigger and baseline checks in SKILL.md are a spot check. A skill that will
run at scale, or one whose value is disputed, deserves measurement instead.
Anthropic publishes a full harness as a plugin:

```bash
/plugin install skill-creator@claude-plugins-official
```

It runs with-skill and without-skill trials of the same prompts in parallel
subagents, grades each against written assertions, aggregates a benchmark with a
browser viewer for human review, and iterates. Its description optimizer is the
part worth borrowing even on its own: it generates a set of realistic trigger
queries, half of them near-misses that should *not* fire, splits them into train
and held-out test sets, and hill-climbs the description while selecting on the
held-out score so the wording does not overfit.

Two of its findings are baked into SKILL.md and worth restating: Claude
undertriggers skills, so descriptions should err on the pushy side; and Claude
only consults skills for work it cannot comfortably do unaided, so trivial
one-step prompts make useless test cases.
