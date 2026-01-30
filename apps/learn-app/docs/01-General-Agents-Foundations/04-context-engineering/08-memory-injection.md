---
sidebar_position: 8
title: "Mid-Stream Memory: Injecting Context at Execution Time"
description: "How to prevent workflow drift by injecting relevant memories at the right moment—ensuring AI has the context it needs for what it's doing NOW, not what you started doing"
keywords:
  [
    "memory injection",
    "workflow drift",
    "semantic memory",
    "execution-time context",
    "PreToolUse hook",
    "UserPromptSubmit",
    "thinking blocks",
    "vector search",
    "deduplication strategy",
    "professional workflows",
    "context relevance",
  ]
chapter: 4
lesson: 8
duration_minutes: 90

# HIDDEN SKILLS METADATA
skills:
  - name: "Understanding Workflow Drift"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain why memories injected at prompt submission become irrelevant as workflows evolve, describing the gap between turn 1 context and turn 20 execution needs across any professional domain"

  - name: "Distinguishing Injection Timing Strategies"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can compare UserPromptSubmit and PreToolUse injection timing, explaining when each is appropriate and why PreToolUse maintains relevance during long workflows"

  - name: "Implementing PreToolUse Memory Injection"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can implement a PreToolUse hook that extracts thinking blocks, queries a vector database for similar memories, and injects them via additionalContext within performance constraints"

  - name: "Designing Deduplication Strategies"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can implement a deduplication system using thinking hashes to prevent the same memory from being injected repeatedly across multiple tool calls"

learning_objectives:
  - objective: "Explain the workflow drift problem and why prompt-time memory injection fails for long-running tasks"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can describe a scenario where turn 1 memories become irrelevant by turn 20, explaining the mismatch between initial intent and evolved execution context"

  - objective: "Compare UserPromptSubmit and PreToolUse injection timing strategies"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student can create a decision matrix showing when to use each strategy based on workflow length, context evolution, and relevance requirements"

  - objective: "Implement a PreToolUse semantic memory injection hook"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student creates a working hook that extracts the last 1,500 characters of thinking, embeds and queries against a vector database, and injects top results via additionalContext in under 500ms"

  - objective: "Design deduplication logic for memory injection systems"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student implements a temp log with thinking hashes that prevents repeated injection of the same memory within a session"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (workflow drift, injection timing comparison, thinking block extraction, vector search integration, additionalContext injection, deduplication via hashing) within B1-B2 range (5-7)"

differentiation:
  extension_for_advanced: "Implement multi-tiered memory with different embedding models for code vs natural language; add confidence scoring to filter low-relevance memories before injection"
  remedial_for_struggling: "Start with a mock vector database (in-memory dictionary with exact match) before adding actual embeddings; focus on the hook lifecycle before optimizing performance"
---

# Mid-Stream Memory: Injecting Context at Execution Time

Imagine an employee who gets reminded of relevant company policies exactly when making decisions, not just at the start of the day.

At 9am, you brief them: "Here are our quality standards, client preferences, and the project scope." Perfect. By 3pm, they're making a critical decision—but the morning briefing has faded. They remember the general direction but not the specific constraint that matters right now.

Now imagine a different employee. Every time they're about to make a decision, a helpful colleague appears: "Hey, remember the Johnson incident? Here's what you need to know for this exact situation." That's memory injection.

You start a complex task with a clear goal. Your AI assistant knows your preferences, your project conventions, your stakeholder requirements. Turn 1 goes perfectly. By turn 20, the AI has forgotten half of what made turn 1 successful.

What happened?

The memories you injected at the beginning are still in context. They haven't disappeared. But they're now buried under 19 turns of conversation, research outputs, and evolving requirements. The AI's attention budget (Lesson 2) means those turn 1 memories are receiving only a fraction of the processing power they need. More importantly, those memories were selected for turn 1's intent. Turn 20 has different intent. The memories that would help turn 20 are sitting unused in your memory store.

This is **workflow drift**. And fixing it requires a fundamental shift in when and how you inject context.

## The Workflow Drift Problem

Semantic memory injection typically happens at prompt submission. You type a request. A hook queries your memory store for relevant context. The results are injected into the AI's context. Then the AI processes your request.

