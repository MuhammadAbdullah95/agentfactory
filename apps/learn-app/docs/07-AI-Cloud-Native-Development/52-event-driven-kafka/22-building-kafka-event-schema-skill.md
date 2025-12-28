---
sidebar_position: 22
title: "Building the Kafka Event Schema Skill"
description: "Transform event schema design patterns from this chapter into a reusable skill for future event-driven projects"
keywords: [kafka, event schema, skill, avro, schema registry, event naming, reusable intelligence, SKILL.md]
chapter: 52
lesson: 22
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "Pattern Extraction for Reusable Skills"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Identify recurring patterns across lessons 10-21 and extract them into skill components"
  - name: "SKILL.md Design"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Create complete SKILL.md with frontmatter, persona, questions, and principles"
  - name: "Skill Validation Through Novel Application"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Test skill on new domain (not Task API) and refine based on gaps discovered"

learning_objectives:
  - objective: "Extract reusable event schema design patterns from chapter learnings into a skill specification"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Skill file creation with patterns from lessons 10, 16, 17, 21"
  - objective: "Design a skill with clear persona, triggering questions, and decision principles"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "SKILL.md file structure validation against creating-skills requirements"
  - objective: "Test the skill on a novel domain (non-Task API) to verify reusability"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Apply skill to e-commerce order events and identify gaps"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (skill extraction, persona design, question structure, principle articulation, frontmatter, validation) within B1 limit. Builds on all previous lessons as prerequisite knowledge."

differentiation:
  extension_for_advanced: "Create multiple skills: event-schema-design, event-naming-conventions, schema-evolution-strategy as separate focused skills"
  remedial_for_struggling: "Focus on persona + 2 questions + 1 principle; expand after validation"
---

# Building the Kafka Event Schema Skill

Throughout lessons 10-21, you've designed Avro schemas for task events, integrated Schema Registry for validation, implemented delivery semantics, and built saga patterns for multi-step workflows. Each lesson solved immediate problems. But the decision frameworks you used---how to name events, what metadata to include, when to evolve schemas---recur across every event-driven project.

This lesson guides you to extract that recurring knowledge into a reusable skill. Three months from now, when you're designing events for an e-commerce system, a notification platform, or an IoT data pipeline, you'll reference this skill instead of rediscovering the same principles. And unlike copying code from lesson 16, a skill captures the *reasoning* behind decisions, making it applicable to contexts you haven't encountered yet.

This is Layer 3: Intelligence Design. You're not just using AI to solve problems (Layer 2). You're encoding your accumulated expertise into a format that makes future projects faster and more reliable.

---

## From Embedded Knowledge to Reusable Intelligence

Your capstone (Lesson 21) created working event-driven notifications for the Task API. The schemas you designed, the naming conventions you chose, the metadata patterns you applied---all embedded in one project.

If you build a second event-driven system next month, you'll face the same decisions:

- "What should I name this event? `order.created` or `OrderCreated`?"
- "What metadata fields does every event need?"
- "How do I evolve schemas without breaking consumers?"
- "Should I use one topic per event type or aggregate events?"

A skill captures these decisions in a format that guides thinking, not just provides answers.

### What Makes Event Schema Patterns Worth Extracting?

Apply the three-test framework:

**1. Frequency**: Does this pattern recur across projects?

Your event schema patterns: Yes. Every event-driven system---whether task management, e-commerce, IoT, or financial services---needs consistent event naming, schema design, and evolution strategies.

**2. Complexity**: Does the pattern involve enough decision points to justify documentation?

Event schema design: Yes. Naming conventions, required fields, optional fields, metadata, versioning, topic organization---each involves tradeoffs that experienced practitioners understand but newcomers struggle with.

**3. Organizational value**: Would multiple teams benefit from this guidance?

Event schemas: Yes. Data teams, backend teams, analytics teams, and ML teams all consume events. Consistent schemas reduce integration friction across the organization.

Your event schema patterns pass all three tests. Extract them into a skill.

---

## Skill Anatomy: Persona + Questions + Principles

A well-designed skill activates reasoning, not pattern retrieval. It accomplishes this through three components working together.

### Component 1: Persona

The persona defines the thinking stance that activates appropriate reasoning. Instead of generic expertise claims, a strong persona forces specific analytical thinking.

**Weak persona** (activates generic mode):
```
You are an expert in Kafka event schemas.
```

