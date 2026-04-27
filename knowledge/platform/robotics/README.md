# Robotics Platform Knowledge

## Use When

Reviewing or designing robotics platform architecture, hardware integration, or control systems.

## Heuristics

- Separate task planning, control logic, driver/vendor SDK adapters, safety checks, telemetry, and UI/operator control.
- Treat topics, commands, trajectories, coordinate frames, calibration data, and hardware states as contracts.
- Verify in simulation, recorded playback, and hardware-in-the-loop where possible.
- Design for physical safety, real-time constraints, and vendor SDK limits.

## Common Risks

- Task planning mixed with low-level control logic.
- Safety checks scattered across application code.
- Hardware dependencies making simulation and testing difficult.

## Detailed Topics

- [`pepper-naoqi.md`](pepper-naoqi.md): Pepper robot and NAOqi application boundaries.
- [`robot-arm-control.md`](robot-arm-control.md): Mechanical arm control, motion planning, drivers, and safety.
- [`industrial-robotics.md`](industrial-robotics.md): Industrial controllers, cells, PLC integration, and production safety.

Frameworks such as ROS 2, MoveIt, and Gazebo live under [`knowledge/frameworks/robotics/`](../../frameworks/robotics/README.md).
