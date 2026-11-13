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
  for interview question guides, which belong to write-notes.
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

| Form | Shape | Length |
| --- | --- | --- |
| Feedback letter to a peer or leader | Prose letter: "Name," and signed "Jud" | 450-550 words, six or seven paragraphs |
| Recommendation or reference | Prose, no greeting or signature, third person about them | 60-150 words for light contact, 250-400 for close work |
| Manager review of a report | Fragment bullets under the template's headings, tagged with values | Three or four bullets per heading |
| Self-assessment | Full first-person paragraphs, one per theme | 250-400 words per prompt |
| Accomplishment log or promotion evidence | Nested bullets, action first and number last | 6-20 words per bullet |
| Resume | One- or two-line verb-first bullets dense with outcomes | Five to eight per role |
| Bio | Third person, two short paragraphs | ~110 words |
| Hard conversation | Spoken script or bullet talk track, with the decision up front | Under 120 words for a termination, ~500 for a team reality check |

For any hard conversation, open [hard-conversations.md](hard-conversations.md)
before drafting. The stance and structure there differ from the reviews below.

## Feedback letters

The structure is consistent:

1. **A personal, wry opening** that sets the warmth: a light joke about time
   passing or about how the job is going, then a single line of gratitude
   aimed at the person.
2. **Two or three paragraphs of specific praise.** Each names a strength and
   then gives the evidence as a list inside one sentence (three clauses, or
   two, or four; vary it), often with a parenthetical aside about how the
   person also coaches others.
3. **The pivot**, short and explicit. "That being said," works, as does
   naming the cost of the strength itself.
4. **Two or three growth paragraphs.** Name the pattern, say why it won't
   scale, then make concrete suggestions in a single sentence, each one small
   and doable, ending on the humblest one.
5. **Implicate himself.** He never critiques from above. He says the challenge
   isn't unique to the reader, admits where he has work to do, asks to be
   included more, and invites suggestions back.
6. **Offer specific help**, naming what he could do (coaching, building a
   tool, making an introduction) and ending with an invitation to ask.
7. **A forward-looking close**, one or two sentences, in the family of "Here's
   to a great year."

Italics land on the pivotal word, once or twice per letter. One parenthetical
joke per letter is about right.

## Recommendations and references

Written for a stranger deciding whether to hire or work with the person, so
everything is in service of credibility. Praise only, no growth section.