**Strong persona** (activates specific reasoning):
```
Think like a data architect designing event contracts for a system where
producers and consumers evolve independently. Your goal: events that remain
compatible as requirements change, that provide enough context for any
consumer, and that enable debugging when things go wrong. Your constraints:
multiple teams consuming the same events, consumers you don't control,
schemas that must evolve over years.
```

The strong persona activates multiple decision frameworks simultaneously: compatibility, context sufficiency, debuggability, long-term evolution.

### Component 2: Questions

Questions structure the analysis that forces context-specific reasoning. Instead of yes/no questions, strong questions require analysis.

**Weak question** (retrieves memorized answer):
```
Should I use Avro for my schemas?
```

**Strong questions** (force context analysis):
```
- What happens when a producer adds a new field that some consumers don't
  understand? (Compatibility implications)
- What information would you need to debug an event that caused a downstream
  failure three hours ago? (Metadata requirements)
- If a consumer needs to process events from six months ago, what schema
  version should they use? (Evolution strategy)
```

Each question forces the user to analyze their specific context before making a decision.

### Component 3: Principles

Principles articulate the decision frameworks that guide application. Instead of prescriptive rules, strong principles explain the reasoning.

**Weak principle** (prescriptive rule):
```
Always include event_id, event_type, and occurred_at in every event.
```

**Strong principle** (decision framework):
```
**Principle: Events are forensic records**

Every event must answer: What happened? When? Why? Who caused it? What was
the state before and after?

Required fields emerge from forensic needs:
- event_id: Deduplicate and trace across systems
- event_type: Route without parsing payload
- occurred_at: Order events, debug timing issues
- correlation_id: Trace across service boundaries
- causation_id: Understand what triggered this event

Optional fields depend on domain:
- actor_id: Who initiated the action (if applicable)
- version: Schema version for compatibility
- source: Which service produced the event

Decision framework: If you can't debug a production issue using only event
data, your metadata is insufficient.
```

The principle explains *why* these fields matter, enabling users to make informed decisions about their specific context.

---

## Extracting Patterns from This Chapter

Let's identify the event schema patterns you've learned across lessons 10-21.

### Pattern 1: Event Naming Conventions (Lessons 10, 16)

From your Task API work:
- Events use `domain.action` format: `task.created`, `task.completed`
- Past tense for actions that happened: `created` not `create`
- Lowercase with dots: `task.created` not `TaskCreated` or `task_created`

**Why this pattern matters**: Consistent naming enables routing without parsing payloads. A consumer subscribing to `task.*` gets all task events. A consumer subscribed to `*.created` gets all creation events across domains.

### Pattern 2: Schema Structure (Lessons 10, 16, 21)

Your event schemas followed a consistent structure:

```json
{
  "event_id": "uuid",
  "event_type": "domain.action",
  "occurred_at": "ISO-8601 timestamp",
  "data": {
    "domain-specific fields"
  },
  "metadata": {
    "correlation_id": "uuid",
    "causation_id": "uuid",
    "source": "service-name"
  }
}
```

**Why this pattern matters**: Separating `data` (domain-specific) from `metadata` (system-specific) enables generic event handling. A logging service processes `metadata` without understanding `data`. A domain service processes `data` without caring about `metadata`.

### Pattern 3: Schema Evolution Strategy (Lesson 10)

You learned compatibility types:
- **Backward compatible**: New schema can read old data (add optional fields with defaults)
- **Forward compatible**: Old schema can read new data (ignore unknown fields)
- **Full compatible**: Both directions work

**Decision framework from experience**: Default to backward compatibility. Add fields as optional with defaults. Never remove required fields. Never change field types.

### Pattern 4: Topic Organization (Lessons 16, 17)

You considered two approaches:
- **Single topic per domain**: `task-events` with all task events
- **Topic per event type**: `task-created`, `task-completed`, `task-deleted`

**Decision framework from experience**: Single topic when consumers need all events in order. Separate topics when consumers subscribe to specific event types and order across types doesn't matter.

### Pattern 5: Transactional Integrity (Lessons 12, 15, 17)

For atomic operations:
- Outbox pattern: Write to database and outbox table in same transaction
- Debezium reads outbox, produces to Kafka
- Saga pattern: Choreographed events with compensation

**Decision framework from experience**: When database write and event publish must be atomic, use outbox. When multiple services must coordinate, use saga with compensation events.

---

