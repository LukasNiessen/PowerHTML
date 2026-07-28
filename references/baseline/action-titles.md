# Action Titles (Taglines)

Load this for every deck. It defines the default headline style: **MBB-style action titles.**

"MBB" means McKinsey, Bain, and BCG. The convention those firms share is that the headline of a slide is
not the slide's topic — it is the **conclusion the slide proves.** The body of the slide is evidence for the
headline. A reader who reads only the headlines, in order, gets the whole argument.

This is the default for every content slide. It is not a mandate: if the user asks for keynote-sparse
titles, single words, playful phrasing, or their own convention, follow the user.

## The rule

Every content slide carries exactly one action title: **a complete declarative sentence stating the slide's
conclusion.** Everything on the slide exists to support it.

## Two tests every deck must pass

**1. Read-through test (storyline).** Strip the deck down to its titles and read them in sequence. They must
form a coherent argument on their own — typically situation, complication, resolution — and someone who saw
only the titles should reach the same conclusion as someone who saw every slide. If the titles read like a
table of contents, they are labels, not action titles. Rewrite them.

**2. "So what" test.** Ask "so what?" of each title. If the title already answers it, the title is doing its
job. If the answer lives only in the body, in a footnote, or in the presenter's mouth, pull it up into the
title.

Write the titles first, as a list, and check both tests before designing a single slide. The title list *is*
the storyline.

## Rules for a single title

- Full sentence: subject + verb, indicative mood. Not a fragment. Not a label. Not a question.
- State the conclusion, not the subject matter.
- Be specific. Use the real number when the number is the point — **rounded.** Titles carry rounded figures
  ("200k monthly downloads"); the body carries the exact ones ("150k + 46k"). A precise number in a title
  reads as a claim about precision and dates the slide.
- Present tense, active voice. Name the actor when there is one.
- **Aim for 8–14 words on one line.** Two lines only when precision genuinely demands it. A title that needs
  two clauses and a semicolon is usually two titles, or a title plus a body row. Short and declarative beats
  complete and heavy: cut modifiers and hedges first, the "so what" last.
- Make it falsifiable. If no informed person could disagree with it, it says nothing.
- Let connectives carry the logic: *because, so, unless, which requires, but, drives, costs, means.*
- Be consistent about terminal punctuation across the deck (all periods, or none).

## Forbidden in an action title

- Label headings: "Market overview", "Q3 results", "Architecture options", "Next steps".
- Colon-label constructions: "Traction: strong growth".
- Teasers and cliffhangers: "What we found will surprise you".
- Rhetorical questions used as headlines.
- Slogans, puns, and wordplay in place of an argument.
- Vague intensifiers with no number behind them: "significant", "massive", "huge growth".
- **Counting an illustrative set.** If the list on the slide is examples, a first focus, or open-ended, never
  put its size in the title. "Eleven more languages" turns a non-exhaustive list into a commitment and
  invites "why isn't X on it?" Say "every language" or name the tier. Only count a set that is genuinely
  closed.
- Unexplained precision that will age badly: exact figures, live counts, or "as of today" numbers.

## Kicker + action title

A small category label above the title — a "kicker" — is the right home for the label the title must not be.
The kicker says where the reader is; the title makes the argument. Write them as a pair:

```text
Current standing | 200k monthly downloads show the demand; we need to support every programming language
```

The kicker is 1–4 words, repeats across the slides of a section, and never argues. This resolves the tension
between "no label headings" and the reader's need for orientation: the label lives in the kicker, which frees
the title to carry the conclusion. Most deck CSS already has a slot for this.

**Inline variant — one line, one element.** Instead of a separate kicker above, set the label and a divider
inside the title itself and bold everything up to and including the divider:

```html
<h2 class="tag"><b>Current standing</b><i>|</i>200k monthly downloads, growing rapidly</h2>
```

Rules for the inline form:

- Label bold, divider bold or light but visually quiet, the sentence in normal weight. Never colour the
  divider as an accent — it is punctuation, not emphasis.
