---
name: dji-drone-platform-architecture
description: Use when reviewing or designing DJI drone platform integration, including DJI Mobile SDK, OSDK, Pilot, waypoint missions, telemetry, camera control, and DJI hardware constraints.
---

# DJI Drone Platform Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/robotics/`
- `knowledge/languages/java/`
- `knowledge/languages/c/`
- `knowledge/languages/python/`
- `knowledge/platform/`

## Workflow

1. Identify integration scenarios: DJI Mobile SDK (Android/iOS), OSDK (onboard), Pilot app integration, waypoint missions, real-time telemetry, camera/gimbal control, and data transmission.
2. Map DJI platform contracts: SDK lifecycle, mission control events, telemetry data format, camera commands, flight controller state, geofence constraints, and return-to-home behavior.
3. Check whether mission logic, telemetry processing, camera control, or safety checks are mixed with domain workflow logic.
4. Review safety and constraints: geofence limits, no-fly zones, battery/signal RTH behavior, SDK version compatibility, regulatory compliance (remote ID, airspace), and offline mission behavior.
5. Recommend mission planner, telemetry handler, camera controller, and safety monitor boundaries.
6. Verify with DJI simulator, hardware-in-the-loop testing, mission dry-run, and geofence boundary scenarios.

## Output Format

```markdown
DJI drone platform architecture:
- Integration scenarios:
- Platform coupling:
- Safety/regulatory concerns:
- Proposed boundaries:
- Verification:
```
