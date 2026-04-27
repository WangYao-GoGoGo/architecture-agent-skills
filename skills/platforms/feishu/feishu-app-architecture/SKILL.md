---
name: feishu-app-architecture
description: Use when reviewing or designing Feishu/Lark app architecture, including bot commands, event subscriptions, card messages, app widgets, OAuth login, and Feishu platform constraints.
---

# Feishu/Lark App Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/communication-platforms/`
- `knowledge/languages/javascript/`
- `knowledge/languages/python/`
- `knowledge/api/`

## Workflow

1. Identify app scenarios: bot commands, event subscriptions (message, member, calendar, drive), interactive cards, app widgets, Feishu Login, and tenant-level permissions.
2. Map Feishu platform contracts: event types, card interaction payloads, message types, OAuth flow, token lifecycle, rate limits, and permission scopes.
3. Check whether event handling, card building, message formatting, or user mapping are mixed with domain workflow logic.
4. Review platform constraints: event retry behavior, token refresh, rate limits, app review requirements, and data residency considerations.
5. Recommend event handler, card builder, message formatter, and authentication adapter boundaries.
6. Verify with Feishu developer sandbox, event replay scenarios, card interaction testing, and permission scope validation.

## Output Format

```markdown
Feishu/Lark app architecture:
- App scenarios:
- Platform coupling:
- Proposed boundaries:
- Permission/data concerns:
- Verification:
```
