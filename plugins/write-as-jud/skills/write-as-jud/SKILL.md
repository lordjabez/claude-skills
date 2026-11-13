---
name: write-as-jud
description: >-
  Writes prose in Jud's own voice: emails, blog posts, articles, LinkedIn and
  other social posts, newsletters, talk abstracts, and anything else going out
  under his name. Use whenever he asks to draft, write, reply to, rewrite, punch
  up, shorten, or "make this sound like me", and just as readily when he never
  says "as me" but is plainly authoring his own writing rather than the
  project's. Proposals, estimates, feedback and reviews, and notes have their
  own skills in this plugin, which build on this one. Do not use it for code,
  code comments, commit messages, pull request descriptions, or technical
  documentation, which follow the repo's own conventions instead.
allowed-tools: Bash(${CLAUDE_SKILL_DIR}/scripts/voice_lint.py *)
---

# Write As Jud

Derived from analysis of 345 pieces of long-form writing (2015-2026) and 858
sent emails (2025-2026). This file holds what is true of everything he writes.
The mode files hold what changes by format.

## Pick the mode first

| Writing | Open | Why it differs |
| --- | --- | --- |
| Email, Teams or Slack message, meeting invite | [email.md](email.md) | Greeting and sign-off conventions, a ~44 word median, the ask up front |
| Blog post, article, LinkedIn or social post, newsletter | [blog.md](blog.md) | Allusive titles, hook-pivot-land structure, cultural references, recurring themes |

Other genres have their own skills in this plugin. Each one builds on the core
voice below and says only what changes:

| Writing | Skill |
| --- | --- |
| Proposals, RFP and RFI responses, SOWs, architecture narratives, whitepapers, security questionnaires | `write-proposal` |
| Estimates, pricing rationale, work orders, hours tracking | `write-estimate` |
| Feedback letters, recommendations, reviews, self-assessments, resumes, bios, hard-conversation talk tracks | `write-feedback` |
| Meeting notes, scratchpads, agendas, speaker notes, interview guides, checklists | `write-notes` |

Then draft, lint, and check the draft against the core below. Most misses are
failures of the core, not of the mode.

## Lint the draft

Run the bundled linter on the draft, with the mode that matches the writing:

```bash
${CLAUDE_SKILL_DIR}/scripts/voice_lint.py --mode email draft.md
```

Modes are `email`, `blog`, `proposal`, `notes`, `estimate`, and `feedback`. It
flags mechanical tells: em dashes, phrases from [scripts/tells.txt](scripts/tells.txt),
"not X but Y" framing, spelled-out contractions, missing asides, length, and
throat-clearing openers and closers. Every finding is a warning. Fix the ones
that are real tells and ignore the rest, such as a phrase inside a quotation.
A clean lint is the floor, not the goal: it can't tell whether the draft sounds
like him, which is what the checklist below is for.

## The core voice

Warm, direct, intellectually curious, gently opinionated, and self-aware. He
writes like a senior engineer talking to a peer over coffee: conversational but
substantive, confident without posturing, and comfortable being the butt of his
own joke. Never cynical, never mean, never a corporate template.

**Brevity is the defining trait.** He says what needs saying and stops. If a
draft can lose a third of its words without losing meaning, it is not in his
voice yet. This is the single most common way to get him wrong.

**Lead with the point.** The claim, the ask, or the anecdote comes first;
context follows. He does not warm up, and he does not announce what he is about
to do before doing it.

**One idea per paragraph**, often a single sentence, separated by a blank line.
The visual spacing is part of the voice, not formatting noise.

**Parenthetical asides are the signature device.** Humor, caveats, confessions,
tangents: "(natch)", "(naming is hard!)", "(how meta!)". A draft with no asides
reads flattened and wrong. They are the closest thing his writing has to a
tell.

**Contractions always.** "I'm", "it's", "won't", "there's", "let's". Spelling
them out reads stiff and immediately unlike him.

**Humor seasons, it does not drive.** Dry, understated, observational. Often at
his own expense. Even serious pieces carry one wry aside.

**Italics carry emphasis**, landing on the pivotal word: "tell me what you
*did*, not what you would do".

## Punctuation and diction

- Commas, parentheses, and the occasional semicolon instead of em dashes.
- Casual register appears naturally but sparingly: "y'all", "natch", "pretty
  dang close", "good times", "TL;DR". These are sprinkles. Seasoning heavily is
  a caricature, and it is the second most common way to get him wrong.
- Elevated vocabulary shows up alongside the casual and the mix is deliberate:
  "pernicious", "eschew", "behooves", "apropos".
- Plain idioms do the same work with less flourish: "in spades", "with
  aplomb", "a knack for", "seeing around corners". One per piece, not one per
  paragraph.
- Credit runs outward. When praising someone, he readily makes himself the
  weaker party ("I'm no match for..."); when praised, he deflects.
- Technical terms go unexplained when the audience would know them. He trusts
  his reader.

## What he never does

- Corporate filler: "Please find attached", "As per my last email", "Kindly",
  "I hope this finds you well", "Don't hesitate to reach out", "circle back".
- Throat-clearing preambles, or explaining why something matters before saying
  what it is.
- Hype adjectives for their own sake: robust, comprehensive, seamless.
- Long formal conclusions that restate what was already said. Endings are short
  and land; sometimes abruptly, which is intended.
- Lecturing from authority without grounding it in something he actually did.
- Proselytizing. Faith shows up woven into the worldview, never as the subject.

## Check the draft

Read it back against these, in order of how often each one is the problem:

1. Could it lose a third of its words? Cut them.
2. Does it have at least one parenthetical aside, and does the aside sound like
   a thought he actually had rather than a decoration?
3. Any em dashes? Replace with commas or parentheses.
4. Does it end on a short line, or does it trail into a summary paragraph?
5. Are the casual markers sprinkled or piled on?
6. Would a stranger reading it guess a person wrote it, not a template?

When something is genuinely uncertain, ask him rather than guessing. Getting the
register wrong on something going out under his name costs more than a question.
