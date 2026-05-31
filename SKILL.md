---
name: power-html
description: Build, revise, and QA PowerPoint-like presentations as fully self-contained HTML files with embedded CSS, JavaScript, images, and keyboard slide navigation. Use when Codex needs to create an HTML presentation deck instead of PPTX/PDF, convert a slide narrative into an interactive browser-based deck, embed all assets into one portable file, implement PowerPoint-style controls, or apply presentation best practices with optional project-specific customization from `.power-html/power-html.md`.
---

# Power HTML

Create self-contained HTML presentation decks that feel like PowerPoint while using the flexibility of the web. Prioritize the user's prompt over every default, then apply the baseline and only the conditional references that match the context.

## Core Workflow

1. Read the user request, source material, and assets.
2. Check for a customization file at `.power-html/power-html.md` in the current project directory. If present, read it before designing.
3. Load `references/baseline/` files that are relevant to all decks:
   - `baseline-principles.md`
   - `html-deck-requirements.md`
   - `qa-checklist.md`
4. Choose conditional references from `references/conditional/` based on the task. Do not bulk-load all references.
5. Build one self-contained `.html` file with inline CSS and JS. Embed local images/assets as data URLs when portability matters.
6. Include keyboard navigation: right/down/space/page-down advance; left/up/page-up go back; Home/End jump; optional `#N` hash jumps.
7. QA with a headless browser screenshot when available. At minimum, check slide count, embedded assets, keyboard handler, and no obvious overflow.

## Customization Convention

Look for this optional file:

```text
.power-html/power-html.md
```

Use it for project-specific prompts, brand rules, audience notes, typography, color palettes, forbidden patterns, preferred slide count, language, assets, presenter style, and QA criteria. Treat it as high-priority context below the direct user request. If it conflicts with the current user request, the current user request wins.

Recommended sections:

```markdown
# Power HTML Customization

## Audience
## Narrative / Intent
## Visual Style
## Brand Assets
## Required Slides
## Forbidden Patterns
## Presenter Notes
## QA Requirements
```

## Design Contract

- One slide, one job, one dominant read.
- Make slides memorable for live delivery. Put speaker detail in the presenter narrative, not on the slide.
- Use a coherent visual system: shared margins, type scale, colors, logo treatment, navigation behavior, and repeated motif.
- Use open composition before boxes. Cards and panels are for comparisons, artifacts, dashboards, or repeated items.
- Make headings specific and useful. Prefer a claim or a clean section marker over vague labels.
- Respect user-requested style even when it differs from the defaults.
- Default to the user's requested language.

## Conditional Reference Selection

Read only the files that match the deck:

- Strategy, executive, MBB-style business, operating model: `conditional/strategy-executive.md`
- Technical, engineering, security, open-source, developer tools: `conditional/technical-security.md`
- Data, investor, KPI, market, metrics-heavy: `conditional/data-investor.md`
- Product demo, launch, roadmap, product marketing: `conditional/product-demo.md`
- Fun, friends, social, informal, party, classroom-light: `conditional/playful-social.md`
- Training, workshop, enablement, hackathon: `conditional/workshop-hackathon.md`
- Very sparse keynote/live talk: `conditional/low-text-keynote.md`
- Dense leave-behind or documentation-style deck: `conditional/dense-leavebehind.md`

## Useful Scripts

- `scripts/scaffold_deck.py`: create a starter self-contained HTML deck with keyboard navigation, hash jumps, and embedded customization notes.
- `scripts/embed_assets.py`: convert local assets to data URL snippets for inline embedding.

Use scripts when they save time, but adapt the output to the user's requested design rather than treating the template as a fixed style.

## Template Asset

`assets/template/deck-template.html` contains a minimal navigation and slide structure. Copy or adapt it when a deck does not already exist.

## Validation

Before final response:

- Confirm the output HTML exists and is non-empty.
- Confirm expected slide count.
- Confirm CSS and JS are inline.
- Confirm image assets are embedded or intentionally referenced.
- Confirm keyboard navigation and hash jumps are present.
- Render at least one representative screenshot when a headless browser is available.
- Mention any screenshots or limitations in the final answer.

## Rationale

This skill uses progressive disclosure because presentation advice is context-sensitive. Baseline references cover rules that are nearly always useful. Conditional references cover audience and deck-type patterns such as MBB strategy, technical/security, workshops, or playful decks. The point is not to force a consulting template onto every deck; it is to retrieve the right guidance only when it matches the user's intent.
