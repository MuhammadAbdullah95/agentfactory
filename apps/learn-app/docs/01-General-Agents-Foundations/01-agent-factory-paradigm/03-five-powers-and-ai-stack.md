---
title: "Five Powers and the Modern AI Stack"
chapter: 1
lesson: 3
duration_minutes: 30
sidebar_position: 3

# HIDDEN SKILLS METADATA
skills:
  - name: "Understanding the UX→Intent Paradigm Shift"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Literacy"
    measurable_at_this_level: "Student can explain the transition from navigation-based interfaces to conversation-based intent and identify which workflows benefit from agentic AI"

  - name: "Identifying the Five Powers of AI Agents"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can recognize and categorize agent capabilities (See, Hear, Reason, Act, Remember) in real systems and explain how they combine to enable autonomous orchestration"

  - name: "Understanding the Three-Layer AI Development Architecture"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can identify and explain the three layers of the modern AI stack: frontier models, AI-first IDEs, and development agents, plus the role of MCP as interoperability standard"

learning_objectives:
  - objective: "Understand the paradigm shift from User Interface (navigation-based) to User Intent (conversation-based) interaction"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Explanation comparing traditional UX workflows versus agentic intent-driven workflows with concrete examples"

  - objective: "Identify the Five Powers (See, Hear, Reason, Act, Remember) and explain how they combine to enable autonomous orchestration"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Analysis of real agentic systems to categorize capabilities by the Five Powers framework"

  - objective: "Recognize the three layers of the modern AI stack and describe what each layer provides"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Classification of AI tools (models, IDEs, agents) into appropriate stack layers with explanation of their roles"

  - objective: "Understand how Model Context Protocol enables tool interoperability and prevents vendor lock-in"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Explanation of MCP as universal standard connecting agents to data/services, analogous to USB for computing"

# Cognitive load tracking
cognitive_load:
  new_concepts: 9
  assessment: "9 concepts (UX→Intent shift, Five Powers, Predictive→Generative→Agentic evolution, 3-layer stack, MCP) within A2 limit of 10 concepts. Framework-heavy but logically connected. ✓"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Analyze a complex agentic system (like Claude Code or customer service AI) to map all Five Powers and identify which powers are most critical for its use case; then research how MCP enables custom integrations for that system"
  remedial_for_struggling: "Focus on single concrete comparison: hotel booking via traditional website (14 steps) vs agentic AI (3 exchanges), then map each action in the agentic version to the Five Powers"

# Generation metadata
generated_by: "content-implementer v2.0.0 (Part 1 consolidation)"
source_spec: "Part 1 consolidation: 4 chapters (32 lessons) → 1 chapter (8 lessons)"
created: "2025-01-22"
git_author: "Claude Code"
workflow: "lesson consolidation (lessons 07 + 08 → 03)"
version: "1.0.0"

# Legacy compatibility (Docusaurus)
prerequisites:
  - "Understanding of basic AI concepts (from Lesson 1-2)"
  - "Familiarity with traditional software interfaces"
---

# Five Powers and the Modern AI Stack

Something fundamental is changing in how humans interact with software. For decades, we built interfaces—buttons, menus, forms—and trained users to navigate them. Success meant making interfaces "intuitive." But what if the interface disappeared entirely? What if users just stated what they wanted, and software figured out how to do it?

