---
title: "Links, Images, and Reusable Templates"
description: "Create reusable specification intelligence using links for references and templates with Persona + Questions + Principles pattern"
sidebar_label: "Links, Images, and Templates"
sidebar_position: 4
lesson: 4
chapter: 9
part: 3
duration: 50
concepts: 5
proficiency: A2
stage: 3
generated_by: content-implementer v1.0.0
source_spec: specs/034-chapter-9-markdown-redesign/spec.md
created: 2025-11-18
workflow: /sp.implement
version: 1.0.0
skills:
  markdown-links:
    proficiency: A2
  markdown-images:
    proficiency: A2
  intelligence-design:
    proficiency: A2
  template-creation:
    proficiency: A2
---

# Links, Images, and Reusable Templates

You've learned the core markdown elements: headings (structure), lists (requirements), and code blocks (outputs). Now you'll add **references** and create **reusable intelligence**.

This lesson marks a shift: from writing individual specifications to **designing intelligence that compounds across projects**. You'll create a **Feature Specification Template** that you can reuse anytime you need to describe a new feature—without referring back to this lesson.

This is intelligence design: build it once, use it everywhere.

---

## Why References Matter in Specifications

**Problem**: Specifications can't exist in isolation. They need to reference:
- Industry standards (OAuth 2.0 spec, REST API conventions)
- Documentation (library docs, framework guides)
- Examples (design patterns, best practices)
- Related work (similar features, prior decisions)

**Solution**: Links and images make specifications **connected** instead of **isolated**.

---

## Concept 1: Links for Reference Materials

Markdown links use this syntax: `[link text](URL)`

### Basic Link Syntax

```markdown
See [CommonMark specification](https://commonmark.org/) for markdown standard.
```

