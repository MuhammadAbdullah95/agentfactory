---
sidebar_position: 7
title: "Lesson 7: Teaching Professional Formats"
description: "Create email-templates skill for consistent, professional communications"
keywords: [email templates, skill composition, business emails, professional formats, openclaw skills]
chapter: 12
lesson: 7
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "Skill Composition"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Can create complementary skills that work together, understanding how to separate concerns between drafting logic and template structure"

  - name: "Template-Based Skill Design"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Can design skills that provide structured templates for AI to follow, ensuring consistent output formats"

learning_objectives:
  - objective: "Create template-based skills that provide structured formats"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Working email-templates skill that OpenClaw successfully uses"
  - objective: "Understand skill composition patterns"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explain how email-drafter and email-templates work together"
  - objective: "Customize templates for your specific domain"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Add at least one custom template based on emails you actually send"

cognitive_load:
  new_concepts: 2
  assessment: "Low cognitive load - skill composition builds directly on L06 patterns, templates are familiar business formats"

differentiation:
  extension_for_advanced: "Create 5+ domain-specific templates covering your most common business scenarios"
  remedial_for_struggling: "Use provided templates without modification, focus on understanding how skills compose"
---

# Teaching Professional Formats

In Lesson 6, you taught your AI employee to draft emails through the `email-drafter` skill. Your employee can now write professional correspondence. But every email still requires you to specify the structure: "Include a greeting, then the main point, then action items, then a sign-off."

What if your employee already knew your preferred formats?

Professional communicators don't reinvent their email structure for every message. They have mental templates: meeting requests follow one pattern, project updates follow another, follow-ups follow a third. The format becomes automatic, freeing mental energy for the actual content.

This lesson teaches your AI employee those same templates. You'll create an `email-templates` skill that complements your `email-drafter` skill. Together, they form a composition: one skill handles the writing logic, the other provides the structural patterns. This is how real employees work with style guides and templates, and it's how your AI employee will work too.

## Why Templates Matter

When you send a meeting request email, recipients expect certain information: the topic, suggested times, and a clear ask. When you send a project update, stakeholders expect status, accomplishments, blockers, and next steps. These aren't arbitrary conventions. They evolved because they work.

Templates provide three benefits:

| Benefit | Without Templates | With Templates |
|---------|------------------|----------------|
| **Consistency** | Format varies by mood and memory | Same professional structure every time |
| **Speed** | Explain format each request | Just specify the content |
| **Quality** | Miss elements, confuse readers | Complete, scannable, action-oriented |

Your AI employee already knows how to write well. Templates tell it what "well" means for your specific communication patterns.

## The email-templates Skill

Navigate to your workspace and create a new skill:

```bash
mkdir -p ~/.openclaw/workspace/skills/email-templates
```

Create the skill file at `~/.openclaw/workspace/skills/email-templates/SKILL.md`:

```markdown
---
name: email-templates
description: Professional email templates for common business scenarios
metadata: { "openclaw": { "always": true } }
---

# Email Templates

Use these templates for common email scenarios. Customize based on context while maintaining the core structure.

## Meeting Request

```
Subject: Meeting Request: [Topic] - [Date/Timeframe]

Hi [Name],

I'd like to schedule a meeting to discuss [topic].

Suggested times:
- [Option 1]
- [Option 2]

Please let me know what works best for you.

Thanks,
[Your name]
```

## Follow-Up After Meeting

```
Subject: Follow-up: [Meeting Topic] - Action Items

Hi [Name],

Thank you for meeting with me today. Here's a summary:

**Key Decisions:**
- [Decision 1]
- [Decision 2]

**Action Items:**
- [ ] [Person]: [Task] by [Date]
- [ ] [Person]: [Task] by [Date]

**Next Steps:**
[What happens next]

Please let me know if I missed anything.

Best,
[Your name]
```

## Project Update

```
Subject: [Project Name] Update - [Date]

Hi team,

**Status:** [On track / At risk / Blocked]

**Completed this week:**
- [Accomplishment 1]
- [Accomplishment 2]

**In progress:**
- [Task 1] - [%] complete
- [Task 2] - [%] complete

**Blockers:**
- [Blocker or "None"]

**Next week:**
- [Plan 1]
- [Plan 2]

Questions? Reply or grab me on Slack.

[Your name]
```

## Cold Outreach

```
Subject: [Specific value prop] for [Company]

Hi [Name],

I noticed [specific observation about their company/work].

At [Your company], we help [target audience] with [specific problem].

[One sentence proof point or case study]

Would you be open to a 15-minute call to explore if this might be relevant for [Company]?

Best,
[Your name]
```
```

**Output:**

After creating this file, verify it exists:

```bash
cat ~/.openclaw/workspace/skills/email-templates/SKILL.md | head -20
```

```
---
name: email-templates
description: Professional email templates for common business scenarios
metadata: { "openclaw": { "always": true } }
---

# Email Templates

Use these templates for common email scenarios...
```

The `"always": true` setting means your employee will always have these templates available, without you needing to request them explicitly.

## How Skills Compose

You now have two email-related skills:

| Skill | Purpose | What It Provides |
|-------|---------|------------------|
| `email-drafter` | Writing logic | Tone, clarity, persuasion techniques |
| `email-templates` | Structure | Formats, sections, expected elements |