This transformation is possible because AI has evolved through three phases: **Predictive AI** (forecasting from data), **Generative AI** (creating content), and now **Agentic AI** (autonomous action). The agentic era combines five capabilities—the **Five Powers**—with a modular **three-layer stack** that makes composition possible. Understanding both the capabilities (what agents can do) and the architecture (how they're built) is essential for building effective AI systems.

This lesson unifies two foundational frameworks: the **Five Powers** that enable autonomous orchestration, and the **Modern AI Stack** that provides the technical foundation. Together, they explain both *why* the UX→Intent shift is happening now and *how* to build systems that leverage it.

---

## Part 1: From User Interface to User Intent

Traditional software interaction follows this model:

**User → Interface → Action**

- **Users navigate** through explicit interfaces (menus, buttons, forms)
- **Every action requires manual initiation** (click, type, submit)
- **Workflows are prescribed** (step 1 → step 2 → step 3)
- **Users must know WHERE to go and WHAT to click**
- **The interface is the bottleneck** between intent and execution

### Example: Booking a Hotel (Traditional UX)

Let's walk through what this looks like in practice:

1. Open travel website
2. Click "Hotels" in navigation menu
3. Enter destination city in search box
4. Select check-in date from calendar picker
5. Select check-out date from calendar picker
6. Click "Search" button
7. Review list of 50+ hotels
8. Click on preferred hotel
9. Select room type from dropdown
10. Click "Book Now"
11. Fill out guest information form (8 fields)
12. Fill out payment form (16 fields)
13. Click "Confirm Booking"
14. Wait for email confirmation

**Total: 14 manual steps**, each requiring the user to know exactly what to do next.

**The design challenge**: Make these 14 steps feel smooth. Reduce friction. Optimize button placement. Minimize form fields. A/B test checkout flow.

**This is "User Interface thinking"**: The user must navigate the interface the developers designed.

### The New Paradigm: User Intent

Now consider a fundamentally different model:

**User Intent → Agent → Orchestrated Actions**

- **Users state intent conversationally** ("I need a hotel in Chicago Tuesday night")
- **AI agents act autonomously** (search, compare, book, confirm)
- **Workflows are adaptive** (agent remembers preferences, anticipates needs)
- **Users describe WHAT they want; agents figure out HOW**
- **Conversation replaces navigation**

### Example: Booking a Hotel (Agentic UX)

The same goal, achieved differently:

**User**: "I need a hotel in Chicago next Tuesday night for a client meeting downtown."

**Agent**: "Found 3 options near downtown. Based on your preferences, I recommend the Hilton Garden Inn—quiet floor available, $189/night, free breakfast. Your usual king bed non-smoking room?"

**User**: "Yes, book it."

**Agent**: "Done. Confirmation sent to your email. Added to calendar. Uber scheduled for Tuesday 8am to O'Hare. Need anything else?"

**Total: 3 conversational exchanges** replacing 14 manual steps.

**What the agent did autonomously:**
- ✅ Remembered user preferences (quiet rooms, king bed, non-smoking)
- ✅ Inferred need for transportation (scheduled Uber without being asked)
- ✅ Integrated with calendar automatically
- ✅ Understood context (client meeting = business district location)

**This is "User Intent thinking"**: The user expresses goals; the agent orchestrates execution.

---

## Part 2: The Five Powers of AI Agents

Agentic AI can accomplish this transformation because it possesses five fundamental capabilities that, when combined, enable autonomous orchestration:

### 1. 👁️ See — Visual Understanding

**What it means:**
- Process images, screenshots, documents, videos
- Extract meaning from visual context
- Navigate interfaces by "seeing" them
- Understand diagrams and visual data

**Example:**
- Claude Code reading error screenshots to debug issues
- AI extracting data from invoices and receipts
- Agents clicking buttons by visually locating them on screen

### 2. 👂 Hear — Audio Processing

**What it means:**
- Understand spoken requests (voice interfaces)
- Transcribe and analyze conversations
- Detect sentiment and tone
- Process audio in real-time

**Example:**
- Voice assistants understanding natural speech
- Meeting transcription and summarization
- Customer service AI detecting frustration in tone

### 3. 🧠 Reason — Complex Decision-Making

**What it means:**
- Analyze tradeoffs and constraints
- Make context-aware decisions
- Chain multi-step reasoning (if X, then Y, then Z)
- Learn from outcomes

**Example:**
- Agent choosing optimal hotel based on price, location, and preferences
- AI debugging code by reasoning through error causes
- Financial agents evaluating investment opportunities

### 4. ⚡ Act — Execute and Orchestrate

**What it means:**
- Call APIs and use tools autonomously
- Perform actions across multiple systems
- Coordinate complex workflows
- Retry and adapt when things fail

**Example:**
- Claude Code writing files, running tests, committing to Git
- Travel agents booking flights and hotels
- E-commerce agents processing orders and tracking shipments

### 5. 💾 Remember — Maintain Context and Learn

**What it means:**
- Store user preferences and history
- Recall previous interactions
- Build domain knowledge over time
- Adapt behavior based on feedback

**Example:**
- Agent remembering you prefer quiet hotel rooms
- AI assistants referencing previous conversations
- Personal AI learning your communication style

### How the Five Powers Combine

**Individually**, each power is useful but limited.

**Combined**, they create something transformational: **autonomous orchestration**.

**Hotel booking example breakdown:**

1. **Hear**: User speaks request ("Find me a hotel in Chicago")
2. **Reason**: Analyzes requirements (location, timing, context)
3. **Remember**: Recalls user prefers quiet rooms, king beds, downtown proximity
4. **Act**: Searches hotels, compares options, filters by criteria
5. **See**: Reads hotel websites, reviews, location maps
6. **Reason**: Evaluates best option considering all factors
7. **Act**: Books room, schedules transportation, updates calendar
8. **Remember**: Stores this interaction to improve future bookings

**The result**: A multi-step workflow orchestrated autonomously, adapting to context and user needs.

---

## Part 3: The Modern AI Stack

The Five Powers explain *what* agents can do. The Modern AI Stack explains *how* they're built. This three-layer architecture represents a fundamental shift from 2024 to 2025: from monolithic tool silos to modular, composable components.

Think of it like a construction project: you need foundation materials (Layer 1), a safe working platform (Layer 2), and skilled workers executing the work (Layer 3).

### Layer 1: Frontier Models—The Reasoning Engines

At the foundation are frontier models—the large language models that power everything above them. These are the brains of the system.

**What Frontier Models Provide:**
- Understanding and generation of text, code, and reasoning
- Chain-of-thought problem solving
- Context-aware adaptation
- Multimodal capabilities (text, images, audio, video)

**Current Frontier Models:**
- **Claude Opus 4.5** (Anthropic) — Extended reasoning, constitutional AI alignment, nuanced understanding
- **GPT-5** (OpenAI) — Advanced reasoning, strong code generation, multimodal capabilities
- **Gemini 2.5** (Google) — Multimodal, competitive programming excellence, integrated with Google services

**The Capability Characteristic:** What distinguishes a frontier model isn't just size—it's reasoning capability. Think of Layer 1 as the difference between hiring someone who can follow simple instructions versus hiring someone who can understand intent and adapt solutions independently.

### Layer 2: AI-First IDEs—The Development Environment

Above the models sits the development environment layer—the tools you use to interact with AI while building software. These aren't traditional IDEs. They're environments designed from the ground up for AI collaboration.

**What AI-First IDEs Provide:**
- Deep integration of models into editing experience
- Context awareness of entire codebase
- Natural conversation while editing
- Rapid feedback loops (ask → edit → see results → refine)

**Current AI-First IDEs:**
- **VS Code** (Microsoft) — Traditional editor with deep Copilot integration; most widely used
- **Cursor** (Anystic) — Purpose-built for AI-assisted development; treats codebase as context
- **Windsurf** (Codeium) — Agentic IDE with multifile understanding
- **Zed** (Zed Industries) — Modern editor with first-class AI collaboration

**The IDE's Role:** In 2024, developers switched constantly between editor, terminal, and ChatGPT. In 2025, modern IDEs integrate these experiences. The model is part of your editing environment, not an external service.

### Layer 3: General and Coding Agents—The Autonomous Workers

The top layer consists of general and coding agents—specialized systems that can autonomously handle significant portions of the development workflow.

**What General Agents Provide:**
- Tool access (filesystem, terminal, APIs)
- Autonomous orchestration of multi-step workflows
- Self-testing and error correction
- Specification-to-code transformation

**The Agent Difference:** A model can generate code. An agent can:
1. Read your codebase (access tools)
2. Understand the structure (reasoning)
3. Generate implementations (models)
4. Test the code (access tools)
5. Debug failures (reasoning loop)
6. Iterate until working (autonomous loop)

Agents are orchestrators. They coordinate between models, development environments, testing systems, and deployment pipelines.

### Model Context Protocol: The USB for AI Tools

Everything in this stack only works smoothly if the layers can communicate effectively. That's where **Model Context Protocol (MCP)** comes in.

**What MCP Is:**
MCP is a universal standard that allows AI systems to connect to data sources, services, and tools without vendor lock-in. Think of it as "USB for AI"—a standardized connector that works with any compatible system.

**Why MCP Matters:**

**Before MCP (2024 tool silos)**:
- Claude had access to specific data sources
- ChatGPT couldn't reach your company's databases
- GitHub Copilot only worked with code repositories
- Each tool required custom integration by the vendor

**After MCP (2025 modular stack)**:
- Any agent can connect to any data source via MCP
- Your databases, APIs, and services work with any LLM
- Developers compose tools instead of choosing monolithic platforms
- No vendor lock-in—switch models without abandoning tool integrations

**Practical Example:**

Imagine you're building an application that needs to access your company's Postgres database and call internal APIs.

*In the old model:*
1. You'd hope Claude had Postgres integration (it doesn't natively)
2. You'd write custom code to connect Claude to your database
3. You'd be locked into Claude for that workflow

