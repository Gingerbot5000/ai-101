# AI-101 Vertical Prompt Packs
*Agent 9/10 — 75 prompts across 5 audiences × 5 topics × 3 tiers*

---

## Audience 1: Job Seeker

### Topic 1 — Resume Bullet Writing

**Beginner**
> "Rewrite this job duty as a resume bullet: [paste duty]. Use an action verb and keep it under 15 words."

*Expected output:* Single bullet starting with past-tense verb (e.g., "Reduced invoice processing time by 30% by automating weekly reports.")

---

**Intermediate**
> "I was a [job title] at [company] for [X years]. Here are 3 duties I performed: [list]. Rewrite each as a strong resume bullet using the formula: Action verb + task + measurable result. If I don't have numbers, suggest plausible ranges I can verify."

*Expected output:* 3 revised bullets with inline notes like `[verify: actual % may vary]` where estimates are used.

---

**Power**
> "Act as a senior resume writer specializing in [industry]. Here is my full work history: [paste]. My target role is [job title] at [company type]. Audit every bullet for: weak verbs, missing metrics, and relevance to the target role. Output a table: Original | Revised | Reason for change. Flag any bullet I should cut entirely."

*Expected output:* Markdown table with 3 columns + a "Cut" section listing low-value bullets with rationale.

---

### Topic 2 — Interview Prep

**Beginner**
> "Give me 5 common interview questions for a [job title] role with a one-sentence tip for answering each."

*Expected output:* Numbered list of 5 Q&A pairs, each under 3 lines.

---

**Intermediate**
> "I have an interview for [job title] at [company]. The job description says they want: [paste 3–5 requirements]. Generate 8 likely interview questions based on those requirements. For each, write a STAR-method answer outline using my background: [2–3 sentences about experience]."

*Expected output:* 8 questions, each followed by a STAR skeleton (Situation / Task / Action / Result) with placeholder prompts filled from the provided background.

---

**Power**
> "Run a mock interview with me for a [job title] role. Ask me one question at a time. After I answer, score my response on: relevance (1–5), specificity (1–5), confidence language (1–5). Give a one-line coaching note. Then ask the next question. Start now."

*Expected output:* Conversational turn-by-turn format. Each AI turn = next question OR scored feedback block before the next question.

---

### Topic 3 — Cover Letter

**Beginner**
> "Write a short cover letter opening paragraph for a [job title] position. My name is [name] and I have [X years] of experience in [field]."

*Expected output:* 3–4 sentence paragraph, professional tone, no filler phrases like "I am writing to apply."

---

**Intermediate**
> "Write a full cover letter for this job posting: [paste JD]. My resume summary: [paste]. Match my experience to their stated requirements. Keep it under 300 words. Use a direct, confident tone — no clichés."

*Expected output:* 3-paragraph cover letter (hook ? match ? close) with a word count footer.

---

**Power**
> "Analyze this job description: [paste]. Extract the top 5 competencies they're hiring for. Then write a cover letter that mirrors their language exactly, embeds a specific achievement for each competency, and ends with a low-pressure CTA. Flag any competency I haven't addressed with a `[GAP — add evidence]` marker."

*Expected output:* Cover letter with inline `[GAP]` markers + a separate "Competency Map" table showing JD requirement ? bullet used.

---

### Topic 4 — LinkedIn Profile

**Beginner**
> "Write a LinkedIn headline for someone who is a [job title] looking for work in [field]. Make it specific and keyword-rich, under 220 characters."

*Expected output:* 2–3 headline variants with character counts.

---

**Intermediate**
> "Rewrite my LinkedIn About section to attract [target role] opportunities. Current version: [paste]. My key achievements: [list 3]. Target industries: [list]. Use first person, lead with value, under 300 words."

*Expected output:* Revised About section with a "hooks" breakdown — first 3 lines optimized for preview cutoff.

---

**Power**
> "Audit my full LinkedIn profile for a job search targeting [role] at [company type]. Profile sections: [paste headline, about, top 3 experience entries]. Score each section 1–10 on keyword density, recruiter appeal, and proof of impact. Output a priority fix list ranked by ROI."

*Expected output:* Scored table by section + ordered action list (e.g., "Fix 1: Headline — add 'open to work' signal keyword").

