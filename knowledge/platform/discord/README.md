# Discord Platform Knowledge

## Use When

Reviewing or designing Discord bot architecture, interactions, or gateway integration.

## Heuristics

- Treat interaction events, gateway events, and REST API calls as platform contracts.
- Keep interaction token handling, rate limit management, and gateway reconnection at the integration edge.
- Separate command routing, domain workflow, message formatting (embeds, components), and delivery.
- Design for Discord's specific gateway intents and 3-second interaction response timeout.

## Common Risks

- Interaction handlers containing full business workflows.
- Gateway reconnection logic not handled.
- Embed and component format details leaking into domain services.
