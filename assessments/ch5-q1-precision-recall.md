# Questions 1-15: Precision_Recall

**Q1. In the origin story of Claude Code, what key discovery did engineer Boris Cherny make after giving Claude direct access to the filesystem?**

A) Claude became smarter at generating code without AI seeing the actual project files

B) Claude naturally started exploring and understanding the codebase without explicit instruction

C) Claude required additional training to understand project structure

D) Claude could only improve performance with manual code annotations

---

**Q2. According to Lesson 1 (Origin Story), what is the primary difference between passive AI assistance and agentic AI like Claude Code?**

A) Passive AI is faster; agentic AI is more thorough

B) Passive AI describes problems and AI suggests generically; agentic AI reads actual code and proposes specific changes with testing

C) Passive AI uses terminal integration; agentic AI relies on chat interfaces

D) Passive AI is proprietary; agentic AI is open-source

---

**Q3. What adoption metric did Claude Code achieve internally at Anthropic by May 2025, according to Lesson 1?**

A) 50% of engineers using it daily

B) 80%+ of engineers using it daily

C) 30% adoption rate

D) 100% immediate adoption on day one

---

**Q4. In Lesson 1, what is the OODA Loop that Claude Code uses when debugging problems?**

A) Observe, Orient, Decide, Accelerate

B) Observe, Optimize, Deploy, Analyze

C) Observe, Orient, Decide, Act (repeating until resolved)

D) Open, Organize, Debug, Automate

---

**Q5. According to Lesson 2 (Installation), which authentication method is recommended for Claude Pro ($20/month) and Max ($200/month) subscribers?**

A) Console API authentication using API keys

B) Enterprise authentication through Amazon Bedrock

C) Claude App Authentication through Claude.ai login

D) OAuth 2.0 with third-party services

---

**Q6. In Lesson 2, what is the command to verify Claude Code installation and check the version?**

A) `claude status`

B) `claude --version`

C) `claude doctor`

D) `claude check-install`

---

**Q7. What does CLAUDE.md provide according to Lesson 5 (Context Files)?**

A) A way to install Claude Code on different operating systems

B) Persistent project context that auto-loads at the start of every session

C) Authentication credentials for the Anthropic API

D) A list of available skills on the system

---

**Q8. According to Lesson 5, which of the following should be included in the CLAUDE.md file?**

A) Your personal passwords and authentication tokens

B) Project overview, technology stack, directory structure, coding conventions, key commands, and important notes

C) Random reminders and personal notes unrelated to the project

D) All source code of your application

---

**Q9. What is AGENTS.md, as introduced in Lesson 5?**

A) A Claude Code-specific configuration file for managing agent permissions

B) A universal standard for project instructions that works across ALL AI coding agents

C) A file that lists all available Claude Code agents

D) An Anthropic-proprietary format that only works with Claude Code

---

**Q10. According to Lesson 7 (Concept Behind Skills), what is the primary bottleneck Claude Code addresses—intelligence, execution capability, or expertise?**

A) Intelligence (making the model smarter)

B) Execution capability (giving AI the ability to run commands)

C) Expertise (providing domain-specific knowledge the model lacks)

D) Terminal integration (providing command-line access)

---

**Q11. In Lesson 7, how does Anthropic frame the relationship between models, agent runtimes, and skills in computing terms?**

A) Models are apps, runtimes are operating systems, skills are processors

B) Models are processors, runtimes are operating systems, skills are applications

C) Models are operating systems, runtimes are applications, skills are processors

D) Models are middleware, runtimes are services, skills are data stores

---

**Q12. According to Lesson 7, what are the three main sources of skills in the ecosystem?**

A) Foundational, Community, and Personal

B) Foundational, Partner, and Enterprise/Custom

C) Built-in, Downloaded, and User-Created

D) Free, Premium, and Enterprise

---

**Q13. What is the three-level architecture for loading skills, as described in Lesson 7?**

A) SKILL.md, supporting files, and configuration files

B) Metadata (always loaded), Full instructions (on-demand), Supporting files (if needed)

C) API endpoints, webhooks, and database connections

D) Frontend, backend, and database

---

**Q14. According to Lesson 8 (Building Skills), what is the most important line in a skill's YAML frontmatter for determining when Claude activates the skill?**

A) The `name` field

B) The `version` field

C) The `description` field

D) The `category` field

---

**Q15. In Lesson 8, what is the structure of an effective skill description formula?**

A) Just list what the skill does without specifying triggers