---

### Topic 5 — Salary Negotiation

**Beginner**
> "What is a polite way to respond when an employer asks 'What are your salary expectations?' Give me 2–3 example sentences."

*Expected output:* 2–3 short scripts with a note on when to use each.

---

**Intermediate**
> "I received a job offer of $[X] for a [job title] in [city]. My research suggests the market rate is $[Y]–$[Z]. Write a negotiation email that: thanks them, expresses enthusiasm, counters at $[target], and provides 2 brief justifications. Keep it under 150 words."

*Expected output:* Ready-to-send email draft with subject line + 2 justification notes labeled for easy swap.

---

**Power**
> "Coach me through a salary negotiation conversation. I'll play myself; you play a hiring manager who starts firm at $[X] and has budget to $[Y] (don't reveal this). Debrief after 5 exchanges: what leverage I used, what I missed, and the final outcome. Start the scene."

*Expected output:* Role-play transcript (labeled turns) + a post-conversation debrief with scores on anchoring, BATNA use, and tone.

---

## Audience 2: Small Business Owner

### Topic 1 — Marketing Copy

**Beginner**
> "Write a 3-sentence Facebook ad for my [type of business]. My offer: [offer]. Target customer: [description]."

*Expected output:* 3-sentence ad with a hook, benefit, and CTA. Character count included.

---

**Intermediate**
> "Create 5 variations of a Google ad headline for [business name], selling [product/service], targeting [customer segment]. Each headline must be under 30 characters. Vary the angle: urgency, social proof, benefit, question, local."

*Expected output:* Table — Angle | Headline | Character count. Highlight any that exceed the limit.

---

**Power**
> "Build a full email marketing sequence for my [business] launching [product/service] on [date]. Audience: existing customers + cold list. Sequence: pre-launch tease (Day -7), announcement (Day 0), objection handler (Day +2), last chance (Day +5). For each email: subject line (A/B variant), preview text, body outline, and primary CTA. Include open rate benchmarks for each email type."

*Expected output:* 4-email structure, each in a collapsible section with fields: Subject A | Subject B | Preview | Body outline | CTA | Benchmark.

---

### Topic 2 — Customer Communication

**Beginner**
> "Write a polite reply to a negative review that says: '[paste review].' Acknowledge the issue, apologize, and invite them to contact us directly."

*Expected output:* 3–5 sentence public reply, professional and non-defensive.

---

**Intermediate**
> "Draft a follow-up email sequence for customers who haven't returned in 90 days. Business: [type]. 3 emails: friendly check-in, special offer, final re-engagement. Keep each under 120 words. Include subject lines."

*Expected output:* 3 email drafts, labeled Email 1/2/3, each with subject line + body.

---

**Power**
> "Create a customer complaint resolution playbook for my [type of business]. Cover these scenarios: refund request, service failure, wrong order, rude staff complaint. For each: initial response script (phone + email), escalation trigger, resolution options, and closing script. Format as a staff reference guide."

*Expected output:* Playbook with 4 scenario sections, each containing a 2-column table (Channel | Script) + escalation decision tree.

---

### Topic 3 — Business Planning

**Beginner**
> "Explain a SWOT analysis in plain language and give me 2 example items for each quadrant for a [type of small business]."

*Expected output:* 4-quadrant list, plain English, 2 examples per quadrant.

---

**Intermediate**
> "I run a [type of business] with [X employees] in [location]. Help me set 3 SMART goals for the next quarter. My priorities: [list 2–3 priorities]. Format each goal with the SMART criteria labeled."

*Expected output:* 3 goals, each broken into Specific / Measurable / Achievable / Relevant / Time-bound rows.

---

**Power**
> "Act as a business strategist. Analyze this situation: [2–3 paragraph business context]. Identify the top 3 strategic risks and 2 growth opportunities. For each risk: likelihood (H/M/L), impact (H/M/L), and a mitigation action. For each opportunity: effort required, estimated revenue upside, and first 30-day action step. Output as an executive summary + action matrix."

*Expected output:* Executive summary (=150 words) + two tables: Risk Matrix and Opportunity Matrix.

---

### Topic 4 — Social Media

