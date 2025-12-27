# 6-Point Spec Blueprint for Skills & Agents

**Purpose**: Every skill and agent MUST include these 6 components to function as a "senior-level" capability, not a fragile prototype.

---

## The 6 Components

### 1. Identity (Persona)

**What to Include**:
- Role ("Senior Content Quality Auditor", "MCP Integration Specialist")
- Tone ("Precise, evidence-based", "Encouraging but rigorous")
- Expertise level ("Expert in pedagogical design", "Deep knowledge of MCP protocol")

**Template**:
```markdown
## Identity

**Role**: [Job title that defines expertise]
**Tone**: [1-2 adjectives describing communication style]
**Expertise**: [What this persona knows deeply]
```

**Why**: Claude performs better with defined personas. Generic "helpful assistant" = generic output.

---

### 2. Context (MCP & Data)

**What to Include**:
- Tool access ("Requires Read, Grep, WebSearch")
- Knowledge base references ("Read constitution.md first")
- MCP servers if applicable ("Access stripe-mcp for billing data")
- External docs to fetch ("Fetch SDK README from GitHub")

**Template**:
```markdown
## Context

### Required Files (Read First)
- `.specify/memory/constitution.md` - Constitutional principles
- `[other required files]`

### Tools Required
- Read, Write, Edit (file operations)
- WebSearch, WebFetch (research)

### MCP Servers (if applicable)
- `[mcp-server-name]` - For [purpose]

### External Documentation
- Fetch: `https://[url]` for [purpose]
```

**Why**: Without context specification, agents operate blind and hallucinate.

---

### 3. Logic (Guardrails)

**What to Include**:
- Mandatory steps ("MUST read quality memory before generating")
- "Never" list ("NEVER expose framework labels to students")
- External scripts for deterministic operations
- Decision trees for complex logic

**Template**:
```markdown
## Logic

### Mandatory Steps
1. [Step that MUST happen first]
2. [Step that MUST happen second]
3. [etc.]

### NEVER (Critical Violations)
- ❌ NEVER [action that would cause failure]
- ❌ NEVER [action that violates principles]

### Decision Tree
```
IF [condition A]
  → [action A]
ELSE IF [condition B]
  → [action B]
ELSE
  → [default action]
```

### External Scripts (Deterministic)
- `scripts/validate.sh` - For [purpose]
```

**Why**: Without guardrails, agents make expensive mistakes that require human cleanup.

---

### 4. Success Trigger

**What to Include**:
- Keywords that activate the skill ("evaluate lesson", "review quality")
- File types it handles ("*.md files in apps/learn-app/docs/")
- Contexts where it applies ("After content-implementer completes")

**Template**:
```markdown
## Success Trigger

### Activation Keywords
- "evaluate [lesson|content|chapter]"
- "check quality of"
- "run [skill-name]"

### File Types
- `*.md` files in educational content directories
- YAML frontmatter with `learning_objectives`

### Invocation Contexts
- Automatic: After content generation
- Manual: User requests evaluation
- Workflow: Part of /sp.implement pipeline
```

**Why**: Without clear triggers, agents don't know when to activate.

---

### 5. Output Standard

**What to Include**:
- Template format (Markdown report, JSON, YAML)
- Required sections in output
- Reporting channels (file path, console summary)

**Template**:
```markdown
## Output Standard

### Format
[Markdown | JSON | YAML]

### Required Sections
1. [Section 1 name and purpose]
2. [Section 2 name and purpose]
3. [etc.]

### Output Location
- Primary: `[file path or console]`
- Summary: `[brief format for orchestrator]`

### Example Output
```[format]
[minimal example]
```
```

**Why**: Without output standards, agents produce inconsistent, unparseable results.

---

### 6. Error Protocol

**What to Include**:
- Fallback behavior when tools unavailable
- Graceful degradation options
- Error reporting format
- Human escalation triggers

**Template**:
```markdown
## Error Protocol

### Tool Unavailable
| Tool | Fallback |
|------|----------|
| WebSearch | Use cached knowledge, note limitation |
| MCP server | Skip integration, report as incomplete |
| External script | Manual validation, flag for human review |

### Graceful Degradation
IF [critical tool unavailable]
  → Report limitation clearly
  → Complete what IS possible
  → Mark output as "PARTIAL - requires human verification"

### Error Reporting
```
❌ ERROR: [Tool/Resource] unavailable
Impact: [What couldn't be completed]
Recommendation: [Next step for human]
```

### Human Escalation
Escalate to human when:
- [ ] Constitutional violation detected
- [ ] Ambiguous requirements
- [ ] [Other escalation triggers]
```

**Why**: Without error protocols, agents fail silently or block workflows.

---

## Compliance Checklist

Before publishing any skill or agent:

- [ ] **Identity**: Persona defined with role, tone, expertise
- [ ] **Context**: Required files, tools, MCPs listed
- [ ] **Logic**: Mandatory steps, NEVER list, decision trees
- [ ] **Success Trigger**: Keywords, file types, invocation contexts
- [ ] **Output Standard**: Format, sections, location, example
- [ ] **Error Protocol**: Fallbacks, degradation, escalation

**Score**: [X/6 components] → If < 6, skill is incomplete.

---

## Example: Complete Skill

See `content-evaluation-framework` (after upgrade) for reference implementation.
