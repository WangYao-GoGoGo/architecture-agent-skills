---
name: epic-platform-architecture
description: Use when reviewing or designing Epic Games platform integration, including Epic Online Services (EOS), achievements, leaderboards, matchmaking, lobbies, and Epic Games Store constraints.
---

# Epic Games Platform Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/communication-platforms/`
- `knowledge/languages/cpp/`
- `knowledge/languages/csharp/`
- `knowledge/api/`

## Workflow

1. Identify integration scenarios: Epic Online Services (EOS) SDK initialization, achievements, leaderboards, matchmaking, lobbies, P2P networking, player data storage, and Epic Games Store overlay.
2. Map EOS contracts: SDK lifecycle, Auth/Connect interface, achievement unlock flow, lobby/session model, P2P packet format, and product user ID format.
3. Check whether game logic, achievement tracking, matchmaking state, or networking code are mixed with EOS SDK calls.
4. Review platform constraints: EOS SDK version compatibility, cross-platform play considerations, Epic Games Store submission requirements, and overlay integration.
5. Recommend game service adapters, achievement manager, matchmaking coordinator, and networking layer boundaries.
6. Verify with EOS sandbox deployment, SDK testing tools, matchmaking simulation, and cross-platform play scenarios.

## Output Format

```markdown
Epic Games platform architecture:
- Integration scenarios:
- SDK coupling:
- Cross-platform concerns:
- Proposed boundaries:
- Verification:
```
