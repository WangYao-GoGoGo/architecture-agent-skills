# PlayStation Platform Knowledge

## Use When

Reviewing or designing PlayStation platform integration, Sony NP SDK, or console architecture.

## Heuristics

- Treat Sony NP SDK initialization, authentication, trophies, leaderboards, cloud saves, and matchmaking as platform contracts.
- Keep game logic, trophy tracking, leaderboard submission, and save data management separate from Sony SDK calls.
- Design for offline mode, PSN service outages, TRC certification, and SDK version changes.
- Separate platform-specific adapters from cross-platform game engine code.

## Common Risks

- Game logic tightly coupled to Sony SDK without abstraction for cross-platform ports.
- Trophy unlock logic scattered across gameplay code.
- TRC certification requirements discovered late in development.
