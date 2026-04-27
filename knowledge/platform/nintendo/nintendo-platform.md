# Nintendo Platform Architecture

## Heuristics

- Treat NintendoSDK initialization, authentication, achievements, leaderboards, cloud saves, and online services as platform contracts.
- Keep game logic, achievement tracking, leaderboard submission, and save data management separate from Nintendo SDK calls.
- Design for offline mode, Nintendo Network service outages, LotCheck (Nintendo certification) requirements, and SDK version changes.
- Separate platform-specific adapters from cross-platform game engine code.
- Design for Nintendo Switch's specific memory constraints, GPU access patterns, and Joy-Con features.

## Common Risks

- Game logic tightly coupled to Nintendo SDK without abstraction for cross-platform ports.
- Achievement unlock logic scattered across gameplay code.
- LotCheck certification requirements discovered late in development.
- Save data format tied to Nintendo cloud save APIs.
- Ignoring Nintendo Switch's unique hardware constraints (docked vs handheld, battery, thermal).

## Verification

- Game logic can be tested without Nintendo SDK calls.
- Achievement and leaderboard operations are centralized.
- Offline mode behavior is explicitly designed.
