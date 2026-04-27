# Gaming Platform Ecosystem Knowledge

Gaming platforms include console SDKs, storefronts, online services, matchmaking, achievements, leaderboards, cloud saves, and certification processes that are partly platform-owned.

Examples include Steam (Steamworks), PlayStation (Sony NP), Xbox (Xbox Live), Nintendo (NintendoSDK), and Epic Games (EOS).

## Heuristics

- Treat SDK initialization, authentication, online service calls, achievement/trophy unlocks, matchmaking sessions, and save data as platform contracts.
- Keep game logic, achievement tracking, leaderboard submission, and matchmaking state separate from platform SDK calls.
- Design for offline mode, platform service outages, certification requirements, and SDK version changes.
- Separate platform-specific adapters from cross-platform game engine code.

## Common Risks

- Game logic tightly coupled to a single platform SDK without abstraction for cross-platform ports.
- Achievement/trophy unlock logic scattered across gameplay code.
- Matchmaking state mixed with game session logic.
- Certification requirements discovered late in development.
- Save data format tied to platform-specific cloud save APIs.
