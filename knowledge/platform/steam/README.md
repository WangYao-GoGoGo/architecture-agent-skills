# Steam Platform Knowledge

## Use When

Reviewing or designing Steam platform integration, Steamworks SDK, or game storefront architecture.

## Heuristics

- Treat Steamworks SDK initialization, authentication, achievements, leaderboards, cloud saves, and matchmaking as platform contracts.
- Keep game logic, achievement tracking, leaderboard submission, and save data management separate from Steam SDK calls.
- Design for offline mode, Steam service outages, certification requirements, and SDK version changes.
- Separate platform-specific adapters from cross-platform game engine code.

## Common Risks

- Game logic tightly coupled to Steamworks SDK without abstraction for other storefronts.
- Achievement unlock logic scattered across gameplay code.
- Save data format tied to Steam cloud save APIs.
