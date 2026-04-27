# Architecture Knowledge

Architecture cards describe larger structural styles, integration patterns, distributed system choices, and architecture governance practices.

## Structure

- `application-styles/`: in-process application structure such as layered, clean, hexagonal, MVC, and modular monolith.
- `distributed-systems/`: service styles, deployment styles, and distributed concerns such as boundaries, failure, and observability.
- `integration-patterns/`: messaging/events, consistency patterns, read/write models, and client-facing edge patterns.
- `decision-governance/`: ADRs, RFCs, fitness functions, review checklists, technical radar, and architecture principles.
- `migration-strategies/`: strategies for incrementally migrating existing code to a better architecture (strangler fig, branch by abstraction, parallel run, expand-contract, feature flags).

## Rule

Use these cards to help skills choose architecture shape from current constraints. Do not force a large architecture style onto a small codebase.
