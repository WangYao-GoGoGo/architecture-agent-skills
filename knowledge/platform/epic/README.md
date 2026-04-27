# Epic Games Platform Knowledge

## Use When

Reviewing or designing Epic Games platform integration, Epic Online Services (EOS) SDK, or storefront architecture.

## Heuristics

- Treat EOS SDK initialization, authentication, achievements, leaderboards, cloud saves, matchmaking, and lobby as platform contracts.
- Keep game logic, achievement tracking, leaderboard submission, and save data management separate from EOS SDK calls.
- Design for offline mode, Epic service outages, and SDK version changes.
- Separate platform-specific adapters from cross-platform game engine code.

## Common Risks

- Game logic tightly coupled to EOS SDK without abstraction for other storefronts.
- Achievement unlock logic scattered across gameplay code.
- Save data format tied to Epic cloud save APIs.
