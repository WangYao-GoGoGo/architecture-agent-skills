# Microservices

## Project Fit

Microservices fit systems where independent ownership, deployment, scaling, or technology choices are worth the operational cost.

## Use When

- Teams need independent ownership, deployment, scaling, or technology choices.
- Business boundaries and data ownership are reasonably clear.
- Services can own their data and release independently.
- The organization can operate distributed systems reliably.

## Avoid When

- Boundaries are unclear and still changing quickly.
- The team cannot support observability, deployment automation, and failure handling.
- Services share one database and require synchronized releases.

## Core Idea

Microservices split a system into independently deployable services that own behavior and data around business capabilities.

## Fits Best With

- Multiple teams with clear domain ownership.
- Capabilities with different scaling or release needs.
- Systems where operational maturity exists or is being deliberately built.

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

## Verification

- Services can deploy independently.
- Each service owns a clear data boundary.
- Failure of one service has bounded impact.
- Observability shows request paths, events, errors, and latency.
 
