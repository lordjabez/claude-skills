---
name: create-skill
description: >-
  Creates a new Claude Code skill, or restructures an existing one, using
  progressive disclosure so SKILL.md stays small and detail loads only when
  needed. Use whenever the user asks to make, write, scaffold, name, refactor,
  split, shrink, debug the triggering of, or review a skill, a SKILL.md file, or
  a slash command. Use it just as readily when the word "skill" never appears:
  turning a repeated workflow, prompt, checklist, or standing set of
  instructions into something reusable is the same request, as is asking why an
  existing skill never fires.
---

# Create Skill

A skill earns its place by changing what Claude does. Two things decide whether
it works: a description that fires at the right moment, and a body that spends
as little context as possible getting there.

Open [reference.md](reference.md) for naming rules, description examples,
frontmatter fields, skill locations, bundled-script mechanics, and how to
measure a skill properly.
Open [template.md](template.md) for a copyable skeleton and a final checklist.

## Step 0: Confirm a skill is the right container

Ask the user only what cannot be inferred from the request:

- What situation should trigger it, in the words a person would actually type?
- What does Claude do differently once it loads? If the honest answer is
  "nothing it would not already do", say so and stop.
- Who is it for: this project (`.claude/skills/`) or every project
  (`~/.claude/skills/`)?

Standing preferences that should always apply are not skills. Put those in
CLAUDE.md or a path-scoped rules file. Automated behavior that must run without
Claude deciding to is not a skill either. That is a hook in `settings.json`.

## Step 1: Name it

Lowercase and hyphenated. The name doubles as the slash command, so read it back
as `/name` and pick the form that sounds right at the point of use:

- A skill that **does something** takes a verb-first imperative: `create-skill`,
  `find-docs`, `review-migrations`. `/create-skill` reads as an instruction.
- A skill that **is knowledge** loaded into context takes a noun phrase:
  `api-conventions`, `markdown`, `claude-api`.

Prefer the verb over agent-form nouns like `skill-creator`.

## Step 2: Write the description

This is the highest-leverage part of the file: always in context, and the only
evidence Claude has when deciding to load the rest.

Write it in third person, describing what the skill does and when to use it.
Name the concrete triggers: the verbs, file types, tool names, and error strings
that should pull it in. Vague descriptions are the single most common reason a
skill never fires.

Lean past merely accurate. Claude undertriggers skills far more often than it
overtriggers them. Name the adjacent phrasings,
and say outright that the skill applies even when the user does not name the
thing directly. A weak and a strong description side by side are in
[reference.md](reference.md); open them if the first draft reads as a category.

Keep it under roughly 1,500 characters, and prefer specificity over hedging.
Read the description back and ask: from this line alone, in a session that knows
nothing else about the skill, would the right prompt trigger it and the wrong
prompt not?

Two mechanics shape both the wording and how it gets tested later:

- Only `description` (plus the optional `when_to_use`) is consulted at decision
  time. Trigger conditions written into the body are never seen, so they cannot
  affect whether the skill loads. Every "use this when" belongs in the
  frontmatter.
- Claude consults skills for work it cannot comfortably do unaided. A one-step
  request like "read this PDF" will not pull in a skill however well the
  description matches, because the base tools already cover it. Skills earn
  their triggers on multi-step or specialized work.

## Step 3: Structure for progressive disclosure

Content sits at one of four levels. Push each piece to the cheapest level that
still works.

1. **Name and description.** Always in context. Budget: a few sentences.
2. **SKILL.md body.** Loaded when the skill triggers. Aim for 150 lines; past
   that, treat every addition as a prompt to push something down a level. Hard
   ceiling 500. It should read as a workflow plus a map of what to open next.
3. **Bundled files** (`reference.md`, `examples.md`, `api/*.md`). Read only when
   the body sends Claude there for a specific need. No size limit that matters.
4. **Scripts and assets** (`scripts/*.py`, `template.drawio`,
   `starter.docx`). Scripts are executed and assets are copied and edited, so
   neither is read into context. Deterministic work belongs here, not in prose
   that Claude has to re-derive each run.

Split a file out when it is needed by one branch of the workflow rather than
every run, when it is lookup material (tables, schemas, field lists) rather than
instruction, or when it would push SKILL.md past a screen or two of reading.
Keep it inline when every run needs it.

When a skill covers several forms or modes and each run needs only one, route
with a table whose last column opens that form's own file (the skeleton in
[template.md](template.md) shows one), and keep in SKILL.md only what every
form shares, such as a final check.

The clearest signal that something belongs in `scripts/` is repetition across
runs. If invoking the skill keeps ending with Claude writing more or less the
same helper, write it once, bundle it, and point at it. That removes the tokens
and the run-to-run variation in one move. The same goes for output: if Claude
keeps assembling the same starting file, bundle a sanitized one as an asset and
have it copy that.

Every bundled file needs a pointer in SKILL.md that says when to open it,
such as "Full field list and validation rules: [reference.md](reference.md)".
A link with no "open this when" line will be ignored or, worse, read every time.

## Step 4: Write the body

- Lead with the workflow. Numbered steps if order matters, headed sections if
  not.
- Write instructions to Claude, not documentation about the skill. "Run X, then
  check Y", not "This skill runs X".
- Show the exact commands, paths, and flags. Do not make Claude guess a filename
  it could have been told.
- Explain why, rather than only commanding. A model that understands the reason
  handles the case you did not anticipate; one following a bare rule does not.
  Catching yourself writing ALWAYS or NEVER in capitals is a signal to reframe
  the rule as its reason.
- Include the failure modes: what usually goes wrong, and what to do about it.
- Cut anything Claude already knows. Generic language or tool knowledge is
  filler; repo-specific and workflow-specific knowledge is the payload.
- Describe the pattern you want. When a skill is derived from samples, drop the
  one-off deviations instead of listing them as things to avoid: the list costs
  context every run and puts the unwanted pattern in front of Claude. A rule
  that is only a prohibition should be rewritten as what to do, or cut.

## Step 5: Verify it

Work through "Verify it" in [template.md](template.md) before calling the skill
done: lint, frontmatter keys, a trigger test, a near-miss test, and a baseline
run without the skill. If a trigger test fails, fix the description, not the
body.

## Step 6: Document it

If the skill lives in a repo or marketplace that lists its skills, such as a
README or a plugin manifest, add it there.
