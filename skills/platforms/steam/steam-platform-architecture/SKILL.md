---
name: steam-platform-architecture
description: Use when reviewing or designing Steam platform integration, including Steamworks SDK, achievements, leaderboards, matchmaking, inventory, cloud saves, and Steam platform constraints.
---

# Steam Platform Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/communication-platforms/`
- `knowledge/languages/cpp/`
- `knowledge/languages/csharp/`
- `knowledge/api/`

## Workflow

1. Identify integration scenarios: Steamworks SDK initialization, achievements, leaderboards, matchmaking, lobbies, inventory/trading, cloud saves, Steam Audio, and DRM.
2. Map Steamworks contracts: SDK lifecycle, callback/result handlers, API call result patterns, Steam ID format, and app ownership validation.
3. Check whether game logic, achievement tracking, leaderboard submission, or matchmaking state are mixed with Steam SDK calls.
4. Review platform constraints: SDK version compatibility, app review requirements, Steam Pipe migration, DRM implications, and anti-cheat integration.
5. Recommend game service adapters, achievement manager, leaderboard service, and matchmaking coordinator boundaries.
6. Verify with Steamworks test app, API call simulation, callback testing, and offline mode scenarios.

## Output Format

```markdown
Steam platform architecture:
- Integration scenarios:
- SDK coupling:
- DRM/review concerns:
- Proposed boundaries:
- Verification:
```
