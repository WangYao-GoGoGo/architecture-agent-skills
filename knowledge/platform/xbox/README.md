# Xbox Platform Knowledge

## Use When

Reviewing or designing Xbox platform integration, Xbox Live SDK, or console architecture.

## Heuristics

- Treat Xbox Live SDK initialization, authentication, achievements, leaderboards, cloud saves, and multiplayer sessions as platform contracts.
- Keep game logic, achievement tracking, leaderboard submission, and save data management separate from Xbox Live SDK calls.
- Design for offline mode, Xbox Live service outages, certification requirements, and SDK version changes.
- Separate platform-specific adapters from cross-platform game engine code.

## Common Risks

- Game logic tightly coupled to Xbox Live SDK without abstraction for cross-platform ports.
- Achievement unlock logic scattered across gameplay code.
- Xbox certification requirements discovered late in development.