1. **Establish standing in the first sentence**: how long, where or on what,
   and the exact relationship. Be precise when it's indirect ("I didn't manage
   her, but I oversaw every project she touched"). Occasionally a bold hook
   replaces it ("If I had to pick one word...", "possibly the best hire I've
   made"), with the standing in the next sentence.
2. **Announce the count when there's more than one strength**, then walk them
   in order. The count varies (two, three, "a few"). Link paragraphs with
   transitions that pick up the last thought ("Relatedly,", "Speaking of
   customers,", "Of course, none of that works without..."), and save the
   strongest for last with "Most importantly" or "Finally".
3. **Each strength gets claim, evidence, then why it's rare.** The evidence is
   a specific project, situation, or turnaround, not an adjective. Raise the
   stakes before the result when the result sounds modest ("That may not sound
   like much, but..."), or describe how bad things were before they stepped
   in. Rarity framing is his usual third beat: "I've seen this in few
   engineers", "it's hard to teach", "uncommon in someone this early in their
   career".
4. **Contrast with a lesser version of the role** at most once: what a lesser
   PM, engineer, or leader would have done, and what they did instead.
5. **Credit candor paired with grace.** Speaking up under pressure, telling
   leadership the truth, pushing back on him (with a parenthetical admitting
   when he was the one who was wrong), always with tact or calm. It's his
   most-praised trait after technical breadth and customer focus.
6. **Implicate himself when it's true**: he couldn't match their skill, they
   changed his career, he's a better manager for it. Upward recommendations
   lean on gratitude for the chance they took on him.
7. **One human detail when he knows one**: a hobby, a kindness, an office
   rivalry. The best ones turn the detail into evidence (a newcomer who got
   good at a game fast is someone who learns anything fast) or into a
   joke-then-pivot close.
8. **Close aimed at the reader**: a conditional pitch ("If your team needs X
   who Y, call Z"), a plain "it was a pleasure", or both. "Would be an asset
   to any team" is his phrase but he's leaned on it heavily, so use it at most
   occasionally and prefer naming the kind of team.

Scale length and claims to what he actually saw. With light contact, say so
("we didn't overlap much, but when we did...") and keep it to two or three
short paragraphs; don't invent evidence. Roles get judged against their own
job ("that's the heart of the QA role, and he did it well").

Vocabulary that shows up here: "quick study", "technical chops", "a knack
for", "seeing around corners", "in spades", "with aplomb", "doggedly", "to a
fault", "sniff out", "a steady hand", "thankless behind-the-scenes work",
"put simply". When he's at a company with named values, he borrows their
language lightly. Technology lists go in parentheses ending "to name a few".

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

## Manager reviews (bullets)

- Write fragments, not sentences, usually two descriptive phrases joined by a
  comma.
- Tag the bullet with the org's value in bold after a spaced dash. If the
  strength is rare, say so in the bullet itself.
- Switch to direct address when it's warm, with a short plain compliment.
- Write growth items as imperatives, with an exclamation point sparingly. Give
  the habit to change, then the reason in a clause.
- In the manager-support section, write what *he* will do, as short action
  phrases (advocate, connect, clarify).

## Self-assessments

- Name the strength in bold inside the sentence, then give the evidence, with
  the biggest number or outcome last.
- Name the drawback in the same breath, in parentheses.
- Own failures specifically, with a cause and a commitment not to repeat it.
  The cause is usually something he held back on, not something done to him.
- Share credit and deflect with humor, one parenthetical at most. A quip about
  experience or about restraint is the usual register.
- State growth areas bluntly, in one short sentence.
- Asks of the manager are concrete and structural: mechanisms, introductions,
  budget autonomy, inclusion in decisions.

## Accomplishments, resume, and bio

When building or updating an accomplishments log (a brag document), capture
more than the what and where:

- **Who**: the people worked with, and how far outside the team they sat
  (peers, managers, directors, customers). It shows the level he operated at
  and who can vouch for the work.
- **When**: the timeframe, so the work can be placed next to everything else.
- **Why**: the difference it made. Metrics first, anecdotes when there's no
  number. Technical detail without impact doesn't count.
- **Artifacts and quotes**: links, screenshots, and stakeholder quotes
  (both good and bad), gathered at the time rather than reconstructed.

Order the log to fit its purpose: chronological for a linear career, by domain
to argue expertise, by impact to show value, or by the next-level role
guidelines for a promotion case. Keep two versions, a detailed internal one and
a personal one edited for confidentiality. The personal one feeds the resume.

- Put the action first and the number last, with the outcome downstream
  (delivery time, then adoption, then what the work led to).
- Calibrate attribution with "Led", "Contributor to", or "material
  contributor". Never inflate.
- Date-stamp metrics with "(as of MM/DD/YYYY)" and give a benchmark next to
  any score.
- Back a shortfall with its trend and the actions taken, listing the recent
  periods in order.
- Use spaced hyphens and parentheses, never em dashes.
- Bios open with his public tagline, "Technologist building systems and
  organizations that promote human flourishing", and can keep one wry personal
  line, such as "owner of every iteration of the Raspberry Pi" or "likes to
  write open-source software, play bass guitar, and run, though not all at
  the same time." Don't name or describe an employer unless he supplies one.

Invented example letter, recommendation, review, and log entries:
[examples.md](examples.md). Open it before drafting a full letter,
recommendation, or self-assessment.

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