B) [Action verb] + [input type] + [output type] + [key features] + [trigger conditions]

C) Describe the file path and configuration requirements

D) Provide code examples without explaining functionality

---

## Question Reasoning & Validation

Q1: Bloom=Remember | DIF=0.68 | DIS=0.35 | DF=all >5%
  Source: Lesson 1 (Origin Story) | Reasoning: Directly stated—Boris Cherny discovered Claude naturally explored codebases when given filesystem access. Tests foundational knowledge of the paradigm shift.

Q2: Bloom=Understand | DIF=0.65 | DIS=0.38 | DF=all >5%
  Source: Lesson 1 (Paradigm Shift section) | Reasoning: Core distinction between passive vs agentic AI models explained in detail. Tests comprehension of the fundamental difference Claude Code introduces.

Q3: Bloom=Remember | DIF=0.72 | DIS=0.32 | DF=all >5%
  Source: Lesson 1 (Dogfooding Results section) | Reasoning: Specific adoption metric (80%+) from internal Anthropic usage. Tests recall of key evidence supporting Claude Code's value.

Q4: Bloom=Remember | DIF=0.61 | DIS=0.40 | DF=all >5%
  Source: Lesson 1 (OODA Loop section) | Reasoning: Explicitly defines OODA Loop acronym and sequence. Tests foundational knowledge of agentic reasoning process.

Q5: Bloom=Understand | DIF=0.66 | DIS=0.36 | DF=all >5%
  Source: Lesson 2 (Authentication Methods section) | Reasoning: Clear guidance on which method applies to specific account types. Tests ability to match authentication to subscription level.

Q6: Bloom=Remember | DIF=0.74 | DIS=0.30 | DF=all >5%
  Source: Lesson 2 (Verification sections across all platforms) | Reasoning: Specific command explicitly shown in every platform's verification step. Tests recall of practical setup knowledge.

Q7: Bloom=Understand | DIF=0.62 | DIS=0.38 | DF=all >5%
  Source: Lesson 5 (What Is CLAUDE.md? section) | Reasoning: Defines CLAUDE.md as persistent project context auto-loading. Tests comprehension of core value proposition.

Q8: Bloom=Understand | DIF=0.58 | DIS=0.42 | DF=all >5%
  Source: Lesson 5 (What Goes Into CLAUDE.md section) | Reasoning: Lists 6 standard sections explicitly in source material. Tests ability to identify appropriate CLAUDE.md content.

Q9: Bloom=Remember | DIF=0.65 | DIS=0.37 | DF=all >5%
  Source: Lesson 5 (The Universal Standard: AGENTS.md section) | Reasoning: Defines AGENTS.md as universal standard adopted by 60,000+ projects. Tests recall of industry-standard context format.

Q10: Bloom=Understand | DIF=0.60 | DIS=0.39 | DF=all >5%
  Source: Lesson 7 (Intelligence + Code = Execution section) | Reasoning: Explicitly states expertise is the missing piece, not intelligence or execution. Tests comprehension of skills' purpose.

Q11: Bloom=Understand | DIF=0.64 | DIS=0.36 | DF=all >5%
  Source: Lesson 7 (The Stack Analogy section) | Reasoning: Directly maps models→processors, runtimes→OS, skills→applications. Tests understanding of conceptual framework.

Q12: Bloom=Remember | DIF=0.67 | DIS=0.34 | DF=all >5%
  Source: Lesson 7 (Three Sources of Encoded Expertise section) | Reasoning: Explicitly lists three sources: Foundational, Partner, Enterprise. Tests recall of skill ecosystem structure.

Q13: Bloom=Understand | DIF=0.59 | DIS=0.41 | DF=all >5%
  Source: Lesson 7 (Won't Many Skills Overload Context? section) | Reasoning: Defines three-level architecture: brief metadata, full instructions on-demand, supporting files if needed. Tests comprehension of progressive disclosure.

Q14: Bloom=Remember | DIF=0.70 | DIS=0.33 | DF=all >5%
  Source: Lesson 8 (The Description Field section) | Reasoning: Explicitly states description determines skill activation. Tests recall of YAML field importance.

Q15: Bloom=Understand | DIF=0.63 | DIS=0.37 | DF=all >5%
  Source: Lesson 8 (The Description Formula section) | Reasoning: Provides exact formula template: [Action verb] + [input type] + [into/for] + [output type] + [key features] + [When to use]. Tests comprehension of effective description writing.
