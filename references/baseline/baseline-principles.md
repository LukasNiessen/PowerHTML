# Baseline Principles

Use these for every Power HTML deck unless the user asks otherwise.

## Narrative

- Decide the audience shift: what should viewers believe, feel, decide, or do after the deck?
- Build a slide sequence, not a pile of pages.
- Draft the storyline as a bare list of slide titles before designing anything. The title list is the
  storyline. **Show that list to the user and get it signed off before building slides** — wording is where
  taste lives, and it usually takes a few rounds. Rewriting a list is cheap; rewriting a deck is not.
- Identify the three to five **load-bearing slides** up front and plan to spend real depth on them, keeping
  the rest lean. See `depth-and-density.md`.
- **Ask how the deck will be consumed** — presented live, sent as a file with no presenter, or both. A deck
  that will be forwarded has to carry its own detail.
- Check that the slide *order* does not presuppose a conclusion you have not earned. Sequence is an argument
  even when the wording is neutral.
- Use section slides to reset attention.
- Put live-talk detail in what the presenter says, not on screen — unless there will be no presenter.
- Cut closing platitudes. End on the concrete thing you want the reader to do.

## Slide Discipline

- One slide, one job.
- One dominant object: headline, image, number, chart, table, diagram, quote, or question.
- Prefer fewer, stronger words — on supporting slides. On load-bearing slides, prefer *sufficient* words.
- If the presenter will explain it verbally, keep the slide as a prompt.
- If a slide needs more than 5 bullets, split it. **When a slide is too dense, split it — never compress it.**
  Slide count is cheap; a crammed slide and a gutted argument are not.

## Communication Patterns

- Use top-down communication: answer first, then support.
- Use Minto-style grouping: mutually exclusive, collectively useful groups where possible.
- Make lists parallel: same grammar, same level of abstraction.
- **Headline every content slide with an MBB-style action title: a full declarative sentence stating the conclusion, not the topic.** Read the titles in sequence and confirm they tell the whole story alone. Full rules, tests, and examples: `action-titles.md`.
- Use simple, memorable, repeatable phrasing for live decks — in the body and in the presenter narrative, not as a substitute for an argued title.

## Visual System

- Establish a small type scale and reuse it.
- Align to a consistent safe area.
- **Pin the slide title to a fixed offset from the top on every slide.** Titles that move vertically between
  slides read as a web page rather than a deck. Body content flows down from the title; trailing empty space
  at the bottom is normal and fine.
- Repeat a motif deliberately: accent bar, watermark, logo rail, section marker, icon style, or layout rhythm.
- **One accent colour, used sparingly.** A dark deck with white text and a single accent reads as more
  authoritative than one with four semantic hues. Resist colour-coding categories (shipped/planned,
  pass/fail, per-language) unless the distinction is the point of the slide — weight, border and position
  carry it just as well and stay quiet. Reach for a second hue only when a slide genuinely encodes two
  independent dimensions.
- Keep contrast high.
- Avoid random decorative shapes, and avoid gradients with more than two stops.
- Use real subject images or meaningful icons.
- **Avoid `text-transform: uppercase` on running content** — body text, list items, exec-summary row labels,
  card headings. It hurts legibility, breaks code and product names, and makes a deck feel like a template.
  Small size and weight already signal a label. Uppercase *is* right for short chrome that must read as a
  stamp rather than prose: status badges ("ILLUSTRATIVE", "DRAFT", "CONFIDENTIAL") and code-panel captions.
  There, add generous letter-spacing (~0.15–0.2em) so it reads as a mark, not shouting.
- **Watch minimum body size.** Secondary and tertiary text is where decks go unreadable: sub-lines under a
  list item, card body copy, timeline captions. Anything a reader is expected to actually read should hold up
  when projected — if you find yourself below roughly 1.2vw for supporting copy, cut words instead of type.
- Keep persistent chrome (page number, watermark, progress bar) quiet but legible — roughly 25–35% opacity.
  Remove it entirely when asked; do not compensate by making it near-invisible.

## HTML Deck Behavior

- Full-viewport slides.
- Instant keyboard navigation, not smooth scroll, for a presentation feel.
- Hash jumps (`#3`) for rehearsal and QA.
- Keep all CSS and JS inline when the user asks for one file.
- Embed images as data URLs when portability matters.
