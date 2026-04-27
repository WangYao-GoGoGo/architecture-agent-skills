# Hexagonal Architecture

## Use When

- Core application logic needs to be independent from delivery mechanisms and infrastructure.
- The same use case may be driven by API, CLI, jobs, events, or tests.

## Core Idea

The application core exposes ports. Adapters connect external systems to those ports.

## Common Ports

- Input ports: use cases invoked by controllers, jobs, or consumers.
- Output ports: persistence, external services, message publishing, cache access.

## Verification

- Core use cases can run in tests with fake adapters.
- External API changes are isolated to adapters.
