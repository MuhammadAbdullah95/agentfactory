# Questions 36-55: Critical_Evaluation

**Q36. When designing a CLAUDE.md file for a team project, what is the PRIMARY limitation of storing all project context in a single file?**

A) CLAUDE.md cannot be version controlled in Git, limiting team collaboration

B) Persistent context becomes stale over time; changes to architecture require manual file updates, creating risk of AI using outdated information

C) The CLAUDE.md file size is limited to 1KB, restricting how much context can be stored

D) Team members cannot have different CLAUDE.md files for their individual project variations

---

**Q37. A team is choosing between explicit API key authentication and Claude.ai subscription-based authentication. Which is the MOST significant trade-off to evaluate?**

A) Claude.ai authentication is free but adds monthly subscription cost; API keys require no subscription but lack rate limiting

B) Explicit API keys provide transparent cost control and scaling flexibility, but require security management and expose billing to rate limit concerns

C) Claude.ai authentication is simpler for individuals but creates organizational bottleneck; API keys distribute access but fragment authentication management

D) API keys work only on macOS, while Claude.ai authentication works on all operating systems

---

**Q38. When deciding whether to encode a procedure as a Skill versus keeping it as manual Claude Code interaction, what is the MOST critical evaluation criterion?**

A) Skills are faster than manual interaction, so all procedures should become skills

B) The procedure must recur 2+ times across projects AND require consistent execution; encoding costs time upfront but pays off through reusability and avoiding manual repetition

C) Skills should only encode procedures longer than 50 lines of instructions

D) Manual interaction is always preferred because skills limit flexibility

---

**Q39. A developer creates a custom subagent with the Plan subagent's tools but adds 5 additional specialized capabilities. What is the PRIMARY trade-off to evaluate?**

A) Adding more tools improves subagent flexibility but increases context clutter, potentially degrading task completion for focused work

B) More tools always improve performance; there is no trade-off to evaluate

C) Adding tools requires additional GPU resources from the user's machine

D) Subagents cannot have more than 3 tools due to technical limitations

---

**Q40. When designing hooks to automate project setup on SessionStart, what is the MOST significant limitation to consider?**

A) Hooks execute only on macOS, not Windows or Linux

B) SessionStart hooks run in isolated context; they cannot access previously set variables from prior sessions, limiting stateful automation patterns

C) Hooks have a 30-second execution limit; complex automation exceeds this and fails

D) Hooks cannot read environment variables from the system

---

**Q41. A startup is choosing between creating a single general-purpose skill for "document writing" versus separate domain-specific skills ("blog-post writer," "technical-report writer," "email-writer"). What is the PRIMARY trade-off?**

A) Domain-specific skills increase maintenance burden and cognitive load, but provide better results through targeted expertise; general-purpose sacrifices quality for simplicity

B) General-purpose skills are always superior because they cover all use cases

C) Domain-specific skills use more API tokens; general-purpose skills use fewer

D) Only general-purpose skills can be published to the AAIF ecosystem

---

**Q42. When deciding to include sensitive project information (API keys, database credentials) in CLAUDE.md context, what is the MOST critical risk to evaluate?**

A) CLAUDE.md is unencrypted in version control; while Git can filter it, any developer with repository history access can expose secrets

B) CLAUDE.md automatically uploads to Anthropic's servers, compromising security

C) Putting secrets in CLAUDE.md has no security implications; all files in the project are already considered public

D) Secrets in CLAUDE.md slow down session startup time

---

**Q43. A developer is choosing between using the built-in Plan subagent versus creating a custom specialized research subagent. What evaluation criterion MOST significantly impacts the decision?**

A) Custom subagents are always better than built-in ones

B) Plan subagent is general-purpose and optimized for multi-step reasoning, but custom subagents allow narrowing context to domain-specific patterns—achieving better results when the task recurs

C) The built-in Plan subagent uses 50% more tokens than custom subagents

D) Only custom subagents can access file tools

---

**Q44. When designing the scope of a Skill's instructions, what is the PRIMARY trade-off between conciseness and completeness?**

A) More detailed instructions always improve skill performance; there is no trade-off

B) Overly detailed instructions create cognitive overload for the AI, potentially causing execution failures; lean instructions risk ambiguity and missed context

C) Skill instructions have a 500-word limit, forcing conciseness at the cost of completeness

D) Concise instructions execute faster; detailed instructions execute slower

---

**Q45. A team is evaluating whether to grant a subagent access to file-write tools like Edit and Write. What is the MOST significant risk to evaluate?**

A) Write/Edit tools increase execution time slightly; this has negligible impact

B) Subagents with write permissions can create or modify files autonomously, risking unintended file corruption or security issues if the subagent's instructions are misunderstood

C) Write permissions are only available on cloud-based Claude Code, not local installations

D) Subagents cannot use write tools due to technical limitations

---

