Now I have solid sourced data. Let me write the full deck content.

---

## Slide Copy: The 2026 Agentic Stack for Builders

---

## Section 1 — What Is the Agentic Stack?

### Beginner
You used to tell software what to do, step by step.
Now you describe a goal, and a chain of AI **agents** handles the steps for you.

The agentic stack is the collection of tools that make this possible — from writing code to connecting apps to shipping designs.

**Five tools. One pipeline. Zero full-time IT staff required.**

### Intermediate
An agentic stack is a set of coordinated AI components that can:
- **Plan** what needs to happen
- **Execute** actions across tools and APIs
- **Iterate** on results without constant human prompting

Each tool in this stack owns a specific layer: code generation, workflow orchestration, tool connectivity, and design-to-build handoff.

### Power User
The 2026 agentic stack achieves **long-horizon task completion** via:
- Stateful agents that maintain context across multi-step sessions
- Standardized interop (MCP) eliminating N×M integration sprawl
- Parallel sandboxed execution across isolated cloud environments
- Design token–aligned code generation closing the designer/developer loop

---

## Section 2 — OpenAI Codex

### Beginner
**Codex is your AI coding partner in the cloud.**

You describe a feature or bug. Codex reads your codebase, writes the code, and creates a pull request for you to review. You never had to open a file.

> "Write a login form with email validation and submit it as a PR."
> ? Codex does it, in its own sandboxed copy of your repo.

### Intermediate
Codex (launched April 2025) runs tasks in **isolated cloud sandbox environments** preloaded with your repository. Key capabilities:
- Write features, fix bugs, propose pull requests
- Longer iterative sessions with context compaction
- Supports `AGENTS.md` for repo-specific agent instructions
- Native MCP support for extending with third-party tools
- Orchestratable via the OpenAI Agents SDK for multi-agent pipelines

Current model: **GPT-5.3-Codex** — 25% faster than its predecessor, combining frontier coding and professional reasoning in one model.

### Power User
GPT-5.3-Codex advances beyond code review into **computer-use–level task execution** — anything a developer can do on a computer, Codex can approximate. Architecture notes:
- **Worktrees + parallel agents**: multiple tasks run concurrently across projects
- **Context compaction** enables large refactors and cross-file migrations without window overflow
- Integrates with `AGENTS.md` convention for per-repo behavioral guardrails
- Cybersecurity capabilities significantly upgraded in GPT-5.2-Codex baseline

---

## Section 3 — Claude Code

### Beginner
**Claude Code lives in your terminal and acts like a senior developer pair.**

It can read your entire project, edit files, run commands, and explain what it changed — all from a chat-style interface. No GUI required.

> "Find the bug causing the login failure and fix it."
> ? Claude Code reads, diagnoses, edits, confirms.

### Intermediate
Claude Code is Anthropic's terminal-based agentic coding CLI. Core behaviors:
- Full filesystem read/write and shell command execution
- Persistent session context (memory files survive across conversations)
- **Built-in MCP client** — connects to any MCP server for extended tool access
- Plan Mode for large refactors before code is touched
- `CLAUDE.md` per-project instruction files for behavioral customization

Powered by **claude-sonnet-4-6** (current default) or **claude-opus-4-6** for complex reasoning tasks.

### Power User
Claude Code implements a **local-first agentic loop** with:
- **Subagent delegation** via the `Agent` tool — spawns specialized agents (Explore, Plan, security-auditor, etc.) for parallelized context-safe research
- **Worktree isolation** — agents operate on temporary git worktrees to prevent main-branch pollution
- Hooks in `~/.claude/settings.json` enforce pre-commit guardrails (secret scanning, format checks)
- MCP server composition: connect Obsidian, databases, Figma, GitHub — all surfaced as native tools

---

## Section 4 — n8n (Workflow Orchestration)

### Beginner
**n8n is the plumbing between your apps — with AI baked in.**

Think of it as a visual flowchart where each box is an app (Gmail, Slack, a database, an AI model). When something happens in one box, n8n automatically triggers the next.

> Email arrives ? AI summarizes it ? Slack gets the summary ? task created in Notion.

No code needed to start. You drag, connect, and run.

### Intermediate
n8n is an **open-source, self-hostable workflow automation platform** with 500+ integrations. AI-specific capabilities:
- **Built-in AI Agent node** with memory, tools, and guardrails
- Agents can reason, branch, and loop within the same visual canvas
- Supports LLM routing (OpenAI, Anthropic, local models via Ollama)
- Human-in-the-loop approval steps inline with automated nodes
- 5,800+ community workflow templates for common AI patterns

Fair-code license: free self-hosted, paid cloud tier for scale.

### Power User
n8n's **agentic execution model** enables:
- **Multi-agent orchestration** on a single canvas — parent agent delegates to sub-workflows
- RAG pipelines with built-in vector store nodes (Pinecone, Qdrant, Supabase pgvector)
- Dynamic tool-calling: agents select which n8n nodes to invoke at runtime
- MCP server compatibility — expose n8n workflows as MCP tools consumable by Codex/Claude Code
- Webhook-triggered agents for event-driven, production-grade automation

---

## Section 5 — MCP (Model Context Protocol)

### Beginner
**MCP is the USB-C port for AI tools.**

Before MCP, every AI tool needed a custom cable to connect to every other service. MCP is one universal plug.

Your AI agent speaks MCP. Your database speaks MCP. They connect — done. No custom code per integration.

> Anthropic introduced MCP in November 2024. By February 2025, over 1,000 open-source connectors existed.

