# Questions 76-100: Decision_Matrix

**Q76. Your team must choose between creating a reusable Claude Code skill or writing a standalone script. The decision factors are: reusability across 5+ projects, maintenance burden, documentation needs, and learning curve. Which analysis BEST captures the trade-offs?**

A) Skills require more upfront effort but enable reuse; scripts are faster initially but duplicate work across projects and create maintenance burden when patterns change

B) Skills are always better because they're more professional and industry-standard

C) Scripts are simpler and don't require understanding Claude Code architecture

D) The choice depends only on project deadline, not on reusability or team size

---

**Q77. A project needs context management for long-running features. Your options are: CLAUDE.md (persistent, checked into git), .claude/settings.json (user-level, not shared), or session-based context (manual each time). Which decision framework BEST guides the choice?**

A) Session context if team is small; settings.json if only one developer needs it; CLAUDE.md if the team shares standards that should persist across all developers and sessions

B) Always use CLAUDE.md because it's the most advanced option

C) Use settings.json for all cases to avoid git conflicts

D) Persistent context is unnecessary if developers communicate regularly

---

**Q78. Your team has three specialized tasks that recur monthly: code review prep, security scanning, and performance analysis. You must decide how to encapsulate these: as separate skills, as a single unified skill, or as individual MCP integrations. What BEST captures the decision factors?**

A) Separate skills enable independent updates, clear ownership, and easy sharing; unified skill is simpler but harder to reuse parts independently; MCP is better for external systems

B) Always combine into one skill to keep Claude Code organized

C) Skills and MCP serve the same purpose, so the choice is arbitrary

D) Each task should be a separate MCP because MCP is the standard

---

**Q79. You're designing configuration for a distributed team (10+ developers across 3 locations, different OS, different model preferences). Which settings hierarchy strategy BEST handles this complexity?**

A) User settings for individual model/API preferences; Project settings (git-checked) for team coding standards; Local settings for developer's machine-specific overrides

B) Single project-wide settings so everyone has identical configuration

C) Each developer creates their own CLAUDE.md to avoid conflicts

D) Settings aren't important for distributed teams; just use defaults

---

**Q80. A feature requires Claude Code to understand your custom ORM library (domain knowledge). You can: teach Claude via CLAUDE.md context, build an MCP server that exposes ORM queries, or create a skill that knows common ORM patterns. Which approach BEST maximizes clarity and reusability?**

A) CLAUDE.md for project-level patterns and examples; MCP if you need Claude to actually query the ORM at runtime; Skill if the ORM knowledge applies across many projects

B) Build the most complex solution (MCP) to show technical depth

C) Just write more detailed comments in code; Claude will understand

D) ORM knowledge doesn't matter; use generic SQL questions instead

---

**Q81. Your workflow involves invoking Claude Code for planning, then subagents for implementation, then verification. A constraint: planning decisions often affect implementation choices. Which orchestration pattern BEST handles this dependency?**

A) Plan sequentially: main agent plans, returns plan to subagent, subagent executes, main agent verifies — allows main agent to refine plan based on subagent feedback

B) Run planning and implementation in parallel to save time

C) Subagents handle everything; the main agent doesn't need to verify

D) Dependencies between tasks don't matter in modern development

---

**Q82. Your project spans microservices (5 services, each with Claude Code contexts) and a shared skill library. When team standards change, you must update multiple places. Which decision captures the cost of consistency?**

A) Shared skills in one central location (checked into git) + service-specific CLAUDE.md overrides; changes to standards update skills once and propagate; service differences still allowed

B) Copy the same CLAUDE.md to each service to ensure consistency

C) Don't worry about consistency; let each service maintain separate standards

D) Standards changes should always be manual updates to avoid automation complexity

---

**Q83. You need Claude to review code against your company's security guidelines (100+ rules). The review process recurs monthly. Which approach BEST balances thoroughness, maintainability, and reusability?**

A) Store guidelines in CLAUDE.md with rule categories; create a skill that orchestrates focused review for each category; invoke skill from project context

B) Manually paste guidelines into every Claude Code session

C) Security reviews are too complex for Claude; always hire specialists

D) Guidelines change constantly, so don't codify them anywhere

---

**Q84. Two workflows compete: Workflow A (manual each step, flexible) vs Workflow B (automated subagents, repeatable). Constraints: time budget (limited), skill diversity (team has only 2 people), change frequency (requirements change weekly). Which analysis BEST recommends a choice?**

A) Manual workflow is better when constraints emphasize flexibility and team capacity; automate when proven patterns recur and need speed; hybrid (manual orchestration + automated details) balances both

B) Always automate everything to maximize efficiency

C) Always manual to maximize flexibility

