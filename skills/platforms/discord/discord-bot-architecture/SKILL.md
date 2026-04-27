---
name: discord-bot-architecture
description: Use when reviewing or designing Discord bot architecture, including slash commands, message components, modals, gateway intents, voice connections, and Discord API constraints.
---

# Discord Bot Architecture

## Knowledge To Use

- `knowledge/platform/communication-platforms/`
- `knowledge/languages/javascript/`
- `knowledge/languages/python/`
- `knowledge/api/`

## Workflow

1. Identify bot scenarios: slash commands, message components (buttons, select menus), modals, gateway events, voice channel connections, and webhook integrations.
2. Map Discord platform contracts: application commands, interaction webhooks, gateway intents, rate limits (global, per-route, per-guild), and sharding requirements.
3. Check whether command handling, event processing, permission checks, or message formatting are mixed with domain workflow logic.
4. Review platform constraints: gateway intent requirements, rate limit tiers, sharding for large bots, interaction timeout (3-second window), and ephemeral message patterns.
5. Recommend command handler, event router, component handler, and gateway connection boundaries.
6. Verify with Discord developer portal, command testing, rate limit simulation, and gateway reconnect scenarios.

## Output Format

```markdown
Discord bot architecture:
- Bot scenarios:
- Platform coupling:
- Proposed boundaries:
- Rate-limit/sharding concerns:
- Verification:
```
