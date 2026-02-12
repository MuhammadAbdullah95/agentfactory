### Core Concept
The Bronze Capstone integrates everything: an orchestrator skill that coordinates your email-drafter, email-templates, and email-summarizer skills with Gmail MCP to create a complete email assistant. This proves you can build production-ready AI Employee workflows.

### Key Mental Models
- **Orchestration Pattern**: One skill/agent coordinates multiple specialists based on task requirements
- **Integration Testing**: Real email access + real skills + real use case = production validation
- **Capability Stack**: Individual skills combine into compound capabilities greater than the sum

### Critical Patterns
- Orchestrator skill structure: Recognizes intent → selects specialist → invokes with context → formats response
- Email workflow: Triage (summarizer) → Draft response (drafter + templates) → Review → Send
- Error handling: Graceful fallbacks when specialists fail or Gmail is unavailable
- Complete test cycle: Real email in → AI processes → Real action out

### Common Mistakes
- Testing orchestration without first verifying each component skill works
- Not documenting which skills the orchestrator depends on
- Skipping the "review before send" step in email workflows
- Treating the capstone as "done" rather than a foundation to build on

### Connections
- **Builds on**: All Part C skills (Lessons 6-10)
- **Leads to**: Proactive monitoring with watchers (Lesson 12)
