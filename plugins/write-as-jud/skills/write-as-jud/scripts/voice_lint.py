#!/usr/bin/env python3
"""Advisory prose linter for the write-as-jud skill.

Usage: voice_lint.py [--mode email|blog|proposal|agenda|estimate|feedback] FILE

FILE may be "-" for stdin. Every finding is a warning and the exit code is
always 0; this is a nudge, not a gate.
"""

import argparse
import re
import sys
from pathlib import Path

MODES = ("email", "blog", "proposal", "agenda", "estimate", "feedback")
CAP = 10
CEILING = {"email": 150, "blog": 700, "feedback": 600}
SKIP_NOT_X = {"agenda"}
SKIP_FRAMING = {"agenda", "estimate"}
UNCONTRACTED_MODES = {"email", "blog", "feedback"}

CODE_FENCE = re.compile(r"^(```|~~~).*?^\1[^\n]*$", re.DOTALL | re.MULTILINE)
INLINE_CODE = re.compile(r"`[^`\n]*`")
URL = re.compile(r"https?://\S+|www\.\S+")
EM_DASH = re.compile(r"—| -- ")
NOT_X_BUT_Y = re.compile(
    r"\bnot (?:just|only|merely|simply) [^.!?;\n]{1,60}?\bbut\b"
    r"|\bnot because [^.!?;\n]{1,60}?\bbut because\b"
    r"|\b(?:it|this|that)(?:'s| is) not [^.!?;\n]{1,40}?[,;] (?:it's|it is|but)\b"
    r"|\b(?:isn't|wasn't|aren't) [^.!?;\n]{1,40}?[,;] (?:it's|it is|it was)\b",
    re.IGNORECASE,
)
UNCONTRACTED = re.compile(
    r"\b(?:it is|that is|there is|do not|does not|did not|is not|are not|was not"
    r"|would not|should not|could not|will not|cannot|I am|I will|I have|I would"
    r"|we are|we will|you are|you will|they are)\b",
    re.IGNORECASE,
)
ASIDE = re.compile(r"\([^()]*[a-z][^()]*\)")
OPENER = re.compile(
    r"^(?:so,|let's|let me|great question|i hope this|i wanted to reach out"
    r"|just following up)",
    re.IGNORECASE,
)
CLOSER = re.compile(
    r"^(?:in summary|in conclusion|to sum up|overall,|let me know if you'd like"
    r"|would you like me to|feel free to reach out|don't hesitate)",
    re.IGNORECASE,
)


def load_tells(path: Path) -> list[tuple[re.Pattern[str], str]]:
    tells = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        phrase, _, hint = (part.strip() for part in line.partition("|"))
        pattern = re.compile(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", re.IGNORECASE)
        tells.append((pattern, hint))
    return tells


def clean(text: str) -> str:
    """Blank out code and URLs, preserving newlines so line numbers hold."""

    def blank(m: re.Match[str]) -> str:
        return re.sub(r"[^\n]", " ", m.group())

    for pattern in (CODE_FENCE, INLINE_CODE, URL):
        text = pattern.sub(blank, text)
    return text


def excerpt(text: str, start: int, end: int) -> str:
    lo, hi = max(0, start - 20), min(len(text), end + 20)
    return " ".join(text[lo:hi].split())


def lint(
    text: str, mode: str, tells: list[tuple[re.Pattern[str], str]]
) -> tuple[list[str], int]:
    findings: dict[str, list[str]] = {}

    def add(check: str, pos: int, msg: str, snippet: str = "") -> None:
        line = text.count("\n", 0, pos) + 1
        tail = f': "{snippet}"' if snippet else ""
        findings.setdefault(check, []).append(f"{line}: [{check}] {msg}{tail}")

    for m in EM_DASH.finditer(text):
        add(
            "em-dash", m.start(), "use a comma or parentheses", excerpt(text, *m.span())
        )
    for pattern, hint in tells:
        for m in pattern.finditer(text):
            msg = "avoid" + (f" (try: {hint})" if hint else "")
            add("tell", m.start(), msg, m.group())
    if mode not in SKIP_NOT_X:
        for m in NOT_X_BUT_Y.finditer(text):
            add("not-x-but-y", m.start(), "contrast framing", m.group())
    if mode in UNCONTRACTED_MODES:
        hits = list(UNCONTRACTED.finditer(text))
        for m in hits[:3]:
            add("uncontracted", m.start(), f"{len(hits)} uncontracted total", m.group())
    words = len(text.split())
    if mode in CEILING and words > CEILING[mode]:
        note = " (fine if it's a guide)" if mode == "blog" else ""
        add("length", 0, f"{words} words, soft ceiling {CEILING[mode]}{note}")
    if (mode == "blog" or (mode == "email" and words > 60)) and not ASIDE.search(text):
        add("no-aside", 0, "no parenthetical aside")
    if mode not in SKIP_FRAMING:
        first = re.search(r"\S", text)
        if first and OPENER.match(text[first.start() :]):
            add(
                "opener",
                first.start(),
                "throat-clearing opener",
                text[first.start() :][:40].split("\n")[0],
            )
        paras = list(re.finditer(r"\S[^\n]*(?:\n[^\n\S]*\S[^\n]*)*", text))
        if paras and CLOSER.match(paras[-1].group()):
            add(
                "closer",
                paras[-1].start(),
                "summary or unsolicited offer",
                paras[-1].group()[:50],
            )

    out = []
    for check, lines in findings.items():
        out.extend(lines[:CAP])
        if len(lines) > CAP:
            out.append(f"[{check}] +{len(lines) - CAP} more")
    return out, sum(len(lines) for lines in findings.values())


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Advisory voice linter (always exits 0)."
    )
    parser.add_argument("--mode", choices=MODES, default="blog")
    parser.add_argument("file", metavar="FILE", help='path, or "-" for stdin')
    args = parser.parse_args()
    raw = (
        sys.stdin.read()
        if args.file == "-"
        else Path(args.file).read_text(encoding="utf-8")
    )
    tells = load_tells(Path(__file__).with_name("tells.txt"))
    results, total = lint(clean(raw), args.mode, tells)
    for line in results:
        print(line)
    print(f"{total} warning(s) in {args.mode} mode")


if __name__ == "__main__":
    main()
