---
name: write-feedback
description: >-
  Writes performance and career writing in Jud's voice: peer and upward
  feedback letters, manager reviews of direct reports, self-assessments,
  accomplishment logs, promotion evidence, growth plans, resume bullets, and
  speaker or professional bios. Use whenever he asks to draft, reword, or
  sharpen feedback for someone, write a LinkedIn recommendation or a
  reference for a former colleague, fill out a review form, write his own
  self-review, log or summarize what he accomplished, update a resume, or
  write a bio, including phrasings like "help me tell them what they're doing
  well", "write up my year", or "turn this into resume bullets". Also covers
  hard conversations: talk tracks and talking points for performance
  problems, terminations, layoffs, role changes, team reality checks,
  customer escalations, and raising concerns about a peer or leader ("how do I
  tell them", "I need to let someone go", "script this conversation"). Not
  for interview question guides, which belong to write-agenda.
allowed-tools: Bash(${CLAUDE_SKILL_DIR}/../write-as-jud/scripts/voice_lint.py *)
---

# Write Feedback

This builds on the core voice in the `write-as-jud` skill
([../write-as-jud/SKILL.md](../write-as-jud/SKILL.md)). Read that first if it
isn't already loaded. This file covers only what changes, and wins where the
two differ.

Derived from a handful of feedback letters, manager reviews, a
self-assessment, review reflections, a growth plan, an accomplishments log, a
resume, a bio, a few dozen talk tracks for difficult conversations, and 32
LinkedIn recommendations written over eight years. It
records the approach (structure, moves, tone, ordering, lengths), not the
source text. Every example in this skill is invented.

## Pick the form

Find the form, then open its file before drafting. Each one holds the
structure and moves for that form only.

| Form | Shape | Length | Open |
| --- | --- | --- | --- |
| Feedback letter to a peer or leader | Prose letter: "Name," and signed "Jud" | 450-550 words, six or seven paragraphs | [letters.md](letters.md) |
| Recommendation or reference | Prose, no greeting or signature, third person about them | 60-150 words for light contact, 250-400 for close work | [recommendations.md](recommendations.md) |
| Manager review of a report | Fragment bullets under the template's headings, tagged with values | Three or four bullets per heading | [manager-reviews.md](manager-reviews.md) |
| Self-assessment | Full first-person paragraphs, one per theme | 250-400 words per prompt | [self-assessments.md](self-assessments.md) |
| Accomplishment log or promotion evidence | Nested bullets, action first and number last | 6-20 words per bullet | [accomplishments.md](accomplishments.md) |
| Resume | One- or two-line verb-first bullets dense with outcomes | Five to eight per role | [accomplishments.md](accomplishments.md) |
| Bio | Third person, two short paragraphs | ~110 words | [accomplishments.md](accomplishments.md) |
| Hard conversation | Spoken script or bullet talk track, with the decision up front | Under 120 words for a termination, ~500 for a team reality check | [hard-conversations.md](hard-conversations.md) |

Hard conversations take a different stance and structure from the reviews,
so don't carry habits from the other forms into them.

## Recurring themes

These show up across every review he writes, of others and of himself. Reach
for them when they fit, and don't force them in:

- **Mechanisms over good intentions.** Tracking, documentation, and async
  communication beat sheer force of will.
- **Inclusion over protecting people's time.** Let the other person decide
  what's worth their attention.
- **Enable vs "doing for".** Delegate, step back, and build leaders, not just
  doers.
- **Listen first.** Ask questions before leading with a well-formed position,
  and go looking for evidence that you're wrong.
- **Scaling.** Ask whether the strength holds as the organization grows.

## Check the draft

Run the linter on the draft first, and fix the findings that are real
tells:

```bash
${CLAUDE_SKILL_DIR}/../write-as-jud/scripts/voice_lint.py --mode feedback FILE
```

Then:

1. Is every piece of praise backed by a specific example?
2. Is the growth section at least as long as the praise, and concrete? (Not
   for recommendations, which have none.)
3. Does he implicate himself or offer help somewhere?
4. Does it end looking forward, in one or two sentences? For a
   recommendation, does it end speaking to the reader?
5. Any adjective standing in for evidence? Replace it with what happened.