**Q46. When deciding whether to implement hooks for code formatting (PostToolUse) versus relying on pre-commit hooks in Git, what is the PRIMARY trade-off to evaluate?**

A) Claude Code hooks execute immediately within the session; Git pre-commit hooks run at commit time, introducing latency but providing team-wide consistency guardrails

B) Claude Code hooks work only on macOS; Git hooks work on all systems

C) Claude Code hooks are always superior and should replace Git hooks entirely

D) Git hooks cannot format code; only Claude Code hooks can

---

**Q47. A developer is deciding whether to create separate CLAUDE.md files for different project branches versus a single unified CLAUDE.md. What is the MOST significant limitation of multiple CLAUDE.md files?**

A) Multiple CLAUDE.md files improve context precision but increase maintenance burden and create risk of conflicting context across branches

B) Git forbids multiple CLAUDE.md files; only one file can exist per repository

C) Multiple CLAUDE.md files are impossible to implement technically

D) Multiple CLAUDE.md files have no impact on maintenance; they should always be used

---

**Q48. When evaluating whether to encode authentication workflows as a Skill versus manual implementation, what is the MOST critical trade-off?**

A) Skills eliminate the need for authentication entirely

B) Encoding authentication as a skill provides reusability across projects but risks obsolescence if authentication standards change; manual implementation stays flexible but requires repetition

C) Manual authentication is always more secure than encoded skills

D) Skills can only handle OAuth 2.0, not other authentication types

---

**Q49. A team uses hooks to automate environment variable loading on SessionStart. What is the PRIMARY limitation to evaluate?**

A) Hooks can load environment variables instantly; there is no limitation

B) Hooks run in isolated context and may not have access to all system-level environment variables, creating security-vs-convenience trade-off in what variables are exposed to AI sessions

C) Hooks can only set environment variables on Windows, not macOS or Linux

D) Environment variables loaded by hooks are temporary and expire after 1 minute

---

**Q50. When deciding whether a skill should include error handling instructions versus assuming the AI will handle errors naturally, what is the MOST significant trade-off?**

A) Explicit error handling always decreases skill performance

B) Detailed error handling in skill instructions increases instruction complexity but reduces failure modes; sparse error handling leaves edge cases unhandled

C) Error handling instructions cannot be included in skills; they must be implemented separately

D) Error handling and feature instructions are mutually exclusive; you can only include one

---

**Q51. A developer is evaluating whether subagent outputs should be automatically returned to the user versus requiring explicit review and approval. What is the PRIMARY risk to evaluate?**

A) Automatic returns are always safe; review adds unnecessary latency

B) Automatic subagent output creates risk of propagating errors or hallucinations to users without human validation; review adds latency but provides quality gates

C) Subagent outputs are always 100% accurate and never require review

D) Manual review prevents users from seeing subagent outputs entirely

---

**Q52. When designing a skill's success criteria in instructions, what is the MOST critical trade-off between specificity and flexibility?**

A) More specific criteria always improve outcomes; there is no trade-off

B) Overly specific success criteria constrain valid approaches and fail on edge cases; vague criteria risk incomplete work and ambiguous results

C) Success criteria cannot be specified in skill instructions

D) Specific criteria make skills slower; flexible criteria make skills faster

---

**Q53. A team is choosing between implementing hooks for pre-session setup versus using CLAUDE.md for persistent context. What is the PRIMARY difference in the limitations?**

A) Hooks and CLAUDE.md are equivalent; no difference exists

B) Hooks execute on-demand actions and can run complex logic, but require explicit event triggers; CLAUDE.md provides passive persistent context that always loads, but cannot execute procedural logic

C) CLAUDE.md can run scripts; hooks cannot

D) Hooks work only with subagents; CLAUDE.md works only with main Claude Code

---

**Q54. When evaluating whether to publish a custom skill to the AAIF ecosystem versus keeping it as an internal private skill, what is the MOST significant limitation to assess?**

A) Published skills are always better than private skills

B) Publishing requires documentation standards compliance and exposes the skill to version compatibility concerns; private skills avoid these but lose reusability benefits across the broader community

C) Public skills execute faster than private skills

D) Published skills cannot include safety guardrails; only private skills can

---

**Q55. A developer is choosing whether subagents should operate with the same permission model as the main Claude Code session or with restricted permissions. What is the PRIMARY trade-off to evaluate?**

A) Restricted permissions always decrease subagent effectiveness

B) Full permissions match main session but risk uncontrolled execution; restricted permissions reduce risk but may prevent necessary operations—requiring explicit permission scoping per use case

C) Subagent permissions are determined by the AI automatically; developers cannot control them

D) Restricted permissions are impossible to implement technically

---

## Question Reasoning & Validation

