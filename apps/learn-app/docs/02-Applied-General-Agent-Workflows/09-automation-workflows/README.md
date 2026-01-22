---
sidebar_position: 9
title: "Chapter 9: Automation & Recurring Workflows"
---

# Chapter 9: Automation & Recurring Workflows

Every week, you do the same things: update a spreadsheet, send status emails, organize downloads, back up important files, check for updates. Each task is small — five minutes here, ten minutes there. But they add up to hours of repetitive work that never produces new value.

**The problem isn't that these tasks are hard. It's that they're endless.**

This chapter teaches you to identify recurring patterns in your work and automate them using your General Agent. You'll move from one-off prompts to scheduled, repeatable workflows that run without your attention.

## Principles Applied

| Principle | How It Applies |
|-----------|---------------|
| **Bash is the Key** | Scheduling (cron), process management, file watching |
| **Small, Reversible Decomposition** | Break complex workflows into testable steps |
| **Constraints and Safety** | Rate limits, error handling, human-in-the-loop gates |
| **Verification as Core Step** | Confirm each automation step succeeded before proceeding |
| **Observability** | Logging, notifications, audit trails for automated actions |

## Interface Focus

**Primary**: Code (automation requires precise, repeatable instructions)
**Secondary**: Cowork (for designing and debugging workflows)

## What You'll Learn

By the end of this chapter, you'll be able to:

- Identify tasks suitable for automation (recurring, predictable, low-risk)
- Design multi-step workflows with error handling and recovery
- Schedule tasks to run automatically (cron, watchers, triggers)
- Add human-in-the-loop approval for sensitive automated actions
- Monitor automated workflows and handle failures gracefully
- Build a library of reusable automation patterns

## Lesson Outline

| Lesson | Title | Focus |
|--------|-------|-------|
| L01 | Spotting Automation Opportunities | Identifying recurring patterns worth automating |
| L02 | Your First Scheduled Task | cron basics, running scripts on schedule |
| L03 | File Watchers & Triggers | Reacting to filesystem changes automatically |
| L04 | Multi-Step Workflows | Chaining operations with error handling |
| L05 | Human-in-the-Loop Gates | Adding approval steps for sensitive actions |
| L06 | Monitoring & Recovery | Logging, notifications, failure handling |
| L07 | Automation Capstone | End-to-end automated workflow for a real use case |

## Connection to AI Employee (Chapter 10)

The automation patterns you build here become the nervous system of your AI Employee. In Chapter 10, these techniques enable:

- Always-on operation via PM2 and process management
- Gmail/File watchers that trigger your employee autonomously
- Scheduled weekly audits that produce the CEO Briefing
- Error recovery and graceful degradation under failures

**Automation is what transforms your AI Employee from reactive assistant to proactive worker.**
