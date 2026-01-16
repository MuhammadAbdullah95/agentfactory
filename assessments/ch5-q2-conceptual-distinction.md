# Questions 16-35: Conceptual_Distinction

**Q16. Which BEST differentiates a skill from direct CLAUDE.md instructions in terms of scope and reusability?**

A) Skills apply only to current project; CLAUDE.md is global across all projects

B) Skills encode reusable expertise patterns that persist across multiple projects; CLAUDE.md provides persistent project-specific context

C) Skills require explicit invocation; CLAUDE.md auto-loads without user action

D) Skills are written in YAML; CLAUDE.md is written in Markdown

---

**Q17. What is the PRIMARY distinction between skills and MCP servers as described in Chapter 5?**

A) Skills are faster because they eliminate network calls; MCP servers require external API connections

B) Skills encode domain expertise and reasoning patterns; MCP servers provide standardized external system access

C) Skills are platform-specific to Claude Code; MCP servers work across multiple AI platforms

D) Skills require YAML frontmatter; MCP servers use JSON configuration

---

**Q18. How BEST differentiates subagents from skills in terms of their primary function?**

A) Subagents provide external system access; skills provide domain expertise

B) Subagents handle complex multi-step tasks with isolated context; skills encode reasoning patterns for automatic activation

C) Subagents require explicit invocation; skills auto-activate based on triggers

D) Subagents use Python scripts; skills use Bash commands

---

**Q19. Which statement BEST captures the distinction between Agent Skills (as taught in Lesson 8) and regular skills?**

A) Agent Skills are only for Claude Code; regular skills work on other platforms

B) Agent Skills are created specifically for agent use; regular skills are manual procedures encoded

C) Agent Skills include YAML frontmatter and explicit reasoning patterns; regular skills are simple command aliases

D) Agent Skills are faster than regular skills

---

**Q20. What PRIMARILY distinguishes the "expertise gap" from the "capability gap" in Claude Code, as explained in Lesson 7?**

A) Expertise gap = missing features; capability gap = missing performance

B) Capability gap = what Claude Code can do; expertise gap = domain knowledge Claude lacks without context

C) Expertise gap = technical skills needed; capability gap = execution tools available

D) Expertise gap = training data; capability gap = model parameters

---

**Q21. According to Chapter 5, why is CLAUDE.md fundamentally different from a single skill?**

A) CLAUDE.md stores credentials; skills store procedures

B) CLAUDE.md provides persistent project-wide context; skills encode reusable expertise for specific repeated patterns

C) CLAUDE.md is required; skills are optional

D) CLAUDE.md uses JSON; skills use YAML

---

**Q22. How BEST differentiates the "three-level loading architecture" (Lesson 7) from simple prompt engineering?**

A) Three-level loading is faster because it caches metadata

B) Three-level loading (metadata → instructions → supporting files) provides efficient, structured expertise encoding; simple prompting is ad-hoc and requires re-explanation

C) Three-level loading is proprietary to Claude; simple prompting works everywhere

D) Three-level loading requires Python; simple prompting uses natural language only

---

**Q23. Which BEST distinguishes when you should use a skill versus when you should use CLAUDE.md?**

A) Skills for beginners; CLAUDE.md for experts

B) CLAUDE.md for one-time project context; skills for reusable patterns you repeat across multiple projects

C) Skills for security; CLAUDE.md for performance

D) Skills for Bash commands; CLAUDE.md for Python scripts

---

**Q24. According to Lesson 9, what is the core distinction between MCP servers and skills in terms of solving the "external access" problem?**

A) MCP servers provide external access; skills cannot access external systems

B) MCP servers are direct external connectors; skills wrap MCP functionality in encoded expertise patterns

C) MCP servers are slower; skills are faster

D) MCP servers require authentication; skills don't

---

**Q25. What PRIMARILY distinguishes subagent delegation (automatic vs explicit) according to Lesson 11?**

A) Automatic delegation is faster; explicit delegation gives more control

B) Automatic delegation (Plan subagent) triggers on complex tasks; explicit delegation is when you manually invoke a specific subagent for a specialized task

C) Automatic delegation requires a trigger; explicit delegation doesn't

D) Automatic delegation uses skills; explicit delegation uses MCP

---

**Q26. How BEST differentiates "compiling MCP to skills" (Lesson 10) from using MCP directly?**

A) Compiling MCP uses cached results; direct MCP doesn't

B) Compiling MCP to skills extracts high-value operations into lean code, reducing token overhead by 98.7%; direct MCP loads all tool definitions eagerly, consuming significantly more tokens

C) Compiling MCP is for security; direct MCP is for performance

D) Compiling MCP requires authorization; direct MCP doesn't

---

**Q27. According to Chapter 5, which statement BEST distinguishes expertise (skills) from execution capability (code)?**

A) Expertise makes execution faster; execution makes expertise work

