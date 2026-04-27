# Error Contracts

## Use When

- Reviewing API response shape, validation errors, domain errors, retries, and client behavior.

## Core Idea

Errors are part of the API. A consistent error contract makes clients simpler and safer.

## Agent Heuristics

- Separate validation, authentication, authorization, conflict, rate limit, and server errors.
- Include stable machine-readable codes.
- Keep human messages helpful but not relied on for logic.
- Avoid leaking stack traces, SQL details, or internal service names.
- Include retry guidance when relevant.

## Verification

- Clients can handle errors programmatically.
- Sensitive implementation details are not exposed.
- Logs still contain enough internal context for debugging.

