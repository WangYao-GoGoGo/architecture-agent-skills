# ArduPilot/PX4 Platform Knowledge

## Use When

Reviewing or designing ArduPilot/PX4 drone platform integration, MAVLink, or mission planning architecture.

## Heuristics

- Treat MAVLink messages, mission commands, telemetry data, flight controller parameters, geofence definitions, and failsafe behavior as platform contracts.
- Keep mission planning, telemetry processing, camera/gimbal control, and safety monitoring separate from domain workflow logic.
- Design for signal loss, battery RTH, geofence violations, sensor degradation, and regulatory compliance.
- Use MAVSDK or DroneKit behind adapters for testability and SITL simulation.

## Common Risks

- Mission logic mixed with MAVSDK/DroneKit calls, making simulation and testing difficult.
- Safety checks (geofence, battery, signal) scattered across application code.
- Offline mission behavior not designed for communication loss scenarios.
