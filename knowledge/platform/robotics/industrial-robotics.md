# Industrial Robotics Architecture

## Heuristics

- Separate production workflow, cell coordination, PLC/fieldbus integration, robot controller programs, safety systems, and operator UI.
- Treat cycle timing, interlocks, teach points, recipes, alarms, and traceability as architecture.
- Keep vendor controller details behind stable plant-level contracts.
- Design for safe degraded modes, maintenance operations, and auditability.

## Common Risks

- Application code assuming ideal hardware timing.
- Safety and production-state logic duplicated across controller, UI, and backend.
- Alarm handling without ownership or recovery paths.
- Hardcoded teach points or recipes mixed into workflow code.

## Verification

- State transitions are explicit for run, pause, fault, recover, maintenance, and manual modes.
- Safety-critical constraints are not only represented in application code.
- Integration tests cover controller disconnects, timeouts, and repeated commands.
