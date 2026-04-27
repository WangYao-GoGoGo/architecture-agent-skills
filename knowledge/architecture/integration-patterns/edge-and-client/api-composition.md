# API Composition

## Project Fit

API composition fits systems where a client-facing endpoint needs to combine data from multiple backend sources.

## Use When

- A screen or API response needs data owned by multiple services.
- The composition layer can manage latency, partial failure, and response shape.
- Backend services should keep their own ownership boundaries.

## Avoid When

- Composition hides business rules that belong to a domain service.
- Fan-out latency and partial failure are not acceptable.
- One backend owner could provide the data more simply.

## Core Idea

An API composition layer calls multiple services and assembles a response for a client or use case.

## Fits Best With

- BFFs, API gateways with light aggregation, GraphQL resolvers, read APIs over microservices.

## Verification

- Fan-out calls have timeouts and failure behavior.
- Response shape matches client needs.
- Composition does not mutate or own source-of-truth data.