This works well for single-turn interactions. But multi-turn workflows create a problem:

**Consider a legal professional reviewing a complex contract:**

**Turn 1:** You ask the AI to review vendor agreement terms. The memory hook finds relevant memories about your firm's standard terms, this client's risk tolerance, and contract negotiation history. Perfect match.

**Turn 5:** The AI has identified a problematic indemnification clause. It's now focused on liability allocation. Your general contract memories are still there, but they're less relevant than memories about indemnification precedents and insurance requirements.

**Turn 12:** The AI is drafting alternative language for the dispute resolution section. It needs memories about this client's arbitration preferences and past dispute history. The indemnification memories from turn 5 are noise.

**Turn 20:** The AI is preparing a summary memo for the partner. The drafting memories from turn 12 are now irrelevant. Client communication preferences would help, but they were never injected.

**Or consider a marketing strategist developing a campaign:**

**Turn 1:** You ask the AI to develop Q4 campaign strategy. The memory hook finds brand voice guidelines, audience demographics, and budget parameters. Perfect match.

**Turn 5:** The AI has pivoted to channel strategy. It's evaluating media mix options. Your brand voice memories are still there, but they're less relevant than memories about channel performance history and media costs.

**Turn 12:** The AI is writing creative briefs for each channel. It needs memories about past creative that worked with this audience, design constraints, and production timelines. The channel strategy memories from turn 5 are noise.

**Turn 20:** The AI is forecasting campaign ROI for leadership approval. The creative brief memories from turn 12 are now irrelevant. CFO preferences for financial presentations would help, but they were never injected.

Each turn, the AI's actual needs drift further from the context you provided at the start. The memories you injected were correct for turn 1. They're wrong for turn 20.

## Two Injection Timing Strategies

Claude Code's hook system offers two points where you can inject context:

| Hook                 | When It Fires              | Best For                                                        |
| -------------------- | -------------------------- | --------------------------------------------------------------- |
| **UserPromptSubmit** | When user submits a prompt | Initial context, session setup, one-shot queries                |
| **PreToolUse**       | Before each tool execution | Ongoing relevance, multi-step workflows, execution-time context |

**UserPromptSubmit** happens once per user message. It's synchronous with your input. The memories it injects reflect what you asked for at that moment.

**PreToolUse** happens potentially many times per user message. Each time the AI is about to use a tool—reading a document, searching files, editing content—this hook fires. That means you get multiple opportunities to inject relevant context throughout the workflow.

The key insight: The AI's thinking evolves during the reasoning process. By turn 20, the AI's thinking block contains intent and reasoning about what it's about to do next. That thinking is the perfect query for semantic memory.

## PreToolUse Memory Injection Architecture

Here's the flow:

```
1. User submits prompt
2. AI reasons about the request → creates thinking block
3. AI decides to take an action (read file, search, edit document)
4. PreToolUse hook fires (synchronous)
   └── Hook reads AI's recent thinking (last 1,500 chars)
   └── Hook embeds the thinking text
   └── Hook queries vector database for similar memories
   └── Hook injects top N memories via additionalContext
5. AI receives the injected memories
6. AI continues reasoning with fresh, relevant context
7. Action executes
8. AI reasons about results → new thinking block
9. AI decides to take another action
10. PreToolUse fires again...
```

**Why this works:** The AI's thinking block contains what it is about to do and why. When you embed that thinking and search for similar memories, you find memories that are relevant to the current action, not the original prompt.

**Legal example:** Turn 20's thinking might be: "I need to summarize the key risks in this agreement for the partner review memo. The main concerns are the indemnification carve-outs and the ambiguous termination provisions. I should highlight these in language appropriate for partner consumption."

Embedding that thinking and searching your memory store finds:

- Partner memo formatting preferences
- This partner's risk communication style
- Previous memos on similar contract issues

These memories are exactly what turn 20 needs. They would never have been selected at turn 1 when the thinking was about reviewing contract terms.

**Marketing example:** Turn 20's thinking might be: "I need to forecast ROI for leadership approval. The campaign costs total $450K across channels. I should present this using the format the CFO prefers."

