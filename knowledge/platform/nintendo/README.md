# Nintendo Platform Knowledge

## Use When

Reviewing or designing Nintendo platform integration, NintendoSDK, or Switch console architecture.

## Heuristics

- Treat NintendoSDK initialization, authentication, achievements, leaderboards, cloud saves, and online services as platform contracts.
- Keep game logic, achievement tracking, leaderboard submission, and save data management separate from Nintendo SDK calls.
- Design for offline mode, Nintendo Network service outages, LotCheck certification, and SDK version changes.
- Separate platform-specific adapters from cross-platform game engine code.

## Common Risks

- Game logic tightly coupled to Nintendo SDK without abstraction for cross-platform ports.
- Achievement unlock logic scattered across gameplay code.
- LotCheck certification requirements discovered late in development.