B) Execution capability lets Claude Code do things; expertise lets it do things WELL for your specific domain

C) Expertise is theory; execution is practice

D) Expertise requires training; execution requires tools

---

**Q28. What PRIMARILY differentiates the "personal assistant" analogy (Lesson 6) from a generic AI assistant in the context of skills?**

A) Personal assistants are faster

B) Personal assistants are expensive; generic assistants are free

C) A personal assistant who knows your style (encoded in skills) delivers consistent, personalized results; a generic assistant repeats the same explanations across tasks

D) Personal assistants require human intervention; generic assistants don't

---

**Q29. How BEST differentiates when a pattern becomes "worthy of a skill" versus remaining a one-time task?**

A) Skills are for complex tasks; one-time tasks are simple

B) Skills are for tasks you repeat 2+ times with consistent explanations; one-time tasks are executed once or with different approaches each time

C) Skills require more time to set up; one-time tasks are faster

D) Skills are for team use; one-time tasks are personal only

---

**Q30. According to Lesson 8, what PRIMARILY distinguishes the skill-creator meta-skill from manually writing SKILL.md files?**

A) Skill-creator is faster because it's automated

B) Skill-creator guides co-learning refinement with Claude; manual writing requires domain expertise upfront without iteration

C) Skill-creator generates better code

D) Skill-creator is more secure

---

**Q31. Which statement BEST differentiates the role of agents versus skills in AI-native development?**

A) Agents are newer than skills

B) Agents provide intelligence and execution capability; skills package domain expertise so agents execute it correctly for YOUR specific context

C) Agents are smarter than skills

D) Agents use code; skills use natural language

---

**Q32. According to Chapter 5, what PRIMARILY distinguishes a "procedure worth encoding" from random workflow steps?**

A) Procedures are longer

B) Procedures are repeated patterns with consistent explanation needs that consume mental energy each time; random steps are one-off decisions made differently each context

C) Procedures are for beginners

D) Procedures require documentation

---

**Q33. How BEST differentiates MCP's security model (Lesson 9) from directly giving Claude Code file system access?**

A) MCP is more restrictive; direct access is more permissive by design

B) MCP provides standardized, opt-in external system access through explicit configuration; direct file access is unlimited

C) MCP is faster than direct access

D) MCP is only for cloud services

---

**Q34. What PRIMARILY distinguishes subagents with "isolated context" (Lesson 11) from a single agent handling all tasks?**

A) Subagents are slower

B) Subagents focus on specialized tasks with clean context, avoiding distraction and confusion that accumulates in a single agent's context window

C) Subagents are only for complex projects

D) Subagents require manual context switching

---

**Q35. According to Chapter 5, which BEST differentiates why "simplicity enables adoption" in the skills architecture versus more complex alternatives?**

A) Simplicity is faster to execute

B) Simplicity (YAML + instructions + files) is accessible to non-technical users and reduces barrier to creating reusable expertise; complexity requires deep technical expertise and limits who can contribute

C) Simplicity is more powerful

D) Simplicity doesn't require tools

---

## Question Reasoning & Validation

Q16: Bloom=Understand | DIF=0.62 | DIS=0.38 | DF=all >5%
  Source: Lesson 5 (CLAUDE.md) and Lesson 7 (Skills Concept) | Reasoning: Distinguishes scope and reusability—CLAUDE.md is project-wide persistent context, while skills encode patterns that travel across projects. Distractors confuse implementation details (YAML/Markdown) or confuse auto-loading behavior.

Q17: Bloom=Understand | DIF=0.58 | DIS=0.42 | DF=all >5%
  Source: Lesson 7 (Skills Concept) and Lesson 9 (MCP Integration) | Reasoning: Core distinction between expertise encoding (skills) vs external system access (MCP). Distractors target performance misconceptions and platform confusion.

Q18: Bloom=Analyze | DIF=0.60 | DIS=0.40 | DF=all >5%
  Source: Lesson 8 (Agent Skills) and Lesson 11 (Subagents) | Reasoning: Subagents manage task complexity and context isolation; skills encode expertise patterns. Distractors confuse tool usage patterns with functional distinctions.

Q19: Bloom=Understand | DIF=0.64 | DIS=0.36 | DF=all >5%
  Source: Lesson 8 (Building Your Own Skills) | Reasoning: Agent Skills are intentional expertise design for AI agents; they're not different technology, but intentional application. Distractors conflate platform specificity with purpose distinction.

Q20: Bloom=Analyze | DIF=0.55 | DIS=0.45 | DF=all >5%
  Source: Lesson 7 (Concept Behind Skills) | Reasoning: Lesson 7 explicitly states "intelligence + execution ≠ expertise." Capability is what Claude can do; expertise is domain knowledge. Distractors target feature confusion or training misconceptions.

