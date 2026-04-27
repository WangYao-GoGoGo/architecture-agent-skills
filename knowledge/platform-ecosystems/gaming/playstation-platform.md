# PlayStation Platform Architecture

## Heuristics

- Treat Sony NP (Network Platform) SDK initialization, authentication, trophies, leaderboards, cloud saves, matchmaking, and party/voice chat as platform contracts.
- Keep game logic, trophy tracking, leaderboard submission, and save data management separate from Sony SDK calls.
- Design for offline mode, PSN service outages, TRC (Technical Requirements Checklist) certification, and SDK version changes.
- Separate platform-specific adapters from cross-platform game engine code.
- Design for PlayStation's specific memory constraints, GPU access patterns, and controller features.

## Common Risks

- Game logic tightly coupled to Sony SDK without abstraction for cross-platform ports.
- Trophy unlock logic scattered across gameplay code.
- Matchmaking state mixed with game session logic.
- TRC certification requirements discovered late in development.
- Save data format tied to PlayStation-specific cloud save APIs.

## Verification

- Game logic can be tested without Sony SDK calls.
- Trophy and leaderboard operations are centralized.
- Offline mode behavior is explicitly designed.
