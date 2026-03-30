# Agent 4 — Visual & Interaction Direction: Dark-Theme Web Slide Deck

## Typography

```css
/* Scale: modular — 1.333 (perfect fourth) */
:root {
  --text-xs:   0.75rem;
  --text-sm:   1rem;
  --text-base: 1.333rem;
  --text-lg:   1.777rem;
  --text-xl:   2.369rem;
  --text-2xl:  3.157rem;
  --text-hero: clamp(2.5rem, 6vw, 5rem);

  /* Stack: geometric mono hero + humanist body — never system-ui alone */
  --font-hero: 'Space Grotesk', 'DM Sans', sans-serif;
  --font-body: 'Inter', sans-serif;          /* fallback only */
  --font-mono: 'JetBrains Mono', monospace;

  --weight-thin:   300;
  --weight-body:   400;
  --weight-accent: 600;
  --weight-hero:   700;

  --tracking-tight: -0.03em;   /* hero headlines */
  --tracking-wide:  0.12em;    /* eyebrow labels */
  --leading-tight:  1.1;
  --leading-body:   1.6;
}

/* Hero headline rule: tight tracking, mixed weight */
.slide-hero h1 {
  font-family: var(--font-hero);
  font-size: var(--text-hero);
  font-weight: var(--weight-hero);
  letter-spacing: var(--tracking-tight);
  line-height: var(--leading-tight);
}

/* Eyebrow labels above headlines */
.eyebrow {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  font-weight: var(--weight-accent);
  letter-spacing: var(--tracking-wide);
  text-transform: uppercase;
  color: var(--accent-primary);
}
```

---

## Color System

```css
:root {
  /* Backgrounds — 3-layer depth */
  --bg-base:    #0a0a0f;   /* void black with a hint of blue */
  --bg-surface: #12121a;   /* card background */
  --bg-raised:  #1c1c28;   /* interactive / hovered */

  /* Accents — ONE saturated hero + ONE muted complement */
  --accent-primary: #7c6af7;   /* electric violet — premium, not neon purple */
  --accent-glow:    rgba(124, 106, 247, 0.25);
  --accent-warm:    #f5a623;   /* amber for callouts/stats — warmth contrast */

  /* Text */
  --text-primary:   #f0f0f8;
  --text-secondary: #8888aa;
  --text-muted:     #44445a;

  /* Borders */
  --border-subtle:  rgba(255,255,255,0.06);
  --border-accent:  rgba(124,106,247,0.4);

  /* Never: pure #000000 bg, pure #ffffff text, #6c63ff purple */
}

/* Glow utility — applied sparingly on key CTAs */
.glow {
  box-shadow:
    0 0 0 1px var(--border-accent),
    0 0 24px var(--accent-glow),
    0 0 48px rgba(124,106,247,0.1);
}
```

---

## Motion Patterns

```css
/* Timing tokens */
:root {
  --ease-spring:  cubic-bezier(0.34, 1.56, 0.64, 1);  /* slight overshoot */
  --ease-smooth:  cubic-bezier(0.4, 0, 0.2, 1);
  --ease-out:     cubic-bezier(0, 0, 0.2, 1);
  --dur-fast:     120ms;
  --dur-base:     240ms;
  --dur-slide:    400ms;
}

/* Slide entrance — stagger children */
.slide-enter {
  animation: slide-up var(--dur-slide) var(--ease-out) both;
}
.slide-enter:nth-child(2) { animation-delay: 80ms; }
.slide-enter:nth-child(3) { animation-delay: 160ms; }
.slide-enter:nth-child(4) { animation-delay: 240ms; }

@keyframes slide-up {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Card hover — lift + glow, NOT scale */
.card {
  transition:
    transform var(--dur-base) var(--ease-spring),
    box-shadow var(--dur-base) var(--ease-smooth);
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.5), 0 0 20px var(--accent-glow);
}

/* Text reveal — clip-path wipe (premium feel) */
@keyframes reveal {
  from { clip-path: inset(0 100% 0 0); }
  to   { clip-path: inset(0 0% 0 0); }
}
.text-reveal {
  animation: reveal 600ms var(--ease-out) both;
}

/* Stat counter — short, precise */
@keyframes count-up {
  from { opacity: 0; transform: translateY(8px) scale(0.95); }
  to   { opacity: 1; transform: translateY(0) scale(1); }
}
```

