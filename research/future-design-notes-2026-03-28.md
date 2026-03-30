# AI-101 Future Design Notes

Date: 2026-03-28

## Why This Note Exists

The deck is in a much better place visually, but it is not "finished forever." This note captures what still feels heavy, what is heavy on purpose, and what the next design pass should improve.

## Core Read

The presentation now feels more like a product keynote and less like an AI template. That was the right move.

What still needs design work is not the overall taste level. It is the information architecture inside a few slides.

## Important Constraint

The prompt slide is heavy for a real reason.

It is not just a pretty slide. It is a live demonstration surface, a teaching tool, and a reusable operator deck. That means some density is necessary. The goal is **not** to make it minimal. The goal is to make it **legible, staged, and intentional**.

Future work should avoid "cleaning it up" by removing the parts that make the demo useful.

## What Still Feels Underdesigned

### 1. The Prompt Slide

Current state:
- Necessary, useful, and much better than before
- Still reads as a dense tool panel instead of a fully designed teaching moment

What it needs:
- Stronger separation between the **teaching framework** and the **live prompt specimen**
- Clearer "where should the audience look first?" logic
- Better chunking of the long prompt text
- A more intentional stage/demo mode feel

Recommended future direction:
- Keep the 4-part formula at the top, but treat it as a compact legend, not equal-weight cards
- Make the example prompt area the hero surface of the slide
- Use progressive reveal or spotlighting so only the currently discussed section gets maximum contrast
- Consider a split mode:
  - **Teach mode:** one section highlighted at a time
  - **Operator mode:** full prompt shown for live use
- Consider adding a "presentation crop" version of the prompt that shows only the current segment plus 1-2 lines of surrounding context

Do not do:
- Do not remove the prompt packet tools entirely
- Do not flatten everything into tiny text to fit more on screen
- Do not turn it into a pretty static diagram if it loses demo utility

### 2. The Overview Slide

Current state:
- Conceptually useful
- Still a little too "list of categories" instead of a designed mental model

What it needs:
- A more memorable organizing visual
- Fewer repeated small icon moments
- A stronger sense of hierarchy between everyday tools and specialist tools

Recommended future direction:
- Build this slide around one central framing metaphor and two supporting columns
- Or turn it into a left-to-right spectrum from broad/general to narrow/specialized
- Let the artwork support the slide, not compete with it

### 3. The Practical Use Cases Slide

Current state:
- Helpful content
- Visually dense because every use case currently gets near-equal weight

What it needs:
- Better grouping
- Fewer simultaneous focal points
- More scannable clusters

Recommended future direction:
- Group by audience type or life/job context instead of one flat grid
- Example buckets:
  - work
  - learning
  - local business
  - personal life
- Consider showing 4-6 featured cases first, then revealing the rest

### 4. Final CTA Slide

Current state:
- Cleaner now
- Still doing two jobs: tool recommendations and personal/contact close

What it needs:
- A stronger sense of emotional finish
- One dominant closing action

Recommended future direction:
- Decide if the close is mainly:
  - "try one of these tools tonight"
  - or "contact Adam / follow up"
- Then subordinate the other goal
- If the tool CTA stays primary, the contact block should feel secondary and lighter

## What Is Intentionally Heavy And Should Stay That Way

These are not bugs. These are tradeoffs.

### Prompt Slide
- It is okay for this slide to be denser than the others
- It is the one slide where the audience should feel the system becoming concrete

### Use Case Coverage
- Breadth matters because the deck is trying to make AI feel relevant across many real-world contexts
- The answer is better grouping, not aggressive deletion

### Footer Navigation
- Because this is a live browser deck, navigation affordances matter more than they would in exported slides
- Keep the controls calm, but do not hide the interaction model

## Best Future Design Bets

If there is time for only one more serious design pass, do these in order:

1. Redesign the prompt slide as a true dual-purpose teaching + operator surface
2. Rebuild the use-cases slide into grouped clusters with featured examples
3. Redesign the overview slide into a stronger mental-model visual
4. Tighten the final CTA into one primary closing move

## Build Notes For Future Me

### Prompt Slide Ideas Worth Exploring

- Add a spotlight state tied to the prompt carousel so the relevant framework label glows while the others dim
- Add a "copy for live demo" control that stays visually separate from the reading surface
- Add collapsible or tabbed prompt views:
  - full prompt
  - highlighted prompt
  - run packet
- Create a larger projector-optimized prompt text block with fewer UI elements visible by default

### Structural Principle

The next redesign should focus less on colors and surfaces and more on:
- sequence
- reveal
- grouping
- focus

Taste is no longer the main problem. Choreography is.

## Short Version

The deck now looks professional.

The next leap is not "more polish." It is designing the dense slides as intentional information systems, especially the prompt slide.
