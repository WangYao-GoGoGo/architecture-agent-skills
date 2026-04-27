---
name: moveit-planning-architecture-review
description: Use when reviewing MoveIt motion planning architecture, planning groups, constraints, collision objects, kinematics, and manipulation pipeline.
---

# MoveIt Planning Architecture Review

## When To Use

- The main decision is about MoveIt planning group configuration, constraint definition, collision scene management, or kinematics setup.
- Reviewing motion planning pipeline, safety limits, or hardware execution.

## Workflow

1. Identify the planning groups and their configuration — joints, links, and kinematics.
2. Review constraint definitions — position, orientation, joint, and path constraints.
3. Check collision object management — planning scene updates, known objects, and octomap.
4. Review motion planning pipeline — planners, adapters, and planning time.
5. Check safety limits — velocity, acceleration, and singularity avoidance.
6. Review hardware execution — controller interfaces, trajectory execution, and error recovery.
7. Recommend the smallest structural change that improves safety or planning reliability.

## Output Format

```markdown
MoveIt architecture review:
- Planning groups:
- Constraint definitions:
- Collision scene:
- Planning pipeline:
- Safety limits:
- Hardware execution:
- Recommended change:
- Verification:
```
