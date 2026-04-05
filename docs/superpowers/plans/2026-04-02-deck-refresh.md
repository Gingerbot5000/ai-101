# AI-101 Deck Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Tighten the AI-101 deck from 11 to 9 slides, update content for 2026, fix hover interactions, and apply consistent visual polish.

**Architecture:** Single-file HTML presentation (`index.html`) with embedded CSS and JS. All changes are in one file. Slides use `data-slide` attributes and array-index-based JS navigation. Removing slides shifts all downstream indices, so the removal + reindex must happen in one atomic task.

**Tech Stack:** HTML, CSS, vanilla JS, p5.js for particle animations

**Spec:** `docs/superpowers/specs/2026-04-02-deck-refresh-design.md`

---

### Task 1: Fix Slide 2 (My Story) content

**Files:**
- Modify: `index.html:3914-3931` (story highlight cards)

- [ ] **Step 1: Update card 1 title and description**

Change line 3916-3917:
```html
<h3>Grammy-winner visuals</h3>
<p>Created a video used as a visual for Grammy Award winner Fatboy Slim.</p>
```

- [ ] **Step 2: Update card 2 title and description**

Change line 3920-3921:
```html
<h3>Built real business websites</h3>
<p>Designed and shipped several live sites for businesses — starting from zero web experience.</p>
```

- [ ] **Step 3: Update card 4 title and description**

Change line 3928-3929:
```html
<h3>Designed apps and games</h3>
<p>Built interactive applications and game prototypes that would have taken a full dev team before.</p>
```

- [ ] **Step 4: Verify in preview**

