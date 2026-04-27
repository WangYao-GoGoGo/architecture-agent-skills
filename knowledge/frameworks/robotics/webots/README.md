# Webots Knowledge

## Heuristics

- Separate world modeling, robot controllers, supervisor scripts, and sensor configuration.
- Keep controller logic testable outside simulation where possible.
- Treat supervisor scripts as integration test harnesses.
- Add proper timing and synchronization for reproducible simulations.

## Common Risks

- Controller logic tied to specific simulation timing.
- Supervisor scripts becoming hidden application logic.
- Simulation fidelity not validated against real hardware.
