---
id: module-1-ros2
title: "Part 1: The Robotic Nervous System"
sidebar_position: 1
sidebar_label: "1. ROS 2 Foundations"
description: "Master ROS 2 middleware - the communication backbone of modern robotics. Build nodes, topics, services, and your first multi-node robot controller."
---

# Part 1: The Robotic Nervous System

**ROS 2 Middleware Foundations**

Every robot is a distributed system. Sensors stream data continuously. Motors demand coordinated commands. AI processes everything in real-time. Without a unified communication layer, controlling a robot becomes chaos—messages collide, timing fails, and coordination breaks down.

This is why professional robotics teams use **ROS 2** (Robot Operating System 2). It's not an operating system in the traditional sense—it's middleware that transforms robots from monolithic programs into modular, distributed networks. Think of ROS 2 as a nervous system: sensory neurons (sensors) feed data to the brain (processing nodes), which sends signals to muscles (actuators). Multiple processes run simultaneously, communicate asynchronously, and fail gracefully.

In this part, you'll move from understanding what physical AI means to implementing the actual middleware that powers it. By the end, you won't just know *how* ROS 2 works—you'll understand *why* distributed middleware is essential for any serious robotics project.

---

## Chapters

### Chapter 1: Introduction to Physical AI

Before writing code, you need the mental model. What makes physical AI different from chatbots and image generators? Why does embodiment change everything? You'll explore the humanoid robotics landscape, understand sensor and actuator systems, and learn why simulation matters before physical deployment. No coding yet—just building the intuition you'll need for everything that follows.

### Chapter 2: ROS 2 Fundamentals

Your first hands-on encounter with distributed robotics. You'll learn the architecture from the ground up: nodes as independent processes, topics for publish/subscribe messaging, services for request/reply patterns, and actions for long-running tasks. You'll write your first Python publisher and subscriber, understand launch files, and discover why Quality of Service settings matter for real robot deployments.

### Chapter 3: Building with ROS 2

Individual pieces come together into complete systems. You'll structure ROS 2 packages properly, coordinate multiple nodes, debug real communication failures, and learn URDF basics for describing robot geometry. The chapter culminates in your first capstone: a multi-node system where sensors, processing, and control nodes work together.

---

## Learning Outcomes

By completing Part 1, you will:

- Explain why distributed middleware is essential for robotics
- Implement publishers and subscribers in Python using rclpy
- Design multi-node systems with proper topic/service patterns
- Debug ROS 2 communication issues using CLI tools
- Build a complete robot controller with launch files

---

## Hardware

All content works on a **laptop with a browser**. We use MockROS and cloud tools so no one is excluded by hardware cost.

| Tier | What You Need | What You Get |
|------|---------------|--------------|
| **1 (Browser)** | Any laptop | Full course via MockROS + cloud CLI |
| **2 (Local)** | Ubuntu 22.04 + RTX GPU | Faster iteration with local ROS 2 |

---

## Capstone: Multi-Node Robot Controller

Design and build a system where 3+ nodes coordinate via topics and services: a sensor node publishes data, a processing node transforms it, and a control node issues commands. One launch file brings everything up. This is the pattern you'll use throughout the course.

---

## Prerequisites

None. Part 1 is the foundation.

*Helpful but not required: Basic Python, command-line familiarity*

---

[**Start Chapter 1 →**](./01-physical-ai/README.md)

**Next:** [Part 2: The Digital Twin →](../module-2-simulation/README.md)
