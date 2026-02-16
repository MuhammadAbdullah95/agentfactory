---
title: "Summary: Your First Real Work"
sidebar_label: "Summary"
sidebar_position: 3.5
---

# Summary: Your First Real Work

## Key Concepts
- **Task Delegation**: Give one natural language instruction; the agent decomposes it into subtasks automatically
- **Agent Loop**: The universal 4-phase cycle every agent system implements -- identical across OpenClaw, Claude Code, CrewAI, and others
- **Output Quality Assessment**: AI Employees excel at information-heavy, structure-dependent, repeatable tasks; they struggle with real-time data, subjective judgment, and genuine creativity
- **Token Costs**: Roughly 4 characters per token; a research task costs ~$0.05-$0.25 while a simple question costs ~$0.005-$0.02
- **Multi-Step Workflows**: One instruction can trigger a chain of operations (research, write, save, analyze) that the agent sequences automatically

## The Agent Loop
1. **Parse Intent** -- Understand the natural language instruction and resolve ambiguity with reasonable defaults
2. **Plan Execution** -- Decide what to do and in what order before producing output
3. **Execute Steps** -- Call tools (web search, file creation, file reading) as needed per the plan
4. **Report Results** -- Format output for the user based on context (tables, checklists, prose)

## Common Mistakes
- Expecting real-time data without verifying the model's knowledge cutoff
- Delegating highly subjective decisions that require personal values or organizational context
- Sending one massive instruction instead of breaking long workflows into checkable steps
- Judging AI capability from marketing claims instead of firsthand experience

## Quick Reference

| Works Well | Struggles With |
|---|---|
| Research and summarization | Tasks requiring real-time data |
| Professional writing with tone control | Highly subjective decisions |
| File creation and management | Unconfigured external services |
| Structured analysis and ranking | Very long, complex workflows |
| Multi-step research-to-report pipelines | Creative work requiring originality |
