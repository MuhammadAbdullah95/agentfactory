# Vertical Intelligence: Runtime Architecture Deep Dive

**Date**: 2025-01-13
**Type**: Meta-Architecture Documentation
**Audience**: Architects using AIDD (AI-Driven Development)

---

## 🎯 The Core Question

> "What is prerequisite knowledge vs what happens at runtime vs what actually makes a skill?"

This is the **meta-architecture** of Vertical Intelligence—understanding the difference between:
1. **Design-Time Knowledge** (what developer/architect must know)
2. **Runtime Discovery** (what AI discovers automatically during execution)
3. **Skill Manifestation** (what transforms knowledge into reusable capability)

---

## 📚 Layer 2: Domain Knowledge - The Developer's Responsibility

### What the Architect/Developer Must Know (Prerequisites)

#### 1. Constitutional Principles (Design-Time Knowledge)
**The architect must understand**:
- Project vision: "Specs Are the New Syntax"
- Core principles (especially Principle 13: Graduated Teaching, Principle 18: Three Roles)
- Target audience tiers (A1-C2 complexity mapping)
- AI Development Spectrum (Assisted 2-3x → Driven 5-10x → Native 50-99x)

**Why prerequisite**: These are **strategic decisions** that cannot be automated:
```markdown
Example Decision: "Should this chapter teach direct commands or AI workflows?"
- Requires: Understanding of Graduated Teaching (Principle 13)
- Requires: Judgment about audience tier (A2 = max 7 concepts)
- Requires: Strategic thinking about when AI adds value vs over-engineering

AI CANNOT make this decision autonomously (yet).
Human architect encodes decision → AI applies consistently.
```

**Location**: `.specify/memory/constitution.md`
**Created**: Design-time by architect
**Updated**: Rarely (only when project vision changes)

#### 2. Domain Patterns (Design-Time Knowledge)
**The architect must establish**:
- Chapter structure (9 lessons per chapter? 3-4 "Try With AI" prompts per lesson?)
- Prerequisites (Chapter 5 requires Chapters 1-4?)
- Complexity mapping (Part 2 = A2 tier, max 7 concepts per section?)
- Pedagogical patterns (clean prompt format: `### Prompt N: Title` → code block → `**Expected outcome:**`)

**Why prerequisite**: These are **structural decisions** that define the project:
```markdown
Example Decision: "How many lessons should a chapter have?"
- Requires: Understanding of cognitive load management
- Requires: Judgment about student attention span
- Requires: Business consideration (book length, pricing)

AI CANNOT decide project structure autonomously.
Human architect defines structure → AI fills in content.
```

**Location**:
- `specs/book/chapter-index.md` (structure, prerequisites, tiers)
- `.claude/skills/` (reusable pedagogical capabilities)
- Spec templates (functional requirements structure)

**Created**: Design-time by architect
**Updated**: Occasionally (when project structure evolves)

#### 3. Quality Standards (Design-Time Knowledge)
**The architect must define**:
- What makes content "good"? (technical accuracy, pedagogical effectiveness, constitutional alignment)
- What are anti-patterns? ("Don't use AI for `uv init`", "Don't inflate durations")
- What are validation criteria? (duration realistic? AI usage strategic? cognitive load within limit?)

**Why prerequisite**: These are **quality judgments** that require domain expertise:
```markdown
Example Decision: "Is 45 minutes for a 1-minute installation too long?"
- Requires: Experience with teaching (what's realistic?)
- Requires: Understanding of student workflow (how long does installation actually take?)
- Requires: Business judgment (is verbosity adding value or just padding?)

AI CANNOT evaluate quality without human-defined standards.
Human architect sets bar → AI validates against it.
```

**Location**:
- Constitution (anti-patterns section)
- Validation criteria (in intelligence object schema)
- Quality gates (in `/sp.loopflow` workflow)

