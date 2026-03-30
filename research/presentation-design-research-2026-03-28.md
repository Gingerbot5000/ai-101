# AI-101 Presentation Design Research

Date: 2026-03-28

## Goal

Turn `index.html` into a professional live browser presentation that feels closer to a product keynote than a stylish AI template.

## Research Inputs

- Figma, "How Teams Tap Into the Power of Design with Figma Slides"
  https://www.figma.com/blog/how-teams-tap-into-the-power-of-design-with-figma-slides/
- Canva, "Presentation design: A beginner's guide to creating impactful slides"
  https://www.canva.com/learn/presentation-ideas/
- Apple, "App Showcase Guide"
  https://images.apple.com/education/docs/app-showcase-guide.pdf
- Local deck research already in repo
  [04-visual-direction.md](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/research/agents/04-visual-direction.md)

## Layer 1: Tried And True

- Strong presentation systems reuse the same visual language across slides instead of redesigning every screen.
- The opening screen needs one clear composition, not several equal focal points.
- Large screens reward fewer accents, clearer typographic scale, and stronger signposting.
- Product demos should look polished, but the deck should still read instantly from the back of the room.

## Layer 2: Current Patterns

- Figma's Slides material leans into design-system transfer, color libraries, animation, and visual storytelling over generic office-slide styling.
- Canva's current presentation guidance reinforces recurring motifs, one accent color used deliberately, interactive moments, mobile awareness, and restraint with animation.
- Apple's showcase guidance still points toward polished presentation mode and demo clarity rather than clutter.

## Layer 3: First Principles For This Deck

- This is a live browser talk, not a PDF-first pitch deck, so the real product is the rendered HTML on a projector.
- The audience is mixed and non-technical, so the deck should feel confident and premium without looking cold or overly enterprise.
- The current deck already has energy. The fix is not "more design." The fix is better taste filters.

## Recommendation

Use an editorial product-keynote direction:

- Custom typography instead of default startup UI typography
- Dark matte surfaces instead of neon glassmorphism
- One primary cool accent with one warm support accent
- Fewer decorative emoji markers
- Quieter navigation chrome
- Terminal-grade prompt panel styling for the live demo slide

## What Changed In Code

- Replaced `Inter` with `Space Grotesk` for headline typography and `Instrument Sans` for body copy.
- Removed the purple secondary accent token and moved to an ice-blue plus brass palette.
- Reworked cards, badges, navigation, and prompt panels into calmer presentation surfaces.
- Removed several decorative emoji markers that reduced professionalism on stage.
- Added regression tests so the new design system is encoded, not just eyeballed.
