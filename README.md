# Power HTML

Power HTML is a Codex skill for building PowerPoint-like presentations as self-contained HTML files. The core idea is to keep the delivery experience of a slide deck while using the flexibility of HTML/CSS/JS: richer layouts, embedded assets, easier iteration, and deterministic keyboard navigation.

## Design Rationale

The skill is structured around progressive disclosure:

- `SKILL.md` contains the workflow, trigger guidance, customization convention, and validation checklist.
- `references/baseline/` contains guidance that applies to nearly every deck.
- `references/conditional/` contains context-specific guidance that should be loaded only when the deck intent matches.
- `scripts/` contains small deterministic helpers for scaffolding decks and embedding local assets.
- `assets/template/` contains a minimal HTML deck template.

This split avoids loading every best-practice document for every presentation. A strategy deck should pull in strategy/executive guidance; a hackathon deck should pull in workshop guidance; a playful friends deck should not accidentally become an MBB-style strategy deck.

## Customization File

Projects can provide local instructions at:

```text
.power-html/power-html.md
```

Use that file for project-specific brand rules, prompt fragments, audience context, visual style, required slides, forbidden patterns, and QA rules. The current user request still wins over the customization file.

## Reference Packs

Baseline references:

- `baseline-principles.md`
- `html-deck-requirements.md`
- `qa-checklist.md`

Conditional references:

- `strategy-executive.md`
- `technical-security.md`
- `data-investor.md`
- `product-demo.md`
- `playful-social.md`
- `workshop-hackathon.md`
- `low-text-keynote.md`
- `dense-leavebehind.md`

The conditional packs intentionally blend well-known presentation practices such as top-down communication, Minto-style pyramid logic, MBB-style answer-first synthesis, live-talk text economy, and technical/open-source presentation patterns. They are defaults, not constraints: user intent and direct instructions override them.
