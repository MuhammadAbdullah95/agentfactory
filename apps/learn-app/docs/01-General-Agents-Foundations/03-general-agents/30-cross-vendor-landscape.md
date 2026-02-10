---
sidebar_position: 30
title: "The Cross-Vendor Landscape: Your Skills Are Portable"
description: "See how Claude Code concepts map to OpenAI Codex, Google Gemini CLI, and emerging industry standards — your agent-building skills transfer everywhere."
keywords: [openai codex, gemini cli, agents.md, mcp, agentic ai foundation, cross-vendor, portable skills]
chapter: 3
lesson: 30
duration_minutes: 25
chapter_type: Concept

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation) - Industry awareness and concept mapping"
layer_1_foundation: "Understanding cross-vendor equivalents, industry standards, market landscape"

# HIDDEN SKILLS METADATA
skills:
  - name: "Cross-Vendor Concept Mapping"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Literacy"
    measurable_at_this_level: "Student can map Claude Code concepts to their equivalents in Codex and Gemini CLI"
  - name: "Industry Standards Awareness"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Remember"
    digcomp_area: "Digital Literacy"
    measurable_at_this_level: "Student can name the three founding projects of the Agentic AI Foundation and explain why standards convergence matters"

learning_objectives:
  - objective: "Map every major Claude Code concept to its cross-vendor equivalent"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Concept mapping exercise"
  - objective: "Explain why MCP, AGENTS.md, and SKILL.md are converging under the Agentic AI Foundation"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Short explanation"
  - objective: "Compare the architectural philosophies of Claude Code vs Codex vs Gemini CLI"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Comparison table completion"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (cross-vendor mapping, AAIF standards convergence, SWE-bench benchmarking, poly-agentic workflows) - within A2 limit of 7"

differentiation:
  extension_for_advanced: "Install Codex CLI or Gemini CLI and compare the experience firsthand"
  remedial_for_struggling: "Focus only on the concept mapping table - the rest is enrichment"

# Generation metadata
generated_by: "content-implementer v2.0.0"
created: "2026-02-11"
last_modified: "2026-02-11"
git_author: "Claude Code"
workflow: "manual"
version: "1.0.0"

# Legacy compatibility (Docusaurus)
prerequisites:
  - "Completion of Lessons 01-29 in this chapter"
  - "Understanding of Skills, MCP, CLAUDE.md, hooks, subagents, and teams"
---

# The Cross-Vendor Landscape: Your Skills Are Portable

You've spent this entire chapter learning Claude Code. Here's the secret: **you weren't just learning one tool.**

Every concept you mastered -- CLAUDE.md project instructions, Skills, MCP servers, hooks, subagents, agent teams -- is part of an emerging industry standard. OpenAI's Codex CLI has its own version of each. Google's Gemini CLI has its own version. And in December 2025, these companies joined forces under the Linux Foundation to make these patterns interoperable.

MIT Technology Review named "Generative Coding" one of its 10 Breakthrough Technologies of 2026. AI now writes approximately 30% of Microsoft's code and more than 25% of Google's. The tools you learned in this chapter are not a niche experiment. They are the new baseline for how software gets built.

---

## The Market in February 2026

The agentic coding market has consolidated into two leaders and several strong contenders.

### Tier 1: The Two Leaders

**Anthropic (Claude Code)**
$1B annual recurring revenue as of February 2026. Claude Code accounts for 4% of all GitHub commits (SemiAnalysis, February 5, 2026). Claude Opus 4.5 holds the top spot on SWE-bench Verified at 80.9%. Philosophy: developer-in-the-loop, local terminal execution, accuracy-first.

**OpenAI (Codex)**
Codex CLI is open source, built in Rust, installable via `npm i -g @openai/codex`. OpenAI launched a macOS desktop app on February 2, 2026, and released GPT-5.3-Codex on February 5, 2026. Codex runs tasks in a cloud sandbox while also supporting local execution. Philosophy: parallel, asynchronous, fire-and-forget delegation.

### Tier 2: Strong Contenders

