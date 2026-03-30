# Prompt Anatomy System — AI-101 Deck (Agent 3 of 10)

---

## Color Legend & Reusable Template

| Tag | Color | Emoji | Purpose |
|-----|-------|-------|---------|
| **ROLE** | Blue | ?? | Who the AI should be |
| **TASK** | Orange | ?? | What action to perform |
| **CONTEXT** | Yellow | ?? | Background / situational info |
| **FORMAT** | Green | ?? | How to structure the output |
| **CONSTRAINTS** | Red | ?? | Limits, rules, exclusions |
| **OUTPUT** | Purple | ?? | The exact deliverable |

---

### Master Template

```
?? [ROLE: You are a ___]
?? [TASK: Your job is to ___]
?? [CONTEXT: The situation is ___]
?? [FORMAT: Structure your response as ___]
?? [CONSTRAINTS: Do not ___, keep it under ___, avoid ___]
?? [OUTPUT: Deliver ___]
```

**Assembled (copy-paste ready):**
```
You are a [ROLE]. [TASK]. [CONTEXT]. 
Structure your response as [FORMAT]. 
Do not [CONSTRAINTS]. 
Deliver [OUTPUT].
```

---

## 10 Industry Prompts — Fully Written + Annotated

---

### 1. Healthcare — Patient Intake Summary

**Full Prompt:**
> You are a clinical documentation specialist. Summarize the key health risks from the following patient intake form. The patient is a 58-year-old male presenting for a routine cardiac checkup with a history of hypertension and type 2 diabetes. Write a concise clinical note in SOAP format. Avoid speculation or diagnosis. Deliver a ready-to-paste clinical note under 200 words.

**Annotated Breakdown:**

| Token | Tag | Text |
|-------|-----|------|
| ?? ROLE | Blue | `a clinical documentation specialist` |
| ?? TASK | Orange | `Summarize the key health risks from the following patient intake form` |
| ?? CONTEXT | Yellow | `58-year-old male, routine cardiac checkup, history of hypertension and type 2 diabetes` |
| ?? FORMAT | Green | `SOAP format` |
| ?? CONSTRAINTS | Red | `Avoid speculation or diagnosis` |
| ?? OUTPUT | Purple | `Ready-to-paste clinical note under 200 words` |

---

### 2. Legal — Contract Risk Review

**Full Prompt:**
> You are a contract attorney specializing in SaaS agreements. Identify clauses that expose the client to unacceptable liability in the following vendor agreement. This is a $2M annual software subscription contract being reviewed before signature. Present findings as a bulleted risk register with severity ratings (High / Medium / Low). Do not offer legal advice or suggest language replacements. Deliver a prioritized risk register suitable for a non-lawyer executive.

**Annotated Breakdown:**

| Token | Tag | Text |
|-------|-----|------|
| ?? ROLE | Blue | `a contract attorney specializing in SaaS agreements` |
| ?? TASK | Orange | `Identify clauses that expose the client to unacceptable liability` |
| ?? CONTEXT | Yellow | `$2M annual software subscription contract, pre-signature review` |
| ?? FORMAT | Green | `Bulleted risk register with severity ratings (High / Medium / Low)` |
| ?? CONSTRAINTS | Red | `Do not offer legal advice or suggest language replacements` |
| ?? OUTPUT | Purple | `Prioritized risk register for a non-lawyer executive` |

---

### 3. Marketing — Campaign Brief

**Full Prompt:**
> You are a senior brand strategist at a performance marketing agency. Write a campaign brief for a product launch. The product is a plant-based protein bar targeting Gen Z fitness enthusiasts in North America; the launch budget is $150K over 8 weeks. Format the brief as a structured one-pager: Objective, Audience, Key Message, Channels, KPIs. Keep total length under 400 words and avoid industry jargon. Deliver a brief that a junior media buyer can execute immediately.

**Annotated Breakdown:**

| Token | Tag | Text |
|-------|-----|------|
| ?? ROLE | Blue | `a senior brand strategist at a performance marketing agency` |
| ?? TASK | Orange | `Write a campaign brief for a product launch` |
| ?? CONTEXT | Yellow | `Plant-based protein bar, Gen Z fitness, North America, $150K / 8-week budget` |
| ?? FORMAT | Green | `Structured one-pager: Objective, Audience, Key Message, Channels, KPIs` |
| ?? CONSTRAINTS | Red | `Under 400 words, avoid industry jargon` |
| ?? OUTPUT | Purple | `Actionable brief a junior media buyer can execute immediately` |

---

### 4. Software Engineering — Code Review

