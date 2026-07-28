# Decision / RFC / Input-Gathering Decks

Use when the deck exists to get input on a decision that has **not been made**: architecture reviews, ADR
pre-reads, option papers, technical kickoffs that need alignment before work starts.

This is the opposite of an executive recommendation deck. There you lead with the answer. Here there is no
answer yet, and pretending otherwise defeats the purpose — you will get agreement instead of thinking.

## Do not let the structure smuggle in a conclusion

Slide order is an argument even when the words are neutral. A framing slide that presupposes one option
("here is where the shared core would sit") has already decided. So:

- Put the **"should we do this at all?"** slide **first** in the section.
- Make the framing slides that follow explicitly conditional — "*if* we do this, here is the part that
  could…", "one framing among several".
- Read the section's titles alone and ask: could a reader conclude the decision is already made? If yes,
  reorder before rewording.

## Include the status quo as a real option

"Change nothing" belongs in the options list, described fairly, with its genuine advantages stated. An
options list where one entry is obviously a straw man reads as a decision already taken and invites nobody to
argue.

## Mark exploratory content as exploratory

A deck that thinks aloud gets read as a decision unless you say so. Use all three:

- A visible badge on the relevant slides — `ILLUSTRATIVE`, `DRAFT`, `FOR DISCUSSION` — as a small uppercase,
  letter-spaced pill in a slide corner. (This is the one place uppercase is right; see baseline principles.)
- Explicit language in the body: "no recommendation attached", "non-exhaustive", "examples to argue against,
  not a menu to pick from".
- Letter the options A/B/C/D rather than numbering them, and add a trailing "…or something none of us has
  thought of yet" entry so the list does not read as closed.

## Make the difficulty legible — this is where the depth goes

Often the real job is to convince competent people that a problem is **harder than it looks**, so they engage
properly instead of answering off the cuff. That earns density: concrete failure modes, real constraints from
the codebase, second-order consequences, the thing that breaks if you choose wrong.

"This is complex" persuades nobody. Five specific reasons, each with an example, persuades everybody. These
are the load-bearing slides — spend the word budget here and keep the rest of the deck lean.

## Prefer the general mechanism over internal blame

When describing a problem inside your own organisation, describe the mechanism rather than the failure:
*"independent libraries drift apart easily, and here is how"* rather than *"our two libraries have diverged,
here is the evidence."* Same information for the purposes of the decision, less politically loaded, ages
better, and it does not put anyone in the room on the defensive. Use the specific internal evidence only when
that evidence is itself the point being argued.

## End on the ask, not on inspiration

The last thing on screen is a concrete request: one question, and a date. Cut closing statements,
restatements of the vision, and exhortations — "bring a position", "let's make this happen", "the dates are
the constraint" — they add nothing and dilute the ask. If the deck has a timeline, the ask often works better
as a highlighted callout on that slide than as a slide of its own.

## Make the ask answerable

Say what a good response contains, and keep that list short. Then say the date, once, in bold. If people have
two separate obligations (propose something; react to what others propose), name both with their own
deadlines and check the dates against your own timeline slide — it is easy to ask for a review on the day the
review is being published rather than the day the decision closes.

## Link the real thing

Put clickable links to the repositories, docs or tickets under discussion on the opening slide and on the ask
slide. Link the canonical destination only — install commands, mirrors and secondary URLs are clutter.
