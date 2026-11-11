---
name: write-proposal
description: >-
  Writes formal technical and proposal content in Jud's voice: architecture
  narratives for RFP, RFI, and ITN responses, proposal sections, statements of
  work, scope and deliverables, ROI and cost justifications, concept papers,
  technical explainers, "future opportunities" sections, and answers to
  security or vendor questionnaires. Use whenever he asks to draft, respond to,
  or tighten anything going to a government buyer, funder, procurement office,
  or partner, even when he never says "proposal" (e.g. "write up the
  architecture section", "answer these security questions", "make the case
  for phase 2"). Not for internal estimates and pricing math, which have their
  own skill, and not for blog posts or email.
allowed-tools: Bash(${CLAUDE_SKILL_DIR}/../write-as-jud/scripts/voice_lint.py *)
---

# Write Proposal

This builds on the core voice in the `write-as-jud` skill
([../write-as-jud/SKILL.md](../write-as-jud/SKILL.md)). Read that first if it
isn't already loaded. This file covers only what changes, and wins where the
two differ.

Derived from a body of buyer-facing and partner-facing writing: architecture
sections of solicitation responses, phased scope documents, SOWs, ROI
arguments, concept papers, and security questionnaire answers. This file
captures the approach and patterns. The examples in examples.md are invented.

## How the voice changes in this register

The core voice (brevity, leading with the point, plain ownership of tradeoffs)
holds. What changes:

| Trait | Blog and email | Here |
| --- | --- | --- |
| Person | "I", contractions | Impersonal or passive ("the recommendation is to", "it is anticipated"), the organization named in third person, "we" rarely and only when taking a position |
| Asides | Humor and confession | Parentheses survive, but they hold scope and examples |
| Titles | Allusive | Literal and descriptive |
| Cultural references | Frequent | None |
| Contractions | Always | Mostly dropped in buyer-facing text, kept in internal decks and partner-facing explainers |
| Humor | Seasoning | Gone for buyers. Internal technical decks keep one dry aside, usually a parenthetical about a tool or a tradeoff |

## Workflow

1. Find the requirement numbering in the solicitation and keep it open. Every
   claim that satisfies a requirement cites it inline, at the end of the
   sentence, by number.
2. Open with the frame: what this section covers and the approach as a whole,
   in two to four sentences. Then say plainly that the design is a starting
   point and will change in discovery. Reword the caveat each time; do not
   reuse a stock paragraph.
3. Give each subsection the same opening sentence pattern (what the components
   are, where they sit in the diagram, what they are responsible for), so a
   reader can jump in anywhere.
4. Recommend, don't list options. "X is recommended as the primary IAM
   solution." Then say why in terms of what the buyer already has or needs.
5. Write the tradeoff out when the recommendation departs from a stated
   requirement. Don't hide it (see the pattern below).
6. Push open details into discovery explicitly, rather than guessing, and
   always name the floor: what will be included at minimum.
7. Close a section when its content is done. No summary paragraph.

## Signature moves

- **Preserve the buyer's investment.** When something works, say so and keep
  it. Retain the proven core logic and repackage it in cloud-native services.
- **Pattern, then scale.** Don't promise everything. Propose a small
  representative sample that becomes a reusable pattern, document it, and let
  the buyer extend it.
- **Honest tradeoff, then a position, then an open door.** Name the requirement
  the choice departs from, give the reason it is still the right call, and
  invite a conversation in discovery.
- **Quote vendors, don't paraphrase them.** Product descriptions go in italics
  inside quotation marks, with a footnote to the official docs. His own prose
  carries the reasoning around the quote, which keeps marketing language
  attributed rather than adopted.
- **Show the arithmetic in ROI.** Give the inputs, the formula on one line,
  then the result as both a dollar figure and a percentage. Follow it with the
  conservative assumption and why the real number is likely better.
- **Phased scope as verb-first bullets.** "Build...", "Replace X with Y,
  integrating with Z", with sub-bullets for the specifics. List what existing
  work gets reused under its own heading.
- **Future-opportunity lists.** One framing paragraph that bounds the current
  scope, then 8-12 verb-first bullets, each specific enough to estimate.
- **Assumptions as numbered or bulleted facts with figures.** Volumes, user
  ratios, retention periods. When something is excluded, give the cost of
  including it: excluded, but possible at extra cost.

## Questionnaire answers

Only the answer column is his, so match the answers, not the questions.

- Lead with the direct answer, then name the specific tool or policy. One to
  three sentences.
- Admit gaps plainly, then give the compensating control.
- Use bullets only for multiple mechanisms, one per line.
- The failure mode is corporate boilerplate: "maintains a robust security
  posture", "a comprehensive approach ensures", "multi-layered defense
  strategy". If an answer reads like that, cut it back to the tool and the
  control.

## Diction

- Allowed and common: "leverage", "cloud-native", "managed service", "modular",
  "well-defined interfaces", "operational burden", "starting point".
- Hedges sound like an engineer, not a lawyer: "should be a small change",
  "can be explored during discovery", "though this would not be required".
- Avoid: "seamless" in his own prose (it only appears inside vendor quotes),
  "robust", "comprehensive", "empower", "cutting-edge", "best-in-class".
- Section labels in lists take a spaced hyphen or en dash. Sentences never take
  em dashes.

Before/after drafts and invented sample passages: [examples.md](examples.md).
Open it when drafting a full section, or when a draft feels generic and needs
calibrating.

## Check the draft

Run the linter on the draft first, and fix the findings that are real
tells:

```bash
${CLAUDE_SKILL_DIR}/../write-as-jud/scripts/voice_lint.py --mode proposal FILE
```

Then:

1. Does every requirement claim cite its number?
2. Is there a recommendation, or just a menu?
3. Is every departure from a requirement stated with its tradeoff?
4. Are unknowns pushed to discovery, each with a named floor?
5. Is any vendor marketing language unquoted? Quote it or cut it.
6. Did any boilerplate adjectives slip in?
7. Does the ROI arithmetic check out exactly?