**Beginner**
> "Write 5 Instagram caption ideas for a [type of business]. Each should be 1–3 sentences with a question at the end to drive comments."

*Expected output:* Numbered list of 5 captions, each with an engagement question.

---

**Intermediate**
> "Create a 2-week social media calendar for [business name] on [platforms]. My content pillars: [list 3]. Mix: 40% educational, 30% promotional, 30% community. Output a table: Day | Platform | Pillar | Caption hook | Visual suggestion."

*Expected output:* 14-row table with all 5 columns populated.

---

**Power**
> "Audit my social media strategy for [business]. Here are my last 10 posts with engagement data: [paste]. Identify patterns in high vs. low performers. Recommend: optimal posting times, top 3 content formats to double down on, 2 content types to drop, and a 30-day experiment to test. Include a before/after content mix comparison."

*Expected output:* Pattern analysis section + recommendations with rationale + a before/after pie chart description.

---

### Topic 5 — Operations & Process

**Beginner**
> "Write a simple onboarding checklist for a new employee at a [type of business]. Include at least 10 items."

*Expected output:* Checkbox-formatted list, grouped by Day 1 / Week 1 / Month 1.

---

**Intermediate**
> "Create a standard operating procedure (SOP) for [specific task, e.g., 'opening the store each morning']. Include: purpose, required materials, step-by-step instructions, quality checks, and who is responsible."

*Expected output:* Structured SOP doc with labeled sections, numbered steps, and a responsibility field per step.

---

**Power**
> "Map the current process for [business workflow, e.g., 'customer order to delivery']. I'll describe it: [paste description]. Identify bottlenecks, redundant steps, and automation opportunities. Redesign the process for 25% fewer steps. Output: current-state flow (numbered) | waste identified | future-state flow | automation tools to consider."

*Expected output:* Two-column process comparison + waste log + tool recommendations table.

---

## Audience 3: Library Staff

### Topic 1 — Reader Recommendations

**Beginner**
> "Recommend 5 fiction books similar to [title] by [author]. Include a one-sentence reason for each match."

*Expected output:* Numbered list, each entry: Title — Author — one-sentence reason.

---

**Intermediate**
> "A patron enjoyed [3 titles]. They prefer [mood/theme] and dislike [element they disliked]. Recommend 5 books with a 2-sentence annotation for each explaining the match. Flag if any are likely to have holds."

*Expected output:* 5 annotated recommendations with a "Likely High-Demand" flag where applicable.

---

**Power**
> "Build a themed reading list for a patron with these constraints: adult fiction, [theme], not published before [year], no more than 400 pages, available in audio. Provide 8 titles ranked by patron match strength. For each: title, author, pub year, page count, audio availability status (if known), and 3-sentence annotation. Include a 'why this order' rationale."

*Expected output:* Ranked list table + annotations block + ordering rationale paragraph.

---

### Topic 2 — Program Planning

**Beginner**
> "Give me 5 program ideas for a public library's summer reading program for kids ages 6–12. Each idea should include a brief description."

*Expected output:* 5 program ideas, each with a 2-sentence description.

---

**Intermediate**
> "Plan a 6-week adult literacy workshop series for a public library. Each session: 90 minutes, 10–15 participants, low-literacy adults. Include session title, learning objective, activity outline, and materials needed. Keep language plain."

*Expected output:* 6-session table — Week | Title | Objective | Activities | Materials.

---

**Power**
> "Design a grant proposal outline for a library program targeting [underserved population]. Funding opportunity: [grant name or type]. Include: needs statement with supporting data prompts, program description, measurable outcomes (SMART), evaluation plan, budget narrative headers, and sustainability section. Flag each section that requires local data I need to fill in."

*Expected output:* Full outline with section headers, 2–3 sentence starters per section, and `[LOCAL DATA NEEDED]` flags.

---

### Topic 3 — Research Assistance

**Beginner**
> "Explain what a peer-reviewed article is in language a high school student would understand. Give 2 examples of where to find them."

*Expected output:* 3–4 sentence plain-language explanation + 2 database examples.

---

**Intermediate**
> "A patron is researching [topic] for a college paper. Suggest 5 search strategies using Boolean operators. Provide the exact search string, which database to use it in, and what type of results to expect."