**Created**: Design-time by architect
**Updated**: Continuously (as lessons learned from each chapter)

---

## ⚡ What Happens at Runtime (Automatic Discovery)

### What the AI Discovers Automatically (No Human Input)

#### 1. Task-Specific Context (Runtime Discovery)
**The AI discovers**:
- Library documentation (Context7: `/anthropics/claude-code` → 8000 tokens)
- Official sources (WebFetch: engineering blogs, docs, announcements)
- Existing specs (similar chapters for pattern reference)
- Available domain skills (which skills in `.claude/skills/` apply to this task?)

**Why runtime**: This is **information retrieval** that changes per task:
```markdown
Example: Chapter 5 needs Claude Code docs
- AI executes: Context7 resolve → `/anthropics/claude-code`
- AI executes: Context7 get-docs → 8000 tokens (Skills, Plugins, MCP)
- AI executes: WebFetch → 3 official URLs
- Result: Comprehensive intelligence gathered in 15 minutes (would take human 2-3 hours)

Human DOES NOT need to manually research every library.
Human architect defines WHICH sources to trust (Context7, official docs).
AI retrieves content automatically at runtime.
```

**Tools Used**:
- `mcp__context7__resolve-library-id`
- `mcp__context7__get-library-docs`
- `WebFetch` (built-in)
- `Read`, `Grep`, `Glob` (for existing specs)

**Triggered**: Every time agent invoked (Phase 0: Context Discovery)

#### 2. Derivations from Constitution + Domain Knowledge (Runtime Synthesis)
**The AI derives**:
- Audience tier (from chapter number in chapter-index: Chapter 5 → Part 2 → A2 tier)
- Complexity level (A2 → max 7 concepts per section)
- Prerequisites (Chapter 5 → requires Chapters 1-4 from dependency graph)
- Teaching pattern (A2 tier → Graduated Teaching Tier 1-2, defer Tier 3)
- AI usage strategy (simple commands direct, complex troubleshooting via AI)

**Why runtime**: This is **logical inference** from established patterns:
```markdown
Example: Deriving audience tier
1. User requests: "Rework Chapter 5"
2. AI reads: `specs/book/chapter-index.md`
3. AI finds: Chapter 5 = Part 2
4. AI reads: Constitution → Part 2 = A2 tier (Aspiring Builders)
5. AI derives: Max 7 concepts, 2 options max, cognitive load managed
6. Result: Audience tier derived WITHOUT asking user

Human DOES NOT need to specify tier every time.
Human architect defined mapping ONCE in chapter-index.
AI applies mapping automatically at runtime.
```

**Logic**:
```python
# Pseudocode: Runtime derivation
def derive_intelligence_object(user_goal: str):
    chapter_num = extract_chapter_number(user_goal)  # "Chapter 5" → 5

    chapter_index = read_file("specs/book/chapter-index.md")
    part_num = chapter_index.get_part_for_chapter(chapter_num)  # 5 → Part 2

    constitution = read_file(".specify/memory/constitution.md")
    audience_tier = constitution.get_tier_for_part(part_num)  # Part 2 → A2

    complexity_level = "A2"  # From tier mapping
    cognitive_load_limit = 7  # From A2 tier rules
    prerequisites = chapter_index.get_prerequisites(chapter_num)  # [1, 2, 3, 4]

    teaching_pattern = apply_graduated_teaching(audience_tier)
    # A2 → "Tier 1: Book teaches, Tier 2: AI companion, Tier 3: Defer"

    ai_usage_strategy = apply_ai_spectrum(audience_tier)
    # A2 → "Direct commands for simple, AI for complex, orchestration intro only"

    return IntelligenceObject(
        task_type="book_chapter",
        audience_tier=audience_tier,
        complexity_level=complexity_level,
        prerequisites=prerequisites,
        cognitive_load_limit=cognitive_load_limit,
        teaching_pattern=teaching_pattern,
        ai_usage_strategy=ai_usage_strategy
    )
```

