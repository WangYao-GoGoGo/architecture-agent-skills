# Epic Games Platform Architecture

## Heuristics

- Treat Epic Online Services (EOS) SDK initialization, authentication, achievements, leaderboards, cloud saves, matchmaking, and lobby as platform contracts.
- Keep game logic, achievement tracking, leaderboard submission, and save data management separate from EOS SDK calls.
- Design for offline mode, Epic service outages, and SDK version changes.
- Separate platform-specific adapters from cross-platform game engine code.
- Use EOS's cross-platform identity and overlay features for multi-storefront support.

## Common Risks

- Game logic tightly coupled to EOS SDK without abstraction for other storefronts.
- Achievement unlock logic scattered across gameplay code.
- Matchmaking and lobby state mixed with game session logic.
- Save data format tied to Epic cloud save APIs.
- Ignoring Epic's specific certification and store submission requirements.

## Verification

- Game logic can be tested without EOS SDK calls.
- Achievement and leaderboard operations are centralized.
- Offline mode behavior is explicitly designed.
