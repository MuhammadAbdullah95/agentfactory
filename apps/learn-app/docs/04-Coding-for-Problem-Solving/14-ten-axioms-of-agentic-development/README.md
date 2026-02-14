---
sidebar_position: 14
title: "Chapter 14: Ten Axioms of Agentic Development"
---

# Chapter 14: Ten Axioms of Agentic Development

## Overview

This chapter bridges Parts 1-3 (experiential learning) with Parts 4-6 (technical implementation), formalizing the developer methodology that has been implicit throughout your work so far. Through General Agents, Applied Workflows, and SDD-RI, you have already practiced these axioms without naming them. Now we make them explicit, providing the rigorous foundation that governs all subsequent Python programming and agent-building work.

The Ten Axioms are not abstract theory. They are distilled from real agentic development practice and directly extend the Seven Principles introduced in Chapter 4.

You will follow Tomás, a new developer building an order management system, as he learns each axiom the hard way — from a $12,000 discount bug to a 2:47 AM production failure. His mentor Lena guides him from shell scripts to production-grade systems, grounding each axiom in a historical milestone: McIlroy's Unix pipes (1964), Codd's relational model (1970), Parnas's information hiding (1972), Beck's test-driven development (2002), Torvalds's Git (2005), and Google's SRE practices (2016).

## Relationship to the Seven Principles (Chapter 4)

| Dimension | Seven Principles | Ten Axioms |
|-----------|-----------------|------------|
| **Audience** | ALL users of AI agents | DEVELOPERS building agents |
| **Scope** | Mindset and approach | Methodology and practice |
| **Level** | How to think about agent work | How to engineer agent systems |
| **Introduced** | Part 1 (foundations) | Part 4 (technical bridge) |

The Principles tell you *how to think*. The Axioms tell you *how to build*.

## The Ten Axioms

| # | Axiom | Principle Connection | Core Teaching |
|---|-------|---------------------|---------------|
| I | Shell as Orchestrator | P1: Bash is the Key | Shell coordinates all tools; programs compute |
| II | Knowledge is Markdown | P5: Persisting State | Markdown is the universal knowledge format |
| III | Programs Over Scripts | P2: Code as Interface | Production requires typed programs with tests and CI |
| IV | Composition Over Monoliths | P4: Decomposition | Build from composable, focused units |
| V | Types Are Guardrails | P6: Constraints | Type systems prevent errors before runtime |
| VI | Data is Relational | P5: Persisting State | SQL as default for structured data |
| VII | Tests Are the Specification | P3: Verification | TDG: tests define correctness |
| VIII | Version Control is Memory | P5: Persisting State | Git as persistent memory layer |
| IX | Verification is a Pipeline | P3: Verification | CI/CD automates verification |
| X | Observability Extends Verification | P7: Observability | Runtime monitoring extends testing |

## Layer Progression

| Lessons | Layer | Focus |
|---------|-------|-------|
| 01-04 | L1 (Manual) | Introduce axioms conceptually with concrete examples |
| 05-07 | L2 (Collaboration) | Explore axioms with AI assistance |
| 08-10 | L2 to L3 | Axioms compose into integrated systems |

## Prerequisites

- **Part 1**: General Agents Foundations (Chapters 1-4)
- **Part 2**: Applied General Agent Workflows (Chapters 5-10)
- **Part 3**: SDD-RI Fundamentals (Chapters 11-13)

## What You'll Learn

- How the shell serves as an orchestration layer distinct from computation
- Why markdown is the universal knowledge format for agent workflows
- The difference between disposable scripts and production programs
- How composition, types, and relational data create robust agent systems
- Test-Driven Generation (TDG) as the specification mechanism for AI-generated code
- Git as persistent memory and CI/CD as automated verification
- How observability extends verification from build-time into runtime
