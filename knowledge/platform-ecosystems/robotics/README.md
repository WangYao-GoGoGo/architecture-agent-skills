# Robotics Platform Ecosystem Knowledge

Robotics platform architecture depends on physical safety, hardware drivers, real-time or near-real-time constraints, simulation, calibration, command/control loops, and vendor SDK limits.

- `pepper-naoqi.md`: Pepper robot and NAOqi application boundaries.
- `robot-arm-control.md`: mechanical arm control, motion planning, drivers, and safety.
- `industrial-robotics.md`: industrial controllers, cells, PLC integration, and production safety.

Frameworks such as ROS 2, MoveIt, and Gazebo live under `knowledge/frameworks/robotics/`. Vendor ecosystems and hardware platforms live here.

## Review Focus

- Separate task planning, control logic, driver/vendor SDK adapters, safety checks, telemetry, and UI/operator control.
- Treat topics, commands, trajectories, coordinate frames, calibration data, and hardware states as contracts.
- Verify in simulation, recorded playback, and hardware-in-the-loop where possible.