Embedding that thinking finds:

- CFO presentation preferences
- ROI calculation standards your company uses
- Past campaign performance benchmarks

Again—exactly what turn 20 needs, not what turn 1 needed.

## Why Thinking Blocks Matter

The AI's thinking isn't just internal monologue. It's structured reasoning that reveals:

- **Current intent:** What the AI is trying to accomplish right now
- **Decision context:** Why the AI chose this approach
- **Constraints remembered:** What limitations the AI is working within
- **Assumptions made:** What the AI believes to be true

This makes thinking blocks the ideal query for semantic search. They contain the dense, specific context about what the AI needs to know.

Compare:

**User prompt (turn 1):** "Review the vendor agreement"

- Broad, could match many memories
- Matches general contract memories
- Doesn't indicate current state

**Thinking block (turn 20):** "I'm preparing the partner memo summarizing key contract risks. The main issues are the indemnification carve-outs in Section 7.2 and the ambiguous termination language in Section 12.1. I should use the format the partner prefers for risk summaries."

- Specific, narrow match space
- Matches memo writing memories, risk communication preferences
- Indicates exactly what the AI needs to know

The specificity of thinking blocks produces more relevant memory retrievals.

## Building Your Memory Corpus

A memory injection system is only as good as its memories. What should you store?

**High-value memories across domains:**

| Domain         | High-Value Memories                                                                                 |
| -------------- | --------------------------------------------------------------------------------------------------- |
| **Legal**      | Precedent patterns, client risk preferences, judge tendencies, clause variations that have worked   |
| **Marketing**  | Brand voice rules, audience insights, successful campaign patterns, stakeholder presentation styles |
| **Research**   | Citation standards, methodology conventions, reviewer preferences, field-specific writing patterns  |
| **Business**   | Process templates, stakeholder communication styles, industry conventions, decision-making patterns |
| **Operations** | Vendor preferences, compliance requirements, approval workflows, exception handling patterns        |
| **Software**   | Error handling patterns, API conventions, architectural decisions, testing strategies               |

**Lower-value memories (across all domains):**

- Standard practices the AI already knows
- Obvious patterns the AI can infer from documents
- One-time decisions that won't recur
- Information that changes frequently

**Memory structure example (Legal):**

```markdown
# Memory: Client Risk Communication for Acme Corp

## Summary

Acme Corp's General Counsel prefers risk summaries that lead with business impact,
not legal analysis. Always quantify exposure when possible.

## Context

After the Henderson dispute, their GC restructured how legal communicates risk
to the board. They now require dollar ranges, not just "material exposure."

## Pattern

GOOD: "This clause exposes us to $500K-$2M in potential liability if the vendor
fails to deliver. We recommend adding a cap at $750K."

NOT: "The indemnification provisions create significant exposure that should
be addressed through additional limitations."

## When to Apply

Any client communication about contract risk. Any memo going to their GC.
```

**Memory structure example (Marketing):**

```markdown
# Memory: CFO Presentation Format

## Summary

CFO requires all campaign proposals to lead with ROI projection and
payback period before any creative discussion.

## Context

After Q2 2024 campaign exceeded budget without clear ROI tracking, CFO
mandated new financial-first presentation format.

## Pattern

GOOD: "This $450K campaign projects 3.2x ROI with 4-month payback, based on
comparable Q3 2023 campaign performance. Here's the channel breakdown..."

NOT: "We've developed an exciting creative concept that will resonate with
our target demographic. The budget is $450K."

## When to Apply

Any campaign proposal going to leadership. Any budget approval request.
```

**Memory structure example (Research):**

```markdown
# Memory: Journal of Applied Psychology Submission Standards

## Summary

JAP requires APA 7th edition with DOI links. Reviewers in this journal
expect power analysis justification and effect size reporting.

## Context

Our lab's 2023 submission was desk-rejected for insufficient power analysis
documentation despite strong methodology otherwise.

## Pattern

GOOD: "Power analysis using G\*Power indicated a required sample of n=120
to detect medium effects (d=0.50) with 80% power at alpha=.05. Our sample
of n=147 exceeded this threshold."

NOT: "The sample size was adequate for the planned analyses."

## When to Apply

Any submission to JAP or similar APA journals in organizational psychology.
```