**Result**: Intelligence object generated with 0-5 clarifying questions (only genuine ambiguities).

#### 3. Pattern Recognition (Runtime Analysis)
**The AI recognizes**:
- Similar chapters (Chapter 5 similar to Chapter 1 in format)
- Naming conventions (lessons named `01-origin-story.md`, `02-installation.md`)
- Structure patterns (all chapters have README.md, 9 lessons, "Try With AI" sections)
- Anti-pattern violations (detecting over-engineering: "8 verbose prompts" vs expected "3-4 focused")

**Why runtime**: This is **intelligent matching** against established patterns:
```markdown
Example: Detecting anti-patterns
1. AI reads: Chapter 12 original lesson (667 lines, 8 "Try With AI" prompts, 45-minute duration)
2. AI reads: Constitution anti-patterns ("Don't inflate durations", "Use 3-4 focused prompts")
3. AI reads: Chapter 1 format (clean prompt format, realistic durations)
4. AI detects: Mismatch (667 lines >> 200-300 expected, 8 prompts >> 3-4 expected)
5. AI flags: "This appears over-engineered. Chapter 1 format would be 200-300 lines with 3-4 prompts."
6. Result: Anti-pattern detected WITHOUT human having to manually compare

Human DOES NOT need to manually audit every lesson.
Human architect defined anti-patterns ONCE in constitution.
AI applies pattern matching automatically at runtime.
```

**Tools Used**:
- Pattern matching algorithms (compare structures)
- Statistical analysis (line count, prompt count, duration estimates)
- Constitutional validation (check against anti-patterns)

---

## 🧩 What Actually Makes a Skill (Capability Manifestation)

### The Three Levels of Skill

#### Level 1: Knowledge (Design-Time)
**What it is**: Information encoded in files
**Examples**:
- Constitution principles (Graduated Teaching, Three Roles)
- Domain patterns (chapter structure, pedagogical formats)
- Anti-patterns ("Don't use AI for simple commands")

**Storage**:
- `.specify/memory/constitution.md`
- `specs/book/chapter-index.md`
- `.claude/skills/[skill-name].md` (SKILL.md files with YAML frontmatter)

**Limitation**: Knowledge alone is NOT a skill. It's data waiting to be applied.

#### Level 2: Capability (Runtime Discovery + Application)
**What it is**: AI's ability to RETRIEVE and APPLY knowledge to specific tasks
**Examples**:
- Reading constitution → deriving audience tier → applying cognitive load limit to lesson
- Reading chapter-index → identifying prerequisites → validating dependency order
- Reading Context7 docs → synthesizing Skills+Plugins+MCP → integrating into chapter

**Process**:
```markdown
Knowledge (design-time) + Context Discovery (runtime) + Intelligence Synthesis (runtime)
= Capability to execute task with full VI stack

Example: "Chapter Planning" capability
1. Knowledge: Constitution (Graduated Teaching), Chapter-index (structure)
2. Context: Chapter 5 is Part 2, A2 tier
3. Synthesis: "Lesson 4 should be 10-12 min, max 7 concepts, Tier 1-2 teaching"
4. Application: Generate plan.md with correct structure
→ This IS the skill manifesting
```

**Storage**: Agents (`.claude/agents/[agent-name].md`) that orchestrate VI stack application

**Key Insight**: Capability = Knowledge × Context × Application Logic

#### Level 3: Reusable Skill (Encoded Workflow)
**What it is**: A **packaged capability** that can be invoked with minimal input
**Examples**:
- `super-orchestra` agent (deep research + market positioning)
- `chapter-planner` agent (spec → lesson plan with proficiency levels)
- `lesson-writer` agent (plan → markdown content with full intelligence)

