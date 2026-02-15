---
sidebar_position: 3
title: "Lesson 3: Your First Real Work"
description: "Make your AI Employee earn its keep with real, valuable tasks that demonstrate genuine productivity gains"
keywords:
  [
    ai employee tasks,
    email triage,
    research assistant,
    practical ai,
    ai productivity,
    task delegation,
    openclaw tasks,
  ]
chapter: 12
lesson: 3
duration_minutes: 30

# HIDDEN SKILLS METADATA
skills:
  - name: "AI Employee Task Delegation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Can delegate real tasks to AI Employee and evaluate output quality against requirements"

  - name: "AI Output Quality Evaluation"
    proficiency_level: "B1"
    category: "Analytical"
    bloom_level: "Evaluate"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Can assess AI-generated work for accuracy, completeness, and usefulness"

  - name: "Domain Task Identification"
    proficiency_level: "B1"
    category: "Strategic"
    bloom_level: "Analyze"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Can identify tasks in own domain suitable for AI Employee delegation"

learning_objectives:
  - objective: "Delegate a real, valuable task to your AI Employee and receive actionable output"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Completed task with documented value delivered"
  - objective: "Evaluate AI Employee output for accuracy, completeness, and practical usefulness"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Written reflection comparing AI output to expected quality standards"
  - objective: "Identify at least three tasks in your domain suitable for AI Employee delegation"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Domain-specific task list with delegation criteria"

cognitive_load:
  new_concepts: 2
  assessment: "2 concepts (task delegation patterns, output evaluation) well within B1 limit of 3-5"

differentiation:
  extension_for_advanced: "Attempt 5+ different domain-specific tasks; measure time savings quantitatively; document edge cases where AI needed guidance"
  remedial_for_struggling: "Start with the research task (requires no external integrations); use provided prompts verbatim before customizing"
---

# Your First Real Work

Your AI Employee is connected. You sent a test message and got a response. That proved the system works. Now let's make it **earn its keep**.

There's a crucial difference between demos and real work. A demo is "Ask AI to write a haiku." Real work is "Sort through my 47 unread emails and tell me which three need my attention today." The first impresses at parties. The second saves your Tuesday morning.

In the next 30 minutes, you'll cross that threshold. You'll give your AI Employee a task that would genuinely consume your time, watch it execute, and measure the value delivered. By the end, you'll have a clear answer to the question every skeptic asks: "But does it actually help?"

---

## The Three Universal Use Cases

We'll work through three types of tasks that apply to nearly everyone. Pick one that matches your immediate situation, or try all three.

### Use Case A: Email Triage

Email is the universal time sink. The average professional spends 28% of their workday on email. Much of that time goes to a single decision: "Do I need to respond to this now, later, or never?"

Send this to your AI Employee via Telegram:

```
Check my last 20 emails. Categorize them as:
1. URGENT - needs response today
2. IMPORTANT - needs response this week
3. FYI - just informational
4. SPAM - can ignore

Summarize the urgent ones in 2 sentences each.
```

**What happens next depends on your setup.** If you have already connected Gmail via `gog` (covered in Lesson 7), your AI Employee will access your actual inbox and return real categorizations. If Gmail is not connected yet, you will see something like:

```
I don't currently have access to your email. To enable email
triage, we'll need to connect Gmail through gog. Would you
like instructions for that?
```

That response itself is valuable information. Your AI Employee is telling you exactly what capability it's missing and what you need to do about it. This is the "honest about limitations" behavior that distinguishes useful AI from hype.

**For now, if email isn't connected**, you can test this pattern by pasting email content directly:

```
Here are my 5 most recent emails. Categorize each as
URGENT/IMPORTANT/FYI/SPAM and give me a 2-sentence summary
of the urgent ones:

[Paste email subjects and first paragraphs here]
```

**What just happened**: Whether using live email access or pasted content, you delegated a cognitive task that normally requires you to read, evaluate, and prioritize. The AI Employee performed the initial triage. You review its categorizations in 30 seconds instead of scanning 20 emails for 15 minutes.

---

### Use Case B: Research Task

