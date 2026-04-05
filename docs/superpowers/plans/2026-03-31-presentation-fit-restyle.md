# AI-101 Presentation Fit Restyle Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restyle and compress the existing AI-101 deck into a premium navy-and-cyan presentation system that fits a desktop `16:9` viewport with no horizontal or vertical scroll while preserving all existing slide structure and copy.

**Architecture:** Keep the single-file presentation architecture in [index.html](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/index.html), tighten the deck through CSS-first changes, and leave the current slide order, markup structure, and runtime behaviors intact. Use [tests/test_presentation_design.py](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/tests/test_presentation_design.py) to lock new presentation-fit markers and hover coverage in place, then finish with browser verification against a local static server.

**Tech Stack:** Static HTML, CSS, vanilla JavaScript, Python `unittest`, local browser verification via `python -m http.server`

---

## File Map

- Modify [index.html](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/index.html)
  - Update root presentation tokens, desktop slide frame rules, and shared hover/focus language.
  - Tighten slide-specific layout selectors for slides `0` through `10`.
  - Preserve current runtime hooks, slide order, and existing copy.
- Modify [tests/test_presentation_design.py](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/tests/test_presentation_design.py)
  - Add regression coverage for the desktop presentation-fit frame, shared hover/focus coverage, slide-group compression rules, and mobile fallback behavior.

### Task 1: Lock the Desktop Presentation Frame and Shared Hover System

**Files:**
- Modify: [tests/test_presentation_design.py](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/tests/test_presentation_design.py)
- Modify: [index.html](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/index.html)

- [ ] **Step 1: Write the failing regression tests for the stage frame and shared hover language**

Add these methods inside `PresentationDesignTests` in [tests/test_presentation_design.py](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/tests/test_presentation_design.py):

```python
    def test_presentation_fit_tokens_lock_desktop_stage_frame(self):
        for marker in (
            "--deck-max-width:",
            "--slide-frame-max-height:",
            "--slide-padding-x:",
            "--slide-padding-top:",
            "--slide-padding-bottom:",
            "--hero-rainbow:",
            "--hover-lift:",
        ):
            self.assertIn(marker, INDEX_HTML)
        self.assertIn("max-height: var(--slide-frame-max-height);", INDEX_HTML)
        self.assertIn("height: var(--slide-frame-max-height);", INDEX_HTML)

    def test_shared_hover_focus_language_covers_major_components(self):
        for marker in (
            ".story-tag:hover",
            ".editorial-callout-block:hover",
            ".specialist-nav-btn:hover",
            ".specialist-dot:hover",
            ".prompt-asset-card:hover",
            ".callback-cta-card:hover",
            "transform: var(--hover-lift);",
        ):
            self.assertIn(marker, INDEX_HTML)
```

- [ ] **Step 2: Run the new tests to verify they fail**

Run:

```powershell
python -m unittest `
  tests.test_presentation_design.PresentationDesignTests.test_presentation_fit_tokens_lock_desktop_stage_frame `
  tests.test_presentation_design.PresentationDesignTests.test_shared_hover_focus_language_covers_major_components `
  -v
