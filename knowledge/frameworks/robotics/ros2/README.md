# ROS 2 Knowledge

## Heuristics

- Separate nodes by ownership, timing, and failure boundaries.
- Treat topics, services, actions, parameters, and launch files as architecture.
- Keep hardware drivers behind stable interfaces.
- Use simulation and replay for verification where possible.
- Make QoS, timing, and safety constraints explicit.

## Common Risks

- Nodes coupled through undocumented topics.
- QoS mismatches causing dropped or stale data.
- Business/task logic tied directly to hardware drivers.

