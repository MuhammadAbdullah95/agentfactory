---
id: module-2-simulation
title: "Part 2: The Digital Twin"
sidebar_position: 2
sidebar_label: "2. Gazebo & Unity Simulation"
description: "Build physics-accurate robot simulations with Gazebo and Unity. Test, crash, and iterate without breaking real hardware."
---

# Part 2: The Digital Twin

**Gazebo & Unity Simulation**

Before you deploy code to a $50,000 robot, you simulate. A digital twin lets you crash into walls, flip over, and drain batteries—all without breaking anything. Simulation is where you iterate fast, test edge cases, and build confidence before the real world.

**Gazebo** provides physics-accurate simulation: gravity, friction, collisions, and sensor noise. Your virtual robot behaves like the real thing. **Unity** adds high-fidelity visualization and human-robot interaction design. Together, they form a complete digital twin pipeline where your ROS 2 nodes control virtual robots that look and act real.

In this part, you'll build simulated worlds, define robot models, and connect everything to the ROS 2 systems you built in Part 1. By the end, you'll have a working simulation environment ready for AI training in Part 3.

---

## Chapters

### Chapter 4: Gazebo Simulation

Your entry into physics simulation. You'll set up Gazebo environments, understand SDF and URDF robot description formats, configure physics engines, and add simulated sensors (cameras, LIDAR, IMUs). Most importantly, you'll connect Gazebo to ROS 2—your publisher/subscriber nodes now control a virtual robot. When things go wrong, you'll debug sensor data, physics collisions, and timing issues.

### Chapter 5: Unity Integration

Gazebo handles physics; Unity handles visuals and interaction. You'll bridge Unity to ROS 2, create compelling visualizations of robot state, and design interfaces for human operators. The chapter culminates in a complete digital twin: Gazebo simulates physics, ROS 2 handles communication, and Unity renders everything beautifully.

---

## Learning Outcomes

By completing Part 2, you will:

- Build Gazebo simulation worlds with physics and sensors
- Define robot models using URDF and SDF formats
- Connect simulations to ROS 2 for closed-loop control
- Create Unity visualizations of robot state
- Design complete simulation pipelines for testing

---

## Hardware

| Tier | What You Need | What You Get |
|------|---------------|--------------|
| **1 (Cloud)** | Any laptop | Full course via [The Construct](https://theconstructsim.com) cloud Gazebo |
| **2 (Local)** | Ubuntu 22.04 + GPU | Local Gazebo + Unity for faster iteration |

---

## Capstone: Complete Digital Twin

Build a pipeline where Gazebo simulates a robot arm, ROS 2 nodes control its motion, and Unity visualizes the result in real-time. Sensor data flows from simulation through your processing nodes back to motor commands. This is the foundation for all AI training in Part 3.

---

## Prerequisites

**Part 1** (ROS 2) complete. You'll need nodes, topics, and launch files.

---

[**← Part 1: ROS 2**](../module-1-ros2/README.md) · [**Start Chapter 4 →**](./04-gazebo/README.md)

**Next:** [Part 3: NVIDIA Isaac →](../module-3-isaac/README.md)
