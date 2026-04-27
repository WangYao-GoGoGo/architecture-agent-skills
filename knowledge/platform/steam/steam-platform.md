# Steam Platform Architecture

## Heuristics

- Treat Steamworks SDK initialization, authentication, achievements, leaderboards, cloud saves, matchmaking, and workshop as platform contracts.
- Keep game logic, achievement tracking, leaderboard submission, and save data management separate from Steam SDK calls.
- Design for offline mode, Steam service outages, certification requirements, and SDK version changes.
- Separate platform-specific adapters from cross-platform game engine code.
- Use Steamworks SDK behind an adapter for testability and portability.

## Common Risks

- Game logic tightly coupled to Steamworks SDK without abstraction for other storefronts.
- Achievement unlock logic scattered across gameplay code.
- Matchmaking state mixed with game session logic.
- Steam certification requirements discovered late in development.
- Save data format tied to Steam cloud save APIs.

## Verification

- Game logic can be tested without Steamworks SDK calls.
- Achievement and leaderboard operations are centralized.
- Offline mode behavior is explicitly designed.