D) Automation and flexibility are mutually exclusive

---

**Q85. Your startup has one core Claude Code skill (customer-facing feature). It's critical that this skill works reliably. You must decide: test it manually each release, use automated testing with GitHub Actions, or use Claude Code's internal verification loop. Which strategy BEST minimizes risk?**

A) Automated testing (CI/CD) catches breakage; Claude Code verification loop validates logic during development; manual spot-checks verify integration — defense in depth

B) Manual testing is always sufficient if developers are careful

C) Automated testing eliminates the need for verification logic

D) Testing is secondary to shipping fast

---

**Q86. A skill needs access to three different data sources: APIs (live data), local files (config), and databases (reference data). Which tool combination BEST handles this without overwhelming skill complexity?**

A) MCP for live APIs (external connectivity); local files through CLAUDE.md examples (knowledge); database queries through skill documentation (reference patterns)

B) Everything should be an MCP because MCP is more advanced

C) Everything should be local files to avoid external dependencies

D) Different data sources require entirely different skills

---

**Q87. Your team uses Claude Code to build microservices. A developer asks: "Should I put all service context in CLAUDE.md, or just the shared architectural patterns?" Which guidance BEST captures the decision?**

A) CLAUDE.md should contain service-shared patterns (standards, conventions) and high-level structure; service-specific implementation details stay in code comments — balances context reuse with clarity

B) Put everything in CLAUDE.md for consistency

C) CLAUDE.md isn't necessary for microservices

D) Each service should have completely separate context with no shared patterns

---

**Q88. A project demands tight integration: Claude Code must read a database schema, understand business rules, and generate accurate data migration scripts. Failure cost is high (production data). Which design approach BEST balances automation with safety?**

A) Skill encapsulates migration patterns + MCP for live schema access + automated testing + manual verification step before execution

B) One-off script without verification

C) Full automation without manual gates

D) Don't automate data migrations; always manual

---

**Q89. Your CLAUDE.md has grown to 500 lines (project overview, file structure, 50+ coding standards, 20+ examples, shell commands, context rules). Reading time is now significant. Which refactoring strategy BEST preserves clarity?**

A) Extract standards into separate docs in .claude/ directory; CLAUDE.md summarizes high-level context and links to details; subagents read full standards as needed

B) Keep everything in one file for simplicity

C) Delete standards to reduce complexity

D) Longer context files improve understanding

---

**Q90. A feature requires multiple subagents (research, implementation, testing). Each must hand off work to the next. Constraint: each subagent must complete independently without waiting for main agent feedback. Which orchestration pattern BEST fits?**

A) Sequential: Main agent spawns subagent 1 (research), gets results, spawns subagent 2 (implementation with research outputs), spawns subagent 3 (testing with implementation outputs)

B) Parallel: All subagents run simultaneously without dependencies

C) All work happens in the main agent to avoid handoff complexity

D) Dependencies between work phases don't matter in modern development

---

**Q91. Your project uses skills in two contexts: local Claude Code development and a production API server. The skill logic is identical, but deployment environments differ. Which approach BEST separates concerns?**

A) Skill contains pure logic (no environment assumptions); wrapper scripts/APIs handle environment-specific configuration (paths, API keys, databases) — reuse skill logic, vary environment

B) Create duplicate skills for each environment

C) Environment doesn't matter; use identical deployment everywhere

D) Skills can't be reused across deployment contexts

---

**Q92. A skill must handle both simple requests (90% of cases, 10ms response) and complex scenarios (10% of cases, 10s response). User expectations: fast responses, complete solutions. Which design BEST balances speed and thoroughness?**

A) Main skill handles simple cases quickly; complex scenarios delegate to deeper analysis subagent; caller chooses depth based on needs

B) Always do deep analysis for every request

C) Only handle simple cases to maintain speed

D) Speed and thoroughness are always opposite

---

**Q93. Your team reviews an incident: Claude Code created a skill, but 5 developers didn't update it when team standards changed. Knowledge capture failed. Which prevention strategy BEST prevents recurrence?**

A) Version skills in git with release notes; include "Last Updated" in skill metadata; document where each skill is used; update CLAUDE.md when team standards change to trigger awareness

B) Recreate skills frequently to keep them fresh

C) Don't share skills; let each developer create their own

D) Skill updates never matter; old skills work the same forever

---

**Q94. A complex orchestration involves: main agent creating a plan, 3 parallel subagents executing tasks, main agent synthesizing results. Failure in one subagent shouldn't block others. Which architecture BEST handles partial failures?**

A) Main agent spawns 3 subagents in parallel; if one fails, captures error, lets others complete, synthesizes available results with failure notes in report

B) One subagent failure stops entire orchestration

