# MoveIt Knowledge

## Heuristics

- Separate motion planning, scene state, kinematics, execution, perception, and task-level logic.
- Treat planning groups, constraints, collision objects, and controllers as architecture contracts.
- Keep safety limits and hardware execution checks explicit.
- Verify with simulation and recorded scenarios before hardware execution.

## Common Risks

- Task logic coupled directly to low-level motion calls.
- Planning scene updates that are stale or implicit.
- Safety constraints represented only in ad hoc code.
