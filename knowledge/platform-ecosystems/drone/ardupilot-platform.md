# ArduPilot/PX4 Platform Architecture

## Heuristics

- Treat MAVLink messages, mission commands, telemetry data, flight controller parameters, geofence definitions, and failsafe behavior as platform contracts.
- Keep mission planning, telemetry processing, camera/gimbal control, and safety monitoring separate from domain workflow logic.
- Design for signal loss, battery RTH, geofence violations, sensor degradation, and regulatory compliance.
- Separate mission planner, telemetry handler, safety monitor, and hardware adapter boundaries.
- Use MAVSDK or DroneKit behind adapters for testability and simulation (SITL).

## Common Risks

- Mission logic mixed with MAVSDK/DroneKit calls, making simulation and testing difficult.
- Safety checks (geofence, battery, signal) scattered across application code.
- Telemetry processing assumptions tied to ArduPilot/PX4's specific MAVLink message format.
- Regulatory compliance (remote ID, no-fly zones, airspace) handled as an afterthought.
- Offline mission behavior not designed for communication loss scenarios.

## Verification

- Mission planning can be tested in SITL (Software In The Loop) without real hardware.
- Safety monitor behavior is centralized and testable.
- Failsafe scenarios (signal loss, low battery, geofence) are explicitly covered.