**Start with 10-20 memories.** You don't need a massive corpus. A focused collection of genuinely useful memories outperforms a large collection of noise.

## Combining Both Injection Strategies

PreToolUse doesn't replace UserPromptSubmit. They serve different purposes:

| Strategy             | Use When                                                         |
| -------------------- | ---------------------------------------------------------------- |
| **UserPromptSubmit** | Session initialization, user preferences, project-wide context   |
| **PreToolUse**       | Task-specific memories, execution-time relevance, long workflows |

A robust system uses both:

1. **UserPromptSubmit** injects baseline context: project conventions, user preferences, active working context
2. **PreToolUse** injects execution-time context: memories relevant to what the AI is doing right now

This layered approach provides both stability (consistent baseline) and adaptability (evolving relevance).

## Lab: Understanding Memory Injection

**Objective:** Understand how workflow drift affects your work and design a memory corpus that maintains relevance throughout multi-step tasks.

**Duration:** 90 minutes

**Choose your path:**

- **Conceptual Track** (60 min): Design memory corpus and understand injection timing
- **Technical Track** (additional 60 min): Implement a working memory injection hook

---

### Part 1: Workflow Drift Analysis (All Participants, 30 min)

**Step 1: Map Your Own Workflow Drift**

Think about a recent complex task you worked on with AI assistance. This could be:

- **Legal:** Reviewing a complex agreement and preparing a client memo
- **Marketing:** Developing a campaign from strategy through creative briefs
- **Research:** Moving from literature review through methodology design
- **Business:** Analyzing a process and developing recommendations
- **Operations:** Troubleshooting an issue across multiple systems

Write down the major turns in that workflow:

```
Turn 1: What you started with
Turn 5: How the focus shifted
Turn 10: What you were working on at this point
Turn 15: How the work evolved further
Turn 20: What you ended up doing
```

**Step 2: Identify the Context Gaps**

For each turn, answer:

- What context would have been most helpful at this turn?
- How different is that from what would have helped at Turn 1?
- What memories were relevant earlier but are now noise?
- What memories would you wish the AI had access to?

**Step 3: Quantify the Drift**

Create a simple drift score for your workflow:

| Turn | Relevance of Turn 1 Context | New Context Needed |
| ---- | --------------------------- | ------------------ |
| 1    | 100%                        | (baseline)         |
| 5    | ?%                          | (list new needs)   |
| 10   | ?%                          | (list new needs)   |
| 15   | ?%                          | (list new needs)   |
| 20   | ?%                          | (list new needs)   |

This exercise makes workflow drift concrete and visible.

---

### Part 2: Memory Corpus Design (All Participants, 30 min)

**Step 1: Brainstorm High-Value Memories**

Based on your workflow analysis, list 15-20 memories that would have helped at different points. Don't worry about format yet—just capture the knowledge.

**Step 2: Categorize by Relevance Pattern**

Group your memories:

**Always Relevant** (inject at UserPromptSubmit):

- General preferences that apply throughout
- Project-wide conventions
- Stakeholder communication styles

**Situationally Relevant** (inject at PreToolUse):

- Task-specific patterns
- Stage-specific knowledge
- Context-dependent rules

**Step 3: Structure 5-7 Key Memories**

Pick your highest-value situationally relevant memories and structure them:

```markdown
# Memory: [Clear, searchable title]

## Summary

[One paragraph: what this memory captures]

## Context

[Why this became important—the history]

## Pattern

[Concrete example of good practice]
[Contrast with what to avoid]

## When to Apply

[Trigger conditions—what thinking would retrieve this]
```

**Deliverable (Conceptual Track):** A memory corpus document with 5-7 well-structured memories for your domain.

---

### Part 3: Technical Implementation (Optional, 60 min)

For those who want to build a working system:

#### Phase A: Set Up Vector Database (20 min)

**Option A: ChromaDB (Recommended)**

```bash
pip install chromadb sentence-transformers
```

```python
import chromadb
from chromadb.utils import embedding_functions

# Initialize with local embedding
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"  # Fast, good quality
)

client = chromadb.Client()
collection = client.create_collection(
    name="professional_memories",
    embedding_function=ef
)
```