Q21: Bloom=Understand | DIF=0.61 | DIS=0.39 | DF=all >5%
  Source: Lesson 5 (CLAUDE.md) and Lesson 7 (Skills Concept) | Reasoning: CLAUDE.md provides one-time project context; skills are reusable expertise patterns. Distractors confuse storage mechanisms (JSON/YAML) with functional purpose.

Q22: Bloom=Analyze | DIF=0.59 | DIS=0.41 | DF=all >5%
  Source: Lesson 7 (The Concept Behind Skills) | Reasoning: Three-level architecture (metadata→instructions→files) is systematic expertise encoding versus ad-hoc prompting. Distractors target performance and platform misconceptions.

Q23: Bloom=Apply | DIF=0.63 | DIS=0.37 | DF=all >5%
  Source: Lessons 5-8 (multiple contexts) | Reasoning: Practical decision: CLAUDE.md for project scope, skills for reusable patterns. Distractors use false dichotomies (beginner vs expert, language choice).

Q24: Bloom=Understand | DIF=0.56 | DIS=0.44 | DF=all >5%
  Source: Lesson 9 (MCP Integration) and Lesson 10 (Compiling MCP to Skills) | Reasoning: Lesson 10 explicitly explains how skills wrap MCP functionality. MCP = raw external access; skills = expertise-driven external access wrapper. Distractors confuse capability with performance.

Q25: Bloom=Analyze | DIF=0.58 | DIS=0.42 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) | Reasoning: Automatic delegation (Plan subagent triggered by complexity); explicit delegation (manual subagent invocation). Distractors confuse speed with control or technology choices.

Q26: Bloom=Apply | DIF=0.61 | DIS=0.39 | DF=all >5%
  Source: Lesson 10 (Compiling MCP to Skills) | Reasoning: Lesson 10 provides concrete numbers (98.7% token reduction). Compiling extracts operations; direct MCP loads everything eagerly. Distractors target security or authorization misconceptions.

Q27: Bloom=Understand | DIF=0.60 | DIS=0.40 | DF=all >5%
  Source: Lesson 7 (Concept Behind Skills) | Reasoning: Lesson 7 explicitly states "Intelligence + Code = Execution" but "Not Expertise." Expertise is domain knowledge (skills); execution is capability (code/tools). Distractors confuse layers.

Q28: Bloom=Understand | DIF=0.65 | DIS=0.35 | DF=all >5%
  Source: Lesson 6 (Teach Claude Your Way) and Lesson 7 (Skills Concept) | Reasoning: Personal assistant analogy = consistent style preservation; generic assistant = repeated explanations. Distractors target cost or speed misconceptions.

Q29: Bloom=Apply | DIF=0.62 | DIS=0.38 | DF=all >5%
  Source: Lesson 6 (Teach Claude Your Way) and Lesson 8 (Building Your Own Skills) | Reasoning: Pattern recurrence (2+) with consistent explanations signals skill-worthy; one-time or varied tasks don't justify skill encoding. Distractors use false complexity signals.

Q30: Bloom=Apply | DIF=0.59 | DIS=0.41 | DF=all >5%
  Source: Lesson 8 (Building Your Own Skills) | Reasoning: Skill-creator enables co-learning iteration; manual writing requires upfront mastery. Distractors target speed vs quality misconceptions.

Q31: Bloom=Understand | DIF=0.57 | DIS=0.43 | DF=all >5%
  Source: Lesson 7 (The Concept Behind Skills) and Chapter 5 overview | Reasoning: Agents (intelligence + execution) + skills (expertise) = effective AI-native work. Distractors confuse age, capability, or implementation language.

Q32: Bloom=Analyze | DIF=0.61 | DIS=0.39 | DF=all >5%
  Source: Lesson 6 (Teach Claude Your Way) | Reasoning: Procedures are repeated with consistent explanation patterns; random steps are contextual decisions. Distractors target length/documentation signals.

Q33: Bloom=Understand | DIF=0.60 | DIS=0.40 | DF=all >5%
  Source: Lesson 9 (MCP Integration) | Reasoning: MCP is opt-in standardized access; direct file access is unrestricted by design. Lesson 9 addresses security principles. Distractors confuse speed with security model.

Q34: Bloom=Analyze | DIF=0.63 | DIS=0.37 | DF=all >5%
  Source: Lesson 11 (Subagents and Orchestration) | Reasoning: Subagent isolation prevents context clutter; single agent accumulates confusion. Lesson 11 explains the "Context Clutter Problem." Distractors target speed or complexity signals.

Q35: Bloom=Apply | DIF=0.64 | DIS=0.36 | DF=all >5%
  Source: Lesson 7 (The Concept Behind Skills) and Chapter 5 overall philosophy | Reasoning: Simplicity (YAML + instructions) enables non-technical adoption; complexity limits contributor base. Distractors misframe simplicity as speed or power.

