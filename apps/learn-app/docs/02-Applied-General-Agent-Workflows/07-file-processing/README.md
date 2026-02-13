---
sidebar_position: 0
title: "Chapter 7: File Processing Workflows"
description: "Direct Claude Code to solve real file organization problems while observing the Seven Principles in action"
slides:
  source: "https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/slides/part-2/chapter-07/file-processing-workflows.pdf"
  title: "File Processing Workflows"
  height: 700
---

# Chapter 7: File Processing Workflows

Your Downloads folder has become chaos. You can't find that tax document from last year. Screenshots pile up with meaningless names. Sound familiar?

Here's what surprises most people. The solution isn't learning bash commands or hiring an assistant. The solution is learning to direct a General Agent effectively. And the patterns you'll master with files apply to every domain where General Agents work.

This chapter uses a universal problem to teach you something far more valuable. You'll solve file chaos through conversation. You'll watch the agent work. You'll observe the Seven Principles in action. You'll build a prompt toolkit that transfers to email management, project organization, data cleaning, and any workflow where you direct General Agents.

Most people prompt blindly. They hope the General Agent understands. You're about to learn the systematic approach that separates effective collaboration from frustration.

In Chapter 6, you learned the Four-Phase Workflow for Claude Code sessions: **Explore → Plan → Implement → Commit**. File processing expands this into a seven-step framework: **Survey → Backup → Design Rules → Test → Execute → Verify → Document**. The extra steps exist because file operations are irreversible — a moved file is moved, a renamed file is renamed. The Four-Phase Workflow assumed version control as your safety net. Here, your files don't have `git revert`, so backups, testing, and verification become explicit steps instead.

## 📚 Teaching Aid

## What You'll Learn

By the end of this chapter, you'll be able to:

| Skill                           | What It Looks Like                                       |
| ------------------------------- | -------------------------------------------------------- |
| Direct file surveys             | "Help me understand what's eating my disk space"         |
| Request safety-first operations | "Back up important files before making changes"          |
| Design organization systems     | "Create categories that make sense for my workflow"      |
| Automate batch operations       | "Rename these 100 screenshots with a consistent pattern" |
| Recover from mistakes           | "Something went wrong — compare against my backup"       |
| Search intelligently            | "Find that PDF from 2023 about taxes"                    |

This isn't about learning bash. It's about learning to work effectively with General Agents.

## Why This Matters

The patterns you learn in this chapter aren't just about files. They're the foundation for building AI Employees that automate these workflows entirely. Learn these patterns now or you'll struggle with automation later.

Every expert who works with General Agents mastered these fundamentals first. File organization is the perfect training ground because the problems are concrete, the feedback is immediate, and the patterns transfer everywhere.

## Chapter Flow

| Lesson                              | Time   | What You'll Do                                 |
| ----------------------------------- | ------ | ---------------------------------------------- |
| 1. Your First Agent Workflow        | 25 min | Survey your files through conversation         |
| 2. The Safety-First Pattern         | 20 min | Learn to require backups before changes        |
| 3. The Organization Workflow        | 25 min | Design and execute file categorization         |
| 4. Batch Operations Workflow        | 30 min | Transform repetitive tasks into scripts        |
| 5. Error Recovery & Resilience      | 20 min | Deliberately break things and recover safely   |
| 6. Search & Discovery Workflow      | 25 min | Find lost files through description            |
| 7. Capstone: Your File Toolkit      | 30 min | Build your personal prompt library             |

**Total time**: Approximately 2 hours 50 minutes

## Seven Principles Observed

You won't memorize these principles. You'll see them in action:

| Principle                  | You'll Observe The Agent...                        |
| -------------------------- | -------------------------------------------------- |
| P1: Bash is the Key        | Using `ls`, `find`, `grep`, `mv` behind the scenes |
| P2: Code as Interface      | Creating reusable scripts for repetitive tasks     |
| P3: Verification           | Checking results after each operation              |
| P4: Decomposition          | Testing on one file before batch operations        |
| P5: Persisting State       | Saving rules and logs to files                     |
| P6: Constraints and Safety | Creating backups before destructive changes        |
| P7: Observability          | Logging everything and showing progress            |

## Prerequisites

Before starting this chapter:

- Complete Part 1
- Have Claude Code installed and working
- Have a Bash-compatible terminal ready:
  - **macOS/Linux**: Your built-in Terminal app works out of the box
  - **Windows**: Install [Git Bash](https://gitforwindows.org/) for a quick start, or run `wsl --install` in PowerShell for the full Linux experience via WSL
  - **Stuck?** Ask your AI agent: *"Help me get a bash terminal working on my machine"*
- Have Python installed for running scripts
- Have a folder with files to organize (Downloads recommended)

## What You'll Build

By the end, you'll have:

| Deliverable        | Purpose                                |
| ------------------ | -------------------------------------- |
| Prompt toolkit     | Reusable prompts for common file tasks |
| Organization rules | Documented categorization logic        |
| Search patterns    | Templates for finding lost files       |
| Automation scripts | Agent-generated code you can reuse     |

## From Manual to Automated

The patterns you learn here become the foundation for AI Employees:

| This Chapter (Manual) | Automated Workflow      |
| --------------------- | ----------------------- |
| Manual prompting      | Automatic file watching |
| One-time organization | Continuous organization |
| "Show me the plan"    | AI decides and acts     |

You're building the vocabulary and verification instincts you'll need for autonomous agents.