- **One line, no manual `<br>`.** Size the type so the *longest* title in the deck fits the safe width at
  your target resolution, then cap every title at that length. Roughly: usable width in px ÷ (font-size ×
  0.47) ≈ the character budget. Shorten the title rather than shrinking the type below readable size.
- A navigational slide (contents, agenda) takes the bare label with no divider and no sentence.

**Pin the title to the top, centre the body in what's left.** In a PowerPoint-style deck the title sits at a
fixed offset from the top edge on every single slide, so it does not move as the reader advances. Vertically
centring the *whole* slide makes titles jump around and reads as a web page. But top-aligning everything
leaves the body clinging under the title with dead space beneath it. Do both:

```css
.slide { display:flex; flex-direction:column; justify-content:flex-start; padding-top:<fixed>; }
h2.tag  { flex:none; margin:0; }                              /* title pinned */
.body   { flex:1; min-height:0;                                /* body owns the rest */
          display:flex; flex-direction:column; justify-content:center;
          padding-top:<clear gap>; }
```

Wrap each slide's content in the `.body` element. The title lands identically on every slide, the content
sits optically centred in the remaining area, and there is a deliberate gap between them rather than a
crammed top and an empty bottom.

## Plain words beat consultant abstractions

Write the title the way you would say it out loud to a colleague. Abstract nouns feel precise on the page and
land as vague on the screen.

| Abstract (weak) | Plain (strong) |
|---|---|
| The demand is language-agnostic | We need to support every programming language |
| Each option trades install simplicity against guaranteed parity | We must decide what is shared and what stays language-specific |
| Where we cut the seam is the decision | We have to decide what lives in the shared core |
| Adoption velocity is inflecting | Downloads doubled in four months |

Prefer concrete verbs and named things. Say "we" when the deck is asking someone to act. If a title needs a
term of art, introduce it in the body, not the headline.

## Where a slogan IS allowed

The **cover slide**, **section dividers**, and the **closing statement** may carry a short memorable line
instead of an action title. A divider marks the start of an argument; it does not have to prove anything.
Everywhere else, the title argues.

## Patterns that work

| Pattern | Shape |
|---|---|
| Claim + reason | "X is Y, because Z" |
| Cost of the status quo | "Doing X today costs N; at scale it costs 10N" |
| Constrained choice | "Three options trade A against B, and none dominates" |
| Consequence / deadline | "Unless we decide X by <date>, Y slips" |
| Recommendation | "We should do X, starting with Y" |
| Reframe | "X is the same problem as Y, not a new one" |
| **Goal + blocker** | **"X for everyone, one critical decision blocks us"** |
| **Fact + implication** | **"200k downloads show the demand; we need to support every language"** |

The last two are the **compressed two-clause** form: two short clauses joined by a comma, semicolon, or dash
— the goal and what stands in its way, or the fact and what follows from it. It is the tightest way to get a
full argument into one line, and it reads as spoken rather than written. Reach for it when titles are coming
out long or essayistic.

## Before → after

| Label (wrong) | Action title (right) |
|---|---|
| Market overview | The market is consolidating around three players, and we are not one of them |
| Q3 results | Q3 revenue grew 12%, entirely from existing accounts |
| Our vision | The demand is language-agnostic, so the product should be too |
| Architecture options | Every option trades a simple install against guaranteed parity |
| Current state | We already build every algorithm twice, and our features have split |
| Team | Five maintainers now cover what one person shipped last year |
| Timeline | Locking the decision this week is the only prerequisite to starting on August 3 |
| Next steps | Two owners and one deadline close the remaining gap by March |
| Why this matters | Every quarter we wait doubles the migration cost |

## Interaction with slide density

An action title carries the argument, so the body can be lighter than you think — often a single chart, a
short evidence row, or three parallel items. If the body restates the title, cut the body. If the title
needs three sentences to be true, the slide is doing two jobs; split it.
