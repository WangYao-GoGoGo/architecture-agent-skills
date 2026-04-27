---
name: robotics-platform-architecture
description: Use when reviewing or designing robotics architecture for Pepper/NAOqi, robot arms, industrial robots, ROS/MoveIt/Gazebo integration, hardware drivers, motion control, safety boundaries, simulation, telemetry, and vendor SDK adapters.
---

# Robotics Platform Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/robotics/`
- `knowledge/frameworks/robotics/`
- `knowledge/languages/python/`
- `knowledge/languages/c/`
- `knowledge/platform/`

## Workflow

1. Identify task logic, planning, control loop, driver/vendor SDK adapters, sensors, actuators, telemetry, operator UI, safety checks, and simulation paths.
2. Map contracts: commands, trajectories, topics, services, actions, coordinate frames, calibration, controller state, alarms, and emergency stop behavior.
3. Check whether hardware or SDK details leak into domain/task logic in a way that blocks testing, simulation, or safe replacement.
4. Review timing, failure modes, cancellation, retries, idempotency, observability, and safety boundaries before recommending code structure.
5. Recommend adapters, state machines, ports, simulation seams, and verification steps only where they make behavior clearer or safer.
6. Verify with simulation, recorded playback, dry-run mode, hardware-in-the-loop, or vendor sandbox tools where available.

## Output Format

```markdown
Robotics architecture review:
- Runtime and hardware boundary:
- Safety/timing risks:
- Coupling risks:
- Recommended structure:
- Verification:
```
