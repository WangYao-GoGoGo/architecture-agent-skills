# Gazebo Knowledge

## Heuristics

- Treat simulation worlds, robot descriptions, plugins, sensors, and controllers as architecture artifacts.
- Keep simulation-only assumptions out of hardware-facing task logic.
- Use simulation to verify timing, failure handling, and integration contracts.
- Make the boundary between model, controller, and environment explicit.

## Common Risks

- Tests passing only because the simulation omits real hardware constraints.
- Plugins becoming hidden application logic.
- Sensor timing and noise not represented in architecture decisions.
