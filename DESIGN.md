# Design System - AI-101

## Product Context
- **What this is:** A live browser-based educational presentation that demystifies AI tools for a mixed non-technical audience through slides and live demos.
- **Who it's for:** Community groups, learners, small-business owners, creators, job seekers, and general audiences who need practical AI framing.
- **Space/industry:** Educational keynote / workshop presentation
- **Project type:** Editorial keynote deck delivered as a static HTML presentation

## Aesthetic Direction
- **Direction:** Editorial product keynote
- **Decoration level:** Intentional
- **Mood:** Calm, premium, credible, and energetic without feeling flashy or trend-chasing. The deck should feel like a well-produced product launch talk, not a startup template.
- **Reference sites:** https://www.figma.com/blog/how-teams-tap-into-the-power-of-design-with-figma-slides/, https://www.canva.com/learn/presentation-ideas/, https://images.apple.com/education/docs/app-showcase-guide.pdf

## Typography
- **Display/Hero:** Space Grotesk - geometric and modern, with enough personality to carry keynote-scale headlines
- **Body:** Instrument Sans - clean, readable, and less generic than default UI sans stacks
- **UI/Labels:** JetBrains Mono - for slide numbers, metadata, controls, and prompt framing
- **Data/Tables:** JetBrains Mono
- **Code:** JetBrains Mono
- **Loading:** Google Fonts
- **Scale:** Hero `clamp(40px, 6vw, 80px)`, H1 `clamp(34px, 5vw, 64px)`, H2 `clamp(28px, 3.5vw, 44px)`, H3 `clamp(16px, 1.8vw, 22px)`, subtitle `clamp(16px, 1.8vw, 24px)`

## Color
- **Approach:** Restrained
- **Primary:** `#8BD6FF` - used for headlines, metadata, active states, and key emphasis
- **Secondary:** `#53B3F8` - deeper blue support for focus accents and subtle tonal variation
- **Warm accent:** `#D7A65A` - sparing contrast for progress, counters, and premium warmth
- **Neutrals:** `#FFFFFF`, `#F5F7FB`, `#AAB7CB`, `#78869A`, `rgba(148, 163, 184, 0.18)`
- **Semantic:** success `#10B981`, warning `#F59E0B`, error `#EF4444`, info `#8BD6FF`
- **Dark mode:** Native design mode. Dark surfaces stay matte, text stays high-contrast, accent saturation stays controlled.

## Spacing
- **Base unit:** 8px
- **Density:** Comfortable
- **Scale:** 2xs(4) xs(8) sm(12) md(16) lg(24) xl(32) 2xl(48) 3xl(64)

## Layout
- **Approach:** Hybrid
- **Grid:** Wide desktop slide canvas with structured card grids and tighter editorial heading blocks
- **Max content width:** 1520px
- **Border radius:** sm 10px, md 14px, lg 18px, full 999px

## Motion
- **Approach:** Minimal-functional
- **Easing:** enter `ease-out`, exit `ease-in`, move `ease-in-out`
- **Duration:** micro 120ms, short 200ms, medium 320ms, long 500ms

## Rules
- Default to left-aligned composition on desktop unless a slide needs a centered hero moment.
- Use one dominant visual idea per slide.
- Keep decorative emoji out of headers, badges, and system markers.
- Favor product-demo clarity over visual gimmicks.
- If a visual choice feels "cool" but hurts scan speed from the back of the room, cut it.

## Future Notes
- Follow-on design thoughts live in [research/future-design-notes-2026-03-28.md](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/research/future-design-notes-2026-03-28.md)

## Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-03-28 | Moved from blue-purple glassmorphism to editorial keynote styling | The original deck looked polished but still read as a template on stage |
| 2026-03-28 | Replaced Inter with Space Grotesk + Instrument Sans | Stronger identity and better headline/body contrast |
| 2026-03-28 | Reduced emoji markers and normalized UI chrome | Increased professionalism and projector readability |
