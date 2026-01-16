# Questions 56-75: Architecture_Analysis

**Q56. In Claude Code's architecture, MCP servers and Skills solve complementary problems in system integration. Which statement BEST describes their primary architectural distinction?**

A) MCP servers provide token-efficient access to external systems; Skills encode expertise for internal Claude processing

B) Skills connect to external systems; MCP servers handle internal knowledge representation

C) Both solve identical problems but MCP is older technology

D) MCP and Skills are interchangeable components with no architectural difference

---

**Q57. When designing a multi-task workflow where Claude Code must: (1) research competitor websites, (2) analyze documentation, and (3) generate design recommendations, what architectural pattern does Claude Code apply to prevent context clutter?**

A) A single monolithic agent with all capabilities loaded into one context window

B) Specialized subagents with isolated context windows, each handling focused tasks

C) Sequential tool invocation in a shared context

D) Multiple separate Claude Code instances running in parallel

---

**Q58. According to Lesson 9 (MCP Integration), the relationship between MCP and Skills can be visualized as complementary access paths. Which component PRIMARY role does MCP serve in this architecture?**

A) MCP stores expertise patterns that Claude Code learns from

B) MCP provides safe, standardized access to external systems and data sources

C) MCP replaces the need for local files in Claude Code

D) MCP encrypts all communication with external services

---

**Q59. The "code execution pattern" described in Lesson 10 demonstrates a critical architectural principle: moving processing logic from Claude's context to local scripts. What is the PRIMARY benefit of this pattern?**

A) Local scripts are more secure than MCP calls

B) Reduces token consumption by up to 98.7% while maintaining full functionality

C) Local scripts always execute faster than network calls

D) Eliminates the need for MCP servers entirely

---

**Q60. In Claude Code's settings hierarchy (Lesson 12), configuration can exist at three levels: user, project, and local. Which architectural principle does this three-level design reflect?**

A) Layered access control with precedence order (local > project > user)

B) Random settings distribution across multiple files

C) All configurations should be identical regardless of scope

D) Settings cannot conflict between different levels

---

**Q61. When a team member joins a project using Claude Code, they need to understand which settings configurations should be version-controlled (shared) and which should be in .gitignore (local-only). This distinction reflects which architectural concern?**

A) Preventing team coordination through isolation

B) Separating shared team standards from personal customization

C) Making all settings identical for all team members

D) Eliminating the need for configuration management

---

**Q62. Hooks in Claude Code (Lesson 13) implement an event-driven architecture. Which component relationship does this pattern establish?**

A) Synchronous blocking calls that halt Claude's execution

B) Event-trigger-action pattern where hooks automatically execute on specific lifecycle events

C) Manual invocation of arbitrary code without event correlation

D) Hooks cannot interact with Claude Code's execution flow

---

**Q63. In the hooks architecture (Lesson 13), a SessionStart hook that loads project context before Claude begins working demonstrates which integration pattern?**

A) Post-processing external data after Claude completes work

B) Pre-processing automation that initializes system state before main execution

C) Concurrent parallel processing unrelated to Claude's workflow

D) Hooks only support cleanup operations, not initialization

---

**Q64. Subagents (Lesson 11) isolate context and maintain independent execution scope. This architectural choice primarily addresses which system-level concern?**

A) Reducing Claude Code's capability level

B) Preventing context clutter and distraction in long multi-task workflows

C) Forcing sequential execution that slows down processing

D) Eliminating team coordination entirely

---

**Q65. When Claude Code's Plan subagent automatically activates for complex tasks, the system demonstrates which architectural principle?**

A) Automatic delegation of work to specialized components based on task complexity

B) Random invocation of subagents without logic

C) All tasks must be handled by the main Claude Code agent

D) Subagents can only be invoked manually with explicit commands

---

**Q66. Lesson 14 (Plugins) describes plugins as bundled capabilities combining skills, agents, hooks, and MCP. This composition architecture serves which primary purpose?**

A) Simplifying reuse by packaging related capabilities together for installation

B) Complicating system architecture unnecessarily

C) Making it impossible to use skills independently

D) Eliminating the need for modular component design

---

