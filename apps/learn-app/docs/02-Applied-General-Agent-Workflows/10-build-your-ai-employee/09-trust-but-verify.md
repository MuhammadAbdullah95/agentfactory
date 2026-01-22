---
sidebar_position: 9
title: "Trust But Verify"
sidebar_label: "L09: Trust But Verify"
description: "Implement Human-in-the-Loop approval workflows that prevent your AI employee from taking sensitive actions without explicit permission."
keywords:
  - Human-in-the-Loop
  - HITL
  - approval workflow
  - permission boundaries
  - sensitive actions
  - governance
chapter: 6
lesson: 9
duration_minutes: 30
tier: "Silver"

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration)"
layer_1_foundation: "Understanding permission boundaries, approval request format"
layer_2_collaboration: "Designing approval workflows with AI assistance"
layer_3_intelligence: "N/A (governance pattern, not intelligence)"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Approval Request Format"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can create properly formatted approval request files"
  - name: "Permission Boundaries"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Evaluate"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can define appropriate thresholds for auto-approve vs require-approval"
  - name: "Folder-Based Workflow"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can implement /Pending_Approval/ → /Approved/ workflow"

learning_objectives:
  - objective: "Design approval request file format with all necessary metadata"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Approval request file contains action, amount, recipient, expiry"
  - objective: "Define permission boundaries for different action categories"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Permission table covers email, payments, social, file operations"
  - objective: "Implement folder-based approval workflow"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Files move from /Pending_Approval/ to /Approved/ or /Rejected/"

cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (approval requests, permission boundaries, folder workflow)"

differentiation:
  extension_for_advanced: "Add expiry handling and escalation rules"
  remedial_for_struggling: "Start with single action type (emails only)"

# Generation metadata
generated_by: "placeholder - to be implemented"
created: "2026-01-07"
version: "0.1.0"
---

# Trust But Verify

:::info Silver Tier Lesson
This lesson is part of the **Silver Tier**. Complete Bronze Tier (L01-L07) first.
:::

## Coming Soon

This lesson will teach you to implement **Human-in-the-Loop (HITL)** approval workflows that prevent your AI employee from taking sensitive actions without your explicit permission.

**What You'll Build:**
- Approval request file format with metadata
- Permission boundaries table (what auto-approves vs requires human)
- Folder-based workflow: `/Pending_Approval/` → `/Approved/` or `/Rejected/`

**Key Concept:** Trust your employee with routine tasks, but require sign-off for anything with real consequences (payments, new contacts, public posts).

---

## Placeholder Content

See [L00: Complete Specification](./00-personal-ai-employee-specification.md) for the full HITL architecture.

**Reference sections:**
- "Human-in-the-Loop Pattern"
- "Permission Boundaries"
- "Approval Request Format"
