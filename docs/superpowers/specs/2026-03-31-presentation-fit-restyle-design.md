# AI-101 Presentation Fit Restyle - Design Spec

**Date:** 2026-03-31  
**Scope:** Full deck restyle and compression for presentation delivery  
**Applies To:** [index.html](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/index.html)  
**Related Reference:** [DESIGN.md](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/DESIGN.md), [2026-03-30-visual-overhaul-design.md](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/docs/superpowers/specs/2026-03-30-visual-overhaul-design.md)

## Context

The deck already has the right narrative structure and approved copy. The user does not want that structure changed, and the copy must remain word-for-word. The issue is presentation fit and visual consistency: the current deck still carries uneven spacing, oversized shells, and slide-to-slide density swings that make some slides feel crowded while others feel loose. This spec defines a restrained restyle that keeps the existing content model intact while making the deck feel more professional, centered, and stage-ready.

This is not a new visual concept for the presentation. It is a controlled restyle and compression pass that preserves the existing slide sequence, content blocks, and interaction model while bringing the whole deck under one stronger presentation system.

## Approved Constraints

- Preserve the existing slide structure. Do not redesign the deck into new slide formats.
- Preserve the existing copy word-for-word. No trimming, rewriting, or content swaps.
- Optimize for a `16:9` presentation viewport first.
- Desktop presentation mode must require no vertical scrolling and no horizontal scrolling.
- Mobile may retain natural scrolling when needed.
- The desired look is a premium navy-and-cyan keynote with rainbow accents reserved for a few hero moments and details.
- Everything meaningful should animate or visually respond on hover, but the result must feel polished rather than playful.
- The work must stay aligned with [DESIGN.md](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/DESIGN.md): Space Grotesk, Instrument Sans, JetBrains Mono, dark editorial keynote styling, and projector readability.

## Chosen Direction

Use the `presentation-fit system` approach.

This means the deck gets a unified desktop slide framework with tighter spacing, better type sizing, more disciplined alignment, and component-level compression instead of trying to brute-force fit through global shrinkage. The goal is to make the deck look intentionally composed on a projector while preserving readability and the current narrative flow.

## Goals

- Make every desktop slide fit within a live `16:9` viewport with no scroll.
- Keep the deck visually consistent from slide to slide.
- Improve centering, alignment, and card discipline so the deck reads as professionally designed.
- Establish restrained hover and focus feedback on every meaningful visual element.
- Preserve existing content and interactions while improving legibility, pacing, and overall polish.

## Non-Goals

- No copy rewrites.
- No slide reordering.
- No content removal.
- No structural redesign of slide concepts.
- No playful rainbow treatment across the whole deck.
- No mobile-first redesign; mobile remains a fallback experience, not the primary composition target.

## Global Visual System

### Color

- Shift the entire deck toward a matte deep-navy canvas.
- Use cyan as the dominant working accent for headings, active states, dividers, outlines, and focused UI moments.
- Keep the warm amber accent for selective counters or premium contrast where it already supports the content.
- Reserve rainbow or multicolor accenting for a small number of hero/details:
  - title-slide highlight treatment
  - story photo ring
  - selected border sweeps or edge glows
  - closing CTA emphasis
- Reduce the amount of unrelated accent color competing within dense slides so the deck reads premium and controlled.

### Surfaces

- Flatten the current glass-heavy look into darker editorial panels with cleaner borders and more restrained shadows.
- Standardize panel radii so cards and callouts feel related instead of custom-sized on every slide.
- Use subtle layered borders and low-contrast background separation rather than bright glow everywhere.
- Keep enough glow to feel alive, but make it localized to hover/focus and hero moments.

### Typography

- Keep the current font families from [DESIGN.md](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/DESIGN.md).
- Tighten headline and subtitle spacing across the deck.
- Slightly reduce desktop `clamp()` ranges for oversized headings, subtitles, and body text so content fits without feeling miniaturized.
- Make labels, monospace metadata, and badges more consistent in size and letter spacing.
- Preserve strong projector readability by protecting line height and contrast even while compressing overall layout.