**Structure**:
```markdown
# Agent Definition (.claude/agents/super-orchestra.md)

## Phase 0: Intelligence Stack Application
Read: Constitution, Domain Knowledge, Context Sources
Derive: Intelligence Object

## Phase 1-N: Workflow Execution
Apply: Full VI stack to each phase
Validate: Against quality gates

## Output
Artifacts + Documentation + System Evolution
```

**Invocation**:
```bash
# Minimal user input
/invoke super-orchestra "Research Skills/Plugins/MCP for Chapter 5"

# Agent automatically:
1. Reads constitution (Layer 1)
2. Reads chapter-index (Layer 2)
3. Discovers context via Context7 + WebFetch (Layer 3)
4. Generates intelligence object (Layer 4)
5. Executes workflow with full VI stack (Layer 5)
6. Documents intelligence journey
```

**Key Insight**: Reusable skill = Capability + Workflow orchestration + Documentation pattern

---

## 🔄 The Complete Flow: Design-Time → Runtime → Skill

### Example: Chapter 5 Skills/Plugins/MCP

#### Design-Time (Architect's Work)
**Human creates** (one-time):
1. **Constitution** (`.specify/memory/constitution.md`):
   - Principle 13: Graduated Teaching (Tier 1 Book → Tier 2 AI Companion → Tier 3 Orchestration)
   - Principle 18: Three Roles (AI as Teacher/Student/Co-Worker)
   - Cognitive Load: A2 tier = max 7 concepts per section
   - Anti-patterns: "Don't use AI for simple commands", "Don't inflate durations"

2. **Chapter Index** (`specs/book/chapter-index.md`):
   - Chapter 5 = Part 2
   - Part 2 = A2 tier (Aspiring Builders)
   - Prerequisites: Chapters 1-4
   - Structure: 9 lessons, 60-80 minutes total

3. **Domain Skills** (`.claude/skills/`):
   - `learning-objectives.md` (how to write measurable objectives)
   - `concept-scaffolding.md` (how to break concepts into learnable steps)
   - `book-scaffolding.md` (how to structure content across chapters)

**Time Investment**: 2-3 days initially, then minimal updates

#### Runtime (AI's Work)
**User invokes** (3-4 hours):
```bash
User: "Rework Chapter 5 - missing Skills/Plugins/MCP. Use Context7 to research comprehensively."
```

**AI executes automatically**:

**Phase 0: Intelligence Stack Discovery**
1. **Read Constitution** (Layer 1):
   ```
   Read: .specify/memory/constitution.md
   Extract: Principle 13, Principle 18, Cognitive Load A2, Anti-patterns
   ```

2. **Read Domain Knowledge** (Layer 2):
   ```
   Read: specs/book/chapter-index.md
   Derive: Chapter 5 → Part 2 → A2 tier → Prerequisites [1,2,3,4]

   Read: .claude/skills/
   Identify: learning-objectives, concept-scaffolding, book-scaffolding applicable
   ```

3. **Discover Context** (Layer 3):
   ```
   Execute: mcp__context7__resolve-library-id "claude-code"
   Execute: mcp__context7__get-library-docs "/anthropics/claude-code" tokens=8000
   Result: Skills (progressive disclosure), Plugins (architecture), MCP (config)

   Execute: WebFetch "https://www.anthropic.com/engineering/equipping-agents..."
   Execute: WebFetch "https://code.claude.com/docs/en/plugins"
   Execute: WebFetch "https://www.claude.com/blog/claude-code-plugins"
   Result: 3 official sources retrieved

   Read: specs/012-chapter-12-uv/spec.md (similar chapter for pattern reference)
   ```