**Full Prompt:**
> You are a principal engineer with deep expertise in Python and distributed systems. Review the following async Python service for correctness, performance, and security issues. This service handles payment webhook events and is being promoted to production. Organize findings as a table: Issue | Severity | Line | Fix. Do not rewrite the code; flag issues only. Deliver a review table sorted by severity descending.

**Annotated Breakdown:**

| Token | Tag | Text |
|-------|-----|------|
| ?? ROLE | Blue | `a principal engineer with expertise in Python and distributed systems` |
| ?? TASK | Orange | `Review the async Python service for correctness, performance, and security issues` |
| ?? CONTEXT | Yellow | `Payment webhook handler being promoted to production` |
| ?? FORMAT | Green | `Table: Issue \| Severity \| Line \| Fix` |
| ?? CONSTRAINTS | Red | `Do not rewrite code; flag issues only` |
| ?? OUTPUT | Purple | `Review table sorted by severity descending` |

---

### 5. Education — Lesson Plan

**Full Prompt:**
> You are a high school STEM curriculum designer with expertise in project-based learning. Create a one-week lesson plan introducing machine learning concepts to 10th graders with no prior programming experience. The school uses Google Classroom and has a 50-minute period. Format as a daily grid: Day | Objective | Activity | Assessment. Keep vocabulary at a 9th-grade reading level; avoid math notation beyond algebra. Deliver a week-long plan a substitute teacher could facilitate.

**Annotated Breakdown:**

| Token | Tag | Text |
|-------|-----|------|
| ?? ROLE | Blue | `a high school STEM curriculum designer specializing in project-based learning` |
| ?? TASK | Orange | `Create a one-week lesson plan introducing machine learning concepts` |
| ?? CONTEXT | Yellow | `10th graders, no prior programming, Google Classroom, 50-minute periods` |
| ?? FORMAT | Green | `Daily grid: Day \| Objective \| Activity \| Assessment` |
| ?? CONSTRAINTS | Red | `9th-grade reading level; no math notation beyond algebra` |
| ?? OUTPUT | Purple | `Week-long plan a substitute teacher could facilitate` |

---

### 6. Finance — Earnings Call Summary

**Full Prompt:**
> You are a sell-side equity analyst covering the tech sector. Summarize the key takeaways from the following Q3 earnings call transcript for investors. This is a mid-cap SaaS company; the audience is institutional portfolio managers deciding whether to adjust their position. Use three sections: Beats/Misses, Management Tone, and Risks to Watch. Do not speculate on stock price movement. Deliver a 250-word memo ready to forward to a portfolio manager.

**Annotated Breakdown:**

| Token | Tag | Text |
|-------|-----|------|
| ?? ROLE | Blue | `a sell-side equity analyst covering the tech sector` |
| ?? TASK | Orange | `Summarize key takeaways from a Q3 earnings call transcript` |
| ?? CONTEXT | Yellow | `Mid-cap SaaS company; audience is institutional PMs deciding on position sizing` |
| ?? FORMAT | Green | `Three sections: Beats/Misses, Management Tone, Risks to Watch` |
| ?? CONSTRAINTS | Red | `Do not speculate on stock price movement` |
| ?? OUTPUT | Purple | `250-word memo ready to forward to a portfolio manager` |

---

### 7. Retail / E-Commerce — Product Description

**Full Prompt:**
> You are a conversion copywriter specializing in DTC e-commerce. Write a product detail page description for a new item. The product is a $280 handcrafted ceramic coffee mug targeted at home barista enthusiasts aged 30–45 who shop on Shopify. Format as: headline (max 8 words), 3-sentence hook, 4 feature bullets, 1 CTA sentence. Do not use words like "perfect," "amazing," or "game-changer." Deliver copy that can be pasted directly into a Shopify product page.

**Annotated Breakdown:**

| Token | Tag | Text |
|-------|-----|------|
| ?? ROLE | Blue | `a conversion copywriter specializing in DTC e-commerce` |
| ?? TASK | Orange | `Write a product detail page description` |
| ?? CONTEXT | Yellow | `$280 handcrafted ceramic mug, home barista audience 30–45, Shopify store` |
| ?? FORMAT | Green | `Headline (8 words max) ? 3-sentence hook ? 4 feature bullets ? 1 CTA` |
| ?? CONSTRAINTS | Red | `No "perfect," "amazing," or "game-changer"` |
| ?? OUTPUT | Purple | `Copy paste-ready for a Shopify product page` |

---

### 8. HR / Recruiting — Job Description

**Full Prompt:**
> You are a talent acquisition specialist with expertise in reducing hiring bias. Rewrite the following internal job description for a public job posting. This is a mid-level data engineer role at a Series B fintech startup; the hiring manager values practical skills over credentials. Structure as: About Us (2 sentences), What You'll Do (5 bullets), What You Bring (5 bullets), What We Offer (3 bullets). Remove any language that implies age, gender, or educational bias. Deliver a job post ready for LinkedIn and Greenhouse.

