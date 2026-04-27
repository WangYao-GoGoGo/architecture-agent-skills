---
name: ardupilot-platform-architecture
description: Use when reviewing or designing ArduPilot/PX4 autopilot platform integration, including MAVLink protocol, ground control station, mission planning, telemetry, and UAV hardware constraints.
---

# ArduPilot/PX4 Platform Architecture

## Knowledge To Use

- `knowledge/platform/robotics/`
- `knowledge/languages/c/`
- `knowledge/languages/cpp/`
- `knowledge/languages/python/`
- `knowledge/platform/`

## Workflow

1. Identify integration scenarios: MAVLink protocol communication, ground control station (Mission Planner, QGroundControl), autonomous mission planning, telemetry streaming, parameter management, and hardware abstraction.
2. Map ArduPilot/PX4 contracts: MAVLink message types, mission command format, parameter namespace, flight mode transitions, geofence definitions, and failsafe behavior.
3. Check whether mission logic, telemetry processing, parameter management, or safety checks are mixed with domain workflow logic.
4. Review safety and constraints: failsafe behavior (RTL, land, loiter), geofence limits, sensor calibration, EKF health, RC loss behavior, and regulatory compliance.
5. Recommend mission planner, telemetry handler, parameter manager, and safety monitor boundaries.
6. Verify with SITL (Software In The Loop) simulation, HITL (Hardware In The Loop), mission replay, and failsafe scenario testing.

## Output Format

```markdown
ArduPilot/PX4 platform architecture:
- Integration scenarios:
- Platform coupling:
- Safety/failsafe concerns:
- Proposed boundaries:
- Verification:
```