---

## Image Placement Rules

```css
/* Rule 1 — Images anchor to edges, never float centered */
.slide-media-left {
  display: grid;
  grid-template-columns: 1fr 1.2fr;   /* content | image */
  gap: 0;
}
.slide-media-left img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  /* Bleed to slide edge, clip at content boundary */
  clip-path: inset(0 0 0 0 round 0 16px 16px 0);
}

/* Rule 2 — Full-bleed hero images get overlay scrim, not opacity */
.slide-hero-image {
  position: absolute;
  inset: 0;
  z-index: 0;
}
.slide-hero-image::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    135deg,
    rgba(10,10,15,0.95) 0%,
    rgba(10,10,15,0.6) 50%,
    rgba(10,10,15,0.3) 100%
  );
}

/* Rule 3 — Icon/screenshot callouts use masked glow containers */
.image-callout {
  border-radius: 12px;
  border: 1px solid var(--border-subtle);
  background: var(--bg-surface);
  padding: 1.5rem;
  position: relative;
  overflow: hidden;
}
.image-callout::before {
  content: '';
  position: absolute;
  top: -40%;
  left: 50%;
  width: 60%;
  height: 60%;
  background: var(--accent-glow);
  filter: blur(60px);
  transform: translateX(-50%);
  pointer-events: none;
}
```

---

## Card Density Rules

```css
/* Density tiers — pick ONE per slide, never mix */

/* Tier 1: Feature cards (2–3 per slide) */
.card-feature {
  padding: 2rem 2rem 1.5rem;
  border-radius: 16px;
  border: 1px solid var(--border-subtle);
  background: var(--bg-surface);
  min-height: 200px;
}

/* Tier 2: Stat cards (3–4 per slide) */
.card-stat {
  padding: 1.5rem;
  border-radius: 12px;
  border: 1px solid var(--border-subtle);
  background: var(--bg-surface);
  text-align: center;
}
.card-stat .stat-value {
  font-size: var(--text-2xl);
  font-weight: var(--weight-hero);
  color: var(--accent-primary);
  letter-spacing: var(--tracking-tight);
}

/* Tier 3: List rows (5–7 per slide max) */
.card-row {
  padding: 0.75rem 1rem;
  border-radius: 8px;
  border-left: 2px solid var(--border-accent);
  background: var(--bg-surface);
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

/* Spacing rule: gap = 1.5× card border-radius */
.card-grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem; }
.card-grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
.card-grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.75rem; }
```

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| `background: #6c63ff` or `#7c4dff` | Generic AI purple — seen on 10k+ Figma kits | Use `#7c6af7` (cooler, slightly desaturated) |
| `font-family: Inter` as primary | Overused; reads as Notion/Notion-adjacent | Lead with Space Grotesk or DM Sans |
| `opacity: 0.7` on hero images | Washes out, looks low-effort | Use layered gradient scrim instead |
| `box-shadow: 0 4px 6px rgba(0,0,0,0.1)` | Invisible on dark bg | Multiply shadow opacity 3–5×: `0 8px 32px rgba(0,0,0,0.6)` |
| Centered floating images | Breaks slide rhythm, looks slide-template | Bleed to edge or hard-anchor to grid |
| `transform: scale(1.05)` on hover | Feels cramped; content jumps | Use `translateY(-4px)` lift only |
| Full-slide bullet lists | Death by bullet — kills premium feel | Max 3 bullets; convert extras to visual cards |
| Gradient text on interactive elements | Clips on Chrome, breaks in Safari | `currentColor` on buttons/chips; gradient only on display text |
| Neon glow on all elements | Visual noise, no hierarchy | Reserve glow for ONE CTA or hero stat per slide |
| `animation-duration: 1s+` for entrance | Feels sluggish | Cap at 400ms; stagger in 80ms increments |

---

**Summary signal:** Dark + premium = restraint + precision. One accent, tight type, edge-anchored images, lift-not-scale hovers, and shadows 3× heavier than you think you need.
