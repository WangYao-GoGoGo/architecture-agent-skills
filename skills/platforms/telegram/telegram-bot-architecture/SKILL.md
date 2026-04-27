---
name: telegram-bot-architecture
description: Use when reviewing or designing Telegram bot architecture, including bot commands, inline queries, callback queries, webhook updates, media handling, and Telegram Bot API constraints.
---

# Telegram Bot Architecture

## Knowledge To Use

- `knowledge/platform/communication-platforms/`
- `knowledge/languages/python/`
- `knowledge/languages/javascript/`
- `knowledge/api/`

## Workflow

1. Identify bot scenarios: command handling, inline queries, callback queries, keyboard markup, webhook updates, media/file handling, and chat member events.
2. Map Telegram Bot API contracts: update types, webhook configuration, message entities, inline query results, callback data, rate limits, and file download/upload.
3. Check whether command routing, conversation state, keyboard building, or media handling are mixed with domain workflow logic.
4. Review platform constraints: webhook vs polling tradeoffs, rate limits (30 messages/second per chat), message size limits, file size limits, and bot privacy mode.
5. Recommend update handler, conversation state machine, keyboard builder, and media service boundaries.
6. Verify with Telegram bot sandbox, webhook testing, rate limit scenarios, and conversation state transitions.

## Output Format

```markdown
Telegram bot architecture:
- Bot scenarios:
- Platform coupling:
- Proposed boundaries:
- Rate-limit/conversation concerns:
- Verification:
```
