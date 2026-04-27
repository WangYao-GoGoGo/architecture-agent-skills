# Discord Bot Architecture

## Heuristics

- Treat interaction events (slash commands, buttons, modals), gateway events, and REST API calls as platform contracts.
- Keep interaction token handling, rate limit management, gateway reconnection, and command registration at the integration edge.
- Separate command routing, domain workflow, message formatting (embeds, components), and delivery.
- Design for Discord's specific gateway intents, interaction response timeouts, and rate limits.
- Use Discord.js or similar SDKs behind adapters for testability.

## Common Risks

- Interaction handlers containing full business workflows.
- Gateway reconnection logic not handled, causing bot disconnection.
- Embed and component format details leaking into domain services.
- Ignoring Discord's 3-second interaction response timeout.
- Rate limit handling absent, causing silent command failures.

## Verification

- Interaction handlers respond within the 3-second window or use deferred responses.
- Gateway reconnection and resume logic is robust.
- Domain workflows can be tested without real Discord API calls.