*Expected output:* Table — Strategy | Search string | Database | Expected result type.

---

**Power**
> "Act as a reference librarian. A patron asks: '[complex research question].' Walk through a full reference interview: clarifying questions you would ask, your search strategy across 3 source types (database, web, print), expected sources to find, and how to evaluate them for credibility. Output as a staff training example."

*Expected output:* Narrative walkthrough structured as: Reference Interview ? Search Strategy ? Source Evaluation rubric.

---

### Topic 4 — Catalog & Metadata

**Beginner**
> "Write a brief catalog description (3–4 sentences) for this book: [title, author, subject]. Keep it spoiler-free and suitable for a public library catalog."

*Expected output:* 3–4 sentence description, reader-facing language, no spoilers.

---

**Intermediate**
> "Suggest 6 subject headings for a book about [topic]. Use Library of Congress Subject Headings (LCSH) format. Explain why each heading applies."

*Expected output:* 6 LCSH-formatted headings with a 1-sentence rationale each.

---

**Power**
> "Review this MARC record for errors and improvements: [paste record]. Check: correct MARC tag usage, subject heading format, ISBN validity format, author name authority, and language code. Output a table: Field | Current value | Issue | Recommended fix."

*Expected output:* MARC audit table with 4 columns + a summary of critical vs. minor errors.

---

### Topic 5 — Community Outreach

**Beginner**
> "Write a social media post announcing a free library event: [event name, date, time, brief description]. Make it friendly and include a call to action."

*Expected output:* 2–3 sentence social post + 3–5 relevant hashtags.

---

**Intermediate**
> "Draft a flyer for a library program in plain language. Event: [details]. Target audience: [audience]. Include: headline, 3 benefit statements, logistics (date/time/location), and a registration CTA. Keep reading level at Grade 6 or below."

*Expected output:* Flyer-formatted text with labeled sections + Flesch-Kincaid grade level estimate.

---

**Power**
> "Develop a 6-month outreach plan for a library branch serving a neighborhood with low library card usage. Goals: increase new card registrations by 20%, grow program attendance by 15%. Include: target segments, outreach channels, monthly milestones, partnership opportunities, and a measurement framework. Flag resource assumptions."

*Expected output:* Strategic plan with a monthly milestone table, KPI tracking sheet outline, and `[RESOURCE ASSUMPTION]` flags.

---

## Audience 4: Educator

### Topic 1 — Lesson Planning

**Beginner**
> "Give me a 45-minute lesson plan outline for teaching [concept] to [grade level]. Include: objective, hook activity, main instruction, practice, and exit ticket."

*Expected output:* 5-section outline with time allocations.

---

**Intermediate**
> "Design a project-based learning unit on [topic] for [grade/subject]. 2-week duration. Include: essential question, daily activity sequence, student product/deliverable, and 3 assessment checkpoints. Align to [standard if known]."

*Expected output:* Unit overview + 10-day activity sequence table + assessment checkpoint descriptions.

---

**Power**
> "Build a complete differentiated lesson plan for [concept] at [grade level]. Include three tracks: below grade level, on grade level, above grade level. For each track: modified objective, scaffolded materials list, activity variant, and success criteria. Include a co-teaching note for a paraprofessional. Align to [standard]."

*Expected output:* 3-track lesson plan in parallel columns + co-teaching sidebar + standards alignment note.

---

### Topic 2 — Differentiation

**Beginner**
> "Give me 3 ways to modify this assignment for a student who struggles with reading: [describe assignment]."

*Expected output:* 3 bullet-point modifications, each with a brief rationale.

---

**Intermediate**
> "I have a student with [learning profile/IEP goal]. The class is doing [activity]. Suggest 5 accommodations and 2 modifications that keep them engaged with the same content. Explain the difference between accommodation and modification."

*Expected output:* Labeled lists (Accommodations vs. Modifications) with explanations + a definition callout box.

---

**Power**
> "Design a Universal Design for Learning (UDL) framework for this unit: [unit topic, grade, duration]. Apply all three UDL principles: Representation, Action & Expression, Engagement. For each principle: list 3 specific strategies, required materials, and how to assess effectiveness. Output as a planning checklist teachers can reuse."

