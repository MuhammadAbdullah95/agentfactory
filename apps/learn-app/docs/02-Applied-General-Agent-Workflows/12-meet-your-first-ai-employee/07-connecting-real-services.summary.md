### Core Concept

Hooks transform your AI Employee from reactive (waits for commands) to proactive (monitors and alerts). Gmail webhooks using Pub/Sub deliver real-time notifications when emails arrive—your employee wakes instantly and can summarize, triage, or alert you without being asked.

### Key Mental Models

- **Reactive vs Proactive**: Reactive = you ask, it responds; Proactive = events trigger automatic action
- **Push vs Poll**: Pub/Sub pushes notifications instantly; polling would check periodically (slower, more resource-intensive)
- **External Content Safety**: Email content can contain malicious instructions; OpenClaw wraps it with safety boundaries by default

### Critical Patterns

- **gog prerequisite**: Install and authenticate gog (Google CLI) before Gmail hooks — `gog auth credentials` then `gog auth add --account your@gmail.com`
- Setup wizard: `openclaw webhooks gmail setup --account your@gmail.com`
- Hook mapping: `match`, `action`, `messageTemplate`, `deliver`, `channel` fields
- Cost control: Set `hooks.gmail.model` to use cheaper model for hook processing
- Start/stop: `openclaw webhooks gmail run` / `openclaw webhooks gmail stop`

### Common Mistakes

- Disabling external content safety (`allowUnsafeExternalContent: true` is dangerous)
- Using expensive models for high-volume hook processing
- Not testing hooks before going live (send yourself test emails first)
- Configuring auto-response without HITL approval (covered in Lesson 8)

### Connections

- **Builds on**: Employee memory and skills (Lessons 5-6)
- **Leads to**: Human-in-the-loop approval (Lesson 8)
