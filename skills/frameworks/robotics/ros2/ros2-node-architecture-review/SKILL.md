---
name: ros2-node-architecture-review
description: Use when reviewing ROS 2 node architecture, topic/service/action design, lifecycle management, launch files, and robot application structure.
---

# ROS 2 Node Architecture Review

## When To Use

- The main decision is about ROS 2 node decomposition, communication pattern selection, lifecycle management, or launch configuration.
- Reviewing QoS settings, timing constraints, or hardware driver boundaries.

## Workflow

1. Identify the node decomposition — node boundaries, ownership, and responsibility.
2. Review communication patterns — topics vs services vs actions for each interface.
3. Check QoS configuration — reliability, durability, history, and deadline settings.
4. Review lifecycle management — managed nodes, state transitions, and error handling.
5. Check launch file structure — composition, parameters, and remapping.
6. Review hardware driver boundaries — stable interfaces and simulation compatibility.
7. Recommend the smallest structural change that improves reliability or maintainability.

## Output Format

```markdown
ROS 2 architecture review:
- Node decomposition:
- Communication patterns:
- QoS configuration:
- Lifecycle management:
- Launch structure:
- Hardware boundaries:
- Recommended change:
- Verification:
```
