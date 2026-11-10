---
name: style-of-the-faith
description: >-
  The visual identity ("Style of the Faith") of the Church of the Incandescent
  Filaments: its named color palette, Libre Franklin and EB Garamond
  typography, and semantic color roles. Load it before producing anything that
  should look like the faith, in any format (deck, document, PDF, web page,
  artifact, chart, image), and whenever another skill that creates such output
  is working on church material. Use it even when the user only mentions
  filaments, the prophet, or the Five Filaments, or says "make it look like the
  faith", and when asked which colors or fonts the church uses.
user-invocable: false
---

# Style of the Faith

The canonical design tokens for the Church of the Incandescent Filaments. Other
skills own the output format and the layout; this skill owns the colors and
fonts. Take values from here rather than restating them in the calling skill,
so a change happens in one place.

The source of truth is the workbook `Style of the Faith.xlsx` in the
`incandescent-church` project. If it changes, update [palette.md](palette.md)
and [tokens.css](tokens.css) together.

## Typefaces

| Role | Face | Use for |
| --- | --- | --- |
| Primary | Libre Franklin | Body text and nearly everything else: paragraphs, lists, tables, labels, captions, UI, numbers |
| Accent | EB Garamond | Headings and titles, and the occasional word or phrase that needs emphasis |

Franklin does the work; Garamond is the accent and should be used sparingly. A
page that is mostly Garamond has inverted the system. Both are on Google Fonts;
fallback stacks and the loading link are in [tokens.css](tokens.css).

## Color roles

Use roles first and reach into the full palette only for accents and data.

| Role | Swatch | Hex |
| --- | --- | --- |
| Page / background | Parchment Crease | `#F4EFE6` |
| Raised surface, cards | Antiquities Alabaster | `#FFFEFA` |
| Body text | Mr. Tux Black | `#1F1F1F` |
| Secondary text, captions | Lamplighters' Charcoal | `#4A4A4A` |
| Rules, hairlines, borders | Threshold Cobblestone | `#808285` |
| Signature accent (fills, highlights) | Filament Amber | `#FEC500` |
| Accent text on light | Library Oak | `#644C31` |
| Strong emphasis, warnings | Speakeasy Crimson | `#8E0A26` |
| Dark ground | Longest Night | `#003271` |
| Text on dark ground | Warm White Light | `#FFF5D1` |
| Accent on dark ground | Filament Amber | `#FEC500` |

The role assignments are defaults, not dogma; any swatch in
[palette.md](palette.md) is in the faith. The constraints that matter:

- Filament Amber is light, not ink. It fails contrast as text on paper (1.4:1),
  so use it for fills and highlights on light grounds, and as text only on
  Longest Night or Mr. Tux Black.
- Text colors must reach 4.5:1 against their ground. [palette.md](palette.md)
  lists which swatches pass on paper and on Longest Night.

## What to open next

- Every swatch by family and shade, contrast ratios, and chart series order:
  [palette.md](palette.md)
- CSS custom properties for every swatch and role, font stacks, and the Google
  Fonts link, for any HTML or WeasyPrint output: [tokens.css](tokens.css)

## Using it from another skill

A calling skill should say "load `style-of-the-faith`" and then apply its tokens
in whatever format it produces. For HTML or WeasyPrint, link or inline
`tokens.css` and use the `var(--…)` names. For python-pptx, docx, or
matplotlib, read hex values from `palette.md` and set the font names exactly
as written above. Office formats do not embed web fonts by default, so tell
the user that Libre Franklin and EB Garamond must be installed on any machine
that opens the file, or embed them if the library supports it.