4. **Generate Intelligence Object** (Layer 4):
   ```json
   {
     "task_type": "book_chapter",
     "audience_tier": "aspiring",
     "complexity_level": "A2",
     "prerequisites": ["chapter-1", "chapter-2", "chapter-3", "chapter-4"],
     "domain_skills": ["learning-objectives", "concept-scaffolding", "book-scaffolding"],
     "teaching_pattern": "Tier 1: Book teaches Skills/Plugins/MCP architecture | Tier 2: AI helps install plugin | Tier 3: Custom development deferred to Part 5/6",
     "ai_usage_strategy": "Direct commands for installation (`/plugin install`), AI for troubleshooting and understanding concepts",
     "cognitive_load_limit": 7,
     "anti_patterns": [
       "Don't use AI for simple `/plugin` command",
       "Don't inflate lesson duration (installation is 2-3 min, not 45 min)",
       "Don't create 8+ verbose prompts (use 3-4 focused from Chapter 1 format)"
     ],
     "content_gap": "Missing unified Skills+Plugins+MCP architecture. Official docs are scattered (agent skills blog, plugins page, MCP protocol). Need ONE cohesive lesson with hands-on plugin installation.",
     "market_positioning": "Must surpass official Anthropic documentation by integrating scattered sources + adding hands-on practice"
   }
   ```

5. **Execute with Full VI Stack** (Layer 5):
   ```markdown
   Invoke: super-orchestra agent

   Phase 1: Spec expansion
   - Expand User Story 4: 3 → 10 acceptance scenarios
   - Add FR-020 to FR-029 (Skills/Plugins/MCP requirements)
   - Add SC-005 to SC-008 (success criteria)
   - Add Eval 8 (Skills and Plugins Personalization)

   Phase 2: Plan expansion
   - Expand Lesson 4: 6-8 min → 10-12 min
   - Add 4 sections: Agent Skills, Plugins, MCP, Hierarchy
   - Add hands-on plugin installation (Prompt 3)

   Phase 3: Tasks expansion
   - Expand Phase 6: 4 → 9 tasks (T019-T027)
   - Add Phase 13: T068A (plugin installation sandbox testing)

   Phase 4: Validation
   - Compare to official docs: 10 differentiators identified
   - Create positioning statement: "More comprehensive than all official resources"
   - Document intelligence journey: 7 artifacts created
   ```

**Time**: 3-4 hours with comprehensive intelligence, market-defining quality

#### Skill Manifestation (System Evolution)
**AI encodes learnings**:
1. **Agent Created** (`.claude/agents/super-orchestra.md`):
   - Captures complete workflow from this session
   - Documents when to use (deep research + market positioning)
   - Defines how to apply VI stack automatically
   - **Result**: Future chapters can invoke with `/invoke super-orchestra [goal]`

2. **Output Style Created** (`.claude/output-styles/super-orchestra-session.md`):
   - Defines communication patterns for deep research tasks
   - Documents iteration logging, evidence tables, positioning validation
   - **Result**: Consistent documentation across Super Orchestra sessions

3. **Pattern Documented** (`.claude/patterns/VERTICAL-INTELLIGENCE-PATTERN.md`):
   - Formalizes 5-layer VI stack
   - Explains design-time vs runtime responsibilities
   - Provides templates for new projects
   - **Result**: Reusable architecture for any domain

4. **Command Updated** (`.claude/commands/sp.loopflow.md`):
   - Adds Super Orchestra mode (lines 36-56)
   - Defines indicators for when to invoke
   - **Result**: `/sp.loopflow` now automatically detects when deep research needed

**Key Insight**: This session's intelligence is now **permanently encoded** in the system. Future chapters benefit automatically.

---

## 🎓 The Three Questions Answered

### Q1: What is Prerequisite Knowledge? (Design-Time)

**Answer**: Strategic decisions the architect must make that cannot be automated:

**Constitutional Decisions** (rare updates):
- Project vision ("Specs Are the New Syntax")
- Core principles (Graduated Teaching, Three Roles)
- Quality standards (what's "good"? what's anti-pattern?)

**Domain Patterns** (occasional updates):
- Project structure (9 lessons per chapter? 3-4 prompts per lesson?)
- Complexity mapping (Part 2 = A2 tier = max 7 concepts?)
- Prerequisites (Chapter 5 requires Chapters 1-4?)