## Presentation-Fit Layout System

### Desktop Frame Rules

- Desktop slides become fixed-height presentation frames sized to the viewport minus navigation chrome.
- The slide canvas must not scroll vertically or horizontally in presentation mode.
- Inner content areas should use disciplined max heights and balanced alignment rather than overflow-based layouts.
- Reduce top and bottom slide padding so more of the canvas is usable for actual content.

### Rhythm and Spacing

- Normalize heading, subtitle, and body spacing so each slide starts from the same visual rhythm.
- Tighten vertical gaps between panels, cards, chips, and support text.
- Reduce excessive card padding and minimum heights where they currently create avoidable overflow.
- Re-center or rebalance slides whose content currently leans too high, too low, or too far wide.

### Width and Alignment

- Keep wide slides from feeling stretched by constraining text measures and tightening content groups inside the available width.
- Use centered composition only where the slide already implies a centered hero or focal object.
- Otherwise keep strong left alignment, but align components to a cleaner common grid so the deck feels more deliberate.

### Overflow Policy

- On desktop, layout compression wins before overflow is allowed.
- Horizontal scrolling is not allowed anywhere in desktop presentation mode.
- Vertical scrolling is not allowed for slide canvases in desktop presentation mode.
- On mobile breakpoints, vertical scrolling remains acceptable and layouts may stack more naturally.

## Interaction and Motion

### Hover and Focus Language

- Every meaningful block should respond to hover or focus:
  - cards
  - chips and tags
  - nav buttons
  - carousel controls
  - orbital nodes
  - assistant cards
  - prompt panels
  - tool panels
  - CTA shells
  - framed media or visual containers
- Response behavior should be consistent:
  - slight upward lift
  - brighter border or accent edge
  - subtle localized glow
  - stronger text/icon contrast
- Plain paragraph text should not animate independently; it should inherit emphasis through the hovered parent container.

### Motion Tone

- Keep the current slide-entry choreography, but unify and shorten it so the deck feels smoother and less uneven.
- Avoid continuous ornamental motion on every component.
- Avoid hover states that resize layouts enough to cause jitter or reflow.
- Respect `prefers-reduced-motion` with simplified fades and static states.

## Slide-by-Slide Design Rules

### Slide 0 - Title

- Keep the hero structure intact.
- Strengthen the navy background and cyan-led focus treatment.
- Reserve a subtle rainbow accent for the title highlight and hero-detail energy.
- Reduce oversized empty space so the hero sits more confidently within the presentation frame.
- Ensure badge, headline, subtitle, and supporting visual stack feel centered and balanced rather than loosely separated.

### Slide 1 - My Story

- Preserve the current narrative stack: title, intro row, highlight cards, tag cloud, kicker.
- Tighten the intro row so the photo and lead statement feel like one composed unit.
- Compress highlight-card padding and rebalance the grid so all cards fit comfortably without feeling cramped.
- Use the photo ring as one of the deck's selective rainbow-accent hero details.
- Keep the tag cloud compact and aligned so it reads as a supporting layer rather than spillover.
- Position the kicker lower with cleaner spacing so the slide lands with intention.

### Slide 2 - Science Proof

- Preserve the existing timeline/node structure.
- Compress heading, subtitle, and node spacing to keep the science slide inside the frame.
- Reduce decorative dead space between the timeline header area and the node shells.
- Make node shells more consistent in height and internal spacing so the three examples read as one editorial system.
- Use cyan as the dominant unifying accent, allowing individual node colors to remain secondary.

### Slide 3 - Education Proof

- Preserve the editorial callout structure and source framing.
- Tighten the height of the tall and wide callout blocks through smaller padding, tighter stat spacing, and more controlled headline/body relationships.
- Improve alignment between the wide left block, the tall right block, and the full-width takeaway block so the slide feels composed rather than stacked.
- Keep the typography strong but reduce any wasted internal space that pushes the slide too tall.

### Slide 4 - Tool Landscape

