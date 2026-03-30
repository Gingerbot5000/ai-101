# AI-101 Live Browser Presentation Polish Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the HTML presentation from polished demo deck to a professional keynote-style live browser presentation.

**Architecture:** Keep the existing single-file deck structure, but replace its visual system at the token and component level. Use a lightweight regression test to lock the new typography, palette, and presentation markers in place.

**Tech Stack:** Static HTML, CSS, JavaScript, Python `unittest`, Playwright browser verification

---

### Task 1: Lock the Design Direction

**Files:**
- Create: `tests/test_presentation_design.py`
- Modify: `index.html`

- [ ] **Step 1: Write failing regression tests for the new design system**
- [ ] **Step 2: Run `python -m unittest tests/test_presentation_design.py` and confirm failure**
- [ ] **Step 3: Implement the design tokens, font system, and professional presentation markers in `index.html`**
- [ ] **Step 4: Re-run `python -m unittest tests/test_presentation_design.py` and confirm pass**

### Task 2: Upgrade Presentation Surfaces

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Restyle the hero, card surfaces, badges, prompt demo panel, and navigation chrome**
- [ ] **Step 2: Remove decorative emoji markers that make the deck feel less professional**
- [ ] **Step 3: Re-open the deck in browser and capture before/after screenshots for key slides**

### Task 3: Document the System

**Files:**
- Create: `DESIGN.md`
- Create: `CLAUDE.md`

- [ ] **Step 1: Write the final deck design system to `DESIGN.md`**
- [ ] **Step 2: Add the design-system handoff note to `CLAUDE.md`**
- [ ] **Step 3: Verify the deck renders with the new system at desktop and mobile widths**