## Building Your Skill: Step-by-Step

You'll create a skill file that captures event schema patterns from this chapter. The skill lives in:

```
.claude/skills/kafka-event-schema/SKILL.md
```

### Step 1: Define Your Frontmatter

The frontmatter determines when the skill triggers. Focus on *triggering conditions*, not process description.

```yaml
---
name: kafka-event-schema
description: |
  Use when designing event schemas for Kafka or event-driven systems.
  Triggers include: event naming, Avro schema design, Schema Registry
  integration, schema evolution, topic organization for events.
  NOT when designing general data schemas or API request/response formats
  (use api-schema-design skill for those).
---
```

**Why this description works**: It specifies when to trigger (event schemas, Kafka) and when NOT to trigger (API schemas). Claude uses this to decide whether to load the full skill.

### Step 2: Write Your Persona

Capture the thinking stance you used throughout this chapter:

```markdown
## Persona

Think like a data architect designing event contracts for an event-driven
system where:
- Multiple teams produce and consume events independently
- Consumers you don't control will process your events
- Schemas must evolve over years without breaking downstream systems
- Production debugging relies entirely on event data

Your goals:
- Events that enable forensic debugging when things go wrong
- Schemas that evolve without breaking existing consumers
- Naming that enables routing without payload inspection
- Metadata that traces requests across service boundaries
```

### Step 3: Structure Your Decision Points

Organize questions around the decisions someone designing event schemas would face:

```markdown
## Decision Points

### Decision 1: Event Naming

**Analysis questions:**
- What domain does this event belong to? (task, order, user, payment)
- What action occurred? (created, updated, completed, failed)
- Will consumers need to subscribe to patterns? (all task events, all created events)

### Decision 2: Required Metadata

**Analysis questions:**
- What would you need to debug an event that caused a failure 3 hours ago?
- How will you trace this event's journey across service boundaries?
- What caused this event to be produced? (user action, system process, another event)

### Decision 3: Schema Structure

**Analysis questions:**
- Which fields are domain-specific (what happened to the task)?
- Which fields are system-specific (correlation, timing, source)?
- How would a generic logging service process this event?

### Decision 4: Evolution Strategy

**Analysis questions:**
- What happens when you add a new field?
- What happens when a consumer doesn't understand a new field?
- How do old events get processed by new consumer code?

### Decision 5: Topic Organization

**Analysis questions:**
- Do consumers need all events from this domain in order?
- Can consumers subscribe to specific event types independently?
- How many event types exist in this domain?
```

### Step 4: Articulate Your Principles

Write the decision frameworks that guide application:

```markdown
## Principles

### Principle 1: Events Are Forensic Records

Every event must answer: What happened? When? Why? Who caused it?

Required fields emerge from forensic needs:
- `event_id`: Deduplicate and trace across systems
- `event_type`: Route without parsing payload
- `occurred_at`: Order events, debug timing issues
- `correlation_id`: Trace request across service boundaries
- `causation_id`: Understand what triggered this event

**Decision test**: If you can't debug a production issue using only event
data, your metadata is insufficient.

### Principle 2: Naming Enables Routing

Use `domain.action` format with past tense:
- `task.created`, `order.completed`, `payment.failed`
- Lowercase, dot-separated

This enables pattern subscriptions:
- `task.*`: All task events
- `*.created`: All creation events across domains

**Decision test**: Can a consumer subscribe to events by pattern without
understanding payload structure?

### Principle 3: Separate Data from Metadata

Structure events with clear separation:
```json
{
  "event_id": "...",
  "event_type": "...",
  "occurred_at": "...",
  "data": { /* domain-specific */ },
  "metadata": { /* system-specific */ }
}
```

This enables:
- Generic event processing (logging, auditing) without domain knowledge
- Domain processing without caring about infrastructure concerns

### Principle 4: Backward Compatibility by Default

Evolution rules:
- Add fields as optional with defaults
- Never remove required fields
- Never change field types
- Use Schema Registry to enforce compatibility

**Decision test**: Can a consumer running code from 6 months ago process
today's events without crashing?

### Principle 5: Topic Granularity Follows Subscription Patterns

- **Single topic**: When consumers need all domain events in order
- **Per-event-type topics**: When consumers subscribe to specific types independently

**Decision test**: Will most consumers ignore most events in this topic?
If yes, split topics.
```

### Step 5: Add Common Patterns Section