**Annotated Breakdown:**

| Token | Tag | Text |
|-------|-----|------|
| ?? ROLE | Blue | `a talent acquisition specialist specializing in reducing hiring bias` |
| ?? TASK | Orange | `Rewrite an internal job description for a public job posting` |
| ?? CONTEXT | Yellow | `Mid-level data engineer, Series B fintech, practical-skills-focused hiring manager` |
| ?? FORMAT | Green | `About Us ? What You'll Do ? What You Bring ? What We Offer` |
| ?? CONSTRAINTS | Red | `Remove language implying age, gender, or educational bias` |
| ?? OUTPUT | Purple | `Job post ready for LinkedIn and Greenhouse` |

---

### 9. Journalism — Article Pitch

**Full Prompt:**
> You are an investigative journalist and story editor at a digital news outlet. Write a story pitch memo for an editor. The story is about AI being used by landlords to automate lease denials in low-income neighborhoods; initial research shows three cities with documented patterns. Format as: Headline, 2-sentence lede, Why Now, Key Sources, Risks & Sensitivities. Pitch length must fit on one screen (under 350 words). Avoid any unverified claims. Deliver a pitch memo an editor could greenlight in a 15-minute meeting.

**Annotated Breakdown:**

| Token | Tag | Text |
|-------|-----|------|
| ?? ROLE | Blue | `an investigative journalist and story editor at a digital news outlet` |
| ?? TASK | Orange | `Write a story pitch memo for an editor` |
| ?? CONTEXT | Yellow | `AI-automated lease denials in low-income neighborhoods; 3 cities with documented patterns` |
| ?? FORMAT | Green | `Headline ? 2-sentence lede ? Why Now ? Key Sources ? Risks & Sensitivities` |
| ?? CONSTRAINTS | Red | `Under 350 words; no unverified claims` |
| ?? OUTPUT | Purple | `Pitch memo an editor could greenlight in a 15-minute meeting` |

---

### 10. Architecture / Design — Client Presentation

**Full Prompt:**
> You are an architect and technical writer specializing in sustainable residential design. Write the narrative section of a client presentation for a proposed home renovation. The project is a passive-house retrofit of a 1960s ranch-style home in Denver; the clients are eco-conscious empty nesters with a $400K renovation budget. Structure as: Design Vision (1 paragraph), Sustainability Strategy (3 bullets), Timeline Overview (phased table), Investment Summary (1 paragraph). Avoid technical jargon and keep the tone warm and aspirational, not academic. Deliver a narrative section a non-architect client will find inspiring and clear.

**Annotated Breakdown:**

| Token | Tag | Text |
|-------|-----|------|
| ?? ROLE | Blue | `an architect and technical writer specializing in sustainable residential design` |
| ?? TASK | Orange | `Write the narrative section of a client presentation for a home renovation` |
| ?? CONTEXT | Yellow | `Passive-house retrofit of 1960s ranch in Denver; eco-conscious empty nesters; $400K budget` |
| ?? FORMAT | Green | `Design Vision ? Sustainability Strategy ? Timeline Table ? Investment Summary` |
| ?? CONSTRAINTS | Red | `No jargon; tone warm and aspirational, not academic` |
| ?? OUTPUT | Purple | `Narrative section a non-architect client will find inspiring and clear` |

---

## Quick Reference Cheat Sheet (Slide-Ready)

```
+-------------------------------------------------------------+
¦              PROMPT ANATOMY — 6-PART SYSTEM                 ¦
+-----------------------------------------------------------¦
¦ ?? ROLE       ¦ "You are a [expert identity]"              ¦
¦ ?? TASK       ¦ "Your job is to [specific action]"         ¦
¦ ?? CONTEXT    ¦ "The situation: [who, what, why, where]"   ¦
¦ ?? FORMAT     ¦ "Structure as [template / layout]"         ¦
¦ ?? CONSTRAINTS¦ "Do not / Limit to / Avoid [rules]"        ¦
¦ ?? OUTPUT     ¦ "Deliver [exact artifact + audience]"      ¦
+-----------------------------------------------------------+

KEY INSIGHT: Every weak prompt is missing 2+ of these tokens.
Every strong prompt has all 6.
```

---

**Agent 3 deliverable complete.** This file contains:
- 1 color-coded master template
- 6-token legend with visual system
- 10 industry prompts fully written + annotated (Healthcare, Legal, Marketing, Engineering, Education, Finance, Retail, HR, Journalism, Architecture)
- 1 slide-ready ASCII cheat sheet
