# Reactor Knowledge

## Heuristics

- Separate Flux/Mono composition, backpressure handling, schedulers, and error recovery.
- Keep reactive chains small enough to reason about.
- Treat subscription context, cancellation, and resource cleanup as architecture.
- Add proper error handling and fallback paths.

## Common Risks

- Blocking calls inside reactive chains.
- Backpressure not configured for fast producers.
- Subscription lifecycle not managed properly.