C) Run subagents sequentially to prevent any failures

D) Failures are rare enough to ignore

---

**Q95. You must document a complex Claude Code workflow for a junior developer. The workflow involves 4 lessons learned (from Chapter 5), 3 custom skills, 2 subagent orchestrations. Which documentation structure BEST enables understanding?**

A) CLAUDE.md documents high-level workflow (links to lessons); each skill documented inline with examples; workflow diagram shows subagent orchestration; developer reads CLAUDE.md first, then follows links

B) One giant narrative document explaining everything

C) No documentation; assume junior developers figure it out

D) Separate documentation for each component with no cross-linking

---

**Q96. A skill depends on three external systems (API, database, file system). Failure tolerance: API can fail temporarily; database cannot fail; file system rarely fails. Which error handling strategy BEST matches tolerance?**

A) Database failures: immediately propagate error, fail fast; API failures: retry with backoff + graceful degradation; file system failures: log and continue with defaults

B) Treat all failures identically

C) Ignore all failures and assume everything works

D) Errors don't depend on the external system

---

**Q97. Your organization has 20 Claude Code projects, each with CLAUDE.md. New architecture guidance requires changes to all 20. Manual updates take 10 hours. Which solution BEST scales to this complexity?**

A) Shared skill containing organization standards + templates; CLAUDE.md references (imports) the shared skill; one update to shared skill propagates to all projects

B) Manually edit all 20 CLAUDE.md files

C) Ignore the need for consistency across projects

D) Start a new organization with fresh standards

---

**Q98. A development team alternates between: week 1 (rapid prototyping, many small tasks), week 2 (quality hardening, few complex tasks, high rigor). Which Claude Code configuration strategy BEST adapts to this rhythm?**

A) Project settings for shared standards; local settings for weekly overrides (verbose AI logging in week 2, permissive in week 1); switch local config between weeks

B) Use identical configuration every week

C) Only use configuration for stable, unchanging projects

D) Weekly changes are too frequent for configuration management

---

**Q99. You're designing a skill that orchestrates multiple specialized subagents. Each subagent must operate independently, but output quality depends on correct handoff order and data format. Which validation approach BEST ensures reliability?**

A) Skill validates: (1) subagent output format before passing to next, (2) completion status before continuing, (3) entire pipeline results before returning; detailed error messages guide fixes

B) Trust subagents to work correctly without validation

C) Validation adds unnecessary complexity

D) Output format doesn't affect reliability

---

**Q100. Your company's Claude Code strategy must grow with the organization: 5 developers today, 50 developers in 3 years. Skills, CLAUDE.md, subagents will scale differently. Which architectural decision BEST enables this growth?**

A) Build shared skill library (version controlled, reviewed) + CLAUDE.md standards (imported from shared library) + subagent framework (with governance) — creates growth-friendly infrastructure

B) Manual, project-specific configurations until scaling becomes necessary

C) Assume current architecture works forever

D) Growth requires rebuilding everything from scratch

---

## Question Reasoning & Validation

Q76: Bloom=Apply | DIF=0.62 | DIS=0.36 | DF=all >5%
  Source: Lesson 07 (Concept Behind Skills) | Reasoning: Compares skill vs script trade-offs across maintenance, reusability, and effort dimensions from Chapter 5's skill architecture understanding

Q77: Bloom=Analyze | DIF=0.58 | DIS=0.38 | DF=all >5%
  Source: Lesson 05 (CLAUDE.md Context Files) | Reasoning: Requires multi-factor decision (team size, permanence, sharing, version control) about context management approaches

Q78: Bloom=Analyze | DIF=0.60 | DIS=0.40 | DF=all >5%
  Source: Lessons 07-08 (Skills), Lesson 09 (MCP Integration) | Reasoning: Decision matrix comparing skill granularity vs MCP integration trade-offs for different task types

Q79: Bloom=Apply | DIF=0.64 | DIS=0.34 | DF=all >5%
  Source: Lesson 12 (Settings Hierarchy) | Reasoning: Applies three-level hierarchy concept to distributed team constraints (OS, location, preferences)

Q80: Bloom=Evaluate | DIF=0.56 | DIS=0.42 | DF=all >5%
  Source: Lessons 05, 09-10 (CLAUDE.md, MCP, Skills) | Reasoning: Domain knowledge encapsulation requires choosing between context, connectivity, and expertise based on reusability

Q81: Bloom=Analyze | DIF=0.59 | DIS=0.39 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) | Reasoning: Sequential vs parallel dependency handling when planning affects implementation

Q82: Bloom=Evaluate | DIF=0.54 | DIS=0.43 | DF=all >5%
  Source: Lesson 05 (CLAUDE.md), Lesson 07 (Skills) | Reasoning: Trade-off between centralized standards (consistency cost) and distributed customization (maintenance cost)

