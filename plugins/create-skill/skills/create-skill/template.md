# Skill Template

Copy the block below into `<location>/skills/<skill-name>/SKILL.md` and replace
the bracketed parts. Delete any section that has nothing to say.

```markdown
---
name: <skill-name>
description: >-
  <What it does, in third person.> Use when <the concrete situations, verbs,
  file types, tool names, and error strings that should trigger it>.
---

# <Skill Name>

<One or two lines on what this skill is for and what it assumes.>

<Pointers to bundled files, each with a reason to open it:>
- <Lookup material>: [reference.md](reference.md)
- <Worked examples>: [examples.md](examples.md)

<Or, when each run needs one of several forms, a routing table:>

| Form | Shape | Open |
| --- | --- | --- |
| <Form A> | <one-line shape> | [form-a.md](form-a.md) |

## <Step 1 name>

<Instructions written to Claude, with exact commands and paths.>

## <Step 2 name>

<...>

## Failure modes

- <What usually goes wrong> → <what to do about it>
```

## Verify it

1. Lint the Markdown: `npx markdownlint-cli --disable MD013 -- <file>.md`.
2. Confirm the frontmatter uses only supported keys (see
   [reference.md](reference.md)). An unknown key is a hard error on packaging.
3. Confirm the skill is listed: run `/skills`, or `/skill-doctor` if available,
   for a structural report.
4. Trigger-test it. In a fresh session, use a phrase from the intended trigger
   set and confirm the skill loads without being named.
5. Near-miss test it. Try a prompt that shares vocabulary or subject matter with
   the skill but needs something else. An obviously unrelated prompt proves
   nothing; the negative case has to be one a naive keyword match would get
   wrong. If either test comes out wrong, fix the description, not the body.
6. Baseline it, for any skill worth the effort of building. Run a representative
   task in a session without the skill and compare. Equivalent outputs mean the
   skill is spending context and buying nothing. Judge it on the general case
   rather than the two or three prompts you happened to test with, and resist
   tightening the skill around those specific examples.

Those checks are enough for a personal or project skill. A skill that will run
at scale, where a spot check is not proof, wants a real eval harness instead:
see "Measuring a skill" in [reference.md](reference.md).

## Checklist before calling it done

- [ ] Name is verb-first if the skill acts, a noun phrase if it is reference
- [ ] Description names concrete triggers, not a category, and errs on the
      pushy side
- [ ] Every "use this when" lives in the frontmatter, not the body
- [ ] SKILL.md is under 150 lines
- [ ] Every bundled file has a "open this when" pointer
- [ ] Form-specific detail lives in per-form files behind a routing table
- [ ] Deterministic or repeated work lives in `scripts/`, not prose, and a
      repeated starting file ships as an asset
- [ ] Rules describe what to do; no lists of one-off patterns to avoid
- [ ] Rules are stated as reasons, not as capitalized ALWAYS/NEVER
- [ ] `npx markdownlint-cli --disable MD013 -- SKILL.md` is clean
- [ ] Trigger-tested in a fresh session: a hit, and a near-miss that stays quiet
- [ ] Baselined against a run without the skill, and it clearly won