Research is where AI Employees shine brightest. The task that would take you three hours of tab-hopping, reading, and note-taking collapses into minutes.

```
Research the top 5 competitors to [YOUR COMPANY] in AI adoption.

For each competitor, tell me:
- What AI tools they're publicly using
- Any announcements about AI initiatives in the last 6 months
- Estimated investment level (low/medium/high based on public signals)

Put findings in a table format.
```

Replace `[YOUR COMPANY]` with your actual employer or a company you're interested in.

**What you'll receive**: A structured analysis that would have required you to visit multiple websites, read press releases, scan LinkedIn posts, and synthesize findings. Your AI Employee does this in parallel, drawing on its knowledge and (if configured with web access) current information.

**Evaluating the output**: This is where your judgment matters. The AI Employee might:

- Miss a competitor you know about (add it to the prompt and ask again)
- Overstate investment levels (ask for sources or qualifying language)
- Include outdated information (ask for recency verification)

The back-and-forth refinement is part of the value. You're not blindly accepting AI output. You're directing an intelligent assistant that gets better with each clarification.

**What just happened**: Research that would consume a morning became a 5-minute task. Not because the AI is smarter than you, but because it can process information in parallel while you provide strategic direction.

---

### Use Case C: Your Domain

The universal use cases prove the concept. The real value comes from tasks specific to your work.

Here are starting prompts for different domains. Pick yours and customize:

**Legal**:

```
Review this contract clause and identify:
1. Potential risks to our company
2. Non-standard terms compared to typical agreements
3. Suggested modifications with rationale

[Paste contract clause here]
```

**Finance**:

```
Analyze these expense categories from Q4:
- What's the month-over-month trend?
- Which categories show unusual variance?
- What questions should I ask department heads about outliers?

[Paste expense data here]
```

**Marketing**:

```
Draft 5 LinkedIn posts about [TOPIC] for our company.

Requirements:
- Professional but not stuffy
- Include one call-to-action per post
- Vary the format (question, statistic, story, etc.)
- Target audience: [DESCRIBE YOUR AUDIENCE]
```

**Development**:

```
Explain this error and suggest fixes:

[Paste error message and relevant code context]

Include:
1. What caused this error
2. How to fix it immediately
3. How to prevent it in the future
```

**Sales**:

```
Draft a follow-up email to [PROSPECT NAME] at [COMPANY].

Context:
- We met at [EVENT/MEETING]
- They expressed interest in [PRODUCT/FEATURE]
- Their main concern was [OBJECTION]

Tone: Professional but warm, not pushy
Goal: Schedule a 15-minute call
```

**Healthcare Administration**:

```
Summarize this patient case for the care coordination meeting:

[Paste relevant case notes - ensure HIPAA compliance by using
deidentified data or approved systems]

Include:
- Key diagnoses and current treatments
- Recent changes or concerns
- Questions for the team
```

**What you're building**: A mental model of which tasks in YOUR domain translate well to AI delegation. The common pattern is work that requires processing information, following a structure, and producing a draft that you then refine.

---

## Reflection: Value Delivered

You've now completed at least one real task with your AI Employee. Before moving on, capture what just happened.

**Exercise: Calculate Your ROI**

Grab a piece of paper (or open a note) and answer:

| Question                                         | Your Answer         |
| ------------------------------------------------ | ------------------- |
| Task you delegated                               |                     |
| Time it would have taken you                     | \_\_\_ minutes      |
| Time to write the prompt                         | \_\_\_ minutes      |
| Time to review output                            | \_\_\_ minutes      |
| Time saved                                       | \_\_\_ minutes      |
| What's your hourly rate (or value of your time)? | $\_\_/hour          |
| Value of time saved                              | $\_\_               |
| Cost of this AI interaction                      | $0 (Kimi free tier) |

**Complete this sentence**: "I just got $**_ worth of value in _** minutes."

This isn't vanity math. This is the business case for AI Employees. When you can demonstrate concrete time savings, you understand why organizations are investing heavily in this technology.

**Quality check**: Was the AI output good enough to use directly, or did it need significant editing?