Include patterns you encountered repeatedly:

```markdown
## Common Patterns

### Pattern: Task Lifecycle Events

```json
{
  "event_type": "task.created",
  "data": {
    "task_id": "uuid",
    "title": "string",
    "owner_id": "uuid"
  }
}
```

### Pattern: Saga Compensation Events

When saga step fails, emit compensation:
- `task.assignment.reversed`
- `user.notification.cancelled`

Compensation events restore previous state, enabling eventual consistency.

### Pattern: Outbox for Atomic Operations

When database write and event must be atomic:
1. Write domain data to main table
2. Write event to `outbox` table in same transaction
3. CDC (Debezium) reads outbox, produces to Kafka
4. Outbox row deleted after successful produce
```

### Step 6: Create the Complete Skill File

Create the directory and file:

```bash
mkdir -p .claude/skills/kafka-event-schema
```

Write the complete SKILL.md combining all sections:

```markdown
---
name: kafka-event-schema
description: |
  Use when designing event schemas for Kafka or event-driven systems.
  Triggers include: event naming, Avro schema design, Schema Registry
  integration, schema evolution, topic organization for events.
  NOT when designing general data schemas or API request/response formats.
---

# Kafka Event Schema Design

## Persona

Think like a data architect designing event contracts for an event-driven
system where:
- Multiple teams produce and consume events independently
- Consumers you don't control will process your events
- Schemas must evolve over years without breaking downstream systems
- Production debugging relies entirely on event data

Your goals:
- Events that enable forensic debugging when things go wrong
- Schemas that evolve without breaking existing consumers
- Naming that enables routing without payload inspection
- Metadata that traces requests across service boundaries

## Decision Points

### Decision 1: Event Naming
[Analysis questions from Step 3]

### Decision 2: Required Metadata
[Analysis questions from Step 3]

### Decision 3: Schema Structure
[Analysis questions from Step 3]

### Decision 4: Evolution Strategy
[Analysis questions from Step 3]

### Decision 5: Topic Organization
[Analysis questions from Step 3]

## Principles

[Principles from Step 4]

## Common Patterns

[Patterns from Step 5]

## Avro Schema Template

```json
{
  "type": "record",
  "name": "DomainEvent",
  "namespace": "com.example.events",
  "fields": [
    {"name": "event_id", "type": "string"},
    {"name": "event_type", "type": "string"},
    {"name": "occurred_at", "type": "string"},
    {"name": "data", "type": ["null", "record"], "default": null},
    {"name": "metadata", "type": {
      "type": "record",
      "name": "EventMetadata",
      "fields": [
        {"name": "correlation_id", "type": ["null", "string"], "default": null},
        {"name": "causation_id", "type": ["null", "string"], "default": null},
        {"name": "source", "type": ["null", "string"], "default": null}
      ]
    }}
  ]
}
```
```

---

## Testing Your Skill: Apply to a Novel Domain

Creating the skill is half the work. The other half is validating that it guides thinking for a *different* system---one you haven't designed events for yet.

Your skill emerged from Task API patterns. Now test it on e-commerce order events.

### The Test Scenario: E-Commerce Order System

Imagine you're designing events for an order management system:

- Orders are created when customers checkout
- Orders transition through states: pending, paid, shipped, delivered, cancelled
- Multiple services consume order events: inventory, shipping, notifications, analytics
- Orders can be partially fulfilled (some items shipped, others backordered)

This is different enough from Task API that you can't just copy schemas.

### Work Through Your Skill

Using only your skill (not Task API examples), design:

**1. Event Naming**

Apply Decision Point 1. What names for order events?

- `order.created` (checkout complete)
- `order.paid` (payment confirmed)
- `order.shipped` (items dispatched)
- `order.delivered` (customer received)
- `order.cancelled` (order terminated)

Does your skill's naming principle work? Yes---`domain.action` format enables `order.*` subscriptions.

**2. Schema Structure**

Apply Decision Point 3. What's in `data` vs `metadata`?

```json
{
  "event_id": "uuid",
  "event_type": "order.created",
  "occurred_at": "2025-01-15T10:30:00Z",
  "data": {
    "order_id": "uuid",
    "customer_id": "uuid",
    "items": [...],
    "total_amount": 99.99,
    "currency": "USD"
  },
  "metadata": {
    "correlation_id": "uuid",
    "causation_id": "uuid",
    "source": "checkout-service"
  }
}
```

