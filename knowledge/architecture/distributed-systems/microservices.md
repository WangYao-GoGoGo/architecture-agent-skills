# Microservices

## Use When

- Teams need independent ownership, deployment, scaling, or technology choices.
- Business boundaries and data ownership are reasonably clear.

## Core Idea

Microservices split a system into independently deployable services that own behavior and data around business capabilities.

## Heuristics

- Split by ownership and business capability, not by technical layer.
- Prefer one service owning each write model.
- Make API, event, and data contracts explicit.
- Design for latency, partial failure, retries, observability, and deployment coordination.
- Consider modular monolith first if boundaries are unclear.

## Risks

- Distributed monolith: many services but tightly coupled releases.
- Shared database ownership.
- Too much synchronous call depth.
- Operational complexity exceeds team capacity.

