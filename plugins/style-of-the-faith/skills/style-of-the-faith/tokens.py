"""Read tokens.css for scripts that build Office files (Word, PowerPoint, Excel).

A builder takes the path to this skill's tokens.css and imports this module from
the same directory, so the parser always matches the file it reads:

    sys.dont_write_bytecode = True  # keep __pycache__ out of the installed skill
    sys.path.insert(0, str(Path(tokens_css).resolve().parent))
    from tokens import load

    tok = load(tokens_css, "build_docx")
    tok("vestment-navy")  # "335384"
    tok("font-body")      # "Libre Franklin"

Standard library only.
"""

import re
import sys
from collections.abc import Callable
from pathlib import Path


def parse(path: str | Path) -> dict[str, str]:
    """Every CSS custom property in the file, with var() references resolved."""
    css = re.sub(
        r"/\*.*?\*/", "", Path(path).read_text(encoding="utf-8"), flags=re.DOTALL
    )
    raw = {k: v.strip() for k, v in re.findall(r"--([\w-]+)\s*:\s*([^;]+);", css)}

    def resolve(v: str) -> str:
        m = re.fullmatch(r"var\(--([\w-]+)\)", v)
        return resolve(raw[m.group(1)]) if m else v

    return {k: resolve(v) for k, v in raw.items()}


def load(path: str | Path, prog: str) -> Callable[[str], str]:
    """A lookup for Office formats: RRGGBB for a color, the first family for a font stack.

    A missing token exits naming the calling script, since a builder must never
    fall back to a color or font of its own.
    """
    values = parse(path)

    def tok(name: str) -> str:
        if name not in values:
            sys.exit(f"{prog}: token --{name} is missing from {path}")
        v = values[name]
        return (
            v.lstrip("#").upper()
            if v.startswith("#")
            else v.split(",")[0].strip("\"' ")
        )

    return tok
