# Robot Arm Control Architecture

## Heuristics

- Separate task intent, motion planning, trajectory execution, driver communication, safety interlocks, and telemetry.
- Treat coordinate frames, tool definitions, calibration, speed/force limits, and workspace constraints as explicit contracts.
- Keep vendor SDK or controller protocols behind adapters.
- Verify planned motion before execution and prefer simulation or dry-run modes for risky changes.

## Common Risks

- Business/task logic coupled directly to vendor driver calls.
- Safety checks implemented only in UI code.
- Coordinate frame conversions scattered across modules.
- Retry logic that repeats unsafe commands.

## Verification

- Command paths include validation, limits, cancellation, and emergency-stop awareness.
- Coordinate frames and calibration data are documented and tested.
- Hardware-facing code can be isolated from planning and domain workflows.
