---
sidebar_position: 0
title: "Build Your GitOps Skill"
description: "Create your GitOps deployment skill FIRST, then learn to understand and improve it throughout the chapter"
chapter: 54
lesson: 0
duration_minutes: 25

skills:
  - name: "Skill-First Learning Application"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student applies skill-creator and fetching-library-docs to build a GitOps skill"

learning_objectives:
  - objective: "Build a GitOps deployment skill using Chapter 5 tools"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student has a working gitops-deployment skill in .claude/skills/"

cognitive_load:
  new_concepts: 2
  assessment: "Applies existing Ch5 knowledge to GitOps domain"

differentiation:
  extension_for_advanced: "Add CI/CD patterns and secret management to initial skill"
  remedial_for_struggling: "Follow exact prompts; customization comes in later lessons"
---

# Build Your GitOps Skill

You're about to learn GitOps with ArgoCD—automating deployments through Git. But you won't start with "what is GitOps?"

You'll start by **building a skill that knows GitOps**.

---

## Step 1: Clone the Skills Lab

```bash
git clone https://github.com/panaversity/claude-code-skills-lab.git
cd claude-code-skills-lab
claude
```

---

## Step 2: Write Your Learning Spec

```
I'm learning GitOps with ArgoCD to automate Kubernetes deployments through Git.

Before I learn the details, help me BUILD a skill that can:
1. Generate ArgoCD Application manifests
2. Create GitHub Actions workflows for CI
3. Design GitOps repository structure
4. Configure sync policies and health checks
5. Implement progressive delivery patterns

Let's do this in two steps:
1. First, use /fetching-library-docs to get ArgoCD documentation
2. Then, use /skill-creator to build a skill called "gitops-deployment"
```

---

## Step 3: Fetch Official Documentation

```
/fetching-library-docs argocd
```

---

## Step 4: Create the Skill

```
/skill-creator
```

You'll see `.claude/skills/gitops-deployment/SKILL.md` created:

```markdown
---
name: gitops-deployment
description: Generate GitOps pipelines with ArgoCD, GitHub Actions, and proper repository structure
allowed-tools: Read, Write, Bash, Glob, Grep
---

## Persona
You are a DevOps engineer specializing in GitOps workflows...

## Principles
1. Git is the single source of truth
2. All changes go through pull requests
3. Automate sync but require manual promotion to prod
4. Use ApplicationSets for multi-environment scaling
...
```

---

## Step 5: Test Your Skill

```
Using my gitops-deployment skill, generate:
- ArgoCD Application for task-api
- GitHub Actions workflow for building and pushing images
- GitOps repo structure for dev/staging/prod

Just generate it—I want to see what my skill produces.
```

---

## What Happens Next

| Lesson | You Learn | Your Skill Improves |
|--------|-----------|---------------------|
| L00 (this) | Build skill first | Initial version from docs |
| L01-04 | CI/CD, GitHub Actions | Understand pipeline patterns |
| L05-09 | ArgoCD, GitOps | Refine: better sync configs |
| L10-17 | Advanced patterns + Capstone | **Production-ready skill** |

---

## Your Growing Skills Library

```
.claude/skills/
├── skill-creator/
├── fetching-library-docs/
├── fastapi-agent-api/       # Chapter 40
├── docker-deployment/       # Chapter 49
├── kubernetes-deployment/   # Chapter 50
├── helm-chart/              # Chapter 51
├── kafka-events/            # Chapter 52
└── gitops-deployment/       # NEW - this chapter
```

---

**Next: Lesson 1 — CI/CD Concepts**
