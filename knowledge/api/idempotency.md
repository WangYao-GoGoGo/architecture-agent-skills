# Idempotency

## Use When

- Designing create, payment, order, retry, webhook, job, or event-consumer workflows.

## Core Idea

Idempotent operations can be safely retried without creating duplicate side effects.

## Agent Heuristics

- Use idempotency keys for externally retried commands.
- Store operation result or deduplication state at the right consistency boundary.
- Make event consumers tolerant of duplicate delivery.
- Separate validation errors from already-processed results.

## Verification

- Repeating the same request does not duplicate business effects.
- Concurrent duplicate requests are handled safely.
- Retry behavior is documented.

