# Saga

## Use When

- A business workflow spans multiple services or data stores and cannot use one transaction.

## Core Idea

A saga coordinates a sequence of local transactions with compensating actions or state transitions.

## Heuristics

- Define each local transaction and compensation.
- Make retries and idempotency explicit.
- Choose orchestration when a central workflow owner is helpful.
- Choose choreography when services can react independently without hidden coupling.

## Risks

- Compensation may not truly undo business effects.
- Workflow state becomes hard to observe.
- Duplicate messages or partial failures break assumptions.

