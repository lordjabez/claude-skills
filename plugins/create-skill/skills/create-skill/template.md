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

## <Step 1 name>

<Instructions written to Claude, with exact commands and paths.>

## <Step 2 name>

<...>

## Failure modes

- <What usually goes wrong> → <what to do about it>
```

Checklist before calling it done:

- [ ] Name is verb-first if the skill acts, a noun phrase if it is reference
- [ ] Description names concrete triggers, not a category, and errs on the
      pushy side
- [ ] Every "use this when" lives in the frontmatter, not the body
- [ ] SKILL.md is under 150 lines
- [ ] Every bundled file has a "open this when" pointer
- [ ] Deterministic or repeated work lives in `scripts/`, not prose
- [ ] Rules are stated as reasons, not as capitalized ALWAYS/NEVER
- [ ] `npx markdownlint-cli --disable MD013 -- SKILL.md` is clean
- [ ] Trigger-tested in a fresh session: a hit, and a near-miss that stays quiet
- [ ] Baselined against a run without the skill, and it clearly won
