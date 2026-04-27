# DJI Drone Platform Architecture

## Heuristics

- Treat mission commands, telemetry data, flight controller state, geofence definitions, and failsafe behavior as platform contracts.
- Keep mission planning, telemetry processing, camera/gimbal control, and safety monitoring separate from domain workflow logic.
- Design for signal loss, battery RTH (Return to Home), geofence violations, sensor degradation, and regulatory compliance.
- Separate mission planner, telemetry handler, safety monitor, and hardware adapter boundaries.
- Use DJI Mobile SDK, OSDK, or Pilot SDK behind adapters for testability and simulation.

## Common Risks

- Mission logic mixed with DJI SDK calls, making simulation and testing difficult.
- Safety checks (geofence, battery, signal) scattered across application code.
- Telemetry processing assumptions tied to DJI's specific data format.
- Regulatory compliance (remote ID, no-fly zones, airspace) handled as an afterthought.
- Offline mission behavior not designed for communication loss scenarios.

## Verification

- Mission planning can be tested without real DJI drone hardware.
- Safety monitor behavior is centralized and testable.
- Failsafe scenarios (signal loss, low battery, geofence) are explicitly covered.