**Q67. In Claude Code's architecture, why does compiling high-token MCP servers into Skills (Lesson 10) achieve 98.7% token reduction while preserving functionality?**

A) Skills use less accurate algorithms than MCP

B) Local script execution replaces eager loading of all MCP tool definitions upfront

C) Skills eliminate external data access capabilities

D) Token reduction is achieved through data compression only

---

**Q68. The architectural pattern where CLAUDE.md teaches Claude "how" to work, while MCP servers provide "where" to find information (Lesson 9), reflects which system design principle?**

A) Combining expertise encoding (CLAUDE.md) with external data access (MCP) for complete agent capability

B) Eliminating the need for context files through MCP alone

C) Making CLAUDE.md and MCP interchangeable components

D) Preventing Claude from accessing external information

---

**Q69. When designing a team workflow, the settings hierarchy with precedence order (local > project > user) allows which architectural flexibility?**

A) Identical settings enforced across all team members equally

B) Individual customization at local level while maintaining shared project standards

C) Preventing team coordination through fragmented configuration

D) Settings cannot be organized hierarchically

---

**Q70. Subagent execution follows a "one task, one completion, return control" model (Lesson 11). This constraint primarily enables which architectural benefit?**

A) Preventing subagents from completing any work

B) Ensuring focused task execution with clean context isolation and predictable control flow

C) Forcing long-running background processes

D) Eliminating the need for task monitoring

---

**Q71. In the MCP architecture described in Lesson 9, the relationship between MCP servers and CLAUDE.md demonstrates which integration principle?**

A) MCP handles external system connections while CLAUDE.md encodes internal expertise and guidelines

B) Both components serve identical functions

C) CLAUDE.md should replace MCP servers

D) External and internal processing cannot be distinguished

---

**Q72. The hooks architecture (Lesson 13) supporting PreToolUse, PostToolUse, SessionStart, and SessionEnd events enables which workflow pattern?**

A) Preventing automation of any system behavior

B) Event-driven workflow automation at multiple lifecycle points for initialization, monitoring, and cleanup

C) Forcing all operations to be manual

D) Hooks cannot execute multiple event types

---

**Q73. When Claude Code automatically invokes the Plan subagent for complex multi-step tasks, the system demonstrates which architectural principle from Lesson 11?**

A) Complexity detection triggering appropriate delegation to specialized components

B) Random unpredictable behavior without pattern

C) All tasks requiring manual subagent invocation

D) Subagents cannot be invoked automatically

---

**Q74. The plugin architecture (Lesson 14) that bundles skills, agents, hooks, and MCP into reusable units supports which team adoption pattern?**

A) Preventing teams from sharing capabilities

B) Simplifying onboarding by allowing team members to install pre-configured capability bundles matching their workflow needs

C) Forcing every team to build plugins from scratch

D) Plugins eliminate the need for individual components

---

**Q75. Across Claude Code's architecture (MCP, Skills, Subagents, Settings, Hooks, Plugins), which overarching design principle appears most consistently?**

A) Monolithic architecture with tightly coupled components

B) Layered composition enabling specialized components to integrate through clear boundaries and orchestration

C) Random component selection without architectural patterns

D) Preventing component reuse or sharing

---

## Question Reasoning & Validation

Q56: Bloom=Analyze | DIF=0.62 | DIS=0.42 | DF=all >5%
  Source: Lesson 9 (MCP Integration) + Lesson 8 (Agent Skills) | Reasoning: Distinguishes complementary architectural roles of external access (MCP) vs internal expertise encoding (Skills), core integration pattern in Chapter 5

Q57: Bloom=Apply | DIF=0.58 | DIS=0.45 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) | Reasoning: Applies subagent architecture to multi-task workflow scenario, demonstrates understanding of context isolation for complexity management

Q58: Bloom=Understand | DIF=0.65 | DIS=0.38 | DF=all >5%
  Source: Lesson 9 (MCP Integration) | Reasoning: Recalls primary role of MCP from lesson introduction, differentiates MCP from internal components

Q59: Bloom=Apply | DIF=0.60 | DIS=0.43 | DF=all >5%
  Source: Lesson 10 (Compiling MCP to Skills) | Reasoning: Applies token optimization principle to code execution pattern, core architectural benefit from Anthropic blog reference in lesson

