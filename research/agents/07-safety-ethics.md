```markdown
# AI Safety & Ethics — Field Guide
### Module 7 of 10 · AI-101 · Non-Technical Edition

---

## LEVEL 1 — BEGINNER RULES
> *Do these every time, no exceptions.*

---

### Rule 1 · Never Share Secrets
**Don't paste passwords, SSNs, API keys, or private health info into any AI chat.**
> *A nurse typed a patient's full record into ChatGPT to "summarize it faster" — now it's in a training dataset.*

---

### Rule 2 · Verify Before You Trust
**AI can state false facts with total confidence. Check any number, date, or claim before using it.**
> *A lawyer cited three AI-generated court cases in a real filing. None of them existed.*

---

### Rule 3 · You Are Still Responsible
**Signing your name to AI output makes it yours. You own the errors too.**
> *A student submitted an AI essay, got caught, and was expelled — "the AI wrote it" was not a defense.*

---

### Rule 4 · Don't Automate Hate
**If you wouldn't say it yourself, don't let AI say it for you.**
> *A marketing team let AI auto-generate ad copy — it produced ethnically biased product descriptions that went live.*

---

### Rule 5 · Disclose When It Matters
**Tell people when AI helped create something they're relying on for decisions.**
> *A doctor received an AI-drafted referral letter. Without knowing, she couldn't catch the hallucinated medication history inside.*

---

### Rule 6 · AI Has No Real-World Awareness
**AI doesn't know today's date, recent news, or your actual situation unless you tell it.**
> *A small business owner got AI-generated legal advice that cited a law that was repealed two years prior.*

---

## LEVEL 2 — INTERMEDIATE CHECKS
> *Do these before deploying or sharing AI output widely.*

---

### Check 1 · Source Audit
**Ask: "Where did this come from?" AI mixes quality sources with garbage. Trace at least one key claim.**
> *A grant proposal included fabricated research statistics that passed three internal reviews before being caught.*

---

### Check 2 · Bias Scan
**Run your output past someone from a different background. AI reflects its training data's biases.**
> *A hiring tool trained on historical résumés down-ranked candidates from women's colleges for 4 years before anyone noticed.*

---

### Check 3 · Scope Creep Guard
**Define the task clearly. Vague prompts produce confidently wrong results in all directions.**
> *"Write a policy for our team" became a 12-page document that included liability clauses the company was not prepared to honor.*

---

### Check 4 · Human-in-the-Loop on High Stakes
**Any output touching money, health, legal, or safety needs a human sign-off before action.**
> *An automated AI email campaign sent refund approvals for claims that hadn't been validated — $40k gone in 6 hours.*

---

### Check 5 · Output Drift Check
**If AI is running repeatedly (scheduled, automated), spot-check it weekly. Models update. Behavior changes.**
> *A weekly AI newsletter ran for 3 months before anyone noticed it had started confidently hallucinating product specs.*

---

### Check 6 · Consent for Synthetic Personas
**Don't let AI impersonate real people, living or dead, without explicit permission.**
> *A startup generated a fake customer testimonial using a real employee's name and photo. It became a legal dispute.*

---

## LEVEL 3 — POWER-USER GOVERNANCE CHECKS
> *Do these when AI is embedded in products, workflows, or org decisions.*

---

### Gov Check 1 · Data Residency & Retention
**Know exactly where your data goes, how long it's stored, and who can access it.**
> *A fintech startup discovered their vendor's AI logs were retained for 2 years and accessible to the vendor's engineers — a GDPR violation.*

---

### Gov Check 2 · Model Change Management
**When the underlying model updates, your system behavior changes. Treat model updates like software releases.**
> *An enterprise chatbot passed QA in January. In March the model silently updated and started giving incorrect policy answers to 10,000 users.*

---

### Gov Check 3 · Adversarial Input Testing
**Test what happens when users try to break, manipulate, or jailbreak your AI-powered feature.**
> *A customer support bot was prompt-injected via a user ticket to reveal internal pricing tiers to competitors.*

---

### Gov Check 4 · Explainability Requirement
**For regulated decisions (credit, hiring, healthcare), you must be able to explain why the AI decided what it did.**
> *A bank's AI loan rejections were legally challenged — the vendor couldn't produce a human-readable explanation, costing the bank a $2M settlement.*

---

### Gov Check 5 · Kill Switch & Rollback Plan
**Every AI system needs a documented off switch and a tested manual fallback.**
> *An AI scheduling system crashed during a hospital's peak intake period. No manual backup existed. Patients waited 6 hours.*

---

### Gov Check 6 · Ongoing Impact Monitoring
**Measure real-world outcomes after deployment. Accuracy in testing ? fairness in production.**
> *An AI content moderation system performed well in testing but over-flagged posts from non-native English speakers by 3x in production.*

---

## Quick Reference Card

| Level | Core Question | Red Flag |
|---|---|---|
| Beginner | "Would I say this myself?" | Sharing private data |
| Intermediate | "Has a human verified this?" | High-stakes auto-send |
| Governance | "Can I audit, explain, and stop this?" | No rollback plan |

---

*Module 7 of 10 · AI-101 · Adam Gurski Professional AI Profile · 2026*
```

Key design choices for card layout:
- Each rule/check is self-contained — works as a standalone card
- Rule name doubles as card header
- Bold one-liner = the card body
- Italic story = footer/caption strip
- Three levels map cleanly to beginner / intermediate / advanced card decks
- Quick Reference table works as a summary/back-of-deck card