| Quality Level       | What It Means                                               |
| ------------------- | ----------------------------------------------------------- |
| **Direct use**      | Output usable as-is or with minor tweaks                    |
| **Good draft**      | Saved significant time but needed 20-30% editing            |
| **Starting point**  | Provided structure or ideas but required substantial rework |
| **Missed the mark** | Needed to re-prompt or rethink the approach                 |

Any of these outcomes is valuable data. "Direct use" means you've found a high-value delegation pattern. "Missed the mark" means you've learned what NOT to delegate, or how to prompt differently next time.

---

## Patterns That Work vs. Patterns That Don't

After working with hundreds of AI Employee users, clear patterns emerge about what tasks translate well to delegation:

**Tasks That Work Well**:

| Task Type                   | Why It Works                                      |
| --------------------------- | ------------------------------------------------- |
| **Information synthesis**   | AI processes large volumes faster than humans     |
| **First drafts**            | Structure and starting point save blank-page time |
| **Research and comparison** | Parallel information gathering is AI strength     |
| **Format conversion**       | Transforming data between formats is mechanical   |
| **Consistency checking**    | AI doesn't get tired or skip items                |

**Tasks That Need Human Judgment**:

| Task Type                   | Why Humans Excel                                   |
| --------------------------- | -------------------------------------------------- |
| **Final decisions**         | Context, relationships, politics that AI can't see |
| **Creative strategy**       | AI can generate options; you choose direction      |
| **Sensitive communication** | Tone, timing, and relationship nuance              |
| **Ethical judgments**       | Values and principles require human ownership      |
| **Novel situations**        | Unprecedented cases need human reasoning           |

The sweet spot is the middle: tasks with clear patterns where AI handles the mechanical work and you provide the judgment.

---

## What Comes Next

You've now experienced the core value proposition of an AI Employee: real work, real value, real time savings. You've gone from "Does this actually work?" to "How do I get more of this?"

The next three lessons answer that question:

- **Lesson 4**: How your AI Employee actually works (the architecture)
- **Lesson 5**: Your Employee's memory (making it remember your preferences)
- **Lesson 6**: Teaching your Employee skills (building portable capabilities)
- **Lessons 7-9**: Connecting real services, trust boundaries, and 24/7 deployment

The experience you just had is the starting point. The skills you're about to build will multiply it.

---

## Try With AI

These prompts help you explore what your AI Employee can handle. Work through them to discover your personal high-value delegation patterns.

### Prompt 1: Calendar Analysis

```
Analyze my calendar for this week. Tell me:
1. What are my busiest days?
2. Are there any scheduling conflicts or back-to-back meetings?
3. Where do I have focus time blocks?
4. Suggest one optimization to improve my week.

[If no calendar access: paste your meeting list]
```

**What you're learning**: Calendar analysis is a compound task. It requires understanding meeting types, recognizing patterns, and making suggestions. You're testing whether your AI Employee can handle multi-step reasoning about your schedule.

### Prompt 2: Meeting Preparation

```
I need to prepare for a meeting about [TOPIC] tomorrow.

Research and give me:
1. Current state of [TOPIC] - what should I know?
2. Key players or stakeholders in this space
3. Three discussion points I should raise
4. One question I should ask that will make me look prepared

Format this as a one-page briefing document.
```

**What you're learning**: Meeting prep combines research, synthesis, and strategic thinking. The AI Employee can gather information faster than you, but your judgment about which points matter most still guides the final preparation.

### Prompt 3: Document Analysis

```
Review this document and give me:
1. Executive summary (3 bullets max)
2. Three strengths of the proposal/argument
3. Three concerns or gaps
4. Recommended action: approve, revise, or reject (with reasoning)

[Paste document or describe it for practice]
```

**What you're learning**: Document review is a staple of professional work. You're testing whether your AI Employee can extract the essential points and provide analytical perspective that helps you make faster decisions.

**Safety reminder**: Be thoughtful about what information you share with your AI Employee. Avoid sharing confidential data, personal information about others, or proprietary company secrets through channels that aren't approved for that sensitivity level. When in doubt, use anonymized or hypothetical examples.
