# API Contract Design

## Use When

- Designing or reviewing REST, RPC, GraphQL, events, or internal service APIs.

## Core Idea

An API is a boundary contract. It should express caller needs without leaking internal persistence, framework, or temporary implementation details.

## Agent Heuristics

- Identify consumers and compatibility needs.
- Keep request and response names domain-oriented.
- Avoid exposing database table shapes as API contracts by default.
- Include validation, errors, pagination, and idempotency in the design.
- Prefer additive changes for backwards compatibility.

## Verification

- Existing consumers can continue working.
- Errors and edge cases have predictable responses.
- The contract can evolve without broad rewrites.