| Tool | Key Stat | Positioning |
|------|----------|-------------|
| **Cursor** | $1B ARR, $29.3B valuation | Fastest SaaS growth in history (SaaStr). IDE-first experience. |
| **GitHub Copilot** | 68% developer usage rate, $400M revenue (2025) | Agent mode GA. Massive distribution via GitHub ecosystem. |
| **Google Gemini CLI** | Open source (Apache 2.0), free tier (1,000 req/day), 1M token context | Accessible, open, enormous context window. |

### Tier 3: Emerging Players

Amazon Q Developer and Devin (which acquired the Windsurf product and brand) round out the landscape.

---

## The Concept Mapping Table

This is the most important table in this lesson. Everything you learned in Chapter 3 has equivalents across the industry:

| What You Learned | Claude Code | OpenAI Codex | Google Gemini CLI | Open Standard |
|---|---|---|---|---|
| Project instructions | CLAUDE.md | AGENTS.md | GEMINI.md | AGENTS.md (AAIF) |
| Agent Skills | `.claude/skills/SKILL.md` | `.agents/skills/SKILL.md` | `.gemini/skills/SKILL.md` | Agent Skills spec (agentskills.io) |
| Tool connectivity | MCP servers in settings.json | MCP servers in config.toml | MCP servers in settings.json | MCP (Linux Foundation) |
| Permission control | allowedTools, permissions | Approval modes (suggest / auto-edit / full-auto) | Tool approval prompts | -- |
| Context hierarchy | Global, Project, Directory | Global, Project | Global, Project, Directory | -- |
| Subagents | Task tool with subagent_type | Cloud sandbox tasks | -- | -- |
| Agent Teams | TeamCreate, TaskCreate, SendMessage | macOS app parallel agents | -- | -- |
| Hooks | Pre/Post tool hooks in settings.json | -- (not yet) | -- (not yet) | -- |
| IDE integration | VS Code extension | VS Code extension | VS Code extension | -- |
| Desktop app | Claude Desktop / Cowork | Codex macOS app | -- | -- |

The pattern: what you know transfers. The directory name changes (`.claude/` vs `.agents/` vs `.gemini/`), but the concepts are the same.

---

## Standards Convergence: The Agentic AI Foundation

In December 2025, the biggest companies in AI did something unusual: they agreed on shared standards.

The **Agentic AI Foundation (AAIF)** formed under the Linux Foundation with platinum members including Anthropic, OpenAI, Google, Microsoft, AWS, Block, Bloomberg, and Cloudflare. The foundation governs three founding projects:

| Project | Created By | What It Standardizes | Adoption |
|---------|-----------|---------------------|----------|
| **MCP** (Model Context Protocol) | Anthropic (donated) | Tool connectivity -- how agents talk to external services | 10,000+ active public servers, 97M monthly SDK downloads |
| **AGENTS.md** | OpenAI (donated) | Project instructions -- how agents understand your codebase | 60,000+ open source projects |
| **goose** | Block (donated) | Open agent runtime -- reference implementation for agentic workflows | Open source agent framework |

A fourth standard, **Agent Skills** (the SKILL.md format), was created by Anthropic on December 18, 2025, and has been adopted by OpenAI, Microsoft (GitHub Copilot), Cursor, Atlassian, and Figma. The specification lives at agentskills.io.

**What this means for you**: The Skills you built in this chapter using `.claude/skills/` follow the same specification that Codex uses in `.agents/skills/` and Gemini CLI uses in `.gemini/skills/`. Different directory names, same format. Your Skills are portable.

---

## Three Philosophies, One Ecosystem

Each tool reflects a different design philosophy. None is universally "best" -- they excel at different work.

| | Claude Code | OpenAI Codex | Gemini CLI |
|---|---|---|---|
| **Philosophy** | "Measure twice, cut once" | "Move fast, iterate" | "Open and accessible" |
| **Execution** | Local terminal | Cloud sandbox + local | Local CLI + cloud inference |
| **Strengths** | Deep reasoning, accuracy, self-correction | Parallel tasks, async delegation, speed | Free tier, 1M context, open source |
| **Best for** | Complex refactoring, architecture work | Batch operations, exploration | Budget-conscious teams, large codebases |
| **Pricing** | $20+/month subscription | $20-$200/month (via ChatGPT) | Free (1,000 req/day) |
| **Open source** | No | CLI is open source (Rust) | Yes (Apache 2.0) |

