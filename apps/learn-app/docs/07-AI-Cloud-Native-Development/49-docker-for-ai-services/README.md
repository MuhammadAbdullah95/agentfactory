---
sidebar_position: 49
title: "Chapter 49: Docker for AI Services"
description: "Containerize AI agents with Docker for portable, reproducible deployments"
---

# Chapter 49: Docker for AI Services

Your agent runs perfectly on your machine. But "works on my machine" doesn't ship products. Docker solves this by packaging your agent, its dependencies, and its runtime environment into a portable container that runs identically everywhere—your laptop, a teammate's machine, or a cloud server.

This chapter teaches containerization from first principles, with a focus on AI service patterns. You'll learn to write efficient Dockerfiles, optimize image sizes, configure networking and storage, handle Python/Node dependencies correctly, and use AI-assisted workflows with Gordon (Docker's AI assistant) to accelerate common tasks.

By the end, your FastAPI agent service from Part 6 will be a portable container ready for Kubernetes deployment.

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Understand container fundamentals**: Images, containers, layers, and the Docker runtime
- **Write production Dockerfiles**: Multi-stage builds, layer caching, and size optimization
- **Configure container networking**: Bridge networks, port mapping, and service discovery
- **Manage persistent data**: Named volumes, bind mounts, and AI model storage patterns
- **Understand Docker's architecture**: containerd, runc, and OCI specifications
- **Handle AI service dependencies**: Python packages, model files, and environment configuration
- **Use Docker Compose**: Multi-container setups for local development (agent + database + redis)
- **Apply security best practices**: Non-root users, minimal base images, and secret handling
- **Leverage Gordon (Docker AI)**: AI-assisted Docker operations for common workflows
- **Create reusable skills**: Transform Docker expertise into organizational intelligence

## Chapter Structure

| Lesson | Title | Layer | Focus |
|--------|-------|-------|-------|
| 1 | Docker Installation & Setup | L1 (Manual) | Platform setup, Docker Desktop, resource configuration |
| 2 | Container Fundamentals | L1 (Manual) | Images vs containers, Docker Hub, layers, lifecycle |
| 3 | Writing Your First Dockerfile | L1 (Manual) | FROM, WORKDIR, COPY, RUN, CMD, layer caching |
| 4 | Container Lifecycle & Debugging | L1 (Manual) | Logs, exec, inspect, port conflicts, restart policies |
| 5 | Multi-Stage Builds & Optimization | L1 (Manual) | Build vs runtime stages, UV, slim/alpine/distroless |
| 6 | Docker Networking Fundamentals | L1 (Manual) | Bridge networks, port mapping, container DNS |
| 7 | Container-to-Container Communication | L1 (Manual) | User-defined networks, service discovery, isolation |
| 8 | Volumes & Persistent Data | L1 (Manual) | Named volumes, bind mounts, AI model storage |
| 9 | Docker Engine Architecture | L1 (Manual) | containerd, runc, OCI specs, runtime stack |
| 10 | Docker Compose for Development | L1 (Manual) | Multi-service orchestration, networks, volumes |
| 11 | Security & Best Practices | L1 (Manual) | Non-root users, Docker Scout, DHI, secrets |
| 12 | AI-Assisted Docker with Gordon | L2 (Collaboration) | Gordon workflows for generation, debugging, optimization |
| 13 | Capstone: Production-Ready Agent | L4 (Spec-Driven) | Specification-first containerization of FastAPI agent |
| 14 | Building the Production Dockerfile Skill | L3 (Intelligence) | Persona + Questions + Principles skill design |

## 4-Layer Teaching Progression

This chapter follows the **4-Layer Teaching Method**:

- **Lessons 1-11 (Layer 1)**: Build mental models manually before AI assistance
- **Lesson 12 (Layer 2)**: Collaborate with Gordon using Three Roles (invisible framework)
- **Lesson 13 (Layer 4)**: Apply all lessons in spec-driven capstone project
- **Lesson 14 (Layer 3)**: Create reusable intelligence that compounds across projects

## Prerequisites

- **Part 6 completion**: A working FastAPI agent service—this is the application you'll containerize in the capstone
- **Basic command-line familiarity**: You should be comfortable running commands in a terminal
- **No Docker experience required**: Lesson 1 covers installation and explains containers from scratch

## Your Part 6 Agent: The Thread Through This Chapter

Throughout this chapter, we build toward containerizing your Part 6 FastAPI agent:

- **Lessons 1-11**: Learn Docker concepts using simplified examples
- **Lesson 12**: Use Gordon (Docker's AI) to optimize your Dockerfile
- **Lesson 13 (Capstone)**: Containerize your actual Part 6 agent for production
- **Lesson 14**: Create a reusable skill for future containerization work

By the end, "works on my machine" becomes "runs anywhere Docker runs."

## Looking Ahead

This chapter produces a container image and a reusable Dockerfile skill. Chapter 50 (Kubernetes) deploys that container to an orchestrated cluster, and Chapter 51 (Helm) packages it for repeatable deployments.