Q60: Bloom=Analyze | DIF=0.64 | DIS=0.41 | DF=all >5%
  Source: Lesson 12 (Settings Hierarchy) | Reasoning: Analyzes three-level architecture and identifies precedence principle (local > project > user), demonstrates architectural understanding

Q61: Bloom=Apply | DIF=0.61 | DIS=0.44 | DF=all >5%
  Source: Lesson 12 (Settings Hierarchy) | Reasoning: Applies .gitignore pattern understanding to distinguish shared vs local configuration, team coordination principle

Q62: Bloom=Understand | DIF=0.67 | DIS=0.36 | DF=all >5%
  Source: Lesson 13 (Hooks and Extensibility) | Reasoning: Identifies event-driven architecture pattern that hooks implement, core conceptual foundation

Q63: Bloom=Apply | DIF=0.59 | DIS=0.46 | DF=all >5%
  Source: Lesson 13 (Hooks and Extensibility) | Reasoning: Applies pre-processing initialization pattern using SessionStart hook, demonstrates practical understanding of lifecycle integration

Q64: Bloom=Analyze | DIF=0.62 | DIS=0.42 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) | Reasoning: Analyzes architectural benefit of context isolation in subagents, addresses "context clutter" problem described in lesson

Q65: Bloom=Apply | DIF=0.63 | DIS=0.39 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) | Reasoning: Applies automatic delegation principle where Plan subagent activates based on complexity, demonstrates understanding of intelligent component activation

Q66: Bloom=Understand | DIF=0.68 | DIS=0.35 | DF=all >5%
  Source: Lesson 14 (Plugins: Putting It All Together) | Reasoning: Recalls plugin composition architecture bundling multiple capabilities, foundational concept for capstone lesson

Q67: Bloom=Analyze | DIF=0.56 | DIS=0.48 | DF=all >5%
  Source: Lesson 10 (Compiling MCP to Skills) | Reasoning: Analyzes mechanism of token reduction through code execution pattern vs eager MCP loading, sophisticated understanding of optimization architecture

Q68: Bloom=Analyze | DIF=0.61 | DIS=0.44 | DF=all >5%
  Source: Lesson 9 (MCP Integration) - "Skills teach HOW, MCP teaches WHERE" | Reasoning: Distinguishes complementary roles of expertise encoding vs external access, demonstrates systems thinking about architecture

Q69: Bloom=Apply | DIF=0.64 | DIS=0.40 | DF=all >5%
  Source: Lesson 12 (Settings Hierarchy) | Reasoning: Applies hierarchy precedence principle to enable both team standardization and individual customization, practical team coordination

Q70: Bloom=Apply | DIF=0.60 | DIS=0.45 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) - "one task, one completion, return control" | Reasoning: Applies subagent execution model constraint to explain benefits of context isolation and predictability

Q71: Bloom=Analyze | DIF=0.63 | DIS=0.42 | DF=all >5%
  Source: Lesson 9 (MCP Integration) + Lesson 6 (CLAUDE.md) | Reasoning: Distinguishes complementary architectural roles of external integration (MCP) vs internal configuration (CLAUDE.md)

Q72: Bloom=Apply | DIF=0.62 | DIS=0.43 | DF=all >5%
  Source: Lesson 13 (Hooks and Extensibility) | Reasoning: Applies event-driven architecture across multiple lifecycle hooks, demonstrates understanding of multi-point automation

Q73: Bloom=Analyze | DIF=0.61 | DIS=0.44 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) | Reasoning: Analyzes automatic delegation pattern triggered by complexity detection, demonstrates understanding of intelligent component orchestration

Q74: Bloom=Apply | DIF=0.65 | DIS=0.38 | DF=all >5%
  Source: Lesson 14 (Plugins: Putting It All Together) | Reasoning: Applies plugin architecture to team adoption scenario, demonstrates understanding of capability bundling for knowledge transfer

Q75: Bloom=Analyze | DIF=0.64 | DIS=0.41 | DF=all >5%
  Source: All Chapter 5 Lessons (9-14) | Reasoning: Analyzes cross-cutting architectural principle of layered composition and clear component boundaries throughout Claude Code platform