Professional developers increasingly use multiple tools for different strengths. Claude Code for the careful architecture work. Codex for parallelized bulk tasks. Gemini CLI for quick queries against massive codebases. This is "poly-agentic" development -- choosing the right tool for each task, not committing to one forever.

---

## SWE-bench: The Coding Benchmark

SWE-bench is a benchmark that tests whether AI can solve real software engineering problems pulled from open source GitHub repositories. Unlike artificial coding challenges, SWE-bench tasks require reading existing code, understanding project context, and producing working fixes.

Multiple variants exist with different difficulty levels. **SWE-bench Verified** uses human-validated problems. **SWE-bench Pro** is harder, with more complex multi-file problems.

### SWE-bench Verified Leaderboard (February 2026)

| Rank | Model | Score |
|------|-------|-------|
| 1 | Claude Opus 4.5 | 80.9% |
| 2 | Claude Opus 4.6 | 80.8% |
| 3 | GPT-5.2 | 80.0% |
| 4 | Gemini 3 Flash | 78.0% |
| 5 | Claude Sonnet 4.5 | 77.2% |
| 6 | Gemini 3 Pro | 76.2% |

**Important caveat**: Companies report scores on different benchmark variants, making direct comparisons tricky. GPT-5.3-Codex scores 56.8% on SWE-bench Pro -- which is a harder test, not a worse score. When comparing models, always check which variant was used.

---

## Why This Matters for Your Career

The patterns you learned in this chapter are not Claude Code patterns. They are **industry patterns**.

When you write a CLAUDE.md file, you are practicing the same skill as writing an AGENTS.md file for Codex or a GEMINI.md file for Gemini CLI. When you build a Skill in `.claude/skills/`, you can port it to Codex or Gemini CLI by moving the SKILL.md file to a different directory. When you connect an MCP server, that same server works with every tool that supports the protocol.

This portability exists because the industry converged. The AAIF ensures that MCP servers, AGENTS.md files, and Agent Skills work the same way regardless of which coding agent you choose. Your investment in learning these patterns compounds across every tool you touch.

The developers who will thrive are not the ones who master one tool. They are the ones who understand the underlying patterns -- context files, skills, tool connectivity, orchestration -- and apply them wherever the work demands. That is what you built in this chapter.

---

## Try With AI

```
What are the architectural differences between you (Claude Code)
and OpenAI's Codex CLI? Be specific about execution model,
sandboxing, and where each tool runs code.
```

**What you're learning:** How to use an AI agent to analyze its own competitive landscape. Claude Code has direct knowledge of its own architecture and can reason about public information on competitors. This develops your ability to gather technical intelligence through AI conversation.

```
I have a skill at .claude/skills/my-skill/SKILL.md. Show me how
to create an equivalent for OpenAI Codex (in .agents/skills/)
and for Gemini CLI (in .gemini/skills/). What changes are needed
in each version?
```

**What you're learning:** Cross-vendor skill porting. The answer reveals how much of the SKILL.md format is universal (most of it) versus vendor-specific (directory path and minor configuration). This is the practical proof that your skills are portable.

```
Search the web for the latest SWE-bench Verified leaderboard.
How do Claude, GPT, and Gemini models compare? What should I
consider beyond benchmark scores when choosing a coding agent?
```

**What you're learning:** Critical evaluation of AI benchmarks. Scores matter, but so do execution model, pricing, context window, and workflow fit. This prompt teaches you to make tool decisions based on multiple factors, not just a single number.

---

## What's Next

You've completed the full Chapter 3 journey -- from your first Claude Code session through skills, MCP, hooks, plugins, agent teams, and now cross-vendor fluency. Next up: the **Chapter Quiz** (Lesson 31) to test your understanding across all 30 lessons.
