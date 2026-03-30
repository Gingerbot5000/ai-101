# AI-101 Presentation Audit - March 28, 2026

Audit target: `index.html`

Goal: identify every time-sensitive or overconfident product claim on the live deck that should be updated before calling the page current as of March 28, 2026.

## Must update

1. `index.html:1680`
   Current: `Updated Feb 2026`
   Replace with: `Updated March 28, 2026`
   Why: the deck still advertises February 2026.

2. `index.html:1814`
   Current: `OpenAI - GPT-4.5`
   Replace with: `OpenAI - GPT-5 family`
   Safer precise version: `OpenAI - GPT-5.3 / GPT-5.4`
   Why: ChatGPT no longer centers on GPT-4.5. OpenAI's current ChatGPT materials reference GPT-5.3 as the flagship model on Free/Go and GPT-5.4 in higher tiers.

3. `index.html:1820`
   Current: `Free tier + $20/mo Pro`
   Replace with: `Free plan available - Plus $20/mo - Pro $200/mo`
   Safer lower-maintenance version: `Free plan available - paid plans available`
   Why: OpenAI's current pricing stack is Free, Go, Plus, Pro, Business, and Enterprise. The current slide understates Pro pricing by 10x and omits Go entirely.

4. `index.html:1827`
   Current: `Anthropic - 3.7 Sonnet`
   Replace with: `Anthropic - Claude Sonnet 4.6`
   Why: Anthropic says Sonnet 4.6 is the default model for Free and Pro users as of February 17, 2026.

5. `index.html:1840`
   Current: `Google - 2.0 Pro`
   Replace with: `Google - Gemini`
   Safer precise version: `Google - Gemini (Google AI plans)`
   Why: the current Google consumer stack is framed around Gemini plus Google AI plans, not `2.0 Pro`.

6. `index.html:1842-1846`
   Current: `Best for Google Workspace integration, massive file processing (up to 2M tokens), and multimodal tasks natively generating video and audio. Deeply connected to Search.` plus `Free with Google - $20/mo Advanced`
   Replace with: `Strong for Google ecosystem workflows, multimodal assistance, long-context tasks, and Search-connected answers.` plus `Free tier available - Google AI plans available`
   Why: `Gemini Advanced` is outdated branding. Google's official plan pages now use Google AI Plus / Pro / Ultra, and video generation is spread across Gemini, Flow, and Whisk. The `2M tokens` claim is also too specific for this consumer-facing slide unless you want to maintain it continuously.

7. `index.html:1878-1879`
   Current: `it answers only from your data. No hallucinations from outside sources.`
   Replace with: `NotebookLM is designed to stay grounded in your sources and show citations back to them, but important details should still be verified.`
   Why: Google help pages do say NotebookLM uses the provided materials for answers, but they also describe outputs as AI-generated and explicitly warn users not to rely on them for professional advice. `No hallucinations` is too strong.

8. `index.html:1890-1891`
   Current: `Open-source AI that rivals GPT-4 in math, logic, and coding. Runs locally or in the cloud.`
   Replace with: `DeepSeek offers current open and reasoning-focused models for coding, math, and technical problem-solving. Available via web, app, and API, with open model options for self-hosted workflows.`
   Why: the GPT-4 comparison is dated. DeepSeek's official site now points users to DeepSeek-V3.2, web/app/API access, and open model repositories.

9. `index.html:1902-1903`
   Current: `xAI's assistant with real-time X/Twitter integration.`
   Replace with: `xAI's assistant with access on the web, X, iOS, and Android. Useful for current events, trend monitoring, and social-media-adjacent analysis.`
   Why: the current Grok product is broader than just X integration.

10. `index.html:2113-2114`
    Current: `Assume anything you type may be used for training.`
    Replace with: `On consumer AI tools, your content may be used to improve models depending on your settings. Business and API products often have different defaults and controls.`
    Why: OpenAI's current help docs distinguish consumer training defaults from business/API defaults, and users can disable training in ChatGPT data controls.

11. `index.html:2183-2184`
    Current: `they're free, instant, and no account needed for most.`
    Replace with: `free tiers are available for several of them, though sign-in requirements and feature limits vary by product.`
    Why: NotebookLM and most Google AI plan features depend on a Google account, and the sentence overstates anonymous access.

## Strongly recommended

1. `index.html:1806-1807`
   Current: `The three most capable general-purpose AI assistants available today.`
   Recommended: `Three leading general-purpose AI assistants available today.`
   Why: `most capable` is an uncited ranking claim, not a stable fact.

2. `index.html:1816-1817`
   Current: `The most widely-used AI assistant worldwide.`
   Recommended: delete this sentence, or replace with `A widely used general-purpose assistant.`
   Why: this is a global market-share claim with no citation on the slide.

3. `index.html:1829-1830`
   Current: `Produces the most human-like text. The absolute top-tier coding assistant in 2026.`
   Recommended: `Known for polished, natural-feeling writing and strong coding performance.`
   Why: both current sentences are absolute and hard to defend in a public educational deck.

4. `index.html:1865`
   Current: `The Search Engine Killer`
   Recommended: `The Research Assistant`
   Why: not inaccurate exactly, but hype-driven and likely to age badly.

5. `index.html:1901`
   Current: `The Unfiltered Voice`
   Recommended: `The Real-Time Companion`
   Why: xAI markets Grok as truth-seeking and multi-platform; `unfiltered` is more vibe than verifiable product description.

6. `index.html:2135-2136`
   Current: `AI-generated content exists in a legal gray area.`
   Recommended: `Ownership, copyright, and disclosure rules for AI-generated content still vary by jurisdiction, industry, and platform.`
   Why: more precise and less hand-wavy.

## Evidence checked

- OpenAI ChatGPT pricing: https://chatgpt.com/pricing
- OpenAI ChatGPT Plus help: https://help.openai.com/en/articles/6950777
- OpenAI ChatGPT Pro help: https://help.openai.com/en/articles/9793128
- OpenAI ChatGPT release notes: https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- OpenAI data controls: https://help.openai.com/en/articles/5722486-how-your-data-is-used-to
- OpenAI enterprise privacy: https://openai.com/enterprise-privacy/
- Anthropic Sonnet 4.6 announcement: https://www.anthropic.com/news/claude-sonnet-4-6
- Anthropic pricing: https://claude.com/pricing
- Google AI plans: https://one.google.com/about/google-ai-plans/
- Google One plan pricing: https://one.google.com/plans
- NotebookLM Help: https://support.google.com/notebooklm/answer/16322204
- NotebookLM work/school access and data protections: https://support.google.com/notebooklm/answer/16337734
- DeepSeek official site: https://www.deepseek.com/
- DeepSeek official GitHub org: https://github.com/deepseek-ai
- Grok official product page: https://x.ai/grok

## Short version

If you only make five edits, make these:

1. Update the timestamp.
2. Replace `GPT-4.5` with current ChatGPT naming and fix ChatGPT Pro pricing.
3. Replace `3.7 Sonnet` with `Claude Sonnet 4.6`.
4. Replace `Google - 2.0 Pro` and `Advanced` branding with current Gemini / Google AI plan language.
5. Remove the NotebookLM and privacy overclaims (`No hallucinations`, `anything you type may be used for training`).