### Intermediate
MCP (Model Context Protocol) is an **open standard** built on JSON-RPC using a **client–host–server architecture**. Three primitive types:

| Primitive | What It Does | Example |
|---|---|---|
| **Tools** | Agent calls an action | Run a SQL query, send a Slack message |
| **Resources** | Agent reads structured data | File contents, database rows, API responses |
| **Prompts** | Pre-built prompt templates | "Summarize this PR", "Draft a reply" |

Adopted by OpenAI, Google DeepMind, Microsoft, Block, Replit, Sourcegraph, and hundreds more.

### Power User
MCP eliminates the **N×M integration problem** — previously, M models × N tools = M×N custom connectors. With MCP: M + N.

Architecture depth:
- **Stateful sessions** maintain context across tool calls within an agent loop
- MCP servers run locally or as remote services (HTTP/SSE or stdio transport)
- **Authorization layer**: OAuth 2.0 support for production-grade credential handling (MCP spec 2025-11-25)
- Composition pattern: chain MCP servers (Figma ? Claude Code ? GitHub) for end-to-end pipelines
- Claude Code ships as both MCP client *and* exposes itself as an MCP server for orchestration by other agents

---

## Section 6 — Figma Dev Handoff

### Beginner
**Figma is where designs live. Dev Mode is how they ship.**

A designer finishes a screen and marks it "Ready for Dev." Developers open Dev Mode and see exact measurements, colors, fonts, and — now — AI-generated code.

The guesswork between "what the designer meant" and "what the developer built" disappears.

### Intermediate
Figma's **Dev Mode** bridges design intent and production code:
- **"Ready for dev" status** creates a clear, filterable queue for developers — no hunting through canvases
- **Code Connect** maps Figma components to your actual component library (React, SwiftUI, Jetpack Compose)
- **Design tokens via Variables** — colors, spacing, and typography exported as structured data
- Inspect panel provides CSS/iOS/Android code snippets auto-generated from layers

2025 addition: **Figma MCP Server** — supplies exact design data (including variable values) directly to agentic coding tools.

### Power User
The **Figma MCP Server** closes the design-to-production loop in agentic workflows:

```
Figma (source of truth)
  +- MCP Server exposes design tokens, layer data, component specs
       +- Claude Code / Codex / Cursor reads via MCP
            +- Generates production-accurate, token-aligned components
                 +- PR created, reviewed, merged
```

Key architectural requirements for this pipeline to work:
1. **Design system uses Figma Variables** — tokens become structured MCP data, not arbitrary pixel values
2. **Code Connect configured** — AI generates your component syntax, not generic HTML
3. **"Ready for dev" discipline** — only finalized frames enter the agent's context; noise excluded
4. Result: AI-generated code matches design system conventions, not just visual appearance

---

## Section 7 — The Full Stack, Connected

### Beginner
Here's how the five tools work together in one project:

```
You describe a feature
  ? Codex or Claude Code writes the code
  ? n8n triggers tests and notifications automatically
  ? MCP connects everything without custom wiring
  ? Figma hands off the exact design the AI should match
```

**One person. Five AI-powered tools. Shipping like a team of ten.**

### Intermediate

| Tool | Layer | Role in Pipeline |
|---|---|---|
| **Figma Dev Mode** | Design | Source of truth for UI intent + token-aligned specs |
| **MCP** | Protocol | Universal connector between every layer |
| **Claude Code** | Local Dev | Terminal agent: read, edit, run, iterate |
| **Codex** | Cloud Dev | Async agent: PRs, large refactors, parallel tasks |
| **n8n** | Orchestration | Glues triggers, approvals, and multi-step flows |

Any layer can be swapped. MCP ensures interoperability regardless of which AI model or tool sits in each slot.

### Power User
The 2026 production agentic pipeline:

1. **Figma MCP Server** ? feeds design context to coding agents
2. **n8n** receives a webhook (new Figma "Ready for dev" frame) ? triggers agent workflow
3. **Claude Code** (via n8n MCP tool call) reads design tokens + existing codebase ? generates component
4. **Codex** runs parallel tasks in cloud sandbox ? proposes PR with tests
5. **n8n** human-in-the-loop node ? developer approves ? auto-merge to staging
6. **MCP** maintains session state and tool authorization across every hop

**Estimated cycle time for a new UI component: minutes, not days.**

---

## Citation Block (for slide footnotes)

- [Introducing Codex — OpenAI](https://openai.com/index/introducing-codex/)
- [Introducing GPT-5.3-Codex — OpenAI](https://openai.com/index/introducing-gpt-5-3-codex/)
- [openai/codex CLI — GitHub](https://github.com/openai/codex)
- [Introducing the Model Context Protocol — Anthropic](https://www.anthropic.com/news/model-context-protocol)
- [MCP Specification 2025-11-25 — modelcontextprotocol.io](https://modelcontextprotocol.io/specification/2025-11-25)
- [What is MCP? — IBM Think](https://www.ibm.com/think/topics/model-context-protocol)
- [microsoft/mcp-for-beginners — GitHub](https://github.com/microsoft/mcp-for-beginners)
- [n8n AI Agents — n8n.io](https://n8n.io/ai-agents/)
- [n8n Guide 2026 — Hatchworks](https://hatchworks.com/blog/ai-agents/n8n-guide/)
- [Figma Dev Mode — Figma](https://www.figma.com/dev-mode/)
- [Figma Design Handoff — Figma](https://www.figma.com/design-handoff/)
- [Is Figma Make ready for dev handoff? — UX Collective](https://uxdesign.cc/is-figma-make-ready-for-dev-handoff-9fe2594630e3)
