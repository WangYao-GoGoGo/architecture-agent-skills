---
name: gazebo-simulation-architecture-review
description: Use when reviewing Gazebo simulation architecture, world models, robot descriptions, plugins, sensors, and simulation pipeline.
---

# Gazebo Simulation Architecture Review

## When To Use

- The main decision is about Gazebo world configuration, robot model integration, plugin design, sensor simulation, or physics setup.
- Reviewing simulation fidelity, timing, or hardware transition strategy.

## Workflow

1. Identify the world configuration — physics engine, gravity, time step, and environment.
2. Review robot description integration — URDF/SDF models, transmissions, and controllers.
3. Check plugin design — model, sensor, system, and visual plugins.
4. Review sensor simulation — camera, lidar, IMU, and noise models.
5. Check simulation timing — real-time factor, step size, and synchronization.
6. Review hardware transition strategy — simulation-only assumptions vs real hardware.
7. Recommend the smallest structural change that improves simulation fidelity or usefulness.

## Output Format

```markdown
Gazebo simulation review:
- World configuration:
- Robot description:
- Plugin design:
- Sensor simulation:
- Timing & synchronization:
- Hardware transition:
- Recommended change:
- Verification:
```
