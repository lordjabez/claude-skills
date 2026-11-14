---
name: write-agenda
description: >-
  Writes interview guides and 1-on-1 agendas in Jud's voice: candidate
  interview scripts, screening-call agendas, behavioral "tell me about a time"
  questions with follow-up probes, recurring 1-on-1 agendas, first-1-on-1
  questions, and question banks for getting to know a direct report or
  gathering feedback on him as a manager. Use whenever he asks to prep, draft,
  or tighten an interview, a phone screen, a 1-on-1, or the questions to ask a
  candidate or a report, even if the word "agenda" never appears. Not for
  meeting, board, workshop, or event agendas, meeting notes, or talk tracks
  for hard conversations (use write-feedback).
allowed-tools: Bash(${CLAUDE_SKILL_DIR}/../write-as-jud/scripts/voice_lint.py *)
---

# Write Agenda

This builds on the core voice in the `write-as-jud` skill
([../write-as-jud/SKILL.md](../write-as-jud/SKILL.md)). Read that first if it
isn't already loaded. This file covers only what changes, and wins where the
two differ.

Derived from interview guides, screening agendas, 1-on-1 agendas, and question
banks in his notebook. Every example in this skill is invented.

Both forms are conversations he leads where the other person should do most
of the talking. Agenda lines are short fragments, questions are short and
open-ended, and a spaced hyphen " - " joins a label to its detail.

## Pick the form

| Form | Shape |
| --- | --- |
| Interview guide or screening agenda | Timeboxed sections, a warm scripted opener, follow-up probes |
| 1-on-1 agenda or question bank | Four to seven short agenda lines, questions grouped by purpose |

## Interview guides and screening agendas

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

Invented examples of an interview opener, a screening agenda, and a 1-on-1
agenda with question banks: [examples.md](examples.md). Open it before
drafting a full guide or agenda.

## Check the draft

Run the linter on the draft first, and fix the findings that are real
tells:

```bash
${CLAUDE_SKILL_DIR}/../write-as-jud/scripts/voice_lint.py --mode agenda FILE
```

Then:

1. Is every interview section timeboxed?
2. Does every interview question have probes after it, aimed at what the
   candidate *did*?
3. Does a 1-on-1 agenda leave the report room to steer, with status last or
   absent?
4. Could any line lose more words?