**Rendered**: See [CommonMark specification](https://commonmark.org/) for markdown standard.

**What this does**:
- Clickable text: "CommonMark specification"
- Points to: https://commonmark.org/
- Readers can verify your references

### When to Use Links in Specifications

**Scenario 1: Reference Industry Standards**

```markdown
## Authentication

Implementation must follow [OAuth 2.0 specification](https://oauth.net/2/).

Security requirements:
- [OWASP Authentication Guidelines](https://owasp.org/www-project-authentication/)
- [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-3/)
```

**Why this matters**: Developers know exactly which standards to follow. No ambiguity about "secure authentication."

**Scenario 2: Link to API Documentation**

```markdown
## Payment Processing

Use [Stripe API](https://stripe.com/docs/api) for payment handling.

Required endpoints:
- [Create Payment Intent](https://stripe.com/docs/api/payment_intents/create)
- [Confirm Payment](https://stripe.com/docs/api/payment_intents/confirm)
```

Developers can click directly to the relevant API docs instead of searching.

**Scenario 3: Reference Design Patterns**

```markdown
## Task State Management

Implement using [State Pattern](https://refactoring.guru/design-patterns/state).

States:
- Created (initial)
- In Progress
- Completed
- Archived

State transitions follow pattern described in [Gang of Four documentation](https://en.wikipedia.org/wiki/State_pattern).
```

Links provide context and learning resources.

---

## Concept 2: Images for Diagrams and Examples

Markdown images use similar syntax: `![alt text](image URL)`

### Basic Image Syntax

```markdown
![Task workflow diagram](https://example.com/images/task-workflow.png)
```

**What this shows**:
- Image displayed inline
- Alt text: "Task workflow diagram" (for accessibility and if image fails to load)
- Image source: URL or relative path

### When to Use Images in Specifications

**Scenario 1: Show User Interface Mockups**

```markdown
## Login Screen Design

![Login screen mockup](./mockups/login-screen.png)

Required elements:
- Email input field
- Password input field (masked)
- "Remember me" checkbox
- "Forgot password?" link
- "Login" button

Layout matches mockup above.
```

**Why this helps**: Visual reference removes ambiguity about UI layout.

**Scenario 2: Show System Architecture**

```markdown
## System Architecture

![Architecture diagram](./diagrams/system-architecture.png)

Components:
- Frontend (React)
- API Gateway (Node.js)
- Task Service (Python)
- Database (PostgreSQL)

Data flow shown in diagram above.
```

One diagram explains relationships better than paragraphs of text.

**Scenario 3: Show Expected Output (Screenshot)**

```markdown
## Dashboard View

![Dashboard screenshot](./screenshots/dashboard-example.png)

User sees:
- Welcome message with name
- Today's tasks (left panel)
- This week's progress (right panel)
- Quick action buttons (bottom)

Visual layout matches screenshot.
```

Screenshot sets clear expectations for developers and designers.

---

## Recognizing Patterns: From Lessons 1-3

Before creating a reusable template, let's identify patterns from what you've learned.

**Reflection Question 1**: What structure did ALL your feature specifications have?

Think about Lessons 1-3. When you specified features, you included:
- Feature name (heading)
- What it does (description)
- What inputs it needs
- What outputs it produces
- What edge cases to handle

**This is a repeatable pattern.**

**Reflection Question 2**: What questions did you ALWAYS ask yourself?

When writing specifications, you asked:
- What is this feature's purpose?
- What does the user provide?
- What does the system return?
- What can go wrong?
- How do I know it works?

**These questions guide every specification.**

**Reflection Question 3**: What principles helped you decide what to include?

You learned principles like:
- Be specific (not vague)
- Show WHAT, not HOW
- Handle edge cases
- Reference authoritative sources
- Make it measurable

**These principles apply to every feature.**

---

## Concept 3: Creating Reusable Specification Templates

Now that you recognize patterns, encode them as a **reusable template**.

**Template structure**:
1. **Persona**: Establishes thinking stance ("Think like X to achieve Y")
2. **Analysis Questions**: Force reasoning about the feature
3. **Principles**: Guide decisions
4. **Template**: Reusable structure to fill in

### Feature Specification Template (Example)

```markdown
# Feature Specification Template

## Persona
"Think like a requirements engineer ensuring any developer could implement this feature unambiguously from the specification alone."

## Analysis Questions

Before writing specification, answer:

1. **What is this feature doing?**
   - One clear sentence describing purpose
   - Why does the user need this?

2. **What inputs does the user provide?**
   - Required vs optional
   - Data types and formats
   - Validation rules

3. **What outputs does the system produce?**
   - Success case: What does user see?
   - Data returned: What information is shown?

4. **What edge cases exist?**
   - Empty inputs
   - Invalid inputs
   - System failures
   - Boundary conditions

5. **How do we validate success?**
   - Measurable criteria
   - Observable behavior
   - Time constraints

## Principles

When writing feature specifications:

1. **Unambiguous Intent**: Any developer reading this knows exactly what to build
2. **Complete Scope**: Nothing left to assumptions
3. **Edge Case Coverage**: Handle failures gracefully
4. **Reference Authority**: Link to standards, patterns, documentation
5. **Measurable Success**: Clear validation criteria

## Template Structure

Use this structure for any feature:

---

### [Feature Name]

**Purpose**: [One sentence: what does this feature do and why?]

**References**:
- [Link to relevant standard/pattern/documentation]

#### Inputs

**Required:**
- [Input 1 name] (type, constraints)
- [Input 2 name] (type, constraints)

**Optional:**
- [Optional input] (type, default value)

#### Expected Output (Success Case)

**System displays:**
```
[Exact output text/format]
```

**System returns:**
```
[API response or data structure]
```

#### Edge Cases

**If [condition 1]:**
```
[Error message or handling behavior]
```

**If [condition 2]:**
```
[Error message or handling behavior]
```

#### Success Criteria

- ✅ [Measurable criterion 1]
- ✅ [Measurable criterion 2]
- ✅ [Measurable criterion 3]

---
```

**What makes this template reusable**:
- **Persona** activates the right mindset (not just copying structure)
- **Questions** force analysis of the specific feature (not generic)
- **Principles** guide decisions when filling template
- **Template** provides consistent structure across all features

---

## Concept 4: Applying Template to Novel Feature

Let's test the template on a feature you haven't specified before: **Delete Task**.

**Before template**: You might write:
```
## Delete Task
User can remove tasks they don't need anymore.
```

Vague. What confirms deletion? What if task doesn't exist? What if it's already deleted?

**Using template**:

### Step 1: Answer Analysis Questions

1. **What is this feature doing?**
   - Permanently removes task from system
   - User needs this to clean up completed or obsolete tasks

2. **What inputs does user provide?**
   - Required: Task ID (integer)

3. **What outputs does system produce?**
   - Success: Confirmation message, task removed from list
   - Failure: Error if task not found

4. **What edge cases exist?**
   - Task ID doesn't exist
   - Task ID is invalid format (not a number)
   - User tries to delete already-deleted task

5. **How do we validate success?**
   - Task no longer appears in task list
   - Confirmation message appears within 1 second
   - Task count decrements by 1

### Step 2: Fill Template Structure

```markdown
### Delete Task

**Purpose**: Permanently remove task from system when user no longer needs it.

**References**:
- [Delete operation patterns](https://restfulapi.net/http-methods/#delete)
- [User confirmation best practices](https://uxplanet.org/confirmation-dialogs-in-ui-design)

#### Inputs

**Required:**
- Task ID (integer, must exist in system)

#### Expected Output (Success Case)

**System displays:**
```
Task deleted successfully.
"[Task name]" has been removed.

Remaining tasks: 4
```

**System behavior:**
- Task removed from database
- Task no longer appears in task list
- Task count updated

#### Edge Cases

**If task ID doesn't exist:**
```
Error: Task not found
Unable to delete task #42. This task does not exist.
Please check the task ID and try again.
```

**If task ID invalid format (not a number):**
```
Error: Invalid task ID
Task ID must be a number.
Example: 42
```

**If delete operation fails:**
```
Error: Unable to delete task
System error occurred. Please try again.
If problem persists, contact support.
```

#### Success Criteria

- ✅ Task deletion completes within 1 second
- ✅ Task no longer appears in list after deletion
- ✅ Task count decrements correctly
- ✅ Confirmation message includes deleted task name
- ✅ Error messages clear and actionable
```

**Notice**:
- You didn't refer back to Lessons 1-3
- Template guided you to complete specification
- All sections filled systematically
- Nothing missing

**This is intelligence reuse**: Template encodes knowledge from past work, applies to new scenarios.

---

## Concept 5: Template Quality Criteria

Not all templates are equally useful. Good templates:

**1. Activate Reasoning (Not Just Structure)**

❌ Bad template:
```
## [Feature Name]
Description: [...]
Requirements: [...]
```

This is just structure. Doesn't help you think through the problem.

✅ Good template:
```
## Persona
"Think like [role] ensuring [outcome]"

## Questions
1. What problem does this solve?
2. What constraints apply?
...
```

This activates analysis. You can't fill it mindlessly.

**2. Apply to 3+ Different Features (General, Not Specific)**

❌ Over-specific template:
```
## User Authentication Feature
OAuth provider: [Google/GitHub]
Redirect URL: [...]
Scope: [email, profile]
```

This only works for OAuth. Not reusable for password auth, API keys, etc.

✅ General template:
```
## Authentication Feature
Method: [OAuth / Password / API Key / SSO]
Security requirements: [...]
Success criteria: [...]
```

Applies to any authentication approach.

**3. Include Decision Frameworks (Principles)**

❌ No guidance:
```
## Feature Specification
Name: [...]
Description: [...]
```

You're on your own deciding what to include.

✅ With principles:
```
## Principles
1. Unambiguous Intent: Could any developer implement from this spec?
2. Edge Case Coverage: What can go wrong?
3. Measurable Success: How do we validate?
```

Principles guide what you write.

---

## Practice Exercise: Create Your Own Template

Now create a reusable template for a different context. Choose ONE:

**Option 1: Error Message Template**
- Create template for specifying any error message
- Include: when it appears, exact text, user actions, recovery steps

**Option 2: API Endpoint Template**
- Create template for specifying any API endpoint
- Include: method, path, request format, response format, status codes

**Option 3: User Story Template**
- Create template for writing user stories
- Include: who, what, why, acceptance criteria, edge cases

### Instructions

1. Open text editor
2. Create file: `my-template.md`
3. Structure:

```markdown
# [Your Template Name]

## Persona
"Think like [role] to ensure [outcome]"

## Analysis Questions

Before using this template, answer:

1. [Question that forces context analysis]
2. [Question that identifies constraints]
3. [Question that surfaces edge cases]
4. [Question that defines success]

## Principles

When using this template:

1. [Principle 1: what quality to ensure]
2. [Principle 2: what to avoid]
3. [Principle 3: what to reference]

## Template

[Your reusable structure here with placeholders]
```

4. Test by applying to two different scenarios
5. Refine if template doesn't work for both

### Success Criteria

**You succeed when**:
- ✅ Template includes Persona + Questions + Principles
- ✅ Template applies to 3+ different scenarios (not over-specific)
- ✅ Questions force reasoning (not just fill-in-the-blank)
- ✅ Principles guide decisions
- ✅ You can use template without referring back to this lesson

---

## Try With AI

Ready to create reusable templates and strengthen specifications with references?

**🔍 Explore Links and Images Impact:**
> "Show me two versions of an API specification: (1) without links or images, and (2) with links to documentation and a diagram showing request/response flow. Explain how links and images improve specification clarity."

**🎯 Practice Template Design:**
> "I'm creating a reusable template for [your chosen domain from practice exercise]: [paste your template]. Ask me questions to refine it: Is the Persona clear and actionable? Do the Questions force analysis (not just fill-in-blanks)? Are Principles decision-guiding? Is this general enough for 3+ scenarios?"

**🧪 Test Template Reusability:**
> "Use this template to specify three different scenarios: [scenario 1], [scenario 2], [scenario 3]. [Paste your template]. Identify any sections that don't work for all scenarios, questions that are unclear, or principles that don't guide decisions."

**🚀 Apply to Your Domain:**
> "Help me create a reusable Feature Specification Template for [your actual work domain]. Guide me through designing Persona (thinking stance), Questions (force analysis of context/constraints/edge cases), and Principles (decision frameworks). Challenge me if any part is too vague or too specific."

---