**Why prerequisite**: AI cannot decide project vision or structure autonomously. These require human judgment, business context, domain expertise.

**Encoded in**: Constitution (`.specify/memory/constitution.md`), Chapter Index (`specs/book/chapter-index.md`), Skills (`.claude/skills/`)

### Q2: What Happens at Runtime? (Automatic Discovery)

**Answer**: Information retrieval and logical inference that AI executes automatically:

**Context Discovery** (every invocation):
- Library documentation (Context7: 8000 tokens in 5 minutes)
- Official sources (WebFetch: 3 URLs in 10 minutes)
- Existing specs (pattern matching)
- Available domain skills (which apply to this task?)

**Intelligence Synthesis** (automatic derivation):
- Audience tier (Chapter 5 → Part 2 → A2 tier → max 7 concepts)
- Prerequisites (dependency graph traversal)
- Teaching pattern (apply Graduated Teaching to A2 tier)
- AI usage strategy (simple = direct, complex = AI)

**Pattern Recognition** (validation):
- Compare to similar chapters (is structure consistent?)
- Detect anti-patterns (8 prompts >> 3-4 expected?)
- Validate against constitution (cognitive load within limit?)

**Why runtime**: This is information gathering and logical application that changes per task. Human architect doesn't need to manually research or validate—AI does it automatically.

**Tools**: Context7 MCP, WebFetch, Read/Grep/Glob, Intelligence Object generation logic

### Q3: What Actually Makes a Skill? (Capability Manifestation)

**Answer**: Three levels of skill manifestation:

**Level 1: Knowledge** (data in files):
- Constitution principles
- Domain patterns
- Anti-patterns
- **Limitation**: Knowledge alone is static. Must be applied.

**Level 2: Capability** (runtime application):
- AI reads knowledge + discovers context + synthesizes intelligence
- Applies to specific task (generate spec with correct structure)
- Validates against quality gates (cognitive load within limit?)
- **Example**: "Chapter Planning" capability = reading constitution + chapter-index + applying Graduated Teaching to generate plan.md

**Level 3: Reusable Skill** (packaged workflow):
- Agent definition (`.claude/agents/super-orchestra.md`)
- Orchestrates VI stack application automatically
- Invoked with minimal user input (`/invoke super-orchestra [goal]`)
- Documents intelligence journey for future reference
- **Example**: `super-orchestra` agent encodes entire deep research + market positioning workflow

**Key Insight**:
```
Skill = Knowledge (design-time)
      × Context Discovery (runtime)
      × Intelligence Synthesis (runtime)
      × Workflow Orchestration (agent)
      × Documentation Pattern (output style)
```

---

## 🚀 Practical Implications for Architects Using AIDD

### What You Design Once (Design-Time Investment)

**Constitution** (~2-3 days initial):
- Define project vision
- Establish core principles (10-20)
- Define target audience tiers
- Document quality standards and anti-patterns

**Domain Knowledge** (~1-2 days initial):
- Create project structure (chapter-index, lesson format)
- Define complexity mapping (Part → Tier → Cognitive Load)
- Establish prerequisite graph (dependencies)
- Build skills library (reusable pedagogical patterns)

**Total Design-Time**: 3-5 days for project foundation

**Maintenance**: 1-2 hours per month (update anti-patterns, refine principles)

### What AI Discovers Automatically (Runtime)

**Per Task** (15-30 minutes):
- Library documentation (Context7: 8000 tokens)
- Official sources (WebFetch: 3+ URLs)
- Existing specs (pattern matching)
- Intelligence object generation

**You Don't**:
- Manually research every library
- Specify audience tier every time (AI derives from chapter number)
- Validate every lesson against constitution (AI applies automatically)
- Repeat anti-pattern checks manually (AI flags violations)

