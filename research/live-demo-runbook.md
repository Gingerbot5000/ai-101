# AI-101 Live Demo Runbook (Reconstruction v2)

## Session Profile
- Runtime target: 30-40 minutes
- Format: 65% demos, 35% concept bridges
- Audience: mixed non-technical stakeholders (business, creative, entrepreneurial, career, personal productivity)
- Primary stack: Google-first (Gemini + NotebookLM + video workflow)
- Backup stack: ChatGPT + Claude

## Required Tabs and Assets (Open Before Start)
1. `04_projects/ai-101/index.html`
2. `https://gemini.google.com`
3. Creative pipeline tools (image refinement and video generation)
4. `https://notebooklm.google.com`
5. `https://chatgpt.com` (backup)
6. `https://claude.ai` (backup)
7. Local fallback folder with pre-captured outputs for each anchor demo (`04_projects/ai-101/research/fallback-pack/README.md`)

## Flow and Timing

### 1) Myth Reset + Framing (2-3 min)
- Slide module: `myth-reset`
- Cue line: "One concept, one proof. Every section gets a live demonstration."
- Goal: reduce fear + hype at the same time.

### 2) Anchor Demo 1: Gemini Canvas Website Build (7 min)
- Slide module: `demo-hook`
- Participation Moment 1: ask audience to choose business goal (leads/event/product launch).
- Prompt (from `#demo-gemini-canvas`):
```text
You are a web designer working for a local business owner.
I am uploading a product photo. Build a one-page responsive website around this product.
Required sections: hero, product story, three benefits, customer proof, call-to-action, contact.
Design constraints: high readability, strong contrast, mobile first, clear buy or quote button.
Output: editable page structure and suggested iteration prompts for improvements.
```
- Transition: "Now that you saw creation, here's the model difference behind it."
- Fallback (under 10 seconds): open pre-captured output `fallback-gemini-site-v1` and narrate same steps.

### 3) Concept Bridge 1: Discriminative vs Generative (2 min)
- Slide module: `concept-bridge-1`
- Analogy lock: archivist (classifies) vs artist (creates).
- Constraint: do not introduce second analogy on this slide.

### 4) Anchor Demo 2: Creative Pipeline (8-10 min)
- Slide module: `creative-pipeline`
- Participation Moment 2: vote on visual direction (premium, playful, bold).
- Prompt A (image direction, from `#demo-image-refine`):
```text
You are a creative director for a product commercial.
Using this uploaded product photo, produce three visual directions:
1) premium cinematic, 2) playful social, 3) bold energetic.
For each direction include: color palette, lighting style, camera angle, and one hero composition instruction.
```
- Prompt B (animation storyboard, from `#demo-veo-sequence`):
```text
Create a short product animation concept from a start frame and end frame.
Goal: show the product transforming into final branded hero shot.
Output: 6-scene storyboard with timing, motion cues, text overlay ideas, and CTA end card.
```
- Transition: "It looks magical, but the mechanics are still mathematical."
- Fallback: show `fallback-creative-pipeline-v1` assets and continue timing.

### 5) Concept Bridge 2: Latent Space + Diffusion (2 min)
- Slide module: `concept-bridge-2`
- Analogy lock: map navigation + noise removal.
- Constraint: no anthropomorphic "AI thinks like a brain" language.

### 6) Anchor Demo 3: NotebookLM Transformation (6-7 min)
- Slide module: `knowledge-transformation`
- Prompt (from `#demo-notebooklm`):
```text
Use these uploaded business materials as the only source of truth.
Create three outputs:
1) a 3-minute audio-style briefing,
2) a concise mind map of core themes,
3) a 7-slide outline for a stakeholder update.
Prioritize clarity, not jargon.
```
- Show outputs in order: audio > map > slides.
- Fallback: pre-captured versions for each output type.

### 7) Anchor Demo 4: Utility Sprint (5-6 min)
- Slide module: `utility-sprint`
- Participation Moment 3: pick first scenario to run.
- Scenarios in deck prompt carousel:
  - Job seeker plan
  - Budget/life admin plan
  - Build-for-fun mini-game concept
- Operator rule: run one scenario deeply, summarize the other two quickly.
- Fallback: pre-captured outputs tied to each scenario.

### 8) Responsible Use Layer (3-4 min)
- Slide module: `responsible-use`
- Emphasize named incidents and mitigation behavior, not fear language.
- Required close phrase: "Human review is a feature, not a failure of AI."

### 9) Practical Close (2 min)
- Slide module: `close`
- Ask attendees to leave with one concrete "tonight action".
- Keep takeaway as slide PDF only.

## Reliability Rules (Live-First)
- If first tool stalls for >8 seconds, switch to backup tool immediately.
- If output quality is poor, run one refinement prompt instead of restarting demo.
- If network fails, switch to fallback artifacts and narrate as planned.

## Final Rehearsal Gate (Do Before Going On Stage)
1. Full run finishes in 30-40 minutes.
2. All 4 anchor demos have tested fallback files.
3. All 3 participation moments are pre-scripted.
4. Citation links open from slide 8 and close slide.
5. Tool capability statements are re-checked against current official docs.
