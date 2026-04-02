# AI-101 Full Deck Visual Overhaul — Design Spec

**Date:** 2026-03-30
**Branch:** `codex/ai101-visual-overhaul`
**Scope:** All 11 slides + global transitions

## Context

The AI-101 presentation is a browser-based educational keynote (vanilla HTML/CSS/JS + p5.js) with 11 slides. The current build has solid content and a dark glassmorphism aesthetic, but slides 4-7 feel visually monotonous (repeated glass card grids) and the rest of the deck needs a consistent quality lift to serve as both a live stage presentation and a portfolio showpiece. This spec defines a per-slide visual treatment that mixes cinematic, data-viz, interactive, and editorial energy to keep audience attention across the full deck.

## Constraints

- **Dual delivery mode:** Live presenter-driven (animations auto-play on slide entry) + async self-guided (hover/click interactions matter)
- **Hardware target:** Modern laptop/GPU — WebGL, canvas, GPU-accelerated CSS all fair game
- **Design system:** Must stay within DESIGN.md (Space Grotesk + Instrument Sans + JetBrains Mono, dark palette with `#8BD6FF` / `#53B3F8` / `#D7A65A` accents)
- **Accessibility:** All animations must respect `prefers-reduced-motion: reduce`
- **Projector readability:** High contrast, large type — "if it looks cool but hurts scan speed from the back of the room, cut it"
- **File:** Single `index.html` with embedded CSS/JS (existing architecture, no build step)

## Global: Cinematic Cross-Dissolve Transitions

**Replace** the current `translateX(60px) + opacity` slide transition.

- Outgoing slide: `scale(0.97)` + `filter: blur(2px)` + `opacity: 0` over 0.6s ease-out
- Incoming slide: starts at `scale(1.03)` + `opacity: 0`, settles to `scale(1)` + `opacity: 1` over 0.6s ease-out
- Direction-aware: keep left/right awareness from current implementation for the subtle positional offset, but the primary motion is scale + blur, not translateX
- Reduced-motion fallback: instant opacity swap (no scale, no blur)

## Slide 0 — Particle Vortex Hero

**Treatment:** Full-screen p5.js canvas behind the title. Particles swirl inward on load and briefly form the outline/silhouette of the title text, then disperse into ambient drift.

- **Canvas:** Full viewport behind slide content, z-index below text
- **Particle count:** ~300-500 (performance-tuned)
- **Behavior:** On slide entry, particles converge toward text bounding box over 1.5s (spring-damped), hold shape for 0.5s, then release into slow ambient drift
- **Title:** Snaps to full opacity at 1.5s (not dependent on particles completing)
- **Subtitle + badge:** Staggered fade-in at 2.0s and 2.3s
- **Colors:** Particles use accent palette (`#8BD6FF`, `#53B3F8`) at varying opacity
- **Idle state:** Particles continue slow drift indefinitely (ambient life)
- **Reduced-motion:** Static title, no particle animation, simple fade-in

## Slide 1 — Timeline Thread

**Treatment:** Photo on the left with a vertical animated thread connecting down to proof cards.

- **Photo:** Keep existing photo ring but add subtle parallax offset on entry (translateY -10px → 0)
- **Thread line:** SVG or CSS pseudo-element, 2px wide, accent color (`#8BD6FF`), draws itself top-to-bottom on slide entry (stroke-dasharray animation, 0.8s)
- **Proof cards:** Positioned along the thread. Each card gets a small circular node where it connects to the thread. Cards fade in staggered as the thread reaches their position
- **Timestamp badges:** Small monospace (JetBrains Mono) date labels on each card node
- **Layout:** Photo top-left, thread descends vertically, cards branch right from the thread
- **Reduced-motion:** Static layout, thread visible at full length, cards visible without stagger

## Slides 2 & 3 — Editorial Callout Blocks

**Treatment:** Magazine-style typography with wipe-reveal entrance animation.

- **Headline stat:** Large pull-quote typography (Space Grotesk, clamp scale ~H1 size), accent color
- **Supporting text:** Instrument Sans body below, normal weight, `--text-dim` color
- **Accent rule:** 2px horizontal line, accent color, separating headline from body, width animates from 0% → 100% on entry (0.4s)
- **Entrance:** `clip-path: inset(0 100% 0 0)` → `inset(0 0% 0 0)` wipe-reveal (0.6s ease-out), staggered per content block
- **Source citations:** Fade-in from bottom at the end of the entrance sequence
- **No counters** — typography and spacing do the work

