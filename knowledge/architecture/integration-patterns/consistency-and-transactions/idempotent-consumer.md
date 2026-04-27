# Idempotent Consumer

## Project Fit

Idempotent consumer fits message, event, webhook, and queue processing where duplicate delivery can happen.

## Use When

- Consumers process messages from brokers, queues, webhooks, or outbox relays.
- The delivery guarantee is at-least-once.
- Retrying can duplicate side effects.

## Avoid When

- Duplicate processing is impossible by contract and verified, which is rare.
- The consumer is read-only and has no meaningful side effects.

## Core Idea

An idempotent consumer can process the same message more than once without duplicating business effects.

## Fits Best With

- Event-driven services, webhooks, queues, sagas, outbox consumers.

## Verification

- Message identity or business idempotency key is stored.
- Duplicate delivery returns the existing result or no-ops safely.
- Concurrent duplicates are handled safely.
