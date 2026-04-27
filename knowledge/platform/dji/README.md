# DJI Drone Platform Knowledge

## Use When

Reviewing or designing DJI drone platform integration, Mobile SDK, or mission planning architecture.

## Heuristics

- Treat mission commands, telemetry data, flight controller state, geofence definitions, and failsafe behavior as platform contracts.
- Keep mission planning, telemetry processing, camera/gimbal control, and safety monitoring separate from domain workflow logic.
- Design for signal loss, battery RTH, geofence violations, sensor degradation, and regulatory compliance.
- Use DJI SDKs behind adapters for testability and simulation.

## Common Risks

- Mission logic mixed with DJI SDK calls, making simulation and testing difficult.
- Safety checks (geofence, battery, signal) scattered across application code.
- Offline mission behavior not designed for communication loss scenarios.