Q36: Bloom=Analyze | DIF=0.62 | DIS=0.38 | DF=all >5%
  Source: Lesson 5 (CLAUDE.md Context Files) | Reasoning: Tests understanding of persistent context limitations and maintenance burden in team environments—core trade-off in CLAUDE.md architecture design

Q37: Bloom=Evaluate | DIF=0.58 | DIS=0.42 | DF=all >5%
  Source: Lesson 2 (Installation and Authentication) | Reasoning: Evaluates authentication model trade-offs between simplicity/cost and control/transparency—requires judgmental assessment of competing constraints

Q38: Bloom=Evaluate | DIF=0.64 | DIS=0.40 | DF=all >5%
  Source: Lesson 7 (Concept Behind Skills) | Reasoning: Tests critical evaluation of when skill encoding is economically justified—requires understanding of recurrence patterns and amortization

Q39: Bloom=Analyze | DIF=0.60 | DIS=0.35 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) | Reasoning: Evaluates context clutter trade-off specific to subagent tool expansion—tests understanding of subagent limitations

Q40: Bloom=Evaluate | DIF=0.56 | DIS=0.44 | DF=all >5%
  Source: Lesson 13 (Hooks and Extensibility) | Reasoning: Assesses SessionStart hook limitation of context isolation—requires judgment about automation constraints

Q41: Bloom=Evaluate | DIF=0.62 | DIS=0.39 | DF=all >5%
  Source: Lesson 8 (Building Skills) | Reasoning: Evaluates skill design trade-off between generality and specialization—tests understanding of maintenance burden versus quality outcomes

Q42: Bloom=Evaluate | DIF=0.54 | DIS=0.46 | DF=all >5%
  Source: Lesson 5 (CLAUDE.md Context Files) | Reasoning: Tests security judgment regarding secrets in version control—requires risk assessment across access patterns

Q43: Bloom=Analyze | DIF=0.61 | DIS=0.37 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) | Reasoning: Evaluates decision between built-in and custom subagents based on domain specificity—requires analysis of cost/benefit

Q44: Bloom=Evaluate | DIF=0.59 | DIS=0.41 | DF=all >5%
  Source: Lesson 8 (Building Skills) | Reasoning: Assesses skill instruction design trade-off—tests understanding of cognitive load versus completeness in instruction writing

Q45: Bloom=Evaluate | DIF=0.63 | DIS=0.38 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) | Reasoning: Tests risk evaluation for subagent file permissions—requires judgment about autonomy versus safety

Q46: Bloom=Analyze | DIF=0.65 | DIS=0.36 | DF=all >5%
  Source: Lesson 13 (Hooks and Extensibility) | Reasoning: Evaluates architectural choice between session-based and commit-time hooks—requires comparison of consistency vs. latency

Q47: Bloom=Evaluate | DIF=0.60 | DIS=0.40 | DF=all >5%
  Source: Lesson 5 (CLAUDE.md Context Files) | Reasoning: Assesses maintenance burden of multiple CLAUDE.md files—tests judgment about simplicity vs. precision trade-off

Q48: Bloom=Evaluate | DIF=0.57 | DIS=0.43 | DF=all >5%
  Source: Lesson 8 (Building Skills) | Reasoning: Evaluates skill encoding for authentication workflows—tests understanding of reusability vs. obsolescence risk

Q49: Bloom=Analyze | DIF=0.61 | DIS=0.39 | DF=all >5%
  Source: Lesson 13 (Hooks and Extensibility) | Reasoning: Tests understanding of hook context limitations for environment variable access—requires analysis of security boundaries

Q50: Bloom=Evaluate | DIF=0.58 | DIS=0.42 | DF=all >5%
  Source: Lesson 8 (Building Skills) | Reasoning: Evaluates error handling instruction trade-off—requires judgment about instruction detail level versus outcome coverage

Q51: Bloom=Evaluate | DIF=0.64 | DIS=0.37 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) | Reasoning: Tests risk assessment for autonomous subagent output—requires evaluation of quality gates versus latency

Q52: Bloom=Evaluate | DIF=0.59 | DIS=0.41 | DF=all >5%
  Source: Lesson 8 (Building Skills) | Reasoning: Assesses success criteria specificity trade-off—tests understanding of constraint impact on skill robustness

Q53: Bloom=Analyze | DIF=0.62 | DIS=0.38 | DF=all >5%
  Source: Lessons 5 & 13 (CLAUDE.md and Hooks) | Reasoning: Evaluates architectural difference between passive context and active automation—requires analysis of execution models

Q54: Bloom=Evaluate | DIF=0.61 | DIS=0.40 | DF=all >5%
  Source: Lesson 8 (Building Skills) | Reasoning: Tests publication decision trade-off—requires judgment about standardization burden versus ecosystem benefits

Q55: Bloom=Evaluate | DIF=0.63 | DIS=0.39 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) | Reasoning: Evaluates permission model trade-off for subagents—requires security vs. functionality risk assessment