Q83: Bloom=Apply | DIF=0.61 | DIS=0.37 | DF=all >5%
  Source: Lesson 05 (CLAUDE.md), Lesson 07-08 (Skills) | Reasoning: Choosing encapsulation for recurring, domain-specific task (security guidelines)

Q84: Bloom=Analyze | DIF=0.63 | DIS=0.35 | DF=all >5%
  Source: Lesson 06 (Three Roles/Teaching Claude), Lesson 11 (Orchestration) | Reasoning: Manual vs automated workflow selection based on time, team capacity, and change frequency constraints

Q85: Bloom=Apply | DIF=0.58 | DIS=0.41 | DF=all >5%
  Source: Lesson 17 (Creator Workflow—verification patterns) | Reasoning: Risk mitigation through layered testing and verification specific to critical production skills

Q86: Bloom=Analyze | DIF=0.62 | DIS=0.36 | DF=all >5%
  Source: Lessons 05, 09-10 (Context files, MCP, Skill architecture) | Reasoning: Complexity management for skill integrating multiple data sources via different mechanisms

Q87: Bloom=Apply | DIF=0.60 | DIS=0.38 | DF=all >5%
  Source: Lesson 05 (CLAUDE.md Context Files) | Reasoning: Context granularity decision for shared vs service-specific knowledge in microservices context

Q88: Bloom=Evaluate | DIF=0.52 | DIS=0.44 | DF=all >5%
  Source: Lesson 17 (Creator Workflow—verification) | Reasoning: Safety-automation trade-off for high-stakes automation (production data) requiring layered safeguards

Q89: Bloom=Apply | DIF=0.64 | DIS=0.33 | DF=all >5%
  Source: Lesson 05 (CLAUDE.md Context Files) | Reasoning: Context scaling and maintainability through documentation organization and reference architecture

Q90: Bloom=Analyze | DIF=0.59 | DIS=0.39 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) | Reasoning: Sequential handoff pattern with independent completion for multi-step workflows

Q91: Bloom=Evaluate | DIF=0.55 | DIS=0.42 | DF=all >5%
  Source: Lesson 07 (Skill Architecture), Lesson 10 (Compiling MCP to Skills) | Reasoning: Skill portability across deployment contexts through separation of logic from environment

Q92: Bloom=Apply | DIF=0.61 | DIS=0.37 | DF=all >5%
  Source: Lesson 11 (Subagents), Lesson 17 (Creator Workflow patterns) | Reasoning: Performance-completeness trade-off resolved through request-type delegation

Q93: Bloom=Evaluate | DIF=0.57 | DIS=0.40 | DF=all >5%
  Source: Lesson 05 (CLAUDE.md), Lesson 08 (Agent Skills) | Reasoning: Organizational knowledge capture and skill discoverability through versioning, metadata, and change communication

Q94: Bloom=Analyze | DIF=0.60 | DIS=0.38 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) | Reasoning: Parallel execution with partial failure tolerance and result synthesis

Q95: Bloom=Apply | DIF=0.65 | DIS=0.32 | DF=all >5%
  Source: Lessons 05, 07, 11 (CLAUDE.md, Skills, Orchestration) | Reasoning: Documentation structure for cross-component workflows with progressive disclosure

Q96: Bloom=Analyze | DIF=0.63 | DIS=0.35 | DF=all >5%
  Source: Lesson 17 (Creator Workflow—error handling implicit in verification) | Reasoning: Error handling strategy matched to failure tolerance levels per component

Q97: Bloom=Evaluate | DIF=0.56 | DIS=0.41 | DF=all >5%
  Source: Lessons 05, 07 (CLAUDE.md, Skills organization) | Reasoning: Scaling configuration management across 20+ projects through shared library and reference architecture

Q98: Bloom=Apply | DIF=0.62 | DIS=0.36 | DF=all >5%
  Source: Lesson 12 (Settings Hierarchy) | Reasoning: Configuration adaptation to cyclical team workflow patterns using hierarchy overrides

Q99: Bloom=Evaluate | DIF=0.58 | DIS=0.40 | DF=all >5%
  Source: Lesson 11 (Subagents), Lesson 17 (Verification patterns) | Reasoning: Validation strategy for orchestrated subagent pipelines ensuring data integrity and error propagation

Q100: Bloom=Analyze | DIF=0.59 | DIS=0.39 | DF=all >5%
  Source: Lesson 16 (Strategic Tool Selection), Lessons 05-14 (All tools) | Reasoning: Architecture scalability from 5 to 50 developers through skill libraries, configuration standards, and governance framework
