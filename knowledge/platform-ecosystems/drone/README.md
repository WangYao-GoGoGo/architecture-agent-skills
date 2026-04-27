# Drone and UAV Platform Ecosystem Knowledge

Drone and UAV platforms include autopilot systems, flight controllers, ground control stations, mission planning, telemetry, and hardware SDKs where the platform owns flight safety, regulatory compliance, and hardware control.

Examples include DJI (Mobile SDK, OSDK, Pilot), ArduPilot (MAVLink), and PX4 (MAVLink, uORB).

## Heuristics

- Treat mission commands, telemetry data, flight controller state, geofence definitions, and failsafe behavior as platform contracts.
- Keep mission planning, telemetry processing, camera/gimbal control, and safety monitoring separate from domain workflow logic.
- Design for signal loss, battery RTH, geofence violations, sensor degradation, and regulatory compliance.
- Separate mission planner, telemetry handler, safety monitor, and hardware adapter boundaries.

## Common Risks

- Mission logic mixed with flight controller SDK calls, making simulation and testing difficult.
- Safety checks (geofence, battery, signal) scattered across application code.
- Telemetry processing assumptions tied to one drone platform's data format.
- Regulatory compliance (remote ID, no-fly zones, airspace) handled as an afterthought.
- Offline mission behavior not designed for communication loss scenarios.
