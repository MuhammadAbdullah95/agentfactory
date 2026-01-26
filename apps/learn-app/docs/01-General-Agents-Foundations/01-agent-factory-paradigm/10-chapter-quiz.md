---
sidebar_position: 10
title: "Chapter 1: The AI Agent Factory Paradigm Quiz"
proficiency_level: A2
layer: 1
estimated_time: "45 mins"
chapter_type: Concept
running_example_id: agent-factory-paradigm-quiz
---

# Chapter 1: The AI Agent Factory Paradigm Quiz

Test your understanding of the foundational concepts that define AI-Driven Development and the Digital FTE vision. This assessment covers all 9 lessons in Chapter 1.

<Quiz
  title="Chapter 1: The AI Agent Factory Paradigm Assessment"
  questions={[
    {
      question: "Which of the following is concrete evidence that AI coding capability reached production quality in 2024-2025?",
      options: ["ChatGPT became more popular than other AI tools", "More blog posts were written about AI development", "OpenAI achieved a perfect score solving all 12 problems at the ICPC World Finals", "AI companies received more venture capital funding"],
      correctOption: 2,
      explanation: "The ICPC World Finals breakthrough in 2025 demonstrated that AI can solve complex algorithmic problems at the highest competitive level—concrete evidence of production-quality capability, not just popularity or funding metrics.",
      source: "Lesson 1: The 2025 Inflection Point"
    },
    {
      question: "According to the 2025 Stack Overflow Developer Survey, what percentage of professional developers use or plan to use AI coding tools?",
      options: ["51%", "66%", "84%", "95%"],
      correctOption: 2,
      explanation: "84% of developers are using or plan to use AI tools, with 51% using them daily. This mainstream adoption indicates AI tools have crossed from experimental to standard practice.",
      source: "Lesson 1: The 2025 Inflection Point"
    },
    {
      question: "In the Agent Maturity Model, what is the primary purpose of the Incubator stage (General Agents)?",
      options: ["Production deployment at scale", "Exploration, discovery, and prototyping", "Cost optimization and efficiency", "Governance and compliance"],
      correctOption: 1,
      explanation: "The Incubator stage uses General Agents like Claude Code for exploration, discovery, and prototyping. It's optimized for flexibility and reasoning, not production scale. Custom Agents (Specialist stage) handle production workloads.",
      source: "Lesson 1: The 2025 Inflection Point"
    },
    {
      question: "When should you use General Agents according to the Agent Factory paradigm?",
      options: ["When you need consistent behavior for thousands of runs", "When you're not sure what the solution should look like", "When cost and latency are the primary concerns", "When you need to enforce specific constraints"],
      correctOption: 1,
      explanation: "General Agents are ideal when requirements are unclear, keep changing, or you're doing something novel. Custom Agents are for when you can precisely define behavior and need reliability at scale.",
      source: "Lesson 1: The 2025 Inflection Point"
    },
    {
      question: "What is 'Premature Specialization' in the Agent Factory paradigm?",
      options: ["Using custom agents without building general agents first", "Building custom agents before requirements stabilize through exploration", "Training AI models too early in development", "Deploying agents to production without testing"],
      correctOption: 1,
      explanation: "Premature Specialization means trying to build custom agents before exploring the problem space with general agents. This leads to rigid solutions that don't match actual needs.",
      source: "Lesson 1: The 2025 Inflection Point"
    },
    {
      question: "What is the core reality behind the 'illusion of memory' in LLMs?",
      options: ["LLMs have perfect memory but pretend not to", "The application stores history and re-sends it; the model reads fresh each time then forgets", "LLMs remember the last 10 conversations automatically", "Memory is stored in the model weights and persists forever"],
      correctOption: 1,
      explanation: "The application (not the model) stores conversation history. Every API call sends the entire history, which the model reads fresh—then immediately forgets. Session continuity is an application feature, not a model capability.",
      source: "Lesson 2: Three Core LLM Constraints"
    },
    {
      question: "When a developer says 'It remembers my coding style,' what's actually happening?",
      options: ["The model learned their style from training data", "The model has no past-session memory; they should use style guides in AGENTS.md", "The model stores preferences in a personal database", "The model's weights were updated with their preferences"],
      correctOption: 1,
      explanation: "LLMs have no memory between sessions. What appears as 'remembering' is actually the application re-injecting context. To preserve style preferences, encode them in persistent files like AGENTS.md.",
      source: "Lesson 2: Three Core LLM Constraints"
    },
    {
      question: "Why is LLM output probabilistic rather than deterministic?",
      options: ["Models are designed to be unpredictable for security", "Models sample from probability distributions, producing different outputs from identical inputs", "Servers introduce random noise to prevent copying", "Each API call uses a different model version"],
      correctOption: 1,
      explanation: "LLMs sample from probability distributions. Even with temperature=0, subtle variations can occur. This means you cannot expect identical code from identical prompts—validation becomes essential.",
      source: "Lesson 2: Three Core LLM Constraints"
    },
    {
      question: "What is the practical implication of probabilistic LLM outputs for software development?",
      options: ["Always use the same prompt for consistent results", "Validation and testing become essential since outputs vary", "Avoid using LLMs for any critical code", "Only use temperature=0 for all tasks"],
      correctOption: 1,
      explanation: "Because outputs vary, validation becomes essential—not optional. Specifications constrain the valid output space, and Test-Driven Development verifies invariants regardless of implementation variation.",
      source: "Lesson 2: Three Core LLM Constraints"
    },
    {
      question: "What happens when an LLM's context window fills up during a long conversation?",
      options: ["The model compresses old information automatically", "Early messages get truncated, losing information", "The model requests more memory from the server", "The conversation quality improves due to more data"],
      correctOption: 1,
      explanation: "When context fills up, early messages are truncated and information is lost. This is why context engineering is a core skill—you must strategically manage what goes into the context window.",
      source: "Lesson 2: Three Core LLM Constraints"
    },
    {
      question: "Which approach helps manage the 'context is limited' constraint in LLMs?",
      options: ["Paste entire codebases into every prompt", "Reference file paths rather than paste entire contents", "Use the longest possible system prompts", "Include all previous conversation history"],
      correctOption: 1,
      explanation: "Context is zero-sum—every token for history is a token not available for code or response. Reference paths rather than pasting contents, maintain PROJECT_CONTEXT.md for state, and start fresh conversations for new topics.",
      source: "Lesson 2: Three Core LLM Constraints"
    },
    {
      question: "What is the most fundamental change in the developer role in the AI era?",
      options: ["Learning new programming syntax", "Mastering additional frameworks and libraries", "Shifting from implementation (typing code) to orchestration (directing AI systems)", "Understanding cloud computing and DevOps better"],
      correctOption: 2,
      explanation: "The core shift is from typist to orchestrator. Your value is no longer in how fast you can type, but in the quality of your ideas and directions. The 10% humans contribute—problem understanding, decisions, quality judgments—becomes infinitely more valuable.",
      source: "Lesson 3: From Coder to Orchestrator"
    },
    {
      question: "What is the OODA loop?",
      options: ["A method for debugging code faster than traditional approaches", "A reasoning framework with Observe, Orient, Decide, Act—used by AI agents to process information and take action", "A programming design pattern for asynchronous operations", "An acronym for four programming languages"],
      correctOption: 1,
      explanation: "OODA (Observe, Orient, Decide, Act) is a reasoning framework from military strategy that describes how AI agents process information and take action. Agentic AI cycles through OODA continuously until goals are achieved.",
      source: "Lesson 3: From Coder to Orchestrator"
    },
    {
      question: "What distinguishes Generation 4 AI tools from Generation 3?",
      options: ["Gen 4 uses larger language models", "Gen 4 agents execute autonomously with multi-turn capability; Gen 3 required step-by-step approval", "Gen 4 is only available to enterprise users", "Gen 4 focuses on code completion while Gen 3 handles full features"],
      correctOption: 1,
      explanation: "Generation 4 (Claude Code, Gemini CLI) agents work autonomously—reading code, running tests, making commits—without requiring step-by-step human approval. The bottleneck shifts from typing speed to human review speed.",
      source: "Lesson 3: From Coder to Orchestrator"
    },
    {
      question: "In the AI-transformed SDLC, what does the developer's role become during the Coding phase?",
      options: ["Type all code manually for quality control", "Validate AI-generated code against specifications and security requirements", "Debug code written by other team members", "Write documentation for the codebase"],
      correctOption: 1,
      explanation: "AI generates 80-90% of routine code. The developer's role shifts to validation: Does this match the spec? Are there security issues? Would an architect approve this approach?",
      source: "Lesson 3: From Coder to Orchestrator"
    },
    {
      question: "Which tasks do orchestrators focus on rather than typists?",
      options: ["Writing boilerplate code and configuration files", "Implementing database queries and API endpoints", "Specification writing, requirement gathering, and validation of AI-generated work", "Remembering programming language syntax without references"],
      correctOption: 2,
      explanation: "Orchestrators focus on the judgment work: writing clear specifications, gathering requirements, designing architecture, and validating AI output. AI handles the mechanical implementation.",
      source: "Lesson 3: From Coder to Orchestrator"
    },
    {
      question: "What are the Five Powers that enable autonomous agents?",
      options: ["Five programming languages you must master", "Five cloud providers for deploying AI systems", "See, Hear, Reason, Act, Remember—five capabilities that combine for autonomous orchestration", "Five types of machine learning models used in production"],
      correctOption: 2,
      explanation: "The Five Powers are: See (visual understanding), Hear (audio processing), Reason (complex decision-making), Act (execute and orchestrate), Remember (maintain context and learn). Combined, they enable autonomous orchestration.",
      source: "Lesson 4: Five Powers and the Modern AI Stack"
    },
    {
      question: "In the Modern AI Stack, what role do AI-First IDEs (Layer 2) play?",
      options: ["They train the AI models on code patterns", "They act as context orchestrators, intelligently selecting relevant code for models", "They replace the need for frontier models entirely", "They only provide syntax highlighting and autocomplete"],
      correctOption: 1,
      explanation: "AI-First IDEs like Cursor and Windsurf are context orchestrators. They intelligently select relevant code, host skills, and create the environment where models, tools, and files meet—solving the context management problem.",
      source: "Lesson 4: Five Powers and the Modern AI Stack"
    },
    {
      question: "What is the primary advantage of a modular, three-layer AI stack compared to monolithic tool ecosystems?",
      options: ["It requires less training for developers to use", "It guarantees all tools are free and open-source", "It prevents vendor lock-in and enables faster evolution by composing independent layers", "It eliminates the need for AI models entirely"],
      correctOption: 2,
      explanation: "The modular stack (Frontier Models → AI-First IDEs → Agent Skills) prevents vendor lock-in. You can swap models via API, choose best-of-breed at each layer, and evolve your stack independently.",
      source: "Lesson 4: Five Powers and the Modern AI Stack"
    },
    {
      question: "How does MCP (Model Context Protocol) function as the 'USB cable for AI'?",
      options: ["It physically connects AI hardware to computers", "It provides a standardized protocol so any MCP-compatible agent can use any MCP server", "It compresses data for faster transmission", "It only works with Anthropic's Claude models"],
      correctOption: 1,
      explanation: "MCP standardizes agent-to-tool connections. Instead of M agents × N tools = M×N custom integrations, MCP provides one protocol for all. Any MCP-compatible agent (Claude, ChatGPT, Gemini, custom) can use any MCP server.",
      source: "Lesson 4: Five Powers and the Modern AI Stack"
    },
    {
      question: "What is the primary business benefit of AAIF (Agentic AI Foundation) for building Digital FTEs?",
      options: ["It provides free hosting for AI agents", "It ensures your Digital FTEs are portable investments that work across platforms, not locked to a single vendor", "It automatically generates code for your agents", "It provides AI models at discounted prices"],
      correctOption: 1,
      explanation: "AAIF provides neutral governance for open standards (MCP, AGENTS.md, goose), ensuring your Digital FTEs can connect to any CRM, work with any AI platform, and adapt to any client's workflow—without custom integration per platform.",
      source: "Lesson 5: AIFF Standards Foundation"
    },
    {
      question: "In MCP's three primitives, what is the difference between Resources and Tools?",
      options: ["Resources are free; Tools require payment", "Resources provide data to read (agent's 'eyes'); Tools execute actions (agent's 'hands')", "Resources work locally; Tools work remotely", "Resources are for developers; Tools are for end users"],
      correctOption: 1,
      explanation: "Resources are what your Digital FTE can see—lead data from CRM, email history, company information. Tools are what your Digital FTE can do—create records, send emails, schedule meetings. Resources read; Tools act.",
      source: "Lesson 5: AIFF Standards Foundation"
    },
    {
      question: "What is the key business advantage of AGENTS.md for selling Digital FTEs to multiple clients?",
      options: ["It reduces the AI model cost per query", "It enables zero-config deployments—same Digital FTE adapts to each client's environment automatically", "It encrypts all communications between agent and client", "It provides automatic scaling for high-traffic applications"],
      correctOption: 1,
      explanation: "AGENTS.md is README for AI agents. Your Digital FTE reads each client's AGENTS.md to understand their coding conventions, build commands, and security requirements—deploying to 100 different organizations without customization.",
      source: "Lesson 5: AIFF Standards Foundation"
    },
    {
      question: "What is the key difference between MCP and Agent Skills?",
      options: ["MCP is open source; Skills are proprietary", "MCP provides connectivity (how agents talk to tools); Skills provide expertise (what agents know how to do)", "MCP is for reading; Skills are for writing", "MCP works with Claude; Skills work with ChatGPT"],
      correctOption: 1,
      explanation: "MCP and Skills are complementary, not competing. MCP connects to tools (agent's hands); Skills encode expertise (agent's training). For Stripe payments: MCP Server connects to Stripe API, while a Skill knows payment best practices.",
      source: "Lesson 5: AIFF Standards Foundation"
    },
    {
      question: "What is 'Progressive Disclosure' in the Agent Skills standard?",
      options: ["Gradually revealing features to users over time", "Loading only skill metadata at startup (~100 tokens), full instructions when activated (<5k), resources on-demand", "Teaching skills in order from simple to complex", "Hiding advanced features from beginner users"],
      correctOption: 1,
      explanation: "Progressive Disclosure reduces token usage by 80-98%. At startup, agents see only name and description (~100 tokens per skill). Full SKILL.md loads when activated (<5k tokens). Supporting resources load only when actually needed.",
      source: "Lesson 5: AIFF Standards Foundation"
    },
    {
      question: "What distinguishes goose from Claude Code?",
      options: ["goose is more powerful than Claude Code", "goose is open-source (Apache 2.0) with visible source code; Claude Code is proprietary", "Claude Code only works offline; goose requires internet", "goose was created by OpenAI; Claude Code by Anthropic"],
      correctOption: 1,
      explanation: "goose (from Block) is open-source under Apache 2.0—you can study its architecture, adapt patterns, and understand production agent implementation. Claude Code is proprietary. Use Claude Code for productivity today; study goose for building Custom Agents tomorrow.",
      source: "Lesson 5: AIFF Standards Foundation"
    },
    {
      question: "What is a Digital FTE?",
      options: ["A part-time AI assistant for coding", "An autonomous AI agent executing the COMPLETE output of a human employee, focused on outcomes not tasks", "A chatbot that answers questions about software", "A tool that increases developer productivity by 20%"],
      correctOption: 1,
      explanation: "FTE = Full-Time Equivalent. A Digital FTE is an autonomous AI agent that executes complete human employee output. Unlike tools (which require operators), Digital FTEs replace the need for operators by focusing on OUTCOMES, not individual tasks.",
      source: "Lesson 6: Digital FTE Business Strategy"
    },
    {
      question: "In the 'Productivity Trap vs Ownership Model' story, why did Sarah get displaced while Marcus succeeded?",
      options: ["Marcus had more technical skills", "Sarah used AI for productivity; Marcus built a Digital FTE encoding his expertise as a product he owns", "Marcus worked in a better industry", "Sarah didn't use AI tools effectively"],
      correctOption: 1,
      explanation: "Sarah positioned AI as a productivity tool—when a cheaper Digital FTE launched, it directly competed with her labor. Marcus positioned his expertise as a product that AI delivers—he owns the Digital FTE that competes with his own labor.",
      source: "Lesson 6: Digital FTE Business Strategy"
    },
    {
      question: "What is 'The Moat' in Digital FTE positioning?",
      options: ["A water feature around data centers", "The 20% of nuanced, experience-based insights that generic AI cannot replicate", "A legal protection for AI intellectual property", "The amount of compute power needed to run agents"],
      correctOption: 1,
      explanation: "The 80/20 split: 80% is commodity (structure, grammar, basic facts—AI excels at this). 20% is the moat—nuance, edge cases, political context, 'gut check' based on years of experience. Your ability to filter, correct, and elevate AI output IS the moat.",
      source: "Lesson 6: Digital FTE Business Strategy"
    },
    {
      question: "In the 'Snakes and Ladders' framework, which layer should third-party developers avoid competing in?",
      options: ["Layer 1: Consumer AI Backbone (OpenAI vs Google war)", "Layer 2: General Agents as Developer Tools", "Layer 3: Custom Agents for Vertical Markets", "Layer 4: Orchestrator Layer"],
      correctOption: 0,
      explanation: "Layer 1 is a brutal two-player game where only OpenAI and Google survive (billions in data, compute, marketing). Don't compete here—avoid the snake. Instead, climb the ladder at Layer 2 (developer tools) or Layer 3 (vertical markets).",
      source: "Lesson 6: Digital FTE Business Strategy"
    },
    {
      question: "What is the economic advantage of Digital FTE labor over human labor for customer support?",
      options: ["Digital FTEs provide better emotional support", "Digital FTEs cost ~$3/ticket vs ~$150/ticket for humans, with 24/7 availability", "Digital FTEs require no infrastructure costs", "Digital FTEs are only useful for simple queries"],
      correctOption: 1,
      explanation: "Human agent: $6k/month, 40 hrs/week, 20 tickets/day = $150/ticket. Digital FTE: $1.5k/month, 168 hrs/week, 500+ tickets/day = $3/ticket. Digital FTE is ~50x more cost-efficient with 24/7 availability.",
      source: "Lesson 6: Digital FTE Business Strategy"
    },
    {
      question: "When would a 'Success Fee' model be better than 'Subscription' for Digital FTE pricing?",
      options: ["When clients want predictable monthly costs", "When outcomes are easily measurable and clients are skeptical ('prove it first')", "When you want recurring passive income", "When clients need 24/7 support coverage"],
      correctOption: 1,
      explanation: "Success Fee (commission on measured outcomes) works when: outcomes are easy to measure, clients are skeptical and want proof first, and you're confident the solution works. Subscription works better for predictable costs and hands-off automation.",
      source: "Lesson 6: Digital FTE Business Strategy"
    },
    {
      question: "What is the 'Shadow Mode' deployment strategy for high-risk domains?",
      options: ["Running the agent only at night when usage is low", "Agent runs and generates recommendations while humans make all final decisions, logging everything for comparison", "Deploying to shadow servers before production", "Hiding the AI from end users"],
      correctOption: 1,
      explanation: "Shadow Mode (Weeks 1-4): Agent runs, generates recommendations, but humans make all final decisions. Log all outputs and decisions. Measure: Does agent agree with humans 80%+? This validates accuracy before any autonomous operation.",
      source: "Lesson 6: Digital FTE Business Strategy"
    },
    {
      question: "Which scenario represents a valid use case for autonomous AI agents?",
      options: ["AI sending legal opinions directly to clients without attorney review", "AI recommending actions while humans approve before execution", "AI executing financial transactions without authorization", "AI screening resumes and forwarding only 'qualified' candidates without human review"],
      correctOption: 1,
      explanation: "Agent should RECOMMEND; human should APPROVE. Legal decisions, medical recommendations, financial transactions, and hiring decisions all require human oversight due to liability, regulatory, and ethical requirements.",
      source: "Lesson 6: Digital FTE Business Strategy"
    },
    {
      question: "What defines AI-Driven Development (AIDD)?",
      options: ["Using AI to write all code without human involvement", "A specification-first methodology transforming developers into specification engineers and architects", "Replacing developers entirely with AI systems", "Using AI only for testing and debugging"],
      correctOption: 1,
      explanation: "AIDD is a specification-first methodology where agents handle implementation while developers focus on architecture and validation. It has nine core characteristics including specification-driven, AI-augmented, quality-gated, and human-verified.",
      source: "Lesson 7: Nine Pillars of AIDD"
    },
    {
      question: "Why does 'Markdown as Programming Language' (Pillar 2) enable new development patterns?",
      options: ["Markdown is faster to parse than other languages", "Markdown specs become executable 'source code' that AI agents read and implement", "Markdown replaces all programming languages", "Markdown is only used for documentation"],
      correctOption: 1,
      explanation: "Markdown specifications become the human-readable 'source code' that AI agents implement. This removes the massive cognitive load of translating ideas into rigid syntax—you express intent, AI handles implementation details.",
      source: "Lesson 7: Nine Pillars of AIDD"
    },
    {
      question: "What is an 'M-Shaped Developer' and why was it nearly impossible before AI?",
      options: ["A developer who works on Monday through Friday", "A developer with deep expertise in 2-4 complementary domains, enabled by AI handling cognitive load across areas", "A developer who only writes mobile applications", "A developer who manages multiple teams"],
      correctOption: 1,
      explanation: "M-Shaped developers have deep expertise in 2-4 complementary domains (e.g., full-stack + DevOps + ML). Before AI, mastering multiple domains required overwhelming cognitive load and hours that weren't available. The nine pillars remove these barriers.",
      source: "Lesson 7: Nine Pillars of AIDD"
    },
    {
      question: "Why is partial adoption of AIDD pillars (e.g., 6 of 9) less effective than complete adoption?",
      options: ["The pillars are designed to only work together", "Partial adoption creates gaps; pillars multiply effects exponentially when combined, not just add linearly", "Some pillars are more important than others", "Partial adoption costs more than complete adoption"],
      correctOption: 1,
      explanation: "Individual tools add value linearly (10-20% gains). Nine pillars working together multiply effects exponentially. Without complete adoption, bottlenecks remain. Example: Skills (Pillar 8) depend on MCP (Pillar 3), SDD (Pillar 7), and Markdown (Pillar 2).",
      source: "Lesson 7: Nine Pillars of AIDD"
    },
    {
      question: "What is the core equation of Spec-Driven Development?",
      options: ["More code = better results", "Vague Idea + AI = 5+ iterations; Clear Specification + AI = 1-2 iterations", "Faster coding = higher quality", "Documentation = specification"],
      correctOption: 1,
      explanation: "The bottleneck has shifted to specification. With clear specs, AI implements in 1-2 refinement cycles. With vague ideas, you spend 5+ iterations on misalignment. SDD front-loads the thinking work for faster, more accurate results.",
      source: "Lesson 8: Spec-Driven Development"
    },
    {
      question: "What are the four elements of a complete specification in SDD?",
      options: ["Code, Tests, Documentation, Deployment", "Intent, Success Criteria, Constraints, Non-Goals", "Frontend, Backend, Database, API", "Planning, Coding, Testing, Releasing"],
      correctOption: 1,
      explanation: "A complete specification includes: Intent (why does this exist?), Success Criteria (what does correct look like?), Constraints (what limits exist?), and Non-Goals (what are we explicitly NOT building?). Non-Goals prevent scope creep.",
      source: "Lesson 8: Spec-Driven Development"
    },
    {
      question: "What are the six phases of the SDD workflow?",
      options: ["Plan, Code, Test, Deploy, Monitor, Maintain", "Specify, Clarify, Plan, Tasks, Implement, Validate", "Gather, Analyze, Design, Build, Review, Release", "Discovery, Definition, Design, Development, Delivery, Deployment"],
      correctOption: 1,
      explanation: "The SDD workflow: Specify (define what), Clarify (remove ambiguity), Plan (design how), Tasks (break down work), Implement (AI executes), Validate (verify quality). Each phase has a quality gate before proceeding.",
      source: "Lesson 8: Spec-Driven Development"
    },
    {
      question: "When is 'Vibe Coding' appropriate vs when is SDD essential?",
      options: ["Vibe coding is always better because it's faster", "Vibe coding works for learning/throwaway code; SDD is essential for production features, security-critical, or AI-assisted development", "SDD is only for large teams, vibe coding for solo developers", "Both approaches produce identical results"],
      correctOption: 1,
      explanation: "Vibe coding works for learning experiments, throwaway prototypes, and simple scripts (<50 lines). SDD is essential when there's business impact, complexity, security/compliance requirements, multiple developers, or AI assistance.",
      source: "Lesson 8: Spec-Driven Development"
    },
    {
      question: "Why does 'AI amplifies your habits' matter for development methodology?",
      options: ["AI makes all development approaches equally effective", "Vibe coding with AI leads to faster, more reliable software", "Spec-driven development becomes MORE critical because AI amplifies both good discipline and bad habits", "AI eliminates the need for any development methodology"],
      correctOption: 2,
      explanation: "AI generates code instantly but won't write specs you didn't ask for or tests you didn't request. Vibe Coding + AI = Amplified Chaos. Spec-Driven + AI = Amplified Excellence. The discipline becomes more critical, not less.",
      source: "Lesson 8: Spec-Driven Development"
    },
    {
      question: "What distinguishes a Digital FTE from a 'tool' in the AI era?",
      options: ["Digital FTEs are more expensive", "Tools wait for prompts; Digital FTEs monitor domains, identify needs, and execute solutions with 24/7 autonomous operation", "Digital FTEs only work for enterprise clients", "Tools are AI-powered; Digital FTEs are not"],
      correctOption: 1,
      explanation: "The FTE threshold isn't just what an agent CAN do, but HOW it exists. Tools wait for prompts. Digital FTEs monitor their domain, identify needs, and execute solutions with the reliability and persistence of a human team member—24/7 autonomous operation.",
      source: "Lesson 9: Synthesis - The Digital FTE Vision"
    },
    {
      question: "What does 'AI is an amplifier' mean for the choice between Vibe Coding and SDD?",
      options: ["AI makes both approaches equally valid", "AI amplifies good habits (SDD) AND bad habits (Vibe Coding)—discipline matters MORE with AI, not less", "AI eliminates the difference between approaches", "AI only amplifies positive outcomes"],
      correctOption: 1,
      explanation: "AI is an amplifier—it amplifies whatever direction you're heading. Clear specifications lead to excellent results fast. Vague requirements lead to terrible results fast. This is why SDD matters MORE in the AI era, not less.",
      source: "Lesson 9: Synthesis - The Digital FTE Vision"
    },
    {
      question: "What creates the 'virtuous cycle' in the Agent Factory paradigm?",
      options: ["Using more expensive AI models", "Clear specs → precise execution → reliable agents → Digital FTEs → multiplied capacity → larger problems → even better specs", "Hiring more developers to review AI output", "Focusing only on one type of agent"],
      correctOption: 1,
      explanation: "Everything compounds: clear specs lead to precise AI execution, which enables reliable Custom Agents, which become Digital FTEs, which multiply capacity for larger problems, which require even better specs. The gap widens with each AI generation.",
      source: "Lesson 9: Synthesis - The Digital FTE Vision"
    },
    {
      question: "According to Chapter 1, what is the fundamental choice developers face?",
      options: ["Which programming language to learn", "Whether to use open-source or proprietary tools", "Path A (treat AI as faster keyboard, vibe code) vs Path B (master Agent Factory paradigm, build Digital FTEs)", "Whether to work remotely or in an office"],
      correctOption: 2,
      explanation: "Path A: Treat AI as a faster keyboard, vibe code, watch technical debt compound while competitors build systematic capabilities. Path B: Master the Agent Factory paradigm, clear specifications, build Digital FTEs, multiply capacity systematically. This book teaches Path B.",
      source: "Lesson 9: Synthesis - The Digital FTE Vision"
    }
  ]}
/>