**Option B: SQLite with Vector Extension**

If you prefer SQLite, use sqlite-vss or sqlite-vec. The setup is more involved but keeps everything in a single file.

#### Phase B: Populate Memory Corpus (15 min)

Add your structured memories from Part 2:

```python
memories = [
    {
        "id": "client-risk-communication",
        "content": """Client Risk Communication for Acme Corp

Acme Corp's General Counsel prefers risk summaries that lead with business impact,
not legal analysis. Always quantify exposure when possible.

After the Henderson dispute, their GC restructured how legal communicates risk.
They now require dollar ranges, not just "material exposure."

Pattern:
GOOD: "This clause exposes us to $500K-$2M in potential liability..."
BAD: "The indemnification provisions create significant exposure..."

Apply to: Any client communication about contract risk. Any memo to their GC."""
    },
    # Add 4-6 more memories...
]

collection.add(
    ids=[m["id"] for m in memories],
    documents=[m["content"] for m in memories]
)
```

#### Phase C: Write the Hook (20 min)

Create `memory_hook.py`:

```python
import hashlib
import time
import re
from dataclasses import dataclass

@dataclass
class Memory:
    id: str
    content: str
    similarity: float

class DeduplicationLog:
    def __init__(self, ttl_seconds: int = 300):
        self.recent: dict[str, float] = {}
        self.ttl = ttl_seconds

    def should_inject(self, memory_id: str, thinking_hash: str) -> bool:
        key = f"{memory_id}:{thinking_hash}"
        now = time.time()
        self.recent = {k: v for k, v in self.recent.items() if now - v < self.ttl}
        if key in self.recent:
            return False
        self.recent[key] = now
        return True

def extract_thinking(transcript: str, char_limit: int = 1500) -> str:
    """Extract recent thinking from transcript."""
    pattern = r'<thinking>(.*?)</thinking>'
    matches = re.findall(pattern, transcript, re.DOTALL)
    if not matches:
        return ""
    return matches[-1].strip()[-char_limit:]

def search_memories(collection, thinking: str, top_k: int = 3) -> list[Memory]:
    """Query ChromaDB for similar memories."""
    if not thinking:
        return []

    results = collection.query(
        query_texts=[thinking],
        n_results=top_k
    )

    memories = []
    for i, doc_id in enumerate(results['ids'][0]):
        memories.append(Memory(
            id=doc_id,
            content=results['documents'][0][i],
            similarity=1 - results['distances'][0][i]
        ))

    # Filter low similarity
    return [m for m in memories if m.similarity > 0.3]

def format_injection(memories: list[Memory]) -> str:
    """Format memories for AI consumption."""
    if not memories:
        return ""

    lines = ["## Relevant Memories\n"]
    for m in memories:
        lines.append(f"### {m.id} (relevance: {m.similarity:.0%})")
        lines.append(m.content)
        lines.append("")

    return "\n".join(lines)

def on_pre_tool_use(transcript: str, collection, dedup_log: DeduplicationLog) -> str:
    """Called before each tool execution."""
    start = time.time()

    thinking = extract_thinking(transcript)
    if not thinking:
        return ""

    memories = search_memories(collection, thinking)

    thinking_hash = hashlib.md5(thinking.encode()).hexdigest()[:8]
    memories = [m for m in memories if dedup_log.should_inject(m.id, thinking_hash)]

    result = format_injection(memories)

    elapsed = time.time() - start
    if elapsed > 0.5:
        print(f"Warning: Memory injection took {elapsed:.2f}s")

    return result
```

#### Phase D: Test the Hook (5 min)

