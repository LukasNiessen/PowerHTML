# Power HTML

**HTML is the new PowerPoint.**

Power HTML is a Codex skill for creating PowerPoint-like presentations as one self-contained HTML file. You keep the deck experience: full-screen slides, keyboard navigation, strong visual rhythm. You gain the web: better layouts, richer styling, embedded assets, fast iteration, and no PPTX rendering drama.

## Why Power HTML

- **One file.** CSS, JavaScript, and assets can be embedded into a portable `.html` deck.
- **Feels like slides.** Arrow keys, space, page up/down, home/end, and hash jumps give it a PowerPoint-like flow.
- **More expressive.** HTML/CSS/JS can do layouts, motion, media, and interactions that are painful in PowerPoint.
- **Presentation-native.** The skill applies consulting-style slide craft: answer-first, one clear job per slide, consistent visual system, and low text density when the speaker will carry the story.
- **Customizable by default.** User instructions always win. Project-specific guidance can be added through a local markdown file.

## Quick Install

### Codex App / Local Skills

Clone this repository into your local agent skills folder:

```powershell
git clone git@github.com:LukasNiessen/PowerHTML.git "$env:USERPROFILE\.agents\skills\power-html"
```

Then restart Codex or open a new Codex session so the skill list is refreshed.

### Project-Local Usage

If you want a repository to carry its own copy of the skill:

```powershell
git clone git@github.com:LukasNiessen/PowerHTML.git .power-html-skill
```

Then add this to the repo's `AGENTS.md`:

```markdown
## Power HTML

When creating or editing HTML presentation decks, follow `.power-html-skill/SKILL.md`.
Load baseline references first, then only the conditional references that match the deck type.
```

## Use It

Ask naturally:

```text
Create a self-contained HTML kickoff deck from these notes.
```

```text
Turn this strategy memo into a browser presentation with arrow-key slide navigation.
```

```text
Make the deck feel like a modern black Cursor/xAI-style product presentation.
```

## Customization File

For project-specific rules, create:

```text
.power-html/power-html.md
```

Use it for:

- audience and language
- brand rules and assets
- visual style
- required sections or slide types
- forbidden patterns
- reusable prompt fragments
- QA requirements

The active user request always overrides this file.

## How It Works

Power HTML uses progressive disclosure:

- `SKILL.md` contains the core workflow and trigger rules.
- `references/baseline/` contains guidance that applies to nearly every deck.
- `references/conditional/` contains context-specific guidance, loaded only when relevant.
- `assets/template/` contains a minimal HTML slide template.
- `scripts/` contains helper scripts for scaffolding decks and embedding local assets.

This keeps the skill lean. A board strategy deck can pull in MBB-style, Minto-style, top-down communication guidance. A hackathon deck can pull in workshop guidance. A playful friends deck does not accidentally become a consulting deck.

### What it is opinionated about

Two things carry most of the quality, and both live in `references/baseline/`:

- **Action titles** (`action-titles.md`) — every content slide is headlined by the conclusion it proves, not
  its topic. Read the titles alone and they are the whole argument. Write that list first, get it signed off,
  then build slides.
- **Depth as a budget** (`depth-and-density.md`) — decks are not uniformly sparse. Three to five slides carry
  the argument and deserve real density; the rest need one idea each. When a slide gets too full, split it
  rather than compress it.

## Repository Layout

| Path | Purpose |
| --- | --- |
| `SKILL.md` | Core workflow for building and QA'ing HTML decks |
| `agents/openai.yaml` | Codex UI metadata |
| `assets/template/deck-template.html` | Starter self-contained HTML deck |
| `scripts/scaffold_deck.py` | Creates a starter deck from a title and slide list |
| `scripts/embed_assets.py` | Converts local files into data URLs for embedding |
| `references/baseline/` | Always-relevant slide and HTML deck principles |
| `references/conditional/` | Deck-type-specific guidance loaded only when useful |

## Design Philosophy

Start with the user's intent. Then make it sharp.

Slides should be simple, memorable, and useful. The headline should carry the point. The layout should guide the eye. The deck should feel coherent from first slide to last. And when PowerPoint gets in the way, HTML should get out of the way.
