---
name: slack-app-architecture
description: Use when reviewing or designing Slack app architecture, including slash commands, event subscriptions, modals, Block Kit, OAuth installation, and Slack platform constraints.
---

# Slack App Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/communication-platforms/`
- `knowledge/languages/javascript/`
- `knowledge/languages/python/`
- `knowledge/api/`

## Workflow

1. Identify app scenarios: slash commands, event subscriptions, interactive components (buttons, modals, select menus), Block Kit messages, OAuth installation flow, and webhook integrations.
2. Map Slack platform contracts: request URL verification, event types, command parsing, interaction payloads, Block Kit composition, rate limits, and token scopes.
3. Check whether command handling, event routing, message formatting, or user mapping are mixed with domain workflow logic.
4. Review platform constraints: request URL verification, retry behavior, rate limits (per-workspace, per-app), token rotation, and Slack Connect considerations.
5. Recommend command handler, event router, Block Kit builder, and OAuth installation boundaries.
6. Verify with Slack app sandbox, command testing, event retry scenarios, and permission scope validation.

## Output Format

```markdown
Slack app architecture:
- App scenarios:
- Platform coupling:
- Proposed boundaries:
- Rate-limit/permission concerns:
- Verification:
```