Navigate to slide 2 and confirm all four card titles read:
1. Grammy-winner visuals (green)
2. Built real business websites (cyan)
3. Started my own company (gold) — unchanged
4. Designed apps and games (purple)

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "fix(slide2): update story cards to match real accomplishments"
```

---

### Task 2: Add global subtle hover glow system

**Files:**
- Modify: `index.html` CSS section (~line 2823 for story cards, ~line 3203 for assistant cards)

- [ ] **Step 1: Replace story-highlight-card hover rule**

Find the existing `.story-highlight-card:hover` block (~line 2823) and replace with:
```css
.story-highlight-card:hover {
    background: rgba(255, 255, 255, 0.06);
    border-left-width: 4px;
    box-shadow:
        0 0 20px color-mix(in srgb, var(--card-accent) 25%, transparent),
        0 8px 32px rgba(0, 0, 0, 0.2),
        inset 0 0 0 1px color-mix(in srgb, var(--card-accent) 30%, transparent);
}
```

- [ ] **Step 2: Replace assistant-card hover rules**

Find the existing `.assistant-card:hover` block (~line 3203) and replace with:
```css
.assistant-card:hover,
.assistant-card:focus-visible {
    background: rgba(255, 255, 255, 0.06);
    box-shadow:
        0 0 20px rgba(139, 214, 255, 0.15),
        0 8px 32px rgba(0, 0, 0, 0.2),
        inset 0 0 0 1px rgba(139, 214, 255, 0.25);
}
.assistant-card:hover .assistant-card-orb,
.assistant-card:focus-visible .assistant-card-orb {
    border-color: rgba(139, 214, 255, 0.4);
    box-shadow: 0 0 24px rgba(139, 214, 255, 0.2), 0 16px 40px rgba(1, 5, 11, 0.28);
    transform: scale(1.06);
}
```

- [ ] **Step 3: Add hover glow to use-case-cluster cards (slide 6/Applications)**

Add after existing `.use-case-cluster` styles:
```css
.use-case-cluster:hover {
    background: rgba(255, 255, 255, 0.06);
    box-shadow:
        0 0 20px rgba(139, 214, 255, 0.1),
        0 8px 32px rgba(0, 0, 0, 0.2),
        inset 0 0 0 1px rgba(148, 163, 184, 0.15);
    transition: background 0.25s ease, box-shadow 0.25s ease;
}
```

- [ ] **Step 4: Add hover glow to safety shields (slide 8)**

Add after existing `.safety-shield` styles:
```css
.safety-shield:hover {
    filter: brightness(1.15);
    box-shadow: 0 0 24px rgba(139, 214, 255, 0.15);
    transition: filter 0.25s ease, box-shadow 0.25s ease;
}
```

- [ ] **Step 5: Add hover glow to tonight/closing cards (slide 9)**

Add after existing `.tonight-card` styles:
```css
.tonight-card:hover {
    background: rgba(255, 255, 255, 0.06);
    box-shadow:
        0 0 20px rgba(139, 214, 255, 0.12),
        0 8px 32px rgba(0, 0, 0, 0.2),
        inset 0 0 0 1px rgba(139, 214, 255, 0.2);
    transition: background 0.25s ease, box-shadow 0.25s ease;
}
```

- [ ] **Step 6: Verify hover effects in preview**

Hover over cards on slides 2, 4, 6, 8, 9 and confirm subtle glow appears on each.

- [ ] **Step 7: Commit**

```bash
git add index.html
git commit -m "feat: add consistent subtle hover glow across all interactive cards"
```

---

### Task 3: Add accent colors to Big Three cards (Slide 4)

**Files:**
- Modify: `index.html:4099-4134` (assistant card HTML)
- Modify: `index.html` CSS section (~line 3190-3220, assistant-card styles)

- [ ] **Step 1: Add CSS custom property support and colored left borders**

Add after the `.assistant-card` base rule:
```css
.assistant-card {
    border-left: 3px solid var(--card-accent, rgba(148, 163, 184, 0.18));
    transition: background 0.25s ease, box-shadow 0.25s ease, border-left-color 0.25s ease;
}
.assistant-card:hover,
.assistant-card:focus-visible {
    border-left-width: 4px;
    box-shadow:
        0 0 20px color-mix(in srgb, var(--card-accent, #8BD6FF) 25%, transparent),
        0 8px 32px rgba(0, 0, 0, 0.2),
        inset 0 0 0 1px color-mix(in srgb, var(--card-accent, #8BD6FF) 30%, transparent);
}
```

- [ ] **Step 2: Add --card-accent to each assistant card HTML**

On the ChatGPT card opening div (~line 4099):
```html
<div class="assistant-card is-active" data-assistant="chatgpt" role="button" tabindex="0" aria-label="Highlight ChatGPT" aria-pressed="true" style="--card-accent: #10B981;">
```

On the Claude card opening div (~line 4111):
```html
<div class="assistant-card" data-assistant="claude" role="button" tabindex="0" aria-label="Highlight Claude" aria-pressed="false" style="--card-accent: #8BD6FF;">
```

On the Gemini card opening div (~line 4123):
```html
<div class="assistant-card" data-assistant="gemini" role="button" tabindex="0" aria-label="Highlight Gemini" aria-pressed="false" style="--card-accent: #D7A65A;">
```

- [ ] **Step 3: Update Claude description to mention Claude Code**

Change line 4118:
```html
<p>Long-form writing, careful reasoning, coding with Claude Code, and structured professional work.</p>
```

- [ ] **Step 4: Update Gemini description to mention AI Studio**

Change line 4130:
```html
<p>Google ecosystem workflows, long-context tasks, multimodal assistance via AI Studio, and Search-connected answers.</p>
```

- [ ] **Step 5: Verify in preview**

Navigate to slide 4 (Big Three). Confirm colored left borders and hover glow on each card.

- [ ] **Step 6: Commit**

```bash
git add index.html
git commit -m "feat(slide4): add accent colors and update Big Three descriptions"
```

---

### Task 4: Add 4th breakthrough card (Math Proofs)

**Files:**
- Modify: `index.html:3953-4000` (science timeline HTML)
- Modify: `index.html` CSS — timeline node sizing to fit 4 across

- [ ] **Step 1: Compact timeline node CSS for 4-across layout**

Find the `.science-timeline` rule and update to ensure 4 columns:
```css
.science-timeline {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    position: relative;
}
```

Reduce `.node-bottom` padding and font sizes:
```css
.node-bottom {
    padding: 20px 16px;
}
.node-bottom .node-title {
    font-size: clamp(22px, 3vw, 36px);
}
.node-bottom p {
    font-size: clamp(13px, 1.3vw, 15px);
    line-height: 1.45;
}
.node-note {
    font-size: clamp(11px, 1.1vw, 13px);
}
```

- [ ] **Step 2: Add the 4th timeline node HTML**

Insert before the closing `</div>` of `.science-timeline` (~line 4000):
```html
<div class="timeline-node" style="--node-color: #ec4899;">
    <div class="node-top">
        <div class="node-badge">MATHEMATICS 2026</div>
    </div>
    <div class="node-graphic">
        <div class="core-glow"></div>
        <div id="p5-box-4" class="p5-canvas-container"></div>
    </div>
    <div class="node-bottom">
        <div class="node-title">Proof Assistant</div>
        <p>Terence Tao &mdash; widely considered the world&rsquo;s greatest living mathematician &mdash; now uses AI as a proof assistant, calling it &ldquo;ready for primetime.&rdquo;</p>
        <div class="node-note">The frontier moved from search to reasoning.</div>
    </div>
</div>
```

- [ ] **Step 3: Add p5.js math icon sketch**

Find the science icon sketch setup (search for `p5-box-1`) and add a 4th sketch for p5-box-4. Create a simple rotating summation symbol animation:
```javascript
if (document.getElementById('p5-box-4')) {
    new p5(function(p) {
        p.setup = function() {
            let c = p.createCanvas(80, 80);
            c.parent('p5-box-4');
            p.noFill();
            p.textAlign(p.CENTER, p.CENTER);
            p.textFont('JetBrains Mono');
        };
        p.draw = function() {
            p.clear();
            p.push();
            p.translate(40, 40);
            p.rotate(p.sin(p.frameCount * 0.02) * 0.15);
            p.stroke(236, 72, 153, 180);
            p.strokeWeight(2);
            // Sigma symbol paths
            p.beginShape();
            p.vertex(18, -22);
            p.vertex(-14, -22);
            p.vertex(4, 0);
            p.vertex(-14, 22);
            p.vertex(18, 22);
            p.endShape();
            // Glow dots
            let t = p.frameCount * 0.05;
            for (let i = 0; i < 5; i++) {
                let angle = t + i * p.TWO_PI / 5;
                let r = 28 + p.sin(angle * 2) * 4;
                p.noStroke();
                p.fill(236, 72, 153, 80 + p.sin(angle) * 40);
                p.circle(p.cos(angle) * r, p.sin(angle) * r, 3);
            }
            p.pop();
        };
    });
}
```

- [ ] **Step 4: Verify in preview**

Navigate to slide 3. Confirm 4 cards fit across, the math icon animates, and the Tao card content reads correctly.

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat(slide3): add math proofs breakthrough card with Tao example"
```

---

### Task 5: Remove slides 4, 5, 7 and reindex

This is the most complex task — removing 3 slides shifts all `data-slide` attributes and JS index references.

**Files:**
- Modify: `index.html` — HTML slide blocks, CSS `data-slide` selectors, JS slide controllers

- [ ] **Step 1: Delete Education Proof slide HTML**

Remove the entire block from `<!-- ===== SLIDE 4: EDUCATION PROOF ===== -->` through the closing `</div>` (~lines 4004-4044).

- [ ] **Step 2: Delete Tool Map slide HTML**

Remove the entire block from `<!-- ===== SLIDE 5: TOOL MAP ===== -->` through the closing `</div>` (~lines 4046-4088).

- [ ] **Step 3: Delete Specialists slide HTML**

Remove the entire block from `<!-- ===== SLIDE 7: SPECIALISTS ===== -->` through the closing `</div>` (~lines 4140-4157).

- [ ] **Step 4: Reindex remaining slide data-slide attributes**

After removal, the remaining slides and their new indices:

| Old data-slide | Slide | New data-slide |
|---|---|---|
| 0 | Title | 0 |
| 1 | My Story | 1 |
| 2 | Breakthroughs | 2 |
| 5 | Big Three | 3 |
| (new) | Additional AI Tools | 4 |
| 7 | Applications | 5 |
| 8 | Prompt Lab | 6 |
| 9 | Safety | 7 |
| 10 | Closing | 8 |

Update every `data-slide="X"` attribute on the remaining slide divs to match the new indices.

- [ ] **Step 5: Update slide-number labels**

Update the slide-number text inside each slide to match new order:
- Breakthroughs: `02 / Science Proof` (keep)
- Big Three: `03 / Core Assistants`
- Additional AI Tools: `04 / Tools`
- Applications: `05 / Applications`
- Prompt Lab: `06 / Prompt Lab`
- Safety: `07 / Safety`
- Closing: `08 / Tonight`

- [ ] **Step 6: Update CSS data-slide selectors**

Search for all `[data-slide="X"]` in CSS and update to new indices. Key mappings:
- `[data-slide="8"]` (Prompt Lab styles) → `[data-slide="6"]`
- `[data-slide="0"]` → `[data-slide="0"]` (no change)
- `[data-slide="1"]` → `[data-slide="1"]` (no change)
- `[data-slide="2"]` → `[data-slide="2"]` (no change)
- `[data-slide="3"]` → remove (education proof deleted)
- `[data-slide="4"]` → remove (tool map deleted)
- `[data-slide="5"]` → `[data-slide="3"]`
- `[data-slide="6"]` → remove (specialists deleted)
- `[data-slide="7"]` → `[data-slide="5"]`
- `[data-slide="9"]` → `[data-slide="7"]`
- `[data-slide="10"]` → `[data-slide="8"]`

- [ ] **Step 7: Update JS slide controller registrations**

Find `registerSlideController` calls and update:
- `registerSlideController(0, ...)` → keep as 0 (title/hero vortex)
- `registerSlideController(5, ...)` → change to `registerSlideController(3, ...)` (Big Three constellation)
- `registerSlideController(6, ...)` → remove entirely (specialists carousel deleted)

- [ ] **Step 8: Remove dead JS code for deleted slides**

Remove the specialist carousel JS: search for `specialistCarousel`, `startSpecialistAutoplay`, `stopSpecialistAutoplay`, `specialistPrevBtn`, `specialistNextBtn` and remove all related code blocks.

Remove orbital diagram JS if any: search for `orbital-node` click handlers and remove.

Remove education proof animation code if any: search for `editorial-callout` animation JS and remove.

- [ ] **Step 9: Remove dead CSS for deleted slides**

Remove CSS rules targeting deleted slide elements:
- `.orbital-diagram`, `.orbital-rings`, `.orbital-ring`, `.orbital-core`, `.orbital-node` and all variants
- `.specialist-carousel`, `.specialist-carousel-track`, `.specialist-nav-btn`, `.specialist-carousel-dots` and all variants
- `.editorial-callout-shell-education` and related
- Animation rules referencing `[data-slide="3"]`, `[data-slide="4"]`, `[data-slide="6"]` (old indices)

- [ ] **Step 10: Verify in preview**

Reload and navigate through all 8 slides (before adding the new tools slide). Confirm:
- Navigation works (Next/Prev, dots, arrow keys)
- Slide counter shows "X / 8" (will be 9 after tools slide added)
- No console errors
- Hero vortex animation still works on slide 0
- Constellation animation still works on slide 3 (Big Three)
- Prompt Lab still functional on slide 6

- [ ] **Step 11: Commit**

```bash
git add index.html
git commit -m "refactor: remove education, tool map, specialists slides and reindex deck to 8 slides"
```

---

### Task 6: Create new Additional AI Tools slide (Slide 4)

**Files:**
- Modify: `index.html` — insert new HTML slide block + CSS styles

- [ ] **Step 1: Add CSS for tool wall**

Add to the CSS section:
```css
/* ===== TOOL WALL (Slide 4) ===== */
.tool-wall {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
    gap: 20px;
    max-width: 900px;
    margin: 0 auto;
    padding: 8px 0;
}
.tool-tile {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    padding: 16px 8px;
    border-radius: 14px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(148, 163, 184, 0.1);
    cursor: pointer;
    transition: background 0.25s ease, box-shadow 0.25s ease, transform 0.25s ease;
    position: relative;
}
.tool-tile:hover {
    background: rgba(255, 255, 255, 0.06);
    box-shadow:
        0 0 20px rgba(139, 214, 255, 0.15),
        0 8px 32px rgba(0, 0, 0, 0.2),
        inset 0 0 0 1px rgba(139, 214, 255, 0.25);
    transform: translateY(-2px);
}
.tool-tile-icon {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    background: rgba(139, 214, 255, 0.08);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: 700;
    font-family: 'Space Grotesk', sans-serif;
    color: var(--accent-primary, #8BD6FF);
    border: 1px solid rgba(139, 214, 255, 0.15);
}
.tool-tile-name {
    font-size: 12px;
    font-family: 'JetBrains Mono', monospace;
    color: var(--text-dim, #AAB7CB);
    text-align: center;
    line-height: 1.3;
}
.tool-tile-category {
    font-size: 9px;
    font-family: 'JetBrains Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-muted, #78869A);
}

/* Hover info card */
.tool-info-card {
    position: fixed;
    z-index: 100;
    padding: 16px 20px;
    border-radius: 14px;
    background: rgba(15, 23, 42, 0.95);
    border: 1px solid rgba(139, 214, 255, 0.2);
    box-shadow: 0 0 20px rgba(139, 214, 255, 0.1), 0 16px 48px rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(16px);
    pointer-events: none;
    opacity: 0;
    transform: translateY(4px);
    transition: opacity 0.2s ease, transform 0.2s ease;
    max-width: 280px;
}
.tool-info-card.visible {
    opacity: 1;
    transform: translateY(0);
    pointer-events: auto;
}
.tool-info-card h4 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 16px;
    font-weight: 600;
    color: #fff;
    margin-bottom: 4px;
}
.tool-info-card p {
    font-family: 'Instrument Sans', sans-serif;
    font-size: 14px;
    color: #AAB7CB;
    line-height: 1.45;
    margin-bottom: 8px;
}
.tool-info-card a {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #8BD6FF;
    text-decoration: none;
}
.tool-info-card a:hover {
    text-decoration: underline;
}
```

- [ ] **Step 2: Add the slide HTML**

Insert after the Big Three slide (new data-slide="4"), before the Applications slide:
```html
<!-- ===== SLIDE 5: ADDITIONAL AI TOOLS ===== -->
<div class="slide" data-slide="4">
    <div class="slide-inner">
        <div class="slide-number">04 / Tools</div>
        <h2 style="margin-bottom: 8px;">Additional AI Tools</h2>
        <p class="subtitle" style="margin-bottom: 20px; max-width: 42ch;">The ecosystem is wide. These are worth knowing.</p>
        <div class="tool-wall" id="toolWall"></div>
        <div class="tool-info-card" id="toolInfoCard">
            <h4 id="toolInfoName"></h4>
            <p id="toolInfoDesc"></p>
            <a id="toolInfoLink" href="#" target="_blank" rel="noopener noreferrer">Visit &rarr;</a>
        </div>
    </div>
</div>
```

- [ ] **Step 3: Add tool data and render JS**

Add to the JS section:
```javascript
const toolWallData = [
    { name: "Suno", cat: "Music", letter: "S", color: "#f472b6", desc: "Generate full songs from a text prompt — vocals, instruments, and production included.", url: "https://suno.ai" },
    { name: "ElevenLabs", cat: "Music", letter: "XI", color: "#a78bfa", desc: "Realistic AI voice generation, cloning, and text-to-speech for any project.", url: "https://elevenlabs.io" },
    { name: "Haiggsfield", cat: "Video", letter: "H", color: "#f59e0b", desc: "AI video generation with character consistency and cinematic control.", url: "https://haiggsfield.ai" },
    { name: "Krea", cat: "Video", letter: "K", color: "#34d399", desc: "Real-time AI image and video generation with creative controls.", url: "https://krea.ai" },
    { name: "Freepik", cat: "Image", letter: "F", color: "#38bdf8", desc: "AI-powered image generation and editing built into a design asset library.", url: "https://freepik.com" },
    { name: "Stable Diffusion", cat: "Image", letter: "SD", color: "#c084fc", desc: "Open-source image generation you can run locally or in the cloud.", url: "https://stability.ai" },
    { name: "NotebookLM", cat: "Research", letter: "NB", color: "#60a5fa", desc: "Upload your own documents and get an AI research assistant grounded in your sources.", url: "https://notebooklm.google.com" },
    { name: "Perplexity", cat: "Research", letter: "P", color: "#2dd4bf", desc: "Direct answers with citations and live web search — sourced, not guessed.", url: "https://perplexity.ai" },
    { name: "Claude Code", cat: "Code", letter: "CC", color: "#8BD6FF", desc: "Anthropic's CLI for agentic coding — plans, edits, and ships code from your terminal.", url: "https://claude.ai" },
    { name: "Codex", cat: "Code", letter: "CX", color: "#10B981", desc: "OpenAI's cloud coding agent — give it a task and it works autonomously in a sandbox.", url: "https://openai.com" },
    { name: "AntiGravity", cat: "Code", letter: "AG", color: "#f59e0b", desc: "Google's code harness for building and deploying with AI assistance.", url: "https://google.com" },
    { name: "Qwen 3.5", cat: "Open Source", letter: "Q", color: "#818cf8", desc: "Alibaba's open-source model family — competitive performance you can self-host.", url: "https://huggingface.co/Qwen" },
    { name: "DeepSeek", cat: "Open Source", letter: "DS", color: "#fb923c", desc: "High-performance open-source reasoning model from DeepSeek.", url: "https://deepseek.com" }
];

function renderToolWall() {
    const wall = document.getElementById('toolWall');
    if (!wall) return;
    wall.innerHTML = '';
    toolWallData.forEach((tool, i) => {
        const tile = document.createElement('div');
        tile.className = 'tool-tile';
        tile.dataset.toolIndex = i;
        tile.innerHTML = `
            <div class="tool-tile-icon" style="color: ${tool.color}; border-color: ${tool.color}33; background: ${tool.color}12;">${tool.letter}</div>
            <div class="tool-tile-name">${tool.name}</div>
            <div class="tool-tile-category">${tool.cat}</div>
        `;
        tile.addEventListener('mouseenter', (e) => showToolInfo(e, tool));
        tile.addEventListener('mouseleave', hideToolInfo);
        wall.appendChild(tile);
    });
}

function showToolInfo(e, tool) {
    const card = document.getElementById('toolInfoCard');
    if (!card) return;
    document.getElementById('toolInfoName').textContent = tool.name;
    document.getElementById('toolInfoDesc').textContent = tool.desc;
    const link = document.getElementById('toolInfoLink');
    link.href = tool.url;
    link.textContent = 'Visit ' + tool.name + ' →';

    const rect = e.currentTarget.getBoundingClientRect();
    let left = rect.right + 12;
    let top = rect.top;

    // Flip left if near right edge
    if (left + 280 > window.innerWidth) {
        left = rect.left - 292;
    }
    // Keep in viewport vertically
    if (top + 120 > window.innerHeight) {
        top = window.innerHeight - 130;
    }

    card.style.left = left + 'px';
    card.style.top = top + 'px';
    card.classList.add('visible');
}

function hideToolInfo() {
    const card = document.getElementById('toolInfoCard');
    if (card) card.classList.remove('visible');
}

renderToolWall();
```

- [ ] **Step 4: Update Applications slide index**

Since this new slide is data-slide="4", bump Applications to data-slide="5", Prompt Lab to 6, Safety to 7, Closing to 8. (If Task 5 already handled this, just verify the new slide is inserted at position 4 in the DOM order.)

- [ ] **Step 5: Verify in preview**

Navigate to slide 5 (Additional AI Tools). Confirm:
- 13 tool tiles render in a grid
- Hovering shows info card with name, description, and link
- Info card positions correctly (flips when near edge)
- No overlap with slide edges

- [ ] **Step 6: Commit**

```bash
git add index.html
git commit -m "feat: add Additional AI Tools slide with hover info cards"
```

---

### Task 7: Global text sizing and spacing polish

**Files:**
- Modify: `index.html` CSS section

- [ ] **Step 1: Bump global body text minimum**

Find the base `.slide p` or body text rule and ensure minimum size:
```css
.slide p,
.subtitle {
    font-size: clamp(16px, 1.6vw, 20px);
}
```

If this conflicts with specific slides that need smaller text (like Prompt Lab), add overrides for those slides.

- [ ] **Step 2: Ensure card title minimum sizing**

```css
.story-highlight-card h3,
.assistant-card-body h3,
.use-case-cluster h3,
.node-title {
    font-size: clamp(17px, 1.8vw, 22px);
}
```

- [ ] **Step 3: Fix closing slide text overflow**

Add to slide 8 (closing) styles:
```css
.callback-cta-card {
    max-width: 100%;
    overflow: hidden;
}
.callback-cta-card h2,
.callback-cta-card .subtitle {
    max-width: 100%;
    overflow-wrap: break-word;
}
```

- [ ] **Step 4: Update title badge date**

Change the title badge text from "Updated March 28, 2026" to "Updated April 2, 2026".

- [ ] **Step 5: Verify all slides fit 1280x800**

Navigate through every slide at 1280x800 viewport. Confirm no overflow, no clipping, no overlap.

- [ ] **Step 6: Commit**

```bash
git add index.html
git commit -m "style: global text sizing, spacing polish, and viewport fit pass"
```

---

### Task 8: Final verification and cleanup

**Files:**
- Modify: `index.html` (any remaining issues)

- [ ] **Step 1: Full slide-through test**

Navigate through all 9 slides in order using Next button. Confirm:
- Transitions work smoothly
- Dot indicators match (9 dots)
- Slide counter shows "X / 9"
- No console errors

- [ ] **Step 2: Test keyboard navigation**

Use left/right arrow keys to navigate through all slides.

- [ ] **Step 3: Test hover interactions on every slide**

Verify hover glow works on:
- Slide 2: story highlight cards
- Slide 3: breakthrough cards (if hoverable)
- Slide 4: Big Three assistant cards
- Slide 5: tool wall tiles + info card popup
- Slide 6: application category cards
- Slide 8: safety shields
- Slide 9: tonight action cards

- [ ] **Step 4: Fix any remaining issues found**

Address anything discovered during testing.

- [ ] **Step 5: Final commit**

```bash
git add index.html
git commit -m "chore: final deck refresh verification and cleanup"
```
