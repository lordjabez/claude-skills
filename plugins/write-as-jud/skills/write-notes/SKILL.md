---
name: write-notes
description: >-
  Writes working documents in Jud's voice: meeting notes, to-do lists, daily
  scratchpads, brainstorms and outlines, question lists for vendor or partner
  meetings, speaker notes and talk tracks, interview guides and screening
  agendas, 1-on-1 agendas and question banks, checklists, and training or workshop designs. Use whenever he asks
  to take, clean up, structure, or draft notes, an agenda, a list of questions,
  talking points, an interview script, a 30/60/90 plan, or an outline, or
  pastes a transcript or messy notes to turn into his style, even when the
  word "notes" never appears. Not for polished prose (use write-as-jud) or
  finished proposals (use write-proposal).
allowed-tools: Bash(${CLAUDE_SKILL_DIR}/../write-as-jud/scripts/voice_lint.py *)
---

# Write Notes

This builds on the core voice in the `write-as-jud` skill
([../write-as-jud/SKILL.md](../write-as-jud/SKILL.md)). Read that first if it
isn't already loaded. This file covers only what changes, and wins where the
two differ.

Derived from about 27k words of notebook pages (daily scratchpads, ~30 dated
meeting notes, brainstorms, estimates, talk tracks), plus slide bullets, speaker
notes, interview guides, screening agendas, and a training program design.
Pasted articles, client wish lists, and borrowed question banks in the notebook
were excluded.

Notes are written for one reader: himself, or a teammate who was in the room.
They're compressed, but never cryptic to that reader.

## Pick the form

| Form | Shape |
| --- | --- |
| Meeting notes | `YYYY-MM-DD Topic` title, attendees line, then flat fragment lines |
| Scratchpad or to-do | Loose noun-phrase headers, imperative bullets nested 1-4 levels |
| Brainstorm | Questions and options, escalating ("Small version... / BIGGER version:") |
| Questions for a meeting | Grouped under short headers, each a direct question in his voice |
| Speaker notes | Sentence fragments with stage directions to himself in parentheses |
| Interview guide or agenda | Timeboxed sections, a warm scripted opener, follow-up probes |
| 1-on-1 agenda or question bank | Four to seven short agenda lines, questions grouped by purpose |
| Checklist or plan | A bold role or phase header, imperative lines, " - DONE" suffixes as items close |
| Training or process design | Roles, prework, rules, then phases with lettered steps |

## Line-level style

- **Fragments.** Drop the articles and drop the verbs wherever meaning
  survives: "Plots rented by season, flat fee for each size tier".
  Lines rarely end in periods.
- **Questions stay questions.** About 8% of lines end in "?", and 30-60% on
  pages prepared for a meeting. Open decisions sit as sibling questions:
  "Print now? / Print on approval?"
- **Uncertainty is marked inline**: "(maybe?)", "(sp?)", "TBD", "??", or a
  trailing "…". Price guesses get doubled marks: "Budget \$2K-\$3K ??"
- **His own opinion goes inline**, flagged: "Not sure about this given...",
  "Smart plugs - cute, but what problem do they solve here?"
