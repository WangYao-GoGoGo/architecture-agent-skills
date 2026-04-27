# Distributed Monolith

## Project Fit

Distributed monolith is usually a warning card, not a target style. Use it to diagnose services that are distributed physically but coupled logically.

## Use When

- Reviewing a system with many services that must be deployed together.
- Services share databases, models, or release cycles.
- Network calls exist without real ownership boundaries.

## Avoid When

- Do not choose this as a desired architecture.
- Do not label every coupled service system this way unless coupling blocks independent change.

## Core Idea

A distributed monolith has the complexity of distributed systems without the autonomy benefits of microservices.

## Signals

- One change requires many coordinated service releases.
- Services cannot be tested independently.
- Database ownership is shared or unclear.
- Synchronous call chains are deep and fragile.

## Improvement Moves

- Clarify ownership and contracts.
- Collapse tightly coupled services back into a module if independence is not needed.
- Introduce compatibility and contract testing.
- Split shared databases by ownership only when migration is justified.

## Verification

- Fewer changes require synchronized deployment.
- Ownership boundaries become visible.
- Failure and latency paths are easier to reason about.