- Keep the orbital diagram and current content hierarchy.
- Compress the surrounding shell so the focal diagram gets priority without overflowing vertically.
- Use a cleaner navy/cyan orbital treatment with restrained support colors on the nodes.
- Make hover/focus on each node feel precise and premium, not game-like.
- Keep the centered focal composition because the slide already depends on a central object.

### Slide 5 - Big Three

- Preserve the assistant constellation structure and assistant cards.
- Tighten constellation spacing so the card stack and background treatment read in one glance.
- Make the active card state clearer through cyan-led emphasis and localized glow.
- Reduce oversized padding inside assistant cards so all three remain comfortably visible on a presentation screen.
- Keep branding readable while bringing the slide into the shared deck system.

### Slide 6 - Specialists

- Preserve the carousel structure, controls, and specialist content.
- Resize carousel shells, controls, and dot/navigation regions to reclaim vertical space.
- Ensure the active specialist card feels centered and presentation-scaled without becoming oversized.
- Add clear hover/focus response to nav controls and active specialist surfaces.
- Keep carousel interaction obvious while visually harmonizing it with the rest of the deck.

### Slide 7 - Applications

- Preserve the current cluster layout and use-case grouping.
- Tighten card padding and the spacing between cluster items so the slide fits the frame cleanly.
- Reduce image/icon and text imbalance so the grid looks professionally weighted.
- Keep the content scan-friendly from left to right without flattening the hierarchy.
- Ensure hover/focus makes each cluster feel selectable and alive without changing the layout.

### Slide 8 - Prompt Lab

- Preserve the formula blocks, prompt example, and prompt asset area.
- Compress the desktop prompt shell more aggressively than looser slides because this is one of the most likely overflow risks.
- Tighten the relationship between the formula grid and the prompt example so they feel like one intentional workspace.
- Keep the prompt area prominent, but remove oversized padding and excessive shell height.
- Add hover and focus polish to formula blocks, asset cards, copy controls, and the prompt display container.

### Slide 9 - Safety

- Preserve the shield/caution framing and the current message structure.
- Tighten spacing so the safety slide feels editorial and authoritative rather than oversized.
- Use cyan as the organizing accent and let any warning tones stay secondary and sparse.
- Keep the message calm, readable, and projector-clear.

### Slide 10 - Close / CTA

- Preserve the closing structure and call-to-action flow.
- Center the CTA card and supporting elements more confidently within the frame.
- Use one of the deck's selective rainbow accents here for edge emphasis and emotional lift.
- Reduce shell bulk so the slide feels elegant and final rather than merely large.
- Make hover/focus on the CTA region the most visible in the deck without breaking the premium tone.

## Responsive Rules

- Desktop and presentation contexts are the source of truth for composition.
- Tablet may inherit most desktop compression rules with slightly more forgiving spacing.
- Mobile may stack more aggressively and allow vertical scrolling where needed.
- Mobile does not need to obey the no-scroll presentation constraint.

## Implementation Boundaries

- Primary work should happen inside [index.html](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/index.html), since the current architecture embeds CSS and JS in a single file.
- The restyle should favor CSS and layout tuning over JavaScript rewrites unless a specific interaction needs adjustment to support the new hover/focus system.
- Existing tests should be updated only if they are coupled to layout assumptions that no longer match the approved design direction.

## Verification Criteria

- Every slide fits inside a desktop `16:9` viewport with no vertical or horizontal scrolling.
- Desktop slides remain visually balanced and readable at presentation scale.
- The deck consistently uses the navy-and-cyan system with rainbow accents only in selected hero/detail moments.
- Every major interactive or framed component has a visible hover/focus response.
- No hover effect causes layout jitter, overflow, or distracting movement.
- Mobile remains usable, with scrolling allowed there when required.
- The final result feels more professional and aligned, not merely smaller.

## Acceptance Summary

This design is successful if the existing deck feels like the same presentation, only cleaner, tighter, more coherent, and more stage-ready. The audience should experience a premium keynote-style deck that fits the screen, reads clearly, and responds gracefully, without noticing that the underlying structure and copy were intentionally left intact.
