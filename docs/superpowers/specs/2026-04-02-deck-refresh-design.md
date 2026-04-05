# AI-101 Deck Refresh — Design Spec

**Date:** 2026-04-02
**Branch:** codex/ai101-visual-overhaul

## Overview

Tighten the deck from 11 slides to 9, update content to reflect 2026 tool landscape, fix hover interactions, and apply consistent visual polish throughout.

## Final Slide Order

| # | Title | Status |
|---|-------|--------|
| 1 | THE AI BREAKDOWN (title) | Polish only |
| 2 | Why I'm Standing Up Here (my story) | Content fix + hover fix |
| 3 | AI is accelerating Nobel-scale discovery | Add 4th card (math proofs), 4-across layout |
| 4 | Meet the Big Three | Add accent colors, update descriptions, fix hover |
| 5 | Additional AI Tools (NEW) | New slide — icon wall with hover info cards |
| 6 | Where this actually saves you time | Polish only |
| 7 | Prompt Lab | Polish only |
| 8 | Move fast, stay honest (safety) | Polish only |
| 9 | Try one thing tonight (closing) | Polish only |

## Removed Slides

- **Old slide 4** ("What the research actually shows" — education proof): Removed entirely
- **Old slide 5** ("The AI tool landscape at a glance" — concentric rings): Replaced by new tool wall
- **Old slide 7** ("When the job gets narrower" — specialists carousel): Tools moved to new tool wall

## Slide-by-Slide Changes

### Slide 2 — My Story

Fix card titles and descriptions to match real accomplishments:

| Current Title | New Title | New Description |
|---|---|---|
| I made a video | Grammy-winner visuals | Created a video used as a visual for Grammy Award winner Fatboy Slim |
| I built a workflow | Built real business websites | Designed and shipped several live sites for businesses — starting from zero web experience |
| I started a business | Started my own company | Research, branding, planning, launch — AI made the iteration loop fast enough that momentum won |
| I designed logos | Designed apps and games | Built interactive applications and game prototypes that would have taken a full dev team before |

- Card accent colors: green (#10B981), cyan (#8BD6FF), gold (#D7A65A), purple (#a78bfa)
- Subtle hover glow matching each card's accent color
- Body text minimum: `clamp(15px, 1.5vw, 18px)`

### Slide 3 — Breakthroughs

Add 4th card, reflow to 4-across:

1. **AlphaFold** — Chemistry Nobel 2024 (keep)
2. **GNoME** — 2.2M candidate crystals (keep)
3. **Weather/Science** — speed + scale pattern (keep)
4. **Math Proofs** (NEW) — Badge: "MATHEMATICS 2026". Headline: "Proof Assistant". Description: "Terence Tao — widely considered the world's greatest living mathematician — now uses AI as a proof assistant, calling it 'ready for primetime' in math and theoretical physics." Takeaway: "The frontier moved from search to reasoning."

- Animated icon for card 4: math-themed (summation/proof symbol)
- Compact padding and font to fit 4 across without overflow
- Subtle hover glow on each card

### Slide 4 — Meet the Big Three

- Keep horizontal card layout with orb icons
- Add colored left borders + matching hover glow:
  - ChatGPT: green (#10B981)
  - Claude: cyan (#8BD6FF)
  - Gemini: gold (#D7A65A)
- Update descriptions:
  - Claude: mention Claude Code as key capability
  - Gemini: mention Google AI Studio and ecosystem integration
- Ensure hover actually triggers (verify CSS specificity)

### Slide 5 — Additional AI Tools (NEW)

- Title: "Additional AI Tools"
- Subtitle: "The ecosystem is wide. These are worth knowing."
- Layout: Grid of rounded-square tiles (~64px icon area), ~4-5 across, centered
- Each tile: glass background, letter/mark icon, tool name below

**Tool list (13 tools):**

| Category | Tools |
|---|---|
| Music | Suno, ElevenLabs |
| Video | Haiggsfield, Krea |
| Image | Freepik, Stable Diffusion |
| Research | NotebookLM, Perplexity |
| Code | Claude Code, Codex, Google AntiGravity |
| Open Source Models | Qwen 3.5, DeepSeek |

**Hover behavior:**
- Floating info card appears adjacent to hovered tile
- Contains: tool name, one-line description, "Visit →" link
- Glass + subtle glow style, same as deck standard
- Card positioned to avoid viewport overflow (flip if near edge)

### Slides 6-9 — Global Polish Only

- **Slide 6 (Applications):** Subtle hover glow on category cards, bump text sizes
- **Slide 7 (Prompt Lab):** No structural changes
- **Slide 8 (Safety):** Hover glow on hex shields
- **Slide 9 (Closing):** Fix text overflow on right edge

## Global Standards

### Hover Effect (all interactive cards)

```css
/* Standard subtle glow */
.card:hover {
    background: rgba(255, 255, 255, 0.06);
    box-shadow:
        0 0 20px rgba(var(--card-accent-rgb), 0.15),
        0 8px 32px rgba(0, 0, 0, 0.2),
        inset 0 0 0 1px rgba(var(--card-accent-rgb), 0.25);
    transition: all 0.25s ease;
}
```

### Text Sizing

- Body minimum: `clamp(16px, 1.6vw, 20px)` across all slides
- Headlines: per DESIGN.md scale (no change)
- Card titles: `clamp(17px, 1.8vw, 22px)` minimum

### Color Consistency

- Dark matte backgrounds (no change)
- Primary accent: #8BD6FF
- Warm accent: #D7A65A (kickers, highlights, progress)
- Card borders: rgba(148, 163, 184, 0.18)
- Per-card accent colors where specified

### Viewport Fit

- All slides must fit 1280x800 without scrolling
- No text overlap or clipping