These skills complement each other through separation of concerns:

```
Your Request: "Draft a meeting request email to John about Q2 planning"
                           │
                           ▼
          ┌────────────────┴────────────────┐
          │                                  │
          ▼                                  ▼
   email-templates                    email-drafter
   (provides structure)               (provides writing)
          │                                  │
          │  "Meeting Request format:        │  "Professional tone,
          │   Subject, Greeting,             │   clear ask, appropriate
          │   Topic, Times, Close"           │   formality level"
          │                                  │
          └────────────────┬────────────────┘
                           │
                           ▼
                    Combined Output:
          Properly structured, well-written email
```

Neither skill alone produces optimal results. The drafter without templates might structure information poorly. The templates without the drafter would be rigid fill-in-the-blank forms. Together, they produce emails that are both well-structured and well-written.

This is skill composition: combining specialized capabilities into a more powerful whole.

## Testing the Composition

Restart your OpenClaw instance to load the new skill, then test the composition:

**Your request:**

```
Use the meeting request template to schedule a call with John about Q2 planning.
I'm flexible next Tuesday or Wednesday afternoon.
```

**Expected response:**

Your AI employee should produce something like:

```
Subject: Meeting Request: Q2 Planning Discussion - Next Week

Hi John,

I'd like to schedule a meeting to discuss our Q2 planning priorities.

Suggested times:
- Tuesday afternoon (2-5 PM)
- Wednesday afternoon (2-5 PM)

Please let me know what works best for you, and I'll send a calendar invite.

Thanks,
[Your name]
```

Notice what happened:
- The **template** provided the structure (subject format, greeting, suggested times section, closing)
- The **drafter** provided the content (natural language, appropriate detail level, professional tone)
- Neither required you to specify format or tone

**What emerged from composition:**

The AI combined structural knowledge from templates with writing ability from the drafter. You specified what you wanted (meeting with John about Q2), and your employee figured out both what to say and how to structure it.

## Adding Your Own Templates

The provided templates cover common scenarios, but your work has unique patterns. Think about emails you send repeatedly:

- Client status updates in your industry
- Internal announcements with your team's conventions
- Responses to common inquiries
- Escalation emails with proper urgency signals

To add a template, edit the skill file and add a new section:

```markdown
## [Your Template Name]

```
Subject: [Pattern]

[Body structure with placeholders]
```
```

For example, if you frequently send deadline reminder emails:

```markdown
## Deadline Reminder

```
Subject: Reminder: [Deliverable] Due [Date]

Hi [Name],

Quick reminder that [deliverable] is due [date/time].

Current status: [what you have / what's missing]

If you need an extension or have questions, please let me know by [earlier date].

Thanks,
[Your name]
```
```

**Output:**

After adding the template, test it:

```
Send a deadline reminder to Sarah about the quarterly report,
which is due this Friday. She sent a draft but it's missing
the financial projections section.
```

Your employee should produce:

```
Subject: Reminder: Quarterly Report Due Friday

Hi Sarah,

Quick reminder that the quarterly report is due this Friday.

Current status: I have your draft, but it's currently missing
the financial projections section.

If you need an extension or have questions, please let me know
by Wednesday.

Thanks,
[Your name]
```

## Three Templates to Add Now

Before moving on, add at least three templates based on emails you actually send. Consider:

1. **A recurring communication** - Something you send weekly or monthly
2. **A response pattern** - How you reply to common questions or requests
3. **A domain-specific format** - A structure unique to your industry or role

Don't aim for perfection. Start with rough templates, then refine them as you see your employee use them. The best templates evolve from real usage.

## Try With AI

These prompts help you practice skill composition and template customization.

### Prompt 1: Template Validation

```
Use the project update template for our website redesign project.
We're 60% complete, on track, with no blockers. This week we
finished the homepage mockups and mobile responsive layouts.
Next week we'll tackle the product pages and checkout flow.
```

**What you're learning:** How your employee interprets templates with real content. Notice whether it follows the structure faithfully while adapting the language naturally. If the output feels robotic, your drafter skill might need adjustment. If the structure is wrong, your template needs clarification.

### Prompt 2: Cold Outreach with Research

```
I need to send a cold outreach email to a marketing director at TechCorp
about our analytics tool. Before drafting, research TechCorp briefly to
find something specific I can reference. Then use the cold outreach template.
```

**What you're learning:** How skills compose with other capabilities. Your employee uses research (finding information about TechCorp), templates (cold outreach structure), and drafting (professional writing) together. This is the beginning of more complex workflow composition you'll explore later.

### Prompt 3: Custom Template Creation

```
Help me create a new email template for [describe a recurring email you send].
Ask me questions about what information is always included, what varies,
and what format my recipients expect. Then write the template in the same
style as my other email templates.
```

**What you're learning:** How to collaborate with AI on skill design. Your employee becomes a template co-creator, asking clarifying questions and proposing structures. This bidirectional process, where you provide domain knowledge and your employee provides structure, produces better templates than either of you would create alone.

**Safety note:** When testing email skills, always review the output before sending. Templates ensure consistency but don't guarantee correctness. Your domain knowledge remains essential for catching errors in names, dates, or context-specific details.