## Slide 4 — Orbital Diagram

**Treatment:** Radial layout replacing the horizontal spectrum bar.

- **Center node:** "AI" label, circular, accent-bordered, subtle pulse animation
- **Orbital rings:** 4 concentric circles (CSS or SVG), each at increasing radius, decreasing opacity (0.3 → 0.1)
- **Nodes:** 4 spectrum items positioned on the rings (innermost = "General chat", outermost = "Reasoning & analysis")
- **Entry animation:** Center appears first, then rings draw outward (stroke-dasharray), then nodes fly in from off-screen edges and settle into position with spring easing (overshoot + settle, 0.8s staggered)
- **Hover:** Node scales up slightly (1.05), ring brightens, description text expands
- **Layout:** Centered on slide, max-width ~800px for the diagram, labels positioned outside nodes
- **Content:** Same 4-tier information (General → Creative → Research → Reasoning), just radial instead of linear

## Slide 5 — Floating Logo Constellation

**Treatment:** Three large logos with parallax drift and p5.js particle background.

- **Logos:** ChatGPT, Claude, Gemini — each ~100-120px, floating with subtle independent drift (CSS animation, different durations: 6s, 7s, 8s)
- **Particle field:** p5.js canvas behind the cards. ~150 particles in slow Brownian drift. On hover over a logo, nearby particles accelerate toward it (gravitational pull effect)
- **Info panels:** On hover (desktop) or click (mobile/async), an info panel expands beside the hovered logo — contains the tool description, badge, pricing. Panel slides in from the direction of the logo
- **Brand glow:** Each logo has a subtle radial gradient halo in its brand color (green/purple/blue) behind it
- **Entry:** Logos scale up from 0.5 → 1.0 with stagger (0.3s delay each), particle field fades in over 1s
- **Default state:** When nothing is hovered, all three info panels are visible in a balanced layout (for live presentation mode where there's no hover)
- **Reduced-motion:** Static layout with all panels visible, no particle field

## Slide 6 — Carousel Showcase

**Treatment:** Horizontal carousel replacing the 2×2 grid. One specialist at a time, full-width.

- **Layout:** Full-width card showing: large logo (80px+), brand-color background wash (subtle gradient), tool name in large type, tagline, description, link
- **Navigation:** Dots indicator at the bottom. Auto-advance every 4s in live mode. Swipeable/clickable in async mode
- **Transition:** Outgoing card slides left + fades, incoming slides in from right + fades in (0.4s)
- **Brand wash:** Each specialist gets a unique subtle background gradient in their brand color direction (Perplexity = cyan wash, NotebookLM = amber, DeepSeek = blue, Grok = red)
- **Progress:** Thin accent-colored progress bar under the active dot that fills over the 4s auto-advance timer
- **4 items:** Perplexity, NotebookLM, DeepSeek, Grok — same content, elevated presentation
- **Keyboard:** Dedicated carousel nav buttons (not left/right arrows, which control slide navigation). Use on-screen prev/next chevrons or dot clicks. Auto-advance pauses on any manual interaction and resumes after 6s idle

## Slide 7 — Illustrated Scene Cards

**Treatment:** Tall cards with prominent AI-generated scene images.

- **Card layout:** Image takes top ~40% of card height, text content below
- **Images:** Use existing assets from `assets/images/generated/practical-use-cases/` (hospitality, trades, libraries, education, job seekers, legal, local news, real estate)
- **Grid:** 2×2 for the 4 clusters (each cluster = 1 card with its dominant image)
- **Image selection:** Use one representative image per cluster (hospitality for "Local business", libraries for "Learning", job seekers for "Career", local news for "Personal projects")
- **Entry:** Cards enter with parallax-style stagger — each card has a slight delay + translateY offset that resolves (like scrolling into view)
- **Hover:** Card lifts slightly (translateY -4px) + shadow deepens
- **Sub-items:** The 2 use cases per cluster appear as compact list items below the image, with the small icon inline
- **Reduced-motion:** Static grid, no stagger

## Slide 8 — Card Stack with Depth

**Treatment:** Prompts as a physical deck of cards with peel animation.

- **Stack:** 3-4 visible cards, each offset by ~4px and rotated ~1-2deg (alternating direction). Active card is front-and-center (upright, no rotation), full opacity
- **Advance:** Top card peels away (translateX + rotate + opacity → 0) revealing the next card beneath, which snaps to front position
- **Formula blocks:** Float alongside the card stack (right side on desktop), connected by thin dotted lines to the relevant parts of the active prompt
- **Prompt display:** Keep existing RTCF color-coding (role/task/context/format syntax highlighting)
- **Copy button:** On the active card, with checkmark animation on click (check icon scales in, holds 1s, fades back to copy icon)
- **Navigation:** Arrow buttons or swipe to advance. Current position indicator (e.g., "3 / 10")
- **Entry:** Stack slides in from the right on slide entry, formula blocks fade in from the left

## Slide 9 — Shield Grid with Pulse

**Treatment:** Safety principles in hexagonal/shield containers with sequential light-up.

- **Container shape:** Hexagonal clip-path (`polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)`) or rounded shield shape
- **Grid:** 3×2 arrangement of shields
- **Entry animation:** Center shield lights up first, then adjacent shields pulse outward in a ripple pattern (0.2s stagger). "Light up" = border brightens from dim to accent color + subtle inner glow
- **Icons:** Existing safety-ethics icons (v2 PNGs), centered in each shield, scale up on the pulse
- **Hover:** Shield border glows brighter, icon scales slightly, description text brightens from dim to primary
- **Idle pulse:** After entry, shields have a very subtle breathing pulse (opacity 0.9 → 1.0, 3s cycle, staggered)
- **Colors:** Shield borders use `--accent` color, backgrounds use the existing glass treatment

## Slide 10 — Callback Montage

**Treatment:** Retrospective background with centered CTA glass card.

- **Background:** 6-8 small thumbnails from earlier slides (hero text, a logo, an evidence stat, a use-case image, a prompt card, a safety icon) — blurred (`filter: blur(8px)`), low opacity (0.15), positioned in a loose scattered layout
- **Thumbnails:** CSS-recreated simplified mini-elements (not screenshot images) — e.g., a small glass card with the title gradient text, a tiny logo cluster, a mini pull-quote block, a small hexagon shield. Styled inline, no external assets needed. Slow drift animation (different speeds/directions per thumbnail)
- **CTA card:** Centered glass card with call-to-action text, contact/follow-up links
- **Entry:** Thumbnails fade in first (0.5s), then CTA card scales up from 0.9 → 1.0 with fade (0.3s delay)
- **Mood:** "Look how much ground we covered" — the montage creates visual weight that makes the closing feel earned

## Implementation Notes

### Files to Modify
- `index.html` — all HTML structure changes + embedded CSS + embedded JS

### Existing Code to Reuse
- p5.js is already loaded via CDN (v1.9.0) — used for slides 0 and 5 particle effects
- Slide engine (navigation, state management, progress bar) — extend, don't replace
- `.glass` class and glassmorphism surface treatment — reuse for new card styles
- `fadeInUp` and stagger animation classes (`.anim-1` through `.anim-5`) — keep for simple reveals
- Badge component (`.badge-blue`, `.badge-purple`, etc.) — reuse as-is
- Prompt catalog system (`ai101-demo-prompt-catalog.js`) — carousel data source for slide 8

### New Code Required
- p5.js sketch for slide 0 (particle vortex)
- p5.js sketch for slide 5 (particle constellation)
- Carousel component JS for slide 6
- Card stack component JS for slide 8
- SVG/CSS orbital diagram for slide 4
- Updated slide transition CSS (cross-dissolve)
- Hexagonal clip-path + ripple animation CSS for slide 9
- Callback montage layout CSS for slide 10

### Performance Budget
- p5.js sketches: only run when their slide is active (pause/resume on slide change)
- Carousel auto-advance: clear interval when slide is not active
- Total additional JS: target < 300 lines
- No new external dependencies beyond existing p5.js

## Verification Plan

1. Open `index.html` in Chrome — navigate all 11 slides, verify each treatment renders correctly
2. Test forward and backward navigation — cross-dissolve transitions in both directions
3. Hover over interactive elements on slides 4, 5, 6, 8, 9 — verify hover states
4. Set `prefers-reduced-motion: reduce` in dev tools — verify all animations gracefully degrade
5. Test at 1920×1080 (projector resolution) — verify readability from distance
6. Test at mobile viewport (375px) — verify responsive layout doesn't break
7. Check for console errors — no JS exceptions on any slide
8. Verify prompt carousel copy-to-clipboard still works on slide 8
9. Performance check — smooth 60fps on slide transitions and p5.js sketches
