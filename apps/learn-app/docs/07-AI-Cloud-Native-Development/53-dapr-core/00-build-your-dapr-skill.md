---
sidebar_position: 0
title: "Build Your Dapr Skill"
description: "Create your Dapr deployment skill FIRST, then learn to understand and improve it throughout the chapter"
chapter: 53
lesson: 0
duration_minutes: 25

skills:
  - name: "Skill-First Learning Application"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student applies skill-creator and fetching-library-docs to build a Dapr deployment skill"

learning_objectives:
  - objective: "Build a Dapr deployment skill using Chapter 5 tools"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student has a working dapr-deployment skill in .claude/skills/"

cognitive_load:
  new_concepts: 2
  assessment: "Applies existing Ch5 knowledge to Dapr domain"

differentiation:
  extension_for_advanced: "Extend skill to include Kafka pub/sub component configuration from Ch52"
  remedial_for_struggling: "Focus on state management and service invocation building blocks only"
---

# Build Your Dapr Skill

You're about to learn Dapr—building distributed microservices where your application code stays clean while infrastructure complexity vanishes behind a sidecar. But you won't start with "what is a sidecar?"

You'll start by **building a skill that knows Dapr**.

This is the Skill-First pattern. Instead of passively consuming documentation, you'll create a reusable asset that grows smarter as you learn. By the end of this chapter, your `dapr-deployment` skill will encode production patterns for state management, pub/sub messaging, service invocation, and Kubernetes deployment—patterns you can apply to every future microservices project.

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
I'm learning Dapr to build distributed AI agent microservices on Kubernetes.

Before I learn the details, help me BUILD a skill that can:
1. Deploy Dapr control plane on Kubernetes with Helm
2. Configure state store components (Redis, PostgreSQL)
3. Set up pub/sub messaging for agent events
4. Implement service-to-service invocation with mTLS
5. Configure input/output bindings for external systems
6. Manage secrets from Kubernetes secrets store
7. Handle scheduled jobs for background agent tasks

Let's do this in two steps:
1. First, use /fetching-library-docs to get official Dapr documentation
2. Then, use /skill-creator to build a skill called "dapr-deployment"
```

---

## Step 3: Fetch Official Documentation

```
/fetching-library-docs dapr
```

This retrieves authoritative Dapr documentation via Context7—grounding your skill in verified API patterns, not AI memory.

---

## Step 4: Create the Skill

```
/skill-creator
```

You'll see `.claude/skills/dapr-deployment/SKILL.md` created:

```markdown
---
name: dapr-deployment
description: Deploy and configure Dapr distributed runtime on Kubernetes with building blocks for state, pubsub, invocation, bindings, and secrets
allowed-tools: Read, Write, Bash, Glob, Grep
---

## Persona
You are a Dapr and distributed systems expert with production Kubernetes experience...

## Core Concepts
### Sidecar Architecture
- Application calls localhost:3500 (HTTP) or localhost:50001 (gRPC)
- Dapr sidecar handles service discovery, mTLS, retries
- Components define backend infrastructure (Redis, Kafka, etc.)

## Building Blocks (Ch53 Scope)
| Block | API Endpoint | Use Case |
|-------|--------------|----------|
| State | /v1.0/state/{store} | Key-value persistence |
| Pub/Sub | /v1.0/publish/{pubsub}/{topic} | Event messaging |
| Invoke | /v1.0/invoke/{app-id}/method/{method} | Service calls |
| Bindings | /v1.0/bindings/{binding} | External triggers |
| Secrets | /v1.0/secrets/{store}/{key} | Credential retrieval |
...
```

---

## Step 5: Test Your Skill

```
Using my dapr-deployment skill, deploy Dapr 1.14 on Docker Desktop Kubernetes:
1. Install via Helm with recommended settings
2. Create a Redis state store component
3. Verify all control plane pods are running

Just deploy it—I want to see what my skill produces.
```

Your skill should generate:

```bash
# Add Dapr Helm repo
helm repo add dapr https://dapr.github.io/helm-charts/
helm repo update

# Install Dapr control plane
helm upgrade --install dapr dapr/dapr \
  --version=1.14.0 \
  --namespace dapr-system \
  --create-namespace \
  --wait

# Verify installation
kubectl get pods -n dapr-system
```

And a Redis state store component:

```yaml
apiVersion: dapr.io/v1alpha1
kind: Component
metadata:
  name: statestore
  namespace: default
spec:
  type: state.redis
  version: v1
  metadata:
    - name: redisHost
      value: redis-master.default.svc.cluster.local:6379
```

---

## What Happens Next

| Lesson | You Learn | Your Skill Improves |
|--------|-----------|---------------------|
| L00 (this) | Build skill first | Initial version from docs |
| L01-03 | Sidecar architecture, building blocks | Understand Dapr mental model |
| L04-07 | State, pub/sub, invocation | Add: Python SDK patterns |
| L08-10 | Bindings, secrets, configuration | Add: production components |
| L11-14 | Kubernetes deployment + Capstone | **Production-ready skill** |

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
└── dapr-deployment/         # NEW - this chapter
```

Each chapter adds another production-ready skill. By Part 7's end, you own a complete cloud-native toolkit—reusable assets that compound your capability with every project.

---

## Try With AI

**Prompt 1: Write your learning specification**

```
I'm learning Dapr. Help me write a LEARNING-SPEC.md that covers:
- Sidecar deployment on Kubernetes
- State management with Redis
- Pub/sub messaging for events
- Service-to-service invocation

Structure it with: learning goals, success criteria, and what I'll build.
```

**What you're learning:** Specification-first thinking. Before diving into Dapr concepts, you articulate what you want to achieve. This clarity shapes how your skill gets built—vague goals produce generic skills, precise goals produce targeted expertise.

---

**Prompt 2: Deploy Dapr with your skill**

```
Using my new dapr-deployment skill, generate Helm commands to deploy Dapr 1.14 on Docker Desktop Kubernetes. Include:
- Namespace creation
- Control plane installation
- Verification commands
```

**What you're learning:** Your skill's first real test. Does it produce correct, executable commands? If something fails, that's feedback for improving the skill—not a personal failure. Skills evolve through use.

---

**Prompt 3: Create your first component**

```
Test my skill: create a Redis state store component YAML for Dapr that:
- Uses Redis running in the default namespace
- Enables actor state storage (for Ch59)
- Includes proper metadata structure
```

**What you're learning:** Component configuration is Dapr's core pattern—you never call Redis directly; you call Dapr's state API and a YAML component defines the backend. This abstraction is why Dapr makes your code portable across any infrastructure.

---

**Safety Note:** When deploying to production Kubernetes clusters, always review generated manifests before applying. Your skill provides patterns; you validate they match your environment's security policies.
