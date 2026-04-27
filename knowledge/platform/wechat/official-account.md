# WeChat Official Account Architecture

## Heuristics

- Treat message callbacks, menu events, OAuth redirects, template messages, and customer-service messages as API contracts.
- Keep signature verification, token refresh, deduplication, and retry handling at the integration edge.
- Separate conversation routing, domain workflow, persistence, and outbound message formatting.
- Make account type and permission constraints visible in the design.

## Common Risks

- Callback handlers containing the full business workflow.
- Access token refresh implemented independently in many modules.
- Duplicate platform events causing repeated side effects.
- Message format details leaking into domain services.

## Verification

- Callback processing is idempotent.
- Token lifecycle and retry behavior are centralized.
- Domain workflows can be tested without real WeChat callbacks.