*Expected output:* 3-section UDL checklist with strategy descriptions, materials, and assessment columns.

---

### Topic 3 — Assessment Creation

**Beginner**
> "Write 5 multiple-choice questions for a quiz on [topic] for [grade level]. Include an answer key."

*Expected output:* 5 questions with 4 options each + answer key at the bottom.

---

**Intermediate**
> "Create a rubric for a [assignment type] on [topic] for [grade level]. Use 4 performance levels: Exceeds, Meets, Approaching, Beginning. Assess 4 criteria. Keep language student-friendly."

*Expected output:* 4×4 rubric grid with descriptors for each cell, totaling 16 cells.

---

**Power**
> "Build a balanced assessment suite for a [unit topic] unit: [grade, duration]. Include: pre-assessment (diagnostic), 2 formative checks with feedback protocols, a summative performance task with rubric, and a student self-reflection tool. Align each to the same learning objectives. Output as a teacher-facing planning doc."

*Expected output:* Multi-section assessment doc with each tool labeled, format described, and alignment table at the end.

---

### Topic 4 — Parent Communication

**Beginner**
> "Write a brief positive note home about a student who showed improvement in [behavior or skill]. Keep it warm, specific, and under 100 words."

*Expected output:* 3–4 sentence note, personalized tone, under 100 words.

---

**Intermediate**
> "Draft an email to parents explaining a new classroom policy: [policy]. Address likely concerns, explain the reason for the policy, and invite questions. Keep it under 250 words. Avoid jargon."

*Expected output:* Email with subject line + 3-paragraph structure (policy ? rationale ? invitation) + word count.

---

**Power**
> "Write a conference preparation guide for a difficult parent meeting about a student's [behavioral/academic concern]. Include: talking points for the teacher, likely parent objections with de-escalation responses, documentation checklist, proposed action plan template, and follow-up email draft. Frame everything as collaborative problem-solving."

*Expected output:* 5-section guide — Talking Points | Objection Map | Documentation Checklist | Action Plan | Follow-up Email.

---

### Topic 5 — Student Feedback

**Beginner**
> "Rewrite this feedback comment to be more growth-oriented: '[paste current comment].' Keep the same core message but use a strengths-based tone."

*Expected output:* Revised comment + a one-sentence note explaining the change in framing.

---

**Intermediate**
> "Write 10 comment bank phrases for [assignment type] that give specific, actionable feedback. Cover: strong work, needs revision, effort noted, missing component, creative thinking. 2 phrases per category."

*Expected output:* 5-category comment bank table — Category | Phrase 1 | Phrase 2.

---

**Power**
> "Design a whole-class feedback strategy after grading [assignment]. I noticed these trends in student work: [list 3 common errors + 2 strengths]. Create: a 10-minute class feedback mini-lesson, a self-correction task, a peer review protocol, and 3 anchor examples (below/meets/exceeds) with annotations. Format for projection and handout use."

*Expected output:* Mini-lesson plan + self-correction worksheet outline + peer review protocol + annotated anchor example descriptions.

---

## Audience 5: Tradesperson

### Topic 1 — Client Estimates & Quotes

**Beginner**
> "Write a professional estimate email for a [trade] job. Job details: [brief description]. My company name: [name]. Keep it short and polished."

*Expected output:* Email template with subject line, itemized scope placeholder, price field, and terms line.

---

**Intermediate**
> "Help me build a quote for a [job type] project. Scope: [describe]. My labor rate: $[X]/hr. Estimated hours: [Y]. Materials: [list with rough costs]. Add a 15% margin and format it as a professional quote document with line items, subtotal, tax line, and total."

*Expected output:* Formatted quote table with all line items + calculated totals + a "Quote valid for 30 days" footer.

---

**Power**
> "I need to write a detailed proposal for a [large project type] job worth approximately $[value]. Client: [type]. Scope: [describe]. Create a professional proposal including: executive summary, detailed scope of work, exclusions list, payment schedule (milestone-based), warranty terms, and change order policy. Flag any terms I should have a lawyer review."

*Expected output:* Full proposal document with 6 labeled sections + `[LEGAL REVIEW ADVISED]` flags on liability/warranty clauses.

---

### Topic 2 — Job Documentation

