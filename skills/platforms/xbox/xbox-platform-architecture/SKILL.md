---
name: xbox-platform-architecture
description: Use when reviewing or designing Xbox platform integration, including Xbox Live SDK, achievements, Game DVR, multiplayer, party chat, cloud saves, and Xbox certification constraints.
---

# Xbox Platform Architecture

## Knowledge To Use

- `knowledge/platform/communication-platforms/`
- `knowledge/languages/cpp/`
- `knowledge/languages/csharp/`
- `knowledge/api/`

## Workflow

1. Identify integration scenarios: Xbox Live SDK initialization, achievements, Game DVR recording, multiplayer (multiplayer manager), party chat, cloud saves, and leaderboards.
2. Map Xbox Live contracts: XAL (Xbox Authentication Library) lifecycle, achievement unlock flow, multiplayer session model, Game DVR clip management, and certification requirements (XRs).
3. Check whether game logic, achievement tracking, multiplayer state, or social features are mixed with platform SDK calls.
4. Review platform constraints: XR (Xbox Requirements) compliance, certification process, GDK (Game Development Kit) versioning, devkit vs retail differences, and cross-platform play considerations.
5. Recommend game service adapters, achievement manager, multiplayer coordinator, and social service boundaries.
6. Verify with Xbox devkit, XR testing tools, multiplayer simulation, and certification dry-run.

## Output Format

```markdown
Xbox platform architecture:
- Integration scenarios:
- SDK coupling:
- XR/certification concerns:
- Proposed boundaries:
- Verification:
```
