---
name: playstation-platform-architecture
description: Use when reviewing or designing PlayStation platform integration, including PlayStation SDK, trophies, online services, matchmaking, parties, and PlayStation platform certification constraints.
---

# PlayStation Platform Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/communication-platforms/`
- `knowledge/languages/cpp/`
- `knowledge/languages/csharp/`
- `knowledge/api/`

## Workflow

1. Identify integration scenarios: PlayStation SDK initialization, trophy system, online services (Sony NP), matchmaking, parties, voice chat, leaderboards, and saved data management.
2. Map PlayStation platform contracts: SDK lifecycle, NP (Network Platform) service calls, trophy unlock flow, matchmaking session model, and certification requirements (TRC).
3. Check whether game logic, trophy tracking, online service calls, or matchmaking state are mixed with platform SDK calls.
4. Review platform constraints: TRC (Technical Requirements Checklist) compliance, certification process, online service SLAs, devkit vs retail differences, and patch certification.
5. Recommend game service adapters, trophy manager, online service client, and matchmaking coordinator boundaries.
6. Verify with PlayStation devkit, TRC testing tools, online service sandbox, and certification dry-run.

## Output Format

```markdown
PlayStation platform architecture:
- Integration scenarios:
- SDK coupling:
- TRC/certification concerns:
- Proposed boundaries:
- Verification:
```