Does your skill's separation principle work? Yes---a logging service can process this without understanding order data.

**3. Evolution Strategy**

Apply Decision Point 4. Later you need to add `shipping_address` to `order.created`.

Following your skill's backward compatibility principle:
- Add `shipping_address` as optional with default null
- Old consumers ignore the new field
- New consumers check for null before using

Does the principle guide correctly? Yes---no breaking changes.

**4. Gaps Discovered**

Working through the order system, you might discover gaps in your skill:

- **Partial fulfillment**: How do you represent `order.partially_shipped`? Your skill doesn't address compound states.
- **Event sequencing**: What ensures `order.shipped` comes after `order.paid`? Your skill doesn't address ordering guarantees.
- **Aggregate events**: Should `order.updated` capture all state changes, or should each transition be a separate event?

These gaps become improvements for your skill.

---

## Integrating Your Skill into Claude Code

Once validated, integrate the skill for future use:

### Step 1: Place the Skill

```bash
# Your skill location
.claude/skills/kafka-event-schema/SKILL.md
```

### Step 2: Verify Skill Loads

In a new conversation, mention event schemas:

```
I'm designing Kafka events for an IoT sensor data pipeline. Help me
structure the event schema.
```

If your skill is correctly structured, Claude references it when designing schemas.

### Step 3: Iterate Based on Use

As you use the skill on real projects:
- Add patterns you discover
- Refine questions that didn't guide well
- Expand principles for edge cases
- Remove guidance that was too prescriptive

Your skill compounds over time, becoming more valuable with each project.

---

## The Broader Value: Intelligence Accumulation

Why create this skill instead of just remembering Lesson 10's patterns?

**Lesson 10 embedded knowledge in one project.** Your Avro schemas for task events worked, but the decision frameworks were context-specific.

**Your skill crystallizes knowledge for reuse.** Six months from now, when you're designing events for a different system, you reference this skill instead of rediscovering principles.

**And the skill compounds.** As you design more event-driven systems, you encounter variations and edge cases. You add them to the skill. Your teammates reference it. The skill becomes a shared reference for event schema decisions across the organization.

This is intelligence accumulation. Not "I know how to write Avro schemas" (too specific). Not "I'm good at Kafka" (vague). But "I have a guidance framework for designing ANY event schema for event-driven systems" (reusable, continuously improving).

That's the value of Layer 3 intelligence design.

---

## Try With AI

**Setup**: You have your Kafka event schema skill created. Now use AI to validate and improve it.

### Prompt 1: Skill Review

```
I've created a Kafka event schema design skill for designing events in
event-driven systems. Here's my skill:

[Paste your complete SKILL.md file]

Review my skill and identify:
- Which decision points are well-guided?
- What decisions are missing or unclear?
- Where are principles too prescriptive (like rules) vs appropriately
  general (like frameworks)?
- How would someone designing events for a new domain use this skill?
```

**What you're learning**: External validation reveals blind spots. Claude identifies gaps you didn't notice because you were too close to the material.

### Prompt 2: Apply to Novel Domain

```
Using the event schema skill I shared, guide me through designing events
for an IoT sensor monitoring system:
- Sensors report temperature, humidity, and pressure every 30 seconds
- Alerts fire when readings exceed thresholds
- Historical data is stored for trend analysis
- Multiple systems consume sensor data: dashboards, alerting, ML training

Walk through each decision point in the skill. Where does it guide clearly?
Where is it unclear for IoT-specific concerns?
```

**What you're learning**: Novel domains reveal whether your skill is truly reusable or just a Task API summary. IoT events have different patterns (high volume, time-series, aggregation) that test your skill's generality.

### Prompt 3: Identify Production Gaps

```
I created an event schema design skill based on a course chapter. My skill
addresses:
- Event naming conventions
- Required metadata fields
- Schema structure (data vs metadata separation)
- Evolution strategy
- Topic organization

Looking at production event-driven systems, what critical patterns am I
missing? What decisions would a production architect make that my skill
doesn't address?
```

**What you're learning**: Production systems have concerns your skill might miss: event compression, partition key selection, dead letter handling for malformed events, schema validation at producer vs consumer.

**Safety Note:** Skills guide thinking, not prescribe answers. When applying your skill to new domains, verify that the patterns actually fit your specific requirements. IoT systems, financial systems, and task management systems have different constraints---adapt the principles accordingly.