**Beginner**
> "Write a brief job completion note I can leave for a customer after finishing a [type of job] at their home. Include: what was done, any recommendations, and my contact info placeholder."

*Expected output:* Half-page customer-facing note, plain language, professional tone.

---

**Intermediate**
> "Create a site visit report template for a [trade] inspection. Fields needed: client info, site address, date, findings (with severity rating), photos needed (list), recommended actions, estimated repair cost range, and follow-up timeline."

*Expected output:* Fillable report template with all fields, severity rating scale defined (1–3 or Low/Med/High), and a signature line.

---

**Power**
> "Build a job documentation system for a small [trade] business handling 10–20 jobs/month. Design: job intake form, daily work log template, punch list format, completion sign-off form, and warranty card template. Each should capture data needed for disputes and warranty claims. Include a note on what records to keep and for how long."

*Expected output:* 5-template system with a records retention table at the end.

---

### Topic 3 — Material & Supply Lists

**Beginner**
> "Give me a materials list for [common job type, e.g., 'installing a bathroom exhaust fan']. Include quantities and standard sizes."

*Expected output:* Bulleted list with item, quantity, and common spec/size per item.

---

**Intermediate**
> "I'm doing a [job type] for a [room size/scope]. Create a materials takeoff list. For each item: material, unit, quantity needed, and a waste factor percentage. Include a running cost column with [X]% markup applied."

*Expected output:* Takeoff table — Material | Unit | Qty | Waste% | Unit Cost (blank) | Extended Cost | Marked-Up Cost.

---

**Power**
> "I have 3 similar jobs coming up this week: [Job 1 brief], [Job 2 brief], [Job 3 brief]. Consolidate materials across all three into a single purchase order optimized for one supplier run. Group by material type, flag overlapping items, and calculate bulk quantity. Note any items that need separate sourcing."

*Expected output:* Consolidated PO table grouped by material type + overlap callouts + separate-sourcing flags.

---

### Topic 4 — Safety & Compliance

**Beginner**
> "List the top 10 OSHA safety rules every [trade] worker should know on a job site. Use plain language."

*Expected output:* Numbered list, plain language, 1–2 sentences per rule.

---

**Intermediate**
> "Create a job site safety checklist for a [trade] project at a [site type, e.g., residential remodel]. Cover: PPE requirements, tool inspection, hazard identification, emergency contacts, and end-of-day shutdown. Format as a daily sign-off sheet."

*Expected output:* Checklist with checkbox format, grouped by phase (start/mid/end of day), with signature line.

---

**Power**
> "Write a safety and compliance manual section for my [trade] business covering: required PPE by task type, OSHA recordkeeping requirements (300 log basics), toolbox talk schedule, incident reporting procedure, and subcontractor safety expectations. Format as a section of a company safety manual. Flag any state-specific items I need to verify locally."

*Expected output:* Multi-section manual excerpt with headers, policy language, tables where needed, and `[VERIFY STATE REGS]` flags.

---

### Topic 5 — Business Communication

**Beginner**
> "Write a professional text message to a client letting them know I'll be 30 minutes late to their job. Keep it brief and apologetic."

*Expected output:* 2–3 sentence text-length message, professional but conversational.

---

**Intermediate**
> "Write a past-due invoice reminder email for a client who is 21 days overdue on a $[amount] invoice for [job type]. Be firm but professional. Include the invoice number placeholder, original due date, payment options, and a deadline to respond."

*Expected output:* Email with subject line, firm-but-professional body (3 paragraphs), payment options list, and response deadline.

---

**Power**
> "A client is disputing my invoice, claiming the work was incomplete. The job was [describe]. My documentation: [describe what you have]. Draft a response letter that: acknowledges their concern professionally, presents the documented evidence, references the signed scope of work, proposes a resolution path, and states next steps if unresolved (without threatening, but implying collections). Include a subject line and make it attorney-sendable."

*Expected output:* Formal dispute response letter with clear evidence section, resolution proposal, escalation language, and a note flagging any claim that needs documentation to be airtight.

---

*75 prompts total — 5 audiences × 5 topics × 3 tiers (Beginner / Intermediate / Power)*
*Each prompt includes: copy-paste prompt text, expected output format description.*