```

Expected:

```text
FAIL: test_presentation_fit_tokens_lock_desktop_stage_frame
FAIL: test_shared_hover_focus_language_covers_major_components
```

- [ ] **Step 3: Implement the desktop frame tokens, fixed-height slide shell, and shared hover/focus base**

Update the existing `:root`, `.slide`, `.slide-inner`, `.gradient-text`, and shared interactive selectors in [index.html](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/index.html) to include this code:

```css
        :root {
            --accent: #8bd6ff;
            --accent-strong: #53b3f8;
            --accent-warm: #d7a65a;
            --surface: rgba(11, 18, 30, 0.84);
            --surface-strong: rgba(12, 20, 33, 0.95);
            --surface-muted: rgba(18, 29, 45, 0.72);
            --surface-border: rgba(148, 163, 184, 0.18);
            --surface-border-strong: rgba(148, 163, 184, 0.34);
            --text: #f5f7fb;
            --text-dim: #aab7cb;
            --text-muted: #78869a;
            --text-bright: #ffffff;
            --danger: #ef4444;
            --success: #10b981;
            --warning: #f59e0b;
            --bg-top: #15314d;
            --bg-mid: #0b1423;
            --bg-base: #060a12;
            --viewport-height: 100vh;
            --safe-bottom: env(safe-area-inset-bottom, 0px);
            --nav-height: 72px;
            --deck-max-width: 1440px;
            --slide-frame-max-height: calc(var(--viewport-height) - var(--nav-height) - 44px);
            --slide-padding-x: clamp(28px, 3vw, 44px);
            --slide-padding-top: clamp(18px, 2vh, 28px);
            --slide-padding-bottom: calc(var(--nav-height) + clamp(14px, 2vh, 20px));
            --hero-rainbow: linear-gradient(135deg, #ffffff 0%, #8bd6ff 38%, #d7a65a 72%, #c084fc 100%);
            --hover-lift: translate3d(0, -4px, 0);
        }

        .slide {
            padding: var(--slide-padding-top) var(--slide-padding-x) var(--slide-padding-bottom);
            overflow: hidden;
        }

        .slide-inner {
            max-width: min(var(--deck-max-width), 100%);
            max-height: var(--slide-frame-max-height);
            height: var(--slide-frame-max-height);
            display: grid;
            align-content: center;
            gap: clamp(10px, 1.2vh, 16px);
        }

        .gradient-text {
            background: var(--hero-rainbow);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .story-tag,
        .editorial-callout-block,
        .specialist-nav-btn,
        .specialist-dot,
        .prompt-asset-card,
        .callback-cta-card {
            transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease, background-color 0.18s ease, filter 0.18s ease;
        }

        .story-tag:hover,
        .story-tag:focus-visible,
        .editorial-callout-block:hover,
        .editorial-callout-block:focus-within,
        .specialist-nav-btn:hover,
        .specialist-nav-btn:focus-visible,
        .specialist-dot:hover,
        .specialist-dot:focus-visible,
        .prompt-asset-card:hover,
        .prompt-asset-card:focus-within,
        .callback-cta-card:hover,
        .callback-cta-card:focus-within {
            transform: var(--hover-lift);
            border-color: rgba(139, 214, 255, 0.28);
            box-shadow: 0 18px 40px rgba(5, 11, 22, 0.32), 0 0 0 1px rgba(139, 214, 255, 0.14);
            filter: brightness(1.02);
        }
```

- [ ] **Step 4: Run the targeted tests to verify the new frame and hover guards pass**

Run:

```powershell
python -m unittest `
  tests.test_presentation_design.PresentationDesignTests.test_presentation_fit_tokens_lock_desktop_stage_frame `
  tests.test_presentation_design.PresentationDesignTests.test_shared_hover_focus_language_covers_major_components `
  -v
```

Expected:

```text
OK
```

- [ ] **Step 5: Commit the frame-system checkpoint**

Run:

```powershell
git add tests/test_presentation_design.py index.html
git commit -m "feat: add presentation-fit frame system"
```

### Task 2: Compress the Title, Story, Science, and Education Slides

**Files:**
- Modify: [tests/test_presentation_design.py](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/tests/test_presentation_design.py)
- Modify: [index.html](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/index.html)

- [ ] **Step 1: Write the failing regression test for the first slide group's compression rules**

Add this method inside `PresentationDesignTests` in [tests/test_presentation_design.py](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/tests/test_presentation_design.py):

```python
    def test_story_and_evidence_slides_get_density_fit_rules(self):
        for marker in (
            '.slide[data-slide="0"] {',
            'padding-top: 16px;',
            '.slide[data-slide="1"] .slide-inner {',
            'max-width: 1380px;',
            '.story-intro-layout {',
            'gap: 24px;',
            '.story-highlight-card {',
            'padding: 16px 18px;',
            '.science-timeline {',
            'margin-top: 20px;',
            '.node-bottom {',
            'padding: 20px 18px;',
            '.editorial-callout-shell {',
            '.editorial-callout-block {',
            'padding: 18px;',
        ):
            self.assertIn(marker, INDEX_HTML)
```

- [ ] **Step 2: Run the new slide-group test to verify failure**

Run:

```powershell
python -m unittest `
  tests.test_presentation_design.PresentationDesignTests.test_story_and_evidence_slides_get_density_fit_rules `
  -v
```

Expected:

```text
FAIL: test_story_and_evidence_slides_get_density_fit_rules
```

- [ ] **Step 3: Tighten slides `0` through `3` without changing their structure or copy**

Replace or extend the existing selectors in [index.html](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/index.html) with this code:

```css
        .slide[data-slide="0"] .slide-inner,
        .slide[data-slide="1"] .slide-inner,
        .slide[data-slide="2"] .slide-inner,
        .slide[data-slide="3"] .slide-inner {
            grid-template-rows: auto auto minmax(0, 1fr);
        }

        .slide[data-slide="0"] {
            padding-top: 16px;
        }

        .slide[data-slide="0"] .slide-inner {
            min-height: var(--slide-frame-max-height);
        }

        .hero-vortex-layer {
            inset: -24px -40px calc(var(--nav-height) * -1) -40px;
        }

        .slide[data-slide="1"] .slide-inner {
            max-width: 1380px;
        }

        .story-intro-layout {
            gap: 24px;
            margin-bottom: 20px;
        }

        .story-highlight {
            gap: 12px;
            margin-bottom: 12px;
        }

        .story-highlight-card {
            padding: 16px 18px;
            border-radius: 16px;
        }

        .story-tag-cloud {
            gap: 6px;
            margin-bottom: 10px;
        }

        .story-kicker {
            margin-top: 2px;
        }

        .science-timeline {
            align-items: stretch;
            margin-top: 20px;
            gap: 16px;
        }

        .node-top {
            margin-bottom: 18px;
            height: 32px;
        }

        .node-graphic {
            width: 88px;
            height: 88px;
            margin-bottom: 18px;
        }

        .node-bottom {
            padding: 20px 18px;
            max-width: 332px;
        }

        .timeline-node:nth-child(3) .node-bottom {
            margin-top: 24px;
        }

        .editorial-callout-shell {
            gap: 10px;
            margin-top: 2px;
        }

        .editorial-callout-block {
            padding: 18px;
            gap: 8px;
        }

        .editorial-stat {
            font-size: clamp(32px, 4.2vw, 54px);
        }

        .editorial-side-item {
            padding: 12px 14px;
            gap: 5px;
        }
```

- [ ] **Step 4: Run the targeted regression test for the first slide group**

Run:

```powershell
python -m unittest `
  tests.test_presentation_design.PresentationDesignTests.test_story_and_evidence_slides_get_density_fit_rules `
  -v
```

Expected:

```text
OK
```

- [ ] **Step 5: Commit the first slide-group compression pass**

Run:

```powershell
git add tests/test_presentation_design.py index.html
git commit -m "feat: tighten story and evidence slides"
```

### Task 3: Compress the Tool, Assistant, Specialist, Applications, and Prompt Slides

**Files:**
- Modify: [tests/test_presentation_design.py](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/tests/test_presentation_design.py)
- Modify: [index.html](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/index.html)

- [ ] **Step 1: Write the failing regression test for slides `4` through `8`**

Add this method inside `PresentationDesignTests` in [tests/test_presentation_design.py](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/tests/test_presentation_design.py):

```python
    def test_tool_and_prompt_slides_get_desktop_fit_guards(self):
        for marker in (
            '.slide[data-slide="4"] .slide-inner,',
            '.slide[data-slide="8"] .slide-inner {',
            '.orbital-diagram {',
            'min-height: 500px;',
            '.assistant-card {',
            'padding: 22px 24px;',
            '.specialist-carousel-track {',
            'min-height: 320px;',
            '.specialist-card {',
            'padding: 28px 30px;',
            '.use-case-cluster {',
            'padding: 18px 18px 16px;',
            '.slide[data-slide="8"] .prompt-example {',
            'padding: 10px 12px;',
        ):
            self.assertIn(marker, INDEX_HTML)
```

- [ ] **Step 2: Run the new slide-group test to verify failure**

Run:

```powershell
python -m unittest `
  tests.test_presentation_design.PresentationDesignTests.test_tool_and_prompt_slides_get_desktop_fit_guards `
  -v
```

Expected:

```text
FAIL: test_tool_and_prompt_slides_get_desktop_fit_guards
```

- [ ] **Step 3: Tighten slides `4` through `8` while preserving their existing interactions**

Update the existing selectors in [index.html](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/index.html) to include this code:

```css
        .slide[data-slide="4"] .slide-inner,
        .slide[data-slide="5"] .slide-inner,
        .slide[data-slide="6"] .slide-inner,
        .slide[data-slide="7"] .slide-inner,
        .slide[data-slide="8"] .slide-inner {
            grid-template-rows: auto auto minmax(0, 1fr);
        }

        .orbital-diagram {
            width: min(760px, 100%);
            min-height: 500px;
            margin: 0 auto;
        }

        .orbital-node {
            width: min(184px, 29vw);
            padding: 16px 16px 14px;
            border-radius: 20px;
        }

        .assistant-card-list {
            gap: 1px;
            border-radius: 24px;
            overflow: hidden;
        }

        .assistant-card {
            gap: 18px;
            padding: 22px 24px;
        }

        .assistant-card-orb {
            width: 76px;
            height: 76px;
        }

        .assistant-card-orb img {
            width: 44px;
            height: 44px;
        }

        .assistant-card-body p {
            font-size: 14px;
            line-height: 1.42;
        }

        .specialist-carousel {
            gap: 12px;
        }

        .specialist-carousel-track {
            min-height: 320px;
        }

        .specialist-card {
            grid-template-columns: 96px 1fr;
            gap: 18px;
            padding: 28px 30px;
        }

        .specialist-card-logo {
            width: 78px;
            height: 78px;
            border-radius: 18px;
        }

        .specialist-card-copy p {
            font-size: 18px;
            line-height: 1.5;
        }

        .specialist-carousel-controls {
            gap: 10px;
        }

        .specialist-nav-btn {
            min-width: 40px;
            min-height: 40px;
        }

        .use-case-groups {
            gap: 12px;
        }

        .use-case-cluster {
            padding: 18px 18px 16px;
            gap: 8px;
        }

        .cluster-list {
            gap: 6px;
        }

        .cluster-point {
            grid-template-columns: 44px 1fr;
            gap: 9px;
            padding: 8px 0;
        }

        .cluster-point .use-icon {
            width: 44px;
            height: 44px;
        }

        .slide[data-slide="8"] {
            padding: var(--slide-padding-top) var(--slide-padding-x) var(--slide-padding-bottom);
        }

        .slide[data-slide="8"] .slide-inner {
            max-width: 1320px;
        }

        .slide[data-slide="8"] .prompt-formula-grid {
            gap: 8px;
            margin-bottom: 6px;
        }

        .slide[data-slide="8"] .formula-block {
            padding: 8px 10px;
        }

        .slide[data-slide="8"] .prompt-example {
            margin-top: 6px;
            padding: 10px 12px;
        }

        .slide[data-slide="8"] .prompt-text {
            min-height: 36px;
            max-height: 92px;
        }

        .slide[data-slide="8"] .prompt-asset-card {
            width: 168px;
        }

        .slide[data-slide="8"] .prompt-asset-preview {
            height: clamp(54px, 7vh, 72px);
        }
```

- [ ] **Step 4: Run the targeted regression test for slides `4` through `8`**

Run:

```powershell
python -m unittest `
  tests.test_presentation_design.PresentationDesignTests.test_tool_and_prompt_slides_get_desktop_fit_guards `
  -v
```

Expected:

```text
OK
```

- [ ] **Step 5: Commit the second slide-group compression pass**

Run:

```powershell
git add tests/test_presentation_design.py index.html
git commit -m "feat: compress tool and prompt slides"
```

### Task 4: Finish the Safety and Close Slides, Restore Mobile Scroll, and Verify the Full Deck

**Files:**
- Modify: [tests/test_presentation_design.py](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/tests/test_presentation_design.py)
- Modify: [index.html](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/index.html)

- [ ] **Step 1: Write the failing regression test for the final slide group and mobile fallback**

Add this method inside `PresentationDesignTests` in [tests/test_presentation_design.py](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/tests/test_presentation_design.py):

```python
    def test_safety_close_and_mobile_rules_preserve_stage_fit(self):
        for marker in (
            '.slide[data-slide="9"] .slide-inner,',
            '.slide[data-slide="10"] .slide-inner {',
            '.safety-shield {',
            'min-height: 216px;',
            'padding: 42px 24px;',
            '.callback-montage {',
            'min-height: 560px;',
            '.callback-cta-card {',
            'width: min(980px, 100%);',
            '@media (max-width: 1180px) {',
            'overflow-y: auto;',
            'max-height: none;',
            'height: auto;',
        ):
            self.assertIn(marker, INDEX_HTML)
```

- [ ] **Step 2: Run the new test to verify failure**

Run:

```powershell
python -m unittest `
  tests.test_presentation_design.PresentationDesignTests.test_safety_close_and_mobile_rules_preserve_stage_fit `
  -v
```

Expected:

```text
FAIL: test_safety_close_and_mobile_rules_preserve_stage_fit
```

- [ ] **Step 3: Finish slides `9` and `10`, then restore scrolling only for the responsive breakpoints**

Update the existing safety, CTA, and media-query selectors in [index.html](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/index.html) to include this code:

```css
        .slide[data-slide="9"] .slide-inner,
        .slide[data-slide="10"] .slide-inner {
            grid-template-rows: auto auto minmax(0, 1fr);
        }

        .safety-shield-grid {
            gap: 12px;
        }

        .safety-shield {
            min-height: 216px;
            padding: 42px 24px;
            gap: 6px;
        }

        .safety-shield .safety-icon {
            width: 48px;
            height: 48px;
        }

        .callback-montage {
            min-height: 560px;
            padding: 24px;
            border-radius: 28px;
        }

        .callback-cta-card {
            width: min(980px, 100%);
            gap: 18px;
            padding: 24px 26px;
        }

        .callback-cta-card .cta-grid {
            gap: 14px;
        }

        .link-card.tonight-card {
            min-height: 0;
        }

        @media (max-width: 1180px) {
            .slide {
                overflow-y: auto;
            }

            .slide-inner {
                max-height: none;
                height: auto;
            }
        }
```

- [ ] **Step 4: Run the full regression suite and desktop browser verification**

Run:

```powershell
python -m unittest tests/test_presentation_design.py -v
```

Expected:

```text
Ran 20 tests

OK
```

Then start a local static server:

```powershell
python -m http.server 4173
```

Open [index.html](/E:/Downloads-Organized/Personal/Adam%20Gurski%20Professional%20AI%20profile/04_projects/ai-101/index.html) in a desktop browser at `http://127.0.0.1:4173/index.html` and visit slides `1`, `2`, `3`, `4`, `5`, `7`, `8`, `9`, and `10`. On each of those slides, run this console snippet:

```javascript
(() => {
  const slide = document.querySelector('.slide.active');
  return {
    slide: slide.dataset.slide,
    overflowY: slide.scrollHeight > slide.clientHeight + 1,
    overflowX: slide.scrollWidth > slide.clientWidth + 1,
  };
})()
```

Expected:

```text
{ overflowY: false, overflowX: false }
```

Then hover these selectors and confirm each gets lift plus brighter edge treatment without layout jitter:

```text
.story-highlight-card
.story-tag
.orbital-node
.assistant-card
.specialist-nav-btn
.use-case-cluster
.prompt-asset-card
.safety-shield
.callback-cta-card
```

- [ ] **Step 5: Commit the completed presentation-fit restyle**

Run:

```powershell
git add tests/test_presentation_design.py index.html
git commit -m "feat: finish presentation-fit restyle"
```
