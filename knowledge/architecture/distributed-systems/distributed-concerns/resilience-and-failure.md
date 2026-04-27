# Resilience And Failure

## Project Fit

Use this card for systems with network calls, queues, external vendors, distributed workflows, or managed runtime platforms.

## Use When

- Reviewing retries, timeouts, circuit breakers, fallbacks, idempotency, and partial failure.
- A workflow crosses process, service, or data-store boundaries.

## Avoid When

- Do not add complex resilience patterns before there is a failure mode to protect.

## Core Idea

Distributed systems fail partially. Architecture should make failure modes explicit and bounded.

## Heuristics

- Set timeouts for remote calls.
- Make retries idempotent.
- Define fallback behavior and user-visible degradation.
- Avoid unbounded synchronous chains.
- Use queues when buffering and retry are more important than immediate response.

## Verification

- Failure of one dependency has known behavior.
- Retries do not duplicate business effects.
- Timeouts and alerts match business impact.