- **Separators**: a spaced hyphen " - " is the main joiner (owner - action,
  term - definition, label - detail). Use "->" for flows ("Photos -> NAS ->
  backup bucket"), slashes for alternatives
  ("Hub/Gateway/Bridge"), and "X = definition" for glossary lines.
  No em dashes.
- **Shorthand**: "mtg", "convo", "esp", "e.g." (heavily), "NLT", "x" for
  multiplication, "vs". Acronyms go unexpanded.
- **Emphasis** is ALL CAPS for reminders to himself ("MERGE WITH VENUE QUOTE +
  HEADCOUNT"), or `*** text ***` for the key takeaway of a session.
- **Parentheses** show up on about one line in eight, for asides and scope:
  "(and the router swap too? And the printer?)"

## Action and ownership markers

- `Name - verb phrase` for owned actions: "Me - Check the storage
  line item"
- `Ask from Name:` for requests made of him, and `Question for Name:` for
  questions he's holding for someone
- `Action:` / `NEXT STEP:` for the takeaway
- " - DONE" appended when closed, rather than deleting or striking through

## Meeting notes

1. Title the page `YYYY-MM-DD Topic`. Check the date with `date`, never assume
   it.
2. Attendees on one line, or as `Name - role` lines for a new group.
3. Write facts as heard, in order, one per line. Short quoted phrases are other
   people's words, so keep them in quotes: `"the green sheet"`.
4. Mix questions he asked (with answers after "?") into the flow: "Can plots be
   shared? Yes, but they're flagged by plot and season."
5. Flag cross-project patterns inline: "(same issue came up in the other mtg)".
6. End with any asks and actions. No summary.

When cleaning up a transcript, compress hard: one line per fact, fragments,
questions kept as questions. Resist turning notes into prose.

## Speaker notes and talk tracks

- Write a full-sentence opening, then switch to bullets. The opening is his
  name and personal tagline ("I'm Jud, a technologist building systems and
  organizations that promote human flourishing"), then why he's there. Never
  describe his employer.
- Bullets are reminders, not a script. They include stage directions: "(tell
  story of the 2am printer driver bug)", "(keep the acronyms out of this part)".
- Talk tracks for hard conversations (performance, terminations, role changes,
  escalations) belong to the `write-feedback` skill, which has a dedicated
  guide for them.

## Interview guides and agendas

- Timebox every section in the header: "Tech Discussion (15-20 minutes)".
- Open with a warm, self-aware script that lowers the stakes: "I'll be typing as
  we go, so if I glance away it's not boredom, just trying to keep up. No secret
  grocery lists, I swear!"
- Questions use "Tell me about a time...", each followed by a probe ladder:
  what you built and for whom, your specific role, challenges, what you learned,
  and what you'd do differently. He wants what the candidate *did*, not what
  they would do.
- Put the follow-up guidance in italics at the top: "*Follow-ups: Look for
  concrete actions...*"
- Keep a set of all-purpose follow-ups that work at any lull: "What else?",
  "Tell me more.", "How did it work out?", "What did you learn?", "How would
  you do things differently next time?". "What else?" beats "Is there anything
  else?" because it assumes there's more to say.
- Budget about 10 minutes per story, and note the pause: wait a full 8 seconds
  before moving on so the candidate is really done.
- Ask about results if the candidate doesn't offer them. In STAR, weight runs
  left to right, so Result matters most.
- To gauge a story's level, ask who they were talking to at the time: peers,
  managers, directors, customers, vendors.

## 1-on-1 agendas and question banks

- Agendas are four to seven short lines, starting with a personal check-in and
  ending with something open: "Open discussion (you pick the topic)" or
  "Create and review action items".
- Status updates come last or not at all. He has other ways to track project
  health and wants the time for development, goals, and blockers.
- The report owns the agenda. Write it that way: "Take the lead in setting an
  agenda".
- Group question banks by purpose under a one-line lead-in: learning how
  someone wants to be managed, making work more enjoyable, career growth, and
  feedback on him as a manager. Every question is short and open-ended.

## Training and process designs

- Define roles first, with constraints in parentheses: "Facilitator (cannot be
  on either Crew or Client teams)".
- Number the phases and letter the steps, each step starting with the actor:
  "Crew schedule and lead the kickoff session."
- Mark which steps are flexible: "(can be async)".
- End with a fill-in template whose hints are in parentheses: "Expected
  Outcomes: (list deliverables here, but focus on what changes for the user)".

Invented examples of each form: [examples.md](examples.md). Open it when
the form is unfamiliar or the draft is drifting toward prose.

## Check the draft

Run the linter on the draft first, and fix the findings that are real
tells:

```bash
${CLAUDE_SKILL_DIR}/../write-as-jud/scripts/voice_lint.py --mode notes FILE
```

Then:

1. Could any line lose more words? Notes should be terser than feels polite.
2. Are open questions still marked as questions, not resolved by guessing?
3. Does every action have an owner?
4. Did any em dash, summary paragraph, or "Key takeaways:" header sneak in?