**Result**: 2-3 hours saved per chapter (research + validation)

### What Gets Better Over Time (Skill Accumulation)

**Session 1**: Chapter 12 UV rework
- Lesson learned: "Don't over-engineer with AI for simple commands"
- Encoded: Constitution anti-patterns section
- Result: Future chapters automatically check for over-engineering

**Session 2**: Chapter 5 Skills/Plugins/MCP
- Lesson learned: "Deep research + market positioning creates 40x output"
- Encoded: `super-orchestra` agent + output style
- Result: Future chapters can invoke Super Orchestra with one command

**Session N**: Each chapter adds lessons
- Constitution gets refined (more precise anti-patterns)
- Agents get smarter (better pattern recognition)
- Skills library grows (more reusable capabilities)

**Key Insight**: **Every task makes the system smarter.** You're not just building chapters—you're building an intelligence-accumulating system.

---

## 📊 ROI Analysis: Design-Time vs Runtime

### Traditional Approach (No VI)

**Per Chapter** (6-8 hours):
- Gather requirements: 1 hour
- Research library docs: 2-3 hours
- Write spec: 1 hour
- Plan lessons: 1-2 hours
- Implement: 3-4 hours
- Validate: 1-2 hours
- **Total**: 9-16 hours per chapter

**13 Chapters**: 117-208 hours (3-5 weeks of full-time work)

### VI Pattern Approach

**Design-Time** (one-time):
- Constitution: 2-3 days (16-24 hours)
- Domain knowledge: 1-2 days (8-16 hours)
- **Total**: 24-40 hours (1 week of full-time work)

**Per Chapter** (3-4 hours):
- Intelligence discovery: 15 min (AI automated)
- Spec with VI context: 30 min
- Plan with VI context: 30 min
- Tasks with VI context: 30 min
- Implement with VI context: 1-2 hours
- Validate with VI context: 30 min
- **Total**: 3-4 hours per chapter

**13 Chapters**: 39-52 hours (1 week of full-time work)

**Total Time**:
- Design-time: 24-40 hours
- Runtime: 39-52 hours
- **Total**: 63-92 hours (1.5-2 weeks of full-time work)

**Savings**: 54-116 hours (50-70% reduction)

**But the REAL value**: Output quality is **market-defining** (surpasses official docs), not just "meets spec."

---

## 🎯 Summary

### Design-Time (Architect Responsibility)
**What**: Strategic decisions about project vision, structure, quality standards
**Why**: Cannot be automated (requires human judgment, business context, domain expertise)
**Encoded**: Constitution, Chapter Index, Skills Library
**Time**: 3-5 days initial, 1-2 hours/month maintenance

### Runtime (AI Automatic)
**What**: Information retrieval, logical inference, pattern recognition
**Why**: Can be automated (information gathering, applying established rules)
**Tools**: Context7, WebFetch, Intelligence Object generation
**Time**: 15-30 minutes per task (would take human 2-3 hours manually)

### Skill Manifestation (System Evolution)
**Level 1 (Knowledge)**: Data in files (constitution, patterns, anti-patterns)
**Level 2 (Capability)**: AI applying knowledge to tasks (runtime synthesis)
**Level 3 (Reusable Skill)**: Packaged workflow (agents orchestrating VI stack)
**Result**: System gets smarter with each task. Intelligence accumulates.

### The 40x Multiplier Formula
```
40x = (Depth of Knowledge × Quality of Context Discovery × Intelligence Synthesis)
    × Workflow Orchestration
    × System Evolution (accumulated learnings)
```

**Not from speed, but from DEPTH + INTELLIGENCE + QUALITY + ACCUMULATION.**

---

**This is the meta-architecture of Vertical Intelligence for AI-Driven Development.** 🎯🚀

**Date**: 2025-01-13
**Audience**: Architects building with AIDD
**Next**: Apply this understanding to design your own VI stack for your domain
