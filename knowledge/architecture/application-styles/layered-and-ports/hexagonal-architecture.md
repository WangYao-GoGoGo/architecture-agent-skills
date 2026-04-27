# Hexagonal Architecture

## Project Fit

Hexagonal architecture is language-neutral. It fits applications where the same core use cases interact with multiple outside systems through explicit ports and adapters.

## Use When

- Core application logic needs to be independent from delivery mechanisms and infrastructure.
- The same use case may be driven by API, CLI, jobs, events, or tests.
- External systems, vendors, databases, queues, or frameworks change independently from core policy.

## Avoid When

- There is only one simple caller and one stable infrastructure detail.
- Ports would mirror one concrete adapter with no substitution or boundary value.
- The team cannot identify the core use cases.

## Core Idea

The application core exposes ports. Adapters connect external systems to those ports.

## Fits Best With

- Backend services with external integrations.
- CLI plus API applications sharing the same use cases.
- Systems that need test doubles for persistence, messaging, payment, search, cache, or vendor APIs.

## Common Ports

- Input ports: use cases invoked by controllers, jobs, or consumers.
- Output ports: persistence, external services, message publishing, cache access.

## Adaptation Notes

- Backend: controllers, jobs, and consumers are input adapters.
- Frontend: UI events can drive use-case functions; API clients are output adapters.
- Shell/operations: commands and environment are adapters around a small core workflow.
- Data pipeline: sources and sinks are adapters around transformation logic.

## Verification

- Core use cases can run in tests with fake adapters.
- External API changes are isolated to adapters.
- Ports are named around core needs, not vendor APIs.