*With MCP:*
1. Your database exposes an MCP server
2. Any agent (Claude, Gemini, GPT, or future models) connects via MCP
3. You can switch models without changing integrations

MCP prevents the lock-in that plagued earlier AI tool ecosystems.

---

## Part 4: The Evolution—Why Now?

Understanding where we are helps explain why the UX→Intent shift is happening now.

AI evolved through three phases:

### Phase 1: Predictive AI

**What it did**: Analyzed historical data to forecast outcomes

**Limitation**: Could only predict, not create or act

**Example**: Netflix recommending movies based on watch history

### Phase 2: Generative AI

**What it does**: Creates new content from patterns

**Limitation**: Generates when prompted, but doesn't take action

**Example**: ChatGPT writing essays, code, or creative content when you ask

### Phase 3: Agentic AI

**What it does**: Takes autonomous action to achieve goals

**Breakthrough**: AI shifts from tool to teammate—from responding to orchestrating

**Example**: Claude Code editing files, running tests, committing changes *without asking for each step*

**The key difference**: Earlier AI waited for commands. Agentic AI initiates, coordinates, and completes workflows autonomously.

This evolution unlocked the Five Powers working together, making the UX→Intent paradigm shift possible.

---

## Part 5: The 2024 vs 2025 Shift—From Silos to Composition

