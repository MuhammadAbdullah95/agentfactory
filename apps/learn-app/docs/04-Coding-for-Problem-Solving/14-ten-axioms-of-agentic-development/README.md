---
sidebar_position: 14
title: "Chapter 14: Ten Axioms of Agentic Development"
slides:
  source: "https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/slides/part-4/chapter-14/the-agentic-engineering-system.pdf"
  title: "The Agentic Engineering System"
  height: 700
---

# Chapter 14: Ten Axioms of Agentic Development

## Overview

Every developer who has worked with an AI coding agent has had the same experience. The first hour feels like magic: you describe what you want, the agent writes it, and it works. The first week is productive: features ship faster than they ever did by hand. Then comes the first month — and the codebase is a mess. Untested scripts everywhere. Documentation scattered or missing. Deployment steps that only work on one person's laptop. The AI wrote code as fast as you could ask for it, and you drowned in the output.

The problem is not the AI. The problem is building without rules.

Think of it this way: a fire hose is incredibly powerful, but nobody points a fire hose at a house without plumbing first. The AI agent is your fire hose. This chapter gives you the plumbing — ten engineering rules that keep the power of AI under control.

### What Are These Ten Axioms?

An axiom is a foundational rule — something you accept as true and build everything else on top of. These ten axioms are not abstract ideas. Each one exists because, without it, a specific thing goes wrong. They come from decades of hard-won software engineering lessons, and they apply directly to how you work with AI agents.

The ten axioms fall into three groups. Think of them like building a house:

**First, you need a solid structure (Axioms I-IV).** These rules govern how your code is organized. Where do you run commands? How do you store knowledge? When does a quick script need to become a real program? How do you break a big system into manageable pieces?

| # | Axiom | The Question It Answers |
|---|-------|------------------------|
| I | Shell as Orchestrator | Where should commands run, and what should they do? |
| II | Knowledge is Markdown | How do you store decisions so both humans and AI can use them? |
| III | Programs Over Scripts | When does a quick script need to become a proper program? |
| IV | Composition Over Monoliths | How do you keep code from growing into an unmanageable blob? |

**Then, you need rules for the data flowing through it (Axioms V-VI).** These rules make sure information stays correct as it moves through your system. Think of them as the pipes and wiring inside the walls — invisible, but everything breaks without them.

| # | Axiom | The Question It Answers |
|---|-------|------------------------|
| V | Types Are Guardrails | How do you catch mistakes before they reach users? |
| VI | Data is Relational | How do you store and connect structured information reliably? |

**Finally, you need a way to know it actually works (Axioms VII-X).** These rules create a chain of verification — from writing the first line of code all the way to monitoring the live system. Think of these as the inspection, testing, and monitoring systems that keep the house safe after you move in.

| # | Axiom | The Question It Answers |
|---|-------|------------------------|
| VII | Tests Are the Specification | How do you define "correct" so the AI builds the right thing? |
| VIII | Version Control is Memory | How do you track what changed, when, and why? |
| IX | Verification is a Pipeline | How do you automatically check every change before it ships? |
| X | Observability Extends Verification | How do you know things are still working after deployment? |

### Why You Cannot Skip Any of Them

You might be tempted to pick the axioms that seem most useful and skip the rest. This does not work — for the same reason you cannot build walls without a foundation.

These axioms depend on each other. If you skip the rules about organizing code (I-IV), the rules about verifying it (VII-X) have nothing solid to check. If you skip the rules about data (V-VI), your well-organized code passes bad information around without anyone noticing. Each axiom covers a gap that the others leave open. The system works because it is complete.

### How This Chapter Works

Each lesson follows the same pattern. You will meet a developer facing a real problem — the kind that costs time, money, or sleep. You will learn the axiom that prevents that problem. You will see it applied with real code and real tools. And you will practice it yourself with AI prompts.

By the end of this chapter, you will have ten rules that work together as one system — taking you from the first terminal command to a running, monitored application.

Let's start with the most basic question: when an AI agent has access to a terminal, what should it actually do with it?

## 📚 Teaching Aid

## Prerequisites

- **Part 1**: General Agents Foundations (Chapters 1-4)
- **Part 2**: Agent Workflow Primitives (Chapters 5-10)
- **Part 3**: Applied Domain Workflows (Chapters 11-13)