```python
# test_memory_hook.py
from memory_hook import *
import chromadb
from chromadb.utils import embedding_functions

# Setup
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
client = chromadb.Client()
collection = client.create_collection("test_memories", embedding_function=ef)

# Add test memories
collection.add(
    ids=["risk-communication", "presentation-format", "methodology-standards"],
    documents=[
        "Client prefers risk summaries with dollar ranges, not vague language.",
        "CFO requires ROI projection first before any creative discussion.",
        "Journal expects power analysis and effect size reporting."
    ]
)

dedup = DeduplicationLog()

# Test 1: Legal context
thinking1 = "I'm preparing a memo about contract risks for the client."
result1 = on_pre_tool_use(f"<thinking>{thinking1}</thinking>", collection, dedup)
print("Test 1 - Risk communication query:")
print(result1)

# Test 2: Marketing context
thinking2 = "I need to present this campaign budget to the CFO."
result2 = on_pre_tool_use(f"<thinking>{thinking2}</thinking>", collection, dedup)
print("Test 2 - Presentation format query:")
print(result2)
```

**Deliverable (Technical Track):** A working memory injection hook with domain-relevant memories.

---

### Assessment Criteria

**Conceptual Understanding (All Participants):**

- Can explain workflow drift with domain-specific examples
- Can distinguish UserPromptSubmit from PreToolUse timing
- Has designed a coherent memory corpus for their domain

**Technical Implementation (Optional):**

- Hook extracts thinking from transcript
- Vector search returns relevant memories
- Deduplication prevents repeated injection
- Performance under 500ms

## Common Issues and Solutions

**Problem: Memories too generic, match everything**

Solution: Make memories specific. Instead of "communicate clearly with clients," write "Acme Corp's GC requires dollar ranges in risk summaries—never use vague terms like 'significant exposure.'"

**Problem: Thinking blocks empty or too short**

Solution: This happens early in workflows before the AI has reasoned much. The hook should gracefully return nothing. Prompt-time injection (UserPromptSubmit) handles early turns.

**Problem: Same memories injected repeatedly despite deduplication**

Solution: The thinking hash changed. This is actually correct behavior. If thinking changed significantly, the memory might be relevant in this new context. Tune your TTL if this is too aggressive.

**Problem: Memories from wrong domain being retrieved**

Solution: Add domain tags to your memories and filter by current context. Or maintain separate collections for different types of work.

## Try With AI

### Prompt 1: Diagnose Your Workflow Drift

```
I'm going to describe a multi-step workflow from my field. For each step, tell me:
1. What context would be most helpful at this step
2. How different that is from step 1's context
3. What memories you wish you had access to

My field: [legal/marketing/research/business/operations/other]

The workflow:
Step 1: [Describe your starting point]
Step 5: [How the work evolved]
Step 10: [Current focus at this point]
Step 15: [Further evolution]
Step 20: [What you ended up doing]

Show me how context needs evolve across this workflow.
```

**What you're learning:** Workflow drift is invisible until you examine it explicitly. This prompt makes the drift concrete by tracking context needs across steps in YOUR domain. You're learning to anticipate where prompt-time injection will fail.

### Prompt 2: Design Your Memory Corpus

```
I work in [describe your field and typical projects in 2-3 sentences].

Help me design a memory corpus of 10-15 memories that would be most valuable
for semantic injection during my workflows. For each memory, specify:
1. Title (searchable identifier)
2. Core content (what AI needs to know)
3. When it's relevant (what thinking would trigger retrieval)

Prioritize memories that:
- Contain non-obvious conventions or preferences
- Apply frequently during my work
- Would be hard for AI to infer from documents alone

Avoid memories that:
- State standard professional practices
- Would match too many different contexts
- Contain information that changes frequently
```

**What you're learning:** Memory corpus design is intentional, not exhaustive. This prompt trains you to identify high-value memories for YOUR domain. You're learning the difference between memories that genuinely help versus documentation that happens to exist.

### Prompt 3: Evaluate Injection Timing

```
For each of these knowledge types from my field, recommend the injection strategy
(UserPromptSubmit, PreToolUse, both, or neither) and explain why:

1. My general writing style preferences
2. The specific project I'm working on today
3. Client/stakeholder communication preferences for specific recipients
4. Standard conventions in my field
5. Historical context about why decisions were made
6. Current deadlines and time constraints
7. My organization's approval workflows
8. Quality standards and review criteria

Format as a table with columns: Knowledge Type | Strategy | Reasoning
```

**What you're learning:** Not all context needs the same injection strategy. Some context is stable across the entire session. Some evolves with the workflow. This prompt builds intuition for matching context to injection timing in your professional domain.