This is the crucial evolution happening right now:

### 2024: Tool Silos (Monolithic)

Each vendor bundled everything:
- Model + IDE + Agent = One package
- Switching models meant relearning the IDE
- Custom integrations only worked with one platform
- Vendor lock-in was inevitable

### 2025: Modular Stack (Composable)

Layers are independent:
- Pick your model (Claude, GPT, Gemini)
- Pick your IDE (Cursor, VS Code, Zed)
- Pick your agent (Claude Code, Aider, Devin)
- Connect them via MCP for data access

**Why this matters**: Competition drives innovation. When tools are modular, each layer improves independently. The best models compete with each other. The best IDEs compete with each other. You benefit from this competition.

---

## Part 6: Why This Shift Matters

The design challenge shifts from *"How do we make this interface intuitive?"* to *"How do we make this agent understand intent accurately?"*

### The Skill Shift

**What mattered in the Interface era:**
- UI/UX design (visual hierarchy, information architecture)
- Frontend frameworks (React, Vue, Angular)
- Form validation and input handling
- CSS and responsive design
- Click-through testing

**What matters in the Intent era:**
- **Intent modeling** (understanding user goals from natural language)
- **Context management** (memory, personalization, preferences)
- **Agent orchestration** (coordinating multi-step workflows)
- **Specification writing** (clear, testable intent descriptions)
- **Evaluation design** (how do you test "understanding"?)
- **Behavioral testing** (does agent respond appropriately to variations?)

**The skill that matters most**: Clear specification writing.

But the nature of specs changes:
- **Before**: "When user clicks button X, do Y"
- **Now**: "When user expresses intent Z (in any phrasing), agent understands and acts appropriately"

---

## Try With AI

Use your AI companion (Claude Code, ChatGPT, Gemini CLI) to explore these concepts:

### Exercise 1: Reimagine a Workflow as Agentic

**Prompt:**
```
I want to reimagine a manual workflow as agentic. Here's what I currently do [describe
a multi-step task you do regularly, like expense reporting, email management, project
planning, scheduling, research compilation, etc.].

Help me reimagine this as an agentic experience:
1. What would I say to an agent to express my intent?
2. What would the agent need to understand about my preferences?
3. What actions would it take autonomously?
4. Which of the Five Powers (See, Hear, Reason, Act, Remember) would it use for each action?
5. What would the agent need to remember for next time?

Let's discover together: What makes this agentic vs. just automated?
```

**What you're learning:** Intent modeling—thinking in goals and context rather than steps and clicks, plus mapping agentic capabilities to the Five Powers framework.

### Exercise 2: Identify the Five Powers in Real Systems

**Prompt:**
```
Let's analyze a real agentic system (like Claude Code, a travel booking agent, or
customer service AI). For the system we choose, help me identify concrete examples of
each power:

1. SEE: How does it process visual information?
2. HEAR: How does it understand natural language input?
3. REASON: What decisions does it make autonomously?
4. ACT: What actions can it take across systems?
5. REMEMBER: What context does it maintain?

Then let's discover: How do these five powers COMBINE to enable orchestration? What
would break if one power was missing?

Now map this system to the three-layer AI stack:
- Which frontier model powers it (Layer 1)?
- What environment does it run in (Layer 2)?
- Is it a general agent or a custom agent (Layer 3)?
```

**What you're learning:** System analysis—understanding how capabilities combine to create emergent behavior, and connecting capabilities to the technical infrastructure that enables them.

### Exercise 3: Map Your Current Tools to the Stack

**Prompt:**
```
I want to understand the modern AI stack better. Here's what I currently use:
- [IDE you use: VS Code, Cursor, etc.]
- [AI model: Claude, ChatGPT, Gemini, etc.]
- [Any agents or automation: GitHub Actions, custom scripts, etc.]

Help me map these to the three-layer stack:
- Layer 1: Which frontier models do I use?
- Layer 2: Which AI-first IDEs do I work in?
- Layer 3: Which development agents or automation tools do I use?

Then identify:
1. What gaps exist in my current stack?
2. Where could MCP help me connect tools that don't currently integrate?
3. If I wanted to switch models (e.g., Claude → GPT-5), what would I need to change?

Give me concrete recommendations for improving my stack composition.
```

**What you're learning:** Recognizing how real tools compose into the three-layer architecture, identifying which layers you already use, and understanding how modularity enables flexibility and prevents vendor lock-in.
