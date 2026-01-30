---
sidebar_position: 11
title: "Chapter 4: Context Engineering Quiz"
description: "Test your understanding of context engineering principles, decision frameworks, and practical application"
keywords:
  [
    "context engineering quiz",
    "attention budget",
    "CLAUDE.md optimization",
    "context zones",
    "progress files",
    "memory injection",
    "context isolation",
  ]
chapter: 4
proficiency_level: B1
layer: 2
estimated_time: "45 mins"
chapter_type: Concept
---

# Chapter 4 Quiz: Context Engineering

Test your mastery of context engineering. This quiz covers all skills from the chapter with scenario-based questions that mirror real decision-making.

<Quiz
title="Chapter 4: Context Engineering Assessment"
questionsPerBatch={18}
questions={[
{
question: "You run `/context` and see 'Context: 142,000 / 200,000 tokens (71%)'. What zone are you in and what should you do?",
options: [
"Green zone - work freely without concern",
"Yellow zone - monitor every 10 messages",
"Red zone - emergency compact required immediately",
"Orange zone - run `/compact` NOW before quality degrades"
],
correctOption: 3,
explanation: "At 71%, you've crossed the 70% quality degradation threshold into Orange zone. The correct action is `/compact` NOW, not waiting. Yellow zone (50-70%) means monitoring; Orange (70-85%) means immediate compaction. Waiting risks output quality as the model makes attention tradeoffs. Red zone (>85%) is emergency territory where compaction becomes urgent.",
source: "Lesson 2: The Attention Budget"
},
{
question: "A consultant claims 'I have 200,000 tokens, so I can fit way more context than I need.' Why is this thinking flawed?",
options: [
"The token count includes output tokens, not input",
"Attention follows a U-shaped curve and quality degrades past 70%",
"System prompts are not included in the limit",
"Token counts are approximations varying by 50%"
],
correctOption: 1,
explanation: "Attention follows a U-shaped curve with high attention at beginning and end, but lower in the middle. Quality degrades sharply after 70% utilization because the model must make attention tradeoffs. The 200K limit is theoretical capacity, not practical working space. This is why context engineering treats 70% as the quality ceiling.",
source: "Lesson 2: The Attention Budget"
},
{
question: "Your `/context` shows 47% context (95,000/200,000 tokens). Your next task requires reading 5 large documents (~15,000 tokens each). What should you do?",
options: [
"Read all documents - you have plenty of room",
"Read all documents but `/compact` immediately after reading",
"Run `/clear` first to maximize available space",
"Summarize documents before reading, or read selectively - full reads push past 70%"
],
correctOption: 3,
explanation: "You're at 47%. Adding 75,000 tokens (5 x 15,000) would push you to ~86%, well into Red zone. Summarize or selectively read to stay under 70%. Reading everything then compacting is reactive, not proactive. `/clear` would lose valuable session context unnecessarily. Strategic reading prevents the problem.",
source: "Lesson 2: The Attention Budget"
},
{
question: "Which components make up context in Claude Code, and what are their typical budget percentages?",
options: [
"System prompt (30%), user messages (40%), tool outputs (30%)",
"System prompt (5-10%), CLAUDE.md (5-10%), tools (10-15%), history (30-40%), outputs (20-30%)",
"CLAUDE.md (50%), conversation history (30%), files read (20%)",
"Prompts (10%), documents (60%), documentation (30%)"
],
correctOption: 1,
explanation: "The five components are: System prompt (5-10%), CLAUDE.md (5-10%), tool definitions (10-15%), message history (30-40%), and tool outputs (20-30%). Message history dominates in late sessions. Understanding this distribution is essential for strategic context management-you optimize the components you control (CLAUDE.md, what files you read).",
source: "Lesson 2: The Attention Budget"
},
{
question: "You're auditing your CLAUDE.md and find a 'Standard Tools' section listing common applications and platforms your team uses. Using the 4-question framework, how should you classify this?",
options: [
"SIGNAL - Claude needs to know the tools",
"SIGNAL - Include everything because it's useful reference",
"NOISE - Claude can infer this from project files and existing documents",
"PARTIAL - Keep critical integrations, remove the rest"
],
correctOption: 2,
explanation: "NOISE. Claude can read project configuration files to discover tools, check setup documents for platform settings, and see references in existing work. This section fails the 4-question audit: Q1 (Would Claude ask?) = No, Q2 (In files?) = Yes. Every line of NOISE dilutes the SIGNAL that Claude actually needs.",
source: "Lesson 4: Signal vs Noise"
},
{
question: "Which of the following is SIGNAL according to the 4-question audit?",
options: [
"Use standard formatting for documents",
"Professional communication uses clear language",
"Reports should have executive summaries",
"Client contracts require 48-hour review periods, not the standard 24 hours"
],
correctOption: 3,
explanation: "'Client contracts require 48-hour review periods' is SIGNAL because it differs from the standard (usually 24 hours). Claude couldn't infer this non-obvious constraint from files alone. The other options are standard conventions Claude already knows from training data. SIGNAL = surprises, exceptions, and project-specific constraints.",
source: "Lesson 4: Signal vs Noise"
},
{
question: "Your CLAUDE.md is 247 lines. According to the chapter, what should your target be?",
options: [
"Under 100 lines for good practice",
"Under 60 lines for optimal attention",
"Under 200 lines is acceptable threshold",
"Line count doesn't matter, only content quality"
],
correctOption: 1,
explanation: "Under 60 lines. Best-in-class teams keep CLAUDE.md under 20 lines. With ~50 system prompt instructions and a 150-200 instruction ceiling before Claude's behavior becomes unpredictable, 60 lines keeps you safely under budget while preserving space for session context.",
source: "Lesson 4: Signal vs Noise"
},
{
question: "You have detailed process documentation (50 lines) in your CLAUDE.md. The 4-question audit reveals: Claude wouldn't ask about it, it's in your standard procedures document, and it changes quarterly. What should you do?",
options: [
"Keep it - process documentation is always useful reference",
"Move to a separate docs file and add a reference line in CLAUDE.md",
"Delete entirely - Claude will read the procedures document",
"Compress to 10 lines of essential steps only"
],
correctOption: 1,
explanation: "Move to docs/process-conventions.md and add a reference line. The content fails 3 of 4 questions, making it noise in CLAUDE.md. But it may be useful reference, so progressive disclosure (external file with reference) is better than deletion. This keeps CLAUDE.md focused while preserving access.",
source: "Lesson 4: Signal vs Noise"
},
{
question: "According to the 'Lost in the Middle' research, where does information receive the LOWEST attention in a long context?",
options: [
"The first 10% of the context",
"The last 10% of the context",
"The middle 80% of the context",
"Attention is distributed evenly throughout context"
],
correctOption: 2,
explanation: "The middle 80% receives ~30% less attention than the beginning or end. This is the 'Lost in the Middle' phenomenon documented by Stanford/Berkeley research (Liu et al. 2023). Information placed in the middle has significantly lower recall probability, which is why strategic positioning matters.",
source: "Lesson 3: Lost in the Middle"
},
{
question: "Your critical rule 'Never share draft documents with external parties' is on line 68 of your 200-line CLAUDE.md. Based on position sensitivity, what's the problem?",
options: [
"No problem - line 68 is early enough",
"Critical rules should always be placed last",
"Line count doesn't affect attention distribution",
"The rule is in the middle 80% danger zone where recall drops ~30%"
],
correctOption: 3,
explanation: "Line 68 of 200 lines is in the middle 80% danger zone (lines 21-180). Critical rules need to be in Zone 1 (first 10%) or Zone 3 (last 10%) for reliable recall. The U-shaped attention curve means middle content gets ~30% less attention than edges.",
source: "Lesson 3: Lost in the Middle"
},
{
question: "You're restructuring your CLAUDE.md using the three-zone strategy. Which content belongs in Zone 3 (last 10%)?",
options: [
"Workflow instructions for starting and ending tasks",
"Project structure and folder organization details",
"Tool and platform information",
"Critical constraints and boundaries"
],
correctOption: 0,
explanation: "Workflow instructions ('How to Start Any Task,' 'When You're Done') belong in Zone 3. Zone 3 gets high attention due to recency, making it ideal for instructions Claude should apply to every task. Critical constraints go in Zone 1 (primacy); reference material goes in Zone 2 (middle).",
source: "Lesson 3: Lost in the Middle"
},
{
question: "A colleague ends their CLAUDE.md with 'Feel free to ask if you have any questions!' Why is this problematic?",
options: [
"It's too informal for professional settings",
"Claude can't actually ask questions proactively",
"It should be in Zone 1 instead",
"It wastes Zone 3 prime real estate that should have actionable workflow instructions"
],
correctOption: 3,
explanation: "'Feel free to ask questions' is boilerplate that wastes Zone 3. The end of CLAUDE.md should have actionable workflow instructions that you want Claude to follow on every task. Zone 3 is prime real estate due to recency effects-don't waste it on generic filler.",
source: "Lesson 3: Lost in the Middle"
},
{
question: "You're building a feature that will take 5 sessions over 3 days. What architecture should you use?",
options: [
"Single continuous conversation with `--continue` flag",
"One long session with aggressive compaction strategy",
"Harness architecture with progress files coordinating independent sessions",
"Multiple sessions sharing the same CLAUDE.md file"
],
correctOption: 2,
explanation: "Harness architecture with progress files. Single conversations accumulate context rot after 3-4 days. The progress file coordinates independent sessions, letting each start fresh while maintaining continuity. This prevents the 'dirty slate' problem of accumulated noise.",
source: "Lesson 8: Progress Files"
},
{
question: "Which section is MOST important in a progress file for preventing repeated work?",
options: [
"Session Log tracking when sessions occurred",
"Decisions Made with rationale and alternatives rejected",
"Not Started listing remaining work items",
"Project metadata and configuration settings"
],
correctOption: 1,
explanation: "'Decisions Made' with rationale and rejected alternatives prevents re-debating settled questions. Without it, Session 7 asks 'Should we use approach A or approach B?' when Session 2 already decided. The rationale captures WHY, preventing future sessions from reconsidering closed decisions.",
source: "Lesson 8: Progress Files"
},
{
question: "Your progress file shows: '- [ ] Client proposal (started Session 3)'. What's missing that would help the next session?",
options: [
"The file path where the proposal lives",
"Priority level for the task",
"Progress annotation (e.g., '70% complete - pricing section remaining')",
"Estimated time remaining to complete"
],
correctOption: 2,
explanation: "Progress annotation. 'Started Session 3' doesn't tell the next session what's done vs. remaining. Good format: 'Client proposal (started Session 3, 70% complete - pricing section remaining).' This prevents duplicate work and provides clear handoff state.",
source: "Lesson 8: Progress Files"
},
{
question: "The session exit protocol has two steps. What are they?",
options: [
"Save file, close terminal window",
"Save work at session boundary, update progress file with session summary",
"Run checks, send to repository",
"Compact context, save conversation history"
],
correctOption: 1,
explanation: "(1) Save work at session boundary, (2) Update progress file with session summary. Never end with incomplete work; always document what happened. This ensures the next session inherits stable state and knows what occurred.",
source: "Lesson 8: Progress Files"
},
{
question: "You started a session asking Claude to 'reorganize the project documentation.' By turn 20, Claude is updating unrelated meeting notes. What's happening?",
options: [
"Claude has a reasoning bug in this session",
"The reorganization is complete and Claude moved on",
"Workflow drift - the memories injected at turn 1 are no longer relevant to turn 20's work",
"Context is full and causing confusion"
],
correctOption: 2,
explanation: "Workflow drift. The memories injected at turn 1 (reorganization patterns) are no longer relevant to turn 20's actual work (meeting notes). The prompt-time context doesn't match execution-time needs. This is why PreToolUse injection matters for long workflows.",
source: "Lesson 9: Memory Injection"
},
{
question: "What makes PreToolUse injection better than UserPromptSubmit injection for long workflows?",
options: [
"PreToolUse is faster to execute on each turn",
"UserPromptSubmit doesn't work with semantic search databases",
"PreToolUse uses fewer tokens per injection",
"PreToolUse fires multiple times, using Claude's current thinking to find relevant memories"
],
correctOption: 3,
explanation: "PreToolUse fires before EACH tool call, using Claude's current thinking block to search for relevant memories. UserPromptSubmit only fires once when the user submits, using the original prompt which becomes less relevant as the workflow evolves.",
source: "Lesson 9: Memory Injection"
},
{
question: "A PreToolUse hook extracts the last 1,500 characters of Claude's thinking block. Why use thinking blocks as the query?",
options: [
"Thinking blocks are easier to parse than messages",
"Thinking blocks contain current intent and reasoning, making them ideal queries for finding contextually relevant memories",
"Thinking blocks are shorter than user messages",
"Claude's thinking is always more accurate than user messages"
],
correctOption: 1,
explanation: "Thinking blocks contain Claude's current intent, decisions, constraints, and assumptions. 'I'm drafting an executive summary for the quarterly report' is a much better query than the original 'reorganize the documentation' because it matches turn 20's actual needs.",
source: "Lesson 9: Memory Injection"
},
{
question: "Your memory injection hook keeps returning the same memories for consecutive tool calls. What mechanism prevents this waste?",
options: [
"Rate limiting on the memory database",
"Caching at the vector database level",
"Deduplication using thinking hashes - skip injection if the same memory was recently injected",
"Maximum injection count per session setting"
],
correctOption: 2,
explanation: "Deduplication using thinking hashes. The hook tracks (memory_id, thinking_hash) pairs with a TTL (~5 minutes). If the same memory was recently injected for similar thinking, it's skipped. This prevents redundant context consumption.",
source: "Lesson 9: Memory Injection"
},
{
question: "Three agents work sequentially: Agent A (research) -> Agent B (analyze) -> Agent C (write). Agent C produces confused output referencing irrelevant research tangents. What's the problem?",
options: [
"Agent C has a bug in its prompting",
"The research from Agent A was incorrect",
"Agent C needs more context to produce quality output",
"Dirty slate problem - Agent C inherited 50,000 tokens of accumulated process instead of ~2,000 tokens needed"
],
correctOption: 3,
explanation: "Dirty slate problem. Agent C inherited Agent A's 15 file reads, 3 exploratory approaches, plus Agent B's analytical tangents. It needed ~2,000 tokens (analysis + task) but got 50,000 tokens of accumulated process. Context isolation solves this.",
source: "Lesson 10: Context Isolation"
},
{
question: "In the clean context pattern, how do agents communicate?",
options: [
"Full context handoff between each agent",
"Each agent receives fresh context and returns only summaries to the orchestrator",
"Shared memory space all agents can read and write",
"Direct agent-to-agent messaging without orchestrator"
],
correctOption: 1,
explanation: "In the clean context pattern, each subagent receives fresh context (only what it needs), operates with full attention budget, and returns summaries to the orchestrator. The orchestrator synthesizes summaries into final output. No context accumulation.",
source: "Lesson 10: Context Isolation"
},
{
question: "You're building a document review pipeline with three independent reviewers. Which subagent pattern should you use?",
options: [
"Stateful (handoff) - reviewers should see each other's findings",
"Stateless (subagent) - each reviewer gets fresh context without influence from others",
"Shared (network) - all reviewers write to common memory",
"Sequential pipeline - one reviewer at a time"
],
correctOption: 1,
explanation: "Stateless (subagent) pattern. Independent reviewers should NOT see each other's findings-that's the point of multiple perspectives. Each gets fresh context with document and criteria only. The orchestrator synthesizes their independent findings.",
source: "Lesson 10: Context Isolation"
},
{
question: "A subagent produces work violating your project conventions because it started with fresh context. What's the workaround?",
options: [
"Use dirty slate instead for consistency",
"Add conventions to every prompt manually",
"Context amnesia workarounds: preload Skills with project knowledge, or include critical context in delegation prompt",
"Disable context isolation for better results"
],
correctOption: 2,
explanation: "Context amnesia workarounds: (1) Preload Skills with project conventions, (2) Master-clone architecture (read CLAUDE.md at task start), or (3) Include critical context explicitly in the delegation prompt. These solve amnesia without dirty slate problems.",
source: "Lesson 10: Context Isolation"
},
{
question: "You're at 75% context utilization, mid-task, with important strategic decisions made this session. What should you do?",
options: [
"`/clear` - get a fresh start immediately",
"`/compact` with custom instructions preserving the strategic decisions",
"Continue working - 75% is fine for now",
"Save decisions to a file then `/clear` everything"
],
correctOption: 1,
explanation: "`/compact` with custom instructions. You're in Orange zone (75%), task incomplete, with valuable decisions to preserve. `/clear` would lose the decisions; continuing risks quality degradation. Compact preserves decisions while reclaiming budget.",
source: "Lesson 11: Context Engineering Playbook"
},
{
question: "Your agent keeps ignoring standards you documented in CLAUDE.md. Using the decision tree, what should you check first?",
options: [
"Whether the model is capable enough",
"Whether to use a different agent",
"Position (are standards in middle 80%?), then noise (buried in 400 lines?), then budget (context at 80%?)",
"If the standards are correctly written"
],
correctOption: 2,
explanation: "The decision tree says: check position first (are standards in the middle 80%?), then signal-to-noise (buried in 400 lines of context?), then budget (is context at 80%?). Most problems have multiple contributing causes; diagnose systematically.",
source: "Lesson 11: Context Engineering Playbook"
},
{
question: "A session is 4 days old with accumulated tangents and outdated decisions. You want to continue the same task. What should you do?",
options: [
"Start fresh session, read the progress file to reconstruct state - sessions expire after ~3 days",
"`claude --continue` - resume where you left off",
"`/compact` the old session to clean it up",
"Merge the old session with a new one"
],
correctOption: 0,
explanation: "Sessions expire after ~3 days. Resuming a 4-day-old session creates more confusion than starting fresh. Start a new session, read the progress file to reconstruct state, then continue with clean context.",
source: "Lesson 11: Context Engineering Playbook"
},
{
question: "Which scenario requires memory injection (PreToolUse hooks)?",
options: [
"A single-turn question about the project",
"A 5-minute task in one session only",
"Any task using Claude Code at all",
"A 20-turn workflow where Claude's actual needs drift far from the original prompt"
],
correctOption: 3,
explanation: "Memory injection (PreToolUse hooks) is for long workflows where Claude's needs drift from the original prompt. Single-turn questions and short tasks work fine with UserPromptSubmit (prompt-time) injection. PreToolUse adds complexity only justified for extended workflows.",
source: "Lesson 9: Memory Injection"
},
{
question: "You're designing a CLAUDE.md for a new project. Which opening is optimal for Zone 1?",
options: [
"## Critical Constraints: Never share drafts externally. Always verify data before reporting.",
"Welcome to the project! This is a client engagement that...",
"## Tools Used: Notion, Slack, Google Workspace",
"This document explains how to work with our processes..."
],
correctOption: 0,
explanation: "Zone 1 (first 10%) gets highest attention due to primacy. Use it for critical constraints like confidentiality rules and non-negotiable requirements. Tool information and welcome messages waste prime position. Critical constraints should be the first thing Claude sees.",
source: "Lesson 3: Lost in the Middle"
},
{
question: "What is 'context rot' and how does it manifest?",
options: [
"When files become corrupted in the file system",
"When Claude's model weights degrade over time",
"When outdated decisions, abandoned approaches, and resolved debates pollute context, diluting signal",
"When API rate limits cause connection issues"
],
correctOption: 2,
explanation: "Context rot occurs when outdated decisions, abandoned approaches, debug tangents, and resolved debates accumulate in context. This dilutes signal-to-noise ratio over time. It's a primary reason long sessions degrade and why fresh sessions with progress files outperform continuation.",
source: "Lesson 7: Context Lifecycle"
},
{
question: "The 4-question audit asks 'Would Claude ask about this on its own?' If YES, what does that indicate?",
options: [
"The content is definitely NOISE and should be removed",
"The content should be moved to a separate file",
"The content is too complex for Claude to understand",
"The content is potentially SIGNAL worth keeping in CLAUDE.md"
],
correctOption: 3,
explanation: "If Claude would ask about something on its own, it indicates genuinely necessary information that Claude can't infer from other sources. This is the first filter in the 4-question audit. If YES, proceed to other questions. If NO, it's likely noise.",
source: "Lesson 4: Signal vs Noise"
},
{
question: "You notice your agent is producing lower quality output despite no changes to your prompts. Context is at 65%. What's likely happening?",
options: [
"The model was updated and became worse",
"65% is still too high for quality work",
"The API is having performance issues",
"Context rot - accumulated noise is diluting attention even below 70%"
],
correctOption: 3,
explanation: "Context rot can degrade quality even below the 70% threshold. The issue isn't total utilization but signal-to-noise ratio. Accumulated tangents, abandoned approaches, and resolved debates dilute attention. Consider compacting or starting fresh with progress file state.",
source: "Lesson 7: Context Lifecycle"
},
{
question: "A team member asks 'Why can't I just use --continue forever?' What's the core limitation?",
options: [
"Context windows are finite; information gets lost, noise accumulates, and the model eventually forgets early context",
"API rate limits prevent long sessions",
"The --continue flag has a built-in timeout",
"Each session costs more money than fresh starts"
],
correctOption: 0,
explanation: "Context windows are finite. Early messages get truncated as new content arrives. Context rot accumulates. The model doesn't truly 'remember' - it re-reads everything fresh each turn. Long sessions compound these issues; fresh sessions with progress files avoid them.",
source: "Lesson 2: The Attention Budget"
},
{
question: "When should you use `/compact` vs `/clear`?",
options: [
"Always use `/clear` because it's simpler",
"Always use `/compact` to preserve everything",
"`/compact` when mid-task with valuable context; `/clear` when starting fresh topic or context is corrupted",
"Neither - let Claude manage context automatically"
],
correctOption: 2,
explanation: "`/compact` preserves important context while reclaiming space - use mid-task when you have valuable decisions and state. `/clear` resets completely - use when starting a new topic, context is severely polluted, or you want a clean slate. Match the tool to the situation.",
source: "Lesson 7: Context Lifecycle"
},
{
question: "Your CLAUDE.md has 150 lines. After applying the 4-question audit to each line, 90 lines fail all questions. What should you do?",
options: [
"Remove the 90 lines of noise, reducing to ~60 lines of pure signal",
"Keep everything - 150 lines isn't excessive",
"Move everything to external docs and start fresh",
"Compress the 90 lines into 30 lines instead"
],
correctOption: 0,
explanation: "Remove the 90 lines that fail the audit. This reduces you to ~60 lines of pure signal - the target range. Every line of noise dilutes the signal that matters. Don't compress noise into fewer lines; eliminate it entirely.",
source: "Lesson 4: Signal vs Noise"
},
{
question: "What distinguishes Zone 2 content from Zone 1 and Zone 3 content?",
options: [
"Zone 2 is for the most important content in CLAUDE.md",
"Zone 2 should be kept empty to maximize other zones",
"Zone 2 gets the highest attention from the model",
"Zone 2 is the 'middle 80%' for stable reference material that's important but not critical"
],
correctOption: 3,
explanation: "Zone 2 (middle 80%) is for stable reference material: workflow patterns, conventions, project structure. It's important but not critical like Zone 1 constraints or Zone 3 workflows. Zone 2 content is consulted when needed, not applied to every interaction.",
source: "Lesson 3: Lost in the Middle"
},
{
question: "You're implementing PreToolUse memory injection. Why extract the LAST 1,500 characters of thinking rather than the first?",
options: [
"The first characters are usually system prompt noise",
"The last characters contain Claude's most current reasoning, decisions, and immediate intent",
"The last characters use fewer tokens to process",
"The first characters are compressed by the model"
],
correctOption: 1,
explanation: "The last 1,500 characters contain Claude's most current reasoning - what it's about to do, why, and what constraints it's considering. Earlier thinking may be exploratory or already resolved. Current intent produces better semantic search queries.",
source: "Lesson 9: Memory Injection"
},
{
question: "An orchestrator spawns 5 research subagents in parallel. Each returns 10,000 tokens of findings. What's the risk if the orchestrator keeps all 50,000 tokens?",
options: [
"The subagents will crash from memory issues",
"The API will reject messages this large",
"Each subagent will see the other's findings",
"The orchestrator's context fills rapidly, limiting its ability to synthesize and reason about findings"
],
correctOption: 3,
explanation: "50,000 tokens of subagent output would consume significant orchestrator context, limiting its ability to synthesize and reason. The orchestrator should receive summaries (~500-1000 tokens each), not full outputs. Subagents do deep work; orchestrators work with distilled insights.",
source: "Lesson 10: Context Isolation"
},
{
question: "What is the 'master-clone' architecture pattern for context isolation?",
options: [
"Running multiple identical Claude instances in parallel",
"Cloning the entire project for each agent",
"Orchestrator reads CLAUDE.md and includes critical context in each subagent delegation prompt",
"Using version control branches to isolate agent work"
],
correctOption: 2,
explanation: "Master-clone: the orchestrator reads CLAUDE.md once and includes critical project context in each subagent's delegation prompt. This gives subagents necessary knowledge without them inheriting accumulated orchestrator context. Fresh context + relevant knowledge.",
source: "Lesson 10: Context Isolation"
},
{
question: "Why is context engineering compared to 'quality control in a factory'?",
options: [
"Both involve physical manufacturing of products",
"Both recognize that input quality determines output quality - garbage in, garbage out",
"Both require expensive equipment and machinery",
"Both are only relevant for large-scale operations"
],
correctOption: 1,
explanation: "Context is the raw material; agent output is the product. Just as manufacturing defects stem from input material quality, agent errors often stem from context quality. Context engineering is quality control - inspecting, filtering, and optimizing inputs to maximize output quality.",
source: "Lesson 1: The Context Bottleneck"
},
{
question: "You're debugging an agent that keeps making the same mistake despite corrections in the conversation. Context is at 45%. What's likely happening?",
options: [
"45% is still too high for reliable operation",
"The model is ignoring your instructions deliberately",
"The correction is in the middle of context where attention is lowest - reposition it or restate at the end",
"The API is caching old responses incorrectly"
],
correctOption: 2,
explanation: "Position matters. A correction made 20 turns ago is now in the 'Lost in the Middle' zone where recall drops ~30%. Restate the correction at the end of your message (Zone 3 for that turn) or add it to CLAUDE.md Zone 1. Fresh context sees old corrections with lower attention.",
source: "Lesson 3: Lost in the Middle"
},
{
question: "Your progress file's 'Decisions Made' section is empty. The team is now in Session 5. What problem will this cause?",
options: [
"Session 5 may re-debate decisions from Sessions 1-4, wasting time and potentially reversing good choices",
"No problem - decisions are stored in project history",
"The project will fail to complete correctly",
"Claude will refuse to continue the work"
],
correctOption: 0,
explanation: "Without recorded decisions, Session 5 has no memory of Sessions 1-4's choices. It may re-debate 'Should we use approach A or approach B?' when Session 2 already decided. Worse, it might choose differently, creating inconsistency. Decisions + rationale prevent revisiting closed questions.",
source: "Lesson 8: Progress Files"
},
{
question: "What's the relationship between Principle 5 (Persisting State in Files) and context engineering?",
options: [
"They're unrelated concepts from different chapters",
"Principle 5 replaces the need for context engineering",
"Context engineering is the WHY behind Principle 5 - files persist state because LLM context is ephemeral and limited",
"Context engineering contradicts Principle 5's recommendations"
],
correctOption: 2,
explanation: "Context engineering explains WHY Principle 5 works. LLM context is ephemeral (forgotten between sessions), limited (finite tokens), and attention-distributed unevenly. Files bypass all three constraints - they persist indefinitely, don't consume context until read, and can be strategically loaded.",
source: "Lesson 1: The Context Bottleneck"
},
{
question: "A professional says 'I'll just use the biggest context window available.' Why isn't this a solution to context engineering?",
options: [
"Bigger windows still have position sensitivity, attention limits, and accumulate noise - size doesn't solve quality",
"Bigger windows cost too much money per request",
"The API doesn't support large context windows",
"Bigger windows are only available for enterprise users"
],
correctOption: 0,
explanation: "A larger context window is bigger, not better. Position sensitivity still causes middle content to get ~30% less attention. Attention is still finite - more context means each token gets less focus. Noise still accumulates. Context engineering addresses quality, not just quantity.",
source: "Lesson 2: The Attention Budget"
},
{
question: "When implementing the three-zone strategy, what percentage of your CLAUDE.md should be in Zone 1?",
options: [
"50% for maximum critical content impact",
"10% - just enough for critical constraints",
"30% to balance primacy with content needs",
"0% - Zone 1 should be empty for flexibility"
],
correctOption: 1,
explanation: "Zone 1 should be ~10% of your CLAUDE.md. With a 60-line target, that's ~6 lines for critical constraints. Zone 1 gets primacy effect (high attention), so reserve it for non-negotiable rules. More than 10% dilutes the primacy advantage.",
source: "Lesson 3: Lost in the Middle"
},
{
question: "You're using semantic search for memory injection. The search returns 10 memories but your token budget allows 3. How should you select?",
options: [
"Take the first 3 results from the search",
"Take the 3 with highest similarity scores AND verify they're not duplicates of recent injections",
"Randomly select 3 for diversity",
"Take the 3 longest memories for maximum context"
],
correctOption: 1,
explanation: "Take highest similarity scores (most relevant to current thinking) AND check against recent injection cache to avoid duplicates. Highest similarity ensures relevance. Deduplication prevents wasting tokens on recently-injected information. Both criteria matter.",
source: "Lesson 9: Memory Injection"
},
{
question: "Your CLAUDE.md says 'Use our standard review process' but doesn't specify what that process is. Is this SIGNAL or NOISE?",
options: [
"SIGNAL - it reminds Claude to use standard processes",
"PARTIAL - the intent is good but execution is incomplete",
"It depends on whether Claude knows the process",
"NOISE - it's an incomplete instruction that Claude can't follow without more context"
],
correctOption: 3,
explanation: "NOISE. An instruction Claude can't act on adds confusion, not value. Either specify the process inline (if under 3 lines) or reference an external file with the details. Incomplete instructions are worse than no instructions - they consume tokens without enabling action.",
source: "Lesson 4: Signal vs Noise"
},
{
question: "What is 'tacit knowledge' in the context of engineering context for AI agents?",
options: [
"Knowledge stored in databases and documentation systems",
"Knowledge that AI models learn during pre-training",
"Implicit knowledge humans have but don't explicitly state - conventions, preferences, 'obvious' requirements",
"Technical specifications written in formal languages"
],
correctOption: 2,
explanation: "Tacit knowledge is what you know but don't think to say - 'obvious' conventions, unstated preferences, assumptions about how things work. Professionals forget to encode it because it's automatic to them. Context engineering surfaces tacit knowledge into explicit instructions.",
source: "Lesson 6: Tacit Knowledge"
},
{
question: "A senior consultant's client recommendations are inconsistent - sometimes accepting approaches they rejected before. What context engineering solution helps?",
options: [
"Encode review criteria and preferences into Skills or AGENTS.md to externalize tacit knowledge",
"Train the consultant to be more consistent",
"Use multiple reviewers to average out inconsistency",
"Skip review entirely for minor recommendations"
],
correctOption: 0,
explanation: "The inconsistency comes from tacit knowledge varying by mood, memory, and context. Externalizing preferences into Skills or AGENTS.md makes criteria consistent and transferable. The agent applies the same standards every time because they're explicit, not implicit.",
source: "Lesson 6: Tacit Knowledge"
},
{
question: "According to the Context Architecture lesson, what are the four context tools and their loading patterns?",
options: [
"All four tools load at session start and stay loaded throughout",
"CLAUDE.md loads always; Skills load on-demand; Subagents use isolated context; Hooks run externally with zero cost",
"Skills and Subagents are the same thing with different names",
"Hooks load first, then CLAUDE.md, then Skills, then Subagents"
],
correctOption: 1,
explanation: "The four tools have distinct loading patterns: CLAUDE.md loads at session start (every request cost), Skills load descriptions at start but full content only when invoked (on-demand), Subagents spawn with fresh isolated context (zero main context cost), and Hooks run externally (zero context cost). Understanding these patterns is key to efficient architecture.",
source: "Lesson 5: Context Architecture"
},
{
question: "A marketing consultant has a 500-line CLAUDE.md containing client context, competitor analysis frameworks, metrics definitions, and campaign templates. What's the architecture problem?",
options: [
"500 lines is acceptable for comprehensive documentation",
"Everything in CLAUDE.md means ~4,000+ tokens consumed every request, even when only client context is needed",
"The content should be split into multiple CLAUDE.md files",
"Hooks should handle all of this content"
],
correctOption: 1,
explanation: "Everything in CLAUDE.md consumes tokens on EVERY request. With 500 lines (~4,000+ tokens), even a simple question about client context loads competitor frameworks, metrics, and templates unnecessarily. Move 'sometimes needed' content to Skills (loaded on-demand) to reduce baseline from ~4,000 tokens to ~400 tokens.",
source: "Lesson 5: Context Architecture"
},
{
question: "Using the Context Architecture decision framework, where should you put 'sometimes needed, substantial content' like a detailed review checklist?",
options: [
"CLAUDE.md - so it's always available",
"Skill - on-demand loading saves context when not reviewing",
"Subagent - for isolated processing",
"Hook - for deterministic execution"
],
correctOption: 1,
explanation: "The decision framework maps 'sometimes needed, stable' content to Skills. A review checklist is needed only when reviewing (not always), is substantial (more than a few lines), and doesn't change frequently. Skills load descriptions at start (~100 tokens) but full content only when invoked, saving context for other work.",
source: "Lesson 5: Context Architecture"
}
]}
/>
